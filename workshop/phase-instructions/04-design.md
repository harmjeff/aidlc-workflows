# Phase 4: Design - Instructions

## Overview

The Design phase creates comprehensive designs for all units, including application design, functional design, infrastructure design, and NFR design. This phase ensures all designs are compatible and cover the full scope before code development begins.

## Objectives

1. Create high-level application design
2. Design functional logic for each unit
3. Design infrastructure for each unit
4. Design NFR implementations
5. Validate design compatibility

## Duration

- **2-Day Workshop**: 135 minutes
- **5-Day Workshop**: 4 hours 15 minutes (split across Day 2)

## Prerequisites

- Units and User Stories phase complete
- Scope Report reviewed and approved
- Units of work defined
- Stories mapped to units

## Step-by-Step Instructions

### Step 1: Start Design Phase

Begin by communicating that Units and User Stories is complete and you're ready for Design:

**Example Input:**
```
Units and User Stories phase complete. All stories assigned to units, dependencies mapped. Ready to proceed to Design phase.
```

The AI will automatically:
- Load Units and User Stories artifacts
- Begin Application Design
- Guide you through all design stages

### Step 2: Application Design

The AI will create high-level application design:

**What Will Be Designed:**
- Component identification
- Component responsibilities
- Component methods
- Service layer design
- Component dependencies

**Example Questions AI May Ask:**
- What architectural pattern should be used?
- How should components be organized?
- What are the service boundaries?

**Example Answers:**
```
[Answer]: A) Layered architecture with service layer
[Answer]: B) Components organized by business domain
[Answer]: C) Service boundaries align with unit boundaries
```

### Step 3: Functional Design (Per Unit)

For each unit, the AI will design functional logic:

**What Will Be Designed:**
- Business logic models
- Domain entities
- Business rules
- Data flow
- Validation logic

**Example Questions AI May Ask:**
- What are the core business entities?
- What business rules apply?
- How should data be validated?

**Example Answers:**
```
[Answer]: A) User, Project, Task entities
[Answer]: B) Tasks must belong to a project, users must be authenticated
[Answer]: C) Input validation at API layer, business validation at service layer
```

### Step 4: NFR Requirements (Per Unit)

For each unit, the AI will assess NFR requirements:

**What Will Be Assessed:**
- Performance requirements
- Security requirements
- Scalability requirements
- Reliability requirements
- Observability requirements

**Example Questions AI May Ask:**
- What are the performance targets?
- What security measures are needed?
- How should the system scale?

**Example Answers:**
```
[Answer]: A) Response time < 2 seconds, support 100 concurrent users
[Answer]: B) OAuth 2.0, encrypted data, role-based access control
[Answer]: C) Horizontal scaling, auto-scaling based on load
```

### Step 5: NFR Design (Per Unit)

For each unit, the AI will design NFR implementations:

**What Will Be Designed:**
- Performance patterns
- Security patterns
- Scalability patterns
- Observability patterns

### Step 6: Infrastructure Design (Per Unit)

For each unit, the AI will design infrastructure:

**What Will Be Designed:**
- Deployment architecture
- Infrastructure services
- Networking
- Storage
- Monitoring

**Example Questions AI May Ask:**
- What cloud provider will be used?
- What deployment model? (Lambda, ECS, EC2, etc.)
- What database technology?

**Example Answers:**
```
[Answer]: A) AWS
[Answer]: B) ECS Fargate for services, Lambda for event processing
[Answer]: C) PostgreSQL for relational data, DynamoDB for high-throughput
```

### Step 7: Design Compatibility Review

The AI will review all designs for compatibility:

**What Will Be Reviewed:**
- Design consistency across units
- Integration compatibility
- Dependency compatibility
- Infrastructure compatibility

**Review the Design Compatibility Report:**
- Check for conflicts
- Validate integration points
- Ensure all scope is covered
- Identify out-of-scope design elements

### Step 8: Generate Design Compatibility Report

The AI will automatically generate the Design Compatibility Report as part of the workflow. To ensure the report is generated:

**Automatic Generation:**
- The AI will create the Design Compatibility Report automatically after completing all design activities
- The report will be saved to `aidlc-docs/construction/design-compatibility-report.md`

**If Report Not Generated:**
- Request report generation: "Please generate the Design Compatibility Report using the template at `report-templates/design-compatibility-report.md`"
- Reference the template: "Use the Design Compatibility Report template to create a complete report reviewing all designs for compatibility"

**Report Generation Request Example:**
```
Please generate the Design Compatibility Report based on all our design work. Use the template at report-templates/design-compatibility-report.md and:
- Review all designs for compatibility
- Validate integration points between units
- Check data model consistency
- Verify API contract compatibility
- Document any design issues and resolutions
- Validate scope coverage
```

**Verify Report Generation:**
- Check that `aidlc-docs/construction/design-compatibility-report.md` exists
- Verify the report contains all required sections from the template
- Ensure compatibility review is complete for all units
- Confirm all design issues are documented with resolutions

### Step 9: Review and Approve Design

Review all design artifacts and approve to proceed:

**Example Phase Boundary Input:**
```
Design phase complete. All designs reviewed, validated for compatibility, and approved. Ready to proceed to Code Development phase.
```

## Deliverables

After completing this phase, you should have:

