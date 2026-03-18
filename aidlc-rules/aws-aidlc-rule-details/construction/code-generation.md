# Code Generation Stage

**Purpose:** Generate code, tests, documentation, and deployment artifacts for a specific unit of work.

**Stage Type:** ALWAYS (per-unit)

**Phase:** CONSTRUCTION

**Load this file when:** Starting Code Generation stage for a unit

**Unload this file after:** Code Generation stage completes and user approves

---

## Execute IF

This stage ALWAYS executes for every unit of work.

## Skip IF

This stage is never skipped - it always executes.

---

## Two-Part Structure

This stage has TWO distinct parts that must be executed sequentially:

**PART 1 - Planning:**
- Create detailed code generation plan with explicit steps
- Get user approval for the plan

**PART 2 - Generation:**
- Execute approved plan to generate code
- Update progress checkboxes immediately after each step
- Get user approval for generated code

---

## Prerequisites

Before starting this stage, ensure:
1. Unit of work is defined in `unit-of-work.md`
2. Unit story mapping exists in `unit-of-work-story-map.md`
3. All prior design stages have been completed (as applicable)
4. Technology stack decisions have been made

---

## PART 1: Planning Steps

### Step 1: Log User Input
**Action:** Log any user input during this stage in `audit.md`.

**Template:** `../../templates/audit-logs/basic-entry.md`

**Log with:**
- Stage: Code Generation - [unit-name]
- Context: Starting Code Generation for unit [unit-name]

### Step 2: Load Unit Design Context
**Action:** Read and analyze ALL design artifacts for this unit:

**Required Artifacts:**
- `aidlc-docs/inception/application-design/unit-of-work.md` - Unit definition
- `aidlc-docs/inception/application-design/unit-of-work-story-map.md` - Story assignments

**Optional Artifacts (if they exist):**
- `aidlc-docs/construction/{unit-name}/functional-design/` - Functional design
- `aidlc-docs/construction/{unit-name}/nfr-requirements/` - NFR requirements and tech stack
- `aidlc-docs/construction/{unit-name}/nfr-design/` - NFR design patterns
- `aidlc-docs/construction/{unit-name}/infrastructure-design/` - Infrastructure design
- `aidlc-docs/inception/reverse-engineering/` - Existing codebase (brownfield)

### Step 3: Understand Unit Context
**Action:** Analyze the unit to understand code generation requirements:
- Unit name, description, and responsibilities
- Assigned user stories
- Business logic and domain entities
- NFR patterns to implement
- Infrastructure to integrate with
- Technology stack to use
- Unit dependencies and interfaces

### Step 4: Create Detailed Code Generation Plan
**Action:** Create comprehensive code generation plan with explicit, numbered steps and checkboxes.

**Plan File Location:** `aidlc-docs/construction/plans/{unit-name}-code-generation-plan.md`

**Template:** `../../templates/plans/stage-plan-base.md`

**CRITICAL:** This plan is the single source of truth for code generation. Every step must be tracked with checkboxes.

**Plan Structure:**
```markdown
### Code Generation Steps

#### Business Logic Layer
- [ ] 1. Generate domain entities
- [ ] 2. Generate business logic services
- [ ] 3. Generate business rules validation
- [ ] 4. Generate business logic tests
- [ ] 5. Generate business logic documentation

#### API Layer
- [ ] 6. Generate API controllers/handlers
- [ ] 7. Generate API request/response models
- [ ] 8. Generate API validation
- [ ] 9. Generate API tests
- [ ] 10. Generate API documentation

#### Repository Layer
- [ ] 11. Generate repository interfaces
- [ ] 12. Generate repository implementations
- [ ] 13. Generate database models
- [ ] 14. Generate repository tests

#### Database Migrations
- [ ] 15. Generate database schema migrations
- [ ] 16. Generate seed data scripts

#### Infrastructure Integration
- [ ] 17. Generate infrastructure configuration
- [ ] 18. Generate deployment scripts

#### Documentation
- [ ] 19. Generate README
- [ ] 20. Generate API documentation
- [ ] 21. Generate deployment guide

#### Final Steps
- [ ] 22. Review all generated code
- [ ] 23. Run tests
- [ ] 24. Present completion message
- [ ] 25. Get user approval
```

**Customize based on:**
- Unit complexity
- Technology stack
- Design artifacts available
- Brownfield vs greenfield

### Step 5: Present Plan to User
**Action:** Inform user that the plan is ready.

**Message:**
```markdown
# 📋 Code Generation Plan Ready - [unit-name]

Plan Location: `aidlc-docs/construction/plans/{unit-name}-code-generation-plan.md`

**Plan Summary:**
- Total Steps: [Number]
- Technology Stack: [Language, Framework, Database]
- Assigned Stories: [Story IDs]

Please review the plan. Once approved, I'll execute it to generate all code.
```

### Step 6: Get User Approval for Plan
**Action:** Wait for user to approve the plan.

**Log approval** in audit.md with timestamp.

---

## PART 2: Generation Steps

### Step 7: Execute Code Generation Plan
**Action:** Execute each step in the approved plan sequentially.

