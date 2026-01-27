# AI-DLC Extension Authoring Guide

## Introduction

This guide explains how to create custom extensions for the AI-DLC (AI-Driven Development Life Cycle) workflow. Extensions allow you to add domain-specific rules, guidelines, and process modifications that integrate seamlessly with the core workflow.

**Universal Design**: Extensions work identically across ALL supported AI-DLC platforms:
- Amazon Q Developer IDE Plugin
- Kiro CLI
- Cursor IDE
- Cline
- Claude Code
- GitHub Copilot

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Cross-Platform Architecture](#cross-platform-architecture)
3. [Creating Your First Extension](#creating-your-first-extension)
4. [Rule Manifest Reference](#rule-manifest-reference)
5. [Content Files](#content-files)
6. [Best Practices](#best-practices)
7. [Testing Extensions](#testing-extensions)
8. [Deployment (All Platforms)](#deployment-all-platforms)
9. [Examples](#examples)
10. [Troubleshooting](#troubleshooting)

---

## Cross-Platform Architecture

### Why Extensions Work Everywhere

AI-DLC uses a **two-tier architecture** that enables universal extensions:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    AI-DLC Two-Tier Architecture                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  TIER 1: Platform-Specific Rule Location (varies by tool)               │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ • Amazon Q:    .amazonq/rules/aws-aidlc-rules/core-workflow.md  │    │
│  │ • Kiro CLI:    .kiro/steering/aws-aidlc-rules/core-workflow.md  │    │
│  │ • Cursor:      .cursor/rules/ai-dlc-workflow.mdc                │    │
│  │ • Cline:       .clinerules/core-workflow.md                     │    │
│  │ • Claude Code: CLAUDE.md                                        │    │
│  │ • Copilot:     .copilot/instructions.md                         │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                              │                                          │
│                              │ References                               │
│                              ▼                                          │
│  TIER 2: Universal Rule Details Location (same for ALL platforms)       │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ .aidlc-rule-details/                                            │    │
│  │  ├── common/           (shared utilities)                       │    │
│  │  ├── inception/        (inception stage details)                │    │
│  │  ├── construction/     (construction stage details)             │    │
│  │  ├── operations/       (operations stage details)               │    │
│  │  │                                                              │    │
│  │  └── extensions/       ← UNIVERSAL EXTENSION LOCATION           │    │
│  │       ├── security-owasp/                                       │    │
│  │       ├── compliance-hipaa/                                     │    │
│  │       └── process-tdd/                                          │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Key Insight**: The `core-workflow.md` file tells the AI to load detailed rules from `.aidlc-rule-details/`. Since ALL platforms use this same location for rule details, extensions placed in `.aidlc-rule-details/extensions/` work automatically on ALL platforms.

### Universal Location

The `core-workflow.md` uses a single universal location:

```markdown
## MANDATORY: Rule Details Loading
**CRITICAL**: When performing any phase, you MUST read and use relevant content from rule detail files in:
- `.aidlc-rule-details/` (Universal location for ALL platforms)
```

Extensions leverage this same universal location, making them automatically work on ALL platforms without any platform-specific configuration.

### Supported Platforms

| Platform | Core Workflow Location | Rule Details Location | Extension Location |
|----------|----------------------|----------------------|-------------------|
| Amazon Q Developer | `.amazonq/rules/aws-aidlc-rules/` | `.aidlc-rule-details/` | `.aidlc-rule-details/extensions/` |
| Kiro CLI | `.kiro/steering/aws-aidlc-rules/` | `.aidlc-rule-details/` | `.aidlc-rule-details/extensions/` |
| Cursor IDE | `.cursor/rules/` | `.aidlc-rule-details/` | `.aidlc-rule-details/extensions/` |
| Cline | `.clinerules/` | `.aidlc-rule-details/` | `.aidlc-rule-details/extensions/` |
| Claude Code | `CLAUDE.md` or `.claude/` | `.aidlc-rule-details/` | `.aidlc-rule-details/extensions/` |
| GitHub Copilot | `.copilot/` or `COPILOT.md` | `.aidlc-rule-details/` | `.aidlc-rule-details/extensions/` |

---

## Quick Start

### 5-Minute Extension

1. **Create folder**: `aidlc-rules/extensions/my-extension/`
2. **Create manifest**: `rule-manifest.yaml`
3. **Add content files**: One `.md` file per stage you want to extend
4. **Test**: Run AI-DLC and enable your extension during Workflow Planning

```bash
# Create extension structure
mkdir -p aidlc-rules/extensions/my-extension
cd aidlc-rules/extensions/my-extension

# Create minimal manifest
cat > rule-manifest.yaml << 'EOF'
name: "my-extension"
version: "1.0.0"
displayName: "My Custom Extension"
description: "Adds custom guidelines to the development process"
category: "quality"
triggers:
  always_available: true
applies_to:
  construction:
    - stage: "code-generation"
      file: "code-guidelines.md"
      action: "append"
priority: 100
tags: ["custom"]
EOF

# Create content file
cat > code-guidelines.md << 'EOF'
## My Custom Guidelines

When generating code, also consider:
- [ ] Custom guideline 1
- [ ] Custom guideline 2
- [ ] Custom guideline 3
EOF
```

---

## Extension Architecture

### How Extensions Work

```
┌─────────────────────────────────────────────────────────────────┐
│                     AI-DLC Core Workflow                        │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ Workflow Planning Stage                                   │  │
│  │  1. Load core rules                                       │  │
│  │  2. Scan extensions/ directory                            │  │
│  │  3. Read rule-manifest.yaml for each extension            │  │
│  │  4. Check triggers against project context                │  │
│  │  5. Present suggested extensions to user                  │  │
│  │  6. Save enabled extensions to enabled-extensions.md      │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                  │
│                              ▼                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ Each Stage (Requirements, Design, Code, etc.)             │  │
│  │  1. Execute core stage logic                              │  │
│  │  2. Check enabled extensions for applies_to this stage    │  │
│  │  3. Load extension content files                          │  │
│  │  4. Apply content (append/prepend/inject-section)         │  │
│  │  5. Continue with extended guidance                       │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Extension Application Order

When multiple extensions apply to the same stage:

1. Extensions sorted by `priority` (lower number = earlier)
2. Extensions with same priority sorted alphabetically by `name`
3. All extension content appended/applied in order
4. Core content always comes first

### Extension Scope

Extensions can affect any combination of AI-DLC stages:

| Phase | Available Stages |
|-------|------------------|
| **Inception** | `workspace-detection`, `reverse-engineering`, `requirements-analysis`, `user-stories`, `workflow-planning`, `application-design`, `units-generation` |
| **Construction** | `functional-design`, `nfr-requirements`, `nfr-design`, `infrastructure-design`, `code-generation`, `build-and-test` |
| **Operations** | `operations` (placeholder) |

---

## Creating Your First Extension

### Step 1: Plan Your Extension

Before creating files, answer these questions:

1. **What problem does this extension solve?**
   - Security vulnerabilities? Compliance requirements? Process improvement?

2. **Which stages need modification?**
   - Requirements? Design? Code generation? Testing?

3. **Who will use this extension?**
   - All projects? Specific project types? Teams with specific needs?

4. **How should it be triggered?**
   - Always available? Suggested for certain keywords? Required for certain project types?

### Step 2: Create Directory Structure

```
aidlc-rules/extensions/your-extension-name/
├── rule-manifest.yaml      # REQUIRED: Metadata and configuration
├── overview.md             # RECOMMENDED: Human-readable description
├── requirements.md         # Content for requirements-analysis stage
├── design.md               # Content for design stages
├── code-guidelines.md      # Content for code-generation stage
├── testing.md              # Content for build-and-test stage
└── questions.md            # Additional questions to ask users
```

### Step 3: Create the Manifest

```yaml
# rule-manifest.yaml
name: "your-extension-name"           # Unique identifier (lowercase, hyphens)
version: "1.0.0"                      # Semantic versioning
displayName: "Your Extension Name"    # Human-readable name
description: "Brief description of what this extension does"
author: "Your Name or Team"
category: "security"                  # security | compliance | process | quality | architecture

triggers:
  suggest_when:
    - project_type: ["web", "api"]
    - has_requirements_keyword: ["keyword1", "keyword2"]
  always_available: true

applies_to:
  inception:
    - stage: "requirements-analysis"
      file: "requirements.md"
      action: "append"
  construction:
    - stage: "code-generation"
      file: "code-guidelines.md"
      action: "append"
    - stage: "build-and-test"
      file: "testing.md"
      action: "append"

priority: 100
conflicts_with: []
depends_on: []
tags: ["tag1", "tag2"]
```

### Step 4: Create Content Files

Each content file should:

- **Start with a header** identifying the extension
- **Use markdown formatting** consistent with AI-DLC
- **Include actionable items** (checklists, questions, guidelines)
- **Reference stage context** where appropriate

Example `code-guidelines.md`:

```markdown
## [Your Extension Name] - Code Generation Guidelines

**Source**: your-extension-name extension v1.0.0

### Additional Considerations

When generating code for this project, the following additional guidelines apply:

#### Guideline Category 1
- [ ] Specific guideline item
- [ ] Another guideline item
- [ ] Additional consideration

#### Guideline Category 2
- [ ] Specific guideline item
- [ ] Another guideline item

### Questions for This Stage

If any of the following are unclear, create clarification questions:

1. Is [specific concern] addressed in the design?
2. Has [specific requirement] been considered?
```

---

## Rule Manifest Reference

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Unique identifier (lowercase, hyphens, no spaces) |
| `version` | string | Semantic version (e.g., "1.0.0") |
| `displayName` | string | Human-readable name for UI display |
| `description` | string | Brief description (1-2 sentences) |
| `category` | string | One of: `security`, `compliance`, `process`, `quality`, `architecture` |
| `applies_to` | object | Mapping of phases to stage configurations |

### Optional Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `author` | string | "Unknown" | Author or team name |
| `triggers` | object | `{}` | Conditions for auto-suggestion |
| `priority` | integer | 100 | Application order (lower = earlier) |
| `conflicts_with` | array | `[]` | Extension names that conflict |
| `depends_on` | array | `[]` | Extension names required first |
| `tags` | array | `[]` | Keywords for discoverability |

### Trigger Configuration

```yaml
triggers:
  # Suggest when ANY of these conditions match
  suggest_when:
    # Match project types (detected during workspace detection)
    - project_type: ["web", "api", "microservice", "library", "cli"]
    
    # Match keywords in requirements (case-insensitive)
    - has_requirements_keyword: ["security", "authentication", "pii"]
    
    # Match programming languages detected
    - programming_language: ["java", "python", "typescript"]
    
    # Match when specific files exist in workspace
    - has_file: ["Dockerfile", "serverless.yml"]
    
    # Match when specific dependencies are present
    - has_dependency: ["express", "spring-boot", "django"]
  
  # If true, extension appears in available list even without trigger match
  always_available: true
  
  # If true, extension is automatically enabled without user confirmation
  auto_enable: false
```

### Stage Application Configuration

```yaml
applies_to:
  inception:
    - stage: "requirements-analysis"  # Stage identifier
      file: "requirements.md"         # Your content file
      action: "append"                # How to apply content
      section: "NFR Section"          # For inject-section action only
      
  construction:
    - stage: "code-generation"
      file: "code-guidelines.md"
      action: "prepend"               # Add before core content
```

**Action Types**:
- `append`: Add content at the end of stage guidance
- `prepend`: Add content at the beginning of stage guidance
- `inject-section`: Insert content into a specific section (requires `section` field)

---

## Content Files

### File Naming Conventions

| File Name | Purpose |
|-----------|---------|
| `overview.md` | Human-readable description of the extension |
| `requirements.md` | Additional requirements considerations |
| `stories.md` | User story additions or templates |
| `design.md` | Design guidelines and patterns |
| `nfr-additions.md` | Non-functional requirement additions |
| `code-guidelines.md` | Code generation guidelines |
| `code-review.md` | Code review checklist additions |
| `testing.md` | Testing requirements and strategies |
| `questions.md` | Additional questions for any stage |

### Content File Template

```markdown
## [Extension Display Name] - [Stage Name] Additions

**Extension**: [extension-name] v[version]
**Applies To**: [Stage Name]

---

### Overview

Brief description of what this extension adds to this stage.

### Additional Requirements/Guidelines

#### Category 1: [Category Name]

**Objective**: What this category achieves

- [ ] Specific item 1
  - Detail or explanation
- [ ] Specific item 2
  - Detail or explanation
- [ ] Specific item 3

#### Category 2: [Category Name]

**Objective**: What this category achieves

- [ ] Specific item 1
- [ ] Specific item 2

### Additional Questions

If the following information is not already captured, add these questions:

**Question 1**: [Question text]
- A) Option A
- B) Option B
- C) Option C
- D) Other (please describe)

[Answer]: 

### References

- [Link to relevant documentation]
- [Link to standards or guidelines]

---

*This content is provided by the [extension-name] extension.*
```

### Writing Effective Content

#### DO:
- ✅ Use clear, actionable language
- ✅ Include checklists with `- [ ]` format
- ✅ Reference specific stages and artifacts
- ✅ Provide context for why items are important
- ✅ Use consistent formatting with AI-DLC style
- ✅ Include `[Answer]:` tags for questions

#### DON'T:
- ❌ Override or contradict core AI-DLC guidance
- ❌ Include implementation details (that's for the core stages)
- ❌ Use different question formats than AI-DLC standard
- ❌ Assume specific technologies (keep technology-agnostic when possible)
- ❌ Include executable code (extensions provide guidance, not code)

---

## Best Practices

### 1. Keep Extensions Focused

Each extension should address ONE specific concern:

✅ **Good**: "OWASP Security Guidelines" - focused on security
❌ **Bad**: "Security and Performance and Compliance" - too broad

### 2. Make Extensions Composable

Design extensions to work together:

```yaml
# Extension A
depends_on: []
conflicts_with: ["competing-extension"]

# Extension B (builds on A)
depends_on: ["extension-a"]
conflicts_with: []
```

### 3. Use Appropriate Triggers

Be specific with triggers to avoid noise:

```yaml
# Too broad - will trigger for almost everything
triggers:
  suggest_when:
    - has_requirements_keyword: ["the", "and", "or"]

# Better - specific to security concerns
triggers:
  suggest_when:
    - has_requirements_keyword: ["authentication", "authorization", "encryption", "pii", "sensitive"]
    - project_type: ["web", "api"]
```

### 4. Version Your Extensions

Follow semantic versioning:
- **MAJOR**: Breaking changes to manifest structure
- **MINOR**: New content files or features
- **PATCH**: Bug fixes, typo corrections

### 5. Document Thoroughly

Include an `overview.md` with:
- Purpose of the extension
- When to use it
- What it adds to each stage
- Prerequisites or assumptions
- Links to external documentation

---

## Testing Extensions

### Manual Testing

1. **Create test project** with characteristics that match your triggers
2. **Run AI-DLC workflow** from Workspace Detection
3. **Verify extension is suggested** during Workflow Planning
4. **Enable the extension** and proceed through stages
5. **Check each affected stage** for proper content application
6. **Review generated artifacts** for extension content

### Testing Checklist

```markdown
## Extension Testing Checklist: [extension-name]

### Manifest Validation
- [ ] YAML syntax is valid
- [ ] All required fields present
- [ ] Stage names match AI-DLC stage identifiers
- [ ] File references point to existing files

### Trigger Testing
- [ ] Extension suggested when triggers match
- [ ] Extension NOT suggested when triggers don't match
- [ ] `always_available: true` works correctly

### Content Application
- [ ] Content appears at correct stages
- [ ] Content applied with correct action (append/prepend/inject)
- [ ] Multiple extensions work together correctly
- [ ] Priority ordering is respected

### Content Quality
- [ ] Markdown renders correctly
- [ ] Questions use proper [Answer]: format
- [ ] Checklists use proper - [ ] format
- [ ] No conflicts with core AI-DLC content
```

### Automated Validation (Future)

```bash
# Validate manifest syntax
ai-dlc validate-extension aidlc-rules/extensions/my-extension/

# Check for common issues
ai-dlc lint-extension aidlc-rules/extensions/my-extension/

# Test trigger matching
ai-dlc test-triggers aidlc-rules/extensions/my-extension/ --context test-context.yaml
```

---

## Deployment (All Platforms)

### Understanding the Universal Deployment Model

Extensions live in `.aidlc-rule-details/extensions/` which is the **same location for ALL platforms**. This means:

1. **Write once, deploy everywhere** - One extension works on all platforms
2. **No platform-specific configuration** - Extensions don't need to know which AI tool is being used
3. **Consistent behavior** - Same extension produces same results regardless of platform

### Deployment to a Project

#### Step 1: Set Up AI-DLC for Your Platform

Follow the platform-specific setup in the main README.md. After setup, your project will have:

```
<my-project>/
├── [Platform-specific files]        # Varies by platform
└── .aidlc-rule-details/             # Universal location
    ├── common/
    ├── inception/
    ├── construction/
    └── operations/
```

#### Step 2: Add Extensions Directory

**Unix/Linux/macOS:**
```bash
# Create extensions directory in the universal location
mkdir -p .aidlc-rule-details/extensions
```

**Windows PowerShell:**
```powershell
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details\extensions"
```

**Windows CMD:**
```cmd
mkdir .aidlc-rule-details\extensions
```

#### Step 3: Copy Extensions

**Unix/Linux/macOS:**
```bash
# Copy a single extension
cp -R /path/to/security-owasp .aidlc-rule-details/extensions/

# Copy multiple extensions
cp -R /path/to/extensions/* .aidlc-rule-details/extensions/
```

**Windows PowerShell:**
```powershell
# Copy a single extension
Copy-Item "C:\path\to\security-owasp" ".aidlc-rule-details\extensions\" -Recurse

# Copy multiple extensions
Copy-Item "C:\path\to\extensions\*" ".aidlc-rule-details\extensions\" -Recurse
```

**Windows CMD:**
```cmd
REM Copy a single extension
xcopy "C:\path\to\security-owasp" ".aidlc-rule-details\extensions\security-owasp\" /E /I

REM Copy multiple extensions
xcopy "C:\path\to\extensions" ".aidlc-rule-details\extensions\" /E /I
```

#### Final Project Structure (All Platforms)

```
<my-project>/
├── [Platform-Specific Location]      # Varies by platform
│   └── core-workflow.md (or equivalent)
│
└── .aidlc-rule-details/              # UNIVERSAL
    ├── common/
    ├── inception/
    ├── construction/
    ├── operations/
    │
    └── extensions/                    # Extensions live here
        ├── _registry.md              # Optional catalog
        ├── security-owasp/
        │   ├── rule-manifest.yaml
        │   └── *.md files
        ├── compliance-hipaa/
        └── process-tdd/
```

### Platform-Specific Deployment Examples

#### Amazon Q Developer

```bash
# Unix/Linux/macOS
mkdir -p .amazonq/rules
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rules .amazonq/rules/
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/

# Add extensions
cp -R ../aidlc-workflows/aidlc-rules/extensions .aidlc-rule-details/
```

#### Kiro CLI

```bash
# Unix/Linux/macOS
mkdir -p .kiro/steering
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rules .kiro/steering/
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/

# Add extensions
cp -R ../aidlc-workflows/aidlc-rules/extensions .aidlc-rule-details/
```

#### Cursor IDE

```bash
# Unix/Linux/macOS
mkdir -p .cursor/rules
# [Create .mdc file as per README]
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/

# Add extensions
cp -R ../aidlc-workflows/aidlc-rules/extensions .aidlc-rule-details/
```

#### Cline

```bash
# Unix/Linux/macOS
mkdir -p .clinerules
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md .clinerules/
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/

# Add extensions
cp -R ../aidlc-workflows/aidlc-rules/extensions .aidlc-rule-details/
```

#### Claude Code

```bash
# Unix/Linux/macOS
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md ./CLAUDE.md
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/

# Add extensions
cp -R ../aidlc-workflows/aidlc-rules/extensions .aidlc-rule-details/
```

#### GitHub Copilot

```bash
# Unix/Linux/macOS
mkdir -p .copilot
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md .copilot/instructions.md
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/

# Add extensions
cp -R ../aidlc-workflows/aidlc-rules/extensions .aidlc-rule-details/
```

### Team/Organization Deployment

#### Option 1: Shared Git Repository

Store extensions in a central repository:

```
organization-aidlc-extensions/
├── security/
│   ├── security-owasp/
│   ├── security-sans/
│   └── security-internal/
├── compliance/
│   ├── compliance-hipaa/
│   ├── compliance-gdpr/
│   └── compliance-pci/
├── process/
│   ├── process-tdd/
│   └── process-code-review/
└── architecture/
    └── aws-well-architected/
```

Teams clone and copy needed extensions:

```bash
# Clone org extensions repo
git clone https://github.com/org/aidlc-extensions.git /tmp/org-extensions

# Copy needed extensions to project
cp -R /tmp/org-extensions/security/security-owasp .aidlc-rule-details/extensions/
cp -R /tmp/org-extensions/compliance/compliance-hipaa .aidlc-rule-details/extensions/
```

#### Option 2: Project Template

Include extensions in your project template/scaffolding:

```
project-template/
├── .amazonq/rules/aws-aidlc-rules/    # Or other platform
├── .aidlc-rule-details/
│   ├── common/
│   ├── inception/
│   ├── construction/
│   ├── operations/
│   └── extensions/
│       ├── security-owasp/            # Pre-included
│       └── compliance-internal/       # Pre-included
└── aidlc-docs/
    └── enabled-extensions.md          # Pre-configured
```

#### Option 3: Git Submodules

Reference extensions as submodules:

```bash
# Add extensions repo as submodule
git submodule add https://github.com/org/aidlc-extensions.git .aidlc-rule-details/extensions

# When cloning project
git clone --recurse-submodules https://github.com/org/my-project.git
```

### Pre-Enabling Extensions

Create `aidlc-docs/enabled-extensions.md` to auto-enable extensions:

```markdown
# Enabled Extensions

The following extensions are enabled for this project:

- security-owasp
- compliance-internal
- process-code-review

## Extension Justification

| Extension | Reason |
|-----------|--------|
| security-owasp | Required for all web applications per security policy |
| compliance-internal | Company compliance requirement |
| process-code-review | Team standard practice |

## Notes

These extensions were pre-enabled based on project template.
Users can disable extensions during Workflow Planning if needed.
```

### Version Control Recommendations

**Always commit** (add to version control):
```
.aidlc-rule-details/extensions/
aidlc-docs/enabled-extensions.md
```

**Add to `.gitignore`** (if using submodules or external refs):
```gitignore
# If using external extension management
.aidlc-rule-details/extensions/*/  # Managed externally
!.aidlc-rule-details/extensions/_registry.md
```

---

## Examples

### Example 1: Security Extension (OWASP)

**Purpose**: Add OWASP Top 10 security considerations

**Directory Structure**:
```
security-owasp/
├── rule-manifest.yaml
├── overview.md
├── requirements.md
├── design.md
├── code-guidelines.md
└── testing.md
```

**rule-manifest.yaml**:
```yaml
name: "security-owasp"
version: "1.0.0"
displayName: "OWASP Security Guidelines"
description: "Incorporates OWASP Top 10 security considerations"
author: "Security Team"
category: "security"

triggers:
  suggest_when:
    - project_type: ["web", "api", "microservice"]
    - has_requirements_keyword: ["security", "authentication", "login", "password", "user", "pii"]
  always_available: true

applies_to:
  inception:
    - stage: "requirements-analysis"
      file: "requirements.md"
      action: "append"
  construction:
    - stage: "nfr-requirements"
      file: "design.md"
      action: "append"
    - stage: "code-generation"
      file: "code-guidelines.md"
      action: "append"
    - stage: "build-and-test"
      file: "testing.md"
      action: "append"

priority: 50
tags: ["security", "owasp", "web-security"]
```

**requirements.md**:
```markdown
## OWASP Security Guidelines - Requirements Additions

**Extension**: security-owasp v1.0.0

### Security Requirements Checklist

Ensure requirements address the following OWASP Top 10 concerns:

#### A01: Broken Access Control
- [ ] Access control requirements defined
- [ ] Role-based permissions specified
- [ ] Resource-level authorization documented

#### A02: Cryptographic Failures
- [ ] Data classification defined (sensitive, PII, etc.)
- [ ] Encryption requirements specified
- [ ] Key management requirements documented

#### A03: Injection
- [ ] Input validation requirements defined
- [ ] Parameterized query requirements documented

[... continue for all OWASP Top 10 ...]

### Additional Security Questions

If not already captured, ask:

**Question S1**: What types of sensitive data will the application handle?
- A) Personal Identifiable Information (PII)
- B) Payment card data
- C) Health information
- D) No sensitive data
- E) Other (please describe)

