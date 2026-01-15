# AI-DLC Workshop Installation Guide

This guide provides step-by-step instructions for setting up AI-DLC workflows in your development environment.

## Prerequisites

Have one of our supported platforms/tools for Assisted AI Coding installed:

| Platform | Installation Link |
|----------|------------------|
| Amazon Q Developer IDE Plugin | [Install](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html) |
| Kiro CLI | [Install](https://kiro.dev/cli/) |
| Kiro | [Install](https://kiro.dev/) |
| Cursor IDE | [Install](https://cursor.com/) |
| Cline VS Code Extension | [Install](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) |
| Claude Code CLI | [Install](https://github.com/anthropics/claude-code) |
| GitHub Copilot | [Install](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) + [Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) |

## Step 1: Clone this Repository

```bash
git clone <this-repo>
cd aidlc-workflows
```

## Step 2: Create a New Project Folder

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

## Step 3: Follow Platform-Specific Setup

Choose your platform below and follow the setup instructions.

---

## Platform-Specific Setup

### Amazon Q Developer IDE Plugin/Extension

AI-DLC uses [Amazon Q Rules](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/context-project-rules.html) to implement its intelligent workflow.

**Unix/Linux/macOS:**
```bash
mkdir -p .amazonq/rules 
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rules .amazonq/rules/ 
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
New-Item -ItemType Directory -Force -Path ".amazonq\rules"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules" ".amazonq\rules\" -Recurse
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
mkdir .amazonq\rules
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules" ".amazonq\rules\" /E /I
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

**Verify Setup:**
1. In the Amazon Q Chat window, locate the `Rules` button in the lower right corner
2. Verify that you see entries for `.amazonq/rules/aws-aidlc-rules` in the displayed list

---

### Kiro CLI (formerly Amazon Q CLI)

AI-DLC uses [Kiro Steering Files](https://kiro.dev/docs/cli/steering/) to implement its intelligent workflow.

**Unix/Linux/macOS:**
```bash
mkdir -p .kiro/steering
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rules .kiro/steering/
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
New-Item -ItemType Directory -Force -Path ".kiro\steering"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules" ".kiro\steering\" -Recurse
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
mkdir .kiro\steering
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules" ".kiro\steering\" /E /I
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

**Verify Setup:**
1. Start Kiro CLI: `kiro-cli`
2. Check your context contents: `/context show`
3. Verify that you see all entries for `.kiro/steering/aws-aidlc-rules`

---

### Cursor IDE

AI-DLC uses [Cursor Rules](https://cursor.com/docs/context/rules) to implement its intelligent workflow.

#### Option 1: Project Rules (Recommended)

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

#### Option 2: AGENTS.md (Simple Alternative)

**Unix/Linux/macOS:**
```bash
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md ./AGENTS.md
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".\AGENTS.md"
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
copy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".\AGENTS.md"
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

**Verify Setup:**
1. Open **Cursor Settings → Rules, Commands**
2. Under **Project Rules**, you should see `ai-dlc-workflow` listed
3. For `AGENTS.md`, it will be automatically detected and applied

---

### Cline

AI-DLC uses Cline Rules to implement its intelligent workflow.

#### Option 1: .clinerules Directory (Recommended)

**Unix/Linux/macOS:**
```bash
mkdir -p .clinerules
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md .clinerules/
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
New-Item -ItemType Directory -Force -Path ".clinerules"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".clinerules\"
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
mkdir .clinerules
copy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".clinerules\"
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

#### Option 2: AGENTS.md (Alternative)

**Unix/Linux/macOS:**
```bash
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md ./AGENTS.md
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".\AGENTS.md"
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
copy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".\AGENTS.md"
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

**Verify Setup:**
1. In Cline's chat interface, look for the Rules popover under the chat input field
2. Verify that `core-workflow.md` is listed and active
3. You can toggle the rule file on/off as needed

---

### Claude Code

AI-DLC uses Claude Code's project memory file (`CLAUDE.md`) to implement its intelligent workflow.

#### Option 1: Project Root (Recommended)

**Unix/Linux/macOS:**
```bash
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md ./CLAUDE.md
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".\CLAUDE.md"
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
copy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".\CLAUDE.md"
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

#### Option 2: .claude Directory

**Unix/Linux/macOS:**
```bash
mkdir -p .claude
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md .claude/CLAUDE.md
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
New-Item -ItemType Directory -Force -Path ".claude"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".claude\CLAUDE.md"
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
mkdir .claude
copy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".claude\CLAUDE.md"
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

**Verify Setup:**
1. Start Claude Code in your project directory (CLI: `claude` or VS Code extension)
2. Use the `/config` command to view current configuration
3. Ask Claude: "What instructions are currently active in this project?"

---

### GitHub Copilot

AI-DLC uses project context files and Copilot's Chat capabilities to implement its intelligent workflow.

#### Option 1: .copilot Directory (Recommended)

**Unix/Linux/macOS:**
```bash
mkdir -p .copilot
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md .copilot/instructions.md
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
New-Item -ItemType Directory -Force -Path ".copilot"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".copilot\instructions.md"
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
mkdir .copilot
copy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".copilot\instructions.md"
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

#### Option 2: Project Root COPILOT.md

**Unix/Linux/macOS:**
```bash
cp ../aidlc-workflows/aidlc-rules/aws-aidlc-rules/core-workflow.md ./COPILOT.md
mkdir -p .aidlc-rule-details
cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details/* .aidlc-rule-details/
```

**Windows PowerShell:**
```powershell
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".\COPILOT.md"
New-Item -ItemType Directory -Force -Path ".aidlc-rule-details"
Copy-Item "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details\*" ".aidlc-rule-details\" -Recurse
```

**Windows CMD:**
```cmd
copy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rules\core-workflow.md" ".\COPILOT.md"
mkdir .aidlc-rule-details
xcopy "..\aidlc-workflows\aidlc-rules\aws-aidlc-rule-details" ".aidlc-rule-details\" /E /I
```

**Verify Setup:**
1. Open VS Code with your project folder
2. Open the Copilot Chat panel (Cmd/Ctrl+Shift+I)
3. Reference the instructions by typing `#file .copilot/instructions.md` or `#file COPILOT.md` in the chat

---

## Step 4: Verify Installation

After completing platform-specific setup, verify your installation:

1. **Check Directory Structure**: Ensure you have:
   - Platform-specific rules directory (`.amazonq/rules/`, `.kiro/steering/`, `.cursor/rules/`, etc.)
   - `.aidlc-rule-details/` directory with subdirectories:
     - `common/`
     - `inception/`
     - `construction/`
     - `operations/`

2. **Test AI-DLC Activation**: 
   - Start a new chat session in your AI coding assistant
   - Begin with: **"Using AI-DLC, I want to [describe your project]"**
   - The AI should respond with the AI-DLC welcome message and begin the workflow

3. **Verify Rules Loading**:
   - Check that your platform recognizes the rules files
   - For Amazon Q/Kiro: Use `/context show` command
   - For Cursor: Check Settings → Rules
   - For Cline: Check Rules popover in chat interface

---

## Troubleshooting

### Rules Not Loading
- **Check file paths**: Ensure files are in the correct location for your platform
- **File encoding**: Ensure files are UTF-8 encoded
- **Restart session**: Start a new chat session after file changes

### Rule Details Not Loading
- **Verify directory structure**: Check that `.aidlc-rule-details/` exists with all subdirectories
- **Check file permissions**: Ensure files are readable

### Platform-Specific Issues

#### Amazon Q Developer / Kiro CLI
- Use `/context show` to verify rules are loaded
- Check `.amazonq/rules/` or `.kiro/steering/` directory structure

#### Cursor
- Check **Cursor Settings → Rules** to ensure the rule is enabled
- If rule is too large (>500 lines), consider splitting into multiple focused rules

#### Cline
- Check the Rules popover under the chat input field
- Toggle rule files on/off as needed using the popover UI

#### Claude Code
- Use `/config` command to view current configuration
- Ask "What instructions are currently active in this project?"

#### GitHub Copilot
- Use `#file <path>` syntax to reference instruction files
- For large instructions, reference specific rule detail files instead of pasting everything

---

## Next Steps

Once installation is complete, proceed to:
- **2-Day Workshop**: See `workshop/01-workshop-2day.md`
- **5-Day Workshop**: See `workshop/02-workshop-5day.md`
- **Phase Instructions**: See `workshop/phase-instructions/` directory

---

## Additional Resources

| Resource | Link |
|----------|------|
| AI-DLC Methodology Blog | [AWS Blog](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) |
| AI-DLC Method Definition Paper | [Paper](https://prod.d13rzhkk8cj2z0.amplifyapp.com/) |
| Contributing Guidelines | [CONTRIBUTING.md](../CONTRIBUTING.md) |
| Code of Conduct | [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) |
