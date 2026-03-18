# Audit Logging Requirements

**Purpose:** Complete audit trail of all workflow interactions

**CRITICAL:** These requirements are MANDATORY and must be followed without exception.

---

## Mandatory Logging Rules

### 1. Log EVERY User Input
- Log with ISO 8601 timestamp (YYYY-MM-DDTHH:MM:SSZ)
- Capture user's COMPLETE RAW INPUT exactly as provided
- NEVER summarize or paraphrase user input
- Log in aidlc-docs/audit.md

### 2. Log EVERY Approval Prompt
- Log with timestamp BEFORE asking the user
- Include complete prompt text
- Include stage context

### 3. Log EVERY User Response
- Log with timestamp AFTER receiving response
- Include complete response text
- Include decision made

### 4. Log ALL Interactions
- Not just approvals - log questions, clarifications, changes
- Include stage context for each entry
- Maintain chronological order

---

## Audit Log Format

**See Template:** `../templates/audit-log-entry.md` for the complete standard format with examples.

**Quick Reference:**

```markdown
## [Stage Name or Interaction Type]
**Timestamp**: [ISO 8601 timestamp]
**User Input**: "[Complete raw user input - never summarized]"
**AI Response**: "[AI's response or action taken]"
**Context**: [Stage, action, or decision made]

---
```

---

## File Management Rules

### ✅ CORRECT Approach
1. Read the audit.md file
2. Append new entry to the end
3. Save the file

### ❌ WRONG Approach
1. Read the audit.md file
2. Overwrite entire file with old content + new entry
3. This causes duplication and potential data loss

**Always use APPEND operations, never OVERWRITE.**

---

## What to Log

### Initial Workflow Start
- User's original request (complete raw input)
- Workspace detection findings
- Initial assessment

### Each Stage
- Stage entry with timestamp
- Questions asked (if any)
- User answers received
- Approval prompts sent
- User approval/rejection responses
- Stage completion

### Mid-Workflow Changes
- User requests for changes
- Plan modifications
- Stage skipping/addition requests

### Workflow End
- Final completion timestamp
- Summary of stages executed
- Summary of stages skipped

---

## Timestamp Format

**Use ISO 8601 format:** YYYY-MM-DDTHH:MM:SSZ

Examples:
- `2026-01-28T14:32:15Z`
- `2026-01-28T09:15:00Z`
- `2026-01-28T23:45:30Z`

---

## Context Information

Include in each log entry:
- **Stage:** Which workflow stage (e.g., "Requirements Analysis", "Code Generation - Unit 1")
- **Action:** What happened (e.g., "Questions generated", "Approval received", "Plan modified")
- **Decision:** What was decided (e.g., "Proceed to next stage", "Regenerate with changes")

---

## Rationale

**Why complete audit trail?**
- Enables workflow resumption
- Provides traceability for decisions
- Documents user requirements exactly as stated
- Supports debugging and improvement
- Creates accountability

**Why never summarize?**
- Preserves exact user intent
- Prevents misinterpretation
- Maintains legal/compliance record
- Enables accurate resumption

**Why append only?**
- Prevents data loss
- Maintains chronological integrity
- Avoids duplication
- Improves performance

---

**Keep this file loaded:** Audit logging applies throughout entire workflow.
