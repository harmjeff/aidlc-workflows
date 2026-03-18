# AIDLC Core Workflow

**PRIORITY:** This workflow OVERRIDES all other built-in workflows for software development

**Version:** 2.0 (Optimized for Context Efficiency)

---

## 🎯 Adaptive Workflow Principle

**The workflow adapts to the work, not the other way around.**

The AI intelligently assesses what stages are needed based on:
1. User's stated intent and clarity
2. Existing codebase state (brownfield vs greenfield)
3. Complexity and scope of change
4. Risk and impact assessment

---

## 📚 Context Management Strategy

### Always in Context
- This core-workflow.md file
- aidlc-docs/aidlc-state.md (workflow state)
- aidlc-docs/audit.md (audit trail)

### Load on Demand
- Common detail files (load at workflow start, keep until workflow end)
- Stage detail files (load when entering stage, unload when stage complete)

### Loading Instructions
```
**LOAD:** Read aidlc-workflow/details/{category}/{file-name}.md
**UNLOAD:** After stage completion, you may release detail file from active context
```

---

## 🔵 INCEPTION PHASE

**Purpose:** Planning, requirements gathering, and architectural decisions  
**Focus:** Determine WHAT to build and WHY

### Stage Execution Order

1. **Workspace Detection** (ALWAYS) → Auto-proceed
2. **Reverse Engineering** (CONDITIONAL: Brownfield only) → Approval required
3. **Requirements Analysis** (ALWAYS: Adaptive depth) → Approval required
4. **User Stories** (CONDITIONAL: Intelligent assessment) → Approval required
5. **Workflow Planning** (ALWAYS) → Approval required
6. **Application Design** (CONDITIONAL: New components) → Approval required
7. **Units Generation** (CONDITIONAL: Multiple units) → Approval required

---

## 🟢 CONSTRUCTION PHASE

**Purpose:** Detailed design, NFR implementation, and code generation  
**Focus:** Determine HOW to build it

### Per-Unit Loop (Execute for Each Unit)

For each unit, execute in sequence:
1. **Functional Design** (CONDITIONAL: New data models/logic) → Approval required
2. **NFR Requirements** (CONDITIONAL: Performance/security needs) → Approval required
3. **NFR Design** (CONDITIONAL: NFR patterns needed) → Approval required
4. **Infrastructure Design** (CONDITIONAL: Infrastructure mapping) → Approval required
5. **Code Generation** (ALWAYS: Two-part) → Approval required

### After All Units Complete

6. **Build and Test** (ALWAYS) → Approval required

---

## 🟡 OPERATIONS PHASE

**Purpose:** Placeholder for future deployment and monitoring  
**Status:** Currently placeholder only

---

## 🔑 Mandatory Rules (CRITICAL)

### 1. Audit Logging (ALWAYS)
- **Log EVERY user input** with ISO 8601 timestamp in audit.md
- **Capture COMPLETE RAW INPUT** - never summarize or paraphrase
- **Log approval prompts** before asking user
- **Log user responses** after receiving
- **APPEND ONLY** - never overwrite audit.md

**Detail File:** Load `aidlc-workflow/details/common/audit-logging.md` at workflow start

### 2. Content Validation (BEFORE FILE CREATION)
- **Validate Mermaid diagrams** before writing
- **Escape special characters** properly
- **Provide text alternatives** for complex visuals
- **Test content parsing** compatibility

**Detail File:** Load `aidlc-workflow/details/common/content-validation.md` at workflow start

### 3. Question Format (NEVER IN CHAT)
- **ALL questions in .md files** with [Answer]: tags
- **Multiple choice format** (A, B, C, D, E)
- **MANDATORY "Other"** as last option
- **Analyze for ambiguities** after collecting answers
- **Create follow-up questions** until ALL ambiguities resolved

**Detail File:** Load `aidlc-workflow/details/common/question-format.md` at workflow start

### 4. Approval Gates (DO NOT PROCEED WITHOUT)
- **Wait for explicit user approval** at every approval gate
- **Present standardized 2-option message** for design/code stages:
  - 🔧 Request Changes
  - ✅ Continue to Next Stage
- **NO emergent 3-option behavior**

### 5. Checkbox Tracking (IMMEDIATE UPDATES)
- **Mark [x] immediately** after completing each plan step
- **Update in SAME interaction** where work is completed
- **Two-level tracking:** Plan-level + Stage-level (aidlc-state.md)
- **NO EXCEPTIONS**

### 6. Proactive Questioning (WHEN IN DOUBT, ASK)
- **Default to asking questions** for clarity
- **Evaluate ALL question categories** before skipping
- **Look for ambiguity indicators:** "depends", "maybe", "not sure", "standard", "typical"
- **Create follow-up questions** for unclear responses

---

## 📂 Directory Structure

```
aidlc-docs/
├── inception/
│   ├── plans/
│   ├── reverse-engineering/  (brownfield only)
│   ├── requirements/
│   ├── user-stories/
│   └── application-design/
├── construction/
│   ├── plans/
│   ├── {unit-name}/
│   │   ├── functional-design/
│   │   ├── nfr-requirements/
│   │   ├── nfr-design/
│   │   ├── infrastructure-design/
│   │   └── code/
│   └── build-and-test/
├── operations/  (placeholder)
├── aidlc-state.md
└── audit.md
```

---

## 🚀 Workflow Execution Instructions

### At Workflow Start

1. **Display welcome message (new workflows only):**
   - Load `aidlc-workflow/details/common/welcome-message.md`
   - Display message to user ONCE
   - Unload immediately after displaying

