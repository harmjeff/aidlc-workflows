"""Claude Code SDK adapter — drives AIDLC workflows via Anthropic SDK with Bedrock.

Unlike the subprocess-based ClaudeCodeAdapter (which runs ``claude -p`` as a
one-shot process), this adapter uses ``anthropic.AnthropicBedrock`` to drive
the executor turn-by-turn.  It intercepts ``handoff_to_simulator`` tool calls
and injects Human Simulator responses using the same system prompt as the
Strands two-agent swarm in ``packages/execution``.

This faithfully recreates the interactive executor↔simulator loop that the CLI
subprocess approach cannot support.
"""

from __future__ import annotations

import json
import logging
import os
import shlex
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path

import anthropic
import boto3

from cli_harness.adapter import AdapterConfig, AdapterResult, CLIAdapter
from cli_harness.normalizer import normalize_output

# Import system prompts directly from the execution package so they stay in sync.
_EXEC_SRC = Path(__file__).resolve().parents[6] / "execution" / "src"
import sys as _sys
_sys.path.insert(0, str(_EXEC_SRC))
from aidlc_runner.agents.executor import EXECUTOR_SYSTEM_PROMPT  # noqa: E402
from aidlc_runner.agents.simulator import SIMULATOR_SYSTEM_PROMPT_TEMPLATE  # noqa: E402

logger = logging.getLogger(__name__)

_MAX_ITERATIONS = 300
_MAX_OUTPUT_CHARS = 50_000


def _log(msg: str) -> None:
    print(f"  [claude-sdk] {msg}", file=_sys.stderr, flush=True)


# ── Tool schemas ──────────────────────────────────────────────────────────────

_TOOL_READ_FILE: dict = {
    "name": "read_file",
    "description": "Read the contents of a file in the run folder.",
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "File path relative to the run folder (e.g. 'aidlc-docs/aidlc-state.md').",
            }
        },
        "required": ["path"],
    },
}

_TOOL_WRITE_FILE: dict = {
    "name": "write_file",
    "description": "Write content to a file in the run folder. Creates parent directories if needed.",
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "Relative to run folder (e.g. 'aidlc-docs/inception/requirements.md').",
            },
            "content": {
                "type": "string",
                "description": "The text content to write to the file.",
            },
        },
        "required": ["path", "content"],
    },
}

_TOOL_LIST_FILES: dict = {
    "name": "list_files",
    "description": "List files and directories within a path in the run folder.",
    "input_schema": {
        "type": "object",
        "properties": {
            "directory": {
                "type": "string",
                "description": "Directory path relative to the run folder. Defaults to '.'.",
                "default": ".",
            }
        },
        "required": [],
    },
}

_TOOL_LOAD_RULE: dict = {
    "name": "load_rule",
    "description": (
        "Load an AIDLC rule file by path. "
        "Use this to read AIDLC workflow rules as you progress through stages."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "rule_path": {
                "type": "string",
                "description": (
                    "Path relative to the rules directory. Examples: "
                    "'core-workflow', 'common/process-overview.md', "
                    "'inception/requirements-analysis.md', 'construction/code-generation.md'."
                ),
            }
        },
        "required": ["rule_path"],
    },
}

_TOOL_RUN_COMMAND: dict = {
    "name": "run_command",
    "description": (
        "Execute a shell command in the run folder. "
        "Use during Build and Test to install dependencies, run tests, and fix issues."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "command": {
                "type": "string",
                "description": "The shell command to execute.",
            },
            "working_directory": {
                "type": "string",
                "description": "Directory relative to the run folder to run in (default: workspace/).",
                "default": "workspace",
            },
        },
        "required": ["command"],
    },
}

_TOOL_HANDOFF_TO_SIMULATOR: dict = {
    "name": "handoff_to_simulator",
    "description": (
        "Hand off to the Human Simulator agent for answers, approvals, or reviews. "
        "The simulator will respond and hand control back to you."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "message": {
                "type": "string",
                "description": (
                    "Message to the simulator — describe what input you need "
                    "(answer questions / approve document / review) and include the "
                    "file path they need to read."
                ),
            }
        },
        "required": ["message"],
    },
}

