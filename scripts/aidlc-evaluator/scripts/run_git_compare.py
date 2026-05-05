#!/usr/bin/env python3
"""Git Version Comparison Runner — compare multiple versions of AIDLC rules.

Runs the AIDLC evaluation pipeline against multiple versions, where each
version specifies a git ref and optionally its own repository URL (GitHub,
GitLab, any git host), executor model, and base config.  Supports repeated
runs per version for non-determinism analysis.

Generates per-scenario detail reports (raw numbers per run) and a rollup
report with avg +/- std dev aggregated across repeated runs.

Usage:
    # Simple ref comparison (all refs share the repo URL from config)
    python run.py git-compare \\
        --refs main,feat/my-feature \\
        --scenarios sci-calc \\
        --runs-per-ref 3

    # Per-version sources via a versions file (different repos, models, etc.)
    python run.py git-compare \\
        --versions-file versions.yaml \\
        --scenarios sci-calc,all-stages \\
        --runs-per-ref 2

    # Incremental mode: add new versions to existing comparison
    python run.py git-compare \\
        --versions-file versions-expanded.yaml \\
        --scenarios sci-calc \\
        --runs-per-ref 2 \\
        --runs-dir runs/sci-calc/git-compare \\
        --incremental

    # Parallel execution: run up to 3 evaluations concurrently
    python run.py git-compare \\
        --versions-file versions.yaml \\
        --scenarios sci-calc \\
        --runs-per-ref 3 \\
        --max-parallel 3

    # Regenerate reports from existing runs
    python run.py git-compare-report \\
        --runs-dir runs/sci-calc/git-compare

Versions file format (versions.yaml):
    versions:
      - name: main-github
        ref: main
        repo: https://github.com/awslabs/aidlc-workflows.git

      - name: my-feature-gitlab
        ref: feat/new-rules
        repo: https://gitlab.com/myorg/aidlc-fork.git
        executor_model: global.anthropic.claude-sonnet-4-6-v1  # optional
        config: config/sonnet-4-6.yaml                         # optional

Incremental mode:
    In incremental mode (--incremental), the script:
    1. Loads existing git-compare-summary.yaml from --runs-dir
    2. Identifies which versions have already been tested
    3. Runs evaluations ONLY for new versions not in the existing summary
    4. Merges new results with existing data
    5. Regenerates all reports with the complete dataset

    Example workflow:
    # Week 1: Test 2 versions
    python run.py git-compare --versions-file v1-2.yaml --scenarios sci-calc --runs-per-ref 3

    # Week 2: Add 3rd version (only runs 1 new version, ~30 min vs ~90 min)
    python run.py git-compare --versions-file v1-3.yaml --scenarios sci-calc --runs-per-ref 3 \\
        --runs-dir runs/sci-calc/git-compare --incremental

    Use --force-rerun to re-run versions that already exist in the summary.
"""

from __future__ import annotations

import argparse
import math
import os
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = REPO_ROOT / "config"
DEFAULT_CONFIG = CONFIG_DIR / "default.yaml"
TEST_CASES_DIR = REPO_ROOT / "test_cases"
SCRIPTS_DIR = REPO_ROOT / "scripts"

# Add shared and reporting packages to path
sys.path.insert(0, str(REPO_ROOT / "packages" / "shared" / "src"))
sys.path.insert(0, str(REPO_ROOT / "packages" / "reporting" / "src"))

from shared.scenario import resolve_scenario, Scenario  # noqa: E402
from reporting.baseline import BaselineMetrics, extract_baseline  # noqa: E402
from reporting.collector import collect  # noqa: E402


# ── Version spec ───────────────────────────────────────────────────────────────


@dataclass
class Version:
    """A single version to compare — a named (repo, ref) pair with optional overrides."""

    name: str
    """Display label used in report column headers and run folder names."""

    ref: str
    """Git ref: branch name, tag, or commit SHA."""

    repo: str | None = None
    """Git repository URL. None means use the value from the base config YAML."""

    executor_model: str | None = None
    """Per-version executor model override. None means use the global default."""

    config: Path | None = None
    """Per-version base config YAML. None means use the global --config value."""


def parse_versions_file(path: Path) -> list[Version]:
    """Load a versions YAML file and return a list of Version objects.

    Expected format::

        versions:
          - name: main-github
            ref: main
            repo: https://github.com/awslabs/aidlc-workflows.git
          - name: my-feature
            ref: feat/my-feature
            repo: https://gitlab.com/myorg/fork.git
            executor_model: global.anthropic.claude-sonnet-4-6-v1
            config: config/sonnet-4-6.yaml   # resolved relative to versions file

    ``repo``, ``executor_model``, and ``config`` are all optional.
    """
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    raw = data.get("versions", [])
    if not raw:
        raise ValueError(f"versions file {path} contains no 'versions' list")

    versions: list[Version] = []
    for i, v in enumerate(raw):
        name = v.get("name", "").strip()
        if not name:
            raise ValueError(f"version entry {i + 1} in {path} is missing 'name'")
        ref = v.get("ref", "").strip()
        if not ref:
            raise ValueError(f"version '{name}' in {path} is missing 'ref'")

        cfg_override: Path | None = None
        if v.get("config"):
            cfg_path = Path(v["config"])
            if not cfg_path.is_absolute():
                cfg_path = path.parent / cfg_path
            cfg_override = cfg_path

        versions.append(Version(
            name=name,
            ref=ref,
            repo=v.get("repo") or None,
            executor_model=v.get("executor_model") or None,
            config=cfg_override,
        ))

    return versions


def versions_from_refs(refs: list[str]) -> list[Version]:
    """Build a list of Versions from a plain list of git refs.

    The version name is derived from the ref by replacing '/' with '_' and
    truncating to 40 characters (same slug logic used for folder names).
    The repo field is left None so each run inherits the repo URL from config.
    """
    return [Version(name=ref_to_slug(ref), ref=ref) for ref in refs]


