# Phase 5: Code Development - Instructions

## Overview

The Code Development phase generates all code for the project units. The AI creates code, tests, and documentation based on the designs from previous phases. This phase implements all functionality defined in the user stories.

## Objectives

1. Generate code for all units
2. Create unit tests
3. Generate API documentation
4. Create deployment artifacts
5. Integrate all units

## Duration

- **2-Day Workshop**: 165 minutes
- **5-Day Workshop**: 1.5 days (Day 3 and Day 4)

## Prerequisites

- Design phase complete
- Design Compatibility Report reviewed and approved
- All designs validated

## Step-by-Step Instructions

### Step 1: Start Code Development Phase

Begin by communicating that Design is complete and you're ready for Code Development:

**Example Input:**
```
Design phase complete. All designs reviewed, validated for compatibility, and approved. Ready to proceed to Code Development phase.
```

The AI will automatically:
- Load Design phase artifacts
- Begin Code Planning for each unit
- Guide you through code generation

### Step 2: Code Planning (Per Unit)

For each unit, the AI will create a detailed code generation plan:

**What Will Be Planned:**
- Code structure
- File organization
- Implementation steps
- Test strategy
- Documentation requirements

**Review the Code Generation Plan:**
- Validate implementation approach
- Check story coverage
- Ensure dependencies are handled
- Approve plan before generation

**Example Questions AI May Ask:**
- What code organization structure should be used?
- What testing framework should be used?
- What documentation format is preferred?

**Example Answers:**
```
[Answer]: A) Layered structure: controllers, services, repositories, models
[Answer]: B) JUnit for Java, Jest for JavaScript
[Answer]: C) OpenAPI/Swagger for API documentation
```

### Step 3: Code Generation (Per Unit)

The AI will generate code for each unit:

**What Will Be Generated:**
- Business logic code
- API layer code
- Repository layer code
- Data models
- Configuration files
- Unit tests
- Code summaries

**Review Generated Code:**
- Check code quality
- Validate functionality
- Ensure tests are comprehensive
- Review code structure

### Step 4: Code Review

Review generated code for each unit:

**Review Areas:**
- Code quality and style
- Test coverage
- Error handling
- Documentation
- Performance considerations

**Provide Feedback:**
- Request changes if needed
- Approve code when satisfied
- Document any deviations

### Step 5: Unit Integration

After all units are generated, integrate them:

**Integration Activities:**
- Connect unit interfaces
- Test integration points
- Resolve integration issues
- Update integration documentation

### Step 6: Code Refinement (5-Day Workshop Only)

For the 5-day workshop, refine and optimize code:

**Refinement Activities:**
- Code optimization
- Performance improvements
- Error handling enhancements
- Documentation updates
- Code quality improvements

### Step 7: Final Code Review

Complete final review of all code:

**Review Checklist:**
- All units implemented
- All tests passing
- Integration complete
- Documentation complete
- Code quality acceptable

### Step 8: Generate Code Summaries and Documentation

The AI will automatically generate code summaries and API documentation as part of the workflow. To ensure all documentation is generated:

**Automatic Generation:**
- The AI will create code summaries automatically for each unit
- Code summaries will be saved to `aidlc-docs/construction/{unit-name}/code/`
- API documentation will be saved to `aidlc-docs/construction/{unit-name}/code/`

**If Documentation Not Generated:**
- Request code summaries: "Please generate code summaries for all units in `aidlc-docs/construction/{unit-name}/code/`"
- Request API documentation: "Please generate API documentation for all units including endpoint documentation and request/response examples"

**Documentation Generation Request Example:**
```
Please generate code summaries and API documentation for all units. For each unit, create:
- Code generation summary with implementation notes
- Architecture decisions documentation
- API specifications with endpoint documentation
- Request/response examples
Save all documentation to aidlc-docs/construction/{unit-name}/code/
```

**Verify Documentation Generation:**
- Check that code summaries exist for all units in `aidlc-docs/construction/{unit-name}/code/`
- Verify API documentation exists for all units
- Ensure documentation is complete and accurate
- Confirm all units have corresponding documentation

### Step 9: Review and Approve Code

Review all code artifacts and approve to proceed:

**Example Phase Boundary Input:**
```
Code Development phase complete. All units implemented, integrated, and reviewed. Ready to proceed to Testing phase.
```

