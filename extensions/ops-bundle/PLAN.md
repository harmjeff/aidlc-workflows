# Plan: `extensions/ops-bundle` — Operational Rules Extension (v2 Format)

## Context

The `ai-dlc-ops` repository (`/home/ec2-user/workplace/ai-dlc-ops`, branch `main`) contains a
comprehensive operational rules framework for aidlc-workflows v1 with 4 domains:
**observability**, **recovery**, **runbooks**, and **deployment**. This plan ports that content
into a v2 extension bundle using the first-class extension mechanism.

Source files live at:
```
git show remotes/origin/main:aidlc-rules/aws-aidlc-rule-details/extensions/observability/
git show remotes/origin/main:aidlc-rules/aws-aidlc-rule-details/extensions/recovery/
git show remotes/origin/main:aidlc-rules/aws-aidlc-rule-details/extensions/runbooks/
git show remotes/origin/main:aidlc-rules/aws-aidlc-rule-details/extensions/deployment/
git show remotes/origin/main:aidlc-rules/aws-aidlc-rule-details/operations/  (workflow overrides)
```

---

## Extension Design

| Field | Value |
|-------|-------|
| Name | `ops-bundle` |
| Version | `0.1.0` |
| requiresBundle | `["core"]` |
| numberRanges | `{ operation: [["4.8", "4.39"]] }` |

**Range rationale**: Core stages occupy indices 1–7 (4.1–4.7). `test-pro` claims 4.40–4.49.
`ops-min` claims 4.50–4.99. Stage graph sorts by `parseInt` on each side of the `.`, so index 8
sorts cleanly after index 7 and before index 40. The float range check (`parseFloat`) gives
`[4.8, 4.39]` which does not overlap test-pro's floor of `4.40`.

Two new stages at `4.8` and `4.9`; indices 10–39 reserved for future growth.

---

## File Tree

```
extensions/ops-bundle/
├── PLAN.md                                      ← this file
├── extension.ts                                 ← manifest
├── stages/
│   └── operation/
│       ├── ops-bundle-rules-validation.md       ← #4.8
│       └── ops-bundle-post-deployment.md        ← #4.9
├── contributions/
│   ├── construction/
│   │   ├── nfr-requirements.md                  ← overlay: domain opt-in + operational NFRs
│   │   ├── nfr-design.md                        ← overlay: domain design enforcement
│   │   └── infrastructure-design.md             ← overlay: deployment design enforcement
│   └── operation/
│       ├── observability-setup.md               ← overlay: AIOBS rules enforcement
│       └── deployment-execution.md              ← overlay: DEPLOY pre-deployment enforcement
└── rules/
    ├── aidlc-ops-bundle-observability.md        ← AIOBS-* (11 source files consolidated)
    ├── aidlc-ops-bundle-recovery.md             ← AIREC-* (5 source files)
    ├── aidlc-ops-bundle-runbooks.md             ← AIRUN-* (6 source files)
    └── aidlc-ops-bundle-deployment.md           ← DEPLOY-* (5 source files)
```

**Total authored files**: 13 (1 manifest + 2 stages + 5 contributions + 4 rule files + this plan)

---

## 1. `extension.ts`

```typescript
import type { ExtensionManifest } from "../../scripts/extension-types.ts";

const extension: ExtensionManifest = {
  name: "ops-bundle",
  version: "0.1.0",
  requiresBundle: ["core"],
  numberRanges: { operation: [["4.8", "4.39"]] },
  contributes: {
    stages: "stages/",
    overlays: "contributions/",
    rules: "rules/",
  },
};

export default extension;
```

---

## 2. Stage: `ops-bundle-rules-validation` (#4.8)

**Purpose**: Read Extension Configuration from `aidlc-docs/aidlc-state.md`, load the rule files
for each enabled ops domain, validate every applicable rule against actual workspace artifacts,
produce a per-domain compliance report.

**Frontmatter**:
- slug: `ops-bundle-rules-validation`
- number: `4.8`
- bundle: `ops-bundle`
- phase: `operation`
- execution: `CONDITIONAL`
- condition: Execute when the ops-bundle is active and at least one domain is enabled
- lead_agent: `aidlc-operations-agent`
- support_agents: `[aidlc-devsecops-agent]`
- mode: `inline`
- produces: `[ops-bundle-validation-report]`
- consumes: `deployment-log` (required), `smoke-test-results` (required), `dashboards` (optional), `alarms` (optional)
- requires_stage: `[deployment-execution, observability-setup]`
- scopes: `[enterprise, feature, infra]`

