# Basic Audit Log Entry Template

Use this format for logging all workflow interactions in `aidlc-docs/audit.md`.

## Format

```markdown
## [Stage Name or Interaction Type]
**Timestamp**: [ISO 8601 timestamp - YYYY-MM-DDTHH:MM:SSZ]
**User Input**: "[Complete raw user input - never summarized]"
**AI Response**: "[AI's response or action taken]"
**Context**: [Stage, action, or decision made]

---
```

## Usage Guidelines

### Timestamp
- Use ISO 8601 format: `2026-01-28T14:30:00Z`
- Always include timezone (Z for UTC)
- Log at the moment of interaction

### User Input
- **CRITICAL**: Capture COMPLETE RAW INPUT exactly as provided
- **NEVER** summarize or paraphrase
- Include full text even if lengthy
- Use quotes around the input

### AI Response
- Describe what action was taken
- Include key decisions made
- Keep concise but complete

### Context
- Specify which stage/phase
- Note what decision was made
- Include relevant metadata

## Examples

### Example 1: User Request
```markdown
## Workspace Detection - Initial Request
**Timestamp**: 2026-01-28T14:30:00Z
**User Input**: "I need to add authentication to my Express.js API"
**AI Response**: "Starting Workspace Detection to analyze existing codebase"
**Context**: Beginning INCEPTION phase, scanning for existing code

---
```

### Example 2: Question Response
```markdown
## Requirements Analysis - Question Response
**Timestamp**: 2026-01-28T14:35:00Z
**User Input**: "A) JWT tokens with refresh token rotation"
**AI Response**: "Recorded authentication method preference"
**Context**: Requirements Analysis, collecting answers to clarification questions

---
```

### Example 3: Approval Decision
```markdown
## Requirements Analysis - Approval
**Timestamp**: 2026-01-28T14:40:00Z
**User Input**: "Yes, the requirements look good. Let's proceed."
**AI Response**: "Requirements approved, proceeding to Workflow Planning"
**Context**: Requirements Analysis complete, user approved requirements.md

---
```

## Critical Rules

1. **ALWAYS append** to audit.md, NEVER overwrite
2. **Log EVERY interaction**, not just approvals
3. **Capture complete raw input**, no summarization
4. **Use consistent format** for all entries
5. **Include timestamp** for every entry

## Tool Usage

### ✅ CORRECT
1. Read audit.md
2. Append new entry using this template

### ❌ WRONG
1. Read audit.md
2. Overwrite entire file with old content + new entry (causes duplication)
