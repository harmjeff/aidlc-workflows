# Greyfield Extension Rules

## Project Type Registration

This section is read by Workspace Detection to dynamically build the project type question.

- **Option Label**: Greyfield
- **Description**: New code integrating with external resources (APIs, databases, event streams) you don't own or modify
- **Pre-Requirements Stage**: External Resource Analysis — load `extensions/project-type/greyfield/external-resource-analysis.md`
- **Workspace Signal**: Files present in `aidlc-docs/external-resources/`

## Opt-In Prompt

> **Timing**: Presented at **Workspace Detection** (not Requirements Analysis) as part of the project type selection question.

The following is how this extension's option appears to the user:

```markdown
## Question 1
What best describes this project?

...
C) Greyfield — new code integrating with external resources (APIs, databases, event streams) you don't own or modify

[Answer]:
```

When selected, this extension's rules are loaded immediately and the **External Resource Analysis** stage runs before Requirements Analysis.

---

## Overview

A greyfield project builds new application code that integrates with external resources (APIs, databases, event streams, services) it does not own or modify. This extension adds External Resource Analysis before Requirements Analysis so the AI understands the external contracts and constraints, and injects those constraints into Requirements Analysis.

---

## User Setup

Before starting an AI-DLC session, place external resource documentation in:

```
aidlc-docs/external-resources/
├── api-specs/        <- OpenAPI/Swagger specs, Postman collections, API documentation
├── db-schemas/       <- Database schemas, ERDs, migration files
├── event-schemas/    <- Event/message schemas (Avro, Protobuf, JSON Schema)
└── docs/             <- Any other reference documentation
```

Any format is accepted. If formal specs aren't available, plain text descriptions or example payloads work.

If no files are found in `aidlc-docs/external-resources/` at Workspace Detection, ask the user to provide external resource documentation before proceeding.

---

## Added Stages

### External Resource Analysis (runs between Workspace Detection and Requirements Analysis)

Load and execute all steps from `extensions/project-type/greyfield/external-resource-analysis.md`.

This stage reads the files in `aidlc-docs/external-resources/` and generates artifacts in `aidlc-docs/inception/external-resources/`:
- `business-overview.md`
- `architecture.md`
- `api-documentation.md`
- `integration-structure.md`
- `resource-inventory.md`
- `technology-stack.md`
- `dependencies.md`

**Skip if**: Prior external resource analysis artifacts exist and the user confirms the external resources have not changed.

---

## Stage Addendums

### Requirements Analysis Addendum

When executing Requirements Analysis, also apply the following after loading prior context (Step 1):

- Load all external resource analysis artifacts from `aidlc-docs/inception/external-resources/`
- Treat external resource contracts as hard design constraints — requirements must not assume changes to external APIs, schemas, data models, or service behaviors
- If any gathered requirement conflicts with an external resource constraint, surface it as an issue to resolve before proceeding
- Reference the relevant external resource artifact in the requirements document when a requirement depends on an external contract
