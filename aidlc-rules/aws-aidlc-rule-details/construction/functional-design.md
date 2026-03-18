# Functional Design Stage

**Purpose:** Design detailed business logic, domain models, and business rules for a specific unit of work.

**Stage Type:** CONDITIONAL (per-unit)

**Phase:** CONSTRUCTION

**Load this file when:** Starting Functional Design stage for a unit

**Unload this file after:** Functional Design stage completes and user approves

---

## Execute IF

Execute this stage if ANY of the following conditions are met:
- New data models or schemas need to be defined
- Complex business logic needs detailed design
- Business rules need explicit definition and documentation
- Domain entities and their relationships need clarification

## Skip IF

Skip this stage if ALL of the following conditions are met:
- Simple logic changes only
- No new business logic to design
- No new data models or entities
- Business rules are already well-defined

---

## Prerequisites

Before starting this stage, ensure:
1. Unit of work is defined in `unit-of-work.md`
2. Unit story mapping exists in `unit-of-work-story-map.md`
3. Application design artifacts exist (if Application Design stage was executed)
4. Requirements and user stories are available (if those stages were executed)

---

## Detailed Steps

### Step 1: Log User Input
**Action:** Log any user input during this stage in `audit.md`.

**Template:** `../../templates/audit-logs/basic-entry.md`

**Log with:**
- Stage: Functional Design - [unit-name]
- Complete raw user input (never summarize)
- ISO 8601 timestamp

### Step 2: Load Unit Context
**Action:** Read and analyze the following artifacts to understand the unit:

**Required Artifacts:**
- `aidlc-docs/inception/application-design/unit-of-work.md` - Unit definition
- `aidlc-docs/inception/application-design/unit-of-work-story-map.md` - Assigned stories

**Optional Artifacts (if they exist):**
- `aidlc-docs/inception/reverse-engineering/` - Existing codebase context
- `aidlc-docs/inception/requirements/requirements.md` - Requirements
- `aidlc-docs/inception/user-stories/stories.md` - User stories
- `aidlc-docs/inception/application-design/` - Component and service definitions

### Step 3: Understand Unit Responsibilities
**Action:** Analyze the unit to understand:
- Unit name, description, and scope
- Assigned user stories
- Component responsibilities
- Dependencies and interfaces

### Step 4: Create Functional Design Plan
**Action:** Create detailed plan with checkboxes for tracking progress.

**File Location:** `aidlc-docs/construction/plans/{unit-name}-functional-design-plan.md`

**Template:** `../../templates/plans/stage-plan-base.md`

**Customize with:**
- Unit context and responsibilities
- Functional design specific steps
- Question categories (see Step 5)
- Expected artifacts (business-logic-model.md, business-rules.md, domain-entities.md)

**Plan Steps:**
```markdown
### Planning Phase
- [ ] 1. Analyze unit context and requirements
- [ ] 2. Generate clarifying questions
- [ ] 3. Collect user answers
- [ ] 4. Analyze answers for ambiguities
- [ ] 5. Create follow-up questions (if needed)
- [ ] 6. Resolve all ambiguities
- [ ] 7. Get user approval to proceed

### Generation Phase
- [ ] 8. Design business logic model
- [ ] 9. Define business rules
- [ ] 10. Define domain entities and relationships
- [ ] 11. Create business-logic-model.md
- [ ] 12. Create business-rules.md
- [ ] 13. Create domain-entities.md
- [ ] 14. Present completion message
- [ ] 15. Get user approval
```

### Step 5: Generate Clarifying Questions
**Action:** Thoroughly analyze the unit to identify ALL areas needing clarification.

**CRITICAL:** Default to asking questions when there is ANY ambiguity.

**Question Categories to Evaluate:**
1. **Business Logic Modeling** - Processing steps, decision points, workflows
2. **Domain Model** - Entities, attributes, relationships, aggregates
3. **Business Rules** - Validation rules, constraints, calculations
4. **Data Flow** - Inputs, outputs, transformations, persistence
5. **Integration Points** - External systems, APIs, dependencies
6. **Validation Rules** - Input validation, business validation, error messages
7. **Error Handling** - Error scenarios, handling, recovery
8. **State Management** - State tracking, transitions, triggers

**Question Format:** `../../templates/questions/multiple-choice-format.md`

**Critical Requirements:**
- Use multiple choice format (A, B, C, D, E)
- **MANDATORY:** Include "Other" as LAST option
- Only include meaningful options
- Use [Answer]: tags for responses

### Step 6: Embed Questions in Plan
**Action:** Add all generated questions to the plan file's "Clarifying Questions" section.

### Step 7: Present Plan to User
**Action:** Inform user that the plan is ready and request answers.

**Message:**
```markdown
# 📋 Functional Design Plan Ready - [unit-name]

Plan Location: `aidlc-docs/construction/plans/{unit-name}-functional-design-plan.md`

Please review the plan and answer the clarifying questions using [Answer]: tags.
```

### Step 8: Collect User Answers
**Action:** Once user confirms, read the plan file and extract answers after [Answer]: tags.

### Step 9: Analyze Answers for Ambiguities
**Action:** **MANDATORY** - Analyze all answers for ambiguities.

**Ambiguity Indicators:**
- "depends", "maybe", "not sure", "mix of", "somewhere between", "standard", "typical"
- Contradictions between answers
- Vague or incomplete responses

**If ambiguities found:** Create clarification file (Step 10)
**If no ambiguities:** Skip to Step 12

### Step 10: Create Follow-Up Questions
**Action:** Create clarification file if ambiguities were found.