2. **Load common detail files:**
   - `aidlc-workflow/details/common/process-overview.md`
   - `aidlc-workflow/details/common/audit-logging.md`
   - `aidlc-workflow/details/common/content-validation.md`
   - `aidlc-workflow/details/common/question-format.md`
   - `aidlc-workflow/details/common/overconfidence-prevention.md`

3. **Check for existing workflow:**
   - If aidlc-state.md exists, load `aidlc-workflow/details/common/session-continuity.md`
   - Resume from current stage

4. **Start new workflow:**
   - Begin with Workspace Detection

### On-Demand Common Files

Load these common files only when needed:
- `common/depth-levels.md` - When understanding adaptive depth concept
- `common/error-handling.md` - When errors occur or resuming with issues
- `common/workflow-changes.md` - When user requests workflow modifications

### At Each Stage

1. **Load stage detail file:**
   - `aidlc-workflow/details/{phase}/{stage-name}.md`

2. **Execute stage steps** as defined in detail file

3. **Update progress:**
   - Mark checkboxes in plan files
   - Update aidlc-state.md

4. **Log all interactions** in audit.md

5. **Wait for approval** (if required)

6. **Unload stage detail file** after completion

### At Workflow End

- Keep common detail files loaded
- Unload all stage detail files
- Final audit log entry

---

## 🔄 Stage Conditional Logic Quick Reference

| Stage | Execute IF | Skip IF |
|-------|-----------|---------|
| Workspace Detection | ALWAYS | Never |
| Reverse Engineering | Brownfield + No artifacts | Greenfield OR Artifacts exist |
| Requirements Analysis | ALWAYS (adaptive depth) | Never |
| User Stories | User-facing OR Complex OR Multi-persona | Pure refactoring OR Simple bug fix |
| Workflow Planning | ALWAYS | Never |
| Application Design | New components OR Service layer | Changes within existing boundaries |
| Units Generation | Multiple units OR Complex breakdown | Single simple unit |
| Functional Design | New data models OR Complex logic | Simple logic changes |
| NFR Requirements | Performance OR Security OR Scalability | No NFR needs |
| NFR Design | NFR Requirements executed | NFR Requirements skipped |
| Infrastructure Design | Infrastructure mapping needed | No infrastructure changes |
| Code Generation | ALWAYS (per-unit) | Never |
| Build and Test | ALWAYS | Never |

---

## 📋 Approval Gates Checklist

- [ ] Reverse Engineering (if executed)
- [ ] Requirements Analysis
- [ ] User Stories - Planning (if executed)
- [ ] User Stories - Generation (if executed)
- [ ] Workflow Planning
- [ ] Application Design (if executed)
- [ ] Units Generation - Planning (if executed)
- [ ] Units Generation - Generation (if executed)
- [ ] Functional Design (per-unit, if executed)
- [ ] NFR Requirements (per-unit, if executed)
- [ ] NFR Design (per-unit, if executed)
- [ ] Infrastructure Design (per-unit, if executed)
- [ ] Code Generation - Planning (per-unit)
- [ ] Code Generation - Generation (per-unit)
- [ ] Build and Test

---

## 🎯 Key Principles

1. **Adaptive Execution** - Only execute stages that add value
2. **Transparent Planning** - Always show execution plan before starting
3. **User Control** - User can request stage inclusion/exclusion
4. **Progress Tracking** - Update aidlc-state.md continuously
5. **Complete Audit Trail** - Log ALL interactions with complete raw input
6. **Quality Focus** - Complex changes get full treatment, simple changes stay efficient
7. **Content Validation** - Always validate before file creation
8. **NO EMERGENT BEHAVIOR** - Use standardized completion messages only

---

## 📖 Detail File Reference

### Common (Load at Start)
- `common/process-overview.md` - Workflow overview and phase descriptions
- `common/audit-logging.md` - Complete audit logging requirements
- `common/content-validation.md` - Mermaid and content validation rules
- `common/question-format.md` - Question formatting and ambiguity resolution
- `common/overconfidence-prevention.md` - Proactive questioning principles
- `common/session-continuity.md` - Resume workflow instructions (load when resuming)
- `common/welcome-message.md` - User welcome message (load once, display, unload)

### Common (Load on Demand)
- `common/depth-levels.md` - Adaptive depth explanation
- `common/error-handling.md` - Error recovery procedures
- `common/workflow-changes.md` - Mid-workflow change handling

### Inception (Load on Demand)
- `inception/workspace-detection.md` - Brownfield/greenfield detection
- `inception/reverse-engineering.md` - Codebase analysis steps
- `inception/requirements-analysis.md` - Requirements gathering with adaptive depth
- `inception/user-stories.md` - Story generation with intelligent assessment
- `inception/workflow-planning.md` - Execution plan creation
- `inception/application-design.md` - Component and service design
- `inception/units-generation.md` - Unit of work decomposition

### Construction (Load on Demand)
- `construction/functional-design.md` - Business logic design per unit
- `construction/nfr-requirements.md` - NFR assessment per unit
- `construction/nfr-design.md` - NFR pattern incorporation per unit
- `construction/infrastructure-design.md` - Infrastructure mapping per unit
- `construction/code-generation.md` - Code generation per unit (two-part)
- `construction/build-and-test.md` - Build and test instructions

### Operations (Placeholder)
- `operations/operations.md` - Future deployment and monitoring

---

**End of Core Workflow**

**Remember:** Load detail files as needed, unload after stage completion to minimize context usage.
