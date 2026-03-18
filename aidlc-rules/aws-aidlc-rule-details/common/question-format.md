# Question Format Requirements

**Purpose:** Structured question collection and ambiguity resolution

**CRITICAL:** NEVER ask questions in chat. ALL questions must be in dedicated .md files.

---

## Mandatory Question Rules

**See Template:** `../templates/question-format.md` for the complete standard format with examples.

### Rule 1: Questions in Files Only

**NEVER ask questions directly in chat.**

ALL questions must be placed in dedicated question files:
- `requirement-verification-questions.md`
- `{stage-name}-plan.md` (with embedded questions)
- `{stage-name}-clarification-questions.md`

### Rule 2: Multiple Choice Format

**Quick Reference:**

```markdown
## Question [Number]
[Clear, specific question text]

A) [First meaningful option]
B) [Second meaningful option]
[...additional options as needed...]
X) Other (please describe after [Answer]: tag below)

[Answer]: 
```

### Rule 3: Mandatory "Other" Option

**CRITICAL:** "Other" is MANDATORY as the LAST option for every question.

### Rule 4: Meaningful Options Only

- Only include options that make sense for the question
- Don't make up options just to fill slots
- Minimum 2 meaningful options + "Other"
- Maximum as many as needed (no artificial limit)

---

## Ambiguity Detection (MANDATORY)

**After collecting answers, MUST analyze for ambiguities.**

### Ambiguity Indicators

Look for these patterns in answers:
- "depends"
- "maybe"
- "not sure"
- "mix of"
- "somewhere between"
- "standard"
- "typical"
- "probably"
- "usually"
- Contradictions between answers
- Vague or borderline responses
- Multiple options selected without clear priority

### Ambiguity Resolution Process

1. **Analyze all collected answers**
2. **Identify ambiguous responses**
3. **Create clarification question file** if issues found
4. **Ask follow-up questions** with same format
5. **Repeat until ALL ambiguities resolved**
6. **Do NOT proceed** to next stage until clarity achieved

### Example Clarification Questions

```markdown
# Requirements Clarification - Follow-Up Questions

Based on your previous answers, I need clarification on the following:

## Question 1
You mentioned "standard authentication". Which specific standard?

A) OAuth 2.0
B) SAML 2.0
C) OpenID Connect
D) Basic HTTP Authentication
E) Other (please describe after [Answer]: tag below)

[Answer]: 

## Question 2
You said "depends on the use case". Can you specify the primary use case?

A) Internal employee access only
B) External customer access only
C) Both internal and external access
D) Partner/vendor access
E) Other (please describe after [Answer]: tag below)

[Answer]: 
```

---

## Contradiction Detection

### Example Contradiction

**Question 3 Answer:** "This is a simple CRUD application"  
**Question 7 Answer:** "We need complex business rules and workflow engine"

**Resolution:** Create follow-up questions to clarify complexity level and specific requirements.

---

## Question Generation Guidelines

### When to Generate Questions

**ALWAYS generate questions unless:**
- Request is exceptionally clear and specific
- All necessary information explicitly provided
- No ambiguity exists in requirements

**Default to asking questions** - Better to ask too many than make wrong assumptions.

### Question Categories to Consider

Evaluate ALL categories before deciding to skip questions:

**Functional Requirements:**
- Core features and capabilities
- User workflows and interactions
- Data models and entities
- Business rules and logic

**Non-Functional Requirements:**
- Performance expectations
- Security requirements
- Scalability needs
- Reliability requirements

**Technical Context:**
- Existing systems and integrations
- Technology preferences or constraints
- Deployment environment
- Development constraints

**Business Context:**
- User types and personas
- Business goals and success criteria
- Timeline and priorities
- Budget or resource constraints

---

## Rationale

**Why questions in files?**
- Provides clear documentation
- Enables review and revision
- Prevents ambiguous verbal exchanges
- Creates traceable record

**Why multiple choice?**
- Faster for users to answer
- Reduces ambiguity
- Provides structure
- Easier to parse programmatically

**Why mandatory "Other"?**
- Prevents forcing incorrect choices
- Captures edge cases
- Allows flexibility
- Improves accuracy

**Why ambiguity resolution?**
- Prevents incorrect assumptions
- Ensures clarity before implementation
- Reduces rework
- Improves quality

---

**Keep this file loaded:** Question format applies throughout entire workflow.
