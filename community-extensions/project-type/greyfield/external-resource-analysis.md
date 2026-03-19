# External Resource Analysis

**Purpose**: Analyze external resources (APIs, databases, event streams, services) the project integrates with and generate documentation artifacts that inform Requirements Analysis and design.

**Execute when**: Greyfield project selected at Workspace Detection.

**Skip when**: Greenfield or brownfield project type.

**Data source**: Files placed by the user in `aidlc-docs/external-resources/` before starting the session.

**If no files found**: Ask the user to provide external resource documentation (API specs, DB schemas, etc.) before proceeding. Do not attempt to infer external resource details without source material.

---

## Step 1: Discover External Resources

Scan `aidlc-docs/external-resources/` and its subdirectories:
- `api-specs/` — OpenAPI/Swagger files, Postman collections, API documentation
- `db-schemas/` — Database schemas, ERDs, migration files, data dictionaries
- `event-schemas/` — Event and message schemas (Avro, Protobuf, JSON Schema, etc.)
- `docs/` — Any other reference documentation (PDFs, markdown, plain text)

Record findings:
```markdown
## External Resource Discovery
- **API Specs Found**: [List files]
- **Database Schemas Found**: [List files]
- **Event Schemas Found**: [List files]
- **Other Docs Found**: [List files]
- **Total Resources Identified**: [Number]
```

---

## Step 2: Generate Business Overview

Create `aidlc-docs/inception/external-resources/business-overview.md`:

```markdown
# External Resources Business Overview

## Business Context Diagram
[Mermaid diagram showing the project and its relationships to external resources]

## Business Description
- **Integration Purpose**: [Why this project integrates with these external resources]
- **Business Transactions**: [List of business transactions the project will perform using external resources]
- **Business Dictionary**: [Key domain terms from the external resources and their meanings]

## Resource-Level Business Descriptions
### [Resource Name]
- **Purpose**: [What this resource provides from a business perspective]
- **Role in Integration**: [How the project uses this resource]
```

---

## Step 3: Generate Architecture Documentation

Create `aidlc-docs/inception/external-resources/architecture.md`:

```markdown
# External Resources Architecture

## Overview
[High-level description of external resources and how they relate to the project being built]

## Architecture Diagram
[Mermaid diagram showing the project (as a placeholder), external APIs, databases, event streams, and data flows]

## Resource Descriptions
### [Resource Name]
- **Type**: [REST API / GraphQL API / Database / Event Stream / etc.]
- **Purpose**: [What it does]
- **Owner**: [Team or organization that owns it]
- **Access Method**: [How the project will connect — REST, SDK, JDBC, etc.]
- **Authentication**: [Auth mechanism — API key, OAuth, IAM, etc.]

## Data Flow
[Mermaid sequence diagram showing key integration workflows between the project and external resources]

## Integration Constraints
- **Rate Limits**: [Known rate or quota limits per resource]
- **SLA / Availability**: [Uptime or reliability characteristics]
- **Data Residency**: [Any data locality or compliance requirements]
```

---

## Step 4: Generate API Documentation

Create `aidlc-docs/inception/external-resources/api-documentation.md`:

```markdown
# External API Documentation

## REST / GraphQL APIs
### [API Name]
- **Base URL**: [Endpoint base]
- **Authentication**: [Method and details]
- **Key Endpoints**:
  | Method | Path | Purpose |
  |--------|------|---------|
  | [GET]  | [/path] | [Description] |
- **Request Format**: [JSON / XML / etc., notable headers or parameters]
- **Response Format**: [Structure, key fields]
- **Error Responses**: [Common error codes and meanings]
- **Rate Limits**: [Limits and behavior when exceeded]

## Databases
### [Database Name]
- **Type**: [PostgreSQL / DynamoDB / etc.]
- **Access**: [Read-only / Read-write, connection method]
- **Key Tables / Collections**: [List with purpose]
- **Schema Summary**: [Key fields and relationships]
- **Constraints**: [Fields or data the project must not modify]

## Event Streams
### [Stream / Topic Name]
- **Platform**: [Kafka / SQS / EventBridge / etc.]
- **Direction**: [Consume / Produce / Both]
- **Schema**: [Event structure and key fields]
- **Ordering / Delivery**: [At-least-once, exactly-once, etc.]
```

