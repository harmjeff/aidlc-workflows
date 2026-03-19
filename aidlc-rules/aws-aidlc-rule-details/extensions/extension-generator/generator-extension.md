# Extension Generator Extension

**Extension**: extension-generator v1.2.0 | **One-time per invocation** | **IDE-Agnostic**

## Purpose

Generates lazy-loaded, phase-specific AI-DLC extension files from compliance frameworks or user-provided rules. Each control is classified to only the phases where it produces actionable guidance — keeping the context window lean at runtime.

**How it works**: Read source data → classify to phases → generate per-phase files → produce lazy-loading manifest → output to `aidlc-docs/extensions/`.

**Context behavior**: Loads once, generates, exits. Does not persist between stages.

**Activation**: Gated by `extension-generator.opt-in.md` during Requirements Analysis.

**Exception**: The security baseline (`community-extensions/security/baseline/`) is cross-cutting and loaded directly by the core workflow — not processed by this generator.

---

## Entry Point

### Recommended Path (opt-in answer A)

1. **Scan `extensions/`** for any extension with `depends_on: ["extension-generator"]` in its manifest — these need phase files generated.
2. **Analyze project context** for domain keywords:
   - Financial/banking/payments → PCI-DSS, SOC 2
   - Healthcare/medical/patient → HIPAA
   - EU users/EU data → GDPR
   - Government/federal → FedRAMP, NIST 800-53
   - General web/API → OWASP Top 10
3. **Present recommendations** including installed extensions needing phase files:

```markdown
Based on your project context, we recommend:

[List extensions with rationale]

A) Use these recommended extensions
B) Modify recommendations
C) Skip extension generation

[Answer]:
```

### Manual Path (opt-in answer B)

```markdown
**How would you like to create your extension?**
A) Name a compliance standard (HIPAA, PCI-DSS, NIST 800-53, etc.)
B) Point me to folder(s) with existing rule docs
C) Describe your rules (see User-Provided Rules below for accepted formats)
D) Generate phase files from an installed extension

[Answer]:
```

**Option A**: Compliance → load `ccm-reference.md` → Scoping Questions → Generate.
**Option B**: Read `.md`, `.txt`, `.yaml`, `.json` files (skip binaries, >100KB). No PDFs — ask user to convert. Classify rule type → Scoping Questions → Generate.
**Option C**: Classify rule type → Scoping Questions → Generate.
**Option D**: Scan `extensions/` for `depends_on: ["extension-generator"]` → Compliance Extension Processing.

---

## Rule Type Classification

| Rule Type | Category | CCM? | Examples |
|-----------|----------|------|----------|
| Compliance/Security | `compliance` | Yes — load `ccm-reference.md` | HIPAA, PCI-DSS, GDPR, NIST, OWASP |
| Coding Standards | `quality` | No | Style guides, linting rules, naming conventions |
| Business Rules | `process` | No | Approval workflows, SLA requirements |
| Architecture | `architecture` | No | API patterns, service boundaries |
| Team Process | `process` | No | PR review rules, branching strategy |

**Mixed inputs**: Split into separate extensions by type. Don't force non-compliance rules through CCM.

---

## Scoping Questions

### All types
1. **Strictness**: Maximum (all MUST) / Balanced (critical=MUST, others=SHOULD) / Advisory (all SHOULD/MAY)
2. **Phases**: All (recommended), or user picks specific phases

### Compliance/Security — also ask:
3. App type, Language(s), Cloud platform
4. Standard-specific: data/assets in scope, compliance tier

### Coding/Architecture — also ask:
3. Language(s), App type, Cloud platform (if relevant)

### Business/Process — no additional questions.

---

## Compliance Extension Processing

For installed extensions with `depends_on: ["extension-generator"]` (Option D or detected in Recommended Path).

### Step 1: Discover

Scan `{rule-details-dir}/extensions/` for manifests with `depends_on: ["extension-generator"]`.

```markdown
**Extensions requiring phase-file generation:**

| # | Extension | Category | Controls File | Status |
|---|-----------|----------|---------------|--------|
| 1 | nist-800-53 | compliance | nist-800-53-controls.md | Needs phase files |

Select extensions (comma-separated numbers, or A for all):
[Answer]:
```

### Step 2: Classify Controls to Phases

