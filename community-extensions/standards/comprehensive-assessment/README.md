# Comprehensive Assessment Extension

Provides detailed, multi-layered assessment frameworks for Requirements Analysis, User Stories, and Workflow Planning stages to make more informed decisions about workflow execution.

---

## What It Does

This extension adds comprehensive assessment criteria for:
- **Requirements Analysis**: Detailed completeness analysis framework
- **User Stories**: Intelligent multi-factor assessment with priority matrix
- **Workflow Planning**: Detailed change impact and risk assessment across multiple layers

**Without this extension:** AI-DLC uses simpler heuristics and basic decision criteria.

**With this extension:** AI-DLC applies structured, comprehensive assessment frameworks with detailed evaluation criteria.

---

## When to Use

Install this extension if:
- You're working on complex, high-risk projects
- You want structured decision-making frameworks
- Your team benefits from detailed assessment documentation
- You need to justify workflow decisions to stakeholders
- You're managing multi-layer system changes (application, infrastructure, operations)

Skip this extension if:
- You prefer lightweight, fast decision-making
- Your projects are relatively simple
- You trust basic heuristics over detailed frameworks
- You want to minimize upfront analysis overhead

---

## Installation

Copy the rule files into your project's extensions directory:

### Kiro
```bash
mkdir -p .kiro/aws-aidlc-rule-details/extensions/standards/comprehensive-assessment
cp community-extensions/standards/comprehensive-assessment/comprehensive-assessment.md .kiro/aws-aidlc-rule-details/extensions/standards/comprehensive-assessment/
cp community-extensions/standards/comprehensive-assessment/comprehensive-assessment.opt-in.md .kiro/aws-aidlc-rule-details/extensions/standards/comprehensive-assessment/
```

### Amazon Q Developer
```bash
mkdir -p .amazonq/aws-aidlc-rule-details/extensions/standards/comprehensive-assessment
cp community-extensions/standards/comprehensive-assessment/comprehensive-assessment.md .amazonq/aws-aidlc-rule-details/extensions/standards/comprehensive-assessment/
cp community-extensions/standards/comprehensive-assessment/comprehensive-assessment.opt-in.md .amazonq/aws-aidlc-rule-details/extensions/standards/comprehensive-assessment/
```

### Cursor / Cline / Claude Code / GitHub Copilot
```bash
mkdir -p .aidlc-rule-details/extensions/standards/comprehensive-assessment
cp community-extensions/standards/comprehensive-assessment/comprehensive-assessment.md .aidlc-rule-details/extensions/standards/comprehensive-assessment/
cp community-extensions/standards/comprehensive-assessment/comprehensive-assessment.opt-in.md .aidlc-rule-details/extensions/standards/comprehensive-assessment/
```

Then start a new AI-DLC session. During Workspace Detection, you'll be asked whether to enable comprehensive assessment frameworks.

---

## What Changes

### Requirements Analysis
- Applies detailed completeness analysis across 6 evaluation areas
- Structured assessment of functional, NFR, user scenarios, business/technical context, quality attributes
- More thorough evaluation before generating requirements

### User Stories
- Uses intelligent multi-factor assessment with priority matrix
- Applies complexity assessment factors for medium-priority cases
- Detailed justification required before executing User Stories stage
- Documents assessment decision for stakeholder review

### Workflow Planning
- Detailed change impact assessment across 4 layers: Application, Infrastructure, Operations, plus Impact Areas
- Structured risk assessment with 4-level risk matrix (Low, Medium, High, Critical)
- Comprehensive analysis of structural, data model, API, and NFR impacts

---

## Trade-offs

**Advantages:**
- More informed, justified decisions
- Better documentation for stakeholders
- Comprehensive risk and impact understanding
- Structured decision frameworks
- Clearer assessment rationale

**Disadvantages:**
- More analysis overhead upfront
- Longer assessment phases
- May feel excessive for simple projects
- Requires more careful documentation review
