# Session Continuity

**Purpose:** Resume workflow from any interruption point

---

## Resume Workflow Process

### Step 1: Read aidlc-state.md FIRST

**MANDATORY:** Always read aidlc-state.md before any other action when resuming.

Extract:
- Current phase (INCEPTION/CONSTRUCTION/OPERATIONS)
- Current stage name
- Completed stages list
- Skipped stages list
- Current unit (if in per-unit loop)
- Last update timestamp

### Step 2: Load Previous Stage Artifacts

**MANDATORY:** Load all artifacts from previous stages before resuming.

See "Smart Context Loading" section below for stage-specific artifacts.

### Step 3: Determine Resume Point

Based on aidlc-state.md:
- If stage is "IN PROGRESS" → Resume within that stage
- If stage is "COMPLETED" → Move to next stage
- If stage is "PENDING" → Start that stage
- If stage is "SKIPPED" → Move to next non-skipped stage

### Step 4: Present Welcome Back Message

```markdown
# Welcome Back to AIDLC Workflow

I've reviewed your workflow state and found:
- **Current Phase:** [INCEPTION/CONSTRUCTION/OPERATIONS]
- **Current Stage:** [Stage name]
- **Status:** [IN PROGRESS/COMPLETED/PENDING]
- **Completed Stages:** [List]
- **Skipped Stages:** [List]

**Context Summary:**
[Brief summary of what has been done so far]

**Next Steps:**
[Specific next steps based on current stage]

Would you like to:
A) Continue from where we left off
B) Review previous work
C) Make changes to the workflow plan
D) Start a different stage

[Answer]:
```

### Step 5: Load Stage Detail File

Load the appropriate detail file for current stage:
- `aidlc-workflow/details/{phase}/{stage-name}.md`

### Step 6: Continue Execution

Resume stage execution from current checkpoint.

---

## Smart Context Loading by Stage

### Early Stages (Workspace Detection, Reverse Engineering)

**Load:**
- aidlc-state.md
- audit.md
- workspace-detection.md (if resuming workspace detection)

### Requirements/Stories Stages

**Load:**
- aidlc-state.md
- audit.md
- Reverse engineering artifacts (if brownfield):
  - architecture.md
  - component-inventory.md
  - technology-stack.md
- requirements.md (if exists)

### Design Stages (Application Design, Units Generation)

**Load:**
- aidlc-state.md
- audit.md
- requirements.md
- stories.md (if executed)
- personas.md (if executed)
- architecture.md (if brownfield)

### Construction Stages (Functional Design, NFR, Infrastructure, Code)

**Load:**
- aidlc-state.md
- audit.md
- ALL inception artifacts:
  - requirements.md
  - stories.md (if executed)
  - components.md (if executed)
  - unit-of-work.md (if executed)
- Unit-specific artifacts:
  - Previous design artifacts for this unit
  - Code files for this unit (if any)

### Build and Test Stage

**Load:**
- aidlc-state.md
- audit.md
- ALL unit code generation plans
- ALL generated code files

---

## Error Handling

### Missing aidlc-state.md

If aidlc-state.md doesn't exist:
1. Assume new workflow
2. Start with Workspace Detection
3. Create aidlc-state.md

### Corrupted aidlc-state.md

If aidlc-state.md is corrupted or unreadable:
1. Check audit.md for last known state
2. Reconstruct state from audit log
3. Ask user to confirm reconstructed state
4. Regenerate aidlc-state.md

### Missing Artifacts

If expected artifacts are missing:
1. Identify which artifacts are missing
2. Determine if they're critical for current stage
3. If critical: Offer to regenerate
4. If non-critical: Offer to skip or regenerate
5. Get user approval before proceeding

### Inconsistent State

If aidlc-state.md conflicts with actual artifacts:
1. List the inconsistencies
2. Ask user which is correct
3. Update aidlc-state.md or regenerate artifacts
4. Log the resolution in audit.md

---

## Checkpoint Strategy

### When to Update aidlc-state.md

Update after:
- Stage completion
- Stage start
- Plan approval
- Significant progress within stage
- User-requested changes

### What to Track in aidlc-state.md

```markdown
# AIDLC Workflow State

**Last Updated:** [ISO 8601 timestamp]

## Current Status
- **Phase:** [INCEPTION/CONSTRUCTION/OPERATIONS]
- **Stage:** [Stage name]
- **Status:** [IN PROGRESS/COMPLETED/PENDING]
- **Current Unit:** [Unit name if in per-unit loop]

## Completed Stages
- [x] Workspace Detection
- [x] Requirements Analysis
- [x] Workflow Planning

## Skipped Stages
- [ ] Reverse Engineering (Greenfield project)
- [ ] User Stories (Simple bug fix)

## Pending Stages
- [ ] Code Generation - Unit 1
- [ ] Code Generation - Unit 2
- [ ] Build and Test

## Notes
[Any important context or decisions]
```

---

## Resume from Mid-Stage

### If Stage Has Plan File

1. Read plan file (e.g., `{unit-name}-code-generation-plan.md`)
2. Check which steps are marked [x] as complete
3. Resume from first unchecked [ ] step
4. Continue execution

### If Stage Has No Plan File

1. Check audit.md for last action in this stage
2. Determine what was completed
3. Ask user to confirm resume point
4. Continue execution

---

## Rationale

**Why read aidlc-state.md first?**
- Provides immediate context
- Prevents redundant work
- Ensures continuity
- Enables smart artifact loading

**Why load previous artifacts?**
- Maintains consistency
- Provides necessary context
- Prevents contradictions
- Enables informed decisions

**Why smart context loading?**
- Minimizes context usage
- Loads only what's needed
- Improves performance
- Reduces token consumption

---

**Load this file:** Only when resuming an existing workflow (aidlc-state.md exists).
