## FUNCTIONAL_DESIGN

Purpose: detailed business logic design per unit (technology-agnostic, no infrastructure concerns). Builds on Application Design from INCEPTION.

Prerequisites: Units Generation complete, unit-of-work artifacts available, Application Design recommended, execution plan indicates stage should execute.

### Steps

1. Analyze Unit Context
   - Read unit definition from `aidlc-docs/inception/application-design/unit-of-work.md`
   - Read assigned stories from `aidlc-docs/inception/application-design/unit-of-work-story-map.md`
   - Understand unit responsibilities and boundaries

2. Create Functional Design Plan
   - Generate plan with checkboxes [] for functional design
   - Focus on business logic, domain models, business rules

3. Generate Context-Appropriate Questions
   - [REQ] Thoroughly analyze unit definition and functional design artifacts to identify ALL areas needing clarification
   - [REQ] Default to asking questions when ANY ambiguity exists
   - EMBED questions using [Answer]: tag format
   - Question categories to consider (evaluate ALL):
     - Business Logic Modeling: core entities, workflows, data transformations, business processes
     - Domain Model: domain concepts, entity relationships, data structures, business objects
     - Business Rules: decision rules, validation logic, constraints, business policies
     - Data Flow: data inputs, outputs, transformations, persistence requirements
     - Integration Points: external system interactions, APIs, data exchange
     - Error Handling: error scenarios, validation failures, exception handling
     - Business Scenarios: edge cases, alternative flows, complex situations
     - Frontend Components (if applicable): UI component structure, user interactions, state management, form handling

4. Store Plan
   - Save as `aidlc-docs/construction/plans/{unit-name}-functional-design-plan.md`
   - Include all [Answer]: tags

5. Collect and Analyze Answers
   - Wait for user to complete all [Answer]: tags
   - [REQ] Review ALL responses for vague/ambiguous answers
   - [REQ] Add follow-up questions for ANY unclear responses
   - Look for: "depends", "maybe", "not sure", "mix of", "somewhere between"
   - Create clarification questions file if ANY ambiguities detected
   - Do not proceed until ALL ambiguities resolved

6. Generate Functional Design Artifacts
   - Create `aidlc-docs/construction/{unit-name}/functional-design/business-logic-model.md`
   - Create `aidlc-docs/construction/{unit-name}/functional-design/business-rules.md`
   - Create `aidlc-docs/construction/{unit-name}/functional-design/domain-entities.md`
   - [COND] unit includes frontend/UI → Create `aidlc-docs/construction/{unit-name}/functional-design/frontend-components.md` with: component hierarchy/structure, props/state definitions, user interaction flows, form validation rules, API integration points

7. Present Completion Message

```markdown
# 🔧 Functional Design Complete - [unit-name]
```

   Optional AI summary: structured bullet-point summary of functional design (business logic models, entities, business rules, domain model structure). No workflow instructions.

```markdown
> **📋 <u>**REVIEW REQUIRED:**</u>**  
> Please examine the functional design artifacts at: `aidlc-docs/construction/[unit-name]/functional-design/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the functional design based on your review  
> ✅ **Continue to Next Stage** - Approve functional design and proceed to **[next-stage-name]**

