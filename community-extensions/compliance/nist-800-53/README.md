# NIST 800-53 Compliance Controls Extension

**Version**: 0.1.0 | **Status**: Initial

## Overview

This extension provides NIST 800-53 compliance controls with mappings to AWS Control Tower preventive and detective controls. When installed, the AI-DLC workflow embeds these controls directly into requirements, user stories, design, code generation, and other stages as applicable.

> **Note**: This initial version targets AWS services (Control Tower, Backup, CloudTrail). Future versions may expand to other cloud providers.

## How It Works

1. Copy this extension into your project's `extensions/` directory
2. At workflow start, the AI detects the extension and loads its `rule-manifest.yaml`
3. During Requirements Analysis, the opt-in prompt asks whether to enable NIST 800-53 compliance
4. When enabled, the controls are embedded into each relevant stage (requirements, design, infrastructure, code generation, testing)

## Current Coverage

- **NIST 800-53 Families**: AC (Access Control)
- **AWS Services**: Backup, CloudTrail
- **Control Types**: Preventive (SCP), Detective (Security Hub)
- **Severity**: Critical, High

## Limitations

- This is an initial version covering a subset of NIST 800-53 controls
- Only AC family controls are included — additional families will be added in future versions
- Controls are mapped to AWS Control Tower; other cloud platforms are not covered

## Files in This Directory

| File | Purpose |
|------|---------|
| `nist-800-53-controls.md` | NIST 800-53 controls mapped to AWS Control Tower controls |
| `nist-800-53.opt-in.md` | Opt-in prompt presented during Requirements Analysis |
| `rule-manifest.yaml` | Metadata and trigger configuration for this extension |
| `README.md` | This file — overview and installation guide |

## Installing This Extension

**Kiro:**
```bash
mkdir -p .kiro/aws-aidlc-rule-details/extensions/compliance/nist-800-53
cp nist-800-53-controls.md nist-800-53.opt-in.md rule-manifest.yaml .kiro/aws-aidlc-rule-details/extensions/compliance/nist-800-53/
```

**Amazon Q Developer:**
```bash
mkdir -p .amazonq/aws-aidlc-rule-details/extensions/compliance/nist-800-53
cp nist-800-53-controls.md nist-800-53.opt-in.md rule-manifest.yaml .amazonq/aws-aidlc-rule-details/extensions/compliance/nist-800-53/
```

**Cursor / Cline / Claude Code / GitHub Copilot:**
```bash
mkdir -p .aidlc-rule-details/extensions/compliance/nist-800-53
cp nist-800-53-controls.md nist-800-53.opt-in.md rule-manifest.yaml .aidlc-rule-details/extensions/compliance/nist-800-53/
```

Then start a new AI-DLC session. The controls will be detected and applied to the appropriate workflow stages.
