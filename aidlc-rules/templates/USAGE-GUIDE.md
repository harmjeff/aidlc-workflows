# Template Usage Guide

Quick reference for using AIDLC workflow templates.

---

## Quick Start

### For AI Models

When executing a workflow stage:

1. **Read the detail file** for the stage (e.g., `details/construction/functional-design.md`)
2. **Follow the steps** in the detail file
3. **When you see a template reference**, read that template file
4. **Copy the template structure** and fill in with actual content
5. **Customize as needed** for the specific context

### For Human Readers

When understanding a workflow stage:

1. **Read the detail file** to understand the process
2. **Refer to templates** only when you need to see the format
3. **Templates show structure**, detail files show process

---

## Template Categories

### 1. Audit Logs (`audit-logs/`)

**Purpose:** Standard formats for logging workflow interactions

**When to use:** Every time you log an interaction in `audit.md`

**Example:**
```markdown
**Template:** `templates/audit-logs/basic-entry.md`

**Log with:**
- Stage: Requirements Analysis
- User Input: "[Complete raw input]"
- Timestamp: 2026-01-28T15:00:00Z
```

**Key templates:**
- `basic-entry.md` - Standard log entry (use for most interactions)
- `stage-start.md` - When starting a stage
- `approval-request.md` - When requesting approval
- `user-response.md` - When logging user response

---

### 2. Completion Messages (`completion-messages/`)

**Purpose:** Standardized formats for stage completion

**When to use:** At the end of every stage when presenting results to user

**Example:**
```markdown
**Template:** `templates/completion-messages/2-option-standard.md`

**CRITICAL:** Use exactly as specified for CONSTRUCTION stages
```

**Key templates:**
- `2-option-standard.md` - MANDATORY for construction stages
- `inception-stage-complete.md` - For inception stages
- `build-and-test-complete.md` - For build and test stage

**Critical Rule:** NEVER create 3-option menus or emergent navigation patterns

---

### 3. Questions (`questions/`)

**Purpose:** Standard formats for asking clarifying questions

**When to use:** When you need to ask user questions during any stage

**Example:**
```markdown
**Template:** `templates/questions/multiple-choice-format.md`

**Critical:** 
- NEVER ask questions in chat
- ALWAYS create question files
- MANDATORY "Other" option for every question
```

**Key templates:**
- `multiple-choice-format.md` - Standard question format
- `clarification-format.md` - For resolving ambiguities

---

### 4. Plans (`plans/`)

**Purpose:** Standard structures for stage planning documents

**When to use:** When creating a plan file for any stage

**Example:**
```markdown
**Template:** `templates/plans/stage-plan-base.md`

**Customize with:**
- Stage-specific steps
- Stage-specific questions
- Expected artifacts
```

**Key templates:**
- `stage-plan-base.md` - Base structure for all plans
- `functional-design-plan.md` - Functional design specific
- `code-generation-plan.md` - Code generation specific

---

### 5. State Tracking (`state/`)

**Purpose:** Standard structure for workflow state tracking

**When to use:** When creating or updating `aidlc-state.md`

**Example:**
```markdown
**Template:** `templates/state/aidlc-state.md`

**Update:**
- Mark current stage as [x] COMPLETED
- Update "Current Stage" field
- Add timestamp
```

**Key templates:**
- `aidlc-state.md` - Complete state file structure
- `workflow-progress-section.md` - Just the progress tracking part

---

### 6. Artifacts (`artifacts/`)

**Purpose:** Complete document templates for generated artifacts

**When to use:** When creating any artifact document (requirements, stories, designs, etc.)

**Example:**
```markdown
**Template:** `templates/artifacts/functional-design/business-logic-model.md`

**Include:**
- Overview and main processing flow
- Decision points
- Business workflows
- [See template for complete structure]
```

**Key template directories:**
- `requirements/` - Requirements documents
- `stories/` - User stories and personas
- `application-design/` - Components, services, dependencies
- `units/` - Unit of work documents
- `functional-design/` - Business logic, rules, entities
- `nfr/` - NFR requirements and design
- `infrastructure/` - Infrastructure design

---

## Common Usage Patterns

### Pattern 1: Creating a Plan File

```markdown
### Step X: Create Plan

**Template:** `templates/plans/stage-plan-base.md`

**Steps:**
1. Read the template
2. Copy the structure
3. Customize with stage-specific:
   - Context
   - Steps with checkboxes
   - Questions
   - Expected artifacts
4. Save to `aidlc-docs/[phase]/plans/[stage-name]-plan.md`
```

### Pattern 2: Asking Questions

```markdown
### Step X: Generate Questions

**Template:** `templates/questions/multiple-choice-format.md`

**Steps:**
1. Read the template
2. Create question file
3. Add questions using format:
   - Multiple choice (A, B, C, D)
   - MANDATORY "Other" as last option
   - [Answer]: tag for each
4. Embed in plan file or create separate file
```

### Pattern 3: Logging Interactions

```markdown
### Step X: Log User Input

**Template:** `templates/audit-logs/basic-entry.md`

**Steps:**
1. Read the template
2. Fill in:
   - Stage name
   - ISO 8601 timestamp
   - Complete raw user input (NEVER summarize)
   - AI response
   - Context
3. Append to `aidlc-docs/audit.md`
```