---
```

8. Wait for Explicit Approval
   - Do not proceed until explicit unambiguous approval
   - changes requested → update design, repeat approval

9. Record Approval and Update Progress
   - Log approval in audit.md with timestamp
   - Record user approval response with timestamp
   - Mark Functional Design complete in aidlc-state.md

## NFR_REQUIREMENTS

Prerequisites: Functional Design complete for unit, functional design artifacts available, execution plan indicates stage should execute.

Purpose: determine non-functional requirements for unit, make tech stack choices.

### Steps

1. Analyze Functional Design
   - Read from `aidlc-docs/construction/{unit-name}/functional-design/`
   - Understand business logic complexity and requirements

2. Create NFR Requirements Plan
   - Generate plan with checkboxes [] for NFR assessment
   - Focus on scalability, performance, availability, security

3. Generate Context-Appropriate Questions
   - [REQ] Thoroughly analyze functional design to identify ALL areas where NFR clarification improves quality
   - [REQ] Default to asking questions when ANY ambiguity exists
   - EMBED questions using [Answer]: tag format
   - Question categories to evaluate (consider ALL):
     - Scalability Requirements: expected load, growth patterns, scaling triggers, capacity planning
     - Performance Requirements: response times, throughput, latency, benchmarks
     - Availability Requirements: uptime, disaster recovery, failover, business continuity
     - Security Requirements: data protection, compliance, authentication, authorization, threat models
     - Tech Stack Selection: technology preferences, constraints, existing systems, integration
     - Reliability Requirements: error handling, fault tolerance, monitoring, alerting
     - Maintainability Requirements: code quality, documentation, testing, operational requirements
     - Usability Requirements: user experience, accessibility, interface requirements

4. Store Plan
   - Save as `aidlc-docs/construction/plans/{unit-name}-nfr-requirements-plan.md`

5. Collect and Analyze Answers
   - Wait for all [Answer]: tags completed
   - [REQ] Review ALL responses for vague/ambiguous answers
   - [REQ] Follow-up for ANY unclear responses
   - Look for: "depends", "maybe", "not sure", "mix of", "somewhere between", "standard", "typical"
   - Do not proceed until ALL ambiguities resolved

6. Generate NFR Requirements Artifacts
   - Create `aidlc-docs/construction/{unit-name}/nfr-requirements/nfr-requirements.md`
   - Create `aidlc-docs/construction/{unit-name}/nfr-requirements/tech-stack-decisions.md`

7. Present Completion Message

```markdown
# 📊 NFR Requirements Complete - [unit-name]
```

   Optional AI summary: structured bullet-point summary (scalability, performance, availability, security, compliance, tech stack decisions). No workflow instructions.

```markdown
> **📋 <u>**REVIEW REQUIRED:**</u>**  
> Please examine the NFR requirements at: `aidlc-docs/construction/[unit-name]/nfr-requirements/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the NFR requirements based on your review  
> ✅ **Continue to Next Stage** - Approve NFR requirements and proceed to **[next-stage-name]**

---
```

8. Wait for Explicit Approval
9. Record Approval and Update Progress (audit.md + aidlc-state.md)


## NFR_DESIGN

Prerequisites: NFR Requirements complete for unit, NFR requirements artifacts available, execution plan indicates stage should execute.

Purpose: incorporate NFR requirements into unit design using patterns and logical components.

### Steps

1. Analyze NFR Requirements
   - Read from `aidlc-docs/construction/{unit-name}/nfr-requirements/`
   - Understand scalability, performance, availability, security needs

2. Create NFR Design Plan
   - Generate plan with checkboxes [] for NFR design
   - Focus on design patterns and logical components

3. Generate Context-Appropriate Questions
   - Analyze NFR requirements to generate ONLY questions relevant to THIS unit's NFR design
   - Categories as inspiration, not mandatory checklist. Skip if not applicable:
     - Resilience Patterns: fault tolerance approach
     - Scalability Patterns: scaling mechanisms
     - Performance Patterns: optimization strategy
     - Security Patterns: security implementation approach
     - Logical Components: infrastructure components (queues, caches, etc.)

4. Store Plan
   - Save as `aidlc-docs/construction/plans/{unit-name}-nfr-design-plan.md`

5. Collect and Analyze Answers
   - Wait for all [Answer]: tags, review for ambiguities, follow up if needed

6. Generate NFR Design Artifacts
   - Create `aidlc-docs/construction/{unit-name}/nfr-design/nfr-design-patterns.md`
   - Create `aidlc-docs/construction/{unit-name}/nfr-design/logical-components.md`

7. Present Completion Message

```markdown
# 🎨 NFR Design Complete - [unit-name]
```

   Optional AI summary: design patterns, logical components, resilience/scalability/performance patterns. No workflow instructions.

```markdown
> **📋 <u>**REVIEW REQUIRED:**</u>**  
> Please examine the NFR design at: `aidlc-docs/construction/[unit-name]/nfr-design/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the NFR design based on your review  
> ✅ **Continue to Next Stage** - Approve NFR design and proceed to **[next-stage-name]**

