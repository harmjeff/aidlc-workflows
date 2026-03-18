# Stage Plan Base Template

This template provides the base structure for all stage planning documents.

## Template

```markdown
# [Stage Name] Plan

**Created**: [ISO 8601 timestamp]
**Stage**: [Stage name]
**Phase**: [INCEPTION/CONSTRUCTION]
**Status**: [PLANNING/APPROVED/IN PROGRESS/COMPLETE]

---

## Context

**Purpose**: [What this stage accomplishes]

**Prerequisites**:
- [Prerequisite 1]
- [Prerequisite 2]

**Inputs**:
- [Input artifact 1]
- [Input artifact 2]

**Outputs**:
- [Output artifact 1]
- [Output artifact 2]

---

## Steps

### Step 1: [Step Name]
- [ ] [Substep 1.1]
- [ ] [Substep 1.2]
- [ ] [Substep 1.3]

### Step 2: [Step Name]
- [ ] [Substep 2.1]
- [ ] [Substep 2.2]

### Step 3: [Step Name]
- [ ] [Substep 3.1]
- [ ] [Substep 3.2]
- [ ] [Substep 3.3]

[Continue with all steps]

---

## Questions

**CRITICAL**: Questions must be embedded in this plan file using [Answer]: tags.

### Question 1
[Question text]

A) [Option]
B) [Option]
C) [Option]
X) Other (please describe after [Answer]: tag below)

[Answer]: 

---

### Question 2
[Question text]

A) [Option]
B) [Option]
X) Other (please describe after [Answer]: tag below)

[Answer]: 

---

[Continue with all questions]

---

## User Answers

**Status**: [PENDING/COLLECTED/CLARIFIED]

**Answers Collected**: [Timestamp]

**Ambiguities**: [NONE/RESOLVED/PENDING CLARIFICATION]

---

## Artifacts to Generate

Based on the plan and user answers, the following artifacts will be generated:

1. **[Artifact 1 Name]** - `[filename].md`
   - Purpose: [What this artifact contains]
   - Location: `aidlc-docs/[path]/`

2. **[Artifact 2 Name]** - `[filename].md`
   - Purpose: [What this artifact contains]
   - Location: `aidlc-docs/[path]/`

[Continue with all artifacts]

---

## Notes

[Any additional notes, decisions, or context]

---

## Approval

**Approval Status**: [PENDING/APPROVED/CHANGES REQUESTED]

**Approved By**: [User]

**Approved At**: [Timestamp]

**Changes Requested**: [If applicable, list requested changes]

---

**Plan Created By**: AI Assistant
**Last Updated**: [Timestamp]
```

## Checkbox Usage

### Plan-Level Checkboxes

- `[ ]` - Step not yet started
- `[x]` - Step completed
- `[~]` - Step in progress (optional)

**CRITICAL**: Update checkboxes [x] IMMEDIATELY after completing each step in the SAME interaction.

### Two-Level Tracking

1. **Plan-Level** (this file) - Track detailed execution progress
2. **Stage-Level** (aidlc-state.md) - Track overall workflow progress

## Status Values

### Plan Status
- **PLANNING** - Plan being created
- **APPROVED** - User approved the plan
- **IN PROGRESS** - Executing plan steps
- **COMPLETE** - All steps finished

### Answer Status
- **PENDING** - Waiting for user to answer questions
- **COLLECTED** - User provided answers
- **CLARIFIED** - Ambiguities resolved

### Ambiguity Status
- **NONE** - No ambiguities detected
- **RESOLVED** - Ambiguities were found and resolved
- **PENDING CLARIFICATION** - Ambiguities found, waiting for clarification

### Approval Status
- **PENDING** - Waiting for user approval
- **APPROVED** - User approved, can proceed
- **CHANGES REQUESTED** - User wants modifications

## Example: Functional Design Plan