---

## Step 5: Generate Integration Structure Documentation

Create `aidlc-docs/inception/external-resources/integration-structure.md`:

```markdown
# Integration Structure

## Integration Patterns
### [Resource Name]
- **Pattern**: [Request-Response / Event-Driven / Polling / Webhook / etc.]
- **SDK / Library**: [Client library or SDK available, if any]
- **Error Handling**: [Retry strategy, circuit breaker, fallback]
- **Data Mapping**: [How external data maps to internal domain models]

## Existing Files / Clients (if any)
[If the user has provided any existing client code or generated SDK files, list them here as candidates for use during code generation]

## Design Patterns Implied by External Resources
[Note any design patterns the external resource constraints suggest — e.g., adapter pattern for an awkward API, repository pattern for DB access, etc.]
```

---

## Step 6: Generate Resource Inventory

Create `aidlc-docs/inception/external-resources/resource-inventory.md`:

```markdown
# External Resource Inventory

## APIs
- [API Name] — [Type] — [Purpose]

## Databases
- [DB Name] — [Type] — [Access level: read-only / read-write]

## Event Streams
- [Stream Name] — [Platform] — [Direction: consume / produce]

## Other Resources
- [Resource Name] — [Type] — [Purpose]

## Total Count
- **Total External Resources**: [Number]
- **APIs**: [Number]
- **Databases**: [Number]
- **Event Streams**: [Number]
- **Other**: [Number]
```

---

## Step 7: Generate Technology Stack Documentation

Create `aidlc-docs/inception/external-resources/technology-stack.md`:

```markdown
# External Technology Stack

## API Technologies
- [Technology] — [Version if known] — [Used by which resource]

## Database Technologies
- [Technology] — [Version if known] — [Resource name]

## Messaging / Streaming Technologies
- [Technology] — [Version if known] — [Resource name]

## Authentication Technologies
- [Technology] — [e.g., OAuth 2.0, API Keys, AWS IAM] — [Resources using it]

## Client Libraries Available
- [Library] — [Version] — [Language] — [Resource it targets]
```

---

## Step 8: Generate Dependencies Documentation

Create `aidlc-docs/inception/external-resources/dependencies.md`:

```markdown
# External Resource Dependencies

## Dependency Diagram
[Mermaid diagram showing relationships between external resources — e.g., if one API calls another, or if a database is shared with another known system]

## Resource Dependencies
### [Resource A] depends on [Resource B]
- **Reason**: [Why this dependency exists]
- **Impact**: [How this affects the project's integration approach]

## Project Dependency on External Resources
### [Resource Name]
- **Criticality**: [Critical / Important / Optional]
- **Fallback**: [What happens if this resource is unavailable]
- **Contract Stability**: [Stable / Versioned / Unstable — based on provided documentation]
```

---

## Step 9: Update State Tracking

Update `aidlc-docs/aidlc-state.md`:

```markdown
## External Resource Analysis Status
- [x] External Resource Analysis - Completed on [timestamp]
- **Artifacts Location**: aidlc-docs/inception/external-resources/
- **Resources Analyzed**: [Number and types]
```

---

## Step 10: Present Completion Message to User

```markdown
# External Resource Analysis Complete

[AI-generated summary of external resources discovered and documented, in bullet points]

> **REVIEW REQUIRED:**
> Please examine the external resource analysis artifacts at: `aidlc-docs/inception/external-resources/`

> **WHAT'S NEXT?**
>
> **You may:**
>
> - **Request Changes** — Ask for modifications to the analysis if required
> - **Approve & Continue** — Approve analysis and proceed to **Requirements Analysis**
```

---

## Step 11: Wait for User Approval

- **MANDATORY**: Do not proceed until user explicitly approves
- **MANDATORY**: Log user's response in audit.md with complete raw input
