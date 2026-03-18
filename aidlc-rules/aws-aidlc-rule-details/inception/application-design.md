# Application Design

**Purpose:** Define components, services, and their responsibilities.

**Stage Type:** CONDITIONAL

**Phase:** INCEPTION

**Load this file when:** Starting Application Design stage

**Unload this file after:** Application Design completes and user approves

---

## Execute IF

- New components or services needed
- Component methods and business rules need definition
- Service layer design required
- Component dependencies need clarification

## Skip IF

- Changes within existing component boundaries
- No new components or methods
- Pure implementation changes

---

## Prerequisites

Before starting this stage, ensure:
1. Requirements Analysis has completed
2. User Stories has completed (if executed)
3. Workflow Planning has completed

---

## Steps

### Step 1: Log User Input
**Action:** Log any user input in audit.md.

**Template:** `../../templates/audit-logs/basic-entry.md`

### Step 2: Load Context
**Action:** Read relevant artifacts:

**Optional Artifacts:**
- `aidlc-docs/inception/reverse-engineering/` - Existing codebase (brownfield)
- `aidlc-docs/inception/requirements/requirements.md` - Requirements
- `aidlc-docs/inception/user-stories/stories.md` - User stories

### Step 3: Determine Design Depth
**Action:** Assess depth needed:
- **Minimal:** Simple components, clear responsibilities
- **Standard:** Normal complexity, moderate detail
- **Comprehensive:** Complex system, detailed design

### Step 4: Generate Clarifying Questions (if needed)
**Action:** Generate questions about:
- Component structure
- Component responsibilities
- Service layer design
- Component dependencies
- Method signatures

**Question Format:** `../../templates/questions/multiple-choice-format.md`

### Step 5: Collect User Answers (if questions asked)
**Action:** Wait for user to answer questions.

### Step 6: Analyze for Ambiguities (if questions asked)
**Action:** Check for ambiguous answers.

**Template:** `../../templates/questions/clarification-format.md`

### Step 7: Generate Application Design Artifacts
**Action:** Create design documents.

**File Location:** `aidlc-docs/inception/application-design/`

**Artifacts to Create:**
1. **components.md** - Component definitions and responsibilities
2. **component-methods.md** - Component methods and signatures
3. **services.md** - Service definitions (if applicable)
4. **component-dependency.md** - Component dependencies
5. **unit-of-work.md** - Units of work (if multiple units)
6. **unit-of-work-dependency.md** - Unit dependencies (if multiple units)
7. **unit-of-work-story-map.md** - Story to unit mapping (if stories exist)

**Include (based on depth):**
- Component layers (presentation, business, data, domain, utilities)
- Component responsibilities
- Method signatures
- Dependencies
- Service definitions

### Step 8: Update State Tracking
**Action:** Update `aidlc-docs/aidlc-state.md`.

**Template:** `../../templates/state/aidlc-state.md`

### Step 9: Present Completion Message
**Action:** Present completion message.

**Template:** `../../templates/completion-messages/inception-stage-complete.md`

### Step 10: Wait for User Response
**Action:** **WAIT FOR EXPLICIT APPROVAL**.

### Step 11: Log User Approval
**Action:** Record approval in audit.md.

**Template:** `../../templates/audit-logs/basic-entry.md`

---

## Artifacts Created

1. **components.md** - Component definitions
2. **component-methods.md** - Component methods
3. **services.md** - Service definitions (if applicable)
4. **component-dependency.md** - Component dependencies
5. **unit-of-work.md** - Units of work (if multiple units)
6. **unit-of-work-dependency.md** - Unit dependencies (if multiple units)
7. **unit-of-work-story-map.md** - Story mapping (if stories exist)

Location: `aidlc-docs/inception/application-design/`

---

## Key Principles

1. **Component-Based Design:** Define clear component boundaries
2. **Responsibility Assignment:** Each component has clear responsibilities
3. **Dependency Management:** Document component dependencies
4. **Service Layer:** Define service layer if needed
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
- **Units Generation** (if multiple units) OR
- **Functional Design** (if single unit or skipping units generation)

---

**End of Application Design Stage Instructions**
