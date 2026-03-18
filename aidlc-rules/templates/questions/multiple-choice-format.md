# Multiple Choice Question Format Template

**CRITICAL**: ALL questions must be placed in dedicated .md files. NEVER ask questions directly in chat.

## Template

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

## Critical Requirements

1. **"Other" is MANDATORY** as the LAST option for every question
2. **Only include meaningful options** - Don't make up options to fill slots
3. **Use as many or as few options** as make sense (minimum 2 + Other)
4. **Number questions sequentially** - Question 1, Question 2, etc.
5. **Use [Answer]: tag** for user responses

## Complete Example

```markdown
# Requirements Clarification Questions

Please answer the following questions to help clarify the requirements.

---

## Question 1
What is the primary user authentication method?

A) Username and password
B) Social media login (Google, Facebook)
C) Single Sign-On (SSO)
D) Multi-factor authentication
E) Other (please describe after [Answer]: tag below)

[Answer]: 

---

## Question 2
Will this be a web or mobile application?

A) Web application
B) Mobile application  
C) Both web and mobile
D) Other (please describe after [Answer]: tag below)

[Answer]: 

---

## Question 3
What is the expected number of concurrent users?

A) Less than 100
B) 100-1,000
C) 1,000-10,000
D) More than 10,000
E) Other (please describe after [Answer]: tag below)

[Answer]: 

---
```

## User Response Format

Users answer by filling in the letter choice after [Answer]: tag:

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

Or for "Other" option:

```markdown
## Question 2
What is the expected number of concurrent users?

A) Less than 100
B) 100-1,000
C) 1,000-10,000
D) More than 10,000
E) Other (please describe after [Answer]: tag below)

[Answer]: E - We expect around 50,000 concurrent users during peak hours
```

## Reading User Responses

After user confirms completion:

1. Read the question file
2. Extract answers after [Answer]: tags
3. Validate all questions are answered
4. Analyze for ambiguities (see clarification template)
5. Proceed with analysis based on responses

## Question File Naming

Use descriptive names:
- `requirement-verification-questions.md`
- `story-planning-questions.md`
- `functional-design-questions.md`
- `nfr-requirements-questions.md`

## File Header Template

```markdown
# [Stage Name] Questions

**Created:** [ISO 8601 timestamp]
**Stage:** [Stage name]
**Purpose:** [Why these questions are being asked]

Please answer the following questions. For each question, provide the letter of your choice after the [Answer]: tag.

If you select "Other", please provide details after the [Answer]: tag.

---

[Questions follow]
```

## Guidelines for Creating Questions

### DO:
- ✅ Ask specific, focused questions
- ✅ Provide meaningful, distinct options
- ✅ Include "Other" as last option
- ✅ Use clear, unambiguous language
- ✅ Group related questions together
- ✅ Number questions sequentially

### DON'T:
- ❌ Ask questions in chat
- ❌ Make up options to fill slots
- ❌ Forget "Other" option
- ❌ Use ambiguous language
- ❌ Ask compound questions
- ❌ Assume user knowledge

## Usage in Detail Files

Reference this template:

```markdown
### Step X: Generate Questions

**CRITICAL:** Never ask questions in chat. ALL questions must be in dedicated .md files.

**Format:** See `templates/questions/multiple-choice-format.md`

**Create file:** `[stage-name]-questions.md`

**Include:**
- File header with timestamp and purpose
- Numbered questions with meaningful options
- MANDATORY "Other" option for each question
- [Answer]: tag for each question
```

## After Questions Are Answered

1. **Read the file** to extract answers
2. **Validate completeness** - All questions answered?
3. **Analyze for ambiguities** - Look for:
   - "depends"
   - "maybe"
   - "not sure"
   - "mix of"
   - "somewhere between"
   - Contradictions between answers
4. **Create clarification questions** if needed (see clarification template)
5. **Do NOT proceed** until all ambiguities resolved

## Why This Format?

- **Documentation**: Questions and answers are preserved
- **Clarity**: Structured format reduces ambiguity
- **Review**: User can review all questions before answering
- **Traceability**: Answers are logged and traceable
- **Flexibility**: "Other" option handles unexpected cases
