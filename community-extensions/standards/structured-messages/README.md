# Structured Messages Extension

Provides polished, consistently formatted completion messages with emojis, visual structure, and clear action prompts for all workflow stages.

---

## What It Does

This extension transforms stage completion messages from simple text to structured, visually appealing formats:
- **Consistent structure**: Three-part message format (Announcement + Summary + Workflow Prompt)
- **Visual enhancement**: Emojis, blockquotes, underlines, and formatting
- **Clear action prompts**: Structured "REVIEW REQUIRED" and "WHAT'S NEXT?" sections
- **User-friendly presentation**: Easy-to-scan, branded messaging

**Without this extension:** AI-DLC uses plain, simple completion messages ("Stage complete. Please review X. Approve to continue").

**With this extension:** AI-DLC presents polished, structured messages with consistent formatting and clear visual hierarchy.

---

## When to Use

Install this extension if:
- You want a polished, professional user experience
- Your team appreciates visual structure and emojis
- You're working in interactive mode with human users
- You value consistent, branded messaging
- Clear action prompts improve your team's workflow

Skip this extension if:
- You prefer minimal, plain text output
- You're using AI-DLC in automation/CI environments
- You want to minimize output formatting overhead
- You find emojis and visual formatting distracting
- You're integrating AI-DLC output into other tools

---

## Installation

Copy the rule files into your project's extensions directory:

### Kiro
```bash
mkdir -p .kiro/aws-aidlc-rule-details/extensions/standards/structured-messages
cp community-extensions/standards/structured-messages/structured-messages.md .kiro/aws-aidlc-rule-details/extensions/standards/structured-messages/
cp community-extensions/standards/structured-messages/structured-messages.opt-in.md .kiro/aws-aidlc-rule-details/extensions/standards/structured-messages/
```

### Amazon Q Developer
```bash
mkdir -p .amazonq/aws-aidlc-rule-details/extensions/standards/structured-messages
cp community-extensions/standards/structured-messages/structured-messages.md .amazonq/aws-aidlc-rule-details/extensions/standards/structured-messages/
cp community-extensions/standards/structured-messages/structured-messages.opt-in.md .amazonq/aws-aidlc-rule-details/extensions/standards/structured-messages/
```

### Cursor / Cline / Claude Code / GitHub Copilot
```bash
mkdir -p .aidlc-rule-details/extensions/standards/structured-messages
cp community-extensions/standards/structured-messages/structured-messages.md .aidlc-rule-details/extensions/standards/structured-messages/
cp community-extensions/standards/structured-messages/structured-messages.opt-in.md .aidlc-rule-details/extensions/standards/structured-messages/
```

Then start a new AI-DLC session. During Workspace Detection, you'll be asked whether to enable structured message formatting.

---

## What Changes

### All Stage Completion Messages
Transforms completion messages to use a three-part structure:

1. **Completion Announcement**: Emoji + stage name (e.g., "# 🔍 Requirements Analysis Complete")

2. **AI Summary** (optional): Factual bullet-point summary of what was created

3. **Formatted Workflow Message**:
   - "REVIEW REQUIRED" section with file paths
   - "WHAT'S NEXT?" section with clear action options
   - Consistent emoji usage and formatting

### Example Transformation

**Without Extension** (plain):
```
Requirements Analysis complete. Please review requirements.md. Approve to continue to next stage.
```

**With Extension** (structured):
```
# 🔍 Requirements Analysis Complete

Requirements analysis has identified [summary]:
• Key functional requirements
• Non-functional requirements
• Technical decisions

> **📋 REVIEW REQUIRED:**
> Please examine the requirements document at: `aidlc-docs/inception/requirements/requirements.md`

> **🚀 WHAT'S NEXT?**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the requirements
> ✅ **Approve & Continue** - Approve requirements and proceed to Workflow Planning
```

---

## Formatting Standards

- **Emojis**: Consistent stage-specific emojis (🔍 Requirements, 📚 Stories, 🏗️ Design, 💻 Code, etc.)
- **Blockquotes**: Used for REVIEW REQUIRED and WHAT'S NEXT sections
- **Underlines**: Used for section headers (implemented with `<u>` tags)
- **Bullet points**: Used for summaries and action options
- **File paths**: Formatted as inline code with backticks

---

## Trade-offs

**Advantages:**
- More polished, professional presentation
- Easier to scan and understand at a glance
- Consistent visual language throughout workflow
- Clear action prompts reduce ambiguity
- Better user experience for interactive sessions

**Disadvantages:**
- More verbose output
- May not suit automation contexts
- Formatting can be distracting for some users
- Harder to parse programmatically
- Additional characters in output
