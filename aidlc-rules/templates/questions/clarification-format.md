# Clarification Question Format Template

Use this format when user answers contain ambiguities that need resolution.

## Template

```markdown
# [Stage Name] Clarification

**Created:** [ISO 8601 timestamp]
**Stage:** [Stage name]
**Purpose:** Resolve ambiguities from previous answers

I need some clarification on your previous answers. Please answer these follow-up questions:

---

## Clarification 1

**Your Previous Answer:** [Quote the ambiguous answer]

**Issue:** [Explain what's ambiguous or unclear]

**Follow-Up Question:** [Specific question to resolve ambiguity]

A) [Option]
B) [Option]
C) [Option]
X) Other (please describe after [Answer]: tag below)

[Answer]: 

---

## Clarification 2

**Your Previous Answer:** [Quote the ambiguous answer]

**Issue:** [Explain what's ambiguous or unclear]

**Follow-Up Question:** [Specific question to resolve ambiguity]

A) [Option]
B) [Option]
X) Other (please describe after [Answer]: tag below)

[Answer]: 

---

[Repeat for each ambiguity]
```

## When to Create Clarification Questions

**MANDATORY**: After collecting answers, analyze for ambiguities.

### Ambiguity Indicators

Look for these patterns in user answers:
- "depends"
- "maybe"
- "not sure"
- "mix of"
- "somewhere between"
- "standard"
- "typical"
- Contradictions between answers
- Vague or borderline responses
- Incomplete answers

### Resolution Process

1. **Analyze all answers** for ambiguities
2. **Identify specific issues** with each ambiguous answer
3. **Create clarification file** if ANY ambiguities found
4. **Ask follow-up questions** to resolve each ambiguity
5. **Repeat until clarity** - Keep asking until ALL resolved
6. **Do NOT proceed** to next stage until clarity achieved

## Complete Example

```markdown
# Requirements Analysis Clarification

**Created:** 2026-01-28T15:00:00Z
**Stage:** Requirements Analysis
**Purpose:** Resolve ambiguities from requirement verification questions

I need some clarification on your previous answers. Please answer these follow-up questions:

---

## Clarification 1

**Your Previous Answer:** "Question 3: C - Somewhere between 1,000 and 10,000 users"

**Issue:** The range is too broad for capacity planning. We need a more specific estimate.

**Follow-Up Question:** What is your best estimate for peak concurrent users?

A) 1,000-2,500 users
B) 2,500-5,000 users
C) 5,000-7,500 users
D) 7,500-10,000 users
E) Other (please describe after [Answer]: tag below)

[Answer]: 

---

## Clarification 2

**Your Previous Answer:** "Question 5: It depends on the user type"

**Issue:** We need to understand the authentication requirements for each user type.

**Follow-Up Question:** Should different user types have different authentication methods?

A) Yes - Admin users need MFA, regular users can use password only
B) Yes - Different authentication for each user type (please specify in Other)
C) No - All users should use the same authentication method
D) Other (please describe after [Answer]: tag below)

[Answer]: 

---

## Clarification 3

**Your Previous Answer:** "Question 7: A and C - Both REST API and GraphQL"

**Issue:** This creates complexity. We need to understand the priority.

**Follow-Up Question:** Which API style should be the primary interface?

A) REST API as primary, GraphQL as optional enhancement
B) GraphQL as primary, REST API for legacy support
C) Both equally important, full implementation of each
D) Other (please describe after [Answer]: tag below)

[Answer]: 

---
```

## File Naming Convention

Use descriptive names that indicate clarification:
- `requirement-verification-clarification.md`
- `story-planning-clarification.md`
- `functional-design-clarification.md`
- `nfr-requirements-clarification.md`

## Usage in Detail Files

Reference this template:

```markdown
### Step X: Analyze Answers for Ambiguities

**MANDATORY:** After collecting answers, analyze for ambiguities.

**Look for:**
- "depends", "maybe", "not sure", "mix of", "somewhere between"
- Contradictions between answers
- Vague or borderline responses

**If ambiguities found:**
1. Create clarification file using `templates/questions/clarification-format.md`
2. Ask follow-up questions for EACH ambiguity
3. Request user to answer clarification questions
4. Repeat until ALL ambiguities resolved

**CRITICAL:** Do NOT proceed to next stage until clarity achieved.
```

## Why Clarification is Critical

**Problem**: Ambiguous requirements lead to incorrect implementations.

**Solution**: Better to ask clarifying questions than to make wrong assumptions.

**Benefits**:
- Prevents costly rework
- Ensures correct understanding
- Builds confidence in requirements
- Reduces implementation risks

## Guidelines for Clarification Questions

### DO:
- ✅ Quote the exact ambiguous answer
- ✅ Explain what's unclear
- ✅ Ask specific follow-up questions
- ✅ Provide clear options
- ✅ Keep asking until resolved

### DON'T:
- ❌ Proceed with ambiguity
- ❌ Make assumptions
- ❌ Accept vague answers
- ❌ Skip clarification to save time
- ❌ Assume "standard" or "typical" implementations

## After Clarification

1. **Read clarification file** to extract answers
2. **Validate resolution** - Are ambiguities resolved?
3. **Update original answers** if needed
4. **Proceed to next step** only when clarity achieved
5. **Log clarification** in audit.md

## Example Audit Log Entry

```markdown
## Requirements Analysis - Clarification Complete
**Timestamp**: 2026-01-28T15:15:00Z
**User Input**: "[User's clarification answers]"
**AI Response**: "All ambiguities resolved, proceeding with requirements generation"
**Context**: Created and resolved requirement-verification-clarification.md with 3 clarifications

---
```