### Pattern 4: Presenting Completion

```markdown
### Step X: Present Completion Message

**Template:** `templates/completion-messages/2-option-standard.md`

**Steps:**
1. Read the template
2. Customize with:
   - Stage name
   - Unit name (if applicable)
   - List of artifacts created
   - Location path
3. Present to user
4. WAIT for explicit approval
```

### Pattern 5: Creating Artifacts

```markdown
### Step X: Generate [Artifact Name]

**Template:** `templates/artifacts/[category]/[artifact-name].md`

**Steps:**
1. Read the template
2. Copy the structure
3. Fill in with actual content
4. Customize sections as needed
5. Save to appropriate location
6. Update plan checkbox [x]
```

---

## Template Reference Quick Links

### Most Frequently Used

1. **Audit Log Entry** - `audit-logs/basic-entry.md` (use in every stage)
2. **2-Option Completion** - `completion-messages/2-option-standard.md` (CRITICAL for construction)
3. **Question Format** - `questions/multiple-choice-format.md` (use when asking questions)
4. **Stage Plan** - `plans/stage-plan-base.md` (use for all planning)
5. **State Tracking** - `state/aidlc-state.md` (update after each stage)

### By Phase

**INCEPTION:**
- Requirements: `artifacts/requirements/*.md`
- User Stories: `artifacts/stories/*.md`
- Application Design: `artifacts/application-design/*.md`
- Units: `artifacts/units/*.md`
- Completion: `completion-messages/inception-stage-complete.md`

**CONSTRUCTION:**
- Functional Design: `artifacts/functional-design/*.md`
- NFR: `artifacts/nfr/*.md`
- Infrastructure: `artifacts/infrastructure/*.md`
- Code Generation: `plans/code-generation-plan.md`
- Completion: `completion-messages/2-option-standard.md` (MANDATORY)

**OPERATIONS:**
- (Placeholder - templates TBD)

---

## Critical Rules

### 1. Audit Logging
- ✅ ALWAYS use `audit-logs/basic-entry.md` format
- ✅ ALWAYS log complete raw user input (never summarize)
- ✅ ALWAYS append to audit.md (never overwrite)
- ✅ ALWAYS include ISO 8601 timestamp

### 2. Completion Messages
- ✅ ALWAYS use `2-option-standard.md` for construction stages
- ✅ NEVER create 3-option menus
- ✅ NEVER create emergent navigation patterns
- ✅ ALWAYS wait for explicit user approval

### 3. Questions
- ✅ ALWAYS use `multiple-choice-format.md`
- ✅ ALWAYS include "Other" as last option
- ✅ NEVER ask questions in chat
- ✅ ALWAYS create question files

### 4. Progress Tracking
- ✅ ALWAYS update plan checkboxes [x] immediately after completing work
- ✅ ALWAYS update in SAME interaction where work is completed
- ✅ ALWAYS update aidlc-state.md after stage completion

### 5. Ambiguity Resolution
- ✅ ALWAYS analyze answers for ambiguities
- ✅ ALWAYS use `clarification-format.md` for follow-ups
- ✅ NEVER proceed with ambiguous answers
- ✅ ALWAYS resolve ALL ambiguities before continuing

---

## Troubleshooting

### Problem: Can't find the right template

**Solution:** Check the template category:
- Logging? → `audit-logs/`
- Questions? → `questions/`
- Artifacts? → `artifacts/[category]/`
- Plans? → `plans/`
- Completion? → `completion-messages/`

### Problem: Template doesn't fit my needs

**Solution:** Templates are customizable:
- Remove sections not applicable
- Add sections for specific needs
- Adjust detail level as needed
- Keep the core structure

### Problem: Not sure which completion message to use

**Solution:**
- CONSTRUCTION stages → `2-option-standard.md` (MANDATORY)
- INCEPTION stages → `inception-stage-complete.md`
- Build and Test → `build-and-test-complete.md`

### Problem: Template seems too detailed

**Solution:** Templates show maximum detail:
- Use what you need
- Skip sections not applicable
- Adjust based on complexity
- Focus on clarity over completeness

---

## Best Practices

### DO:
- ✅ Read the template before using it
- ✅ Customize templates for your context
- ✅ Follow the structure but adapt content
- ✅ Reference templates in detail files
- ✅ Keep templates and detail files in sync

### DON'T:
- ❌ Copy templates without customization
- ❌ Embed template content in detail files
- ❌ Modify templates without updating all uses
- ❌ Skip sections without good reason
- ❌ Create new formats when templates exist

---

## Getting Help

### Questions About Templates?
- Check `templates/README.md` for overview
- Check this guide for usage patterns
- Check individual template files for detailed instructions

### Questions About Workflow?
- Check detail files in `details/` directory
- Check `steering/core-workflow.md` for overall workflow
- Check `tmp/aidlc-analysis.md` for comprehensive analysis

### Need to Update Templates?
- Update the template file in `templates/` directory
- Changes automatically apply to all future uses
- No need to update detail files (they reference templates)
- Document changes in template file

---

**Last Updated:** January 28, 2026  
**Version:** 1.0  
**Status:** Phase 1 Complete
