# Extensible Rules System - Implementation Plan

## Overview

This document outlines the plan to add an optional, extensible rules system to AI-DLC that allows users to add custom rules for specific aspects of the software development process (security guidelines, regulatory compliance, TDD, etc.) with **minimal changes** to the existing core workflow.

**Universal Design**: This system is designed to work across ALL supported AI-DLC platforms:
- Amazon Q Developer IDE Plugin
- Kiro CLI
- Cursor IDE
- Cline
- Claude Code
- GitHub Copilot

---

## Goals

1. **Minimal Invasiveness**: Changes to existing AI-DLC files should be minimal
2. **Additive by Design**: Custom rules extend, not replace, core functionality
3. **Self-Describing**: Each rule contains metadata describing when/how to apply it
4. **Discoverable**: System automatically detects and loads applicable rules
5. **Curated**: Repository owners can curate rules for specific SDLC impacts
6. **Universal**: Extensions work identically across all supported platforms

---

## Cross-Platform Compatibility

### Why Universal Extensions Work

AI-DLC uses a **two-tier architecture** across all platforms:

1. **Platform-Specific Rule Location** (varies by platform):
   - Amazon Q: `.amazonq/rules/aws-aidlc-rules/`
   - Kiro CLI: `.kiro/steering/aws-aidlc-rules/`
   - Cursor: `.cursor/rules/ai-dlc-workflow.mdc`
   - Cline: `.clinerules/`
   - Claude Code: `CLAUDE.md` or `.claude/CLAUDE.md`
   - GitHub Copilot: `.copilot/instructions.md` or `COPILOT.md`

2. **Universal Rule Details Location** (same for all platforms):
   - `.aidlc-rule-details/` - Contains detailed stage instructions loaded on-demand

**Key Insight**: The `core-workflow.md` file (copied to platform-specific locations) instructs the AI to load detailed rules from `.aidlc-rule-details/`. This common location is where extensions live, making them **automatically universal**.

### Simplified Universal Location

The `core-workflow.md` uses a single universal location:

```markdown
## MANDATORY: Rule Details Loading
**CRITICAL**: When performing any phase, you MUST read and use relevant content from rule detail files in:
- `.aidlc-rule-details/` (Universal location for ALL platforms)
```

Extensions leverage this same universal location, making them automatically work on ALL platforms without any platform-specific configuration.

---

## Proposed Directory Structure

### Source Repository Structure
```
aidlc-workflows/                     # This repository
├── aidlc-rules/
│   ├── aws-aidlc-rules/             # Core workflow (existing)
│   │   └── core-workflow.md
│   ├── aws-aidlc-rule-details/      # Core rule details (existing)
│   │   ├── common/
│   │   ├── inception/
│   │   ├── construction/
│   │   └── operations/
│   │
│   └── extensions/                   # NEW: Extension templates/examples
│       ├── _registry.md
│       ├── security-owasp/
│       ├── compliance-hipaa/
│       ├── process-tdd/
│       └── aws-well-architected/
```

### Project Deployment Structure (Universal)
```
<my-project>/
├── [Platform-Specific Location]      # Varies by platform (see above)
│   └── core-workflow.md (or equivalent)
│
└── .aidlc-rule-details/              # UNIVERSAL - Same for ALL platforms
    ├── common/
    ├── inception/
    ├── construction/
    ├── operations/
    │
    └── extensions/                    # NEW: Custom rules (universal location)
        ├── _registry.md
        │
        ├── security-owasp/            # Example: OWASP security guidelines
        │   ├── rule-manifest.yaml     # Metadata: when/how to apply
        │   ├── overview.md            # Human-readable description
        │   ├── requirements.md        # Additions to requirements analysis
        │   ├── design.md              # Additions to design stages
        │   ├── code-review.md         # Additions to code generation
        │   └── testing.md             # Additions to test stages
        │
        ├── compliance-hipaa/          # Example: HIPAA compliance
        │   ├── rule-manifest.yaml
        │   ├── overview.md
        │   └── ...
        │
        ├── process-tdd/               # Example: Test-Driven Development
        │   ├── rule-manifest.yaml
        │   ├── overview.md
        │   └── ...
        │
        └── aws-well-architected/      # Example: AWS Well-Architected
            ├── rule-manifest.yaml
            ├── overview.md
            └── ...
```

