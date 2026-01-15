# AI-DLC 2-Day Workshop Guide

## Overview

This 2-day workshop provides a condensed, hands-on experience with the AI-DLC workflow. The workshop focuses on completing a simplified project end-to-end, demonstrating key phases and deliverables.

**Target Audience**: Teams new to AI-DLC who want a quick introduction and practical experience.

**Workshop Goals**:
1. Understand AI-DLC workflow phases
2. Complete a small project using AI-DLC
3. Generate key deliverables and reports
4. Learn how to transition phases and provide boundaries

---

## Day 1 Schedule

### Morning Session (3.5 hours)

#### 9:00 AM - 9:30 AM: Welcome and Setup (30 min)
- **Activity**: Workshop introduction, agenda review
- **Setup**: Verify AI-DLC installation (see [installation guide](00-installation-guide.md))
- **Deliverable**: All participants have working AI-DLC setup

#### 9:30 AM - 11:00 AM: Phase 1 - Discovery (90 min)
- **Objective**: Establish environment, coding standards, and Agile process
- **Instructions**: See [Discovery phase instructions](phase-instructions/01-discovery.md)
- **Key Activities**:
  - Workspace detection
  - Environment setup documentation
  - Coding standards definition
  - Agile process establishment
- **Deliverable**: [Discovery Report](report-templates/discovery-report.md)
- **Example Phase Boundary Input**: 
  ```
  "Discovery phase complete. Ready to proceed to Vision phase."
  ```

#### 11:00 AM - 11:15 AM: Break (15 min)

#### 11:15 AM - 12:00 PM: Phase 2 - Vision (45 min)
- **Objective**: Encapsulate complete business vision and MVP scope
- **Instructions**: See [Vision phase instructions](phase-instructions/02-vision.md)
- **Key Activities**:
  - Requirements analysis
  - Business vision documentation
  - MVP scope definition
  - Stakeholder alignment
- **Deliverable**: [Business Vision Report](report-templates/business-vision-report.md)
- **Note**: Vision phase continues after lunch

#### 12:00 PM - 12:30 PM: Lunch (30 min)

#### 12:30 PM - 1:00 PM: Phase 2 - Vision (Complete) (30 min)
- **Objective**: Complete business vision and MVP scope
- **Key Activities**:
  - Finalize requirements analysis
  - Complete business vision documentation
  - Finalize MVP scope definition
  - Stakeholder alignment confirmation
- **Deliverable**: [Business Vision Report](report-templates/business-vision-report.md)
- **Example Phase Boundary Input**:
  ```
  "Vision phase complete. MVP scope approved. Ready to proceed to Units and User Stories phase."
  ```

### Afternoon Session (3.5 hours)

#### 1:00 PM - 2:30 PM: Phase 3 - Units and User Stories (90 min)
- **Objective**: Break down problem into units and associated stories
- **Instructions**: See [Units and User Stories phase instructions](phase-instructions/03-units-and-stories.md)
- **Key Activities**:
  - User story generation
  - Units of work decomposition
  - Story-to-unit mapping
  - Scope validation
- **Deliverable**: [Scope Report](report-templates/scope-report.md)
- **Example Phase Boundary Input**:
  ```
  "Units and User Stories phase complete. All stories assigned to units. Ready to proceed to Design phase."
  ```

#### 3:30 PM - 3:45 PM: Break (15 min)

#### 3:45 PM - 4:30 PM: Phase 4 - Design (45 min)
- **Objective**: Begin design review for all units
- **Instructions**: See [Design phase instructions](phase-instructions/04-design.md)
- **Key Activities**:
  - Application design overview
  - Initial functional design
  - Design planning
- **Deliverable**: Initial design artifacts
- **Note**: Complete design review continues on Day 2 morning

---

## Day 2 Schedule

### Morning Session (3.5 hours)

#### 9:00 AM - 9:15 AM: Day 1 Recap (15 min)
- **Activity**: Review Day 1 deliverables and progress
- **Discussion**: Address any questions or concerns

#### 9:15 AM - 9:45 AM: Phase 4 - Design (Complete) (30 min)
- **Objective**: Complete design review for all units
- **Key Activities**:
  - Complete functional design per unit
  - Infrastructure design (if applicable)
  - NFR design (if applicable)
  - Design compatibility review
- **Deliverable**: [Design Compatibility Report](report-templates/design-compatibility-report.md)
- **Example Phase Boundary Input**:
  ```
  "Design phase complete. All designs reviewed and compatible. Ready to proceed to Code Development phase."
  ```

#### 9:45 AM - 10:00 AM: Break (15 min)

#### 10:00 AM - 12:00 PM: Phase 5 - Code Development (Part 1) (120 min)
- **Objective**: AI builds the code for all units
- **Instructions**: See [Code Development phase instructions](phase-instructions/05-code-development.md)
- **Key Activities**:
  - Code generation planning
  - Code generation per unit
  - Code review and validation
  - Unit test generation
- **Note**: Code Development continues after lunch

#### 12:00 PM - 12:30 PM: Lunch (30 min)

#### 12:30 PM - 1:00 PM: Phase 5 - Code Development (Complete) (30 min)
- **Objective**: Complete code development for all units
- **Key Activities**:
  - Finalize code generation
  - Complete code review and validation
  - Finalize unit test generation
