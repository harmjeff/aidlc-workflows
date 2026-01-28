# Available Extensions

This directory contains optional rules that can be enabled for specific project needs. Extensions allow you to add domain-specific guidelines, compliance requirements, or process modifications that integrate seamlessly with the core AI-DLC workflow.

---

## How Extensions Work

1. **Discovery**: During Workflow Planning, AI-DLC scans this directory for extensions
2. **Trigger Matching**: Extensions are suggested based on project characteristics (type, keywords, files)
3. **User Selection**: Users enable/disable extensions as needed
4. **Application**: Enabled extensions add content to relevant stages automatically

---

## Enabling Extensions

### Option 1: During Workflow Planning (Recommended)
Extensions are offered during the Workflow Planning stage based on trigger matching.

### Option 2: Manual Pre-enablement
Create `aidlc-docs/enabled-extensions.md` in your project:

```markdown
# Enabled Extensions

The following extensions are enabled for this project:

- security-owasp
- compliance-hipaa
- process-tdd

## Selection Rationale

| Extension | Reason |
|-----------|--------|
| security-owasp | Required for web applications per security policy |
| compliance-hipaa | Healthcare data handling requirements |
| process-tdd | Team development standard |
```

---

## Creating New Extensions

Each extension is a folder containing:

```
extension-name/
├── rule-manifest.yaml    # REQUIRED: Metadata and configuration
├── overview.md           # RECOMMENDED: Human-readable description
├── requirements.md       # Content for requirements-analysis stage
├── design.md             # Content for design stages
├── code-guidelines.md    # Content for code-generation stage
└── testing.md            # Content for build-and-test stage
```

### Minimal rule-manifest.yaml

```yaml
name: "my-extension"
version: "1.0.0"
displayName: "My Extension"
description: "Brief description of what this extension does"
category: "quality"  # security | compliance | process | quality | architecture

triggers:
  always_available: true

applies_to:
  construction:
    - stage: "code-generation"
      file: "code-guidelines.md"
      action: "append"

priority: 100
tags: ["custom"]
```

See `EXTENSION-AUTHORING-GUIDE.md` in the repository root for complete documentation on creating extensions.

---

## Extension Application Rules

- Extensions are applied **AFTER** core stage logic completes
- Extensions **ADD** to existing guidance (never replace core functionality)
- Multiple extensions can apply to the same stage
- `priority` in manifest determines application order (lower = earlier)
- Extensions with conflicts specified in `conflicts_with` cannot both be enabled

---

## Available Extensions

### security-baseline
**Security Baseline - Linting & Static Analysis** (v1.0.0)

Establishes baseline code security rules for linting, static analysis, and security scanning across all projects.

| Property | Value |
|----------|-------|
| Category | `security` |
| Priority | 50 |
| Stages Affected | NFR Requirements, Functional Design, Code Generation, Build and Test |
| Auto-suggested | Yes (for web, api, microservice, library, cli, backend projects) |

**Provides:**
- Language-specific linter configurations (ESLint, Bandit, SpotBugs, gosec)
- Secure design patterns and anti-patterns
- Input validation and parameterized query guidelines
- SAST and dependency scanning requirements
- CI/CD security gate recommendations

---

### Adding More Extensions

To add additional extensions:
1. Copy extension folders from the AI-DLC repository (`aidlc-rules/extensions/`)
2. Or create custom extensions following the authoring guide
3. Extensions will be automatically discovered during Workflow Planning

---

*For more information, see:*
- `EXTENSION-AUTHORING-GUIDE.md` - Complete guide to creating extensions
- `EXTENSIBLE-RULES-PLAN.md` - Implementation plan and architecture