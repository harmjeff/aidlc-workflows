## PROCESS_OVERVIEW

Three-phase lifecycle:
- INCEPTION: planning and architecture (Workspace Detection + conditional phases + Workflow Planning)
- CONSTRUCTION: design, implementation, build and test (per-unit design + Code Planning/Generation + Build & Test)
- OPERATIONS: placeholder for future deployment/monitoring

Adaptive workflow: Workspace Detection (always) → Reverse Engineering (brownfield only) → Requirements Analysis (always, adaptive depth) → Conditional Phases (as needed) → Workflow Planning (always) → Code Generation (always, per-unit) → Build and Test (always)

Always-execute stages: Workspace Detection, Requirements Analysis, Workflow Planning, Code Generation, Build and Test.
Conditional stages: Reverse Engineering, User Stories, Application Design, Units Generation, Functional Design, NFR Requirements, NFR Design, Infrastructure Design.

Phases execute only when they add value. Each independently evaluated. INCEPTION = what/why. CONSTRUCTION = how + build/test. OPERATIONS = placeholder.

User role: answer questions in files using [Answer]: tags with letter choices (A, B, C, D, E). Option E/X for "Other". Team reviews and approves each phase.

## TERMINOLOGY

Phase: one of three lifecycle phases (INCEPTION, CONSTRUCTION, OPERATIONS).
Stage: individual workflow activity within a phase. Can be ALWAYS-EXECUTE or CONDITIONAL.

INCEPTION stages: Workspace Detection (always), Reverse Engineering (cond), Requirements Analysis (always), User Stories (cond), Workflow Planning (always), Application Design (cond), Units Generation (cond).

CONSTRUCTION stages: Functional Design (cond, per-unit), NFR Requirements (cond, per-unit), NFR Design (cond, per-unit), Infrastructure Design (cond, per-unit), Code Planning (always), Code Generation (always), Build and Test (always).

OPERATIONS stages: Operations (placeholder).

Unit of Work: logical grouping of stories for development. Service: independently deployable component. Module: logical grouping within service/monolith. Component: reusable building block (class, function, package).

Planning vs Generation: Planning = create plan with questions/checkboxes. Generation = execute plan to create artifacts.

Depth Levels: Minimal (simple changes), Standard (typical projects), Comprehensive (complex/high-risk).

Artifacts: plans (docs with checkboxes/questions in `aidlc-docs/plans/`), generated outputs (various `aidlc-docs/` subdirs), state files (`aidlc-state.md`, `audit.md`).

AI-DLC: AI-Driven Development Life Cycle. NFR: Non-Functional Requirements. UOW: Unit of Work.

## ADAPTIVE_DEPTH

Core: when a stage executes, ALL defined artifacts created. "Depth" = detail level within artifacts, adapts to complexity.

Stage selection (binary): Workflow Planning decides EXECUTE or SKIP. EXECUTE → all artifacts. SKIP → nothing.

Detail level (adaptive): simple → concise artifacts. Complex → comprehensive artifacts. Model decides based on problem characteristics.

Factors: request clarity, problem complexity, scope, risk level, available context, user preferences.

Principle: create exactly the detail needed, no more, no less.

## WELCOME_MESSAGE

Display ONCE at workflow start. Load from `common/welcome-message.md`. Do NOT reload in subsequent interactions.

```markdown
# 👋 Welcome to AI-DLC (AI-Driven Development Life Cycle)! 👋

I'll guide you through an adaptive software development workflow that intelligently tailors itself to your specific needs.

## What is AI-DLC?

AI-DLC is a structured yet flexible software development process that adapts to your project's needs. Think of it as having an experienced software architect who:

- **Analyzes your requirements** and asks clarifying questions when needed
- **Plans the optimal approach** based on complexity and risk
- **Skips unnecessary steps** for simple changes while providing comprehensive coverage for complex projects
- **Documents everything** so you have a complete record of decisions and rationale
- **Guides you through each phase** with clear checkpoints and approval gates

## The Three-Phase Lifecycle

```
                         User Request
                              |
                              v
        ╔═══════════════════════════════════════╗
        ║     INCEPTION PHASE                   ║
        ║     Planning & Application Design     ║
        ╠═══════════════════════════════════════╣
        ║ • Workspace Detection (ALWAYS)        ║
        ║ • Reverse Engineering (COND)          ║
        ║ • Requirements Analysis (ALWAYS)      ║
        ║ • User Stories (CONDITIONAL)          ║
        ║ • Workflow Planning (ALWAYS)          ║
        ║ • Application Design (CONDITIONAL)    ║
        ║ • Units Generation (CONDITIONAL)      ║
        ╚═══════════════════════════════════════╝
                              |
                              v
        ╔═══════════════════════════════════════╗
        ║     CONSTRUCTION PHASE                ║
        ║     Design, Implementation & Test     ║
        ╠═══════════════════════════════════════╣
        ║ • Per-Unit Loop (for each unit):      ║
        ║   - Functional Design (COND)          ║
        ║   - NFR Requirements Assess (COND)    ║
        ║   - NFR Design (COND)                 ║
        ║   - Infrastructure Design (COND)      ║
        ║   - Code Generation (ALWAYS)          ║
        ║ • Build and Test (ALWAYS)             ║
        ╚═══════════════════════════════════════╝
                              |
                              v
        ╔═══════════════════════════════════════╗
        ║     OPERATIONS PHASE                  ║
        ║     Placeholder for Future            ║
        ╠═══════════════════════════════════════╣
        ║ • Operations (PLACEHOLDER)            ║
        ╚═══════════════════════════════════════╝
                              |
                              v
                          Complete