### Platform-Specific Examples

**Amazon Q Developer:**
```
<my-project>/
├── .amazonq/
│   └── rules/
│       └── aws-aidlc-rules/
│           └── core-workflow.md
└── .aidlc-rule-details/
    ├── common/, inception/, construction/, operations/
    └── extensions/                    # ← Extensions here (universal)
```

**Cursor IDE:**
```
<my-project>/
├── .cursor/
│   └── rules/
│       └── ai-dlc-workflow.mdc
└── .aidlc-rule-details/
    ├── common/, inception/, construction/, operations/
    └── extensions/                    # ← Extensions here (universal)
```

**Claude Code:**
```
<my-project>/
├── CLAUDE.md
└── .aidlc-rule-details/
    ├── common/, inception/, construction/, operations/
    └── extensions/                    # ← Extensions here (universal)
```

---

## Rule Manifest Schema

Each extension folder MUST contain a `rule-manifest.yaml` file:

```yaml
# rule-manifest.yaml
name: "security-owasp"
version: "1.0.0"
displayName: "OWASP Security Guidelines"
description: "Incorporates OWASP Top 10 security considerations into the development lifecycle"
author: "Security Team"
category: "security"  # security | compliance | process | quality | architecture

# When this rule should be offered/applied
triggers:
  # Auto-suggest when these conditions are met
  suggest_when:
    - project_type: ["web", "api", "microservice"]
    - has_requirements_keyword: ["security", "authentication", "authorization", "pii", "sensitive"]
  # User can always manually enable regardless of triggers
  always_available: true

# Which AI-DLC stages this rule affects
applies_to:
  inception:
    - stage: "requirements-analysis"
      file: "requirements.md"
      action: "append"  # append | prepend | inject-section
    - stage: "user-stories"
      file: "stories.md"
      action: "append"
  construction:
    - stage: "functional-design"
      file: "design.md"
      action: "append"
    - stage: "nfr-requirements"
      file: "nfr-additions.md"
      action: "append"
    - stage: "code-generation"
      file: "code-review.md"
      action: "append"
    - stage: "build-and-test"
      file: "testing.md"
      action: "append"

# Priority when multiple rules apply to same stage (lower = earlier)
priority: 100

# Conflicts with other rules (mutually exclusive)
conflicts_with: []

# Requires other rules to be enabled first
depends_on: []

# Tags for discoverability
tags: ["security", "owasp", "web-security", "api-security"]
```

---

## Minimal Changes to Existing AI-DLC

### Change 1: Add Extension Loading to `core-workflow.md`

**Location**: After the "MANDATORY: Rule Details Loading" section

**Addition** (~20 lines):

```markdown
## OPTIONAL: Extension Rules Loading

**After loading core rules**, check for enabled extensions:

1. **Check for extensions directory**: Look for `extensions/` in `.aidlc-rule-details/`
2. **Load enabled extensions**: 
   - Check `aidlc-docs/enabled-extensions.md` for user-selected extensions
   - If file doesn't exist, scan extensions and suggest relevant ones based on triggers
3. **For each enabled extension**:
   - Read `rule-manifest.yaml` to understand when to apply
   - Load extension files at appropriate stages
   - Apply content according to `action` (append/prepend/inject-section)

**Extension Application Points**:
- Extensions are applied AFTER core stage logic
- Extensions ADD to existing guidance (never replace)
- Multiple extensions can apply to the same stage
- Priority determines application order
- Apply extensions at each stage as specified in their `applies_to` configuration
```

**Note**: No changes are required to individual stage documents. The `core-workflow.md` already controls the entire flow and can instruct the AI to apply extensions at each stage.

