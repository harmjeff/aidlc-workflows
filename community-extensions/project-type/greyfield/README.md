# Greyfield Extension

Use this extension when your project integrates with **external resources (APIs, databases, event streams) that you don't own or modify**.

---

## What Is Greyfield?

A greyfield project builds new application code against external resources whose contracts you must respect but cannot change. The AI needs to understand those resources before making design decisions.

**Greyfield examples:**
- A new service consuming an existing third-party or internal API
- A new application backed by a shared database you don't control
- A new integration layer between two existing external systems
- A new microservice publishing to or consuming from an existing event bus

**Not greyfield:**
- Modifying existing source code you own — use the [brownfield extension](../brownfield/README.md)
- A new project with no external resource constraints — use greenfield (the default)

---

## Supplying External Resource Data

Before starting your AI-DLC session, place external resource documentation in your project workspace:

```
<project-root>/
└── aidlc-docs/
    └── external-resources/
        ├── api-specs/        <- OpenAPI/Swagger specs, Postman collections, API docs
        ├── db-schemas/       <- Database schemas, ERDs, migration files
        ├── event-schemas/    <- Event/message schemas (Avro, Protobuf, JSON Schema)
        └── docs/             <- Any other reference documentation
```

Any format is accepted: `.yaml`, `.json`, `.md`, `.pdf`, plain text. If you don't have formal specs, plain text descriptions or example request/response payloads work — place them in `docs/`.

The AI reads these files during the **External Resource Analysis** stage before generating any design or code.

---

## How It Changes the Workflow

Enabling greyfield adds:

1. **External Resource Analysis stage** — documents external APIs, databases, and schemas before Requirements Analysis, producing the same artifact set as Reverse Engineering but focused on resources you integrate with rather than code you own
2. **Requirements Analysis addendum** — treats external resource contracts as hard design constraints

---

## Installing This Extension

Copy `greyfield.md` and `external-resource-analysis.md` into your project's extensions directory.

**Kiro:**
```bash
mkdir -p .kiro/aws-aidlc-rule-details/extensions/project-type/greyfield
cp greyfield.md external-resource-analysis.md .kiro/aws-aidlc-rule-details/extensions/project-type/greyfield/
```

**Amazon Q Developer:**
```bash
mkdir -p .amazonq/aws-aidlc-rule-details/extensions/project-type/greyfield
cp greyfield.md external-resource-analysis.md .amazonq/aws-aidlc-rule-details/extensions/project-type/greyfield/
```

**Cursor / Cline / Claude Code / GitHub Copilot:**
```bash
mkdir -p .aidlc-rule-details/extensions/project-type/greyfield
cp greyfield.md external-resource-analysis.md .aidlc-rule-details/extensions/project-type/greyfield/
```

Then place your external resource documentation in `aidlc-docs/external-resources/` and start a new AI-DLC session, selecting **Greyfield** when prompted for your project type during Workspace Detection.
