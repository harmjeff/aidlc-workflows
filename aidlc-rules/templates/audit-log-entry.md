# Audit Log Entry Template

**Purpose:** Standard format for logging all workflow interactions

**Usage:** Use this template for every audit log entry in `aidlc-docs/audit.md`

---

## Standard Format

```markdown
## [Stage Name or Interaction Type]
**Timestamp**: [ISO 8601 timestamp]
**User Input**: "[Complete raw user input - never summarized]"
**AI Response**: "[AI's response or action taken]"
**Context**: [Stage, action, or decision made]

---
```

## Field Descriptions

- **Stage Name or Interaction Type:** Name of the workflow stage or type of interaction (e.g., "Requirements Analysis", "Code Generation - Unit 1", "Approval Request")
- **Timestamp:** ISO 8601 format timestamp (YYYY-MM-DDTHH:MM:SSZ)
- **User Input:** Complete raw user input exactly as provided - NEVER summarize or paraphrase
- **AI Response:** AI's response or action taken in response to user input
- **Context:** Additional context about the stage, action, or decision made

## Examples

### Example 1: Initial Request

```markdown
## Workflow Start - Initial Request
**Timestamp**: 2026-01-28T14:32:15Z
**User Input**: "I want to build a REST API for managing user accounts with authentication"
**AI Response**: "Starting AIDLC workflow. Performing workspace detection to determine if this is a greenfield or brownfield project."
**Context**: Initial user request logged at workflow start

---
```

### Example 2: Question Answers

```markdown
## Requirements Analysis - Question Answers Received
**Timestamp**: 2026-01-28T15:45:30Z
**User Input**: "I've answered all the questions in requirement-verification-questions.md"
**AI Response**: "Reading answers from requirement-verification-questions.md. Analyzing for ambiguities."
**Context**: Requirements Analysis stage, collecting user answers to clarification questions

---
```

### Example 3: Approval Response

```markdown
## Functional Design Approval - unit-auth-service
**Timestamp**: 2026-01-28T16:20:45Z
**User Input**: "✅ Continue to Next Stage"
**AI Response**: "User approved functional design. Proceeding to NFR Requirements stage."
**Context**: Functional Design stage completed for unit-auth-service

---
```

## Critical Rules

1. **ALWAYS log with timestamp** - Use ISO 8601 format
2. **NEVER summarize user input** - Capture complete raw input exactly as provided
3. **ALWAYS append** - Never overwrite the entire audit.md file
4. **Log EVERY interaction** - Not just approvals, but all user inputs
5. **Include context** - Provide stage and action context for each entry
