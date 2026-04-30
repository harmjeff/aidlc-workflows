"""Kiro CLI adapter — drives AIDLC workflows via kiro-cli subprocess.

Uses ``kiro-cli chat`` with ``--no-interactive`` and ``--trust-all-tools``
flags for fully headless execution.

AIDLC rules are injected through Kiro's steering-file mechanism by writing
them to ``.kiro/steering/aidlc-rules.md`` inside the workspace.
"""

from __future__ import annotations

import logging
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

from cli_harness.adapter import AdapterConfig, AdapterResult, CLIAdapter
from cli_harness.normalizer import normalize_output
from cli_harness.prompt_template import render_prompt
from cli_harness.simulator import HumanSimulator

import sys as _sys
_EXEC_SRC = Path(__file__).resolve().parents[6] / "execution" / "src"
if str(_EXEC_SRC) not in _sys.path:
    _sys.path.insert(0, str(_EXEC_SRC))
from aidlc_runner.post_run import run_post_evaluation  # noqa: E402
from aidlc_runner.config import ExecutionConfig, SandboxConfig, RunnerConfig  # noqa: E402

_SHARED_SRC = Path(__file__).resolve().parents[6] / "shared" / "src"
if str(_SHARED_SRC) not in _sys.path:
    _sys.path.insert(0, str(_SHARED_SRC))
from shared.sandbox import _get_container_cli  # noqa: E402

logger = logging.getLogger(__name__)

_KIRO_CLI = "kiro-cli"

# Matches ANSI escape sequences: CSI sequences (\x1b[...X), OSC sequences (\x1b]...\x07),
# and simple two-byte escapes (\x1b followed by one char).
_ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]|\x1b\][^\x07]*\x07|\x1b.")


def _strip_ansi(text: str) -> str:
    """Remove ANSI escape sequences from text."""
    return _ANSI_RE.sub("", text)


def _log(msg: str) -> None:
    """Print a progress message to stderr."""
    print(f"  [kiro-cli] {msg}", file=sys.stderr, flush=True)


