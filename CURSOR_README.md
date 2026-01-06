# AI-DLC for Cursor

AI-DLC is an intelligent software development workflow that adapts to your needs, maintains quality standards, and keeps you in control of the process. This guide shows how to set up AI-DLC with Cursor.

## Prerequisites

- [Cursor IDE](https://cursor.com/)
- VS Code or compatible editor (Cursor is built on VS Code)

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

### Cursor Setup

AI-DLC uses [Cursor Rules](https://cursor.com/docs/context/rules) to implement its intelligent workflow. Cursor supports multiple rule formats:

1. **Project Rules** (Recommended): Stored in `.cursor/rules/` as `.mdc` files with YAML frontmatter
2. **AGENTS.md**: A simple markdown file in the project root

We'll set up both options for maximum compatibility.

#### Option 1: Project Rules (Recommended)

Project Rules provide the most flexibility with metadata, scoping, and rule types. Copy the AI-DLC workflow to your project's workspace:

**Unix/Linux/macOS:**
```bash
# Create .cursor/rules directory
mkdir -p .cursor/rules

# Create .mdc file with frontmatter and workflow content
cat > .cursor/rules/ai-dlc-workflow.mdc << 'EOF'
---
description: "AI-DLC (AI-Driven Development Life Cycle) adaptive workflow for software development"
alwaysApply: true
---

EOF
cat ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md >> .cursor/rules/ai-dlc-workflow.mdc

# Copy rule details to .aidlc-rule-details (loaded on-demand by the workflow)
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
# Create .cursor/rules directory
New-Item -ItemType Directory -Force -Path ".cursor\rules"

# Create frontmatter and write to .mdc file
$frontmatter = @"
---
description: "AI-DLC (AI-Driven Development Life Cycle) adaptive workflow for software development"
alwaysApply: true
---

"@
$frontmatter | Out-File -FilePath ".cursor\rules\ai-dlc-workflow.mdc" -Encoding utf8

# Append core workflow content to .mdc file
Get-Content "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" | Add-Content ".cursor\rules\ai-dlc-workflow.mdc"

# Copy rule details to .aidlc-rule-details (loaded on-demand by the workflow)
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
REM Create .cursor/rules directory
mkdir .cursor\rules

REM Create frontmatter in .mdc file
(
echo ---
echo description: "AI-DLC (AI-Driven Development Life Cycle) adaptive workflow for software development"
echo alwaysApply: true
echo ---
echo.
) > .cursor\rules\ai-dlc-workflow.mdc

REM Append core workflow content to .mdc file
type "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" >> .cursor\rules\ai-dlc-workflow.mdc

REM Copy rule details to .aidlc-rule-details (loaded on-demand by the workflow)
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

**Understanding `.mdc` Files:**

- **File Extension**: `.mdc` (Markdown with Cursor metadata)
- **Format**: YAML frontmatter (between `---` markers) followed by markdown content
- **Location**: Place directly in `.cursor/rules/` directory (no subfolders needed)
- **Metadata**: Use YAML frontmatter to configure rule behavior

**Rule Type Options:**

- **`alwaysApply: true`** (Recommended): Applies to every chat session, ensuring AI-DLC is always active
- **`alwaysApply: false`**: Agent decides when to apply based on the description
- **`globs: ['**/*.ts', '**/*.js']`**: Apply only when working with specific file patterns
- Manual application: Use `@ai-dlc-workflow` in chat to invoke manually

#### Option 2: AGENTS.md (Simple Alternative)

For simpler setups, you can use `AGENTS.md` as a single markdown file:

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

**Note:** `AGENTS.md` is a plain markdown file without metadata. It's automatically applied when present in the project root or subdirectories.

### Verifying Setup

To confirm that the AI-DLC rules are correctly set up:

1. **Check file structure:**
   - **Project Rules**: `.cursor/rules/ai-dlc-workflow.mdc` should exist
   - **AGENTS.md**: `AGENTS.md` should exist in project root (if using Option 2)
   - `.aidlc-rule-details/` should contain subdirectories with detailed rule files (loaded on-demand)

2. **Verify in Cursor:**
   - Open **Cursor Settings → Rules, Commands**
   - Under **Project Rules**, you should see `ai-dlc-workflow` listed
   - Check the rule status (Always Apply, Apply Intelligently, etc.)
   - For `AGENTS.md`, it will be automatically detected and applied

3. **Test in Chat:**
   - Start a chat session in Cursor
   - Type: "Using AI-DLC, create a simple hello world application"
   - The workflow should activate and guide you through the process

![AI-DLC Rules in Cursor](./assets/images/cursor-ide-aidlc-rules-loaded.png?raw=true "AI-DLC Rules in Cursor")

### Why This Structure?

**Separation of Concerns:**
- **Core Workflow** (`.cursor/rules/ai-dlc-workflow.mdc` or `AGENTS.md`): Main workflow logic loaded by Cursor
- **Rule Details** (`.aidlc-rule-details/`): Detailed stage-specific instructions loaded on-demand
- This keeps Cursor's context lean while providing full functionality when needed

**Benefits:**
- **Project Rules**: Support metadata, scoping, and rule types for fine-grained control
- **AGENTS.md**: Simple, readable, and automatically applied
- **On-demand loading**: Detailed rules are only loaded when needed, saving context tokens
- **Version controlled**: All rules are part of your repository

## Best Practices for Cursor Rules

Based on [Cursor's official documentation](https://cursor.com/docs/context/rules) and community best practices:

### 1. Keep Rules Focused and Actionable

- Keep individual rules under 500 lines
- Split large rules into multiple, composable rules
- Provide concrete examples or referenced files
- Avoid vague guidance - write rules like clear internal documentation

### 2. Use Appropriate Rule Types

- **Always Apply**: For critical workflows like AI-DLC that should always be active
- **Apply Intelligently**: For domain-specific knowledge that's contextually relevant
- **Apply to Specific Files**: For file-pattern-specific guidelines (e.g., `['**/*.test.ts']`)
- **Apply Manually**: For optional workflows invoked with `@rule-name`

### 3. Modular Structure

For larger projects, create modular rules aligned with your code structure:

```bash
.cursor/rules/
  ├── ai-dlc-workflow.mdc        # Main AI-DLC workflow
  ├── frontend-standards.mdc     # Frontend-specific rules (globs: ['src/frontend/**'])
  ├── backend-standards.mdc      # Backend-specific rules (globs: ['src/backend/**'])
  └── api-standards.mdc          # API-specific rules (globs: ['src/api/**'])
```

### 4. Reference Files and Templates

Use `@filename.ts` to include files in your rule's context:

```yaml
---
description: "Use this template for Express services"
globs: ['src/services/**']
---

Follow this template when creating Express services:

@express-service-template.ts
```

### 5. Maintain Up-to-Date Documentation

- Regularly update rules to reflect current project decisions
- Include ticket IDs or issue references for traceability
- Document architectural decisions and their rationale

### 6. Rule Precedence

Cursor applies rules in this order (earlier sources take precedence):
1. **Team Rules** (if on Team/Enterprise plan)
2. **Project Rules** (`.cursor/rules/`)
3. **User Rules** (global settings)
4. **AGENTS.md** (project root or subdirectories)

## Managing Rules

### Viewing and Editing Rules

1. Open **Cursor Settings → Rules, Commands**
2. View all project rules and their status
3. Edit rules directly from the settings UI
4. Toggle rules on/off as needed

### Creating New Rules

1. Use the **New Cursor Rule** command (Cmd/Ctrl+Shift+P)
2. Or go to **Cursor Settings → Rules, Commands → + Add Rule**
3. Choose rule type and configure metadata
4. Cursor creates the `.mdc` file with YAML frontmatter automatically

### Importing Rules

You can import rules from external sources:

1. **Remote Rules (GitHub)**: Import from any GitHub repository
   - Go to **Cursor Settings → Rules, Commands**
   - Click `+ Add Rule` → **Remote Rule (Github)**
   - Paste the GitHub repository URL
   - Rules stay synced with the source repository

2. **Agent Skills**: Enable specialized capabilities from the Agent Skills standard
   - Go to **Cursor Settings → Rules → Import Settings**
   - Toggle **Agent Skills** on or off

## Usage

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

## Troubleshooting

### Rule Not Being Applied

1. **Check rule type**: For "Apply Intelligently", ensure a description is defined
2. **Check file patterns**: For "Apply to Specific Files", ensure the file pattern matches referenced files
3. **Verify rule status**: Check **Cursor Settings → Rules** to ensure the rule is enabled
4. **Check precedence**: Team Rules take precedence over Project Rules

### Rule Too Large

If your rule exceeds 500 lines:
- Split into multiple focused rules
- Move detailed instructions to `.aidlc-rule-details/` for on-demand loading
- Use file references (`@filename`) instead of inline content

### AGENTS.md Not Detected

- Ensure `AGENTS.md` is in the project root or relevant subdirectory
- Restart Cursor if the file was just created
- Check that the file is not in `.gitignore`

## Additional Resources

- [Cursor Rules Documentation](https://cursor.com/docs/context/rules)
- [Cursor Agent Skills](https://cursor.com/docs/context/skills)
- [AI-DLC Methodology Blog](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)
- [AI-DLC Method Definition Paper](https://prod.d13rzhkk8cj2z0.amplifyapp.com/)

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