Read the controls file. For each control, assign to phases based on:

| Control Characteristic | Phases | Why |
|---|---|---|
| Access enforcement, authorization | requirements, design, code-guidelines, testing | Architecture + IAM code + verification |
| Logging, monitoring, audit trails | design, infrastructure, testing | Log architecture + service config + verification |
| Encryption, key management | requirements, design, infrastructure, code-guidelines, testing | Every layer |
| Preventive controls (SCP, policies) | design, infrastructure, code-guidelines | Constraints + IaC + policy-as-code |
| Detective controls (Security Hub) | infrastructure, testing | Service enablement + verification |
| Network controls | design, infrastructure, nfr-additions | Patterns + config |
| Data classification, privacy | requirements, stories, design | Requirements + data flow |
| Backup, recovery | nfr-additions, infrastructure, testing | RTO/RPO + config + recovery testing |

**Principle**: Only assign to phases with actionable output. If a control only affects infra, it goes in `infrastructure.md` only.

### Step 3: Scoping Questions

Same as above — strictness, phases, app type, language, cloud platform.

### Step 4: Generate Phase Files

Generate only files for phases with assigned controls using the Universal Template (below).

Example — NIST 800-53 AC controls:

| Control | requirements | design | infrastructure | code-guidelines | testing |
|---|---|---|---|---|---|
| AC-3 (Access Enforcement) | ✓ | ✓ | ✓ | ✓ | ✓ |
| AC-6(1) (Least Privilege) | ✓ | ✓ | ✓ | ✓ | ✓ |
| AC-6(9) (Log Privileged Functions) | | ✓ | ✓ | | ✓ |

Files not needed (`stories.md`, `nfr-additions.md`) are never created.

### Step 5: Generate Manifest

Create `rule-manifest.yaml` in the output directory referencing only generated files:

```yaml
applies_to:
  inception:
    - stage: "requirements-analysis"
      file: "requirements.md"
      action: "append"
    - stage: "application-design"
      file: "design.md"
      action: "append"
  construction:
    - stage: "infrastructure-design"
      file: "infrastructure.md"
      action: "append"
    - stage: "code-generation"
      file: "code-guidelines.md"
      action: "append"
    - stage: "build-and-test"
      file: "testing.md"
      action: "append"
```

**Critical**: Manifest MUST NOT reference nonexistent files. At runtime each stage loads only its file — the original controls data is never loaded.

### Step 6: Review

Show: generated files, controls per file, strictness, CCM domains. Offer: **approve** / **change** / **discard**.

---

## Output Location

All generated output goes to `aidlc-docs/extensions/[category]/[standard-name]/`:

```
aidlc-docs/extensions/compliance/nist-800-53/
├── rule-manifest.yaml     # Lazy-loading phase mappings
├── overview.md            # Scope, sources, CCM domains
├── ccm-mapping.md         # Framework ↔ CCM crosswalk (compliance only)
├── requirements.md        # Only if controls map here
├── design.md              # Only if controls map here
├── infrastructure.md      # Only if controls map here
├── code-guidelines.md     # Only if controls map here
└── testing.md             # Only if controls map here
```

Source data stays in `extensions/` (installed from `community-extensions/`). Runtime output lives in `aidlc-docs/extensions/`.

---

## Universal Template

All generated phase files follow this pattern:

```markdown
## [Standard] - {STAGE} Guidelines

**Extension**: [name] v[version] | **Applies To**: {STAGE} | **Type**: [type]

---

### {CONTENT_TYPE}

#### [Control Area]: [Name]

**Reference**: [Control ID, e.g., "NIST AC-3" or "STYLE-03"]
**CCM Mapping**: [CCM Domain-ID] ← compliance only

- [MUST/SHOULD/MAY] [Specific actionable item]

### {STAGE}-Specific Additions

[Phase-specific content per substitution table]

### Checklist

- [ ] [Verifiable item]
```

**Substitution table**:

