# Workspace Detection

**Purpose**: Determine workspace state and select the project type that governs the workflow.

## Step 1: Check for Existing AI-DLC Project

Check if `aidlc-docs/aidlc-state.md` exists:
- **If exists**: Resume from last phase (load context from previous phases)
- **If not exists**: Continue with new project assessment

## Step 2: Scan Workspace for Existing Code and Resources

**Scan for existing source code:**
- Source files (.java, .py, .js, .ts, .jsx, .tsx, .kt, .kts, .scala, .groovy, .go, .rs, .rb, .php, .c, .h, .cpp, .hpp, .cc, .cs, .fs, etc.)
- Build files (pom.xml, package.json, build.gradle, etc.)
- Project structure indicators
- Identify workspace root directory (NOT aidlc-docs/)

**Scan for external resource documentation:**
- `aidlc-docs/external-resources/` directory and its contents

**Record findings:**
```markdown
## Workspace Scan
- **Existing Source Code**: [Yes/No]
- **Languages Detected**: [List if found]
- **Build System**: [Maven/Gradle/npm/etc. if found]
- **Project Structure**: [Monolith/Microservices/Library/Empty]
- **External Resource Docs**: [Yes/No — files found in aidlc-docs/external-resources/]
- **Workspace Root**: [Absolute path]
```

## Step 3: Build and Present Project Type Question

**Scan `extensions/project-type/`** for installed extension folders. For each folder found, read the `## Project Type Registration` section of its rules file (`*.md`, excluding README.md) to get the **Option Label**, **Description**, and **Workspace Signal**.

**Build the question dynamically:**
- Option A is always **Greenfield** — new project, no existing code or external resource constraints (built-in, no extension required)
- Additional lettered options come from installed project-type extensions, sorted alphabetically by Option Label
- Always include a final "Other" option

**Pre-populate the suggested answer** using each extension's Workspace Signal:
- If a signal matches the workspace scan, note it as the suggested answer in the question file

If no project-type extensions are installed, skip this question and proceed directly as Greenfield.

Create `aidlc-docs/inception/workspace-detection-questions.md`:

```markdown
# Project Type Selection

Based on the workspace scan, please confirm your project type.
[If a suggestion applies, note it here: "Suggested: [Option X] based on [signal detected]"]

## Question 1
What best describes this project?

A) Greenfield — new project with no existing code or external resource constraints
[B... dynamically added from installed extensions, one per letter]
[Last letter]) Other (please describe after [Answer]: tag below)

[Answer]:
```

**MANDATORY**: Present the question file to the user and STOP. Do not proceed until the question is answered.

## Step 4: Load Extension and Set Project Type

**If the user selected Greenfield (A):**
- Set project type: `Greenfield`
- No extension to load
- Next stage: Requirements Analysis

**If the user selected an extension-backed option:**
- Read the extension's rules file to get its Option Label and Pre-Requirements Stage
- Set project type: the extension's Option Label
- Load the extension's rules file
- Execute any setup checks defined in the extension (e.g., checking for required input files) before proceeding
- Next stage: the Pre-Requirements Stage defined in the extension

**If the user selected Other or described a project type with no matching installed extension:**
- Inform the user: "The project type you described may require an extension that isn't installed. Check `community-extensions/project-type/` for available project-type extensions, install the appropriate one, and start a new session to reload the rules."
- Do not proceed until the extension is installed and the session is restarted

**If a Workspace Signal was detected but no matching extension is installed:**
- Note this in the question file suggestion (e.g., "Existing source code detected — a project-type extension may be needed")
- Let the user choose; if they select a type requiring a missing extension, apply the rule above

## Step 5: Create Initial State File

Create `aidlc-docs/aidlc-state.md`:

```markdown
# AI-DLC State Tracking

## Project Information
- **Project Type**: [Greenfield / Brownfield / Greyfield]
- **Start Date**: [ISO timestamp]
- **Current Stage**: INCEPTION - Workspace Detection
- **Active Extensions**: [brownfield / greyfield / none]

## Workspace State
- **Existing Source Code**: [Yes/No]
- **External Resource Docs**: [Yes/No]
- **Workspace Root**: [Absolute path]

## Code Location Rules
- **Application Code**: Workspace root (NEVER in aidlc-docs/)
- **Documentation**: aidlc-docs/ only
- **Structure patterns**: See code-generation.md Critical Rules

## Stage Progress
[Will be populated as workflow progresses]
```

## Step 6: Present Completion Message

```markdown
# Workspace Detection Complete

- **Project Type**: [Selected project type]
- **Active Extension**: [Extension name, or "none" for Greenfield]
- [AI-generated summary of relevant workspace findings in bullet points]
- **Next Step**: Proceeding to **[Pre-Requirements Stage name from extension, or "Requirements Analysis" for Greenfield]**...
```

## Step 7: Log and Proceed

- Log findings and user's project type selection in `aidlc-docs/audit.md`
- Automatically proceed to the next stage for the selected project type (no further user gate)