_EXECUTOR_TOOLS = [
    _TOOL_READ_FILE,
    _TOOL_WRITE_FILE,
    _TOOL_LIST_FILES,
    _TOOL_LOAD_RULE,
    _TOOL_RUN_COMMAND,
    _TOOL_HANDOFF_TO_SIMULATOR,
]

_SIMULATOR_TOOLS = [
    _TOOL_READ_FILE,
    _TOOL_WRITE_FILE,
    _TOOL_LIST_FILES,
]


# ── Token accumulator ─────────────────────────────────────────────────────────

@dataclass
class _TokenBucket:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0

    def add(self, usage: anthropic.types.Usage) -> None:
        self.input_tokens += getattr(usage, "input_tokens", 0)
        self.output_tokens += getattr(usage, "output_tokens", 0)
        self.cache_read_tokens += getattr(usage, "cache_read_input_tokens", 0)
        self.cache_write_tokens += getattr(usage, "cache_creation_input_tokens", 0)

    @property
    def total(self) -> int:
        return self.input_tokens + self.output_tokens + self.cache_read_tokens + self.cache_write_tokens


@dataclass
class _UsageTracker:
    executor: _TokenBucket = field(default_factory=_TokenBucket)
    simulator: _TokenBucket = field(default_factory=_TokenBucket)
    handoff_count: int = 0

    def to_dict(self) -> dict:
        e, s = self.executor, self.simulator
        return {
            "input_tokens": e.input_tokens + s.input_tokens,
            "output_tokens": e.output_tokens + s.output_tokens,
            "total_tokens": e.total + s.total,
            "cache_read_tokens": e.cache_read_tokens + s.cache_read_tokens,
            "cache_write_tokens": e.cache_write_tokens + s.cache_write_tokens,
            "executor_input_tokens": e.input_tokens,
            "executor_output_tokens": e.output_tokens,
            "executor_total_tokens": e.total,
            "simulator_input_tokens": s.input_tokens,
            "simulator_output_tokens": s.output_tokens,
            "simulator_total_tokens": s.total,
            "handoffs": self.handoff_count,
            "num_turns": self.handoff_count,
        }


# ── Tool execution ────────────────────────────────────────────────────────────

def _resolve_safe(base: Path, relative: str) -> Path:
    resolved = (base / relative).resolve()
    if not str(resolved).startswith(str(base.resolve())):
        raise ValueError(f"Path traversal denied: {relative}")
    return resolved


def _exec_tool(name: str, tool_input: dict, run_folder: Path, rules_dir: Path) -> str:
    """Execute a tool call and return its string result."""
    try:
        if name == "read_file":
            path = tool_input["path"]
            target = _resolve_safe(run_folder, path)
            if not target.exists():
                return f"Error: File not found: {path}"
            if not target.is_file():
                return f"Error: Not a file: {path}"
            return target.read_text(encoding="utf-8")

        elif name == "write_file":
            path, content = tool_input["path"], tool_input.get("content", "")
            target = _resolve_safe(run_folder, path)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            return f"Written: {path} ({len(content)} chars)"

        elif name == "list_files":
            directory = tool_input.get("directory", ".")
            target = _resolve_safe(run_folder, directory)
            if not target.exists():
                return f"Error: Directory not found: {directory}"
            if not target.is_dir():
                return f"Error: Not a directory: {directory}"
            entries = sorted(target.iterdir())
            lines = [
                f"  {e.relative_to(run_folder)}{'/' if e.is_dir() else ''}"
                for e in entries
            ]
            return "\n".join(lines) if lines else f"(empty: {directory})"

        elif name == "load_rule":
            rule_path = tool_input["rule_path"]
            if rule_path in ("core-workflow", "core-workflow.md"):
                target = rules_dir / "aws-aidlc-rules" / "core-workflow.md"
            else:
                target = rules_dir / "aws-aidlc-rule-details" / rule_path
                if not target.suffix:
                    target = target.with_suffix(".md")
            resolved = target.resolve()
            if not str(resolved).startswith(str(rules_dir.resolve())):
                return f"Error: Path traversal denied: {rule_path}"
            if not resolved.exists():
                return f"Error: Rule not found: {rule_path}"
            return resolved.read_text(encoding="utf-8")

        elif name == "run_command":
            command = tool_input["command"]
            working_dir = tool_input.get("working_directory", "workspace")
            cwd = _resolve_safe(run_folder, working_dir)
            if not cwd.is_dir():
                return f"[error: working directory not found: {working_dir}]"
            env = {
                "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                "HOME": str(run_folder),
                "LANG": os.environ.get("LANG", "C.UTF-8"),
                "TERM": "dumb",
            }
            for var in ("UV_CACHE_DIR", "UV_PYTHON", "NODE_PATH", "NPM_CONFIG_CACHE",
                        "VIRTUAL_ENV", "PYTHONPATH"):
                if (val := os.environ.get(var)):
                    env[var] = val
            try:
                # nosec B603 - shlex.split with shell=False, path validated via _resolve_safe
                # nosemgrep: dangerous-subprocess-use-audit
                result = subprocess.run(
                    shlex.split(command),
                    shell=False,
                    cwd=str(cwd),
                    capture_output=True,
                    text=True,
                    timeout=120,
                    env=env,
                )
                output = result.stdout + result.stderr
                if len(output) > _MAX_OUTPUT_CHARS:
                    output = output[:_MAX_OUTPUT_CHARS] + "\n... (output truncated)"
                return f"[exit code: {result.returncode}]\n{output}"
            except subprocess.TimeoutExpired:
                return "[error: command timed out after 120s]"
            except OSError as e:
                return f"[error: {e}]"

        else:
            return f"[error: unknown tool: {name}]"

    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        logger.exception("Tool %r failed", name)
        return f"[error: {e}]"


