# User Stories

**Purpose:** Generate user stories and personas for user-facing features.

**Stage Type:** CONDITIONAL

**Phase:** INCEPTION

**Load this file when:** Starting User Stories stage

**Unload this file after:** User Stories completes and user approves

---

## Execute IF

Execute if ANY of the following (High Priority Indicators):
- New user-facing features or functionality
- Changes affecting user workflows or interactions
- Multiple user types or personas involved
- Complex business requirements with acceptance criteria needs
- Customer-facing API or service changes

## Skip IF

Skip ONLY IF (Low Priority - Simple Cases):
- Pure internal refactoring with zero user impact
- Simple bug fixes with clear, isolated scope
- Infrastructure changes with no user-facing effects
- Technical debt cleanup with no functional changes

---

## Two-Part Structure

**PART 1 - Planning:**
- Create story plan with questions
- Collect answers
- Analyze for ambiguities
- Get approval

**PART 2 - Generation:**
- Execute approved plan to generate stories and personas

---

## Prerequisites

Before starting this stage, ensure:
1. Requirements Analysis has completed (if executed)
2. User request is understood

---

## PART 1: Planning Steps

### Step 1: Log User Input
**Action:** Log any user input in audit.md.

**Template:** `../../templates/audit-logs/basic-entry.md`

### Step 2: Perform Intelligent Assessment
**Action:** Assess if user stories add value for this specific request.

**Consider:**
- User impact (direct or indirect)
- Business context
- Complexity
- Team collaboration needs

### Step 3: Load Context
**Action:** Read relevant artifacts:

**Optional Artifacts:**
- `aidlc-docs/inception/reverse-engineering/` - Existing codebase (brownfield)
- `aidlc-docs/inception/requirements/requirements.md` - Requirements

### Step 4: Determine Story Depth
**Action:** Determine depth level:

- **Minimal:** Simple features, few stories
- **Standard:** Normal complexity, moderate number of stories
- **Comprehensive:** Complex features, many stories, detailed personas

### Step 5: Create Story Generation Plan
**Action:** Create plan with questions.

**File Location:** `aidlc-docs/inception/plans/story-generation-plan.md`

**Template:** `../../templates/plans/stage-plan-base.md`

### Step 6: Generate Questions
**Action:** Generate questions about:
- User types and personas
- User goals and workflows
- Acceptance criteria
- Story priorities
- Epic structure (if needed)

**Question Format:** `../../templates/questions/multiple-choice-format.md`

### Step 7: Present Plan to User
**Action:** Inform user that plan is ready.

### Step 8: Collect User Answers
**Action:** Wait for user to answer questions.

### Step 9: Analyze for Ambiguities
**Action:** Check for ambiguous answers.

**Template:** `../../templates/questions/clarification-format.md`

### Step 10: Get Approval to Proceed
**Action:** Request approval to generate stories.

---

## PART 2: Generation Steps

### Step 11: Generate User Stories
**Action:** Create stories document.

**File Location:** `aidlc-docs/inception/user-stories/stories.md`

**Include:**
- Story format (As a... I want to... So that...)
- Epic structure (if using epics)
- Story IDs, priorities, acceptance criteria
- Story summary
- Traceability to requirements

### Step 12: Generate Personas
**Action:** Create personas document.

**File Location:** `aidlc-docs/inception/user-stories/personas.md`

**Include (based on depth):**
- **Minimal:** Basic persona descriptions
- **Standard:** Persona details, goals, pain points
- **Comprehensive:** Detailed personas with scenarios

### Step 13: Update State Tracking
**Action:** Update `aidlc-docs/aidlc-state.md`.

**Template:** `../../templates/state/aidlc-state.md`

### Step 14: Present Completion Message
**Action:** Present completion message.

**Template:** `../../templates/completion-messages/inception-stage-complete.md`

### Step 15: Wait for User Response
**Action:** **WAIT FOR EXPLICIT APPROVAL**.

### Step 16: Log User Approval
**Action:** Record approval in audit.md.

**Template:** `../../templates/audit-logs/basic-entry.md`

---

## Artifacts Created

1. **Plan:** `aidlc-docs/inception/plans/story-generation-plan.md`
2. **Stories:** `aidlc-docs/inception/user-stories/stories.md`
3. **Personas:** `aidlc-docs/inception/user-stories/personas.md`

---

## Key Principles

1. **Intelligent Assessment:** Only create stories when they add value
2. **Two-Part Process:** Planning then generation
3. **User-Centric:** Focus on user goals and workflows
4. **Traceability:** Link stories to requirements
5. **Explicit Approval:** WAIT for user approval

---

## Templates Reference

- **Audit Logs:** `../../templates/audit-logs/basic-entry.md`
- **Plans:** `../../templates/plans/stage-plan-base.md`
- **Questions:** `../../templates/questions/multiple-choice-format.md`
- **Clarifications:** `../../templates/questions/clarification-format.md`
- **Completion:** `../../templates/completion-messages/inception-stage-complete.md`
- **State:** `../../templates/state/aidlc-state.md`

---

## Next Stage

After approval:
- **Workflow Planning** stage

---

**End of User Stories Stage Instructions**
