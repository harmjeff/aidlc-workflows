# Workspace Detection

**Purpose:** Determine project context (brownfield vs greenfield) and establish workflow resumption capability.

**Stage Type:** ALWAYS

**Phase:** INCEPTION

**Load this file when:** Starting a new AIDLC workflow

**Unload this file after:** Workspace detection is complete and auto-proceed to next stage

---

## Execute IF

**ALWAYS** - This stage executes for every workflow.

## Skip IF

Never skipped - this is a mandatory stage.

---

## Steps

### Step 1: Log Initial User Request
**Action:** Log the complete raw user input in audit.md.

**Template:** `../../templates/audit-logs/basic-entry.md`

**CRITICAL:** Never summarize or paraphrase the user's request.

### Step 2: Check for Existing Workflow State
**Action:** Look for `aidlc-docs/aidlc-state.md` file.

**IF EXISTS:** This is a workflow resumption
- Read the file to understand current state
- Follow session continuity procedures (see common/session-continuity.md)
- Present "Welcome Back" message to user
- Skip remaining workspace detection steps

**IF NOT EXISTS:** This is a new workflow
- Continue to next step

### Step 3: Scan Workspace for Existing Code
**Action:** Search for common project indicators:
- Source code directories (src/, lib/, app/, packages/)
- Package management files (package.json, pom.xml, requirements.txt, etc.)
- Build configuration files
- Framework indicators
- Infrastructure as Code

### Step 4: Determine Project Type
**Action:** Classify the project:

**Brownfield Project:** Existing codebase detected
- Existing source code files found
- Existing project structure present

**Greenfield Project:** No existing codebase
- Empty workspace or minimal files
- Starting from scratch

### Step 5: Check for Existing Reverse Engineering Artifacts
**Action:** Only if Brownfield Project - Look for `aidlc-docs/inception/reverse-engineering/` directory.

**Check for artifacts:**
- business-overview.md
- architecture.md
- code-structure.md
- api-documentation.md
- component-inventory.md
- technology-stack.md
- dependencies.md
- code-quality-assessment.md
- reverse-engineering-timestamp.md

**IF ALL ARTIFACTS EXIST:** Reverse engineering already completed
**IF MISSING OR INCOMPLETE:** Reverse engineering needed

### Step 6: Create Initial aidlc-state.md
**Action:** Only if new workflow - Create `aidlc-docs/aidlc-state.md`.

**Template:** `../../templates/state/aidlc-state.md`

**Customize with:**
- Project Type: [Brownfield/Greenfield]
- Current Phase: INCEPTION
- Current Stage: Workspace Detection
- Reverse Engineering Needed: [Yes/No]

### Step 7: Log Findings in audit.md
**Action:** Append detection results to audit.md.

**Template:** `../../templates/audit-logs/basic-entry.md`

**Include:**
- Project type determination
- Reverse engineering artifact status
- Next stage determination

### Step 8: Determine Next Stage
**Action:** Determine the next stage based on findings:

- **IF Brownfield AND No Reverse Engineering Artifacts:** → Reverse Engineering
- **IF Brownfield AND Reverse Engineering Artifacts Exist:** → Requirements Analysis
- **IF Greenfield:** → Requirements Analysis

### Step 9: Present Completion Message to User
**Action:** Present appropriate completion message based on project type.

**For Brownfield Project (No Artifacts):**
```markdown
# 🔍 Workspace Detection Complete

**Project Type:** Brownfield (existing codebase detected)
**Reverse Engineering Status:** Not yet performed
**Next Stage:** Reverse Engineering

I detected existing code in your workspace. I'll now analyze your existing codebase to understand its structure, architecture, and components.

---
```

**For Brownfield Project (Artifacts Exist):**
```markdown
# 🔍 Workspace Detection Complete

**Project Type:** Brownfield (existing codebase detected)
**Reverse Engineering Status:** Already completed
**Next Stage:** Requirements Analysis

I found existing reverse engineering artifacts. I'll use these to understand your codebase and proceed to requirements analysis.

---
```

**For Greenfield Project:**
```markdown
# 🔍 Workspace Detection Complete

**Project Type:** Greenfield (new project)
**Next Stage:** Requirements Analysis

This is a new project starting from scratch. I'll now proceed to understand what you want to build.

---
```

### Step 10: Automatically Proceed to Next Stage
**Action:** **NO APPROVAL NEEDED** - This stage auto-proceeds.

Move directly to the next stage (Reverse Engineering or Requirements Analysis).

---

## Artifacts Created

1. **aidlc-docs/aidlc-state.md** (if new workflow)
2. **Audit log entries in aidlc-docs/audit.md**

---

## Key Principles

1. **Auto-Proceed:** This is the ONLY stage that auto-proceeds without approval
2. **Complete Raw Input:** Never summarize user input in audit.md
3. **Brownfield vs Greenfield:** Detection determines workflow path
4. **Artifact Reuse:** Reuses previous reverse engineering work when available

---

## Templates Reference

All templates are located in `../../templates/` directory:

- **Audit Logs:** `audit-logs/basic-entry.md`
- **State:** `state/aidlc-state.md`

---

## Next Stage

- **IF Brownfield (no artifacts):** Reverse Engineering
- **IF Brownfield (artifacts exist):** Requirements Analysis
- **IF Greenfield:** Requirements Analysis

---

**End of Workspace Detection Stage Instructions**