---
```

8. Wait for Explicit Approval
9. Record Approval and Update Progress (audit.md + aidlc-state.md)

## INFRASTRUCTURE_DESIGN

Prerequisites: Functional Design complete, NFR Design recommended, execution plan indicates stage should execute.

Purpose: map logical software components to actual infrastructure choices for deployment.

### Steps

1. Analyze Design Artifacts
   - Read functional design from `aidlc-docs/construction/{unit-name}/functional-design/`
   - Read NFR design from `aidlc-docs/construction/{unit-name}/nfr-design/` (if exists)
   - Identify logical components needing infrastructure

2. Create Infrastructure Design Plan
   - Generate plan with checkboxes [] for infrastructure design
   - Focus on mapping to actual services (AWS, Azure, GCP, on-premise)

3. Generate Context-Appropriate Questions
   - Generate ONLY questions relevant to THIS unit's infrastructure needs
   - Categories as inspiration, not mandatory checklist. Skip if not applicable:
     - Deployment Environment: cloud provider, environment setup
     - Compute Infrastructure: compute service choice
     - Storage Infrastructure: database/storage selection
     - Messaging Infrastructure: messaging/queuing services
     - Networking Infrastructure: load balancing, API gateway
     - Monitoring Infrastructure: observability tooling
     - Shared Infrastructure: infrastructure sharing strategy

4. Store Plan
   - Save as `aidlc-docs/construction/plans/{unit-name}-infrastructure-design-plan.md`

5. Collect and Analyze Answers

6. Generate Infrastructure Design Artifacts
   - Create `aidlc-docs/construction/{unit-name}/infrastructure-design/infrastructure-design.md`
   - Create `aidlc-docs/construction/{unit-name}/infrastructure-design/deployment-architecture.md`
   - [COND] shared infrastructure → Create `aidlc-docs/construction/shared-infrastructure.md`

7. Present Completion Message

```markdown
# 🏢 Infrastructure Design Complete - [unit-name]
```

   Optional AI summary: infrastructure services, deployment architecture, cloud provider choices. No workflow instructions.

```markdown
> **📋 <u>**REVIEW REQUIRED:**</u>**  
> Please examine the infrastructure design at: `aidlc-docs/construction/[unit-name]/infrastructure-design/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the infrastructure design based on your review  
> ✅ **Continue to Next Stage** - Approve infrastructure design and proceed to **Code Generation**

---
```

8. Wait for Explicit Approval
9. Record Approval and Update Progress (audit.md + aidlc-state.md)

## CODE_GENERATION

Two parts: Part 1 Planning, Part 2 Generation.
For brownfield: "generate" means modify existing files when appropriate, not create duplicates.

Prerequisites: Unit Design complete, NFR Implementation (if executed) complete, all unit design artifacts available.

### PART 1: PLANNING

1. Analyze Unit Context
   - Read unit design artifacts
   - Read unit story map for assigned stories
   - Identify dependencies and interfaces
   - Validate unit ready for code generation

2. Create Detailed Unit Code Generation Plan
   - Read workspace root and project type from `aidlc-docs/aidlc-state.md`
   - Determine code location (see Critical Rules for structure patterns)
   - Brownfield: review reverse engineering code-structure.md for existing files to modify
   - Document exact paths (never aidlc-docs/)
   - Create explicit steps for unit generation:
     1. Project Structure Setup (greenfield only)
     2. Business Logic Generation
     3. Business Logic Unit Testing
     4. Business Logic Summary
     5. API Layer Generation
     6. API Layer Unit Testing
     7. API Layer Summary
     8. Repository Layer Generation
     9. Repository Layer Unit Testing
     10. Repository Layer Summary
     11. Frontend Components Generation (if applicable)
     12. Frontend Components Unit Testing (if applicable)
     13. Frontend Components Summary (if applicable)
     14. Database Migration Scripts (if data models exist)
     15. Documentation Generation (API docs, README updates)
     16. Deployment Artifacts Generation
   - Number each step sequentially
   - Include story mapping references
   - Add checkboxes [] for each step

3. Include Unit Generation Context
   - Stories implemented by this unit
   - Dependencies on other units/services
   - Expected interfaces and contracts
   - Database entities owned by this unit
   - Service boundaries and responsibilities

4. Create Unit Plan Document
   - Save as `aidlc-docs/construction/plans/{unit-name}-code-generation-plan.md`
   - Include step numbering, unit context, dependencies, story traceability
   - This plan is single source of truth for Code Generation

