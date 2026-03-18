# NFR Design Stage

**Purpose:** Incorporate non-functional requirement patterns into the design and define logical components for a specific unit of work.

**Stage Type:** CONDITIONAL (per-unit)

**Phase:** CONSTRUCTION

**Load this file when:** Starting NFR Design stage for a unit

**Unload this file after:** NFR Design stage completes and user approves

---

## Execute IF

Execute this stage if BOTH of the following conditions are met:
- NFR Requirements stage was executed for this unit
- NFR patterns need to be incorporated into the design

## Skip IF

Skip this stage if ANY of the following conditions are met:
- No NFR requirements were identified
- NFR Requirements Assessment stage was skipped
- NFR patterns are already well-defined

---

## Prerequisites

Before starting this stage, ensure:
1. NFR Requirements artifacts exist for this unit
2. Functional Design artifacts exist (if Functional Design stage was executed)
3. Unit of work is defined in `unit-of-work.md`
4. Technology stack decisions have been made

---

## Detailed Steps

### Step 1: Log User Input
**Action:** Log any user input during this stage in `audit.md`.

**Template:** `../../templates/audit-logs/basic-entry.md`

**Log with:**
- Stage: NFR Design - [unit-name]
- Complete raw user input (never summarize)
- ISO 8601 timestamp

### Step 2: Load NFR Requirements Context
**Action:** Read and analyze the NFR requirements artifacts:

**Required Artifacts:**
- `aidlc-docs/construction/{unit-name}/nfr-requirements/nfr-requirements.md` - NFR requirements
- `aidlc-docs/construction/{unit-name}/nfr-requirements/tech-stack-decisions.md` - Tech stack decisions

**Optional Artifacts (if they exist):**
- `aidlc-docs/construction/{unit-name}/functional-design/` - Functional design artifacts
- `aidlc-docs/inception/application-design/unit-of-work.md` - Unit definition
- `aidlc-docs/inception/application-design/components.md` - Component definitions

### Step 3: Analyze NFR Requirements
**Action:** Analyze the NFR requirements to understand design implications:
- Performance requirements and their design impact
- Security requirements and necessary patterns
- Scalability requirements and architectural patterns
- Reliability requirements and fault tolerance patterns
- Technology stack choices and their implications

### Step 4: Create NFR Design Plan
**Action:** Create detailed plan with checkboxes for tracking progress.

**File Location:** `aidlc-docs/construction/plans/{unit-name}-nfr-design-plan.md`

**Template:** `../../templates/plans/stage-plan-base.md`

**Customize with:**
- NFR requirements summary
- NFR design specific steps
- Question categories
- Expected artifacts (nfr-design-patterns.md, logical-components.md)

**Plan Steps:**
```markdown
### Planning Phase
- [ ] 1. Analyze NFR requirements and tech stack
- [ ] 2. Generate clarifying questions
- [ ] 3. Collect user answers
- [ ] 4. Analyze answers for ambiguities
- [ ] 5. Create follow-up questions (if needed)
- [ ] 6. Resolve all ambiguities
- [ ] 7. Get user approval to proceed

### Generation Phase
- [ ] 8. Design performance patterns
- [ ] 9. Design security patterns
- [ ] 10. Design scalability patterns
- [ ] 11. Design reliability patterns
- [ ] 12. Define logical components
- [ ] 13. Create nfr-design-patterns.md
- [ ] 14. Create logical-components.md
- [ ] 15. Present completion message
- [ ] 16. Get user approval
```

### Step 5: Generate Clarifying Questions
**Action:** Generate questions about NFR pattern implementation.

**Question Categories to Evaluate:**
1. **Performance Patterns** - Caching, optimization, async processing
2. **Security Patterns** - Authentication, authorization, encryption implementation
3. **Scalability Patterns** - Load balancing, stateless design, partitioning
4. **Reliability Patterns** - Retry, circuit breaker, fallback, health checks
5. **Component Structure** - Layering, boundaries, interactions
6. **Integration Approaches** - How to integrate with external systems

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
# 📋 NFR Design Plan Ready - [unit-name]

Plan Location: `aidlc-docs/construction/plans/{unit-name}-nfr-design-plan.md`

