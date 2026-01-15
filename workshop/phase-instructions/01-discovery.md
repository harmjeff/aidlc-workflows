# Phase 1: Discovery - Instructions

## Overview

The Discovery phase establishes the foundation for your project by defining the development environment, coding standards, and Agile process. This phase ensures all team members understand how to work together and what standards to follow.

## Objectives

1. Establish development environment and tools
2. Define coding standards and conventions
3. Establish Agile process and workflow
4. Document team structure and roles
5. Set up project structure and conventions

## Duration

- **2-Day Workshop**: 90 minutes
- **5-Day Workshop**: 2 hours

## Prerequisites

- AI-DLC installation complete (see `00-installation-guide.md`)
- Project workspace created
- Team members identified

## Step-by-Step Instructions

### Step 1: Start AI-DLC Workflow

Begin by activating the AI-DLC workflow:

**Example Input:**
```
Using AI-DLC, I want to establish the development environment, coding standards, and Agile process for our project.
```

The AI will automatically:
- Detect workspace state
- Begin workspace detection phase
- Guide you through the discovery process

### Step 2: Workspace Detection

The AI will analyze your workspace and determine:
- Project type (greenfield/brownfield)
- Existing code structure
- Technology stack (if brownfield)

**What to Provide:**
- Information about existing codebase (if any)
- Project goals and context
- Team preferences

### Step 3: Environment Setup

Work with the AI to document:

**Development Environment:**
- Operating systems and versions
- Development tools (IDE, editors)
- Version control system (Git, SVN, etc.)
- Build tools (Maven, Gradle, npm, etc.)
- Runtime environments

**Example Questions AI May Ask:**
- What programming languages will you use?
- What build system do you prefer?
- What IDE or editor will the team use?

**Example Answers:**
```
[Answer]: A) Java with Maven for build system
[Answer]: B) VS Code as the primary IDE
[Answer]: C) Git for version control
```

### Step 4: Coding Standards Definition

Define coding standards for your project:

**Areas to Cover:**
- Code style and formatting
- Naming conventions
- Documentation requirements
- Code review process
- Testing standards

**Example Questions AI May Ask:**
- What code style guide should be followed?
- What naming conventions should be used?
- What level of code documentation is required?

**Example Answers:**
```
[Answer]: A) Google Java Style Guide
[Answer]: B) camelCase for variables, PascalCase for classes
[Answer]: C) Javadoc required for all public methods
```

### Step 5: Agile Process Establishment

Define your Agile process:

**Areas to Cover:**
- Sprint duration and structure
- Story point estimation
- Definition of Done
- Retrospective process
- Daily standup format

**Example Questions AI May Ask:**
- What is your sprint duration?
- How do you estimate story points?
- What is your Definition of Done?

**Example Answers:**
```
[Answer]: A) 2-week sprints
[Answer]: B) Fibonacci sequence (1, 2, 3, 5, 8, 13)
[Answer]: C) Code reviewed, tests passing, documentation updated
```

### Step 6: Team Structure

Document team structure and roles:

**Information to Provide:**
- Team members and roles
- Responsibilities
- Communication channels
- Decision-making process

### Step 7: Generate Discovery Report

The AI will automatically generate the Discovery Report as part of the workflow. To ensure the report is generated:

**Automatic Generation:**
- The AI will create the Discovery Report automatically after completing all discovery activities
- The report will be saved to `aidlc-docs/inception/discovery-report.md`

**If Report Not Generated:**
- Request report generation: "Please generate the Discovery Report using the template at `report-templates/discovery-report.md`"
- Reference the template: "Use the Discovery Report template to create a complete report with all sections filled in"

**Report Generation Request Example:**
```
Please generate the Discovery Report based on our discovery phase work. Use the template at report-templates/discovery-report.md and fill in all sections with the information we've discussed:
- Environment setup: [summarize your environment]
- Coding standards: [summarize your standards]
- Agile process: [summarize your process]
- Team structure: [summarize your team]
```

