#!/usr/bin/env python3
"""Master run script for AIDLC evaluation framework.

This is the main entry point for running AIDLC evaluations in various modes.
It dispatches to specialized runner scripts in the scripts/ directory.

Available modes:
  - full              Full evaluation (execute workflow + score outputs)
  - cli               Evaluation through a CLI AI assistant (kiro-cli, claude-code, etc.)
  - ide               Evaluation through an IDE AI assistant (cursor, cline, kiro)
  - batch             Batch evaluation across multiple models
  - compare           Generate cross-model comparison report
  - ext-test          Test extension hooks with different opt-in configurations
  - ext-report        Regenerate extension test comparison report
  - git-compare       Compare multiple git refs across scenarios with repeated runs
  - git-compare-report Regenerate git comparison reports from existing runs
  - trend             Generate trend report across AIDLC rules releases
  - test              Run unit tests for all packages

Usage:
    # Full pipeline evaluation
    python run.py full --vision test_cases/sci-calc/vision.md

    # CLI evaluation
    python run.py cli --cli kiro-cli --scenario sci-calc

    # IDE evaluation
    python run.py ide --ide cursor --scenario sci-calc

    # Batch evaluation across models
    python run.py batch --models all --scenario sci-calc

    # Generate comparison report
    python run.py compare --scenario sci-calc

    # Test extension hooks (all yes vs all no)
    python run.py ext-test --scenario sci-calc

    # Regenerate extension comparison report
    python run.py ext-report --runs-dir runs/sci-calc/extension-test

    # Compare git refs (branches, tags, commits)
    python run.py git-compare --refs main,feat/my-feature --scenarios sci-calc --runs-per-ref 3

    # Regenerate git comparison reports from existing runs
    python run.py git-compare-report --runs-dir runs/sci-calc/git-compare

    # Generate trend report across releases
    python run.py trend --baseline test_cases/sci-calc/golden.yaml

    # Run tests
    python run.py test

    # Get help for a specific mode
    python run.py full --help
    python run.py cli --help
    python run.py ext-test --help
    python run.py git-compare --help
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SCRIPTS_DIR = REPO_ROOT / "scripts"

# Modes that require Docker sandbox
DOCKER_DEPENDENT_MODES = {"full", "cli", "ide", "batch", "git-compare", "ext-test"}


def check_docker_sandbox() -> bool:
    """Check if Docker is available and the sandbox image exists.

    Returns:
        True if Docker and sandbox image are available, False otherwise
    """
    try:
        # Check if Docker is running
        result = subprocess.run(
            ["docker", "info"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5,
        )
        if result.returncode != 0:
            return False

        # Check if sandbox image exists
        result = subprocess.run(
            ["docker", "images", "-q", "aidlc-sandbox:latest"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        return bool(result.stdout.strip())
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="run.py",
        description="AIDLC Evaluation Framework — unified entry point",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    subparsers = parser.add_subparsers(
        dest="mode",
        title="evaluation modes",
        description="Choose an evaluation mode to run",
        help="Mode-specific help available via: python run.py <mode> --help",
    )

    # Full evaluation mode
    subparsers.add_parser(
        "full",
        help="Full evaluation: execute AIDLC workflow + score outputs",
        add_help=False,
    )

    # CLI evaluation mode
    subparsers.add_parser(
        "cli",
        help="Evaluation through CLI AI assistants (kiro-cli, claude-code, etc.)",
        add_help=False,
    )

    # IDE evaluation mode
    subparsers.add_parser(
        "ide",
        help="Evaluation through IDE AI assistants (cursor, cline, kiro)",
        add_help=False,
    )

    # Batch evaluation mode
    subparsers.add_parser(
        "batch",
        help="Batch evaluation across multiple Bedrock models",
        add_help=False,
    )

    # Comparison report mode
    subparsers.add_parser(
        "compare",
        help="Generate cross-model comparison report from batch runs",
        add_help=False,
    )

    # Extension test mode
    subparsers.add_parser(
        "ext-test",
        help="Test extension hooks with different opt-in configurations",
        add_help=False,
    )

    # Extension report regeneration mode
    subparsers.add_parser(
        "ext-report",
        help="Regenerate extension test comparison report from completed runs",
        add_help=False,
    )

    # Git compare mode
    subparsers.add_parser(
        "git-compare",
        help="Compare multiple git refs across scenarios with repeated runs",
        add_help=False,
    )

    # Git compare report regeneration mode
    subparsers.add_parser(
        "git-compare-report",
        help="Regenerate git comparison reports from existing runs",
        add_help=False,
    )

    # Trend report mode
    subparsers.add_parser(
        "trend",
        help="Generate trend report across AIDLC rules releases",
        add_help=False,
    )

    # Test mode
    subparsers.add_parser(
        "test",
        help="Run unit tests for all packages",
        add_help=False,
    )

    # Parse just the mode, then delegate to the appropriate script
    args, remaining = parser.parse_known_args()

    if not args.mode:
        parser.print_help()
        sys.exit(1)

    # Map modes to scripts
    mode_to_script = {
        "full": SCRIPTS_DIR / "run_evaluation.py",
        "cli": SCRIPTS_DIR / "run_cli_evaluation.py",
        "ide": SCRIPTS_DIR / "run_ide_evaluation.py",
        "batch": SCRIPTS_DIR / "run_batch_evaluation.py",
        "compare": SCRIPTS_DIR / "run_comparison_report.py",
        "ext-test": SCRIPTS_DIR / "run_extension_test.py",
        "ext-report": SCRIPTS_DIR / "regenerate_extension_report.py",
        "git-compare": SCRIPTS_DIR / "run_git_compare.py",
        "git-compare-report": SCRIPTS_DIR / "regenerate_git_compare_report.py",
        "trend": SCRIPTS_DIR / "run_trend_report.py",
        "test": SCRIPTS_DIR / "run_evaluation.py",  # test mode is in run_evaluation.py
    }

    script = mode_to_script[args.mode]

    if not script.exists():
        print(f"Error: script not found: {script}", file=sys.stderr)
        sys.exit(1)

    # Build command to delegate to the specific script
    cmd = [sys.executable, str(script)]

    # For test mode, add --test flag
    if args.mode == "test":
        cmd.append("--test")

    # Forward all remaining arguments
    cmd.extend(remaining)

    # Check Docker sandbox availability for modes that need it
    if args.mode in DOCKER_DEPENDENT_MODES:
        if not check_docker_sandbox():
            print("=" * 70, file=sys.stderr)
            print("ERROR: Docker sandbox image not found", file=sys.stderr)
            print("=" * 70, file=sys.stderr)
            print(file=sys.stderr)
            print("The evaluation framework requires the Docker sandbox image", file=sys.stderr)
            print("'aidlc-sandbox:latest' to run generated code safely.", file=sys.stderr)
            print(file=sys.stderr)
            print("To build the image, run:", file=sys.stderr)
            print("  ./docker/sandbox/build.sh", file=sys.stderr)
            print(file=sys.stderr)
            print("Or manually:", file=sys.stderr)
            print("  docker build -t aidlc-sandbox:latest docker/sandbox/", file=sys.stderr)
            print(file=sys.stderr)
            print("To run without Docker (not recommended for untrusted code),", file=sys.stderr)
            print("set 'execution.sandbox.enabled: false' in config/default.yaml", file=sys.stderr)
            print("=" * 70, file=sys.stderr)
            sys.exit(1)

    # Execute the script
    try:
        # nosec B603 - Executing trusted framework scripts from scripts/ directory
        # nosemgrep: dangerous-subprocess-use-audit
        result = subprocess.run(cmd)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\n[Interrupted]", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Error running {script.name}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