# ── Agent loops ───────────────────────────────────────────────────────────────

def _run_simulator_turn(
    client: anthropic.AnthropicBedrock,
    simulator_model: str,
    simulator_system: str,
    handoff_message: str,
    run_folder: Path,
    rules_dir: Path,
    usage: _UsageTracker,
) -> str:
    """Run one simulator turn and return the final text response."""
    messages: list[dict] = [{"role": "user", "content": handoff_message}]
    _log(f"  → simulator turn (handoff #{usage.handoff_count + 1})")

    for _ in range(50):
        response = client.messages.create(
            model=simulator_model,
            max_tokens=8192,
            system=simulator_system,
            tools=_SIMULATOR_TOOLS,
            messages=messages,
        )
        usage.simulator.add(response.usage)

        tool_uses = [b for b in response.content if b.type == "tool_use"]
        text_blocks = [b for b in response.content if b.type == "text"]

        if not tool_uses:
            # Simulator finished — collect its text response
            return "\n".join(b.text for b in text_blocks).strip() or "(no response)"

        # Execute simulator tool calls (file ops only)
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for tu in tool_uses:
            result_text = _exec_tool(tu.name, tu.input, run_folder, rules_dir)
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": tu.id,
                "content": result_text,
            })
        messages.append({"role": "user", "content": tool_results})

    return "[error: simulator exceeded max iterations]"


def _run_executor_loop(
    client: anthropic.AnthropicBedrock,
    executor_model: str,
    simulator_model: str,
    simulator_system: str,
    initial_prompt: str,
    run_folder: Path,
    rules_dir: Path,
    usage: _UsageTracker,
) -> None:
    """Run the executor agent loop, injecting simulator turns on handoff calls."""
    messages: list[dict] = [{"role": "user", "content": initial_prompt}]

    for iteration in range(_MAX_ITERATIONS):
        response = client.messages.create(
            model=executor_model,
            max_tokens=8192,
            system=EXECUTOR_SYSTEM_PROMPT,
            tools=_EXECUTOR_TOOLS,
            messages=messages,
        )
        usage.executor.add(response.usage)

        tool_uses = [b for b in response.content if b.type == "tool_use"]

        if response.stop_reason == "end_turn" and not tool_uses:
            _log(f"Executor finished after {iteration + 1} iterations")
            return

        messages.append({"role": "assistant", "content": response.content})
        tool_results = []

        for tu in tool_uses:
            if tu.name == "handoff_to_simulator":
                usage.handoff_count += 1
                sim_response = _run_simulator_turn(
                    client=client,
                    simulator_model=simulator_model,
                    simulator_system=simulator_system,
                    handoff_message=tu.input.get("message", ""),
                    run_folder=run_folder,
                    rules_dir=rules_dir,
                    usage=usage,
                )
                _log(f"  ← simulator responded ({len(sim_response)} chars)")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tu.id,
                    "content": sim_response,
                })
            else:
                result_text = _exec_tool(tu.name, tu.input, run_folder, rules_dir)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tu.id,
                    "content": result_text,
                })

        messages.append({"role": "user", "content": tool_results})

    _log(f"[WARN] Executor hit max iterations ({_MAX_ITERATIONS})")