**CRITICAL RULES:**
1. **Execute steps in order** - Follow the plan sequence
2. **Update checkboxes immediately** - Mark [x] after completing each step
3. **Generate complete code** - Don't use placeholders or TODOs
4. **Follow design artifacts** - Implement according to design documents
5. **Apply NFR patterns** - Incorporate NFR design patterns
6. **Write tests** - Generate tests for all code
7. **Document code** - Add inline documentation

**For each step:**
1. Read the step description
2. Execute the step (generate code, tests, docs)
3. Mark the step complete [x] in the plan file
4. Continue to next step

### Step 8: Generate Business Logic Layer
**Action:** Generate domain entities, business services, business rules, and tests.

**Follow:**
- Functional design artifacts (business-logic-model.md, business-rules.md, domain-entities.md)
- NFR design patterns
- Technology stack decisions

**Update plan:** Mark business logic steps [x] immediately after completion.

### Step 9: Generate API Layer
**Action:** Generate API controllers/handlers, request/response models, validation, and tests.

**Follow:**
- Functional design artifacts
- NFR design patterns (authentication, authorization, validation)
- API technology decisions

**Update plan:** Mark API layer steps [x] immediately after completion.

### Step 10: Generate Repository Layer
**Action:** Generate repository interfaces, implementations, database models, and tests.

**Follow:**
- Domain entities from functional design
- Database technology decisions
- NFR design patterns (connection pooling, query optimization)

**Update plan:** Mark repository layer steps [x] immediately after completion.

### Step 11: Generate Database Migrations
**Action:** Generate database schema migrations and seed data scripts.

**Follow:**
- Domain entities
- Database technology decisions
- Migration tool decisions

**Update plan:** Mark database migration steps [x] immediately after completion.

### Step 12: Generate Infrastructure Integration
**Action:** Generate infrastructure configuration and deployment scripts.

**Follow:**
- Infrastructure design artifacts
- Deployment architecture
- Infrastructure as Code tool decisions

**Update plan:** Mark infrastructure steps [x] immediately after completion.

### Step 13: Generate Documentation
**Action:** Generate README, API documentation, and deployment guide.

**Include:**
- How to build and run
- How to test
- How to deploy
- API endpoints and usage
- Configuration options

**Update plan:** Mark documentation steps [x] immediately after completion.

### Step 14: Review Generated Code
**Action:** Review all generated code for completeness and quality.

**Check:**
- All plan steps completed [x]
- No placeholders or TODOs
- Tests are present
- Documentation is complete
- Code follows design artifacts
- NFR patterns are applied

### Step 15: Run Tests
**Action:** Run all generated tests to verify code works.

**If tests fail:** Fix issues and re-run tests.

**Update plan:** Mark test step [x] after tests pass.

### Step 16: Update State Tracking
**Action:** Update `aidlc-docs/aidlc-state.md` to reflect completion.

**Template:** `../../templates/state/aidlc-state.md`

### Step 17: Present Completion Message
**Action:** Present standardized 2-option completion message.

**Template:** `../../templates/completion-messages/2-option-standard.md`

**MANDATORY FORMAT:**
```markdown
# 🔧 Code Generation Complete - [unit-name]

Artifacts Created:
- ✅ Business Logic Layer - [Number] files
- ✅ API Layer - [Number] files
- ✅ Repository Layer - [Number] files
- ✅ Database Migrations - [Number] files
- ✅ Tests - [Number] files
- ✅ Documentation - [Number] files

Location: `[code location]`

---

What would you like to do?

🔧 **Request Changes** - Ask for modifications
✅ **Continue to Next Stage** - Approve and proceed

---
```

**CRITICAL:** Do NOT create 3-option menus or emergent navigation patterns.

### Step 18: Wait for User Response
**Action:** **WAIT FOR EXPLICIT APPROVAL** - Do NOT proceed until user confirms.

**Handle response:**
- If "Request Changes" → Make modifications and return to Step 17
- If "Continue" → Proceed to Step 19

### Step 19: Log User Approval
**Action:** Record approval in audit.md with complete raw input.

**Template:** `../../templates/audit-logs/basic-entry.md`

### Step 20: Update Final Plan Progress
**Action:** Mark all remaining steps as [x] in the plan file.

---

## Artifacts Created

1. **Plan:** `aidlc-docs/construction/plans/{unit-name}-code-generation-plan.md`
2. **Code:** Generated code files in appropriate directories
3. **Tests:** Generated test files
4. **Documentation:** README, API docs, deployment guide
5. **Infrastructure:** Configuration and deployment scripts

---

## Key Principles

1. **Plan-Driven Generation:** Follow the approved plan exactly
2. **Immediate Progress Tracking:** Update checkboxes after each step
3. **Complete Code:** No placeholders or TODOs
4. **Design-Driven:** Implement according to design artifacts
5. **Pattern Application:** Apply NFR design patterns
6. **Test Coverage:** Generate tests for all code
7. **Documentation:** Document all code and APIs
8. **Explicit Approval:** WAIT for user approval before proceeding

---

## Templates Reference

All templates are located in `../../templates/` directory:

- **Audit Logs:** `audit-logs/basic-entry.md`
- **Plans:** `plans/stage-plan-base.md`
- **Completion:** `completion-messages/2-option-standard.md`
- **State:** `state/aidlc-state.md`

---

## Next Stage

After approval:
- If more units exist → **Code Generation** for next unit
- If all units complete → **Build and Test** stage

---

**End of Code Generation Stage Instructions**