5. Summarize Unit Plan
   - Provide summary to user: generation approach, step sequence, story coverage, total steps, estimated scope

6. Log Approval Prompt
   - Log prompt with timestamp in `aidlc-docs/audit.md`

7. Wait for Explicit Approval
   - Do not proceed until user approves entire plan

8. Record Approval Response
   - Log in `aidlc-docs/audit.md` with timestamp

9. Update Progress
   - Mark Code Planning complete in `aidlc-state.md`

### PART 2: GENERATION

10. Load Unit Code Generation Plan
    - Read from `aidlc-docs/construction/plans/{unit-name}-code-generation-plan.md`
    - Identify next uncompleted step (first [] checkbox)

11. Execute Current Step
    - Verify target directory from plan (never aidlc-docs/)
    - Brownfield: check if target file exists
    - file exists → modify in-place (never create `ClassName_modified.java`, `ClassName_new.java`)
    - file doesn't exist → create new
    - Write locations: application code → workspace root, documentation → `aidlc-docs/construction/{unit-name}/code/` (markdown only), build/config → workspace root

12. Update Progress
    - Mark completed step [x] in plan
    - Mark associated unit stories [x] when generation finished
    - Update `aidlc-docs/aidlc-state.md`
    - Brownfield: verify no duplicate files created

13. Continue or Complete
    - more steps → return to step 10
    - all complete → present completion message

14. Present Completion Message

```markdown
# 💻 Code Generation Complete - [unit-name]
```

   Optional AI summary: brownfield: distinguish modified vs created files. Greenfield: list created files with paths. List tests, docs, deployment artifacts. No workflow instructions.

```markdown
> **📋 <u>**REVIEW REQUIRED:**</u>**  
> Please examine the generated code at:
> - **Application Code**: `[actual-workspace-path]`
> - **Documentation**: `aidlc-docs/construction/[unit-name]/code/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the generated code based on your review  
> ✅ **Continue to Next Stage** - Approve code generation and proceed to **[next-unit/Build & Test]**

---
```

15. Wait for Explicit Approval
16. Record Approval and Update Progress (audit.md + aidlc-state.md)

### Critical Rules

Code Location:
- Application code: workspace root only (NEVER aidlc-docs/)
- Documentation: aidlc-docs/ only (markdown summaries)
- Read workspace root from aidlc-state.md before generating

Structure patterns by project type:
- Brownfield: use existing structure (e.g., `src/main/java/`, `lib/`, `pkg/`)
- Greenfield single unit: `src/`, `tests/`, `config/` in workspace root
- Greenfield multi-unit (microservices): `{unit-name}/src/`, `{unit-name}/tests/`
- Greenfield multi-unit (monolith): `src/{unit-name}/`, `tests/{unit-name}/`

Brownfield File Modification:
- Check if file exists before generating
- exists → modify in-place (never create copies)
- doesn't exist → create new
- Verify no duplicate files after generation

Planning Phase:
- Explicit numbered steps for all generation activities
- Story traceability in plan
- Document unit context and dependencies
- Explicit user approval before generation

Generation Phase:
- NO HARDCODED LOGIC: only execute what plan says
- FOLLOW PLAN EXACTLY: no deviation from step sequence
- UPDATE CHECKBOXES: mark [x] immediately after each step
- STORY TRACEABILITY: mark unit stories [x] when implemented
- RESPECT DEPENDENCIES: only implement when dependencies satisfied

Automation Friendly Code:
- Add `data-testid` to interactive elements (buttons, inputs, links, forms)
- Naming: `{component}-{element-role}` (e.g., `login-form-submit-button`)
- No dynamic/auto-generated IDs that change between renders
- Keep `data-testid` values stable across code changes

Completion Criteria:
- Complete plan created and approved
- All plan steps marked [x]
- All unit stories implemented
- All code and tests generated
- Deployment artifacts generated
- Unit ready for build and verification


## BUILD_AND_TEST

Purpose: build all units, execute comprehensive testing strategy.

Prerequisites: Code Generation complete for all units, all code artifacts generated.

### Steps

1. Analyze Testing Requirements
   - Unit tests: already generated per unit during code generation
   - Integration tests: interactions between units/services
   - Performance tests: load, stress, scalability
   - End-to-end tests: complete user workflows
   - Contract tests: API contract validation between services
   - Security tests: vulnerability scanning, penetration testing

2. Generate Build Instructions

Create `aidlc-docs/construction/build-and-test/build-instructions.md`:

```markdown
# Build Instructions

