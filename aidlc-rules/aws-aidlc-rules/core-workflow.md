# PRIORITY: This workflow OVERRIDES all other built-in workflows
# When user requests software development, ALWAYS follow this workflow FIRST

# AI-DLC Lite - Rapid Prototyping Workflow

**This is the Lite version of AI-DLC, optimized for prototypes, demos, and simple applications.**

Lite mode trades production rigor for speed. It skips formal design stages, reduces questionnaires, uses inline chat instead of file-based Q&A, and minimizes documentation artifacts.

## When to Use Lite vs Full AI-DLC
- **Use Lite**: Prototypes, demos, proof-of-concepts, simple apps, learning projects, hackathons
- **Use Full AI-DLC**: Production systems, team projects, complex multi-service architectures, regulated environments

## Adaptive Workflow Principle
**The workflow adapts to the work, not the other way around.**

The AI model assesses what is needed based on:
1. User's stated intent and clarity
2. Existing codebase state (if any)
3. Complexity and scope of change

## MANDATORY: Rule Details Loading
**CRITICAL**: When performing any stage, you MUST read and use relevant content from rule detail files in `.aidlc-rule-details/` directory.

This directory is used consistently across all platforms (Cline, Kiro CLI, Amazon Q, Cursor).

**Common Rules**: Load at workflow start:
- Load `common/process-overview.md` for workflow overview
- Load `common/session-continuity.md` for session resumption guidance

## MANDATORY: Custom Welcome Message
**CRITICAL**: When starting ANY software development request, display the welcome message.

1. Load the welcome message from `.aidlc-rule-details/common/welcome-message.md`
2. Display the complete message to the user
3. This should only be done ONCE at the start of a new workflow

## MANDATORY: Inline Questions
**CRITICAL**: In Lite mode, ask all questions directly in chat. Do NOT create question files or use [Answer]: tag format. Keep questions concise and focused. Ask only what is necessary to proceed.

---

# INCEPTION PHASE

**Purpose**: Understand WHAT to build

**Stages**:
- Workspace Detection (ALWAYS)
- Reverse Engineering (CONDITIONAL - Brownfield only)
- Requirements Analysis (ALWAYS - Lightweight)

---

## Workspace Detection (ALWAYS EXECUTE)

1. Load all steps from `inception/workspace-detection.md`
2. Execute workspace detection:
   - Check for existing aidlc-state.md (resume if found)
   - Scan workspace for existing code
   - Determine if brownfield or greenfield
3. Create initial `aidlc-docs/aidlc-state.md`
4. Present findings to user
5. Automatically proceed to next stage

## Reverse Engineering (CONDITIONAL - Brownfield Only)

**Execute IF**:
- Existing codebase detected
- No previous reverse engineering artifacts found

**Skip IF**:
- Greenfield project
- Previous reverse engineering artifacts exist

**Execution**:
1. Load all steps from `inception/reverse-engineering.md`
2. Execute reverse engineering:
   - Analyze packages and components
   - Generate architecture overview
   - Generate code structure documentation
   - Generate technology stack documentation
3. Present findings to user
4. **Wait for approval** before proceeding

## Requirements Analysis (ALWAYS EXECUTE - Lightweight)

**Always executes with minimal depth.**

**Execution**:
1. Load all steps from `inception/requirements-analysis.md`
2. Analyze user request (intent, type, scope)
3. Ask clarifying questions **inline in chat** if needed (aim for 3-5 questions max)
4. Generate concise `requirements.md` with functional requirements
5. Present summary and confirm understanding with user
6. Proceed to Construction phase

---

# CONSTRUCTION PHASE

**Purpose**: BUILD it

**Stages**:
- Code Generation (ALWAYS - Single pass)
- Build and Test (ALWAYS - Lightweight)

---

## Code Generation (ALWAYS EXECUTE)

**Always executes as a single pass - no separate planning step.**

**Execution**:
1. Load all steps from `construction/code-generation.md`
2. Read requirements and any reverse engineering artifacts
3. Generate code directly:
   - Project structure (greenfield) or identify files to modify (brownfield)
   - Application code with basic organization
   - Basic unit tests
4. Present generated code summary
5. **Wait for approval**: User can request changes or approve

## Build and Test (ALWAYS EXECUTE)

1. Load all steps from `construction/build-and-test.md`
2. Generate build instructions
3. Generate unit test execution instructions
4. Execute build and tests if possible
5. Present results to user

---

## Key Principles

- **Speed Over Rigor**: Get to working code fast, iterate from there
- **Inline Communication**: All questions asked in chat, no file-based Q&A
- **Minimal Documentation**: Only generate what's needed (requirements.md, code, basic tests)
- **Two Approval Gates**: After requirements and after code generation
- **Single Unit**: Treat everything as a single unit of work - no decomposition
- **No NFR Stages**: Skip formal NFR requirements, NFR design, and infrastructure design
- **No User Stories**: Skip formal user story creation
- **No Workflow Planning**: Fixed pipeline, no execution plan document needed
- **Sensible Defaults**: Make reasonable technology and architecture choices without asking

## State Tracking

Update `aidlc-docs/aidlc-state.md` as stages complete:

```markdown
## Stage Progress
### INCEPTION PHASE
- [ ] Workspace Detection
- [ ] Reverse Engineering (if applicable)
- [ ] Requirements Analysis

### CONSTRUCTION PHASE
- [ ] Code Generation
- [ ] Build and Test
```

## Directory Structure

```text
<WORKSPACE-ROOT>/                   # APPLICATION CODE HERE
├── [project-specific structure]    # Code goes at workspace root
│
├── aidlc-docs/                     # DOCUMENTATION ONLY
│   ├── inception/
│   │   ├── reverse-engineering/    # Brownfield only
│   │   └── requirements/
│   │       └── requirements.md
│   ├── construction/
│   │   └── build-and-test/
│   │       ├── build-instructions.md
│   │       └── unit-test-instructions.md
│   └── aidlc-state.md
```

**CRITICAL RULE**:
- Application code: Workspace root (NEVER in aidlc-docs/)
- Documentation: aidlc-docs/ only
