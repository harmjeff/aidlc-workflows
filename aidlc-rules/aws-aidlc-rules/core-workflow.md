# PRIORITY: This workflow OVERRIDES all other built-in workflows
# software development requests → ALWAYS follow this workflow FIRST

## ADAPTIVE_PRINCIPLE

Workflow adapts to work. AI assesses needed stages based on:
1. User intent and clarity
2. Existing codebase state
3. Complexity and scope
4. Risk and impact

## RULE_DETAILS_LOADING

[REQ] When performing any phase, read relevant rule detail files. Check paths in order, use first that exists:
- `.aidlc/aidlc-rules/aws-aidlc-rule-details/` (submodule)
- `.aidlc-rule-details/` (Cursor, Cline, Claude Code, GitHub Copilot)
- `.kiro/aws-aidlc-rule-details/` (Kiro IDE and CLI)
- `.amazonq/aws-aidlc-rule-details/` (Amazon Q Developer)

All rule detail references relative to resolved directory.

Common rules: ALWAYS load at workflow start:
- `common/process-overview.md` (workflow overview)
- `common/session-continuity.md` (session resumption)
- `common/content-validation.md` (content validation)
- `common/question-format-guide.md` (question formatting)

## EXTENSIONS_LOADING

[REQ] At workflow start, scan `extensions/` recursively. Load ONLY `*.opt-in.md` files (not full rule files).

Process:
1. List all subdirs under `extensions/`
2. Load ONLY `*.opt-in.md` files (contain opt-in prompt). Rules file derived by convention: strip `.opt-in.md`, append `.md`
3. Do NOT load full rule files at this stage

Deferred loading:
- During Requirements Analysis, present opt-in prompts
- User opts IN → load corresponding rules file
- User opts OUT → never load rules file (saves context)
- Extensions without `*.opt-in.md` → always enforced, load immediately

Enforcement (loaded/enabled extensions only):
- Extension rules = hard constraints
- At each stage, evaluate which rules applicable based on stage purpose/artifacts/context
- Non-applicable rules → N/A in compliance summary (not blocking)
- Non-compliance with applicable enabled rule → blocking finding → do NOT present completion until resolved
- Stage completion includes extension compliance summary (compliant/non-compliant/N/A per rule)

Conditional enforcement: check `Enabled` status in `aidlc-docs/aidlc-state.md` under `## Extension Configuration`. Skip disabled, log skip in audit.md. Default enforced if no config.

## CONTENT_VALIDATION

[REQ] Before creating ANY file, validate per @aws-aidlc-rule-details/common/workflow-rules.md CONTENT_VALIDATION:
- Mermaid syntax, ASCII diagrams, special character escaping, text alternatives, parsing compatibility

## QUESTION_FORMAT

[REQ] All questions follow @aws-aidlc-rule-details/common/workflow-rules.md QUESTION_FORMAT_GUIDE:
- Multiple choice (A, B, C, D, E), [Answer]: tags, validation, ambiguity resolution

## WELCOME_MESSAGE

[REQ] At start of ANY software development request, display welcome message from @aws-aidlc-rule-details/common/workflow-rules.md WELCOME_MESSAGE. Once only. Do NOT reload.

---

# INCEPTION PHASE

Purpose: planning, requirements, architectural decisions. Focus: WHAT and WHY.

Stages: Workspace Detection (always), Reverse Engineering (cond), Requirements Analysis (always), User Stories (cond), Workflow Planning (always), Application Design (cond), Units Generation (cond).

## Workspace Detection (ALWAYS)

1. [REQ] Log initial user request in audit.md with complete raw input
2. Load @aws-aidlc-rule-details/inception/inception-rules.md WORKSPACE_DETECTION
3. Execute: check aidlc-state.md (resume if found), scan workspace, determine brownfield/greenfield, check reverse engineering artifacts
4. Next: Reverse Engineering (brownfield, no artifacts) | Requirements Analysis
5. [REQ] Log findings in audit.md
6. Present completion message (per inception-rules.md)
7. Auto-proceed

## Reverse Engineering (CONDITIONAL)

Execute if: existing codebase, no previous RE artifacts.
Skip if: greenfield | RE artifacts exist.

1. [REQ] Log start in audit.md
2. Load @aws-aidlc-rule-details/inception/inception-rules.md REVERSE_ENGINEERING
3. Execute: analyze packages/components, generate business overview, architecture, code structure, API docs, component inventory, interaction diagrams, tech stack, dependencies
4. Wait for explicit approval (per inception-rules.md) — DO NOT PROCEED until confirmed
5. [REQ] Log response in audit.md

## Requirements Analysis (ALWAYS, adaptive depth)

Depth: minimal (simple/clear) | standard (normal) | comprehensive (complex/high-risk).