# ── Adapter ───────────────────────────────────────────────────────────────────

class ClaudeCodeSDKAdapter(CLIAdapter):
    """Adapter that drives AIDLC workflows via the Anthropic SDK with an embedded simulator.

    Uses ``anthropic.AnthropicBedrock`` to run an executor agent that can
    interactively hand off to a Human Simulator agent mid-workflow, matching
    the two-agent Strands Swarm in ``packages/execution``.
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    @property
    def name(self) -> str:
        return "claude-code-sdk"

    def check_prerequisites(self) -> tuple[bool, str]:
        """Verify AWS credentials are resolvable via boto3."""
        try:
            session = boto3.Session()
            creds = session.get_credentials()
            if creds is None:
                return False, "No AWS credentials found. Configure via profile, env vars, or IAM role."
            return True, "AWS credentials available"
        except Exception as e:
            return False, f"AWS credential check failed: {e}"

    def run(self, config: AdapterConfig) -> AdapterResult:
        """Execute the full AIDLC workflow through the Anthropic SDK with an embedded simulator."""
        ok, msg = self.check_prerequisites()
        if not ok:
            return AdapterResult(success=False, output_dir=config.output_dir, error=msg)

        start_time = time.monotonic()
        config.output_dir.mkdir(parents=True, exist_ok=True)
        workspace = config.output_dir / "workspace"
        workspace.mkdir(exist_ok=True)
        _log(f"Run folder: {config.output_dir}")

        import shutil

        try:
            # Copy input documents into the run folder (matching execution runner layout)
            shutil.copy2(config.vision_path, config.output_dir / "vision.md")
            vision_content = config.vision_path.read_text(encoding="utf-8")

            tech_env_content: str | None = None
            if config.tech_env_path and config.tech_env_path.is_file():
                shutil.copy2(config.tech_env_path, config.output_dir / "tech-env.md")
                tech_env_content = config.tech_env_path.read_text(encoding="utf-8")

            # Also place vision.md in workspace for the executor to find
            shutil.copy2(config.vision_path, workspace / "vision.md")
            if tech_env_content:
                shutil.copy2(config.tech_env_path, workspace / "tech-env.md")

            # rules_path is already set up by the orchestrator (output_dir/aidlc-rules);
            # use it directly rather than copying again.
            rules_dir = config.rules_path

            # Build simulator system prompt
            if tech_env_content:
                tech_env_section = (
                    "\n## The technical environment\n\n"
                    "The following is the technical environment document that defines HOW "
                    "the project must be built — languages, frameworks, cloud services, "
                    "security controls, testing standards, and prohibited technologies. "
                    "Use this as a binding reference when answering technical questions "
                    "and reviewing designs and code:\n\n"
                    "---\n"
                    f"{tech_env_content}\n"
                    "---\n"
                )
            else:
                tech_env_section = ""
            simulator_system = SIMULATOR_SYSTEM_PROMPT_TEMPLATE.format(
                vision_content=vision_content,
                tech_env_section=tech_env_section,
            )

            # Build initial prompt (mirrors runner.py)
            initial_prompt = (
                "Begin the AIDLC workflow and execute it TO COMPLETION through ALL phases. "
                "The project vision is available at vision.md in the run folder. "
            )
            if tech_env_content:
                initial_prompt += (
                    "The technical environment document is available at tech-env.md "
                    "in the run folder. It defines the required languages, frameworks, "
                    "cloud services, security controls, testing standards, and prohibited "
                    "technologies. Follow it as a binding reference during all Construction stages. "
                )
            initial_prompt += (
                "Start by loading the core workflow rules and the process overview, then "
                "execute every stage of the Inception phase followed by every stage of the "
                "Construction phase. The workspace directory is 'workspace/' (currently empty — "
                "this is a greenfield project). You MUST generate all application code in "
                "workspace/ before the workflow is complete. Do NOT stop after requirements — "
                "continue through application design, code generation, and build-and-test."
            )

            # Resolve models
            executor_model = config.model or "global.anthropic.claude-opus-4-6-v1"
            simulator_model = getattr(config, "simulator_model", None) or executor_model

            # Build Bedrock client
            session_kwargs: dict = {}
            if config.aws_profile:
                session_kwargs["profile_name"] = config.aws_profile
            aws_region = getattr(config, "aws_region", None) or os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
            boto_session = boto3.Session(**session_kwargs)
            frozen = boto_session.get_credentials().get_frozen_credentials()
            client = anthropic.AnthropicBedrock(
                aws_access_key=frozen.access_key,
                aws_secret_key=frozen.secret_key,
                aws_session_token=frozen.token,
                aws_region=aws_region,
            )

            _log(f"Executor model: {executor_model}")
            _log(f"Simulator model: {simulator_model}")

            # Run the executor↔simulator loop
            usage = _UsageTracker()
            _run_executor_loop(
                client=client,
                executor_model=executor_model,
                simulator_model=simulator_model,
                simulator_system=simulator_system,
                initial_prompt=initial_prompt,
                run_folder=config.output_dir,
                rules_dir=rules_dir,
                usage=usage,
            )

            elapsed_seconds = time.monotonic() - start_time
            usage_extra = usage.to_dict()
            usage_extra["duration_ms"] = int(elapsed_seconds * 1000)
            usage_extra["model"] = executor_model

            _log(
                f"Completed in {elapsed_seconds:.0f}s — "
                f"{usage_extra['total_tokens']:,} total tokens, "
                f"{usage_extra['handoffs']} handoffs"
            )

            # Move aidlc-docs from workspace/ up to run_folder/ if the executor placed them there
            src_docs = workspace / "aidlc-docs"
            dst_docs = config.output_dir / "aidlc-docs"
            if src_docs.is_dir() and not dst_docs.exists():
                shutil.move(str(src_docs), str(dst_docs))

            # Write run metadata
            normalize_output(
                source_dir=workspace,
                output_dir=config.output_dir,
                adapter_name=self.name,
                model_hint=executor_model,
                elapsed_seconds=elapsed_seconds,
                token_usage=usage_extra,
            )

            has_docs = dst_docs.is_dir() and any(dst_docs.iterdir())
            return AdapterResult(
                success=has_docs,
                output_dir=config.output_dir,
                aidlc_docs_dir=dst_docs if has_docs else None,
                workspace_dir=workspace,
                elapsed_seconds=elapsed_seconds,
                extra=usage_extra,
                error=None if has_docs else "No aidlc-docs produced",
            )

        except Exception as exc:
            elapsed_seconds = time.monotonic() - start_time
            logger.exception("claude-code-sdk adapter run failed")
            return AdapterResult(
                success=False,
                output_dir=config.output_dir,
                workspace_dir=workspace,
                error=f"claude-code-sdk adapter error: {exc}",
                elapsed_seconds=elapsed_seconds,
            )


def _setup_rules(rules_dir: Path, rules_path: Path) -> None:
    """Copy or link the AIDLC rules into the run folder."""
    import shutil
    rules_dir.mkdir(parents=True, exist_ok=True)
    if rules_path.is_dir():
        for rule_file in sorted(rules_path.rglob("*.md")):
            rel = rule_file.relative_to(rules_path)
            dst = rules_dir / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(rule_file, dst)
        _log(f"Copied AIDLC rules ({sum(1 for _ in rules_dir.rglob('*.md'))} files)")
    else:
        shutil.copy2(rules_path, rules_dir / rules_path.name)
        _log(f"Copied AIDLC rules file: {rules_path.name}")