### Change 2: Add Extension Selection to Workflow Planning

**Location**: `workflow-planning.md` - Add new step after Step 1

**Addition** (~15 lines):

```markdown
### Step 1.5: Extension Selection

1. **Scan available extensions** in `.aidlc-rule-details/extensions/` directory
2. **Check for pre-enabled extensions** in `aidlc-docs/enabled-extensions.md`
3. **Suggest relevant extensions** based on trigger conditions:
   - Match project type against extension triggers
   - Match requirements keywords against extension triggers
4. **Present extension options** to user:
   - List suggested extensions with brief descriptions
   - Allow user to enable/disable extensions
   - Save selections to `aidlc-docs/enabled-extensions.md`
5. **Log extension decisions** in `audit.md`
```

### Change 3: Create Extension Registry Template

**New File**: `.aidlc-rule-details/extensions/_registry.md`

```markdown
# Available Extensions

This directory contains optional rules that can be enabled for specific project needs.

## Extension Categories

| Category | Purpose |
|----------|---------|
| `security` | Security guidelines, threat modeling, secure coding |
| `compliance` | Regulatory compliance (HIPAA, GDPR, SOC2, etc.) |
| `process` | Development process modifications (TDD, BDD, etc.) |
| `quality` | Code quality, testing standards, documentation |
| `architecture` | Architectural frameworks (AWS Well-Architected, etc.) |

## Enabling Extensions

Extensions are enabled during Workflow Planning stage. You can also manually create/edit `aidlc-docs/enabled-extensions.md`:

```markdown
# Enabled Extensions

- security-owasp
- compliance-hipaa
- process-tdd
```

## Creating New Extensions

See `EXTENSION-AUTHORING-GUIDE.md` for instructions on creating custom extensions.
```

---

## Summary of Changes

| File | Change Type | Lines Added |
|------|-------------|-------------|
| `core-workflow.md` | Addition | ~20 lines |
| `workflow-planning.md` | Addition | ~15 lines |
| `extensions/_registry.md` | New file | ~50 lines |
| **Total Core Changes** | | **~85 lines** |

**Why so minimal?** The `core-workflow.md` already controls the entire AI-DLC flow. Extension logic is added once there, and it applies to all stages automatically. No changes are needed to individual stage documents like `requirements-analysis.md`, `code-generation.md`, etc.

---

## Implementation Phases

### Phase 1: Foundation (Week 1)
- [ ] Create `extensions/` directory structure
- [ ] Create `_registry.md` template
- [ ] Define `rule-manifest.yaml` schema
- [ ] Create extension authoring guide

### Phase 2: Core Integration (Week 2)
- [ ] Update `core-workflow.md` with extension loading (~20 lines)
- [ ] Update `workflow-planning.md` with extension selection (~15 lines)
- [ ] Create `enabled-extensions.md` template

### Phase 3: Sample Extensions (Week 3)
- [ ] Create `security-owasp` sample extension
- [ ] Create `process-tdd` sample extension
- [ ] Create `compliance-template` skeleton extension
- [ ] Test extension loading and application

### Phase 4: Documentation & Testing (Week 4)
- [ ] Complete extension authoring guide
- [ ] Add extension troubleshooting guide
- [ ] Test with real-world scenarios
- [ ] Document edge cases and limitations

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Extension conflicts | Medium | Medium | Conflict detection in manifest |
| Performance impact | Low | Low | Lazy loading, caching |
| Complexity increase | Medium | Medium | Keep extensions additive only |
| User confusion | Medium | Low | Clear documentation, suggestions |

---

## Success Criteria

1. **Minimal Disruption**: Existing AI-DLC workflows work unchanged without extensions
2. **Easy Adoption**: Users can enable extensions with a single selection
3. **Clear Authoring**: New extensions can be created following documented patterns
4. **Maintainable**: Extensions can be versioned and updated independently
5. **Discoverable**: Relevant extensions are suggested based on project context