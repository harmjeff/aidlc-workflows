# Build and Test Stage

**Purpose:** Generate comprehensive build and test instructions for all units.

**Stage Type:** ALWAYS

**Phase:** CONSTRUCTION

**Load this file when:** Starting Build and Test stage (after all units are coded)

**Unload this file after:** Build and Test stage completes and user approves

---

## Execute IF

This stage ALWAYS executes after all units have completed code generation.

## Skip IF

This stage is never skipped - it always executes.

---

## Prerequisites

Before starting this stage, ensure:
1. All units have completed Code Generation stage
2. All code has been generated for all units
3. All tests have been generated for all units
4. Technology stack decisions are documented

---

## Detailed Steps

### Step 1: Log User Input
**Action:** Log any user input during this stage in `audit.md`.

**Template:** `../../templates/audit-logs/basic-entry.md`

**Log with:**
- Stage: Build and Test
- Context: Starting Build and Test stage for all units

### Step 2: Load All Unit Context
**Action:** Read and analyze all unit artifacts:

**Required Artifacts:**
- `aidlc-docs/inception/application-design/unit-of-work.md` - All units
- `aidlc-docs/construction/plans/*-code-generation-plan.md` - All code generation plans
- `aidlc-docs/construction/*/nfr-requirements/tech-stack-decisions.md` - Tech stack for each unit

**Optional Artifacts:**
- `aidlc-docs/construction/*/infrastructure-design/` - Infrastructure for each unit

### Step 3: Identify All Units
**Action:** Create a list of all units that need build and test instructions.

**For each unit, identify:**
- Unit name
- Technology stack
- Dependencies on other units
- Test types needed (unit, integration, performance, etc.)

### Step 4: Generate Build Instructions
**Action:** Create comprehensive build instructions for all units.

**File Location:** `aidlc-docs/construction/build-and-test/build-instructions.md`

**Include:**
- Prerequisites (tools, dependencies)
- Build steps for each unit
- Build order (considering dependencies)
- Build verification steps
- Troubleshooting common build issues

### Step 5: Generate Unit Test Instructions
**Action:** Create unit test instructions for all units.

**File Location:** `aidlc-docs/construction/build-and-test/unit-test-instructions.md`

**Include:**
- How to run unit tests for each unit
- Test coverage requirements
- Test data setup
- Expected test results
- Troubleshooting test failures

### Step 6: Generate Integration Test Instructions
**Action:** Create integration test instructions for interactions between units.

**File Location:** `aidlc-docs/construction/build-and-test/integration-test-instructions.md`

**Include:**
- How to run integration tests
- Test environment setup
- Test data requirements
- Integration test scenarios
- Expected results
- Troubleshooting

### Step 7: Generate Performance Test Instructions
**Action:** Create performance test instructions (if applicable).

**File Location:** `aidlc-docs/construction/build-and-test/performance-test-instructions.md`

**Include:**
- How to run performance tests
- Performance test scenarios
- Load patterns
- Performance metrics to measure
- Performance targets
- Troubleshooting performance issues

### Step 8: Generate Additional Test Instructions
**Action:** Create additional test instructions as needed:
- Contract tests (if microservices)
- Security tests (if security requirements)
- E2E tests (if user-facing)

**File Locations:** `aidlc-docs/construction/build-and-test/[test-type]-test-instructions.md`

### Step 9: Generate Build and Test Summary
**Action:** Create summary document with overview of all build and test activities.

**File Location:** `aidlc-docs/construction/build-and-test/build-and-test-summary.md`

**Include:**
- Overview of all units
- Build order and dependencies
- Test types and coverage
- Quality gates
- CI/CD integration points
- Next steps

### Step 10: Update State Tracking
**Action:** Update `aidlc-docs/aidlc-state.md` to reflect completion.

**Template:** `../../templates/state/aidlc-state.md`

### Step 11: Present Completion Message
**Action:** Present completion message to user.

**Message:**
```markdown
# 🔧 Build and Test Instructions Complete

Artifacts Created:
- ✅ `build-instructions.md` - Build instructions for all units
- ✅ `unit-test-instructions.md` - Unit test instructions
- ✅ `integration-test-instructions.md` - Integration test instructions
- ✅ `performance-test-instructions.md` - Performance test instructions (if applicable)
- ✅ `build-and-test-summary.md` - Summary of all build and test activities

Location: `aidlc-docs/construction/build-and-test/`

---

**Ready to proceed to Operations stage?**

A) Yes, proceed to Operations stage
B) No, I want to review/modify the instructions first

[Answer]: 
```

### Step 12: Wait for User Response
**Action:** **WAIT FOR EXPLICIT APPROVAL** - Do NOT proceed until user confirms.

### Step 13: Log User Approval
**Action:** Record approval in audit.md with complete raw input.

**Template:** `../../templates/audit-logs/basic-entry.md`

---

## Artifacts Created

1. **Build Instructions:** `aidlc-docs/construction/build-and-test/build-instructions.md`
2. **Unit Test Instructions:** `aidlc-docs/construction/build-and-test/unit-test-instructions.md`
3. **Integration Test Instructions:** `aidlc-docs/construction/build-and-test/integration-test-instructions.md`
4. **Performance Test Instructions:** `aidlc-docs/construction/build-and-test/performance-test-instructions.md` (if applicable)
5. **Additional Test Instructions:** As needed
6. **Build and Test Summary:** `aidlc-docs/construction/build-and-test/build-and-test-summary.md`

---

## Key Principles

1. **Comprehensive Instructions:** Cover all units and test types
2. **Clear Steps:** Provide step-by-step instructions
3. **Troubleshooting:** Include troubleshooting guidance
4. **Quality Gates:** Define quality gates and acceptance criteria
5. **CI/CD Ready:** Instructions should be automatable
6. **Complete Audit Trail:** Log ALL user inputs
7. **Explicit Approval:** WAIT for user approval before proceeding

---

## Templates Reference

All templates are located in `../../templates/` directory:

- **Audit Logs:** `audit-logs/basic-entry.md`
- **State:** `state/aidlc-state.md`

---

## Next Stage

After approval:
- **Operations** stage (placeholder for future deployment and monitoring workflows)

---

**End of Build and Test Stage Instructions**