**Steps**:
1. Load aidlc-operations-agent persona
2. Read Extension Configuration → build active-domain list
3. For each active domain, load `{{HARNESS_DIR}}/rules/aidlc-ops-bundle-<domain>.md`; skip any with answer D
4. Validate every rule against actual code/IaC/design artifacts (compliant → pass; non-compliant → blocking finding)
5. Generate `aidlc-docs/operation/ops-bundle-rules-validation/ops-bundle-validation-report.md`
6. Update state
7. Present completion (blocking findings → "Request Changes" only)

**Domain processing order** (dependency-driven):
1. Observability (prerequisite for runbooks/recovery)
2. Recovery (depends on observability alarms)
3. Runbooks (depends on alarm inventory)
4. Deployment (depends on observability + recovery scopes)

---

## 3. Stage: `ops-bundle-post-deployment` (#4.9)

**Purpose**: Execute the 6-phase post-deployment testing framework ported from the v1 operations
override (`post-deployment-testing.md`).

**Frontmatter**:
- slug: `ops-bundle-post-deployment`
- number: `4.9`
- bundle: `ops-bundle`
- phase: `operation`
- execution: `CONDITIONAL`
- condition: Execute when ops-bundle is active and deployment is complete
- lead_agent: `aidlc-quality-agent`
- support_agents: `[aidlc-operations-agent, aidlc-devsecops-agent]`
- mode: `inline`
- produces: `[ops-bundle-post-deployment-report]`
- consumes: `ops-bundle-validation-report` (required), `deployment-log` (required)
- requires_stage: `[ops-bundle-rules-validation]`
- scopes: `[enterprise, feature, infra]`
- when: `{producer-in-plan: ops-bundle-validation-report}`

**Steps**:
1. Load personas
2. Read deployment outputs
3. Evaluate 6 test phases (Integration, Functional, Non-Functional, Security, Operational Readiness, Production Deployment) — none may be skipped; each is Automatable, Customer-staged, or N/A
4. Execute Automatable phases, record outputs
5. Document Customer-staged phases with instructions
6. Generate report
7. Update state; present completion

---

## 4. Contribution: `contributions/construction/nfr-requirements.md`

