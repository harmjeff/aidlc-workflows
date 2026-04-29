#!/usr/bin/env python3
"""Regenerate git comparison reports from completed runs.

Scans a git-compare runs directory for its git-compare-summary.yaml, groups
run folders by (version, scenario), and regenerates all per-scenario detail
reports and the rollup report without re-running any evaluations.

Usage:
    python run.py git-compare-report --runs-dir runs/sci-calc/git-compare
    python run.py git-compare-report --runs-dir runs/git-compare
"""

from __future__ import annotations

import argparse
import sys
from datetime import UTC, datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent

# Add scripts dir so we can import shared report logic from run_git_compare
sys.path.insert(0, str(REPO_ROOT / "scripts"))
# Add packages needed by run_git_compare imports
sys.path.insert(0, str(REPO_ROOT / "packages" / "shared" / "src"))
sys.path.insert(0, str(REPO_ROOT / "packages" / "reporting" / "src"))

from run_git_compare import write_reports  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="regenerate_git_compare_report",
        description="Regenerate git comparison reports from completed runs",
    )
    parser.add_argument(
        "--runs-dir", type=Path, required=True,
        help="Git compare runs directory containing git-compare-summary.yaml",
    )
    args = parser.parse_args()

    summary_path = args.runs_dir / "git-compare-summary.yaml"
    if not summary_path.exists():
        print(f"Error: {summary_path} not found", file=sys.stderr)
        print(
            "Make sure --runs-dir points to the git-compare output directory "
            "that contains git-compare-summary.yaml.",
            file=sys.stderr,
        )
        sys.exit(1)

    with open(summary_path, encoding="utf-8") as f:
        summary = yaml.safe_load(f) or {}

    version_names: list[str] = summary.get("version_names", [])
    scenarios: list[str] = summary.get("scenarios", [])
    all_results: list[dict] = summary.get("runs", [])

    if not version_names or not scenarios or not all_results:
        print(
            "Error: git-compare-summary.yaml is missing version_names, scenarios, or runs.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(
        f"Loaded summary: {len(all_results)} run(s) across "
        f"{len(version_names)} version(s) and {len(scenarios)} scenario(s)"
    )
    print(f"  Versions:  {', '.join(version_names)}")
    print(f"  Scenarios: {', '.join(scenarios)}")

    generated_at = datetime.now(UTC).isoformat(timespec="seconds")

    write_reports(
        runs_dir=args.runs_dir,
        scenarios=scenarios,
        version_names=version_names,
        all_results=all_results,
        generated_at=generated_at,
    )

    print(f"\nReports regenerated in: {args.runs_dir / 'comparison'}")


if __name__ == "__main__":
    main()
