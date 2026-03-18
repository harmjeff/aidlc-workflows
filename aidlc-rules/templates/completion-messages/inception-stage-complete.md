# Inception Stage Completion Message Template

Use this format for INCEPTION phase stage completions.

## Template

```markdown
# ✅ [Stage Name] Complete

I've completed the [stage name] stage.

**Artifacts Created:**
- ✅ `[artifact1].md` - [Brief description]
- ✅ `[artifact2].md` - [Brief description]
- ✅ `[artifact3].md` - [Brief description]

**Location:** `aidlc-docs/inception/[stage-folder]/`

**Summary:**
[1-2 sentence summary of what was accomplished]

---

**Ready to proceed to [Next Stage Name]?**

Please confirm to continue, or let me know if you'd like any changes.
```

## Customization Points

- `[Stage Name]` - e.g., "Requirements Analysis", "User Stories", "Application Design"
- `[stage name]` - Lowercase version
- `[artifact1].md`, etc. - Actual artifact filenames
- `[Brief description]` - One-line description
- `[stage-folder]` - e.g., "requirements", "user-stories", "application-design"
- `[Next Stage Name]` - What comes next

## Examples

### Example 1: Requirements Analysis Complete

```markdown
# ✅ Requirements Analysis Complete

I've completed the requirements analysis stage.

**Artifacts Created:**
- ✅ `requirements.md` - Comprehensive requirements document with functional and non-functional requirements
- ✅ `requirement-verification-questions.md` - Clarification questions and answers

**Location:** `aidlc-docs/inception/requirements/`

**Summary:**
Analyzed your request and documented 8 functional requirements and 5 non-functional requirements. All ambiguities have been resolved through clarification questions.

---

**Ready to proceed to Workflow Planning?**

Please confirm to continue, or let me know if you'd like any changes.
```

### Example 2: User Stories Complete

```markdown
# ✅ User Stories Complete

I've completed the user stories stage.

**Artifacts Created:**
- ✅ `stories.md` - 12 user stories organized into 3 epics with acceptance criteria
- ✅ `personas.md` - 3 user personas representing different stakeholder types

**Location:** `aidlc-docs/inception/user-stories/`

**Summary:**
Created comprehensive user stories covering all requirements with clear acceptance criteria. Defined 3 personas: End User, Administrator, and API Consumer.

---

**Ready to proceed to Workflow Planning?**

Please confirm to continue, or let me know if you'd like any changes.
```

### Example 3: Application Design Complete

```markdown
# ✅ Application Design Complete

I've completed the application design stage.

**Artifacts Created:**
- ✅ `components.md` - 8 components across presentation, business logic, and data access layers
- ✅ `component-methods.md` - Detailed method signatures for all components
- ✅ `services.md` - 3 service definitions with responsibilities
- ✅ `component-dependency.md` - Component dependency graph and relationships

**Location:** `aidlc-docs/inception/application-design/`

**Summary:**
Designed complete application architecture with clear component boundaries, method signatures, and dependency relationships. System is ready for decomposition into units of work.

---

**Ready to proceed to Units Generation?**

Please confirm to continue, or let me know if you'd like any changes.
```

## Differences from Construction Format

### Inception Format:
- ✅ emoji (checkmark)
- Simpler approval language
- "Ready to proceed to [Next Stage]?"
- More conversational tone

### Construction Format:
- 🔧 emoji (wrench)
- Explicit 2-option menu
- Unit-specific
- More structured

## Usage in Detail Files

```markdown
### Step X: Present Completion Message

**Format:** See `templates/completion-messages/inception-stage-complete.md`

**Customize with:**
- Stage Name: [Current stage]
- Artifacts: [List of created files]
- Summary: [Brief accomplishment summary]
- Next Stage: [What comes next]
```

## When to Use

Use this template for:
- Workspace Detection (auto-proceed, no approval)
- Reverse Engineering
- Requirements Analysis
- User Stories
- Workflow Planning
- Application Design
- Units Generation

Do NOT use for:
- Construction phase stages (use 2-option-standard.md)
- Build and Test (use build-and-test-complete.md)