[Answer]: 
```

### Example 2: Process Extension (TDD)

**Purpose**: Modify workflow to follow Test-Driven Development

**rule-manifest.yaml**:
```yaml
name: "process-tdd"
version: "1.0.0"
displayName: "Test-Driven Development"
description: "Modifies code generation to follow TDD practices (write tests first)"
author: "Engineering Team"
category: "process"

triggers:
  suggest_when:
    - has_requirements_keyword: ["tdd", "test-driven", "test first"]
  always_available: true

applies_to:
  inception:
    - stage: "workflow-planning"
      file: "workflow-modifications.md"
      action: "append"
  construction:
    - stage: "code-generation"
      file: "tdd-process.md"
      action: "prepend"
    - stage: "build-and-test"
      file: "testing-emphasis.md"
      action: "prepend"

priority: 25  # Lower priority to apply TDD process early
tags: ["tdd", "testing", "process", "agile"]
```

**tdd-process.md**:
```markdown
## Test-Driven Development Process

**Extension**: process-tdd v1.0.0

### MODIFIED Code Generation Sequence

**⚠️ IMPORTANT**: This extension modifies the standard code generation sequence.

For each component/function, follow this order:

1. **Write Test First**
   - [ ] Create test file for component
   - [ ] Write failing test that defines expected behavior
   - [ ] Verify test fails (red phase)