## Prerequisites
- **Build Tool**: [Tool name and version]
- **Dependencies**: [List all required dependencies]
- **Environment Variables**: [List required env vars]
- **System Requirements**: [OS, memory, disk space]

## Build Steps

### 1. Install Dependencies
\`\`\`bash
[Command to install dependencies]
# Example: npm install, mvn dependency:resolve, pip install -r requirements.txt
\`\`\`

### 2. Configure Environment
\`\`\`bash
[Commands to set up environment]
# Example: export variables, configure credentials
\`\`\`

### 3. Build All Units
\`\`\`bash
[Command to build all units]
# Example: mvn clean install, npm run build, brazil-build
\`\`\`

### 4. Verify Build Success
- **Expected Output**: [Describe successful build output]
- **Build Artifacts**: [List generated artifacts and locations]
- **Common Warnings**: [Note any acceptable warnings]

## Troubleshooting

### Build Fails with Dependency Errors
- **Cause**: [Common causes]
- **Solution**: [Step-by-step fix]

### Build Fails with Compilation Errors
- **Cause**: [Common causes]
- **Solution**: [Step-by-step fix]
```

3. Generate Unit Test Execution Instructions

Create `aidlc-docs/construction/build-and-test/unit-test-instructions.md`:

```markdown
# Unit Test Execution

## Run Unit Tests

### 1. Execute All Unit Tests
\`\`\`bash
[Command to run all unit tests]
# Example: mvn test, npm test, pytest tests/unit
\`\`\`

### 2. Review Test Results
- **Expected**: [X] tests pass, 0 failures
- **Test Coverage**: [Expected coverage percentage]
- **Test Report Location**: [Path to test reports]

### 3. Fix Failing Tests
If tests fail:
1. Review test output in [location]
2. Identify failing test cases
3. Fix code issues
4. Rerun tests until all pass
```

4. Generate Integration Test Instructions

Create `aidlc-docs/construction/build-and-test/integration-test-instructions.md`:

```markdown
# Integration Test Instructions

## Purpose
Test interactions between units/services to ensure they work together correctly.

## Test Scenarios

### Scenario 1: [Unit A] → [Unit B] Integration
- **Description**: [What is being tested]
- **Setup**: [Required test environment setup]
- **Test Steps**: [Step-by-step test execution]
- **Expected Results**: [What should happen]
- **Cleanup**: [How to clean up after test]

### Scenario 2: [Unit B] → [Unit C] Integration
[Similar structure]

## Setup Integration Test Environment

### 1. Start Required Services
\`\`\`bash
[Commands to start services]
# Example: docker-compose up, start test database
\`\`\`

### 2. Configure Service Endpoints
\`\`\`bash
[Commands to configure endpoints]
# Example: export API_URL=http://localhost:8080
\`\`\`

## Run Integration Tests

### 1. Execute Integration Test Suite
\`\`\`bash
[Command to run integration tests]
# Example: mvn integration-test, npm run test:integration
\`\`\`

### 2. Verify Service Interactions
- **Test Scenarios**: [List key integration test scenarios]
- **Expected Results**: [Describe expected outcomes]
- **Logs Location**: [Where to check logs]

### 3. Cleanup
\`\`\`bash
[Commands to clean up test environment]
# Example: docker-compose down, stop test services
\`\`\`
```

5. Generate Performance Test Instructions (if applicable)

Create `aidlc-docs/construction/build-and-test/performance-test-instructions.md`:

