# Brownfield Extension

Use this extension when your project involves modifying an **existing codebase**.

---

## What Is Brownfield?

A brownfield project has existing source code that will be modified as part of this work. AI-DLC needs to understand the existing system before making changes.

**Brownfield examples:**
- Adding a feature to an existing application
- Refactoring or migrating an existing system
- Fixing bugs in a production codebase
- Upgrading a framework or dependency across an existing codebase

**Not brownfield:**
- A new project with no existing code — use greenfield (the default)
- Integrating with external APIs or databases you don't own or modify — use the [greyfield extension](../greyfield/README.md)

---

## How It Changes the Workflow

Enabling brownfield adds:

1. **Reverse Engineering stage** — analyzes your existing codebase before Requirements Analysis, producing architecture docs, API docs, component inventory, and more
2. **Workflow Planning addendum** — adds transformation scope analysis and multi-package coordination
3. **Code Generation addendum** — enforces file-modification-in-place rules (never create duplicate files like `ClassName_modified.java`)

---

## Installing This Extension

Copy `brownfield.md` and `reverse-engineering.md` into your project's extensions directory.

**Kiro:**
```bash
mkdir -p .kiro/aws-aidlc-rule-details/extensions/project-type/brownfield
cp brownfield.md reverse-engineering.md .kiro/aws-aidlc-rule-details/extensions/project-type/brownfield/
```

**Amazon Q Developer:**
```bash
mkdir -p .amazonq/aws-aidlc-rule-details/extensions/project-type/brownfield
cp brownfield.md reverse-engineering.md .amazonq/aws-aidlc-rule-details/extensions/project-type/brownfield/
```

**Cursor / Cline / Claude Code / GitHub Copilot:**
```bash
mkdir -p .aidlc-rule-details/extensions/project-type/brownfield
cp brownfield.md reverse-engineering.md .aidlc-rule-details/extensions/project-type/brownfield/
```

Then start a new AI-DLC session and select **Brownfield** when prompted for your project type during Workspace Detection.