Please review the plan and answer the NFR design questions using [Answer]: tags.
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

**File Location:** `aidlc-docs/construction/plans/{unit-name}-nfr-design-clarifications.md`

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

### Step 14: Generate NFR Design Patterns Document
**Action:** Create NFR design patterns document.

**File Location:** `aidlc-docs/construction/{unit-name}/nfr-design/nfr-design-patterns.md`

**Template:** `../../templates/artifacts/nfr/nfr-design-patterns.md`

**Include:**
- Overview of NFR design patterns
- Performance patterns (caching, async, database optimization)
- Security patterns (authentication, authorization, encryption, validation, audit logging)
- Scalability patterns (load balancing, stateless design, partitioning, auto-scaling)
- Reliability patterns (retry, circuit breaker, fallback, timeout, health check)
- Integration patterns
- Observability patterns (logging, metrics, tracing)

**Update plan:** Mark steps 8-13 as [x] immediately after creating file.

### Step 15: Generate Logical Components Document
**Action:** Create logical components document.

**File Location:** `aidlc-docs/construction/{unit-name}/nfr-design/logical-components.md`

**Template:** `../../templates/artifacts/nfr/logical-components.md`

**Include:**
- Overview of component architecture
- Layered architecture description
- Logical components with responsibilities, interfaces, dependencies
- Component interactions and data flow
- Component boundaries
- Cross-cutting concerns (logging, error handling, transactions, security)
- Deployment considerations
- Component testing strategy

**Update plan:** Mark step 14 as [x] immediately after creating file.

### Step 16: Update State Tracking
**Action:** Update `aidlc-docs/aidlc-state.md` to reflect completion.

**Template:** `../../templates/state/aidlc-state.md`

### Step 17: Present Completion Message
**Action:** Present standardized 2-option completion message.

**Template:** `../../templates/completion-messages/2-option-standard.md`

**MANDATORY FORMAT:**
```markdown
# 🔧 NFR Design Complete - [unit-name]

Artifacts Created:
- ✅ `nfr-design-patterns.md` - NFR design patterns and implementation
- ✅ `logical-components.md` - Logical component structure and responsibilities

Location: `aidlc-docs/construction/{unit-name}/nfr-design/`

---

What would you like to do?

🔧 **Request Changes** - Ask for modifications
✅ **Continue to Next Stage** - Approve and proceed

---
```

**CRITICAL:** Do NOT create 3-option menus or emergent navigation patterns.

### Step 18: Wait for User Response
**Action:** **WAIT FOR EXPLICIT APPROVAL** - Do NOT proceed until user confirms.

**Handle response:**
- If "Request Changes" → Make modifications and return to Step 17
- If "Continue" → Proceed to Step 19

### Step 19: Log User Approval
**Action:** Record approval in audit.md with complete raw input.

**Template:** `../../templates/audit-logs/basic-entry.md`

### Step 20: Update Final Plan Progress
**Action:** Mark all remaining steps as [x] in the plan file.

---

## Artifacts Created

1. **Plan:** `aidlc-docs/construction/plans/{unit-name}-nfr-design-plan.md`
2. **NFR Design Patterns:** `aidlc-docs/construction/{unit-name}/nfr-design/nfr-design-patterns.md`
3. **Logical Components:** `aidlc-docs/construction/{unit-name}/nfr-design/logical-components.md`
4. **Clarifications (if needed):** `aidlc-docs/construction/plans/{unit-name}-nfr-design-clarifications.md`

**Artifact Templates:** See `../../templates/artifacts/nfr/` directory

---

## Key Principles

1. **Pattern-Based Design:** Apply proven NFR patterns
2. **Clear Component Boundaries:** Define explicit component responsibilities
3. **Ambiguity Resolution:** MUST analyze answers and create follow-ups
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
- **Artifacts:** `artifacts/nfr/*.md`
- **Completion:** `completion-messages/2-option-standard.md`
- **State:** `state/aidlc-state.md`

---

## Next Stage

After approval:
- **Infrastructure Design** stage (if infrastructure design needed)
- **Code Generation** stage (if ready to generate code)

---

**End of NFR Design Stage Instructions**
