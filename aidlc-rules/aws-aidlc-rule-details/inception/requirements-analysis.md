# Requirements Analysis (Lite)

**Purpose**: Quickly understand what the user wants to build.

**Always executes.** Keep it lightweight - aim for speed over exhaustive coverage.

## Prerequisites
- Workspace Detection must be complete
- Reverse Engineering must be complete (if brownfield)

## Step 1: Load Context (if brownfield)

**IF brownfield project**:
- Read `aidlc-docs/inception/reverse-engineering/architecture.md`
- Read `aidlc-docs/inception/reverse-engineering/code-structure.md`
- Use these to understand existing system when analyzing request

## Step 2: Analyze User Request

Quickly assess:
- **Intent**: What does the user want to build or change?
- **Type**: New feature, bug fix, enhancement, new project, etc.
- **Scope**: Single file, single component, or multiple components?

## Step 3: Ask Clarifying Questions (Inline)

**CRITICAL**: Ask questions directly in the chat. Do NOT create question files.

- Ask only questions that are necessary to start generating code
- Aim for **3-5 questions maximum**
- Focus on:
  - Core functionality that isn't clear from the request
  - Technology preferences (if not already determined by brownfield context)
  - Any critical constraints or must-haves
- Make sensible assumptions for anything non-critical and state them
- Do NOT ask about NFRs, scalability, security patterns, or deployment architecture

**Example**:
```
Before I start building, I have a few questions:

1. [Core functionality question]
2. [Technology preference question]
3. [Key constraint question]

I'll assume [assumption 1] and [assumption 2] unless you tell me otherwise.
```

## Step 4: Generate Requirements Document

After receiving answers, create `aidlc-docs/inception/requirements/requirements.md`:

```markdown
# Requirements

## Project Overview
- **Type**: [New project / Enhancement / Bug fix / etc.]
- **Scope**: [Brief scope description]

## Functional Requirements
1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]
...

## Assumptions
- [Assumption 1]
- [Assumption 2]
...

## Out of Scope
- [What this prototype does NOT include]
```

Keep it concise. A prototype's requirements document should be 1-2 pages at most.

## Step 5: Update State

Update `aidlc-docs/aidlc-state.md`:
- Mark Requirements Analysis as complete

## Step 6: Confirm and Proceed

Present a brief summary:

```markdown
# Requirements Analysis Complete

Here's what I'll build:
- [1-3 bullet point summary of what will be built]

**Assumptions I'm making:**
- [Key assumptions]

**Out of scope:**
- [What's excluded]

Does this look right? I'll proceed to code generation.
```

- Wait for user confirmation
- If user confirms or says to proceed, move to Code Generation
- If user requests changes, update requirements and re-confirm
