# AI-DLC Lite - Workflow Overview

**Purpose**: Technical reference for AI model to understand the Lite workflow structure.

## The Two-Phase Lifecycle
- **INCEPTION PHASE**: Understand the workspace and gather requirements
- **CONSTRUCTION PHASE**: Generate code, build, and test

## The Lite Workflow

```
User Request → Workspace Detection → [Reverse Engineering] → Requirements Analysis → Code Generation → Build and Test → Complete
```

- **Workspace Detection** (always) - Detect greenfield vs brownfield
- **Reverse Engineering** (brownfield only) - Analyze existing codebase
- **Requirements Analysis** (always) - Lightweight requirements gathering with inline questions
- **Code Generation** (always) - Single-pass code generation
- **Build and Test** (always) - Build verification and unit tests

## How It Works
- AI analyzes your request and workspace to understand what to build
- Questions are asked inline in chat (no file-based questionnaires)
- Code is generated in a single pass (no separate planning step)
- Only two approval gates: after requirements and after code generation
- Everything is treated as a single unit of work

## Key Differences from Full AI-DLC
- No User Stories stage
- No Workflow Planning stage
- No Application Design or Units Generation stages
- No Functional Design, NFR Requirements, NFR Design, or Infrastructure Design stages
- No file-based question format with [Answer]: tags
- No formal audit trail
- No contradiction detection or multi-round clarification
- No per-step checkbox tracking
- Minimal documentation artifacts
