# Reverse Engineering (Lite)

**Purpose**: Quickly analyze existing codebase to understand what's there before making changes.

**Execute when**: Brownfield project detected (existing code found in workspace)

**Skip when**: Greenfield project (no existing code)

## Step 1: Scan Workspace

- Identify all packages and their relationships
- Determine build system and dependencies
- Identify key services, APIs, and data stores
- Note programming languages and frameworks

## Step 2: Generate Architecture Overview

Create `aidlc-docs/inception/reverse-engineering/architecture.md`:

```markdown
# System Architecture

## Overview
[High-level description of the system]

## Components
### [Component/Package Name]
- **Purpose**: [What it does]
- **Type**: [Application/Infrastructure/Model/Test]
- **Dependencies**: [What it depends on]

## Key APIs
### [Endpoint/Interface Name]
- **Method**: [GET/POST/PUT/DELETE]
- **Path**: [/api/path]
- **Purpose**: [What it does]

## Data Stores
- [Database/Store] - [Purpose]
```

## Step 3: Generate Code Structure Documentation

Create `aidlc-docs/inception/reverse-engineering/code-structure.md`:

```markdown
# Code Structure

## Build System
- **Type**: [Maven/Gradle/npm/etc.]
- **Configuration**: [Key build files]

## Key Files
[List source files with their purposes - these are candidates for modification]
- `[path/to/file]` - [Purpose]

## Programming Languages and Frameworks
- [Language] - [Version] - [Framework]
```

## Step 4: Generate Technology Stack Documentation

Create `aidlc-docs/inception/reverse-engineering/technology-stack.md`:

```markdown
# Technology Stack

## Languages
- [Language] - [Version]

## Frameworks
- [Framework] - [Version] - [Purpose]

## Infrastructure
- [Service] - [Purpose]

## Dependencies
- [Key dependency] - [Version] - [Purpose]
```

## Step 5: Update State

Update `aidlc-docs/aidlc-state.md`:
- Mark Reverse Engineering as complete

## Step 6: Present Findings

```markdown
# Reverse Engineering Complete

[Summary of key findings in bullet points]

**Artifacts generated:**
- `aidlc-docs/inception/reverse-engineering/architecture.md`
- `aidlc-docs/inception/reverse-engineering/code-structure.md`
- `aidlc-docs/inception/reverse-engineering/technology-stack.md`

Does this look accurate? Any corrections before I proceed to Requirements Analysis?
```

## Step 7: Wait for Approval

- Wait for user to confirm or request corrections
- Once confirmed, proceed to Requirements Analysis
