# NFR Requirements Stage

**Purpose:** Assess non-functional requirements (performance, security, scalability, reliability) and make technology stack decisions for a specific unit of work.

**Stage Type:** CONDITIONAL (per-unit)

**Phase:** CONSTRUCTION

**Load this file when:** Starting NFR Requirements stage for a unit

**Unload this file after:** NFR Requirements stage completes and user approves

---

## Execute IF

Execute this stage if ANY of the following conditions are met:
- Performance requirements exist for this unit
- Security considerations need to be addressed
- Scalability concerns are present
- Reliability requirements need definition
- Technology stack selection is required
- Maintainability requirements need specification

## Skip IF

Skip this stage if ALL of the following conditions are met:
- No non-functional requirements for this unit
- Technology stack is already determined
- No performance, security, or scalability concerns

---

## Prerequisites

Before starting this stage, ensure:
1. Unit of work is defined in `unit-of-work.md`
2. Functional Design artifacts exist (if Functional Design stage was executed)
3. Application design artifacts exist (if Application Design stage was executed)
4. Requirements document is available (if Requirements Analysis was executed)

---

## Detailed Steps

### Step 1: Log User Input
**Action:** Log any user input during this stage in `audit.md`.

**Template:** `../../templates/audit-logs/basic-entry.md`

**Log with:**
- Stage: NFR Requirements - [unit-name]
- Complete raw user input (never summarize)
- ISO 8601 timestamp

### Step 2: Load Unit Context
**Action:** Read and analyze the following artifacts to understand the unit:

**Required Artifacts:**
- `aidlc-docs/inception/application-design/unit-of-work.md` - Unit definition
- `aidlc-docs/construction/{unit-name}/functional-design/` - Functional design artifacts (if executed)

**Optional Artifacts (if they exist):**
- `aidlc-docs/inception/requirements/requirements.md` - Requirements document
- `aidlc-docs/inception/user-stories/stories.md` - User stories
- `aidlc-docs/inception/reverse-engineering/technology-stack.md` - Existing tech stack (brownfield)
- `aidlc-docs/inception/application-design/components.md` - Component definitions

### Step 3: Analyze Unit Context
**Action:** Analyze the unit to understand NFR implications:
- Unit responsibilities and scope
- Functional design and business logic complexity
- Data volume and processing requirements
- User-facing vs. backend nature
- Integration points and dependencies
- Existing technology constraints (brownfield)

### Step 4: Create NFR Requirements Plan
**Action:** Create detailed plan with checkboxes for tracking progress.

**File Location:** `aidlc-docs/construction/plans/{unit-name}-nfr-requirements-plan.md`

**Template:** `../../templates/plans/stage-plan-base.md`

**Customize with:**
- Unit context and functional complexity
- NFR requirements specific steps
- Comprehensive NFR question categories
- Expected artifacts (nfr-requirements.md, tech-stack-decisions.md)

**Plan Steps:**
```markdown
### Planning Phase
- [ ] 1. Analyze unit context and functional design
- [ ] 2. Generate comprehensive NFR questions
- [ ] 3. Collect user answers
- [ ] 4. Analyze answers for ambiguities
- [ ] 5. Create follow-up questions (if needed)
- [ ] 6. Resolve all ambiguities
- [ ] 7. Get user approval to proceed

### Generation Phase
- [ ] 8. Assess performance requirements
- [ ] 9. Assess security requirements
- [ ] 10. Assess scalability requirements
- [ ] 11. Assess reliability requirements
- [ ] 12. Assess maintainability requirements
- [ ] 13. Make technology stack decisions
- [ ] 14. Create nfr-requirements.md
- [ ] 15. Create tech-stack-decisions.md
- [ ] 16. Present completion message
- [ ] 17. Get user approval
```

### Step 5: Generate Comprehensive NFR Questions
**Action:** Generate comprehensive questions across ALL NFR categories.

**CRITICAL:** Ask questions across all NFR categories unless there is explicit justification to skip.

**Question Categories to Evaluate:**
1. **Performance Requirements** - Response times, throughput, latency, resource usage
2. **Security Requirements** - Authentication, authorization, data protection, compliance
3. **Scalability Requirements** - Growth expectations, load patterns, scaling strategy
4. **Reliability Requirements** - Availability, fault tolerance, disaster recovery
5. **Maintainability Requirements** - Code quality, documentation, testing, monitoring
6. **Technology Stack** - Language, framework, database, infrastructure preferences

