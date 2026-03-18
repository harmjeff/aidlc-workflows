# Workspace Detection

**Purpose**: Determine workspace state and check for existing AI-DLC Lite projects

## Step 1: Check for Existing AI-DLC Project

Check if `aidlc-docs/aidlc-state.md` exists:
- **If exists**: Resume from last stage (load context from previous stages)
- **If not exists**: Continue with new project assessment

## Step 2: Scan Workspace for Existing Code

**Determine if workspace has existing code:**
- Scan workspace for source code files (.java, .py, .js, .ts, .jsx, .tsx, .kt, .go, .rs, .rb, .php, .c, .cpp, .cs, etc.)
- Check for build files (pom.xml, package.json, build.gradle, etc.)
- Look for project structure indicators
- Identify workspace root directory (NOT aidlc-docs/)

**Record findings:**
```markdown
## Workspace State
- **Existing Code**: [Yes/No]
- **Programming Languages**: [List if found]
- **Build System**: [Maven/Gradle/npm/etc. if found]
- **Project Structure**: [Monolith/Microservices/Library/Empty]
- **Workspace Root**: [Absolute path]
```

## Step 3: Determine Next Stage

**IF workspace is empty (no existing code)**:
- Set flag: `brownfield = false`
- Next stage: Requirements Analysis

**IF workspace has existing code**:
- Set flag: `brownfield = true`
- Check for existing reverse engineering artifacts in `aidlc-docs/inception/reverse-engineering/`
- **IF reverse engineering artifacts exist**: Load them, skip to Requirements Analysis
- **IF no reverse engineering artifacts**: Next stage is Reverse Engineering

## Step 4: Create Initial State File

Create `aidlc-docs/aidlc-state.md`:

```markdown
# AI-DLC Lite State Tracking

## Project Information
- **Mode**: AI-DLC Lite
- **Project Type**: [Greenfield/Brownfield]
- **Start Date**: [ISO timestamp]
- **Current Stage**: INCEPTION - Workspace Detection
- **Workspace Root**: [Absolute path]

## Code Location Rules
- **Application Code**: Workspace root (NEVER in aidlc-docs/)
- **Documentation**: aidlc-docs/ only

## Stage Progress
### INCEPTION PHASE
- [x] Workspace Detection
- [ ] Reverse Engineering (if applicable)
- [ ] Requirements Analysis

### CONSTRUCTION PHASE
- [ ] Code Generation
- [ ] Build and Test
```

## Step 5: Present Completion Message

**For Brownfield Projects:**
```markdown
# Workspace Detection Complete

- **Project Type**: Brownfield project
- [Summary of workspace findings]
- **Next**: Proceeding to Reverse Engineering...
```

**For Greenfield Projects:**
```markdown
# Workspace Detection Complete

- **Project Type**: Greenfield project
- **Next**: Proceeding to Requirements Analysis...
```

## Step 6: Automatically Proceed

- **No user approval required** - this is informational only
- Automatically proceed to next stage
