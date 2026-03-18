# Workflow Planning

**Purpose:** Determine which phases to execute, depth levels, and create execution plan.

**Stage Type:** ALWAYS

**Phase:** INCEPTION

**Load this file when:** Starting Workflow Planning stage

**Unload this file after:** Workflow Planning completes and user approves

---

## Execute IF

**ALWAYS** - This stage executes for every workflow.

---

## Prerequisites

Before starting this stage, ensure:
1. Workspace Detection has completed
2. Reverse Engineering has completed (if brownfield)
3. Requirements Analysis has completed
4. User Stories has completed (if executed)

---

## Steps

### Step 1: Log User Input
**Action:** Log any user input in audit.md.

**Template:** `../../templates/audit-logs/basic-entry.md`

### Step 2: Load All Prior Context
**Action:** Read all prior artifacts:

**Required Artifacts:**
- `aidlc-docs/aidlc-state.md` - Current state

**Optional Artifacts:**
- `aidlc-docs/inception/reverse-engineering/` - Existing codebase (brownfield)
- `aidlc-docs/inception/requirements/requirements.md` - Requirements
- `aidlc-docs/inception/user-stories/` - User stories

### Step 3: Analyze Request Complexity
**Action:** Assess complexity and scope:
- Simple vs complex changes
- Single component vs multiple components
- Clear requirements vs ambiguous requirements
- Low risk vs high risk
- Small scope vs large scope

### Step 4: Determine Phases to Execute
**Action:** Decide which phases and stages are needed:

**INCEPTION PHASE:**
- ✅ Workspace Detection (completed)
- ✅ Reverse Engineering (completed if brownfield)
- ✅ Requirements Analysis (completed)
- ✅ User Stories (completed if executed)
- ✅ Workflow Planning (current)
- ❓ Application Design (conditional)
- ❓ Units Generation (conditional)

**CONSTRUCTION PHASE:**
- ❓ Functional Design (conditional, per-unit)
- ❓ NFR Requirements (conditional, per-unit)
- ❓ NFR Design (conditional, per-unit)
- ❓ Infrastructure Design (conditional, per-unit)
- ✅ Code Generation (always, per-unit)
- ✅ Build and Test (always)

**OPERATIONS PHASE:**
- ❓ Operations (placeholder)

### Step 5: Determine Depth Levels
**Action:** For each stage, determine depth level:
- **Minimal:** Simple, clear, low risk
- **Standard:** Normal complexity
- **Comprehensive:** Complex, high risk, large scope

### Step 6: Create Multi-Package Change Sequence (if brownfield)
**Action:** If multiple packages need changes, determine order:
- Identify dependencies between packages
- Determine change sequence
- Document rationale for sequence

### Step 7: Generate Workflow Visualization
**Action:** Create workflow visualization.

**MANDATORY:** Validate Mermaid syntax before writing.

**Content Validation:** See `common/content-validation.md`

**Include:**
- Text alternative for accessibility
- All phases and stages
- Conditional logic indicators
- Depth level indicators

### Step 8: Create Workflow Plan Document
**Action:** Create comprehensive workflow plan.

**File Location:** `aidlc-docs/inception/workflow-plan.md`

**Include:**
- Phases to execute
- Stages to execute (with conditional logic)
- Depth levels for each stage
- Multi-package sequence (if applicable)
- Workflow visualization
- Rationale for decisions

### Step 9: Update aidlc-state.md
**Action:** Update state with execution plan.

**Template:** `../../templates/state/aidlc-state.md`

**Add:**
- Execution plan reference
- Adaptive detail levels
- Notes about workflow decisions

### Step 10: Present Recommendations to User
**Action:** Present workflow recommendations.

**CRITICAL:** Emphasize user control to override recommendations.

**Message:**
```markdown
# 📋 Workflow Plan Ready

I've analyzed your request and created a recommended workflow plan.

**Recommended Phases:**
- 🔵 INCEPTION: [Stages to execute]
- 🟢 CONSTRUCTION: [Stages to execute]
- 🟡 OPERATIONS: [Stages to execute]

**Depth Levels:**
- [Stage]: [Minimal/Standard/Comprehensive]

**Plan Location:** `aidlc-docs/inception/workflow-plan.md`

---

**IMPORTANT:** This is a recommendation. You can:
- Accept the plan as-is
- Request modifications
- Skip stages you don't need
- Add stages I didn't recommend

**What would you like to do?**

A) Accept the plan and proceed
B) Request modifications to the plan
C) Other (please specify)

[Answer]: 
```

### Step 11: Wait for User Response
**Action:** **WAIT FOR EXPLICIT APPROVAL**.

### Step 12: Handle User Response
**Action:** Based on user's choice:
- If accept → Proceed to Step 13
- If modifications → Make changes and return to Step 10
- If other → Discuss and adjust

### Step 13: Log User Approval
**Action:** Record approval in audit.md.

**Template:** `../../templates/audit-logs/basic-entry.md`

### Step 14: Finalize Workflow Plan
**Action:** Mark Workflow Planning as complete in aidlc-state.md.

---

## Artifacts Created

1. **Workflow Plan:** `aidlc-docs/inception/workflow-plan.md`
2. **Updated State:** `aidlc-docs/aidlc-state.md`

---

## Key Principles

1. **Adaptive Execution:** Only execute stages that add value
2. **Transparent Planning:** Show execution plan before starting
3. **User Control:** User can override recommendations
4. **Content Validation:** Validate Mermaid syntax before writing
5. **Explicit Approval:** WAIT for user approval

---

## Templates Reference

- **Audit Logs:** `../../templates/audit-logs/basic-entry.md`
- **State:** `../../templates/state/aidlc-state.md`

---

## Next Stage

After approval:
- **Application Design** (if needed) OR
- **Units Generation** (if needed) OR
- **Functional Design** (if skipping inception design stages)

---

**End of Workflow Planning Stage Instructions**
