# Phase 2: Vision - Instructions

## Overview

The Vision phase encapsulates the complete business vision for the project and defines the MVP scope. This phase ensures all stakeholders understand what is being built and why, and establishes clear boundaries for the initial release.

## Objectives

1. Document complete business vision
2. Gather and analyze requirements
3. Define MVP scope
4. Align stakeholders
5. Assess risks and constraints

## Duration

- **2-Day Workshop**: 105 minutes
- **5-Day Workshop**: 2 hours 45 minutes (split across Day 1)

## Prerequisites

- Discovery phase complete
- Discovery Report reviewed and approved
- Stakeholders identified

## Step-by-Step Instructions

### Step 1: Start Vision Phase

Begin by communicating that Discovery is complete and you're ready for Vision:

**Example Input:**
```
Discovery phase complete. Environment established, coding standards defined, Agile process documented. Ready to proceed to Vision phase.
```

The AI will automatically:
- Load Discovery phase artifacts
- Begin Requirements Analysis
- Guide you through vision and scope definition

### Step 2: Requirements Analysis

The AI will analyze your project request and gather requirements:

**What to Provide:**
- Project description and goals
- Business objectives
- User needs
- Functional requirements
- Non-functional requirements

**Example Initial Input:**
```
Using AI-DLC, I want to build a task management system that allows teams to collaborate on projects, assign tasks, and track progress.
```

### Step 3: Answer Clarifying Questions

The AI will ask questions to understand requirements better:

**Example Questions:**
- Who are the primary users of this system?
- What are the core features needed for MVP?
- What are the performance requirements?
- What are the security requirements?

**Example Answers:**
```
[Answer]: A) Project managers, team members, and stakeholders
[Answer]: B) User authentication, project creation, task assignment, progress tracking
[Answer]: C) Support 100 concurrent users, response time < 2 seconds
[Answer]: D) OAuth 2.0 authentication, encrypted data storage
```

### Step 4: Business Vision Documentation

Work with the AI to document:

**Business Vision:**
- Problem statement
- Solution overview
- Business objectives
- Success criteria
- Target users

**Example Questions AI May Ask:**
- What problem does this solve?
- What are the key business objectives?
- How will success be measured?

**Example Answers:**
```
[Answer]: A) Teams struggle to coordinate tasks and track project progress
[Answer]: B) Improve team productivity by 30%, reduce project delays by 20%
[Answer]: C) User adoption rate, task completion rate, project on-time delivery
```

### Step 5: MVP Scope Definition

Define what's included in the MVP:

**In-Scope:**
- Core features for initial release
- Essential user workflows
- Minimum viable functionality

**Out-of-Scope:**
- Features deferred to future releases
- Nice-to-have features
- Advanced functionality

**Example Questions AI May Ask:**
- What features are essential for MVP?
- What can be deferred to later releases?
- What are the acceptance criteria for MVP?

**Example Answers:**
```
[Answer]: A) User authentication, project management, task assignment, basic reporting
[Answer]: B) Advanced analytics, integrations, mobile app, real-time notifications
[Answer]: C) Users can create projects, assign tasks, and view progress dashboard
```

### Step 6: Stakeholder Alignment

Ensure stakeholders are aligned:

**Activities:**
- Review Business Vision Report
- Validate MVP scope
- Confirm requirements
- Address concerns

### Step 7: Risk Assessment

Identify and document risks:

**Risk Areas:**
- Technical risks
- Schedule risks
- Resource risks
- Scope risks

### Step 8: Generate Business Vision Report

The AI will automatically generate the Business Vision Report as part of the workflow. To ensure the report is generated:

**Automatic Generation:**
- The AI will create the Business Vision Report automatically after completing all vision activities
- The report will be saved to `aidlc-docs/inception/business-vision-report.md`

**If Report Not Generated:**
- Request report generation: "Please generate the Business Vision Report using the template at `report-templates/business-vision-report.md`"
- Reference the template: "Use the Business Vision Report template to create a complete report with all sections filled in"

**Report Generation Request Example:**
```
Please generate the Business Vision Report based on our vision phase work. Use the template at report-templates/business-vision-report.md and fill in all sections with:
- Business vision: [summarize your vision]
- MVP scope: [list in-scope and out-of-scope features]
- Requirements: [summarize key requirements]
- Stakeholders: [list stakeholders and approval status]
```

**Verify Report Generation:**
- Check that `aidlc-docs/inception/business-vision-report.md` exists
- Verify the report contains all required sections from the template
- Ensure no placeholder text remains
- Confirm the report is readable by non-technical stakeholders

