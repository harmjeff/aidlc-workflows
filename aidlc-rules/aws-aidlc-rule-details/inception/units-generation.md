# Units Generation

## Purpose
Decompose system into manageable units of work for structured implementation.

## Execute IF
- System needs decomposition into multiple units of work **OR**
- Multiple services or modules required **OR**
- Complex system requiring structured breakdown

## Skip IF
- Single simple unit **AND**
- No decomposition needed **AND**
- Straightforward single-component implementation

---

## Two-Part Structure

This stage has two distinct parts:
1. **PART 1 - Planning:** Create unit plan, generate questions, collect answers, analyze ambiguities, get approval
2. **PART 2 - Generation:** Execute approved plan to generate unit artifacts

---

## PART 1 - Planning Steps

### 1. Log User Input
- **MANDATORY:** If user provides any input during this phase, log it in audit.md
- Use ISO 8601 timestamp format
- Capture complete raw input (never summarize)

### 2. Load Units Generation Steps
- Load all detailed steps from this file
- Understand two-part structure
- Understand unit decomposition criteria

### 3. Load Prior Context

**If Brownfield Project:**
- Load all reverse engineering artifacts from `aidlc-docs/inception/reverse-engineering/`
- Understand existing architecture
- Understand existing components

**Load Requirements:**
- Load requirements.md from Requirements Analysis stage

**If User Stories Executed:**
- Load stories.md
- Load personas.md

**Load Application Design:**
- Load components.md
- Load component-methods.md
- Load services.md
- Load component-dependency.md

### 4. Analyze Decomposition Needs

#### 4.1. Identify Decomposition Factors

**Complexity Factors:**
- Number of components involved
- Number of services involved
- Number of user stories to implement
- Technical complexity
- Integration complexity

**Organizational Factors:**
- Can work be parallelized?
- Are there natural boundaries?
- Are there dependencies between parts?
- Can parts be tested independently?

**Risk Factors:**
- High-risk areas that need isolation
- Areas requiring different expertise
- Areas with different timelines

#### 4.2. Determine Unit Boundaries

**Possible unit boundaries:**
- By component (one unit per component)
- By service (one unit per service)
- By feature (one unit per feature)
- By layer (one unit per architectural layer)
- By user story (one unit per story or epic)
- By module (one unit per module)
- Custom boundaries based on project needs

### 5. Create Unit of Work Plan

Create `aidlc-docs/inception/plans/unit-of-work-plan.md` using template from:
**`aidlc-workflow/templates/plans/units-generation-plan.md`**

**Template includes:**
- Plan overview
- 6 context-appropriate questions (decomposition strategy, granularity, dependencies, prioritization, testing, story mapping)
- Generation steps with checkboxes
- Mandatory artifacts list
- User instructions

### 6. Request User Input

```markdown
# 📦 Units Generation Planning

I've created a plan for decomposing the system into units of work. I need your input on a few questions to ensure the breakdown is appropriate for your needs.

**Plan File:** `aidlc-docs/inception/plans/unit-of-work-plan.md`

**Please:**
1. Open the plan file
2. Answer each question by entering the letter of your choice after [Answer]:
3. If you select "Other", provide details after the [Answer]: tag
4. Let me know when you've completed all questions

I'll wait for your responses before proceeding.
```

### 7. Collect Answers

- Wait for user to complete questions
- Read the plan file to extract answers
- Parse answers after [Answer]: tags
- Validate all questions are answered

### 8. Analyze Answers for Ambiguities

**MANDATORY:** Analyze ALL answers for ambiguities, contradictions, or unclear responses.

**Ambiguity Indicators:**
- "depends", "maybe", "not sure", "mix of", "somewhere between", "standard", "typical"
- Contradictions between answers
- Vague or borderline responses
- Incomplete "Other" descriptions

**If ANY ambiguities found:**

#### 8.1. Create Follow-Up Questions

Create `aidlc-docs/inception/plans/unit-planning-clarification.md` using template from:
**`aidlc-workflow/templates/questions/clarification-format.md`**

#### 8.2. Request Clarification

```markdown
# 🔍 Clarification Needed

I need some clarification on a few of your answers to ensure I create the right unit breakdown.

**Follow-Up Questions File:** `aidlc-docs/inception/plans/unit-planning-clarification.md`

Please answer these follow-up questions and let me know when complete.
```

#### 8.3. Repeat Until Resolved

- Collect follow-up answers
- Analyze again for ambiguities
- Create additional follow-up questions if needed
- **Do NOT proceed until ALL ambiguities are resolved**

