# Welcome Message Extension

Displays a friendly welcome message at the start of any AI-DLC workflow, introducing users to the process and setting expectations.

---

## What It Does

This extension adds a comprehensive welcome message that:
- Explains what AI-DLC is and how it works
- Shows the three-phase lifecycle with visual diagram
- Describes each phase's purpose and activities
- Outlines key principles and user's role
- Sets expectations for what happens next

**Without this extension:** AI-DLC starts directly with Workspace Detection without introduction.

**With this extension:** Users see a welcoming introduction to the AI-DLC process before work begins.

---

## When to Use

Install this extension if:
- You have team members new to AI-DLC
- You want users to understand the workflow upfront
- You're onboarding users to the AI-DLC methodology
- You prefer a more guided, educational experience
- You're running AI-DLC in interactive mode with humans

Skip this extension if:
- Your team already knows AI-DLC well
- You're running AI-DLC in automation/CI environments
- You prefer to get straight to work without preamble
- You want to minimize initial output/context
- You're using AI-DLC programmatically

---

## Installation

Copy the rule files into your project's extensions directory:

### Kiro
```bash
mkdir -p .kiro/aws-aidlc-rule-details/extensions/standards/welcome-message
cp community-extensions/standards/welcome-message/welcome-message.md .kiro/aws-aidlc-rule-details/extensions/standards/welcome-message/
cp community-extensions/standards/welcome-message/welcome-message.opt-in.md .kiro/aws-aidlc-rule-details/extensions/standards/welcome-message/
```

### Amazon Q Developer
```bash
mkdir -p .amazonq/aws-aidlc-rule-details/extensions/standards/welcome-message
cp community-extensions/standards/welcome-message/welcome-message.md .amazonq/aws-aidlc-rule-details/extensions/standards/welcome-message/
cp community-extensions/standards/welcome-message/welcome-message.opt-in.md .amazonq/aws-aidlc-rule-details/extensions/standards/welcome-message/
```

### Cursor / Cline / Claude Code / GitHub Copilot
```bash
mkdir -p .aidlc-rule-details/extensions/standards/welcome-message
cp community-extensions/standards/welcome-message/welcome-message.md .aidlc-rule-details/extensions/standards/welcome-message/
cp community-extensions/standards/welcome-message/welcome-message.opt-in.md .aidlc-rule-details/extensions/standards/welcome-message/
```

Then start a new AI-DLC session. During Workspace Detection, you'll be asked whether to display the welcome message.

---

## What Changes

### Workflow Start
- A comprehensive welcome message is displayed before Workspace Detection
- Message explains AI-DLC, the three phases, and what to expect
- Includes visual workflow diagram
- Only shown once per project (not on session resumption)

---

## Trade-offs

**Advantages:**
- Better onboarding for new users
- Clear expectations set upfront
- Educational about the process
- More welcoming and guided experience

**Disadvantages:**
- Additional output at workflow start
- Uses context space for introduction
- May be unnecessary for experienced users
- Not suitable for automation contexts
