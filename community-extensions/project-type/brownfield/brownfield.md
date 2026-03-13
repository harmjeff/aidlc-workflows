# Brownfield Extension Rules

## Project Type Registration

This section is read by Workspace Detection to dynamically build the project type question.

- **Option Label**: Brownfield
- **Description**: Modifying an existing codebase
- **Pre-Requirements Stage**: Reverse Engineering — load `extensions/project-type/brownfield/reverse-engineering.md`
- **Workspace Signal**: Existing source code files detected in workspace root

## Opt-In Prompt

> **Timing**: Presented at **Workspace Detection** (not Requirements Analysis) as part of the project type selection question.

The following is how this extension's option appears to the user:

```markdown
## Question 1
What best describes this project?

...
B) Brownfield — modifying an existing codebase

[Answer]:
```

When selected, this extension's rules are loaded immediately and the **Reverse Engineering** stage runs before Requirements Analysis.

---

## Overview

A brownfield project modifies existing source code. This extension adds Reverse Engineering before Requirements Analysis so the AI understands the existing system, and injects brownfield-specific considerations into Workflow Planning and Code Generation.

---

## Added Stages

### Reverse Engineering (runs between Workspace Detection and Requirements Analysis)

Load and execute all steps from `extensions/project-type/brownfield/reverse-engineering.md`.

This stage analyzes the existing codebase and generates artifacts in `aidlc-docs/inception/reverse-engineering/`:
- `business-overview.md`
- `architecture.md`
- `code-structure.md`
- `api-documentation.md`
- `component-inventory.md`
- `technology-stack.md`
- `dependencies.md`
- `code-quality-assessment.md`

**Skip if**: Prior reverse-engineering artifacts exist and the user confirms they are current.

---

## Stage Addendums

### Workflow Planning Addendum

When executing Workflow Planning, also apply the following after loading prior context (Step 1):

#### Transformation Scope Analysis

Determine whether the change is a single component modification or a broader transformation:
- Single component change vs. architectural transformation
- Application-layer only vs. infrastructure changes included
- Deployment model changes (e.g., Lambda to Container, EC2 to Serverless)

For transformations, identify all related components requiring changes:
- Infrastructure packages (CDK stacks, Terraform modules)
- Shared packages (models, utilities, client libraries)
- Dependent services that call the component being changed
- Supporting concerns (monitoring, logging, CI/CD pipelines)

#### Component Relationship Mapping

For each component affected, document in the execution plan:

```markdown
## Component Relationships
- **Primary Component**: [Package being changed]
- **Infrastructure Components**: [CDK/Terraform packages]
- **Shared Components**: [Models, utilities, clients]
- **Dependent Components**: [Services that call this component]
- **Supporting Components**: [Monitoring, logging, deployment]
```

For each related component include:
- **Change Type**: Major, Minor, or Configuration-only
- **Change Reason**: Direct dependency, deployment model, networking, etc.
- **Change Priority**: Critical, Important, or Optional

#### Multi-Package Coordination

When multiple packages require changes:

1. Analyze build-system dependencies and API contracts between packages
2. Determine update strategy — sequential, parallel, or hybrid — based on dependencies
3. Document in the execution plan:

```markdown
## Package Update Strategy
- **Update Approach**: [Sequential / Parallel / Hybrid]
- **Critical Path**: [Packages that must be updated first]
- **Coordination Points**: [Shared APIs, infrastructure, data contracts]
- **Testing Checkpoints**: [When to validate integration between packages]
```

4. List the **Package Change Sequence** in the execution plan with each package's update order and dependency rationale.

---

### Code Generation Addendum

When executing Code Generation, also apply the following in Step 2 (Create Plan) and Step 11 (Execute Step):

#### File Modification Rules

- **Check before creating**: Verify whether the target file already exists before generating
- **Modify in-place**: If the file exists, modify it directly — never create copies named `ClassName_modified.java`, `service-new.ts`, `handler_updated.py`, etc.
- **Create only when absent**: If the file does not exist, create it at the correct path
- **Verify after each step**: Confirm no duplicate files were created alongside the original
- **Reflect in the plan**: For each step in the code generation plan, explicitly note whether it will **modify existing** or **create new**