### 9. Log Approval Prompt

Use audit log format from **`aidlc-workflow/templates/audit-logs/basic-entry.md`**:
- Stage: "Units Generation - Planning Approval Request"
- Context: "Units Generation PART 1 complete, waiting for approval to proceed to PART 2"

### 10. Wait for Explicit Approval (PART 1)

```markdown
# 📦 Units Generation Planning Complete

I've completed the planning phase for units generation.

**Plan Summary:**
- Decomposition strategy: [Strategy]
- Unit granularity: [Granularity]
- Unit dependencies: [Sequential/Parallel/Mixed]
- Unit prioritization: [Approach]
- Testing strategy: [Approach]

**Next Steps:**
I'm ready to generate the unit of work breakdown based on this plan.

---

**📋 Please approve the plan so I can proceed with unit generation, or request changes if needed.**
```

- **MANDATORY:** Do NOT proceed to PART 2 until user confirms
- User must approve the plan
- User may request changes to the plan
- Log approval prompt with timestamp

### 11. Log User Response (PART 1)

Use audit log format from **`aidlc-workflow/templates/audit-logs/basic-entry.md`**:
- Stage: "Units Generation - Planning User Response"
- Context: "User approval received for unit generation plan"

---

## PART 2 - Generation Steps

### 12. Load Unit Generation Plan

- Read `aidlc-docs/inception/plans/unit-of-work-plan.md`
- Review user answers
- Understand unit decomposition approach
- Load all design artifacts for reference

### 13. Execute Plan Steps

Work through each checkbox in the plan:

#### 13.1. Identify Unit Boundaries

Based on decomposition strategy:
- Define clear boundaries for each unit
- Ensure units are cohesive (related functionality together)
- Ensure units are loosely coupled (minimal dependencies)
- Ensure units are testable independently (where possible)

#### 13.2. Define Each Unit of Work

For each unit:
- Unit name and identifier
- Unit purpose and scope
- Unit responsibilities
- Components included in unit
- Services included in unit
- Estimated complexity
- Estimated effort

#### 13.3-13.5. Map Components, Services, and Stories

- Assign each component to a unit
- Assign each service to a unit
- Assign each user story to a unit (if applicable)
- Ensure all items are assigned
- Document rationale for assignments

#### 13.6-13.8. Dependencies and Prioritization

- Identify unit dependencies (what it depends on, what depends on it)
- Create unit dependency graph (visualize dependencies, identify critical path)
- Prioritize units (based on business value, risk, dependencies, technical foundation)

#### 13.9. Update Progress

**MANDATORY:** After completing each step, mark [x] in the plan file in the SAME interaction where work is completed.

### 14. Generate unit-of-work.md

Create `aidlc-docs/inception/application-design/unit-of-work.md`:

**Structure:**
- Overview (total units, decomposition approach)
- For each unit:
  - ID, priority, status
  - Purpose, scope, responsibilities
  - Components, services, user stories
  - Dependencies (depends on, required by)
  - Estimated complexity and effort
  - Testing strategy, acceptance criteria
  - Notes
- Unit summary (counts by priority and type)
- Implementation sequence (recommended order, parallel opportunities)

### 15. Generate unit-of-work-dependency.md

Create `aidlc-docs/inception/application-design/unit-of-work-dependency.md`:

**Structure:**
- Dependency overview
- Dependency graph (text representation)
- Unit dependencies detailed (for each unit: depends on, required by, external dependencies)
- Circular dependencies (status and resolution)
- Critical path (units that must be completed in order)
- Parallel development opportunities
- Integration points (between units)

### 16. Generate unit-of-work-story-map.md

**Only if using user stories:**

Create `aidlc-docs/inception/application-design/unit-of-work-story-map.md`:

**Structure:**
- Mapping overview
- Story-to-unit mapping (for each unit: assigned stories with priorities and acceptance criteria)
- Unit-to-story mapping table
- Story coverage (total, mapped, unmapped)
- Story implementation sequence

### 17. Update State Tracking

Update `aidlc-docs/aidlc-state.md` using template from:
**`aidlc-workflow/templates/state/aidlc-state.md`**
- Mark Units Generation as completed
- Update timestamp
- Set next stage to Construction Phase

### 18. Log Completion in audit.md

Use audit log format from **`aidlc-workflow/templates/audit-logs/basic-entry.md`**:
- Stage: "Units Generation - Stage Complete"
- Context: Units defined, dependencies mapped, stories mapped (if applicable), next stage

