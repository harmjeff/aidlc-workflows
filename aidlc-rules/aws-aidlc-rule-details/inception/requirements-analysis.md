# Requirements Analysis

**Purpose:** Analyze user request, gather functional and non-functional requirements.

**Stage Type:** ALWAYS (Adaptive Depth)

**Phase:** INCEPTION

**Load this file when:** Starting Requirements Analysis stage

**Unload this file after:** Requirements Analysis completes and user approves

---

## Execute IF

**ALWAYS** - This stage executes for every workflow, but depth varies based on request clarity and complexity.

## Depth Levels

- **Minimal:** Simple, clear request - just document intent analysis
- **Standard:** Normal complexity - gather functional and non-functional requirements
- **Comprehensive:** Complex, high-risk - detailed requirements with traceability

---

## Prerequisites

Before starting this stage, ensure:
1. Workspace Detection has completed
2. Reverse Engineering has completed (if brownfield)
3. User request is logged in audit.md

---

## Steps

### Step 1: Log User Input
**Action:** Log any user input during this stage in audit.md.

**Template:** `../../templates/audit-logs/basic-entry.md`

### Step 2: Load Context
**Action:** Read relevant artifacts:

**Optional Artifacts (if they exist):**
- `aidlc-docs/inception/reverse-engineering/` - Existing codebase context (brownfield)
- Initial user request from audit.md

### Step 3: Analyze User Request
**Action:** Perform intent analysis:
- What is the user trying to achieve?
- What problem are they solving?
- What are the key requirements?
- What is the scope?
- What are the constraints?

### Step 4: Determine Requirements Depth
**Action:** Assess what depth of requirements gathering is needed:

**Minimal Depth IF:**
- Request is very clear and specific
- Low complexity
- Low risk
- Small scope

**Standard Depth IF:**
- Normal complexity
- Moderate risk
- Medium scope
- Some ambiguity

**Comprehensive Depth IF:**
- High complexity
- High risk
- Large scope
- Significant ambiguity
- Multiple stakeholders

### Step 5: Generate Clarifying Questions (if needed)
**Action:** If Standard or Comprehensive depth, generate questions.

**Question Categories:**
1. **Functional Requirements** - What the system should do
2. **Non-Functional Requirements** - Performance, security, scalability
3. **User Experience** - User workflows, interfaces
4. **Data Requirements** - Data models, storage, processing
5. **Integration Requirements** - External systems, APIs
6. **Constraints** - Technical, business, regulatory

**Question Format:** `../../templates/questions/multiple-choice-format.md`

### Step 6: Collect User Answers (if questions asked)
**Action:** Wait for user to answer questions.

### Step 7: Analyze Answers for Ambiguities (if questions asked)
**Action:** Check for ambiguous answers and create follow-up questions if needed.

**Template:** `../../templates/questions/clarification-format.md`

### Step 8: Generate Requirements Document
**Action:** Create requirements document.

**File Location:** `aidlc-docs/inception/requirements/requirements.md`

**Include (based on depth):**
- **Minimal:** Intent analysis, key requirements
- **Standard:** Functional requirements, non-functional requirements, constraints
- **Comprehensive:** Detailed requirements, user scenarios, traceability matrix

### Step 9: Update State Tracking
**Action:** Update `aidlc-docs/aidlc-state.md` to reflect completion.

**Template:** `../../templates/state/aidlc-state.md`

### Step 10: Present Completion Message
**Action:** Present completion message to user.

**Template:** `../../templates/completion-messages/inception-stage-complete.md`

**Customize with:**
- Stage: Requirements Analysis
- Artifacts: requirements.md
- Next Stage: User Stories or Workflow Planning

### Step 11: Wait for User Response
**Action:** **WAIT FOR EXPLICIT APPROVAL** - Do NOT proceed until user confirms.

### Step 12: Log User Approval
**Action:** Record approval in audit.md.

**Template:** `../../templates/audit-logs/basic-entry.md`

---

## Artifacts Created

1. **requirements.md** - Requirements document
2. **requirement-verification-questions.md** (if questions asked)

Location: `aidlc-docs/inception/requirements/`

---

## Key Principles

1. **Adaptive Depth:** Adjust detail level based on complexity
2. **Clarity First:** Resolve ambiguities before proceeding
3. **User-Centric:** Focus on what user wants to achieve
4. **Complete Audit Trail:** Log all user inputs
5. **Explicit Approval:** WAIT for user approval

---

## Templates Reference

- **Audit Logs:** `../../templates/audit-logs/basic-entry.md`
- **Questions:** `../../templates/questions/multiple-choice-format.md`
- **Clarifications:** `../../templates/questions/clarification-format.md`
- **Completion:** `../../templates/completion-messages/inception-stage-complete.md`
- **State:** `../../templates/state/aidlc-state.md`

---

## Next Stage

After approval:
- **User Stories** (if user-facing features) OR
- **Workflow Planning** (if skipping user stories)

---

**End of Requirements Analysis Stage Instructions**
