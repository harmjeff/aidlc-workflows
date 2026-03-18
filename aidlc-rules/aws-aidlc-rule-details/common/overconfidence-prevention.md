# Overconfidence Prevention

**Stage Type**: COMMON  
**Load Timing**: Load at workflow start, reference throughout  
**Unload Timing**: Keep in context throughout workflow

---

## Purpose

Prevents AI overconfidence by encouraging proactive questioning and thorough requirements gathering.

---

## Problem Statement

AI-DLC can exhibit overconfidence by not asking enough clarifying questions, even for complex project intent statements. This leads to assumptions being made instead of gathering proper requirements.

---

## Root Cause

Overconfidence is caused by directives that encourage skipping questions:
- "Skip entire categories if not applicable"
- "Use categories as inspiration, NOT as mandatory checklist"
- "Only if" conditions that discourage thorough analysis

These directives tell the AI to avoid asking questions rather than encouraging comprehensive requirements gathering.

---

## Solution: Proactive Questioning Approach

### Updated Philosophy

**OLD APPROACH**: "Only ask questions if absolutely necessary"  
**NEW APPROACH**: "When in doubt, ask the question - overconfidence leads to poor outcomes"

### Key Principles

1. **Default to Asking**: When there's any ambiguity, ask clarifying questions
2. **Comprehensive Coverage**: Evaluate ALL relevant categories, don't skip areas
3. **Thorough Analysis**: Carefully analyze ALL user responses for ambiguities
4. **Mandatory Follow-up**: Create follow-up questions for ANY unclear responses
5. **No Proceeding with Ambiguity**: Don't move forward until ALL ambiguities are resolved

---

## Implementation Guidelines

### For Question Generation
- Evaluate ALL question categories, don't skip any
- Ask questions wherever clarification would improve quality
- Include comprehensive question categories in each stage
- Default to inclusion rather than exclusion of questions

### For Answer Analysis
Look for vague responses:
- "depends", "maybe", "not sure"
- "mix of", "somewhere between"
- Undefined terms and references to external concepts
- Contradictory or incomplete answers

Create follow-up questions for ANY ambiguities.

### For Follow-up Questions
- Create separate clarification files when ambiguities are detected
- Ask specific questions to resolve each ambiguity
- Don't proceed until ALL unclear responses are clarified
- Be thorough - better to over-clarify than under-clarify

---

## Quality Assurance

### Red Flags to Watch For
- Stages completing without asking any questions on complex projects
- Proceeding with vague or ambiguous user responses
- Skipping entire question categories without justification
- Making assumptions instead of asking for clarification

### Success Indicators
- Appropriate number of clarifying questions for project complexity
- Thorough analysis of user responses with follow-up when needed
- Clear, unambiguous requirements before proceeding to implementation
- Reduced need for changes during later stages due to better upfront clarification

---

## Key Takeaway

**It's better to ask too many questions than to make incorrect assumptions.**

The cost of asking clarifying questions upfront is far less than the cost of implementing the wrong solution based on assumptions.

---

## Context Management

**When to Load**: At workflow start

**When to Keep**: Throughout entire workflow execution

**Related Files**:
- `question-format.md` - How to format questions
- All stage files - Apply proactive questioning principle