### 19. Present Completion Message

Use template from **`aidlc-workflow/templates/completion-messages/units-generation-complete.md`**

Fill in:
- Unit counts (total, by priority)
- Unit names and descriptions
- Dependency mapping details
- Story mapping details (if applicable)
- Implementation strategy (sequence, parallel opportunities, effort estimate)
- Next steps (CONSTRUCTION phase details)

### 20. Wait for Explicit Approval (PART 2)

- **MANDATORY:** Do NOT proceed until user confirms
- User must review unit breakdown and approve
- User may request changes or adjustments
- Log approval prompt with timestamp

**Approval Prompt Log:**
Use audit log format from **`aidlc-workflow/templates/audit-logs/basic-entry.md`**:
- Stage: "Units Generation - Generation Approval Request"
- Context: "Waiting for user to review unit breakdown"

### 21. Log User Response (PART 2)

Use audit log format from **`aidlc-workflow/templates/audit-logs/basic-entry.md`**:
- Stage: "Units Generation - Generation User Response"
- Context: "User approval received for unit breakdown"

---

## Artifacts Created

1. **aidlc-docs/inception/plans/unit-of-work-plan.md** - Unit generation approach, questions, answers, steps
2. **aidlc-docs/inception/application-design/unit-of-work.md** - Unit definitions, responsibilities, assignments, sequence
3. **aidlc-docs/inception/application-design/unit-of-work-dependency.md** - Dependencies, critical path, parallel opportunities, integration points
4. **aidlc-docs/inception/application-design/unit-of-work-story-map.md** - Story-to-unit mapping, sequence, coverage (if using stories)
5. **aidlc-docs/inception/plans/unit-planning-clarification.md** - Follow-up questions and clarifications (if ambiguities found)

---

## Load This File When
- Starting Units Generation stage
- After Application Design (if executed) or Workflow Planning
- System needs decomposition into multiple units

## Unload This File After
- PART 1 complete and approved
- PART 2 complete and approved
- All 3 mandatory artifacts generated
- Ready to proceed to CONSTRUCTION phase

---

## Key Principles

### Cohesive Units
- Each unit should have related functionality
- Units should have clear, single purpose
- Units should be independently understandable

### Loose Coupling
- Minimize dependencies between units
- Use clear interfaces between units
- Avoid circular dependencies

### Testable Units
- Units should be testable independently (where possible)
- Clear acceptance criteria per unit
- Integration points well-defined

### Manageable Size
- Units should be completable in reasonable time
- Not too large (overwhelming)
- Not too small (overhead)

### Two-Part Structure
- PART 1: Planning with questions and approval
- PART 2: Generation with execution and approval
- Two approval gates ensure quality

---

## Common Issues

### Issue: Too Many Units
**Solution:** Review unit boundaries. Combine related units. Ensure each unit provides meaningful value. Consider coarser granularity.

### Issue: Circular Dependencies Between Units
**Solution:** Identify the cycle. Restructure unit boundaries to break the cycle. Consider extracting shared functionality into separate unit.

### Issue: Uneven Unit Sizes
**Solution:** Review large units for decomposition opportunities. Review small units for combination opportunities. Aim for balanced effort across units.

### Issue: Unclear Unit Boundaries
**Solution:** Define what each unit DOES and does NOT do. Ensure responsibilities don't overlap. Clarify with user if needed.

### Issue: User Provides Vague Decomposition Preferences
**Solution:** Create follow-up questions. Provide examples of different approaches. Don't proceed until clear direction is established.

---

## Success Criteria

- [x] Prior context loaded (requirements, design, stories)
- [x] Decomposition needs analyzed
- [x] Unit generation plan created
- [x] Questions generated and answered
- [x] Ambiguities identified and resolved
- [x] PART 1 approval received
- [x] Plan steps executed with checkbox updates
- [x] Unit boundaries identified
- [x] All units defined with clear responsibilities
- [x] Components mapped to units
- [x] Services mapped to units
- [x] Stories mapped to units (if applicable)
- [x] Unit dependencies identified and mapped
- [x] Unit dependency graph created
- [x] Units prioritized
- [x] unit-of-work.md generated
- [x] unit-of-work-dependency.md generated
- [x] unit-of-work-story-map.md generated (if applicable)
- [x] State tracking updated
- [x] Audit log entries created
- [x] Completion message presented
- [x] PART 2 approval received
- [x] Ready to proceed to CONSTRUCTION phase