class KiroCLIAdapter(CLIAdapter):
    """Adapter for kiro-cli.

    Uses ``kiro-cli chat --no-interactive --trust-all-tools`` for headless
    execution via subprocess.
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    @property
    def name(self) -> str:
        return "kiro-cli"

    def check_prerequisites(self) -> tuple[bool, str]:
        """Verify that ``kiro-cli`` is on PATH."""
        if not shutil.which(_KIRO_CLI):
            return False, (
                f"'{_KIRO_CLI}' not found in PATH. "
                "Install the Kiro CLI first (https://kiro.dev)."
            )
        return True, f"Kiro CLI ('{_KIRO_CLI}') found"

    def run(self, config: AdapterConfig) -> AdapterResult:
        """Execute the full AIDLC workflow through kiro-cli.

        Runs directly in ``<output_dir>/workspace/`` — no temp dir or copy step.
        """
        ok, msg = self.check_prerequisites()
        if not ok:
            return AdapterResult(
                success=False,
                output_dir=config.output_dir,
                error=f"Prerequisites not met: {msg}",
            )

        start_time = time.monotonic()

        # Work directly in the final output location
        config.output_dir.mkdir(parents=True, exist_ok=True)
        workspace = config.output_dir / "workspace"
        workspace.mkdir(exist_ok=True)
        _log(f"Workspace: {workspace}")

        try:
            # Copy input documents
            shutil.copy2(config.vision_path, workspace / "vision.md")
            _log(f"Copied vision: {config.vision_path}")
            if config.tech_env_path and config.tech_env_path.is_file():
                shutil.copy2(config.tech_env_path, workspace / "tech-env.md")
                _log(f"Copied tech-env: {config.tech_env_path}")

            # Inject AIDLC rules via steering files
            steering_dir = workspace / ".kiro" / "steering"
            steering_dir.mkdir(parents=True, exist_ok=True)

            rules_path = config.rules_path
            if rules_path.is_dir():
                parts = []
                for rule_file in sorted(rules_path.rglob("*.md")):
                    parts.append(rule_file.read_text(encoding="utf-8"))
                rules_content = "\n\n".join(parts)
            else:
                rules_content = rules_path.read_text(encoding="utf-8")

            (steering_dir / "aidlc-rules.md").write_text(
                rules_content, encoding="utf-8"
            )
            _log(f"Injected AIDLC rules ({len(rules_content)} chars)")

            # Build executor prompt — instructs kiro to pause at review gates
            # so the human simulator can respond rather than self-approving.
            prompt = config.prompt_template or render_prompt(
                openapi_content=config.openapi_content,
                with_simulator=True,
            )

            # Build the human simulator (Bedrock) for review gates
            vision_content = config.vision_path.read_text(encoding="utf-8")
            tech_env_content = (
                config.tech_env_path.read_text(encoding="utf-8")
                if config.tech_env_path and config.tech_env_path.is_file()
                else None
            )
            simulator_model = getattr(config, "simulator_model", None) or config.model or "global.anthropic.claude-opus-4-6-v1"
            aws_region = getattr(config, "aws_region", None) or "us-east-1"
            simulator = HumanSimulator.from_adapter_config(
                run_folder=config.output_dir,
                vision_content=vision_content,
                tech_env_content=tech_env_content,
                openapi_content=config.openapi_content,
                aws_profile=config.aws_profile,
                aws_region=aws_region,
                model=simulator_model,
            )
            _log(f"Simulator model: {simulator_model}")

            # Run kiro interactively with stdin piping so the human simulator
            # can respond at each gate instead of kiro self-approving.
            # One persistent kiro process; we write prompts to stdin and read
            # output until kiro goes idle (gate detected via output idle timeout).
            cmd = [_KIRO_CLI, "chat", "--trust-all-tools"]
            if config.model:
                cmd += ["--model", config.model]

            log_path = config.output_dir / "kiro-session.log"
            _log(f"Session log: {log_path}")

            gate_count = 0
            max_gates = 20
            total_rc = 0
            # Idle timeout: if kiro produces no output for this many seconds,
            # treat it as a gate (pausing for user input).
            idle_timeout_s = 12.0

            import queue
            import threading

            with open(log_path, "w", encoding="utf-8") as log_file:
                # nosec B603 - Executing user's Kiro CLI with validated configuration
                # nosemgrep: dangerous-subprocess-use-audit
                process = subprocess.Popen(
                    cmd,
                    cwd=str(workspace),
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    bufsize=0,  # unbuffered bytes — avoids macOS pipe buffering deadlock
                )

                line_queue: queue.Queue = queue.Queue()

                def _reader_thread() -> None:
                    """Push decoded lines onto line_queue; sentinel None on EOF."""
                    while True:
                        chunk = process.stdout.read(4096)
                        if not chunk:
                            line_queue.put(None)
                            break
                        text = chunk.decode("utf-8", errors="replace")
                        line_queue.put(text)

                reader = threading.Thread(target=_reader_thread, daemon=True)
                reader.start()

                def _is_complete() -> bool:
                    """Return True if construction docs exist in workspace."""
                    construction = workspace / "aidlc-docs" / "construction"
                    return construction.is_dir() and any(construction.rglob("*.md"))

                # Accumulate partial output into lines for clean printing
                _line_buf: list[str] = [""]
                _last_printed: list[str] = [""]

                _SKIP_PREFIXES = (
                    "⠀", "⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏",  # spinners
                    "⣴", "⣿", "⠿", "╭", "╰", "│",  # box-drawing / braille logo
                    "▸ Credits:", "Credits:",
                    "Model:", "Plan:", "All tools are", "Agents can",
                    "Learn more", "https://", "Did you know", "Jump into",
                    "Use /", "1.", "2.", "3.",  # help text
                )

                def _print_kiro_line(line: str) -> None:
                    """Print meaningful kiro output lines to stderr."""
                    s = line.strip()
                    if not s or len(s) < 8:
                        return
                    for pfx in _SKIP_PREFIXES:
                        if s.startswith(pfx):
                            return
                    # Skip lines that are pure ANSI remnants
                    if s.startswith(("38;", "5;", "[0m", "[1m", "[32m", "[33m")):
                        return
                    if s == _last_printed[0]:
                        return
                    _last_printed[0] = s
                    print(f"  [kiro] {s}", file=sys.stderr, flush=True)

                def _flush_line_buf() -> None:
                    """Flush accumulated partial line buffer."""
                    line = _line_buf[0]
                    _line_buf[0] = ""
                    if line:
                        _print_kiro_line(line)

                def _read_until_idle(idle_s: float) -> str:
                    """Drain line_queue until idle_s seconds with no new data,
                    or until construction docs appear in the workspace."""
                    chunks: list[str] = []
                    while True:
                        try:
                            item = line_queue.get(timeout=idle_s)
                        except queue.Empty:
                            break  # idle — kiro is waiting for input
                        if item is None:
                            break  # EOF
                        clean = _strip_ansi(item)
                        log_file.write(clean)
                        log_file.flush()
                        chunks.append(clean)
                        # Accumulate into lines and print when complete
                        for char in clean:
                            if char == "\n":
                                _flush_line_buf()
                            else:
                                _line_buf[0] += char
                        if self.verbose:
                            sys.stderr.write(item)
                            sys.stderr.flush()
                        # Check completion after every chunk so we don't wait
                        # for an idle timeout when kiro keeps streaming output.
                        if _is_complete():
                            break
                    return "".join(chunks)

                # Consume the startup banner
                _read_until_idle(3.0)

                # Send the initial prompt
                _log(f"Sending initial prompt ({len(prompt)} chars)")
                log_file.write(f"\n{'='*60}\nINITIAL PROMPT\n{'='*60}\n")
                log_file.flush()
                process.stdin.write((prompt + "\n").encode())
                process.stdin.flush()

                while gate_count < max_gates:
                    remaining = config.timeout_seconds - (time.monotonic() - start_time)
                    if remaining <= 0:
                        _log("Timeout reached")
                        process.kill()
                        break

                    turn_output = _read_until_idle(idle_timeout_s)

                    # Check if process ended
                    if process.poll() is not None:
                        total_rc = process.returncode
                        _log(f"Kiro exited with code {total_rc}")
                        break

                    # Check if workflow is complete
                    aidlc_docs_dir = workspace / "aidlc-docs"
                    if aidlc_docs_dir.is_dir():
                        has_construction = (
                            any((aidlc_docs_dir / "construction").rglob("*.md"))
                            if (aidlc_docs_dir / "construction").is_dir() else False
                        )
                        file_count = sum(1 for _ in aidlc_docs_dir.rglob("*") if _.is_file())
                        _log(f"  aidlc-docs: {file_count} files, construction={'yes' if has_construction else 'no'}")
                        if has_construction:
                            _log("Construction phase complete — terminating kiro")
                            process.kill()
                            try:
                                process.wait(timeout=10)
                            except subprocess.TimeoutExpired:
                                pass
                            total_rc = 0
                            break

                    if not turn_output.strip():
                        # No output and not complete — kiro may be at a gate
                        gate_count += 1
                        _log(f"Gate #{gate_count}: running simulator review...")
                        log_file.write(f"\n{'='*60}\nGATE {gate_count}\n{'='*60}\n")
                        log_file.flush()

                        sim_response = simulator.respond(
                            "The AIDLC executor has paused for your review. "
                            "Read the relevant aidlc-docs files to understand what was just produced, "
                            "then answer any questions, approve documents, or provide feedback. "
                            "Keep your response concise so the executor can continue."
                        )
                        _log(f"Gate #{gate_count}: simulator responded ({len(sim_response)} chars)")
                        log_file.write(f"[simulator]: {sim_response}\n")
                        log_file.flush()
                        process.stdin.write((sim_response + "\n").encode())
                        process.stdin.flush()
                    else:
                        # Got output — kiro is still working, keep reading
                        _log(f"  kiro produced {len(turn_output)} chars, continuing...")

                if process.poll() is None:
                    process.kill()
                    try:
                        process.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        pass

            elapsed_seconds = time.monotonic() - start_time
            _log(f"Completed in {elapsed_seconds:.0f}s ({gate_count} simulator gate(s))")

            # List workspace contents for debugging
            _log("Workspace contents:")
            for item in sorted(workspace.iterdir()):
                _log(f"  {item.name}/") if item.is_dir() else _log(f"  {item.name}")

            # Move aidlc-docs up from workspace/ to output_dir/ (sibling of workspace/)
            src_docs = workspace / "aidlc-docs"
            dst_docs = config.output_dir / "aidlc-docs"
            if src_docs.is_dir():
                if dst_docs.exists():
                    shutil.rmtree(dst_docs)
                shutil.move(str(src_docs), str(dst_docs))

            # Write run-meta.yaml and run-metrics.yaml
            # Kiro CLI does not expose token usage; pass turn count
            # so downstream reports show "data unavailable" rather than
            # silently reporting zeros that look like infinite efficiency.
            normalize_output(
                source_dir=workspace,
                output_dir=config.output_dir,
                adapter_name=self.name,
                elapsed_seconds=elapsed_seconds,
                token_usage={
                    "num_turns": gate_count,
                    "model": config.model or "",
                },
            )

            # Stage 2: post-run tests — same logic as the Strands runner
            _log("Running post-run test evaluation...")
            sandbox_enabled = _get_container_cli() is not None
            runner_cfg = RunnerConfig()
            runner_cfg.execution = ExecutionConfig(
                post_run_tests=True,
                post_run_timeout=300,
                sandbox=SandboxConfig(enabled=sandbox_enabled),
            )
            test_results_path = run_post_evaluation(config.output_dir, runner_cfg)
            if test_results_path:
                _log(f"Test results: {test_results_path}")
            else:
                _log("No testable project detected — post-run tests skipped.")

            has_docs = dst_docs.is_dir() and any(dst_docs.iterdir())

            if total_rc == 0 and has_docs:
                return AdapterResult(
                    success=True,
                    output_dir=config.output_dir,
                    aidlc_docs_dir=dst_docs,
                    workspace_dir=workspace,
                    elapsed_seconds=elapsed_seconds,
                )

            error_detail = (
                f"kiro-cli completed {turn} turn(s), "
                "no aidlc-docs/ output was produced."
                if not has_docs
                else f"kiro-cli completed {turn} turn(s) "
                "but aidlc-docs/ may be incomplete."
            )
            return AdapterResult(
                success=has_docs,
                output_dir=config.output_dir,
                aidlc_docs_dir=dst_docs if has_docs else None,
                workspace_dir=workspace,
                error=error_detail if not has_docs else None,
                elapsed_seconds=elapsed_seconds,
            )

        except subprocess.TimeoutExpired:
            elapsed_seconds = time.monotonic() - start_time
            process.kill()
            _log(f"Timeout after {elapsed_seconds:.0f}s — killed process")
            return AdapterResult(
                success=False,
                output_dir=config.output_dir,
                workspace_dir=workspace,
                error=f"kiro-cli timed out after {config.timeout_seconds}s",
                elapsed_seconds=elapsed_seconds,
            )

        except Exception as exc:
            elapsed_seconds = time.monotonic() - start_time
            logger.exception("kiro-cli adapter run failed")
            return AdapterResult(
                success=False,
                output_dir=config.output_dir,
                workspace_dir=workspace,
                error=f"kiro-cli adapter error: {exc}",
                elapsed_seconds=elapsed_seconds,
            )