```markdown
# Functional Design Plan - user-service

**Created**: 2026-01-28T15:30:00Z
**Stage**: Functional Design
**Phase**: CONSTRUCTION
**Status**: APPROVED

---

## Context

**Purpose**: Design detailed business logic for the user-service unit

**Prerequisites**:
- Units Generation complete
- Unit definition available
- User stories assigned to this unit

**Inputs**:
- `unit-of-work.md` - Unit definition
- `unit-of-work-story-map.md` - Assigned stories
- `stories.md` - Full story details

**Outputs**:
- `business-logic-model.md` - Core business logic and workflows
- `business-rules.md` - Validation rules and constraints
- `domain-entities.md` - Entity definitions and relationships

---

## Steps

### Step 1: Analyze Unit Context
- [x] Read unit definition from unit-of-work.md
- [x] Read assigned stories from unit-of-work-story-map.md
- [x] Understand unit responsibilities and boundaries

### Step 2: Identify Business Logic Components
- [x] Identify core business workflows
- [x] Identify data transformations
- [x] Identify business processes

### Step 3: Define Domain Model
- [x] Identify domain entities
- [x] Define entity relationships
- [x] Define entity attributes

### Step 4: Document Business Rules
- [x] Identify validation rules
- [x] Identify business constraints
- [x] Identify decision logic

### Step 5: Generate Artifacts
- [ ] Generate business-logic-model.md
- [ ] Generate business-rules.md
- [ ] Generate domain-entities.md

---

## Questions

**CRITICAL**: Questions must be embedded in this plan file using [Answer]: tags.

### Question 1
What user data should be stored in the system?

A) Basic profile only (name, email)
B) Extended profile (name, email, phone, address, preferences)
C) Minimal data (email only for authentication)
D) Other (please describe after [Answer]: tag below)

[Answer]: B

---

### Question 2
Should user passwords be stored or use external authentication?

A) Store hashed passwords in database
B) Use external OAuth providers only
C) Both - allow password or OAuth
D) Other (please describe after [Answer]: tag below)

[Answer]: C

---

## User Answers

**Status**: COLLECTED

**Answers Collected**: 2026-01-28T15:35:00Z

**Ambiguities**: NONE

---

## Artifacts to Generate

Based on the plan and user answers, the following artifacts will be generated:

1. **Business Logic Model** - `business-logic-model.md`
   - Purpose: Core business logic and workflows for user management
   - Location: `aidlc-docs/construction/user-service/functional-design/`

2. **Business Rules** - `business-rules.md`
   - Purpose: Validation rules and business constraints
   - Location: `aidlc-docs/construction/user-service/functional-design/`

3. **Domain Entities** - `domain-entities.md`
   - Purpose: Entity definitions and relationships
   - Location: `aidlc-docs/construction/user-service/functional-design/`

---

## Notes

- User service handles authentication and profile management
- Support both password and OAuth authentication
- Extended profile data required for personalization

---

## Approval

**Approval Status**: APPROVED

**Approved By**: User

**Approved At**: 2026-01-28T15:40:00Z

**Changes Requested**: None

---

**Plan Created By**: AI Assistant
**Last Updated**: 2026-01-28T15:40:00Z
```

## Usage in Detail Files

Reference this template:

```markdown
### Step X: Create [Stage] Plan

**Action:** Create detailed plan with checkboxes

**Template:** See `templates/plans/stage-plan-base.md`

**Customize:**
- Stage name and context
- Steps specific to this stage
- Questions specific to this stage
- Artifacts specific to this stage

**Include:**
- [ ] All steps with checkboxes
- [ ] Context-appropriate questions
- [ ] Expected artifacts
- [ ] Approval section
```

## Critical Rules

1. **Update checkboxes immediately** after completing each step
2. **Embed questions** in plan file with [Answer]: tags
3. **Analyze answers** for ambiguities before proceeding
4. **Get approval** before executing plan
5. **Track progress** at both plan and stage levels
