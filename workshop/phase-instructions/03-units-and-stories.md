# Phase 3: Units and User Stories - Instructions

## Overview

The Units and User Stories phase breaks down the problem into manageable units of work and creates user stories with acceptance criteria. This phase ensures the work is properly decomposed and all requirements are captured as testable user stories.

## Objectives

1. Generate user stories from requirements
2. Create user personas
3. Decompose system into units of work
4. Map stories to units
5. Validate scope boundaries

## Duration

- **2-Day Workshop**: 90 minutes
- **5-Day Workshop**: 135 minutes

## Prerequisites

- Vision phase complete
- Business Vision Report reviewed and approved
- Requirements documented

## Step-by-Step Instructions

### Step 1: Start Units and User Stories Phase

Begin by communicating that Vision is complete and you're ready for Units and User Stories:

**Example Input:**
```
Vision phase complete. Business vision documented, MVP scope approved by stakeholders. Ready to proceed to Units and User Stories phase.
```

The AI will automatically:
- Load Vision phase artifacts
- Begin User Stories generation
- Guide you through story creation and unit decomposition

### Step 2: User Stories Planning

The AI will create a plan for generating user stories:

**What the AI Will Do:**
- Analyze requirements
- Identify user personas
- Plan story breakdown approach
- Create story generation plan

**Example Questions AI May Ask:**
- How should stories be organized? (User journey-based, feature-based, persona-based)
- What level of detail is needed for stories?
- How should acceptance criteria be structured?

**Example Answers:**
```
[Answer]: A) User journey-based approach
[Answer]: B) Detailed stories with clear acceptance criteria
[Answer]: C) Given-When-Then format for acceptance criteria
```

### Step 3: Answer Story Planning Questions

Provide answers to questions about story structure and format:

**Areas to Consider:**
- Story organization approach
- Persona identification
- Story granularity
- Acceptance criteria format

### Step 4: User Stories Generation

The AI will generate user stories based on your answers:

**What Will Be Generated:**
- User personas
- User stories with acceptance criteria
- Story prioritization
- Story dependencies

**Review the Generated Stories:**
- Ensure all requirements are covered
- Validate story completeness
- Check acceptance criteria clarity

### Step 5: Units of Work Planning

The AI will create a plan for decomposing the system into units:

**What the AI Will Do:**
- Analyze stories and requirements
- Identify logical units of work
- Plan decomposition approach
- Create unit generation plan

**Example Questions AI May Ask:**
- How should the system be decomposed? (Microservices, modules, components)
- What are the unit boundaries?
- How should dependencies be managed?

**Example Answers:**
```
[Answer]: A) Microservices architecture with independent services
[Answer]: B) Service boundaries based on business domains
[Answer]: C) API contracts for inter-service communication
```

### Step 6: Answer Unit Planning Questions

Provide answers to questions about unit decomposition:

**Areas to Consider:**
- Unit boundaries
- Dependency management
- Deployment strategy
- Team ownership

### Step 7: Units Generation

The AI will generate units of work:

**What Will Be Generated:**
- Unit definitions
- Unit responsibilities
- Unit dependencies
- Story-to-unit mapping

**Review the Generated Units:**
- Ensure all stories are assigned
- Validate unit boundaries
- Check dependency relationships

### Step 8: Scope Validation

Validate that scope is properly defined:

**In-Scope Validation:**
- All MVP features have stories
- All stories are assigned to units
- Dependencies are identified

**Out-of-Scope Validation:**
- Deferred features are documented
- Out-of-scope items are clearly marked
- Future work is identified

### Step 9: Generate Scope Report and Artifacts

The AI will automatically generate the Scope Report and all artifacts as part of the workflow. To ensure all reports are generated:

**Automatic Generation:**
- The AI will create the Scope Report automatically after completing units and stories
- The report will be saved to `aidlc-docs/inception/scope-report.md`
- User stories will be saved to `aidlc-docs/inception/user-stories/stories.md`
- Personas will be saved to `aidlc-docs/inception/user-stories/personas.md`
- Unit definitions will be saved to `aidlc-docs/inception/application-design/unit-of-work.md`
- Dependencies will be saved to `aidlc-docs/inception/application-design/unit-of-work-dependency.md`
- Story-to-unit mapping will be saved to `aidlc-docs/inception/application-design/unit-of-work-story-map.md`

**If Reports Not Generated:**
- Request report generation: "Please generate the Scope Report using the template at `report-templates/scope-report.md`"
- Request artifacts: "Please generate all units and user stories artifacts including stories.md, personas.md, unit-of-work.md, unit-of-work-dependency.md, and unit-of-work-story-map.md"

**Report Generation Request Example:**
```
Please generate the Scope Report and all artifacts based on our units and user stories work. Use the template at report-templates/scope-report.md and create:
- Scope Report with in-scope and out-of-scope validation
- User stories document with all stories and acceptance criteria
- Personas document with all user personas
- Unit of work definitions for all units
- Unit dependency matrix
- Story-to-unit mapping
```

**Verify Report Generation:**
- Check that all artifact files exist in their expected locations
- Verify the Scope Report contains all required sections from the template
- Ensure all stories are documented in stories.md
- Confirm all units are defined in unit-of-work.md
- Verify story-to-unit mapping is complete

### Step 10: Review and Approve

Review the generated artifacts and approve to proceed:

