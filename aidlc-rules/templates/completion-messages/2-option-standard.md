# Standardized 2-Option Completion Message Template

**CRITICAL**: This is the MANDATORY format for all CONSTRUCTION phase stage completions.

**NO EMERGENT BEHAVIOR**: Do NOT create 3-option menus or other navigation patterns.

## Template

```markdown
# 🔧 [Stage Name] Complete - [unit-name]

I've completed the [stage name] for the **[unit-name]** unit.

**Artifacts Created:**
- ✅ `[artifact1].md` - [Brief description]
- ✅ `[artifact2].md` - [Brief description]
- ✅ `[artifact3].md` - [Brief description]

**Location:** `aidlc-docs/construction/{unit-name}/[stage-folder]/`

---

**What would you like to do?**

🔧 **Request Changes** - Ask for modifications to the [artifacts]

✅ **Continue to Next Stage** - Approve and proceed to [next stage name]

---

Please choose one of the options above.
```

## Customization Points

Replace these placeholders:

- `[Stage Name]` - e.g., "Functional Design", "NFR Requirements", "Code Generation"
- `[unit-name]` - The specific unit being worked on
- `[stage name]` - Lowercase version for sentence
- `[artifact1].md`, `[artifact2].md`, etc. - Actual artifact filenames
- `[Brief description]` - One-line description of each artifact
- `[stage-folder]` - e.g., "functional-design", "nfr-requirements"
- `[artifacts]` - Reference to what was created
- `[next stage name]` - The stage that comes next

## Examples

### Example 1: Functional Design Complete

```markdown
# 🔧 Functional Design Complete - user-service

I've completed the functional design for the **user-service** unit.

**Artifacts Created:**
- ✅ `business-logic-model.md` - Core business logic and workflows
- ✅ `business-rules.md` - Validation rules and business constraints
- ✅ `domain-entities.md` - Entity definitions and relationships

**Location:** `aidlc-docs/construction/user-service/functional-design/`

---

**What would you like to do?**

🔧 **Request Changes** - Ask for modifications to the functional design

✅ **Continue to Next Stage** - Approve and proceed to NFR Requirements

---

Please choose one of the options above.
```

### Example 2: Code Generation Complete

```markdown
# 🔧 Code Generation Complete - payment-service

I've completed the code generation for the **payment-service** unit.

**Artifacts Created:**
- ✅ `PaymentService.ts` - Business logic implementation
- ✅ `PaymentController.ts` - API endpoints
- ✅ `PaymentRepository.ts` - Data access layer
- ✅ `payment.test.ts` - Unit tests
- ✅ `payment-api.md` - API documentation

**Location:** `aidlc-docs/construction/payment-service/code/`

---

**What would you like to do?**

🔧 **Request Changes** - Ask for modifications to the generated code

✅ **Continue to Next Stage** - Approve and proceed to next unit or Build and Test

---

Please choose one of the options above.
```

## Usage in Detail Files

Reference this template in detail files:

```markdown
### Step X: Present Completion Message

**MANDATORY:** Use the standardized 2-option completion message format.

**Template:** See `templates/completion-messages/2-option-standard.md`

**Customize with:**
- Stage Name: [Current stage]
- Unit Name: [Current unit]
- Artifacts: [List of created files]
- Next Stage: [What comes next]

**CRITICAL:** Do NOT create 3-option menus or emergent navigation patterns.
```

## Critical Rules

1. **ALWAYS use exactly 2 options** - Request Changes OR Continue
2. **NO 3-option menus** - This is emergent behavior and prohibited
3. **Use emoji consistently** - 🔧 for changes, ✅ for continue
4. **List all artifacts** - Be specific about what was created
5. **Include location** - Show where files are saved
6. **Be clear about next step** - Tell user what "Continue" means

## Why This Format?

- **Simplicity**: Two clear choices reduce decision paralysis
- **Consistency**: Same format across all construction stages
- **Control**: User has clear control over workflow progression
- **Clarity**: No ambiguity about what each option does

## Prohibited Patterns

❌ **DO NOT** create 3-option menus like:
- Option 1: Request Changes
- Option 2: Continue to Next Stage
- Option 3: Skip to Different Stage

❌ **DO NOT** add navigation options like:
- "Go back to previous stage"
- "Jump to different phase"
- "Review all artifacts"

✅ **DO** keep it simple: Request Changes OR Continue