**Verify Report Generation:**
- Check that `aidlc-docs/inception/discovery-report.md` exists
- Verify the report contains all required sections from the template
- Ensure no placeholder text remains (like `[Project Name]` or `[Date]`)

### Step 8: Review and Approve Discovery

Review the generated Discovery Report and approve to proceed:

**Example Phase Boundary Input:**
```
Discovery phase complete. Environment established, coding standards defined, Agile process documented. Ready to proceed to Vision phase.
```

## Deliverables

After completing this phase, you should have:

1. **Discovery Report** (`aidlc-docs/inception/discovery-report.md`)
   - Environment setup documentation
   - Coding standards document
   - Agile process definition
   - Team structure documentation

2. **Workspace State** (`aidlc-docs/aidlc-state.md`)
   - Project type identified
   - Workspace structure documented

3. **Audit Trail** (`aidlc-docs/audit.md`)
   - All decisions and discussions logged

## Report Validation

### Step 9: Validate Discovery Report

Before proceeding to the next phase, validate the Discovery Report:

**Access the Report:**
- Open `aidlc-docs/inception/discovery-report.md` (or the location specified by the AI)
- Review the complete report

**Validation Checklist:**
- [ ] **Environment Setup**: All development tools, versions, and configurations documented
- [ ] **Coding Standards**: Code style guide, naming conventions, and documentation standards defined
- [ ] **Agile Process**: Sprint structure, estimation method, Definition of Done documented
- [ ] **Team Structure**: Team members, roles, and communication channels documented
- [ ] **Project Structure**: Directory structure and configuration management documented
- [ ] **Quality Assurance**: Testing strategy and code quality tools documented
- [ ] **Dependencies**: Core dependencies and library versions listed
- [ ] **Human Tasks**: All required human tasks to complete the phase are listed

**What to Check:**
1. **Completeness**: All sections are filled in (no placeholder text like `[Project Name]` or `[Date]`)
2. **Accuracy**: Information matches your team's actual setup and decisions
3. **Actionability**: Human tasks section has clear, actionable items
4. **Team Alignment**: All team members can understand and follow the documented standards

**If Issues Found:**
- Request changes from the AI: "Please update the Discovery Report to include [specific item]"
- Review the report template: [Discovery Report template](../report-templates/discovery-report.md)
- Document any corrections in the audit trail

**Validation Complete When:**
- All checklist items are verified
- Report is complete and accurate
- Team has reviewed and approved the report
- Ready to proceed to Vision phase

## Example Phase Boundary Inputs

When you're ready to move to the next phase, use one of these inputs:

**Option 1 (Detailed):**
```
Discovery phase complete. Environment established, coding standards defined, Agile process documented. Ready to proceed to Vision phase.
```

**Option 2 (Simple):**
```
Discovery complete. Proceed to Vision phase.
```

**Option 3 (With Specifics):**
```
Discovery phase complete. We've established:
- Java 17 with Maven build system
- Google Java Style Guide
- 2-week sprints with Fibonacci estimation
Ready to proceed to Vision phase.
```

## Tips for Success

1. **Be Specific**: Provide detailed answers to questions
2. **Involve Team**: Get team input on standards and processes
3. **Document Decisions**: Ensure all decisions are captured
4. **Review Thoroughly**: Review the Discovery Report before proceeding
5. **Use Examples**: Reference existing projects or standards when possible

## Common Questions

**Q: What if we don't know all the answers?**
A: Provide your best answers. You can refine later. The AI will ask follow-up questions if needed.

**Q: Can we skip some areas?**
A: The AI will adapt based on your project needs. Some areas may be optional.

**Q: What if we want to change something later?**
A: You can always update the Discovery Report. Document changes in the audit trail.

## Next Phase

After completing Discovery, proceed to:
- **Phase 2: Vision** (see [02-vision.md](02-vision.md))
