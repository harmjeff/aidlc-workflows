# AI-DLC for Cline

AI-DLC is an intelligent software development workflow that adapts to your needs, maintains quality standards, and keeps you in control of the process. This guide shows how to set up AI-DLC with Cline.

## Prerequisites

- [Cline VS Code Extension](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev)
- VS Code or compatible editor

## Quick Start

Clone this repo:
```bash
git clone <this-repo>
```

Create a new project folder:

**Unix/Linux/macOS:**
```bash
mkdir <my-project>
cd <my-project>
```

**Windows PowerShell:**
```powershell
New-Item -ItemType Directory -Name "<my-project>"
Set-Location "<my-project>"
```

**Windows CMD:**
```cmd
mkdir <my-project>
cd <my-project>
```

### Cline Setup

AI-DLC uses Cline Rules to implement its intelligent workflow. To activate AI-DLC in your project with Cline, copy the rules to your project's workspace under the `<project-root>/.clinerules/` folder.

Copy the AI-DLC workflow to your project's workspace:

**Unix/Linux/macOS:**
```bash
# Copy the core workflow to .clinerules (loaded by Cline at startup)
mkdir -p .clinerules
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md .clinerules/

# Copy rule details to .aidlc-rule-details (loaded on-demand by the workflow)
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
# Copy the core workflow to .clinerules (loaded by Cline at startup)
New-Item -ItemType Directory -Force -Path ".clinerules"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".clinerules\"

# Copy rule details to .aidlc-rule-details (loaded on-demand by the workflow)
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
REM Copy the core workflow to .clinerules (loaded by Cline at startup)
mkdir .clinerules
copy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".clinerules\"

REM Copy rule details to .aidlc-rule-details (loaded on-demand by the workflow)
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

To confirm that the AI-DLC rules are correctly set up:

1. **Check file structure:**
   - `.clinerules/` should contain only `core-workflow.md` (loaded by Cline at startup)
   - `.aidlc-rule-details/` should contain subdirectories with detailed rule files (loaded on-demand)
2. **Verify in Cline:**
   - In Cline's chat interface, look for the Rules popover under the chat input field
   - Verify that `core-workflow.md` is listed and active
   - You can toggle the rule file on/off as needed using the popover UI

If you do not see the `core-workflow.md` rule loaded, please check the directory where you previously issued the `mkdir` and `cp` commands.

![AI-DLC Rules in Cline](./assets/images/cline-ide-aidlc-rules-loaded.png?raw=true "AI-DLC Rules in Cline")

**Why this separation?**
- Cline automatically loads all files in `.clinerules/` at startup
- The detailed rule files are large and would consume too many resources if all loaded at once
- The workflow dynamically loads only the rule details it needs from `.aidlc-rule-details/`
- This keeps Cline's startup lean while providing full functionality

## Alternative Setup: AGENTS.md Support

Cline also supports the AGENTS.md standard as a fallback. You can create a single AGENTS.md file in your project root:

**Unix/Linux/macOS:**
```bash
# Copy core workflow to AGENTS.md
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md ./AGENTS.md

# Copy rule details to .aidlc-rule-details (loaded on-demand by the workflow)
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
# Copy core workflow to AGENTS.md
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".\AGENTS.md"

# Copy rule details to .aidlc-rule-details (loaded on-demand by the workflow)
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
REM Copy core workflow to AGENTS.md
copy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".\AGENTS.md"

REM Copy rule details to .aidlc-rule-details (loaded on-demand by the workflow)
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

This allows you to use the same rules file across different AI coding tools. The rule details must still be copied to `.aidlc-rule-details/` for on-demand loading.

## Managing Rules

Cline v3.13+ includes a Rules popover UI accessible from the chat interface that allows you to:
- View active global and workspace rules
- Toggle specific rule files on/off
- Add new rule files to your workspace
- Manage different rule contexts easily

### Usage

1. Start any software development project by stating your intent starting with the phrase "Using AI-DLC, ..." in the chat
2. AI-DLC workflow automatically activates and guides you from there
3. Answer structured questions that AI-DLC asks you
4. Carefully review every plan that AI generates. Provide your oversight and validation
5. Review the execution plan to see which stages will run
6. Carefully review the artifacts and approve each stage to maintain control
7. All the artifacts will be generated in the `aidlc-docs/` directory

## Three-Phase Adaptive Workflow

AI-DLC follows a structured three-phase approach that adapts to your project's complexity:

- **🔵 INCEPTION PHASE**: Determines **WHAT** to build and **WHY**
  - Requirements analysis and validation
  - User story creation (when applicable)
  - Application Design and creating units of work for parallel development
  - Risk assessment and complexity evaluation

- **🟢 CONSTRUCTION PHASE**: Determines **HOW** to build it
  - Detailed component design
  - Code generation and implementation
  - Build configuration and testing strategies
  - Quality assurance and validation

- **🟡 OPERATIONS PHASE**: Deployment and monitoring (future)
  - Deployment automation and infrastructure
  - Monitoring and observability setup
  - Production readiness validation

## Key Features

- **Adaptive Intelligence**: Only executes stages that add value to your specific request
- **Context-Aware**: Analyzes existing codebase and complexity requirements
- **Risk-Based**: Complex changes get comprehensive treatment, simple changes stay efficient
- **Question-Driven**: Structured multiple-choice questions in files, not chat
- **Always in Control**: Review execution plans and approve each phase

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