- **Deliverable**: Code artifacts and summaries
- **Example Phase Boundary Input**:
  ```
  "Code Development phase complete. All units implemented. Ready to proceed to Testing phase."
  ```

### Afternoon Session (3.5 hours)

#### 1:00 PM - 2:15 PM: Phase 6 - Testing (75 min)
- **Objective**: Test plan generation, test harness, and execution
- **Instructions**: See [Testing phase instructions](phase-instructions/06-testing.md)
- **Key Activities**:
  - Test plan generation
  - Test harness setup
  - Test execution
  - Test results review
  - Fix any failing tests
  - Validate test coverage
- **Deliverable**: Test results and build instructions
- **Example Phase Boundary Input**:
  ```
  "Testing phase complete. All tests passing. Workshop complete."
  ```

#### 2:15 PM - 2:30 PM: Break (15 min)

#### 2:30 PM - 4:30 PM: Demo and Final Review (120 min)
- **Activity**: Live demonstration of completed project
- **Demo Activities**:
  - Showcase working application
  - Walk through key features
  - Demonstrate test execution
  - Review generated code and documentation
  - Highlight AI-DLC workflow benefits
- **Final Review**:
  - Review all generated deliverables
  - Workshop learnings and takeaways
  - How to apply AI-DLC to real projects
  - Best practices and tips
  - Q&A session
- **Deliverable**: Workshop summary, demo recording (if applicable), and next steps

---

## Workshop Deliverables Checklist

By the end of the workshop, participants should have:

### Phase 1 - Discovery
- [ ] Discovery Report (`aidlc-docs/inception/discovery-report.md`)
- [ ] Environment setup documentation
- [ ] Coding standards document
- [ ] Agile process definition

### Phase 2 - Vision
- [ ] Business Vision Report (`aidlc-docs/inception/business-vision-report.md`)
- [ ] Requirements document
- [ ] MVP scope definition
- [ ] Stakeholder alignment confirmation

### Phase 3 - Units and User Stories
- [ ] Scope Report (`aidlc-docs/inception/scope-report.md`)
- [ ] User stories document
- [ ] Units of work definition
- [ ] Story-to-unit mapping

### Phase 4 - Design
- [ ] Design Compatibility Report (`aidlc-docs/construction/design-compatibility-report.md`)
- [ ] Application design artifacts
- [ ] Functional design per unit
- [ ] Infrastructure design (if applicable)

### Phase 5 - Code Development
- [ ] Generated code for all units
- [ ] Unit tests
- [ ] Code summaries per unit
- [ ] Build configuration

### Phase 6 - Testing
- [ ] Test plan
- [ ] Test execution results
- [ ] Build instructions
- [ ] Test coverage report

---

## Time Management Tips

1. **Stick to Timeboxes**: Each phase has a specific time allocation. Use timers to stay on track.

2. **Use Example Inputs**: When transitioning between phases, use the provided example phase boundary inputs to clearly communicate completion.

3. **Parallel Work**: For larger teams, consider splitting units across team members during Code Development phase.

4. **Focus on Learning**: Don't worry about perfect code - focus on understanding the workflow and process.

5. **Document Decisions**: Use the AI-DLC audit trail to capture all decisions and discussions.

---

## Example Project Suggestions

For the 2-day workshop, choose a simple project that can be completed end-to-end:

1. **Todo List API**: REST API for managing todo items
   - Simple CRUD operations
   - Single unit of work
   - Minimal infrastructure needs

2. **User Authentication Service**: Basic authentication service
   - User registration and login
   - JWT token generation
   - Single unit of work

3. **File Upload Service**: Service for uploading and managing files
   - File upload endpoint
   - File storage
   - Single unit of work

4. **Simple E-commerce Cart**: Shopping cart functionality
   - Add/remove items
   - Calculate totals
   - Single unit of work

---

## Common Challenges and Solutions

### Challenge: Phase Taking Too Long
**Solution**: Use the phase boundary inputs to move forward. You can always refine later.

### Challenge: AI Not Following Workflow
**Solution**: Ensure AI-DLC rules are properly installed. Start requests with "Using AI-DLC, ..."

### Challenge: Unclear Requirements
**Solution**: Use the Vision phase to ask clarifying questions. Don't proceed until requirements are clear.

### Challenge: Design Incompatibilities
**Solution**: Use the [Design Compatibility Report](report-templates/design-compatibility-report.md) to identify and resolve conflicts before coding.

---

## Next Steps After Workshop

1. **Apply to Real Project**: Use AI-DLC on your next project
2. **Customize Workflow**: Adapt phases to your team's needs
3. **Share Learnings**: Document what worked and what didn't
4. **Iterate**: Refine your AI-DLC usage based on experience

---

## Additional Resources

- **5-Day Workshop**: For more comprehensive coverage, see [5-Day Workshop Guide](02-workshop-5day.md)
- **Phase Instructions**: Detailed instructions in [phase-instructions/](phase-instructions/) directory
- **Report Templates**: Templates in [report-templates/](report-templates/) directory
- **AI-DLC Documentation**: See main [README.md](../README.md) for complete documentation