# ── Metrics and formatting ─────────────────────────────────────────────────────


# Metric rows used in all reports: (display_name, attr_name, higher_is_better)
# attr_name="" marks a section-header row (no data cell).
# "wall_clock_min" is a computed alias for wall_clock_ms / 60000.
METRIC_ROWS: list[tuple[str, str, bool]] = [
    ("**Unit Tests**", "", True),
    ("Pass %", "tests_pass_pct", True),
    ("Passed", "tests_passed", True),
    ("Failed", "tests_failed", False),
    ("Total", "tests_total", True),
    ("Coverage %", "coverage_pct", True),
    ("**Contract Tests**", "", True),
    ("Passed", "contract_passed", True),
    ("Failed", "contract_failed", False),
    ("Total", "contract_total", True),
    ("**Code Quality**", "", True),
    ("Lint Errors", "lint_errors", False),
    ("Lint Warnings", "lint_warnings", False),
    ("Lint Total", "lint_total", False),
    ("Security Findings", "security_total", False),
    ("Security High", "security_high", False),
    ("Duplication Blocks", "duplication_blocks", False),
    ("**Qualitative**", "", True),
    ("Overall Score", "qualitative_score", True),
    ("Inception Score", "inception_score", True),
    ("Construction Score", "construction_score", True),
    ("**Artifacts**", "", True),
    ("Source Files", "source_files", True),
    ("Test Files", "test_files", True),
    ("Total Files", "total_files", True),
    ("Lines of Code", "lines_of_code", True),
    ("Doc Files", "doc_files", True),
    ("**Execution**", "", True),
    ("Total Tokens", "total_tokens", False),
    ("Executor Tokens", "executor_total_tokens", False),
    ("Simulator Tokens", "simulator_total_tokens", False),
    ("Wall Clock (min)", "wall_clock_min", False),
    ("Handoffs", "handoffs", False),
    ("**Context Size**", "", True),
    ("Max Tokens", "context_size_max", False),
    ("Avg Tokens", "context_size_avg", False),
    ("Median Tokens", "context_size_median", False),
]


def ref_to_slug(ref: str, max_len: int = 40) -> str:
    """Convert a git ref or version name to a filesystem-safe slug.

    Replaces '/' with '_' and truncates to max_len characters.
    """
    return ref.replace("/", "_")[:max_len]


def get_metric_value(metrics: BaselineMetrics, attr: str) -> float | None:
    """Extract a metric value from BaselineMetrics, handling the wall_clock_min alias."""
    if attr == "wall_clock_min":
        return metrics.wall_clock_ms / 60000 if metrics.wall_clock_ms else None
    return getattr(metrics, attr, None)


def format_num(val: float | int | None, decimals: int = 1) -> str:
    """Format a number for display, returning em-dash for None."""
    if val is None:
        return "\u2014"
    if isinstance(val, float):
        return f"{val:.{decimals}f}"
    return str(val)


def _mean(values: list[float]) -> float:
    return sum(values) / len(values)