**Example Phase Boundary Input:**
```
Units and User Stories phase complete. All stories assigned to units, dependencies mapped. Ready to proceed to Design phase.
```

## Deliverables

After completing this phase, you should have:

1. **Scope Report** (`aidlc-docs/inception/scope-report.md`)
   - In-scope validation
   - Out-of-scope documentation
   - Scope boundaries
   - Future work identification

2. **User Stories** (`aidlc-docs/inception/user-stories/stories.md`)
   - User stories with acceptance criteria
   - Story prioritization
   - Story dependencies

3. **User Personas** (`aidlc-docs/inception/user-stories/personas.md`)
   - User persona definitions
   - Persona characteristics
   - Persona-to-story mapping

4. **Units of Work** (`aidlc-docs/inception/application-design/unit-of-work.md`)
   - Unit definitions
   - Unit responsibilities
   - Unit boundaries

5. **Unit Dependencies** (`aidlc-docs/inception/application-design/unit-of-work-dependency.md`)
   - Dependency matrix
   - Dependency relationships
   - Integration points

6. **Story-to-Unit Mapping** (`aidlc-docs/inception/application-design/unit-of-work-story-map.md`)
   - Story assignments
   - Unit coverage
   - Story dependencies

## Report Validation

### Step 11: Validate Scope Report and Artifacts

Before proceeding to the next phase, validate all generated artifacts:

**Access the Reports:**
- Open `aidlc-docs/inception/scope-report.md` (or the location specified by the AI)
- Open `aidlc-docs/inception/user-stories/stories.md`
- Open `aidlc-docs/inception/user-stories/personas.md`
- Open `aidlc-docs/inception/application-design/unit-of-work.md`
- Review all generated artifacts

**Scope Report Validation Checklist:**
- [ ] **In-Scope Validation**: All MVP features have corresponding user stories and unit assignments
- [ ] **Story-to-Unit Mapping**: All stories are assigned to units with clear coverage
- [ ] **Scope Completeness**: All MVP features covered, no gaps identified
- [ ] **Out-of-Scope Documentation**: Deferred features clearly documented with rationale
- [ ] **Future Work Identification**: Future releases and priorities documented
- [ ] **Unit Decomposition**: Units clearly defined with responsibilities and dependencies
- [ ] **Dependency Matrix**: Unit dependencies documented with integration methods
- [ ] **Story Summary**: Total stories, breakdown by unit, and completeness verified
- [ ] **Scope Boundaries**: Clear boundaries between in-scope and out-of-scope
- [ ] **Human Tasks**: All required human tasks to complete the phase are listed

**User Stories Validation:**
- [ ] All stories have clear acceptance criteria
- [ ] Stories follow INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- [ ] Stories are assigned to personas
- [ ] Stories are prioritized and estimated
- [ ] Story dependencies are identified

**Units Validation:**
- [ ] All units have clear purposes and responsibilities
- [ ] Unit boundaries are well-defined
- [ ] Dependencies between units are documented
- [ ] Integration points are identified

**What to Check:**
1. **Coverage**: Every MVP feature from Vision phase has at least one user story
2. **Assignment**: Every story is assigned to exactly one unit
3. **Completeness**: No placeholder text or incomplete sections
4. **Clarity**: Scope boundaries are unambiguous
5. **Traceability**: Can trace from MVP features → Stories → Units

**Validation Questions:**
- Are all MVP features covered by user stories?
- Are all stories assigned to appropriate units?
- Are unit boundaries clear and logical?
- Are dependencies between units documented?
- Is out-of-scope work clearly identified?

**If Issues Found:**
- Request changes from the AI: "Please update the Scope Report to include [specific item]"
- Review the report template: [Scope Report template](../report-templates/scope-report.md)
- Document any corrections in the audit trail

**Validation Complete When:**
- All checklist items are verified
- All artifacts are complete and accurate
- Scope boundaries are clear and validated
- Ready to proceed to Design phase

## Example Phase Boundary Inputs

When you're ready to move to the next phase, use one of these inputs:

**Option 1 (Detailed):**
```
Units and User Stories phase complete. All stories assigned to units, dependencies mapped. Ready to proceed to Design phase.
```

**Option 2 (Simple):**
```
Units and User Stories complete. Proceed to Design phase.
```

**Option 3 (With Specifics):**
```
Units and User Stories phase complete. We've created:
- 15 user stories across 3 personas
- 3 units of work: User Service, Project Service, Task Service
- Dependencies mapped and validated
Ready to proceed to Design phase.
```

## Tips for Success

1. **Complete Stories**: Ensure all requirements are captured as stories
2. **Clear Acceptance Criteria**: Write testable acceptance criteria
3. **Validate Scope**: Use Scope Report to ensure boundaries are clear
4. **Review Dependencies**: Understand unit dependencies before design
5. **Involve Team**: Get team input on story breakdown and unit boundaries

## Common Questions

**Q: How many stories should we have?**
A: Enough to cover all MVP features. Typically 10-20 stories for a small project.

**Q: How should units be sized?**
A: Units should be independently deployable (for microservices) or logically cohesive (for monoliths).

**Q: What if a story doesn't fit in any unit?**
A: Review unit boundaries. You may need to adjust units or create a new unit.

**Q: Can stories span multiple units?**
A: Stories should map to a primary unit. Integration between units is handled in design.

## Next Phase

After completing Units and User Stories, proceed to:
- **Phase 4: Design** (see [04-design.md](04-design.md))