**Question Format:** `../../templates/questions/multiple-choice-format.md`

**Critical Requirements:**
- Use multiple choice format (A, B, C, D, E)
- **MANDATORY:** Include "Other" as LAST option
- Only include meaningful options
- Use [Answer]: tags for responses

### Step 6: Embed Questions in Plan
**Action:** Add all generated questions to the plan file's "Comprehensive NFR Questions" section.

### Step 7: Present Plan to User
**Action:** Inform user that the plan is ready and request answers.

**Message:**
```markdown
# 📋 NFR Requirements Plan Ready - [unit-name]

Plan Location: `aidlc-docs/construction/plans/{unit-name}-nfr-requirements-plan.md`

Please review the plan and answer the NFR questions using [Answer]: tags.
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

**File Location:** `aidlc-docs/construction/plans/{unit-name}-nfr-requirements-clarifications.md`

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

### Step 14: Generate NFR Requirements Document
**Action:** Create NFR requirements document.

**File Location:** `aidlc-docs/construction/{unit-name}/nfr-requirements/nfr-requirements.md`

**Template:** `../../templates/artifacts/nfr/nfr-requirements.md`

**Include:**
- Performance requirements (response time, throughput, latency, resources)
- Security requirements (authentication, authorization, data protection, compliance)
- Scalability requirements (growth expectations, geographic distribution, scaling strategy)
- Reliability requirements (availability, fault tolerance, disaster recovery, data consistency)
- Maintainability requirements (code quality, documentation, testing, monitoring, logging, deployment)
- Usability requirements (if applicable)
- Compatibility requirements (if applicable)

**Update plan:** Mark steps 8-14 as [x] immediately after creating file.

### Step 15: Generate Tech Stack Decisions Document
**Action:** Create technology stack decisions document.

**File Location:** `aidlc-docs/construction/{unit-name}/nfr-requirements/tech-stack-decisions.md`

**Template:** `../../templates/artifacts/nfr/tech-stack-decisions.md`

**Include:**
- Programming language decision and rationale
- Framework decision and rationale
- Database decision and rationale
- Caching strategy
- Message queue/event bus (if applicable)
- Cloud services
- API technology
- Authentication & authorization
- Testing frameworks
- Monitoring and observability tools
- CI/CD tools
- Security tools
- Existing technology constraints (brownfield)
- Team skills considerations
- Cost considerations

**Update plan:** Mark step 15 as [x] immediately after creating file.

### Step 16: Update State Tracking
**Action:** Update `aidlc-docs/aidlc-state.md` to reflect completion.

**Template:** `../../templates/state/aidlc-state.md`

### Step 17: Present Completion Message
**Action:** Present standardized 2-option completion message.

**Template:** `../../templates/completion-messages/2-option-standard.md`

**MANDATORY FORMAT:**
```markdown
# 🔧 NFR Requirements Complete - [unit-name]

Artifacts Created:
- ✅ `nfr-requirements.md` - Comprehensive NFR requirements
- ✅ `tech-stack-decisions.md` - Technology stack decisions and rationale

Location: `aidlc-docs/construction/{unit-name}/nfr-requirements/`

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

1. **Plan:** `aidlc-docs/construction/plans/{unit-name}-nfr-requirements-plan.md`
2. **NFR Requirements:** `aidlc-docs/construction/{unit-name}/nfr-requirements/nfr-requirements.md`
3. **Tech Stack Decisions:** `aidlc-docs/construction/{unit-name}/nfr-requirements/tech-stack-decisions.md`
4. **Clarifications (if needed):** `aidlc-docs/construction/plans/{unit-name}-nfr-requirements-clarifications.md`

**Artifact Templates:** See `../../templates/artifacts/nfr/` directory

---

## Key Principles

1. **Comprehensive Assessment:** Evaluate ALL NFR categories
2. **Thorough Questioning:** Ask questions across all categories
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
- **Artifacts:** `artifacts/nfr/*.md`
- **Completion:** `completion-messages/2-option-standard.md`
- **State:** `state/aidlc-state.md`

---

## Next Stage

After approval:
- If NFR design needed → **NFR Design** stage
- If no NFR design → **Infrastructure Design** or **Code Generation** stage

---

**End of NFR Requirements Stage Instructions**
