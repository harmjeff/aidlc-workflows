# Approval Prompt Template

**Purpose:** Standard format for requesting user approval at stage completion

**Usage:** Use this template when requesting approval to proceed to next stage

---

## Standard Approval Prompt Format

```markdown
# ✅ Ready to [Action] - [unit-name if applicable]

[Brief description of what has been completed and what will happen next]

**[Summary of work completed or plan created]**

**Proceed with [action]?**

A) Yes, proceed with [action]
B) No, I want to review/modify [what] first

[Answer]: 
```

## Examples by Context

### Approval to Proceed with Generation

```markdown
# ✅ Ready to Generate Functional Design - auth-service

All clarifying questions have been answered. I'm ready to generate the functional design artifacts:

1. **business-logic-model.md** - Business logic flow and processing model
2. **business-rules.md** - Business rules, validations, and constraints
3. **domain-entities.md** - Domain entities and relationships

**Proceed with generation?**

A) Yes, proceed with generation
B) No, I want to review/modify the plan first

[Answer]: 
```

### Approval of Plan

```markdown
# ✅ Ready to Execute Code Generation Plan - auth-service

I've created a detailed code generation plan with 20 steps covering:
- Business logic layer
- API layer
- Repository layer
- Database migrations
- Documentation
- Deployment artifacts

**Plan Location:** `aidlc-docs/construction/plans/auth-service-code-generation-plan.md`

**Proceed with executing this plan?**

A) Yes, proceed with code generation
B) No, I want to review/modify the plan first

[Answer]: 
```

### Approval to Proceed to Next Stage

```markdown
# ✅ Ready to Proceed to Next Stage

Requirements Analysis is complete. All requirements have been documented and clarified.

**Artifacts Created:**
- requirements.md
- requirement-verification-questions.md (with answers)

**Next Stage:** User Stories

**Proceed to User Stories stage?**

A) Yes, proceed to User Stories
B) No, I want to review/modify requirements first

[Answer]: 
```

## Critical Rules

1. **Always log approval prompt** in audit.md BEFORE asking user
2. **Use clear action description** - User should know what will happen
3. **Provide context** - Show what was completed or what will be done
4. **Two options** - Yes/No or Proceed/Review format
5. **Wait for explicit response** - Do NOT proceed without user confirmation
6. **Log user response** in audit.md AFTER receiving it

## Audit Log Format for Approval Prompts

### Before Asking

```markdown
## [Stage Name] - Approval Request
**Timestamp**: [ISO 8601 timestamp]
**User Input**: N/A
**AI Response**: "Requesting approval to proceed with [action]. Approval prompt presented to user."
**Context**: [Stage name], requesting approval to [action]

---
```

### After Receiving Response

```markdown
## [Stage Name] - Approval Response
**Timestamp**: [ISO 8601 timestamp]
**User Input**: "[Complete raw user response]"
**AI Response**: "User approved. Proceeding with [action]." OR "User requested changes. Returning to [step]."
**Context**: [Stage name], user [approved/requested changes]

---
```