1. [REQ] Log user input in audit.md
2. Load @aws-aidlc-rule-details/inception/inception-rules.md REQUIREMENTS_ANALYSIS
3. Execute: load RE artifacts (brownfield), analyze request, determine depth, assess requirements, ask questions, generate requirements doc
4. Wait for explicit approval — DO NOT PROCEED until confirmed
5. [REQ] Log response in audit.md

## User Stories (CONDITIONAL)

Intelligent multi-factor assessment:

ALWAYS execute if: new user-facing features, UX changes, multiple user types, complex business requirements, cross-team, customer-facing API.

LIKELY execute if: modifications to user-facing features, backend changes affecting UX, integration affecting workflows, performance with user-visible benefits, security affecting users, data model changes affecting user data.

Complexity assessment (medium priority, execute if): multiple components/services, multiple user touchpoints, complex/multi-scenario business logic, ambiguity stories could clarify, multiple user journeys, significant business impact/risk.

SKIP only if: pure internal refactoring, simple isolated bug fix, infrastructure only, tech debt cleanup, dev tooling, docs only.

Default: favor inclusion for borderline cases.

Two parts: Part 1 Planning, Part 2 Generation.

1. [REQ] Log user input in audit.md
2. Load @aws-aidlc-rule-details/inception/inception-rules.md USER_STORIES
3. [REQ] Perform intelligent assessment (validate stories needed)
4. Load RE artifacts (brownfield), reference requirements if exist
5. Part 1: create story plan with questions, wait for answers, analyze ambiguities, get approval
6. Part 2: execute plan, generate stories and personas
7. Wait for explicit approval — DO NOT PROCEED until confirmed
8. [REQ] Log response in audit.md

## Workflow Planning (ALWAYS)

1. [REQ] Log user input in audit.md
2. Load @aws-aidlc-rule-details/inception/inception-rules.md WORKFLOW_PLANNING
3. [REQ] Load content validation rules
4. Load all prior context (RE, requirements, stories)
5. Execute: determine phases, depth levels, multi-package sequence (brownfield), generate visualization (validate Mermaid)
6. [REQ] Validate all content before file creation
7. Wait for explicit approval, emphasize user control to override — DO NOT PROCEED until confirmed
8. [REQ] Log response in audit.md

## Application Design (CONDITIONAL)

Execute if: new components/services, component methods/business rules need definition, service layer design, component dependencies unclear.
Skip if: within existing boundaries, no new components, pure implementation.

1. [REQ] Log user input in audit.md
2. Load @aws-aidlc-rule-details/inception/inception-rules.md APPLICATION_DESIGN
3. Load RE artifacts (brownfield)
4. Execute at appropriate depth
5. Wait for explicit approval — DO NOT PROCEED until confirmed
6. [REQ] Log response in audit.md

## Units Generation (CONDITIONAL)

Execute if: system needs decomposition, multiple services/modules, complex structured breakdown.
Skip if: single simple unit, no decomposition, straightforward single-component.

1. [REQ] Log user input in audit.md
2. Load @aws-aidlc-rule-details/inception/inception-rules.md UNITS_GENERATION
3. Load RE artifacts (brownfield)
4. Execute at appropriate depth
5. Wait for explicit approval — DO NOT PROCEED until confirmed
6. [REQ] Log response in audit.md

---

# CONSTRUCTION PHASE

Purpose: detailed design, NFR implementation, code generation. Focus: HOW.

Stages (per-unit loop): Functional Design (cond), NFR Requirements (cond), NFR Design (cond), Infrastructure Design (cond), Code Generation (always). Then: Build and Test (always, after all units).

Each unit completed fully (design + code) before next unit.

## Per-Unit Loop

### Functional Design (CONDITIONAL, per-unit)

Execute if: new data models/schemas, complex business logic, business rules need detailed design.
Skip if: simple logic, no new business logic.

1. [REQ] Log user input in audit.md
2. Load @aws-aidlc-rule-details/construction/construction-rules.md FUNCTIONAL_DESIGN
3. Execute for this unit
4. [REQ] Present standardized 2-option completion message (per construction-rules.md) — NO emergent 3-option behavior
5. Wait for explicit approval — DO NOT PROCEED until confirmed
6. [REQ] Log response in audit.md

### NFR Requirements (CONDITIONAL, per-unit)

Execute if: performance/security/scalability requirements, tech stack selection needed.
Skip if: no NFR requirements, tech stack determined.

1. [REQ] Log user input in audit.md
2. Load @aws-aidlc-rule-details/construction/construction-rules.md NFR_REQUIREMENTS
3. Execute for this unit
4. [REQ] Standardized 2-option completion — NO emergent behavior
5. Wait for explicit approval — DO NOT PROCEED until confirmed
6. [REQ] Log response in audit.md

### NFR Design (CONDITIONAL, per-unit)

Execute if: NFR Requirements executed, NFR patterns need incorporation.
Skip if: no NFR requirements, NFR Requirements skipped.