**File Location:** `aidlc-docs/construction/plans/{unit-name}-functional-design-clarifications.md`

**Template:** `../../templates/questions/clarification-format.md`

**For each ambiguity:**
- Quote the ambiguous answer
- Explain the issue
- Ask specific follow-up question
- Provide clear options

### Step 11: Repeat Until Resolved
**Action:** Repeat Steps 8-10 until ALL ambiguities are resolved.

**CRITICAL:** Do NOT proceed until complete clarity is achieved.

### Step 12: Get User Approval to Proceed
**Action:** Request approval to proceed with generation phase.

**Log approval prompt** in audit.md with timestamp.

### Step 13: Update Plan Progress
**Action:** Mark planning phase steps (1-7) as [x] in the plan file.

**CRITICAL:** Update in SAME interaction where work is completed.

### Step 14: Generate Business Logic Model
**Action:** Create business logic model document.

**File Location:** `aidlc-docs/construction/{unit-name}/functional-design/business-logic-model.md`

**Template:** `../../templates/artifacts/functional-design/business-logic-model.md`

**Include:**
- Overview and main processing flow
- Decision points and branching logic
- Business workflows
- Processing scenarios (success, failure, edge cases)
- Data transformations
- Integration points
- State management

**Update plan:** Mark step 8 as [x] immediately after creating file.

### Step 15: Generate Business Rules Document
**Action:** Create business rules document.

**File Location:** `aidlc-docs/construction/{unit-name}/functional-design/business-rules.md`

**Template:** `../../templates/artifacts/functional-design/business-rules.md`

**Include:**
- Validation rules (input and business)
- Business constraints
- Calculations and formulas
- Business invariants
- Conditional logic
- Error handling rules

**Update plan:** Mark step 9 as [x] immediately after creating file.

### Step 16: Generate Domain Entities Document
**Action:** Create domain entities document.

**File Location:** `aidlc-docs/construction/{unit-name}/functional-design/domain-entities.md`

**Template:** `../../templates/artifacts/functional-design/domain-entities.md`

**Include:**
- Domain entities with attributes and relationships
- Value objects
- Aggregates and aggregate roots
- Entity relationships diagram
- Domain events
- Persistence considerations

**Update plan:** Mark step 10 as [x] immediately after creating file.

### Step 17: Update State Tracking
**Action:** Update `aidlc-docs/aidlc-state.md` to reflect completion.

**Template:** `../../templates/state/aidlc-state.md`

### Step 18: Present Completion Message
**Action:** Present standardized 2-option completion message.

**Template:** `../../templates/completion-messages/2-option-standard.md`

**MANDATORY FORMAT:**
```markdown
# 🔧 Functional Design Complete - [unit-name]

Artifacts Created:
- ✅ `business-logic-model.md` - Business logic flow and processing
- ✅ `business-rules.md` - Business rules and validations
- ✅ `domain-entities.md` - Domain entities and relationships

Location: `aidlc-docs/construction/{unit-name}/functional-design/`

---

What would you like to do?

🔧 **Request Changes** - Ask for modifications
✅ **Continue to Next Stage** - Approve and proceed

---
```

**CRITICAL:** Do NOT create 3-option menus or emergent navigation patterns.

### Step 19: Wait for User Response
**Action:** **WAIT FOR EXPLICIT APPROVAL** - Do NOT proceed until user confirms.

**Handle response:**
- If "Request Changes" → Make modifications and return to Step 18
- If "Continue" → Proceed to Step 20

### Step 20: Log User Approval
**Action:** Record approval in audit.md with complete raw input.

**Template:** `../../templates/audit-logs/basic-entry.md`

### Step 21: Update Final Plan Progress
**Action:** Mark all remaining steps as [x] in the plan file.

---

## Artifacts Created

1. **Plan:** `aidlc-docs/construction/plans/{unit-name}-functional-design-plan.md`
2. **Business Logic Model:** `aidlc-docs/construction/{unit-name}/functional-design/business-logic-model.md`
3. **Business Rules:** `aidlc-docs/construction/{unit-name}/functional-design/business-rules.md`
4. **Domain Entities:** `aidlc-docs/construction/{unit-name}/functional-design/domain-entities.md`
5. **Clarifications (if needed):** `aidlc-docs/construction/plans/{unit-name}-functional-design-clarifications.md`

**Artifact Templates:** See `../../templates/artifacts/functional-design/` directory

---

## Key Principles

1. **Proactive Questioning:** Default to asking questions when there is ANY ambiguity
2. **Thorough Analysis:** Evaluate ALL question categories
3. **Ambiguity Resolution:** MUST analyze answers and create follow-ups for unclear responses
4. **Immediate Progress Tracking:** Update checkboxes in SAME interaction
5. **Standardized Completion:** MUST use 2-option format (no emergent behavior)
6. **Complete Audit Trail:** Log ALL user inputs with complete raw input
7. **Explicit Approval:** WAIT for user approval before proceeding

---

## Templates Reference

All templates are located in `../../templates/` directory:

- **Audit Logs:** `audit-logs/basic-entry.md`
- **Plans:** `plans/stage-plan-base.md`
- **Questions:** `questions/multiple-choice-format.md`, `questions/clarification-format.md`
- **Artifacts:** `artifacts/functional-design/*.md`
- **Completion:** `completion-messages/2-option-standard.md`
- **State:** `state/aidlc-state.md`

---

## Next Stage

After approval:
- If NFR requirements exist → **NFR Requirements** stage
- If no NFR requirements → **Code Generation** stage

---

**End of Functional Design Stage Instructions**