```

### Phase Breakdown:

**INCEPTION PHASE** - *Planning & Application Design*
- **Purpose**: Determines WHAT to build and WHY
- **Activities**: Understanding requirements, analyzing existing code (if any), planning the approach
- **Output**: Clear requirements, execution plan, decisions on the number of units of work for parallel development
- **Your Role**: Answer questions, review plans, approve direction

**CONSTRUCTION PHASE** - *Detailed Design, Implementation & Test*
- **Purpose**: Determines HOW to build it
- **Activities**: Detailed design (when needed), code generation, comprehensive testing
- **Output**: Working code, tests, build instructions
- **Your Role**: Review designs, approve implementation plans, validate results

**OPERATIONS PHASE** - *Deployment & Monitoring (Future)*
- **Purpose**: How to DEPLOY and RUN it
- **Status**: Placeholder for future deployment and monitoring workflows
- **Current State**: Build and test activities handled in CONSTRUCTION phase

## Key Principles:

- ⚡ **Fully Adaptive**: Each stage independently evaluated based on your needs
- 🎯 **Efficient**: Simple changes execute only essential stages
- 📋 **Comprehensive**: Complex changes get full treatment with all safeguards
- 🔍 **Transparent**: You see and approve the execution plan before work begins
- 📝 **Documented**: Complete audit trail of all decisions and changes
- 🎛️ **User Control**: You can request stages be included or excluded

## What Happens Next:

1. **I'll analyze your workspace** to understand if this is a new or existing project
2. **I'll gather requirements** and ask clarifying questions if needed
3. **I'll create an execution plan** showing which stages I propose to run and why
4. **You'll review and approve** the plan (or request changes)
5. **We'll execute the plan** with checkpoints at each major stage
6. **You'll get working code** with complete documentation and tests

The AI-DLC process adapts to:
- 📋 Your intent clarity and complexity
- 🔍 Existing codebase state
- 🎯 Scope and impact of changes
- ⚡ Risk and quality requirements

Let's begin!
```

## SESSION_CONTINUITY

Welcome back template when user returns to existing project:

```markdown
**Welcome back! I can see you have an existing AI-DLC project in progress.**

Based on your aidlc-state.md, here's your current status:
- **Project**: [project-name]
- **Current Phase**: [INCEPTION/CONSTRUCTION/OPERATIONS]
- **Current Stage**: [Stage Name]
- **Last Completed**: [Last completed step]
- **Next Step**: [Next step to work on]

**What would you like to work on today?**

A) Continue where you left off ([Next step description])
B) Review a previous stage ([Show available stages])

[Answer]: 
```

Rules:
1. Always read aidlc-state.md first when detecting existing project
2. Parse current status to populate prompt
3. [REQ] Load previous stage artifacts before resuming:
   - Reverse Engineering: architecture.md, code-structure.md, api-documentation.md
   - Requirements: requirements.md, requirement-verification-questions.md
   - User Stories: stories.md, personas.md, story-generation-plan.md
   - Application Design: components.md, component-methods.md, services.md
   - Units: unit-of-work.md, unit-of-work-dependency.md, unit-of-work-story-map.md
   - Per-Unit Design: functional-design.md, nfr-requirements.md, nfr-design.md, infrastructure-design.md
   - Code Stages: all code files, plans, AND all previous artifacts