1. **Design Compatibility Report** (`aidlc-docs/construction/design-compatibility-report.md`)
   - Design compatibility review
   - Integration validation
   - Out-of-scope design elements
   - Compatibility issues and resolutions

2. **Application Design** (`aidlc-docs/inception/application-design/`)
   - Components definition
   - Component methods
   - Services definition
   - Component dependencies

3. **Functional Design** (per unit) (`aidlc-docs/construction/{unit-name}/functional-design/`)
   - Business logic models
   - Domain entities
   - Business rules

4. **NFR Requirements** (per unit) (`aidlc-docs/construction/{unit-name}/nfr-requirements/`)
   - NFR assessment
   - Technology stack selection

5. **NFR Design** (per unit) (`aidlc-docs/construction/{unit-name}/nfr-design/`)
   - NFR patterns
   - Logical components

6. **Infrastructure Design** (per unit) (`aidlc-docs/construction/{unit-name}/infrastructure-design/`)
   - Infrastructure services
   - Deployment architecture

## Report Validation

### Step 10: Validate Design Compatibility Report and All Designs

Before proceeding to the next phase, validate all design artifacts:

**Access the Reports:**
- Open `aidlc-docs/construction/design-compatibility-report.md` (or the location specified by the AI)
- Review all design artifacts in `aidlc-docs/inception/application-design/`
- Review all unit design artifacts in `aidlc-docs/construction/{unit-name}/`

**Design Compatibility Report Validation Checklist:**
- [ ] **Design Overview**: All design artifacts listed with status
- [ ] **Component Compatibility**: All components integrate correctly with each other
- [ ] **Data Model Compatibility**: Data models are consistent across units
- [ ] **API Contract Compatibility**: API contracts are compatible between units
- [ ] **Infrastructure Compatibility**: Infrastructure components are compatible
- [ ] **Scope Coverage**: All in-scope features have corresponding designs
- [ ] **Story Design Coverage**: All user stories have design coverage
- [ ] **Out-of-Scope Design Elements**: Out-of-scope designs clearly identified
- [ ] **Integration Points**: All integration points between units documented
- [ ] **Design Issues**: Any identified issues documented with resolutions
- [ ] **Design Quality**: Design quality metrics and best practices verified
- [ ] **Human Tasks**: All required human tasks to complete the phase are listed

**Application Design Validation:**
- [ ] Components clearly defined with responsibilities
- [ ] Component methods documented
- [ ] Services defined with orchestration patterns
- [ ] Component dependencies mapped

**Functional Design Validation (per unit):**
- [ ] Business logic models documented
- [ ] Domain entities defined
- [ ] Business rules documented

**Infrastructure Design Validation (per unit):**
- [ ] Infrastructure services mapped
- [ ] Deployment architecture defined
- [ ] NFR patterns incorporated (if applicable)

**What to Check:**
1. **Compatibility**: No conflicts between unit designs
2. **Completeness**: All units have complete designs
3. **Integration**: Integration points are clearly defined
4. **Coverage**: All stories and features have design coverage
5. **Consistency**: Designs are consistent across units

**Validation Questions:**
- Are all designs compatible with each other?
- Do integration points between units work correctly?
- Are data models consistent across units?
- Are API contracts compatible?
- Is all in-scope work covered by designs?

**If Issues Found:**
- Request changes from the AI: "Please update the Design Compatibility Report to resolve [specific issue]"
- Review the report template: [Design Compatibility Report template](../report-templates/design-compatibility-report.md)
- Resolve conflicts before proceeding to code development
- Document any corrections in the audit trail

**Validation Complete When:**
- All checklist items are verified
- All designs are compatible
- No unresolved conflicts
- All scope is covered
- Ready to proceed to Code Development phase

## Example Phase Boundary Inputs

When you're ready to move to the next phase, use one of these inputs:

**Option 1 (Detailed):**
```
Design phase complete. All designs reviewed, validated for compatibility, and approved. Ready to proceed to Code Development phase.
```

**Option 2 (Simple):**
```
Design complete. Proceed to Code Development phase.
```

**Option 3 (With Specifics):**
```
Design phase complete. We've completed:
- Application design with 5 components
- Functional design for 3 units
- Infrastructure design: AWS ECS Fargate, PostgreSQL, DynamoDB
- All designs validated for compatibility
Ready to proceed to Code Development phase.
```

## Tips for Success

1. **Complete All Designs**: Don't skip design stages - they inform code generation
2. **Review Compatibility**: Use Design Compatibility Report to catch issues early
3. **Validate Scope**: Ensure all in-scope items are designed
4. **Document Decisions**: Capture all design decisions and rationale
5. **Think Integration**: Consider how units integrate when designing

## Common Questions

**Q: Do we need to design all units before coding?**
A: Yes, complete all designs first. This ensures compatibility and prevents rework.

**Q: What if designs conflict?**
A: Use the Design Compatibility Report to identify conflicts. Resolve before coding.

**Q: Can we skip NFR design?**
A: Only if there are no NFR requirements. Most projects need at least basic NFR design.

**Q: What if infrastructure changes?**
A: Update infrastructure design and regenerate Design Compatibility Report.

## Next Phase

After completing Design, proceed to:
- **Phase 5: Code Development** (see [05-code-development.md](05-code-development.md))