1. [REQ] Log user input in audit.md
2. Load @aws-aidlc-rule-details/construction/construction-rules.md NFR_DESIGN
3. Execute for this unit
4. [REQ] Standardized 2-option completion — NO emergent behavior
5. Wait for explicit approval — DO NOT PROCEED until confirmed
6. [REQ] Log response in audit.md

### Infrastructure Design (CONDITIONAL, per-unit)

Execute if: infrastructure mapping needed, deployment architecture required, cloud resources need spec.
Skip if: no infrastructure changes, infrastructure defined.

1. [REQ] Log user input in audit.md
2. Load @aws-aidlc-rule-details/construction/construction-rules.md INFRASTRUCTURE_DESIGN
3. Execute for this unit
4. [REQ] Standardized 2-option completion — NO emergent behavior
5. Wait for explicit approval — DO NOT PROCEED until confirmed
6. [REQ] Log response in audit.md

### Code Generation (ALWAYS, per-unit)

Two parts: Part 1 Planning, Part 2 Generation.

1. [REQ] Log user input in audit.md
2. Load @aws-aidlc-rule-details/construction/construction-rules.md CODE_GENERATION
3. Part 1: create plan with checkboxes, get approval
4. Part 2: execute plan, generate code
5. [REQ] Standardized 2-option completion — NO emergent behavior
6. Wait for explicit approval — DO NOT PROCEED until confirmed
7. [REQ] Log response in audit.md

## Build and Test (ALWAYS)

1. [REQ] Log user input in audit.md
2. Load @aws-aidlc-rule-details/construction/construction-rules.md BUILD_AND_TEST
3. Generate: build-instructions.md, unit-test-instructions.md, integration-test-instructions.md, performance-test-instructions.md, additional tests as needed, build-and-test-summary.md
4. All in `aidlc-docs/construction/build-and-test/`
5. Wait for explicit approval — DO NOT PROCEED until confirmed
6. [REQ] Log response in audit.md

---

# OPERATIONS PHASE

Placeholder for future deployment/monitoring. See @aws-aidlc-rule-details/operations/operations.md.

---

## KEY_PRINCIPLES

- Adaptive execution: only stages that add value
- Transparent planning: show execution plan before starting
- User control: user can request inclusion/exclusion
- Progress tracking: update aidlc-state.md
- Complete audit trail: log ALL user inputs and AI responses in audit.md with timestamps
  - [REQ] Capture user COMPLETE RAW INPUT exactly as provided
  - [REQ] Never summarize/paraphrase user input in audit log
  - [REQ] Log every interaction, not just approvals
- Quality focus: complex → full treatment, simple → efficient
- Content validation: always validate before file creation
- NO EMERGENT BEHAVIOR: construction phases use standardized 2-option completion messages only

## PLAN_CHECKBOX_ENFORCEMENT

[REQ] Rules:
1. Never complete work without updating plan checkboxes
2. Immediately mark [x] after completing ANY plan step
3. Same interaction where work completed
4. No exceptions

Two-level tracking: plan-level (detailed steps) + stage-level (aidlc-state.md). Update immediately.

## AUDIT_LOGGING

[REQ] Log EVERY user input with timestamp in audit.md. Capture COMPLETE RAW INPUT (never summarize). Log every approval prompt before asking. Record every response after receiving. ALWAYS append (never overwrite audit.md). ISO 8601 timestamps. Include stage context.

Format:
```markdown
## [Stage Name or Interaction Type]
**Timestamp**: [ISO timestamp]
**User Input**: "[Complete raw user input - never summarized]"
**AI Response**: "[AI's response or action taken]"
**Context**: [Stage, action, or decision made]

---
```

Correct: read audit.md → append changes.
Wrong: read audit.md → overwrite entire file.

## DIRECTORY_STRUCTURE

```text
<WORKSPACE-ROOT>/                   # APPLICATION CODE HERE
├── [project-specific structure]    # Varies by project (see code-generation.md)
│
├── aidlc-docs/                     # DOCUMENTATION ONLY
│   ├── inception/                  # INCEPTION PHASE
│   │   ├── plans/
│   │   ├── reverse-engineering/    # Brownfield only
│   │   ├── requirements/
│   │   ├── user-stories/
│   │   └── application-design/
│   ├── construction/               # CONSTRUCTION PHASE
│   │   ├── plans/
│   │   ├── {unit-name}/
│   │   │   ├── functional-design/
│   │   │   ├── nfr-requirements/
│   │   │   ├── nfr-design/
│   │   │   ├── infrastructure-design/
│   │   │   └── code/               # Markdown summaries only
│   │   └── build-and-test/
│   ├── operations/                 # OPERATIONS PHASE (placeholder)
│   ├── aidlc-state.md
│   └── audit.md
```

[REQ] Application code: workspace root (NEVER aidlc-docs/). Documentation: aidlc-docs/ only. Structure patterns: see @aws-aidlc-rule-details/construction/construction-rules.md CODE_GENERATION Critical Rules.