| File | {STAGE} | {CONTENT_TYPE} | Additions |
|------|---------|---------------|-----------|
| requirements.md | Requirements Analysis | Requirements | Clarifying questions |
| stories.md | User Stories | Acceptance Criteria | User stories |
| design.md | Design | Architectural Constraints | Patterns/anti-patterns tables |
| nfr-additions.md | NFR | NFR Additions | Metrics, tool requirements |
| infrastructure.md | Infrastructure | Infrastructure Requirements | Cloud service requirements table |
| code-guidelines.md | Code Generation | Coding Requirements | Code examples (3-8 lines, user's language) |
| testing.md | Build and Test | Testing Requirements | Scans/tools, test scenarios, CI/CD gates |

---

## User-Provided Rules (Future — Currently Planned)

The generator will support converting user-provided rules into the same lazy-loaded extension format. This section documents what will be accepted and how it works.

### Accepted Input Formats

| Format | How to provide | What the generator does |
|---|---|---|
| **Markdown files** (`.md`) | Point to folder (Option B) | Reads, classifies rule type, generates phase files |
| **Plain text** (`.txt`) | Point to folder (Option B) | Same as markdown — parsed for rule patterns |
| **YAML/JSON** (`.yaml`, `.json`) | Point to folder (Option B) | Reads structured rules, maps to phases |
| **Verbal description** | Describe in chat (Option C) | Asks clarifying questions, generates rules |
| **Existing style guides** | Point to folder (Option B) | Extracts rules, assigns IDs (e.g., STYLE-01) |
| **Wiki/docs exports** | Point to folder (Option B) | Reads, structures into extension format |

### What the Generator Produces

For non-compliance rules, the generator:
1. **Assigns rule IDs** — e.g., `STYLE-01`, `BIZ-03`, `ARCH-02`, `PROC-01`
2. **Classifies to phases** — coding standards → `code-guidelines.md`; architecture rules → `design.md`; process rules → `requirements.md`
3. **Generates lazy-loaded files** — same manifest structure, same per-phase loading
4. **No CCM mapping** — uses the rule's own categorization instead

### Rule Type Examples

**Coding standards** → primarily `code-guidelines.md`, possibly `testing.md`:
- "Use 2-space indentation" → `STYLE-01` in `code-guidelines.md`
- "All functions must have JSDoc" → `STYLE-02` in `code-guidelines.md`

**Business rules** → primarily `requirements.md`, possibly `design.md`:
- "Loan amounts > $50K require manager approval" → `BIZ-01` in `requirements.md`
- "All PII must be masked in logs" → `BIZ-02` in `requirements.md` + `code-guidelines.md`

**Architecture patterns** → primarily `design.md`, possibly `infrastructure.md`:
- "All services must use event-driven communication" → `ARCH-01` in `design.md`
- "Database per service, no shared databases" → `ARCH-02` in `design.md` + `infrastructure.md`

**Team process** → primarily `requirements.md`:
- "All PRs require 2 approvals" → `PROC-01` in `requirements.md`
- "Feature branches must include ticket ID" → `PROC-02` in `requirements.md`

---

## Content Quality Rules

1. **Traceable**: Compliance = framework ref + CCM ID. Non-compliance = own rule IDs
2. **Specific**: Actionable items only — not "ensure quality"
3. **Real references**: Actual control/rule IDs, no vague pointers
4. **Tailored**: Code examples match user's language, infra matches cloud platform
5. **Strictness-aware**: MUST/SHOULD/MAY per scoping answer
6. **Verifiable checklists**: Every `- [ ]` is pass/fail
7. **Code in code-guidelines.md only**: Other files = guidance, not code
8. **Gaps documented**: Unmapped compliance controls go in `ccm-mapping.md`
9. **Baseline dedup**: Overlap with security-baseline → reference its rule ID

---

## Edge Cases

- **No tools available**: Use CCM mappings + training data + official URLs. Tell user to verify.
- **Unknown standard**: Ask for docs/description. Map to CCM where possible.
- **Existing output**: Ask user — overwrite, keep, or cancel. Never silently overwrite.
- **Broad standard** (NIST 800-53): Ask which control families matter. Suggest focused subset.
- **Multiple standards**: Separate extensions, note shared CCM domains for overlap.
- **No CCM mapping**: Manual map to closest domains, confidence = Medium/Low, document rationale.
- **Incomplete/contradictory docs**: Clarify, map what exists, note gaps or ask precedence.
- **Partial phase files exist**: Offer to generate missing ones or regenerate all.

---

*v1.2.0 — Compliance extension processing with lazy loading. User-provided rules documented for future implementation.*