2. **Write Minimal Implementation**
   - [ ] Write just enough code to pass the test
   - [ ] Verify test passes (green phase)

3. **Refactor**
   - [ ] Improve code quality while keeping tests passing
   - [ ] Ensure all tests still pass after refactoring

### TDD Checklist for Each Unit

- [ ] Tests written BEFORE implementation
- [ ] Each test defines ONE behavior
- [ ] Tests are independent and isolated
- [ ] Test names describe expected behavior
- [ ] All tests pass before moving to next component
```

### Red-Green-Refactor Cycle

```
┌─────────┐     ┌─────────┐     ┌──────────┐ 
│  RED    │ ──► │  GREEN  │ ──► │ REFACTOR │ 
│ (Write  │     │ (Write  │     │ (Improve │ 
│  Test)  │     │  Code)  │     │  Code)   │ 
└─────────┘     └─────────┘     └────┬─────┘ 
     ▲                               │
     └───────────────────────────────┘
```
```

### Example 3: Compliance Extension (HIPAA)

**Purpose**: Add HIPAA compliance requirements for healthcare applications

**rule-manifest.yaml**:
```yaml
name: "compliance-hipaa"
version: "1.0.0"
displayName: "HIPAA Compliance"
description: "Adds HIPAA compliance requirements for healthcare applications"
author: "Compliance Team"
category: "compliance"

triggers:
  suggest_when:
    - has_requirements_keyword: ["hipaa", "healthcare", "phi", "patient", "medical", "health"]
  always_available: true
  auto_enable: false  # Requires explicit user confirmation due to compliance implications

applies_to:
  inception:
    - stage: "requirements-analysis"
      file: "hipaa-requirements.md"
      action: "append"
    - stage: "user-stories"
      file: "hipaa-stories.md"
      action: "append"
  construction:
    - stage: "nfr-requirements"
      file: "hipaa-nfr.md"
      action: "append"
    - stage: "infrastructure-design"
      file: "hipaa-infrastructure.md"
      action: "append"
    - stage: "build-and-test"
      file: "hipaa-testing.md"
      action: "append"

priority: 10  # High priority - compliance should be considered early
conflicts_with: []
depends_on: ["security-owasp"]  # HIPAA builds on general security
tags: ["compliance", "hipaa", "healthcare", "phi", "security"]
```

