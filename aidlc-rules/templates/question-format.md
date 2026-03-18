# Question Format Template

**Purpose:** Standard format for all questions in the AIDLC workflow

**Usage:** Use this template when creating question files at any stage

**Critical Rule:** NEVER ask questions in chat - ALL questions must be in dedicated .md files

---

## Standard Question Format

```markdown
## Question [Number]
[Clear, specific question text]

A) [First meaningful option]
B) [Second meaningful option]
C) [Third meaningful option]
[...additional options as needed...]
X) Other (please describe after [Answer]: tag below)

[Answer]: 
```

## Field Descriptions

- **Question Number:** Sequential number for the question
- **Question Text:** Clear, specific question that needs to be answered
- **Options A, B, C, etc.:** Meaningful options that make sense for the question
- **Option X (Other):** MANDATORY last option for every question
- **[Answer]: tag:** Where user will provide their answer

## Critical Requirements

1. **"Other" is MANDATORY** as the LAST option for every question
2. **Only include meaningful options** - Don't make up options just to fill slots
3. **Minimum 2 meaningful options + "Other"**
4. **No artificial maximum** - Use as many options as needed
5. **Use [Answer]: tags** for all responses

## Complete Example

```markdown
# Requirements Clarification Questions

Please answer the following questions to help clarify the requirements.

## Question 1
What is the primary user authentication method?

A) Username and password
B) Social media login (Google, Facebook)
C) Single Sign-On (SSO)
D) Multi-factor authentication
E) Other (please describe after [Answer]: tag below)

[Answer]: 

## Question 2
What is the expected user load?

A) Less than 100 users
B) 100-1,000 users
C) 1,000-10,000 users
D) More than 10,000 users
E) Other (please describe after [Answer]: tag below)

[Answer]: 

## Question 3
Will this integrate with existing systems?

A) Yes, with existing database
B) Yes, with existing authentication system
C) Yes, with multiple existing systems
D) No, standalone system
E) Other (please describe after [Answer]: tag below)

[Answer]: 
```

## User Response Examples

### Standard Option Selection

```markdown
## Question 1
What is the primary user authentication method?

A) Username and password
B) Social media login (Google, Facebook)
C) Single Sign-On (SSO)
D) Multi-factor authentication
E) Other (please describe after [Answer]: tag below)

[Answer]: C
```

### "Other" Option with Description

```markdown
## Question 2
What is the expected user load?

A) Less than 100 users
B) 100-1,000 users
C) 1,000-10,000 users
D) More than 10,000 users
E) Other (please describe after [Answer]: tag below)

[Answer]: E - We expect variable load, starting with 500 users but could scale to 50,000 within 6 months
```

## Clarification Questions Template

When ambiguities are found in answers, use this format for follow-up questions:

```markdown
# [Stage Name] Clarifications - [unit-name if applicable]

**Created:** [ISO 8601 timestamp]

Some of your previous answers need clarification. Please answer the following follow-up questions.

---

## Clarification 1
**Original Question:** [Question text]
**Your Answer:** [User's answer]
**Issue:** [Explain the ambiguity]

**Clarifying Question:**
[New question with options following standard format]

[Answer]: 

---

## Clarification 2
[Repeat structure for each ambiguity]

---
```

## Ambiguity Indicators to Look For

When analyzing answers, look for these patterns that indicate ambiguity:
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
