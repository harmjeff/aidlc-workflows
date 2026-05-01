# CLAUDE.md — aidlc-evaluator

Agent guidance for working in `scripts/aidlc-evaluator`.

## Security scanning

Run all local scans in one pass before pushing:

```bash
cd scripts/aidlc-evaluator

# Semgrep (matches CI ruleset exactly)
uv run semgrep scan --oss-only --metrics=off --config=r/all \
  --exclude .venv --exclude runs --exclude test_cases

# Bandit (source only, exclude .venv)
uv run bandit -r packages/ scripts/ run.py -ll

# Checkov (IaC/config)
uv run checkov -d . --output cli

# gitleaks (secrets)
gitleaks detect --source . --no-git --config .gitleaks.toml

# Grype (dependency vulnerabilities)
/usr/local/bin/grype dir:. --exclude './.venv' --exclude './runs'

# Markdownlint (source docs only)
npx markdownlint-cli2 "*.md" "docs/*.md" "packages/**/*.md" \
  "!**/.venv/**" "!**/node_modules/**"
```

## Semgrep suppression — CRITICAL

**Always put `# nosemgrep` on the same line as the flagged code.** Preceding-line comments are not reliably associated with new findings in PRs.

Use the **full dotted rule ID**. CI uses `--config=r/all` (full Semgrep registry).

```python
# CORRECT — inline on the flagged line
result = subprocess.run(cmd)  # nosec B603 nosemgrep: python.lang.security.audit.dangerous-subprocess-use-audit.dangerous-subprocess-use-audit

# WRONG — preceding line not reliable for new findings in new files
# nosemgrep: dangerous-subprocess-use-audit
result = subprocess.run(cmd)
```

## Interpreting CI results

The PR check list has TWO semgrep entries:

| Check name | What it is | How to read it |
| ---------- | ---------- | -------------- |
| `semgrep` (security-scanners workflow) | Live scan of the PR diff | **This is the authoritative result** |
| `Semgrep OSS` (Code Scanning) | GitHub's annotation of the SARIF from the previous push | Can show stale findings; ignore if `semgrep` is green |

If `semgrep` passes but `Semgrep OSS` shows findings, the findings are stale from a prior commit. They will clear on the next push that re-uploads a clean SARIF.

## Working location

All changes must be inside `scripts/aidlc-evaluator/`. Verify before committing:

```bash
git diff --name-only main..HEAD | grep -v "^scripts/aidlc-evaluator/"
# Should produce no output
```

## Branch

Active development branch: `fix/evaluator-update` on `harmjeff/aidlc-workflows` fork.
Target: `awslabs/aidlc-workflows` PR #235.