---

## Troubleshooting

### Extension Not Appearing

**Symptoms**: Extension doesn't show in Workflow Planning suggestions

**Checklist**:
- [ ] Extension folder exists in `aidlc-rules/extensions/`
- [ ] `rule-manifest.yaml` exists and has valid YAML syntax
- [ ] `name` field is unique across all extensions
- [ ] Either triggers match OR `always_available: true`

**Debug**:
```bash
# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('rule-manifest.yaml'))"
```

### Extension Content Not Applied

**Symptoms**: Extension enabled but content not appearing in stages

**Checklist**:
- [ ] `applies_to` stage names match AI-DLC stage identifiers exactly
- [ ] Content files exist and are named correctly
- [ ] `file` field in manifest matches actual filename
- [ ] `action` is one of: append, prepend, inject-section

### Conflict with Other Extensions

**Symptoms**: Unexpected behavior when multiple extensions enabled

**Checklist**:
- [ ] Check `conflicts_with` in both extensions' manifests
- [ ] Check `priority` values for application order
- [ ] Review both extensions' content for contradictions

### Common YAML Errors

```yaml
# ERROR: Missing quotes around special characters
description: This has a colon: in it  # Will fail

# FIX: Quote the string
description: "This has a colon: in it"

# ERROR: Incorrect indentation
applies_to:
inception:  # Wrong - needs to be indented
  - stage: "requirements-analysis"

# FIX: Correct indentation
applies_to:
  inception:
    - stage: "requirements-analysis"
```

