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

            # Two-phase approach using kiro's --no-interactive + --resume:
            #
            # Phase 1: run kiro with initial prompt until inception is complete
            #          (execution-plan.md exists). Kiro runs with --no-interactive
            #          so it exits cleanly after inception.
            # Simulator: review inception artifacts and produce feedback.
            # Phase 2: resume kiro with --resume [feedback] to drive construction.
            #
            # This uses kiro's native conversation continuation rather than
            # fighting its internal steering rules.
            base_flags = ["--no-interactive", "--trust-all-tools"]
            if config.model:
                base_flags += ["--model", config.model]

            log_path = config.output_dir / "kiro-session.log"
            _log(f"Session log: {log_path}")

            gate_count = 0
            total_rc = 0

            def _run_kiro_phase(phase_prompt: str, phase_name: str) -> tuple[str, int]:
                """Run one kiro phase and return (output, exit_code)."""
                if phase_name == "phase-1":
                    cmd = [_KIRO_CLI, "chat"] + base_flags + [phase_prompt]
                else:
                    cmd = [_KIRO_CLI, "chat"] + base_flags + ["--resume", phase_prompt]

                _log(f"{phase_name}: launching kiro ({len(phase_prompt)} chars)")

                # nosec B603 - Executing user's Kiro CLI with validated configuration
                # nosemgrep: dangerous-subprocess-use-audit
                proc = subprocess.Popen(
                    cmd,
                    cwd=str(workspace),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                )

                output_lines: list[str] = []
                last_printed = [""]
                line_buf = [""]

                def _print_line(line: str) -> None:
                    s = line.strip()
                    if not s or len(s) < 8:
                        return
                    skip = ("⠀","⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏",
                            "⣴","⣿","⠿","╭","╰","│","▸ Credits:","Credits:",
                            "Model:","Plan:","All tools are","Agents can",
                            "Learn more","https://","Did you know","Jump into",
                            "Use /","38;","5;","[0m","[1m")
                    if any(s.startswith(p) for p in skip):
                        return
                    if s == last_printed[0]:
                        return
                    last_printed[0] = s
                    print(f"  [kiro] {s}", file=sys.stderr, flush=True)

                with open(log_path, "a", encoding="utf-8") as lf:
                    lf.write(f"\n{'='*60}\n{phase_name.upper()}\n{'='*60}\n")
                    lf.flush()
                    while True:
                        chunk = proc.stdout.read(4096)
                        if not chunk:
                            break
                        text = chunk.decode("utf-8", errors="replace")
                        clean = _strip_ansi(text)
                        lf.write(clean)
                        lf.flush()
                        output_lines.append(clean)
                        for ch in clean:
                            if ch == "\n":
                                _print_line(line_buf[0])
                                line_buf[0] = ""
                            else:
                                line_buf[0] += ch
                        if self.verbose:
                            sys.stderr.write(text)
                            sys.stderr.flush()

                proc.wait()
                return "".join(output_lines), proc.returncode

            # Phase 1: inception
            _log("Phase 1: running inception...")
            inception_prompt = (
                prompt
                + "\n\nIMPORTANT: Execute ONLY the INCEPTION PHASE stages "
                + "(Workspace Detection, Requirements Analysis, Workflow Planning, "
                + "Application Design, Units Generation). "
                + "Stop after completing the Workflow Planning stage and producing "
                + "aidlc-docs/inception/plans/execution-plan.md. "
                + "Do NOT proceed to Construction. End your response when inception is done."
            )
            phase1_output, rc1 = _run_kiro_phase(inception_prompt, "phase-1")
            _log(f"Phase 1 complete (exit {rc1})")

            # Check inception produced docs
            inception_dir = workspace / "aidlc-docs" / "inception"
            has_inception = inception_dir.is_dir() and any(inception_dir.rglob("*.md"))
            _log(f"Inception docs: {'found' if has_inception else 'NOT FOUND'}")

            # Simulator reviews inception
            gate_count += 1
            _log(f"Gate #{gate_count}: simulator reviewing inception...")
            sim_feedback = simulator.respond(
                "The AIDLC executor has completed the Inception phase. "
                "Please review the inception artifacts in aidlc-docs/inception/ — "
                "requirements, execution plan, application design, and any other documents produced. "
                "Answer any open questions, approve or request changes to the design, "
                "and provide clear direction for the Construction phase. "
                "Be specific and concise so the executor can proceed."
            )
            _log(f"Gate #{gate_count}: simulator responded ({len(sim_feedback)} chars)")

            # Phase 2: construction
            _log("Phase 2: running construction with simulator feedback...")
            construction_prompt = (
                "The human reviewer has reviewed the inception artifacts and provides this feedback:\n\n"
                f"{sim_feedback}\n\n"
                "Now proceed with the CONSTRUCTION PHASE as planned in the execution plan. "
                "Execute Code Generation and Build and Test stages to completion."
            )
            phase2_output, rc2 = _run_kiro_phase(construction_prompt, "phase-2")
            _log(f"Phase 2 complete (exit {rc2})")
            total_rc = rc2

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