def _stdev(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    m = _mean(values)
    return math.sqrt(sum((v - m) ** 2 for v in values) / (len(values) - 1))


def load_run_metrics(run_folder: Path) -> BaselineMetrics | None:
    """Load evaluation metrics from a run folder."""
    try:
        data = collect(run_folder)
        return extract_baseline(data)
    except Exception as e:
        print(f"  [WARN] Failed to collect metrics from {run_folder}: {e}", file=sys.stderr)
        return None


# ── Execution ──────────────────────────────────────────────────────────────────


def run_single_evaluation(
    version: Version,
    scenario: Scenario,
    run_index: int,
    runs_per_ref: int,
    runs_dir: Path,
    base_config: Path,
    profile: str,
    region: str,
    scorer_model: str,
    default_executor_model: str | None,
    use_sandbox: bool,
) -> dict:
    """Run a single evaluation for one (version, scenario, run_index) combination.

    The effective config, executor model, and rules repo/ref are resolved
    by layering version-level overrides on top of the global defaults.

    Returns a summary dict describing the run result.
    """
    effective_config = version.config or base_config
    effective_executor = version.executor_model or default_executor_model
    folder_slug = ref_to_slug(version.name)

    # Generate folder name upfront - orchestrator controls the output location
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S-%f")
    folder_name = f"{timestamp}-{folder_slug}"
    run_folder = runs_dir / folder_name

    _safe_print(f"\n{'=' * 70}")
    _safe_print(f"  Version:  {version.name}")
    _safe_print(f"  Ref:      {version.ref}")
    if version.repo:
        _safe_print(f"  Repo:     {version.repo}")
    _safe_print(f"  Scenario: {scenario.name}")
    _safe_print(f"  Run:      {run_index}/{runs_per_ref}")
    _safe_print(f"{'=' * 70}\n")

    cmd = [
        sys.executable, str(SCRIPTS_DIR / "run_evaluation.py"),
        "--config", str(effective_config),
        "--vision", str(scenario.vision_path),
        "--golden", str(scenario.golden_aidlc_docs_path),
        "--profile", profile,
        "--region", region,
        "--scorer-model", scorer_model,
        "--rules-ref", version.ref,
        "--report-format", "both",
        "--output-dir", str(run_folder),  # Pass full folder path, not parent dir
    ]

    if version.repo:
        cmd += ["--rules-repo", version.repo]
    if scenario.tech_env_path.is_file():
        cmd += ["--tech-env", str(scenario.tech_env_path)]
    if scenario.openapi_path.is_file():
        cmd += ["--openapi", str(scenario.openapi_path)]
    if scenario.golden_baseline_path.is_file():
        cmd += ["--baseline", str(scenario.golden_baseline_path)]
    if effective_executor:
        cmd += ["--executor-model", effective_executor]
    cmd.append("--sandbox" if use_sandbox else "--no-sandbox")

    # Create log directory
    log_dir = runs_dir / ".git-compare-logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{timestamp}-{folder_slug}-{scenario.name}-run{run_index}.log"

    start_monotonic = time.monotonic()  # Track elapsed time
    started_at = datetime.now(UTC).isoformat(timespec="seconds")
    runs_dir.mkdir(parents=True, exist_ok=True)

    with open(log_path, "w", encoding="utf-8") as log_file:
        # Write header to identify this run in the log
        log_file.write(f"=== Git-Compare Run Log ===\n")
        log_file.write(f"Version: {version.name}\n")
        log_file.write(f"Ref: {version.ref}\n")
        log_file.write(f"Repo: {version.repo or '(from config)'}\n")
        log_file.write(f"Scenario: {scenario.name}\n")
        log_file.write(f"Run: {run_index}/{runs_per_ref}\n")
        log_file.write(f"Started: {started_at}\n")
        log_file.write(f"{'=' * 70}\n\n")
        log_file.flush()

        result = subprocess.run(cmd, stdout=log_file, stderr=subprocess.STDOUT)  # nosec B603 

    elapsed_s = time.monotonic() - start_monotonic
    status = "success" if result.returncode == 0 else "failed"
    _safe_print(
        f"  [{status.upper()}] version={version.name}, scenario={scenario.name}, "
        f"run={run_index} \u2014 {elapsed_s / 60:.1f} min (exit {result.returncode})"
    )

    # We told run_evaluation.py exactly where to write, so use that folder
    if run_folder.is_dir():
        output_dir = run_folder
        _safe_print(f"  Output: {output_dir.name}")

        # Move log file with descriptive name
        final_log_name = f"git-compare-{folder_slug}-{scenario.name}-run{run_index}.log"
        final_log_path = output_dir / final_log_name
        shutil.move(str(log_path), str(final_log_path))

        # Write metadata to identify this run
        meta = {
            "git_compare_version_name": version.name,
            "git_compare_ref": version.ref,
            "git_compare_repo": version.repo,
            "git_compare_scenario": scenario.name,
            "git_compare_run_index": run_index,
            "git_compare_runs_per_version": runs_per_ref,
        }
        with open(output_dir / "git-compare-meta.yaml", "w", encoding="utf-8") as f:
            yaml.safe_dump(meta, f, default_flow_style=False, sort_keys=False)
    else:
        _safe_print(f"  [WARN] Run folder not created: {run_folder}")
        output_dir = run_folder  # Use the expected path even if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(log_path), str(output_dir / "git-compare-run.log"))

    # Clean temp log dir if empty
    if log_dir.exists() and not any(log_dir.iterdir()):
        log_dir.rmdir()

    return {
        "version_name": version.name,
        "ref": version.ref,
        "repo": version.repo,
        "scenario": scenario.name,
        "run_index": run_index,
        "started_at": started_at,
        "elapsed_seconds": round(elapsed_s, 1),
        "exit_code": result.returncode,
        "status": status,
        "output_dir": str(output_dir),
    }


# ── Report generation ──────────────────────────────────────────────────────────


def _run_label(res: dict) -> str:
    """Column label for an individual run in the detail report."""
    return f"{res['version_name']} run-{res['run_index']}"


def generate_scenario_detail_report(
    scenario_name: str,
    version_names: list[str],
    run_results: list[dict],
    generated_at: str,
) -> str:
    """Generate a per-scenario detail report with one column per individual run.

    Columns are ordered by version (preserving the order in version_names)
    then by run index. Each cell contains the raw numeric value for that run.
    """
    lines: list[str] = [
        f"# Git Version Comparison \u2014 {scenario_name}",
        "",
        f"**Scenario:** {scenario_name}",
        f"**Generated:** {generated_at}",
        "",
        "## Run Detail (Raw Numbers)",
        "",
        "Each column is one individual run. "
        "Runs are grouped by version (in the order specified) then sorted by run index.",
        "",
    ]

    version_order = {n: i for i, n in enumerate(version_names)}
    sorted_results = sorted(
        run_results,
        key=lambda r: (version_order.get(r["version_name"], 999), r["run_index"]),
    )

    col_labels: list[str] = []
    col_metrics: list[BaselineMetrics | None] = []
    for res in sorted_results:
        col_labels.append(_run_label(res))
        folder = Path(res["output_dir"])
        col_metrics.append(load_run_metrics(folder) if folder.is_dir() else None)

    header = "| Metric |"
    separator = "|--------|"
    for label in col_labels:
        header += f" {label} |"
        separator += "---------|"
    lines.append(header)
    lines.append(separator)

    for display_name, attr, _ in METRIC_ROWS:
        if not attr:
            row = f"| {display_name} |"
            for _ in col_labels:
                row += " |"
            lines.append(row)
            continue

        row = f"| {display_name} |"
        for metrics in col_metrics:
            if metrics is None:
                row += " \u2014 |"
            else:
                val = get_metric_value(metrics, attr)
                row += f" {format_num(val)} |"
        lines.append(row)

    lines.append("")

    # Run status table
    lines.extend([
        "",
        "## Run Status",
        "",
        "| Version | Ref | Repo | Run | Status | Duration (min) | Output |",
        "|---------|-----|------|-----|--------|----------------|--------|",
    ])
    for res in sorted_results:
        marker = "PASS" if res["status"] == "success" else "FAIL"
        duration = res.get("elapsed_seconds", 0) / 60
        repo_display = res.get("repo") or "*(from config)*"
        lines.append(
            f"| {res['version_name']} | {res['ref']} | {repo_display} "
            f"| {res['run_index']} | {marker} | {duration:.1f} "
            f"| `{res['output_dir']}` |"
        )
    lines.append("")

    return "\n".join(lines)


def _build_rollup_section(
    scenario_name: str,
    version_names: list[str],
    run_results: list[dict],
) -> list[str]:
    """Build markdown lines for one scenario's rollup table (avg +/- std dev)."""
    lines: list[str] = [
        f"## Scenario: {scenario_name}",
        "",
    ]

    # Group loaded metrics by version name
    version_metrics: dict[str, list[BaselineMetrics]] = {n: [] for n in version_names}
    for res in run_results:
        vn = res["version_name"]
        folder = Path(res["output_dir"])
        if folder.is_dir():
            m = load_run_metrics(folder)
            if m is not None:
                version_metrics.setdefault(vn, []).append(m)

    # Build column descriptors: (header_label, version_name, metrics_list)
    columns: list[tuple[str, str, list[BaselineMetrics]]] = []
    for vn in version_names:
        mlist = version_metrics.get(vn, [])
        columns.append((f"{vn} (n={len(mlist)})", vn, mlist))

    if not any(mlist for _, _, mlist in columns):
        lines.append("_No metrics available for this scenario._")
        return lines

    baseline_name = version_names[0] if version_names else None

    header = "| Metric |"
    separator = "|--------|"
    for label, _, _ in columns:
        header += f" {label} |"
        separator += "---------|"
    lines.append(header)
    lines.append(separator)

    for display_name, attr, higher_is_better in METRIC_ROWS:
        if not attr:
            row = f"| {display_name} |"
            for _ in columns:
                row += " |"
            lines.append(row)
            continue

        # Compute per-version (avg, stdev)
        version_stats: list[tuple[float | None, float | None]] = []
        for _, vn, mlist in columns:
            vals = [v for v in (get_metric_value(m, attr) for m in mlist) if v is not None]
            if not vals:
                version_stats.append((None, None))
            elif len(vals) == 1:
                version_stats.append((vals[0], None))
            else:
                version_stats.append((_mean(vals), _stdev(vals)))

        baseline_avg = version_stats[0][0] if version_stats else None

        row = f"| {display_name} |"
        for i, (_label, _vn, _mlist) in enumerate(columns):
            avg, std = version_stats[i]
            if avg is None:
                row += " \u2014 |"
                continue

            cell = format_num(avg)
            if std is not None and std > 0:
                cell += f" \u00b1 {format_num(std)}"

            # Delta indicator vs baseline version (skip for the baseline column itself)
            if i > 0 and baseline_avg is not None:
                delta = avg - baseline_avg
                if abs(delta) > 0.001:
                    cell += (" ^" if delta > 0 else " v") if higher_is_better \
                        else (" v" if delta > 0 else " ^")

            row += f" {cell} |"
        lines.append(row)

    lines.append("")
    lines.append(
        f"**Legend:** ^ = better than `{baseline_name}` (baseline version), "
        f"v = worse. \u00b1 = sample std dev across repeated runs."
    )

    return lines


def generate_rollup_report(
    scenarios: list[str],
    version_names: list[str],
    all_results: list[dict],
    generated_at: str,
) -> str:
    """Generate the multi-scenario rollup report (avg +/- std dev per version).

    One section per scenario; delta indicators vs the first version listed.
    """
    lines: list[str] = [
        "# Git Version Comparison \u2014 Rollup Report",
        "",
        f"**Generated:** {generated_at}",
        f"**Versions:** {', '.join(version_names)}",
        f"**Scenarios:** {', '.join(scenarios)}",
        "",
        "> Values shown as `avg \u00b1 std_dev` when multiple runs were performed.",
        "> ^ = better than baseline version (first version listed), v = worse.",
        "",
    ]

    for scenario_name in scenarios:
        scenario_results = [r for r in all_results if r["scenario"] == scenario_name]
        lines.extend(_build_rollup_section(scenario_name, version_names, scenario_results))
        lines.append("")

    return "\n".join(lines)


def write_reports(
    runs_dir: Path,
    scenarios: list[str],
    version_names: list[str],
    all_results: list[dict],
    generated_at: str,
) -> None:
    """Write all per-scenario detail reports and the rollup report to disk.

    Outputs are written to <runs_dir>/comparison/:
      - <scenario>-report.md / <scenario>-report.yaml  (one per scenario)
      - rollup-report.md / rollup-data.yaml
    """
    comparison_dir = runs_dir / "comparison"
    comparison_dir.mkdir(parents=True, exist_ok=True)

    for scenario_name in scenarios:
        scenario_results = [r for r in all_results if r["scenario"] == scenario_name]
        if not scenario_results:
            continue

        print(f"  Writing detail report: {scenario_name}...")
        md = generate_scenario_detail_report(
            scenario_name=scenario_name,
            version_names=version_names,
            run_results=scenario_results,
            generated_at=generated_at,
        )
        md_path = comparison_dir / f"{scenario_name}-report.md"
        md_path.write_text(md, encoding="utf-8")
        print(f"    {md_path}")

        yaml_data: dict = {
            "generated_at": generated_at,
            "scenario": scenario_name,
            "version_names": version_names,
            "runs": [
                {
                    "version_name": r["version_name"],
                    "ref": r["ref"],
                    "repo": r.get("repo"),
                    "run_index": r["run_index"],
                    "status": r["status"],
                    "elapsed_seconds": r.get("elapsed_seconds"),
                    "output_dir": r["output_dir"],
                }
                for r in sorted(scenario_results, key=lambda x: (x["version_name"], x["run_index"]))
            ],
        }
        yaml_path = comparison_dir / f"{scenario_name}-report.yaml"
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(yaml_data, f, default_flow_style=False, sort_keys=False)
        print(f"    {yaml_path}")

    print("  Writing rollup report...")
    rollup_md = generate_rollup_report(
        scenarios=scenarios,
        version_names=version_names,
        all_results=all_results,
        generated_at=generated_at,
    )
    rollup_md_path = comparison_dir / "rollup-report.md"
    rollup_md_path.write_text(rollup_md, encoding="utf-8")
    print(f"    {rollup_md_path}")

    rollup_yaml: dict = {
        "generated_at": generated_at,
        "version_names": version_names,
        "scenarios": scenarios,
        "runs": all_results,
    }
    rollup_yaml_path = comparison_dir / "rollup-data.yaml"
    with open(rollup_yaml_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(rollup_yaml, f, default_flow_style=False, sort_keys=False)
    print(f"    {rollup_yaml_path}")

    print("  Writing interactive HTML report...")
    from generate_html_report import generate_interactive_html_report
    html_report = generate_interactive_html_report(
        scenarios=scenarios,
        version_names=version_names,
        all_results=all_results,
        generated_at=generated_at,
        runs_dir=runs_dir,
    )
    html_path = comparison_dir / "interactive-report.html"
    html_path.write_text(html_report, encoding="utf-8")
    print(f"    {html_path}")


# ── Parallel execution ────────────────────────────────────────────────────────


# Global lock for thread-safe printing
_print_lock = threading.Lock()


def _safe_print(*args, **kwargs):
    """Thread-safe print for parallel execution."""
    with _print_lock:
        print(*args, **kwargs)


@dataclass
class WorkItem:
    """A single evaluation work item for parallel execution."""
    version: Version
    scenario: "Scenario"
    run_index: int
    runs_per_ref: int
    runs_dir: Path
    base_config: Path
    profile: str
    region: str
    scorer_model: str
    default_executor_model: str | None
    use_sandbox: bool


def execute_work_item(item: WorkItem) -> dict:
    """Execute a single evaluation work item (thread-safe wrapper).

    This is called by ThreadPoolExecutor and wraps run_single_evaluation
    with thread-safe output handling.
    """
    return run_single_evaluation(
        version=item.version,
        scenario=item.scenario,
        run_index=item.run_index,
        runs_per_ref=item.runs_per_ref,
        runs_dir=item.runs_dir,
        base_config=item.base_config,
        profile=item.profile,
        region=item.region,
        scorer_model=item.scorer_model,
        default_executor_model=item.default_executor_model,
        use_sandbox=item.use_sandbox,
    )


def run_parallel_evaluations(
    work_items: list[WorkItem],
    max_workers: int,
) -> list[dict]:
    """Run evaluations in parallel with progress tracking.

    Args:
        work_items: List of work items to execute
        max_workers: Maximum number of concurrent workers

    Returns:
        List of result dicts in original submission order
    """
    all_results = []
    total = len(work_items)
    completed = 0

    _safe_print(f"\n{'=' * 70}")
    _safe_print(f"  Parallel Execution: {total} runs, max {max_workers} concurrent")
    _safe_print(f"{'=' * 70}\n")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all work with tracking
        future_to_item = {
            executor.submit(execute_work_item, item): (i, item)
            for i, item in enumerate(work_items)
        }

        # Collect results as they complete
        for future in as_completed(future_to_item):
            idx, item = future_to_item[future]
            completed += 1

            try:
                result = future.result()
                all_results.append((idx, result))

                status = "✓" if result.get("status") == "success" else "✗"
                duration = result.get("elapsed_seconds", 0) / 60
                _safe_print(
                    f"  [{completed:2d}/{total}] {status} {item.version.name:30s} "
                    f"{item.scenario.name:15s} run-{item.run_index}  ({duration:.1f} min)"
                )

            except Exception as e:
                _safe_print(
                    f"  [{completed:2d}/{total}] ✗ {item.version.name:30s} "
                    f"{item.scenario.name:15s} run-{item.run_index}  ERROR: {e}"
                )
                # Create error result
                error_result = {
                    "version_name": item.version.name,
                    "ref": item.version.ref,
                    "repo": item.version.repo,
                    "scenario": item.scenario.name,
                    "run_index": item.run_index,
                    "status": "error",
                    "error": str(e),
                    "output_dir": str(
                        item.runs_dir
                        / f"failed-{ref_to_slug(item.version.name)}-{item.scenario.name}-run{item.run_index}"
                    ),
                }
                all_results.append((idx, error_result))

    _safe_print(f"\n{'=' * 70}")
    _safe_print(f"  Parallel execution complete: {completed}/{total} finished")
    _safe_print(f"{'=' * 70}\n")

    # Sort by original submission order
    all_results.sort(key=lambda x: x[0])
    return [result for _, result in all_results]


# ── Incremental mode helpers ──────────────────────────────────────────────────


def load_existing_summary(runs_dir: Path) -> dict | None:
    """Load existing git-compare-summary.yaml if it exists.

    Returns:
        Summary dict with keys: version_names, scenarios, runs_per_version, runs
        Returns None if summary doesn't exist.

    Raises:
        ValueError: If summary exists but is malformed.
    """
    summary_path = runs_dir / "git-compare-summary.yaml"
    if not summary_path.exists():
        return None

    with open(summary_path, encoding="utf-8") as f:
        summary = yaml.safe_load(f) or {}

    required_keys = ["version_names", "scenarios", "runs_per_version", "runs"]
    missing = [k for k in required_keys if k not in summary]
    if missing:
        raise ValueError(
            f"Existing summary at {summary_path} is missing required keys: {missing}"
        )

    return summary


def filter_new_versions(
    versions: list[Version],
    existing_version_names: set[str],
    force_rerun: bool,
) -> tuple[list[Version], list[Version]]:
    """Separate versions into new vs. already-tested.

    Args:
        versions: All versions from versions file
        existing_version_names: Version names from existing summary
        force_rerun: If True, treat all versions as new

    Returns:
        (new_versions, skipped_versions)
    """
    if force_rerun:
        return versions, []

    new_versions = [v for v in versions if v.name not in existing_version_names]
    skipped_versions = [v for v in versions if v.name in existing_version_names]

    return new_versions, skipped_versions


def merge_summaries(
    existing_summary: dict,
    new_results: list[dict],
    new_versions: list[Version],
    new_elapsed_seconds: float,
) -> dict:
    """Merge new run results into existing summary.

    Args:
        existing_summary: Loaded from git-compare-summary.yaml
        new_results: Run results from newly executed versions
        new_versions: Version objects for newly tested versions
        new_elapsed_seconds: Elapsed time for new runs

    Returns:
        Updated summary dict with merged data
    """
    new_version_names = [v.name for v in new_versions]

    # Merge version names (preserve order: existing + new)
    all_version_names = existing_summary["version_names"] + new_version_names

    # Merge version specs
    existing_version_specs = existing_summary.get("versions", [])
    new_version_specs = [
        {
            "name": v.name,
            "ref": v.ref,
            "repo": v.repo,
            "executor_model": v.executor_model,
        }
        for v in new_versions
    ]
    all_version_specs = existing_version_specs + new_version_specs

    # Merge run results
    all_runs = existing_summary["runs"] + new_results

    # Update counts
    runs_succeeded = sum(1 for r in all_runs if r.get("status") == "success")
    runs_failed = sum(1 for r in all_runs if r.get("status") != "success")

    # Track incremental runs
    incremental_runs = existing_summary.get("incremental_runs", [])
    incremental_runs.append({
        "added_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "versions_added": new_version_names,
        "runs_added": len(new_results),
        "elapsed_seconds": round(new_elapsed_seconds, 1),
    })

    return {
        "started_at": existing_summary["started_at"],  # Keep original start time
        "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),  # Update
        "total_elapsed_seconds": existing_summary["total_elapsed_seconds"],  # Original only
        "incremental_runs": incremental_runs,  # Track all incremental additions
        "version_names": all_version_names,
        "versions": all_version_specs,
        "scenarios": existing_summary["scenarios"],
        "runs_per_version": existing_summary["runs_per_version"],
        "total_runs": len(all_runs),
        "runs_succeeded": runs_succeeded,
        "runs_failed": runs_failed,
        "runs": all_runs,
    }


# ── CLI ────────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="run_git_compare",
        description=(
            "Compare multiple versions of AIDLC rules across scenarios and repeated runs. "
            "Each version can target a different git repository (GitHub, GitLab, etc.), "
            "ref, executor model, and base config."
        ),
    )

    # Version specification — mutually exclusive
    version_group = parser.add_mutually_exclusive_group(required=True)
    version_group.add_argument(
        "--refs", type=str, default=None,
        help=(
            "Comma-separated git refs to compare. "
            "All refs share the repository URL from the base config YAML. "
            "Use --versions-file when different repos or per-version settings are needed."
        ),
    )
    version_group.add_argument(
        "--versions-file", type=Path, default=None,
        help=(
            "Path to a YAML file defining named versions with per-version repo URL, "
            "ref, executor model, and config overrides. "
            "Mutually exclusive with --refs."
        ),
    )

    parser.add_argument(
        "--scenarios", type=str, default="sci-calc",
        help="Comma-separated scenario names (default: sci-calc)",
    )
    parser.add_argument(
        "--runs-per-ref", type=int, default=1,
        help="Number of evaluation runs per (version, scenario) pair (default: 1)",
    )

    # Global config (can be overridden per-version via versions file)
    parser.add_argument(
        "--config", type=Path, default=DEFAULT_CONFIG,
        help="Base config YAML (default: config/default.yaml)",
    )
    parser.add_argument("--profile", default=None, help="AWS profile")
    parser.add_argument("--region", default=None, help="AWS region")
    parser.add_argument(
        "--executor-model", default=None,
        help="Default executor model ID (can be overridden per-version in versions file)",
    )
    parser.add_argument("--scorer-model", default=None, help="Override scorer model ID")

    # Output
    parser.add_argument(
        "--runs-dir", type=Path, default=None,
        help=(
            "Base directory for all run outputs. "
            "Defaults to runs/<scenario>/git-compare/ for a single scenario "
            "or runs/git-compare/ when multiple scenarios are specified."
        ),
    )

    # Sandbox
    sandbox_group = parser.add_mutually_exclusive_group()
    sandbox_group.add_argument(
        "--sandbox", action="store_true", default=True,
        help="Run generated code in Docker sandbox (default)",
    )
    sandbox_group.add_argument(
        "--no-sandbox", action="store_false", dest="sandbox",
        help="Run generated code directly on host (no isolation)",
    )

    # Incremental mode
    parser.add_argument(
        "--incremental", action="store_true", default=False,
        help=(
            "Incremental mode: only run evaluations for versions not present in "
            "existing git-compare-summary.yaml, then merge results and regenerate "
            "reports. Requires --runs-dir to point to an existing git-compare output."
        ),
    )
    parser.add_argument(
        "--force-rerun", action="store_true", default=False,
        help=(
            "With --incremental, re-run evaluations for versions that already exist "
            "in the summary (default: skip existing versions)."
        ),
    )

    # Parallel execution
    parser.add_argument(
        "--max-parallel", type=int, default=1,
        help=(
            "Maximum number of evaluations to run in parallel (default: 1). "
            "Recommended: 2-4 depending on system resources. Each parallel run "
            "consumes ~2GB RAM and spawns a Docker container in sandbox mode. "
            "Higher values may hit Bedrock API rate limits."
        ),
    )

    args = parser.parse_args()

    # Build version list
    versions: list[Version]
    if args.versions_file:
        if not args.versions_file.exists():
            parser.error(f"versions file not found: {args.versions_file}")
        try:
            versions = parse_versions_file(args.versions_file)
        except (ValueError, yaml.YAMLError) as e:
            parser.error(str(e))
    else:
        refs = [r.strip() for r in args.refs.split(",") if r.strip()]
        if not refs:
            parser.error("--refs must specify at least one git ref")
        versions = versions_from_refs(refs)

    if not versions:
        parser.error("No versions to compare")

    # Parse scenarios
    scenario_names = [s.strip() for s in args.scenarios.split(",") if s.strip()]
    if not scenario_names:
        parser.error("--scenarios must specify at least one scenario name")

    resolved_scenarios: list[Scenario] = []
    for name in scenario_names:
        try:
            resolved_scenarios.append(resolve_scenario(name, TEST_CASES_DIR))
        except FileNotFoundError as e:
            parser.error(str(e))

    # Default runs_dir
    if args.runs_dir is None:
        if len(resolved_scenarios) == 1:
            args.runs_dir = REPO_ROOT / "runs" / resolved_scenarios[0].name / "git-compare"
        else:
            args.runs_dir = REPO_ROOT / "runs" / "git-compare"

    # Load base config for credential/model defaults
    base_cfg: dict = {}
    if args.config and args.config.exists():
        with open(args.config, encoding="utf-8") as f:
            base_cfg = yaml.safe_load(f) or {}

    if args.profile is None:
        args.profile = base_cfg.get("aws", {}).get("profile")
        # Allow None profile to use default credentials (e.g., EC2 instance role)
        # Just ensure it's explicitly set to something (even if None)

    if args.region is None:
        args.region = base_cfg.get("aws", {}).get("region")
        if args.region is None:
            parser.error("--region is required (or set aws.region in config YAML)")

    if args.scorer_model is None:
        args.scorer_model = base_cfg.get("models", {}).get("scorer", {}).get("model_id")
        if args.scorer_model is None:
            parser.error("--scorer-model is required (or set models.scorer.model_id in config YAML)")

    # Validate parallel execution settings
    if args.max_parallel < 1:
        parser.error("--max-parallel must be >= 1")

    if args.max_parallel > 8:
        print(
            f"WARNING: --max-parallel {args.max_parallel} is quite high. "
            f"Each parallel run consumes ~2GB RAM and may hit Bedrock rate limits.",
            file=sys.stderr
        )

    # Suggest optimal settings based on system resources
    cpu_count = os.cpu_count() or 1
    if args.max_parallel > cpu_count:
        print(
            f"INFO: --max-parallel {args.max_parallel} exceeds CPU count ({cpu_count}). "
            f"Consider using --max-parallel {min(cpu_count, 4)} for optimal performance.",
            file=sys.stderr
        )

    # Handle incremental mode
    existing_summary = None
    skipped_versions: list[Version] = []
    all_versions = versions  # Keep reference to all versions for final version_names

    if args.incremental:
        if not args.runs_dir:
            parser.error("--incremental requires --runs-dir to be specified")
        if not args.runs_dir.exists():
            parser.error(f"--runs-dir does not exist: {args.runs_dir}")

        try:
            existing_summary = load_existing_summary(args.runs_dir)
        except ValueError as e:
            parser.error(str(e))

        if existing_summary is None:
            parser.error(
                f"--incremental requires existing git-compare-summary.yaml in {args.runs_dir}"
            )

        # Validate consistency
        existing_scenarios = existing_summary["scenarios"]
        if set(scenario_names) != set(existing_scenarios):
            parser.error(
                f"Scenarios mismatch: new={scenario_names}, existing={existing_scenarios}"
            )
        if args.runs_per_ref != existing_summary["runs_per_version"]:
            parser.error(
                f"--runs-per-ref mismatch: new={args.runs_per_ref}, "
                f"existing={existing_summary['runs_per_version']}"
            )

        # Filter versions
        existing_version_names = set(existing_summary["version_names"])
        new_versions, skipped_versions = filter_new_versions(
            versions, existing_version_names, args.force_rerun
        )

        if skipped_versions:
            print("Git Version Comparison (Incremental Mode)")
            print(f"  Skipping {len(skipped_versions)} already-tested versions:")
            for v in skipped_versions:
                print(f"    - {v.name}")
            print()

        if not new_versions:
            print("No new versions to test. Regenerating reports from existing data...\n")
            write_reports(
                runs_dir=args.runs_dir,
                scenarios=scenario_names,
                version_names=existing_summary["version_names"],
                all_results=existing_summary["runs"],
                generated_at=datetime.now(UTC).isoformat(timespec="seconds"),
            )
            print(f"\n  Results: {args.runs_dir}")
            sys.exit(0)

        versions = new_versions  # Only run new versions

    version_names = [v.name for v in versions]
    total_runs = len(versions) * len(resolved_scenarios) * args.runs_per_ref

    mode_str = "Git Version Comparison (Incremental Mode)" if args.incremental else "Git Version Comparison"
    print(mode_str)
    if args.incremental and existing_summary:
        print(f"  Existing vers: {len(existing_summary['version_names'])} ({', '.join(existing_summary['version_names'])})")
        print(f"  New versions:  {len(version_names)} ({', '.join(version_names)})")
    else:
        print(f"  Versions:     {', '.join(version_names)}")
    print(f"  Scenarios:    {', '.join(s.name for s in resolved_scenarios)}")
    print(f"  Runs per ver: {args.runs_per_ref}")
    print(f"  Total runs:   {total_runs}")
    print(f"  Max parallel: {args.max_parallel}")
    print(f"  Profile:      {args.profile}")
    print(f"  Region:       {args.region}")
    print(f"  Scorer:       {args.scorer_model}")
    print(f"  Output:       {args.runs_dir}")
    for v in versions:
        repo_display = v.repo or "*(from config)*"
        model_display = v.executor_model or args.executor_model or "*(from config)*"
        print(f"    [{v.name}]  ref={v.ref}  repo={repo_display}  model={model_display}")

    overall_start = time.monotonic()
    overall_started_at = datetime.now(UTC).isoformat(timespec="seconds")

    # Choose execution mode based on --max-parallel
    if args.max_parallel == 1:
        # Sequential execution (original behavior)
        all_results: list[dict] = []
        for version in versions:
            for scenario in resolved_scenarios:
                for run_idx in range(1, args.runs_per_ref + 1):
                    try:
                        summary = run_single_evaluation(
                            version=version,
                            scenario=scenario,
                            run_index=run_idx,
                            runs_per_ref=args.runs_per_ref,
                            runs_dir=args.runs_dir,
                            base_config=args.config,
                            profile=args.profile,
                            region=args.region,
                            scorer_model=args.scorer_model,
                            default_executor_model=args.executor_model,
                            use_sandbox=args.sandbox,
                        )
                        all_results.append(summary)
                    except Exception as e:
                        print(
                            f"\n[ERROR] Failed version={version.name}, "
                            f"scenario={scenario.name}, run={run_idx}: {e}",
                            file=sys.stderr,
                        )
                        all_results.append({
                            "version_name": version.name,
                            "ref": version.ref,
                            "repo": version.repo,
                            "scenario": scenario.name,
                            "run_index": run_idx,
                            "status": "error",
                            "error": str(e),
                            "output_dir": str(
                                args.runs_dir
                                / f"failed-{ref_to_slug(version.name)}-{scenario.name}-run{run_idx}"
                            ),
                        })
    else:
        # Parallel execution
        work_items = []
        for version in versions:
            for scenario in resolved_scenarios:
                for run_idx in range(1, args.runs_per_ref + 1):
                    work_items.append(WorkItem(
                        version=version,
                        scenario=scenario,
                        run_index=run_idx,
                        runs_per_ref=args.runs_per_ref,
                        runs_dir=args.runs_dir,
                        base_config=args.config,
                        profile=args.profile,
                        region=args.region,
                        scorer_model=args.scorer_model,
                        default_executor_model=args.executor_model,
                        use_sandbox=args.sandbox,
                    ))

        all_results = run_parallel_evaluations(work_items, args.max_parallel)

    overall_elapsed = time.monotonic() - overall_start
    generated_at = datetime.now(UTC).isoformat(timespec="seconds")

    # Write top-level summary
    args.runs_dir.mkdir(parents=True, exist_ok=True)

    # Merge results if incremental mode
    report_version_names = version_names
    report_all_results = all_results
    if existing_summary:
        print("\nMerging results with existing runs...")
        summary_data = merge_summaries(
            existing_summary=existing_summary,
            new_results=all_results,
            new_versions=versions,
            new_elapsed_seconds=overall_elapsed,
        )
        report_version_names = summary_data["version_names"]
        report_all_results = summary_data["runs"]
    else:
        version_specs = [
            {
                "name": v.name,
                "ref": v.ref,
                "repo": v.repo,
                "executor_model": v.executor_model,
            }
            for v in versions
        ]
        summary_data = {
            "started_at": overall_started_at,
            "generated_at": generated_at,
            "total_elapsed_seconds": round(overall_elapsed, 1),
            "version_names": version_names,
            "versions": version_specs,
            "scenarios": [s.name for s in resolved_scenarios],
            "runs_per_version": args.runs_per_ref,
            "total_runs": total_runs,
            "runs_succeeded": sum(1 for r in all_results if r.get("status") == "success"),
            "runs_failed": sum(1 for r in all_results if r.get("status") != "success"),
            "runs": all_results,
        }

    summary_path = args.runs_dir / "git-compare-summary.yaml"
    with open(summary_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(summary_data, f, default_flow_style=False, sort_keys=False)
    print(f"\n  Summary: {summary_path}")

    # Generate all reports (with merged data if incremental)
    print("\nGenerating reports...")
    write_reports(
        runs_dir=args.runs_dir,
        scenarios=[s.name for s in resolved_scenarios],
        version_names=report_version_names,
        all_results=report_all_results,
        generated_at=generated_at,
    )

    # Final summary
    print(f"\n{'=' * 70}")
    print("  Git Compare Complete")
    print(f"{'=' * 70}")
    if existing_summary:
        print(f"  New runs time: {overall_elapsed / 60:.1f} min")
        print(f"  New runs:      {len(all_results)}")
        print(f"  Total versions: {len(report_version_names)} ({len(existing_summary['version_names'])} existing + {len(version_names)} new)")
        print(f"  Total runs:     {len(report_all_results)} ({len(existing_summary['runs'])} existing + {len(all_results)} new)")
        print(f"  Succeeded:      {sum(1 for r in report_all_results if r.get('status') == 'success')}")
        print(f"  Failed:         {sum(1 for r in report_all_results if r.get('status') != 'success')}")
    else:
        print(f"  Total time:  {overall_elapsed / 60:.1f} min")
        print(f"  Total runs:  {len(all_results)}")
        print(f"  Succeeded:   {sum(1 for r in all_results if r.get('status') == 'success')}")
        print(f"  Failed:      {sum(1 for r in all_results if r.get('status') != 'success')}")

    # Show run details (only new runs in incremental mode)
    for r in all_results:
        marker = "PASS" if r.get("status") == "success" else "FAIL"
        duration = r.get("elapsed_seconds", 0) / 60
        print(
            f"    [{marker}] {r['version_name']:30s}  {r['scenario']:15s}  "
            f"run-{r['run_index']}  {duration:.1f} min"
        )
    print(f"\n  Results: {args.runs_dir}")

    # Exit status based on all results (including existing in incremental mode)
    failed = sum(1 for r in report_all_results if r.get("status") != "success")
    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
