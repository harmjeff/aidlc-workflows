# Question Thoroughness Extension

Encourages comprehensive question generation and thorough answer analysis to prevent overconfidence and reduce assumptions.

---

## What It Does

This extension modifies AI-DLC's question generation behavior to:
- Default to asking questions when there's any ambiguity
- Evaluate ALL relevant question categories comprehensively
- Thoroughly analyze user responses for vagueness or contradictions
- Create follow-up questions for ANY unclear responses
- Prevent proceeding until ALL ambiguities are resolved

**Without this extension:** AI-DLC generates questions based on necessity, focusing on critical gaps only.

**With this extension:** AI-DLC takes a more thorough approach, asking clarifying questions proactively to ensure complete understanding before implementation.

---

## When to Use

Install this extension if:
- Your project is complex with many unknowns
- Requirements are not fully defined upfront
- You want to minimize rework due to assumptions
- Your team prefers thorough upfront clarification
- You're working on high-risk or business-critical systems

Skip this extension if:
- You have well-defined, clear requirements
- You prefer faster iteration with minimal questions
- You're comfortable providing clarifications as needed during implementation
- You're working on simple or low-risk changes

---

## Installation

Copy the rule files into your project's extensions directory:

### Kiro
```bash
mkdir -p .kiro/aws-aidlc-rule-details/extensions/standards/question-thoroughness
cp community-extensions/standards/question-thoroughness/question-thoroughness.md .kiro/aws-aidlc-rule-details/extensions/standards/question-thoroughness/
cp community-extensions/standards/question-thoroughness/question-thoroughness.opt-in.md .kiro/aws-aidlc-rule-details/extensions/standards/question-thoroughness/
```

### Amazon Q Developer
```bash
mkdir -p .amazonq/aws-aidlc-rule-details/extensions/standards/question-thoroughness
cp community-extensions/standards/question-thoroughness/question-thoroughness.md .amazonq/aws-aidlc-rule-details/extensions/standards/question-thoroughness/
cp community-extensions/standards/question-thoroughness/question-thoroughness.opt-in.md .amazonq/aws-aidlc-rule-details/extensions/standards/question-thoroughness/
```

### Cursor / Cline / Claude Code / GitHub Copilot
```bash
mkdir -p .aidlc-rule-details/extensions/standards/question-thoroughness
cp community-extensions/standards/question-thoroughness/question-thoroughness.md .aidlc-rule-details/extensions/standards/question-thoroughness/
cp community-extensions/standards/question-thoroughness/question-thoroughness.opt-in.md .aidlc-rule-details/extensions/standards/question-thoroughness/
```

Then start a new AI-DLC session. During Requirements Analysis, you'll be asked whether to enable thorough question generation for this project.

---

## What Changes

### Requirements Analysis
- More comprehensive question categories evaluated
- Questions asked proactively rather than only when absolutely necessary
- Enhanced answer analysis for vague responses

### User Stories
- All question categories evaluated (no skipping categories)
- Strengthened answer analysis requirements
- Mandatory follow-up questions for ambiguities

### Functional Design
- Comprehensive evaluation of all design aspects
- Expanded question categories (data flow, integration, error handling)
- Strengthened ambiguity detection and resolution

### NFR Requirements
- Expanded beyond basic NFRs to include reliability, maintainability, usability
- Enhanced answer analysis for technical ambiguities
- Thorough evaluation of all NFR categories

---

## Key Principles

1. **Default to Asking**: When there's any ambiguity, ask clarifying questions
2. **Comprehensive Coverage**: Evaluate ALL relevant categories, don't skip areas
3. **Thorough Analysis**: Carefully analyze ALL user responses for ambiguities
4. **Mandatory Follow-up**: Create follow-up questions for ANY unclear responses
5. **No Proceeding with Ambiguity**: Don't move forward until ALL ambiguities are resolved

---

## Trade-offs

**Advantages:**
- Fewer assumptions and misunderstandings
- Better quality requirements upfront
- Reduced rework during implementation
- Clearer, more complete specifications

**Disadvantages:**
- More questions to answer upfront
- Longer Requirements/Design phases
- May feel excessive for simple projects
- Requires more time investment early in the workflow