---

## Getting Help

### Resources

- AI-DLC Documentation: See `aidlc-rules/aws-aidlc-rule-details/`
- Extension Examples: See `aidlc-rules/extensions/` directory
- Implementation Plan: See `aidlc-rules/EXTENSIBLE-RULES-PLAN.md`

### Reporting Issues

When reporting extension issues, include:
1. Extension name and version
2. `rule-manifest.yaml` content
3. AI-DLC stage where issue occurs
4. Expected vs actual behavior
5. Error messages (if any)

---

## Appendix: Stage Identifier Reference

| Phase | Stage | Identifier |
|-------|-------|------------|
| Inception | Workspace Detection | `workspace-detection` |
| Inception | Reverse Engineering | `reverse-engineering` |
| Inception | Requirements Analysis | `requirements-analysis` |
| Inception | User Stories | `user-stories` |
| Inception | Workflow Planning | `workflow-planning` |
| Inception | Application Design | `application-design` |
| Inception | Units Generation | `units-generation` |
| Construction | Functional Design | `functional-design` |
| Construction | NFR Requirements | `nfr-requirements` |
| Construction | NFR Design | `nfr-design` |
| Construction | Infrastructure Design | `infrastructure-design` |
| Construction | Code Generation | `code-generation` |
| Construction | Build and Test | `build-and-test` |
| Operations | Operations | `operations` |

---

*This guide is part of the AI-DLC Extensible Rules System.*