## Deliverables

After completing this phase, you should have:

1. **Code Artifacts** (workspace root)
   - Source code for all units
   - Configuration files
   - Build files

2. **Unit Tests** (workspace root)
   - Unit tests for all units
   - Test utilities
   - Test configuration

3. **Code Summaries** (per unit) (`aidlc-docs/construction/{unit-name}/code/`)
   - Code generation summaries
   - Implementation notes
   - Architecture decisions

4. **API Documentation** (`aidlc-docs/construction/{unit-name}/code/`)
   - API specifications
   - Endpoint documentation
   - Request/response examples

5. **Build Configuration** (workspace root)
   - Build scripts
   - Dependency files
   - Environment configuration

## Code Validation

### Step 10: Validate Generated Code

Before proceeding to the next phase, validate all generated code:

**Access the Code:**
- Review source code in workspace root (not in `aidlc-docs/`)
- Review code summaries in `aidlc-docs/construction/{unit-name}/code/`
- Review API documentation in `aidlc-docs/construction/{unit-name}/code/`

**Code Validation Checklist:**
- [ ] **Code Completeness**: All units have complete code implementations
- [ ] **Build Success**: Code builds successfully without errors
- [ ] **Unit Tests**: Unit tests exist for all units
- [ ] **Test Execution**: Unit tests can be executed (may not all pass yet)
- [ ] **Code Structure**: Code follows the defined project structure
- [ ] **Coding Standards**: Code adheres to documented coding standards
- [ ] **Integration**: Units are integrated correctly
- [ ] **Documentation**: Code summaries and API documentation are complete
- [ ] **Dependencies**: All dependencies are properly configured

**What to Check:**
1. **Build Verification**: Run build command and verify success
   ```bash
   # Example commands (adjust for your build system):
   mvn clean install
   npm run build
   gradle build
   ```
2. **Code Review**: Review generated code for quality and completeness
3. **Test Existence**: Verify unit tests exist for all units
4. **Integration**: Verify units integrate correctly
5. **Documentation**: Review code summaries and API documentation

**Build Verification Steps:**
1. Navigate to workspace root
2. Run build command for your project type
3. Verify build completes successfully
4. Check for any warnings or errors
5. Verify build artifacts are generated

**Code Quality Checks:**
- Code follows coding standards from Discovery phase
- Code structure matches design from Design phase
- Error handling is implemented
- Code is properly documented
- No obvious bugs or issues

**If Issues Found:**
- Request fixes from the AI: "Please fix [specific issue] in the generated code"
- Review code generation plan: Check `aidlc-docs/construction/plans/{unit-name}-code-generation-plan.md`
- Fix issues manually if needed, document changes
- Re-run build to verify fixes

**Validation Complete When:**
- Code builds successfully
- All units are implemented
- Unit tests exist (may not all pass - that's for Testing phase)
- Integration is complete
- Ready to proceed to Testing phase

## Example Phase Boundary Inputs

When you're ready to move to the next phase, use one of these inputs:

**Option 1 (Detailed):**
```
Code Development phase complete. All units implemented, integrated, and reviewed. Ready to proceed to Testing phase.
```

**Option 2 (Simple):**
```
Code Development complete. Proceed to Testing phase.
```

**Option 3 (With Specifics):**
```
Code Development phase complete. We've implemented:
- User Service: 5 endpoints, 15 unit tests
- Project Service: 4 endpoints, 12 unit tests
- Task Service: 6 endpoints, 18 unit tests
- All units integrated and tested
Ready to proceed to Testing phase.
```

## Tips for Success

1. **Review Plans**: Review code generation plans before approving
2. **Incremental Approval**: Approve code unit by unit
3. **Test Early**: Run tests as code is generated
4. **Document Decisions**: Capture implementation decisions
5. **Integration Focus**: Pay attention to integration points

## Common Questions

**Q: Can we modify generated code?**
A: Yes, but document changes. The AI can regenerate if needed.

**Q: What if tests fail?**
A: Review failures, fix issues, and regenerate if needed.

**Q: Can we skip some units?**
A: No, all units should be implemented for complete functionality.

**Q: What if code quality is poor?**
A: Request improvements or refine manually. Document quality issues.

## Next Phase

After completing Code Development, proceed to:
- **Phase 6: Testing** (see [06-testing.md](06-testing.md))