```markdown
# Performance Test Instructions

## Purpose
Validate system performance under load to ensure it meets requirements.

## Performance Requirements
- **Response Time**: < [X]ms for [Y]% of requests
- **Throughput**: [X] requests/second
- **Concurrent Users**: Support [X] concurrent users
- **Error Rate**: < [X]%

## Setup Performance Test Environment

### 1. Prepare Test Environment
\`\`\`bash
[Commands to set up performance testing]
# Example: scale services, configure load balancers
\`\`\`

### 2. Configure Test Parameters
- **Test Duration**: [X] minutes
- **Ramp-up Time**: [X] seconds
- **Virtual Users**: [X] users

## Run Performance Tests

### 1. Execute Load Tests
\`\`\`bash
[Command to run load tests]
# Example: jmeter -n -t test.jmx, k6 run script.js
\`\`\`

### 2. Execute Stress Tests
\`\`\`bash
[Command to run stress tests]
# Example: gradually increase load until failure
\`\`\`

### 3. Analyze Performance Results
- **Response Time**: [Actual vs Expected]
- **Throughput**: [Actual vs Expected]
- **Error Rate**: [Actual vs Expected]
- **Bottlenecks**: [Identified bottlenecks]
- **Results Location**: [Path to performance reports]

## Performance Optimization

If performance doesn't meet requirements:
1. Identify bottlenecks from test results
2. Optimize code/queries/configurations
3. Rerun tests to validate improvements
```

6. Generate Additional Test Instructions (as needed)

   Based on project requirements:
   - Contract Tests (microservices): Create `aidlc-docs/construction/build-and-test/contract-test-instructions.md` (API contract validation, consumer-driven contracts, schema validation)
   - Security Tests: Create `aidlc-docs/construction/build-and-test/security-test-instructions.md` (vulnerability scanning, dependency security, auth testing, input validation)
   - End-to-End Tests: Create `aidlc-docs/construction/build-and-test/e2e-test-instructions.md` (complete user workflows, cross-service scenarios, UI testing)

7. Generate Test Summary

Create `aidlc-docs/construction/build-and-test/build-and-test-summary.md`:

```markdown
# Build and Test Summary

## Build Status
- **Build Tool**: [Tool name]
- **Build Status**: [Success/Failed]
- **Build Artifacts**: [List artifacts]
- **Build Time**: [Duration]

## Test Execution Summary

### Unit Tests
- **Total Tests**: [X]
- **Passed**: [X]
- **Failed**: [X]
- **Coverage**: [X]%
- **Status**: [Pass/Fail]

### Integration Tests
- **Test Scenarios**: [X]
- **Passed**: [X]
- **Failed**: [X]
- **Status**: [Pass/Fail]

### Performance Tests
- **Response Time**: [Actual] (Target: [Expected])
- **Throughput**: [Actual] (Target: [Expected])
- **Error Rate**: [Actual] (Target: [Expected])
- **Status**: [Pass/Fail]

### Additional Tests
- **Contract Tests**: [Pass/Fail/N/A]
- **Security Tests**: [Pass/Fail/N/A]
- **E2E Tests**: [Pass/Fail/N/A]

## Overall Status
- **Build**: [Success/Failed]
- **All Tests**: [Pass/Fail]
- **Ready for Operations**: [Yes/No]

## Next Steps
[If all pass]: Ready to proceed to Operations phase for deployment planning
[If failures]: Address failing tests and rebuild
```

8. Update State Tracking
   - Mark Build and Test complete in `aidlc-docs/aidlc-state.md`

9. Present Results to User

```
"🔨 Build and Test Complete!

**Build Status**: [Success/Failed]

**Test Results**:
✅ Unit Tests: [X] passed
✅ Integration Tests: [X] scenarios passed
✅ Performance Tests: [Status]
✅ Additional Tests: [Status]

**Generated Files**:
1. ✅ build-instructions.md
2. ✅ unit-test-instructions.md
3. ✅ integration-test-instructions.md
4. ✅ performance-test-instructions.md (if applicable)
5. ✅ [additional test files as needed]
6. ✅ build-and-test-summary.md

Review the summary in aidlc-docs/construction/build-and-test/build-and-test-summary.md

**Ready to proceed to Operations stage for deployment planning?""
```

10. Log Interaction

[REQ] Log in `aidlc-docs/audit.md`:

```markdown
## Build and Test Stage
**Timestamp**: [ISO timestamp]
**Build Status**: [Success/Failed]
**Test Status**: [Pass/Fail]
**Files Generated**:
- build-instructions.md
- unit-test-instructions.md
- integration-test-instructions.md
- performance-test-instructions.md
- build-and-test-summary.md

---
```
