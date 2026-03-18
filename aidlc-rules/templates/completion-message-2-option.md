# Completion Message Template (2-Option Format)

**Purpose:** Standardized completion message for all construction stages

**Usage:** Use this EXACT format for completion messages in all construction stages

**Critical Rule:** MANDATORY 2-option format - NO emergent 3-option behavior allowed

---

## Standard Format

```markdown
# 🔧 [Stage Name] Complete - [unit-name]

I've completed the [stage name] for the **[unit-name]** unit.

**Artifacts Created:**
- ✅ `[artifact-1].md` - [Description]
- ✅ `[artifact-2].md` - [Description]
- ✅ `[artifact-3].md` - [Description]

**Location:** `aidlc-docs/construction/{unit-name}/[stage-folder]/`

---

**What would you like to do?**

🔧 **Request Changes** - Ask for modifications to the [stage name]

✅ **Continue to Next Stage** - Approve and proceed to the next stage

---

Please choose one of the options above.
```

## Field Descriptions

- **Stage Name:** Name of the completed stage (e.g., "Functional Design", "NFR Requirements")
- **unit-name:** Name of the unit of work
- **Artifacts Created:** List of all artifacts created with checkmarks
- **Location:** Path to where artifacts are stored
- **Two Options:** EXACTLY two options - Request Changes OR Continue to Next Stage

## Examples by Stage

### Functional Design

```markdown
# 🔧 Functional Design Complete - auth-service

I've completed the functional design for the **auth-service** unit.

**Artifacts Created:**
- ✅ `business-logic-model.md` - Business logic flow and processing model
- ✅ `business-rules.md` - Business rules, validations, and constraints
- ✅ `domain-entities.md` - Domain entities and relationships

**Location:** `aidlc-docs/construction/auth-service/functional-design/`

---

**What would you like to do?**

🔧 **Request Changes** - Ask for modifications to the functional design

✅ **Continue to Next Stage** - Approve and proceed to the next stage

---

Please choose one of the options above.
```

### NFR Requirements

```markdown
# 🔧 NFR Requirements Complete - auth-service

I've completed the NFR requirements assessment for the **auth-service** unit.

**Artifacts Created:**
- ✅ `nfr-requirements.md` - Comprehensive NFR requirements
- ✅ `tech-stack-decisions.md` - Technology stack decisions and rationale

**Location:** `aidlc-docs/construction/auth-service/nfr-requirements/`

---

**What would you like to do?**

🔧 **Request Changes** - Ask for modifications to the NFR requirements

✅ **Continue to Next Stage** - Approve and proceed to the next stage

---

Please choose one of the options above.
```

### NFR Design

```markdown
# 🔧 NFR Design Complete - auth-service

I've completed the NFR design for the **auth-service** unit.

**Artifacts Created:**
- ✅ `nfr-design-patterns.md` - NFR design patterns and implementations
- ✅ `logical-components.md` - Logical component architecture

**Location:** `aidlc-docs/construction/auth-service/nfr-design/`

---

**What would you like to do?**

🔧 **Request Changes** - Ask for modifications to the NFR design

✅ **Continue to Next Stage** - Approve and proceed to the next stage

---

Please choose one of the options above.
```

### Infrastructure Design

```markdown
# 🔧 Infrastructure Design Complete - auth-service

I've completed the infrastructure design for the **auth-service** unit.

**Artifacts Created:**
- ✅ `infrastructure-design.md` - Infrastructure services and mappings
- ✅ `deployment-architecture.md` - Deployment architecture and configuration

**Location:** `aidlc-docs/construction/auth-service/infrastructure-design/`

---

**What would you like to do?**

🔧 **Request Changes** - Ask for modifications to the infrastructure design

✅ **Continue to Next Stage** - Approve and proceed to the next stage

---

Please choose one of the options above.
```

### Code Generation

```markdown
# 🔧 Code Generation Complete - auth-service

I've completed code generation for the **auth-service** unit.

**Artifacts Created:**
- ✅ Business logic implementation
- ✅ API layer implementation
- ✅ Repository layer implementation
- ✅ Unit tests
- ✅ Integration tests
- ✅ Documentation

**Location:** `aidlc-docs/construction/auth-service/code/`

---

**What would you like to do?**

🔧 **Request Changes** - Ask for modifications to the generated code

✅ **Continue to Next Stage** - Approve and proceed to the next stage

---

Please choose one of the options above.
```

## Critical Rules

1. **EXACTLY 2 options** - Never add a third option or other emergent behavior
2. **Use emoji indicators** - 🔧 for Request Changes, ✅ for Continue
3. **Consistent wording** - Always use "Request Changes" and "Continue to Next Stage"
4. **List all artifacts** - Show what was created with checkmarks
5. **Show location** - Provide path to artifacts
6. **Wait for response** - Do NOT proceed without explicit user choice

## Prohibited Behaviors

❌ **DO NOT:**
- Add a third option like "Review Artifacts"
- Change the wording of the two options
- Proceed without waiting for user response
- Use different emoji or formatting
- Skip the artifact list
- Omit the location path

✅ **DO:**
- Use exactly this format
- Wait for explicit user choice
- Log the user's response in audit.md
- Handle both options appropriately