### Step 9: Review and Approve Vision

Review the generated Business Vision Report and approve to proceed:

**Example Phase Boundary Input:**
```
Vision phase complete. Business vision documented, MVP scope approved by stakeholders. Ready to proceed to Units and User Stories phase.
```

## Deliverables

After completing this phase, you should have:

1. **Business Vision Report** (`aidlc-docs/inception/business-vision-report.md`)
   - Business vision documentation
   - Problem statement
   - Solution overview
   - Business objectives
   - Success criteria

2. **Requirements Document** (`aidlc-docs/inception/requirements/requirements.md`)
   - Functional requirements
   - Non-functional requirements
   - User scenarios
   - Constraints and assumptions

3. **MVP Scope Definition** (included in Business Vision Report)
   - In-scope features
   - Out-of-scope features
   - Acceptance criteria

4. **Risk Assessment** (included in Business Vision Report)
   - Identified risks
   - Mitigation strategies

## Report Validation

### Step 10: Validate Business Vision Report

Before proceeding to the next phase, validate the Business Vision Report:

**Access the Report:**
- Open `aidlc-docs/inception/business-vision-report.md` (or the location specified by the AI)
- Review the complete report

**Validation Checklist:**
- [ ] **Business Vision**: Problem statement, solution overview, and business objectives clearly defined
- [ ] **Target Users**: User types and their needs documented
- [ ] **Success Criteria**: Clear, measurable criteria for project success
- [ ] **MVP Scope**: In-scope and out-of-scope features clearly defined
- [ ] **Requirements Summary**: Functional and non-functional requirements documented
- [ ] **Stakeholder Alignment**: Stakeholders identified and approval status documented
- [ ] **Risks and Constraints**: Risks identified with mitigation strategies
- [ ] **Timeline and Milestones**: High-level timeline and key milestones documented
- [ ] **Human Tasks**: All required human tasks to complete the phase are listed

**What to Check:**
1. **Completeness**: All sections are filled in (no placeholder text)
2. **Clarity**: Non-technical stakeholders can understand the business vision
3. **Scope Boundaries**: MVP scope is clearly defined with no ambiguity
4. **Stakeholder Approval**: All key stakeholders have reviewed and approved
5. **Actionability**: Human tasks section has clear, actionable items

**Validation Questions:**
- Can a non-technical stakeholder read and understand the business vision?
- Is the MVP scope clear enough to prevent scope creep?
- Are all stakeholders aligned on the vision and scope?
- Are the success criteria measurable?

**If Issues Found:**
- Request changes from the AI: "Please update the Business Vision Report to clarify [specific item]"
- Review the report template: [Business Vision Report template](../report-templates/business-vision-report.md)
- Document any corrections in the audit trail

**Validation Complete When:**
- All checklist items are verified
- Report is complete and accurate
- Stakeholders have reviewed and approved the report
- Ready to proceed to Units and User Stories phase

## Example Phase Boundary Inputs

When you're ready to move to the next phase, use one of these inputs:

**Option 1 (Detailed):**
```
Vision phase complete. Business vision documented, MVP scope approved by stakeholders. Ready to proceed to Units and User Stories phase.
```

**Option 2 (Simple):**
```
Vision complete. Proceed to Units and User Stories phase.
```

**Option 3 (With Specifics):**
```
Vision phase complete. We've documented:
- Business vision: Task management system for team collaboration
- MVP scope: User auth, projects, tasks, basic reporting
- Approved by: Product Owner, Tech Lead, Stakeholders
Ready to proceed to Units and User Stories phase.
```

## Tips for Success

1. **Be Clear**: Provide clear, specific requirements
2. **Think MVP**: Focus on minimum viable functionality
3. **Involve Stakeholders**: Get stakeholder input and approval
4. **Document Everything**: Ensure all decisions are captured
5. **Validate Scope**: Use the Business Vision Report to validate scope

## Common Questions

**Q: What if requirements change?**
A: Document changes in the audit trail. You can update requirements, but be aware of impact on scope.

**Q: How detailed should requirements be?**
A: Detailed enough to understand what to build, but not so detailed that they constrain design.

**Q: What if stakeholders disagree?**
A: Use the Business Vision Report to facilitate discussion. Document all perspectives.

## Next Phase

After completing Vision, proceed to:
- **Phase 3: Units and User Stories** (see [03-units-and-stories.md](03-units-and-stories.md))