**Target**: `nfr-requirements` (construction #3.2, 8 steps)

```yaml
target: nfr-requirements
bundle: ops-bundle
adds:
  produces:
    - ops-bundle-domain-configuration
    - ops-bundle-operational-nfrs
  required_sections:
    - "Operational Domain Configuration"
    - "Operational NFRs"
fragments:
  - anchor: after-step:4
    order: 100
  - anchor: after-step:6
    order: 110
```

**Fragment after-step:4**: Present 4 domain opt-in questions (observability, recovery, runbooks,
deployment) using the A/B/C/D pattern from v1 opt-in files. Record answers in
`aidlc-docs/aidlc-state.md` Extension Configuration table.

**Fragment after-step:6**: For each enabled domain, capture operational NFRs (SLOs/SLIs, on-call
signals, runbook hooks, deployment safety constraints). Write to
`aidlc-docs/construction/{unit-name}/nfr-requirements/ops-bundle-operational-nfrs.md`.

---

## 5. Contribution: `contributions/construction/nfr-design.md`

**Target**: `nfr-design` (construction #3.3, 8 steps)

```yaml
target: nfr-design
bundle: ops-bundle
adds:
  produces:
    - ops-bundle-domain-design-compliance
  required_sections:
    - "Operational Domain Design Compliance"
fragments:
  - anchor: after-step:5
    order: 100
```

**Fragment after-step:5**: For each enabled domain, enforce NFR Design stage requirements from
its rule file (e.g., observability requires KPI derivation, alarm design, quadrant coverage map;
recovery requires MTTR/RTO/RPO per scope; runbooks requires alarm inventory). Produce compliance
documentation.

---

## 6. Contribution: `contributions/construction/infrastructure-design.md`

**Target**: `infrastructure-design` (construction #3.4, 8 steps)

```yaml
target: infrastructure-design
bundle: ops-bundle
adds:
  produces:
    - ops-bundle-deployment-design-compliance
  required_sections:
    - "Deployment Rules Compliance"
fragments:
  - anchor: after-step:5
    order: 100
```

**Fragment after-step:5**: If deployment domain is enabled: enforce DEPLOY-STRAT rules (IaC tool
selection, phased deployment across fault isolation boundaries, alarm-gated validation, automatic
rollback, pipeline rules). Blocking findings prevent stage completion.

---

## 7. Contribution: `contributions/operation/observability-setup.md`

**Target**: `observability-setup` (operation #4.4, 6 steps)

```yaml
target: observability-setup
bundle: ops-bundle
adds:
  produces:
    - ops-bundle-observability-compliance
  required_sections:
    - "AIOBS Rules Compliance"
fragments:
  - anchor: after-step:3
    order: 100
```

**Fragment after-step:3**: If observability domain is enabled: load AIOBS rules and verify design
satisfies all AIOBS-STRAT rules before artifact generation. Blocking findings halt progress.

---

## 8. Contribution: `contributions/operation/deployment-execution.md`

**Target**: `deployment-execution` (operation #4.3, 7 steps)

```yaml
target: deployment-execution
bundle: ops-bundle
adds:
  produces:
    - ops-bundle-deployment-execution-compliance
fragments:
  - anchor: after-step:3
    order: 100
```

**Fragment after-step:3**: If deployment domain is enabled: run DEPLOY-STRAT pre-deployment
checks (IaC present, alarm gates ready, rollback mechanism confirmed, phasing plan verified).
Blocking findings halt at pre-deployment gate.

---

## 9. Rule Files

Each rule file consolidates all source files for its domain into a single file with this structure:

```markdown
# Ops-Bundle: <Domain> Domain Rules

## Conditional Loading
These rules apply ONLY when <Domain> is enabled (Answer A, B, or C).
Answer D or absent: skip and log in audit.md.
Answer C: apply ONLY the ## Custom Rules section.

## Overview
[Condensed from <domain>-baseline.md]

## Blocking Finding Behavior
[Verbatim blocking behavior section with rule IDs]

## Stage Enforcement Table
| Stage | Mandatory |
| NFR Design | ✅ MUST enforce |
| Code Generation | ✅ MUST enforce |
| Operations | ✅ MUST enforce |

## Rules
### <PREFIX> Strategy Rules
[STRAT rules with verification criteria]

### <PREFIX> <Concern> Rules
[Concern-specific rules]

...

## Custom Rules Template
[Template with <PREFIX>-CUSTOM- prefix]
```

### Source file mapping per domain:

**`aidlc-ops-bundle-observability.md`** (source: `extensions/observability/`):
- `observability-baseline.md` — Overview, Stage Enforcement, Blocking Behavior, AIOBS-STRAT-001–005
- `observability-alarms.md` — AIOBS-ALARM-001–005
- `observability-dashboards.md` — AIOBS-DASH-001–018
- `observability-differential.md` — AIOBS-DIFF-001–002, AIOBS-CLIENT-001–003
- `observability-metrics.md` — AIOBS-MET-001–004
- `observability-logging.md` — AIOBS-LOG-001–003
- `observability-tracing.md` — AIOBS-TRACE-000–002
- `observability-llm-rules.md` — AIOBS-LLM-001–004
- `observability-closed-loop.md` — AIOBS-LOOP-001–005 (future capability)
- `observability-custom.md` — Custom rules template

**`aidlc-ops-bundle-recovery.md`** (source: `extensions/recovery/`):
- `recovery-baseline.md` — Overview, AIREC-STRAT rules
- `recovery-instance.md` — Instance-level recovery controls
- `recovery-az.md` — AZ-level recovery controls
- `recovery-region.md` — Region-level recovery controls

**`aidlc-ops-bundle-runbooks.md`** (source: `extensions/runbooks/`):
- `runbooks-baseline.md` — Overview, AIRUN-STRAT rules
- `runbooks-structure.md` — Content/formatting rules
- `runbooks-automation.md` — Automation levels and execution
- `runbooks-security.md` — Security-specific runbook procedures
- `runbooks-custom.md` — Custom template

**`aidlc-ops-bundle-deployment.md`** (source: `extensions/deployment/`):
- `deployment-baseline.md` — Overview, DEPLOY-STRAT rules, DEPLOY-COMP-001
- `deployment-application.md` — Application deployment patterns
- `deployment-pipeline.md` — Pipeline rules (DEPLOY-PIPE-*)
- `deployment-iac.md` — Infrastructure-as-Code rules

---

## Implementation Sequence

1. Write `extension.ts`
2. Write 4 rule files (read source via `git show`, consolidate)
3. Write 2 stage files
4. Write 5 contribution overlay files
5. Bump version (`core/tools/aidlc-version.ts`) + README badge + CHANGELOG
6. Run `bun scripts/package.ts` to regenerate dist/
7. Run `bun scripts/package.ts --check` to verify no drift
8. Run `bash tests/run-tests.sh --smoke` + `--unit`

---

## Verification

```bash
bun scripts/package.ts                    # Build
bun scripts/package.ts --check            # Drift guard
bash tests/run-tests.sh --smoke           # Smoke tests
bash tests/run-tests.sh --unit            # Unit tests (includes t68 version sync)
ls dist/claude/extensions/ops-bundle/     # Confirm presence in all harness dist trees
ls dist/kiro/extensions/ops-bundle/
ls dist/codex/extensions/ops-bundle/
```
