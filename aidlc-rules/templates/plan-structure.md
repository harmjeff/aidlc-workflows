# Plan Structure Template

**Purpose:** Standard structure for all plan files in the AIDLC workflow

**Usage:** Use this template when creating plan files for any stage

**File Naming:** `{unit-name}-{stage-name}-plan.md` or `{stage-name}-plan.md`

---

## Standard Plan Structure

```markdown
# [Stage Name] Plan - [unit-name if applicable]

**Unit Name:** [unit-name] (if per-unit stage)
**Created:** [ISO 8601 timestamp]
**Status:** Planning

---

## Context

[Provide relevant context for this stage]

**[Context Item 1]:** [Description]

**[Context Item 2]:** [Description]

**[Context Item 3]:** [Description]

---

## [Stage Name] Steps

### Planning Phase
- [ ] 1. [Step description]
- [ ] 2. [Step description]
- [ ] 3. [Step description]
- [ ] 4. [Step description]
- [ ] 5. [Step description]
- [ ] 6. [Step description]
- [ ] 7. [Step description]

### Generation Phase
- [ ] 8. [Step description]
- [ ] 9. [Step description]
- [ ] 10. [Step description]
- [ ] 11. [Step description]
- [ ] 12. [Step description]
- [ ] 13. [Step description]
- [ ] 14. [Step description]
- [ ] 15. [Step description]

---

## Clarifying Questions

**DIRECTIVE:** [Directive about question generation for this stage]

**Question Categories to Consider:**
- [Category 1]
- [Category 2]
- [Category 3]
- [Category 4]

### [Category 1] Questions

[Generate questions for this category]

### [Category 2] Questions

[Generate questions for this category]

[Continue for all categories]

---

## User Answers

[This section will be filled with user responses using [Answer]: tags]

---

## Artifacts to Generate

1. **[artifact-1].md** - [Description]
2. **[artifact-2].md** - [Description]
3. **[artifact-3].md** - [Description]

---

## Notes

[Space for additional notes or considerations]
```

## Examples by Stage Type

### Functional Design Plan

```markdown
# Functional Design Plan - auth-service

**Unit Name:** auth-service
**Created:** 2026-01-28T14:30:00Z
**Status:** Planning

---

## Unit Context

**Unit Description:** Authentication service handling user login, registration, and token management

**Assigned Stories:** US-001, US-002, US-003

**Unit Responsibilities:**
- User authentication
- Token generation and validation
- Password management
- Session management

**Unit Dependencies:**
- User database
- Email service
- Logging service

---

## Functional Design Steps

### Planning Phase
- [ ] 1. Analyze unit context and requirements
- [ ] 2. Generate clarifying questions
- [ ] 3. Collect user answers
- [ ] 4. Analyze answers for ambiguities
- [ ] 5. Create follow-up questions (if needed)
- [ ] 6. Resolve all ambiguities
- [ ] 7. Get user approval to proceed

### Generation Phase
- [ ] 8. Design business logic model
- [ ] 9. Define business rules
- [ ] 10. Define domain entities and relationships
- [ ] 11. Create business-logic-model.md
- [ ] 12. Create business-rules.md
- [ ] 13. Create domain-entities.md
- [ ] 14. Present completion message
- [ ] 15. Get user approval

---

## Clarifying Questions

**DIRECTIVE:** Thoroughly analyze the unit to identify ALL areas needing clarification. Default to asking questions when there is ANY ambiguity.

**Question Categories to Consider:**
- Business Logic Modeling
- Domain Model
- Business Rules
- Data Flow
- Integration Points

### Business Logic Modeling Questions

## Question 1
What is the primary authentication flow?

A) Username/password with JWT tokens
B) OAuth 2.0 with external providers
C) SAML-based SSO
D) Multi-factor authentication
E) Other (please describe after [Answer]: tag below)

[Answer]: 

[Continue with more questions]

---

## User Answers

[This section will be filled with user responses]

---

## Artifacts to Generate

1. **business-logic-model.md** - Business logic flow and processing model
2. **business-rules.md** - Business rules, validations, and constraints
3. **domain-entities.md** - Domain entities and relationships

---

## Notes

[Space for additional notes]
```

### Code Generation Plan

```markdown
# Code Generation Plan - auth-service

**Unit Name:** auth-service
**Created:** 2026-01-28T16:00:00Z
**Status:** Planning

**IMPORTANT:** This plan is the single source of truth for Code Generation (PART 2). Every step listed here must be executed and marked complete [x] immediately after completion.

---

## Unit Context

**Unit Description:** Authentication service handling user login, registration, and token management

**Assigned Stories:** US-001, US-002, US-003

**Unit Dependencies:**
- User database (PostgreSQL)
- Email service (SendGrid)
- Logging service (CloudWatch)

**Expected Interfaces:**
- POST /api/auth/register
- POST /api/auth/login
- POST /api/auth/refresh
- POST /api/auth/logout

---

## Code Generation Steps

### Business Logic Layer
- [ ] 1. Generate authentication business logic
- [ ] 2. Generate token management logic
- [ ] 3. Generate password hashing logic
- [ ] 4. Generate business logic unit tests
- [ ] 5. Create business logic summary

### API Layer
- [ ] 6. Generate REST API endpoints
- [ ] 7. Generate request/response models
- [ ] 8. Generate API validation logic
- [ ] 9. Generate API unit tests
- [ ] 10. Create API layer summary

### Repository Layer
- [ ] 11. Generate user repository
- [ ] 12. Generate session repository
- [ ] 13. Generate repository unit tests
- [ ] 14. Create repository layer summary

### Database
- [ ] 15. Generate database migration scripts
- [ ] 16. Generate seed data scripts

### Documentation
- [ ] 17. Generate API documentation (OpenAPI/Swagger)
- [ ] 18. Update README with setup instructions

### Deployment
- [ ] 19. Generate Dockerfile
- [ ] 20. Generate deployment configuration

---

## Story Traceability

**US-001: User Registration**
- Steps 1, 6, 11, 15

**US-002: User Login**
- Steps 1, 2, 6, 12

**US-003: Token Refresh**
- Steps 2, 6, 12

---

## Artifacts to Generate

- Business logic files
- API endpoint files
- Repository files
- Unit test files
- Integration test files
- Database migration scripts
- API documentation
- Deployment artifacts

---

## Notes

[Space for additional notes]
```

## Critical Rules

1. **Use checkboxes [ ] for all steps** - Mark [x] immediately after completion
2. **Number steps sequentially** - Makes progress tracking clear
3. **Separate Planning and Generation phases** - For two-part stages
4. **Include context section** - Provide relevant background information
5. **Embed questions in plan** - Use [Answer]: tags for responses
6. **List artifacts to generate** - Show what will be created
7. **Update immediately** - Mark checkboxes in SAME interaction as work completion

## Checkbox Update Rules

**MANDATORY:**
- Mark [x] immediately after completing each step
- Update in SAME interaction where work is completed
- NO EXCEPTIONS - Every step completion MUST be tracked
- Never complete work without updating checkboxes