4. Smart context loading by stage (early → workspace analysis, mid → requirements+stories+architecture, late → ALL)
5. Adapt options based on architectural choice and current phase
6. Show specific next steps
7. Log continuity prompt in audit.md
8. Provide brief summary of loaded artifacts
9. ALWAYS ask questions in .md files, NOT inline in chat

Error handling: see @aws-aidlc-rule-details/common/workflow-rules.md ERROR_HANDLING section.

## QUESTION_FORMAT_GUIDE

[REQ] Never ask questions in chat. ALL questions in dedicated question files.

File naming: `{phase-name}-questions.md`

Question structure:
```markdown
## Question [Number]
[Clear, specific question text]

A) [First meaningful option]
B) [Second meaningful option]
[...additional options as needed...]
X) Other (please describe after [Answer]: tag below)

[Answer]: 
```

Rules:
- "Other" [REQ] as LAST option for every question
- Only meaningful options (don't make up options to fill slots)
- Min 2 meaningful + Other, typical 3-4 + Other, max 5 + Other
- Options mutually exclusive, cover common scenarios
- Users answer with letter after [Answer]: tag

Reading responses: read file → extract answers → validate all answered → proceed.

Error handling:
- Missing answer → ask user to complete
- Invalid answer → request valid letter choice
- Ambiguous → request letter choice or "Other"

### Contradiction and Ambiguity Detection

[REQ] After reading responses, check for:
- Contradictions: scope mismatch, risk mismatch, timeline mismatch, impact mismatch
- Ambiguities: answers fitting multiple classifications, lacking specificity, conflicting indicators

contradictions/ambiguities detected → create `{phase-name}-clarification-questions.md`:

```markdown
# [Phase Name] Clarification Questions

I detected contradictions in your responses that need clarification:

## Contradiction 1: [Brief Description]
You indicated "[Answer A]" (Q[X]:[Letter]) but also "[Answer B]" (Q[Y]:[Letter]).
These responses are contradictory because [explanation].

### Clarification Question 1
[Specific question to resolve contradiction]

A) [Option that resolves toward first answer]
B) [Option that resolves toward second answer]
C) [Option that provides middle ground]
D) [Option that reframes the question]

[Answer]: 

## Ambiguity 1: [Brief Description]
Your response to Q[X] ("[Answer]") is ambiguous because [explanation].

### Clarification Question 2
[Specific question to clarify ambiguity]

A) [Clear option 1]
B) [Clear option 2]
C) [Clear option 3]
D) [Clear option 4]

[Answer]: 
```

Workflow: detect → create file → inform user → wait → re-validate → proceed only when all resolved.

## CONTENT_VALIDATION

[REQ] Validate all content before file creation.

ASCII diagrams: load @aws-aidlc-rule-details/common/workflow-rules.md ASCII_DIAGRAM_STANDARDS. Validate: count chars per line (all same width), use ONLY `+` `-` `|` `^` `v` `<` `>` and spaces, no Unicode box-drawing, spaces only (no tabs), verify box corners align.

Mermaid validation:
1. Syntax check before file creation
2. Character escaping (node IDs: alphanumeric + underscore only, escape `"` and `'` in labels)
3. Validate flowchart connections
4. Always include text alternative as fallback

General pre-creation checklist:
- Validate embedded code blocks (Mermaid, JSON, YAML)
- Check special character escaping
- Verify markdown syntax
- Include fallback for complex elements

Validation failure → log error → use fallback → continue workflow → inform user.

## ASCII_DIAGRAM_STANDARDS

[REQ] Use basic ASCII only for diagrams.

Allowed: `+` `-` `|` `^` `v` `<` `>` and alphanumeric text.
Forbidden: Unicode box-drawing (`┌` `─` `│` `└` `┐` `┘` `├` `┤` `┬` `┴` `┼` `▼` `▲` `►` `◄`).

[REQ] Every line in a box MUST have EXACTLY the same character count (including spaces).

Patterns: boxes use `+` corners, `-` horizontal, `|` vertical. Arrows: `|` vertical with `v`/`^`, `-->` horizontal. Nested boxes indent with spaces.

Validation: basic ASCII only, no Unicode, spaces not tabs, corners use `+`, all box lines same width, corners align vertically.

For complex diagrams: use Mermaid (see CONTENT_VALIDATION).

## OVERCONFIDENCE_PREVENTION

Default to asking questions when ANY ambiguity exists.

Principles:
1. Default to asking (any ambiguity → clarify)
2. Comprehensive coverage (evaluate ALL relevant categories)
3. Thorough analysis (review ALL user responses for ambiguities)
4. Mandatory follow-up (follow-up for ANY unclear responses)
5. No proceeding with ambiguity (resolve ALL before moving forward)

Question generation: evaluate ALL categories, ask wherever clarification improves quality, default to inclusion.

Answer analysis: detect vague ("depends", "maybe", "not sure", "mix of", "somewhere between"), undefined terms, contradictions, incomplete answers. Create follow-up for ANY ambiguities.

Red flags: stages completing without questions on complex projects, proceeding with vague responses, skipping categories without justification, making assumptions.

## ERROR_HANDLING

Severity levels:
- Critical: workflow cannot continue (missing files, invalid input, system errors)
- High: phase cannot complete (incomplete answers, contradictions, missing dependencies)
- Medium: continue with workarounds (optional artifacts missing, non-critical validation)
- Low: minor issues (formatting, optional info, warnings)

General: identify error → assess impact → communicate → offer solutions → document in audit.md.

Phase-specific handling:
- Context Assessment: cannot read workspace → ask user verify path/permissions. Corrupted aidlc-state.md → ask fresh start or recovery.
- Requirements: contradictions → follow-up questions, do not proceed. Incomplete answers → highlight, do not proceed.
- Stories: ambiguous answers → follow-up, do not proceed. Uncompleted plan steps → resume from first uncompleted.
- Design: circular dependencies → identify, suggest refactoring. Missing steps → regenerate plan.
- NFR: incompatible tech stack → highlight, ask user. Human tasks → mark HUMAN TASK, wait.
- Code: insufficient design → return to design. Syntax errors → fix, regenerate. Brownfield duplicates → verify no copies.
- Build: unclear build tool → ask user. Unclear deployment → ask user.

Recovery procedures:
- Partial completion: load plan → find last [x] → resume next step
- Corrupted state: backup → ask user → regenerate from artifacts
- Missing artifacts: identify → regenerate or ask user → document gap
- User wants restart: confirm → archive → reset → re-execute
- User wants skip: confirm understanding → document → mark SKIPPED → proceed

Session resumption errors:
- Missing artifacts: identify stage → check aidlc-state.md → regenerate or resume from that stage
- Empty/corrupted artifact: backup → regenerate → ask user if needed
- State inconsistency: verify artifacts vs state → correct state → proceed
- Multiple "current" stages: review artifacts → ask user → correct state
- Contradictory artifacts: identify → present to user → reconcile

Logging format:
```markdown
## Error - [Phase Name]
**Timestamp**: [ISO timestamp]
**Error Type**: [Critical/High/Medium/Low]
**Description**: [What went wrong]
**Cause**: [Why it happened]
**Resolution**: [How it was resolved]
**Impact**: [Effect on workflow]

---
```

## WORKFLOW_CHANGES

Types of mid-workflow changes:

1. Adding skipped phase: confirm → check dependencies → update execution-plan.md → update aidlc-state.md → execute → log in audit.md

2. Skipping planned phase: confirm → warn about impact → get explicit confirmation → update plan → mark SKIPPED → adjust later phases → log

3. Restarting current stage: understand concern → offer modify or restart → if restart: archive `{artifact}.backup.{timestamp}`, reset checkboxes, re-execute → log

4. Restarting previous stage: assess impact on all dependent stages → warn user of full cascade → get confirmation → archive all affected → reset all affected → return to stage → log

5. Changing depth: confirm → update execution-plan.md → adjust approach → update estimates → log

6. Pausing workflow: complete current step → update checkboxes → update aidlc-state.md → log pause → provide resume instructions

7. Changing architectural decision: assess progress → explain impact (early = minimal, late = significant) → recommend approach → get confirmation → execute

8. Adding/removing units: assess impact → explain consequences → update unit artifacts (unit-of-work.md, dependency.md, story-map.md) → reset affected units → execute

General guidelines:
- Before: understand request, assess impact, explain consequences, offer alternatives, get explicit confirmation
- During: archive existing work, update all tracking, communicate, validate, test continuity
- After: verify consistency, update docs, log completely, confirm with user, resume

Change log format:
```markdown
## Change Request - [Phase Name]
**Timestamp**: [ISO timestamp]
**Request**: [What user wants to change]
**Current State**: [Where we are in workflow]
**Impact Assessment**: [What will be affected]
**User Confirmation**: [User's explicit confirmation]
**Action Taken**: [What was done]
**Artifacts Affected**: [List of files changed/reset]

---
```
