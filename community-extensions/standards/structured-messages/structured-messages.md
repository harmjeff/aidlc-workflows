# Structured Messages Rules

## Overview
This extension provides consistent, visually structured completion messages for all workflow stages. Messages use a three-part format with emojis, blockquotes, and clear action prompts.

## Message Template

All stage completion messages must follow this three-part structure:

### Part 1: Completion Announcement (Mandatory)
Always start with this format:
```markdown
# [emoji] [Stage Name] Complete
```

**Stage-Specific Emojis:**
- Requirements Analysis: 🔍
- User Stories: 📚
- Workflow Planning: 📋
- Application Design: 🏗️
- Units Generation: 📦
- Functional Design: 🔧
- NFR Requirements: ⚡
- NFR Design: 🛡️
- Infrastructure Design: 🏛️
- Code Generation: 💻
- Build and Test: 🧪
- Operations: 🚀

### Part 2: AI Summary (Optional)
Provide structured bullet-point summary of artifacts created:
- Format: "[Stage] has [action] [description]:"
- Use bullet points for key items
- List artifacts, components, or decisions made
- Keep factual and content-focused
- **DO NOT include workflow instructions** like "please review", "let me know", "proceed to next phase", "before we proceed"
- No prescriptive language about what user should do next

**Example:**
```markdown
Requirements analysis has identified a microservices architecture:
• 5 functional requirements covering user management and data processing
• 3 non-functional requirements for security and performance
• Architectural decision: REST API with JWT authentication
```

### Part 3: Formatted Workflow Message (Mandatory)
Always end with this exact format:

```markdown
> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine [artifact description] at: `[file-path]`
[Additional file paths if applicable]



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to [artifacts] based on your review
[Additional contextual options if applicable]
> ✅ **[Approval Action]** - Approve [artifacts] and proceed to **[Next Stage]**

---
```

**Formatting Rules:**
- Use blockquotes (>) for both sections
- Use bold for section headers with underline tags: `<u>**HEADER:**</u>`
- File paths in inline code: \`path/to/file.md\`
- Action options with emoji bullets: 🔧 🔄 📝 ✅
- Bold for action labels: **Request Changes**, **Approve & Continue**
- Always end with horizontal rule: `---`
- Double line break between blockquote sections

## Stage Addendums

### Requirements Analysis Addendum
Present completion message in this structure:

```markdown
# 🔍 Requirements Analysis Complete

[AI Summary - optional]

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the requirements document at: `aidlc-docs/inception/requirements/requirements.md`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** -  Ask for modifications to the requirements if required based on your review
> [IF User Stories will be skipped, add:]
> 📝 **Add User Stories** - Choose to Include **User Stories** stage (currently skipped based on project simplicity)
> ✅ **Approve & Continue** - Approve requirements and proceed to **[User Stories/Workflow Planning]**

---
```

### User Stories Addendum
```markdown
# 📚 User Stories Complete

[AI Summary - optional]

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the user stories and personas at: `aidlc-docs/inception/user-stories/stories.md` and `aidlc-docs/inception/user-stories/personas.md`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** -  Ask for modifications to the stories or personas based on your review
> ✅ **Approve & Continue** - Approve user stories and proceed to **Workflow Planning**

---
```

### Workflow Planning Addendum
```markdown
# 📋 Workflow Planning Complete

[AI Summary - optional]

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the workflow plan at: `aidlc-docs/inception/workflow-planning.md`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the workflow plan
> ✅ **Approve & Continue** - Approve workflow plan and proceed to **[Next Stage]**

---
```

### Application Design Addendum
```markdown
# 🏗️ Application Design Complete

[AI Summary - optional]

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the application design artifacts at: `aidlc-docs/inception/application-design/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the application design if required
> [IF Units Generation is skipped:]
> 📝 **Add Units Generation** - Choose to include **Units Generation** stage (currently skipped)
> ✅ **Approve & Continue** - Approve design and proceed to **[Units Generation/CONSTRUCTION PHASE]**

---
```

### Functional Design Addendum (per-unit)
```markdown
# 🔧 Functional Design Complete - [unit-name]

[AI Summary - optional]

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the functional design artifacts at: `aidlc-docs/construction/[unit-name]/functional-design/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the functional design based on your review
> ✅ **Continue to Next Stage** - Approve functional design and proceed to **[next-stage-name]**

---
```

### NFR Requirements Addendum (per-unit)
```markdown
# ⚡ NFR Requirements Complete - [unit-name]

[AI Summary - optional]

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the NFR requirements at: `aidlc-docs/construction/[unit-name]/nfr-requirements/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the NFR requirements based on your review
> ✅ **Continue to Next Stage** - Approve NFR requirements and proceed to **[next-stage-name]**

---
```

### NFR Design Addendum (per-unit)
```markdown
# 🛡️ NFR Design Complete - [unit-name]

[AI Summary - optional]

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the NFR design at: `aidlc-docs/construction/[unit-name]/nfr-design/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the NFR design based on your review
> ✅ **Continue to Next Stage** - Approve NFR design and proceed to **[next-stage-name]**

---
```

### Infrastructure Design Addendum (per-unit)
```markdown
# 🏛️ Infrastructure Design Complete - [unit-name]

[AI Summary - optional]

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the infrastructure design at: `aidlc-docs/construction/[unit-name]/infrastructure-design/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the infrastructure design based on your review
> ✅ **Continue to Next Stage** - Approve infrastructure design and proceed to **[next-stage-name]**

---
```

### Code Generation Addendum (per-unit)
```markdown
# 💻 Code Generation Complete - [unit-name]

[AI Summary - optional]

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the generated code at:
> - **Application Code**: `[actual-workspace-path]`
> - **Documentation**: `aidlc-docs/construction/[unit-name]/code/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the generated code based on your review
> 🔄 **Generate Next Unit** - [IF more units] Continue to code generation for next unit: **[next-unit-name]**
> ✅ **Continue to Next Stage** - [IF last unit] Approve code and proceed to **Build and Test**

---
```

### Build and Test Addendum
```markdown
# 🧪 Build and Test Instructions Complete

[AI Summary - optional]

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the build and test instructions at: `aidlc-docs/construction/build-and-test/`



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** - Ask for modifications to the instructions based on your review
> ✅ **Approve & Continue** - Approve instructions and proceed to **Operations** (or complete workflow)

---
```

## Rules

### RULE-SM-01: Mandatory Three-Part Structure
**Rule**: All stage completion messages must follow the three-part structure: Completion Announcement + AI Summary (optional) + Formatted Workflow Message.

**Verification**:
- Part 1 is always present with correct emoji and format
- Part 3 is always present with blockquotes and action options
- Part 2 is included only when there's meaningful summary content

### RULE-SM-02: Consistent Formatting
**Rule**: All formatted elements (blockquotes, underlines, emojis, bold text) must be consistently applied according to the template.

**Verification**:
- Blockquotes used for REVIEW REQUIRED and WHAT'S NEXT
- Underline tags used for section headers
- File paths in inline code format
- Action options with emoji bullets
- Horizontal rule at the end

### RULE-SM-03: No Workflow Instructions in Summary
**Rule**: Part 2 (AI Summary) must be factual and content-focused. It must NOT include workflow instructions like "please review", "let me know", "proceed to", etc.

**Verification**:
- Summary describes what was created, not what user should do
- No imperative language in summary
- Workflow instructions only in Part 3 (Formatted Workflow Message)

### RULE-SM-04: Stage-Appropriate Action Options
**Rule**: Action options in "WHAT'S NEXT?" section must be appropriate for the current stage and workflow state.

**Verification**:
- "Request Changes" is always an option
- Conditional options (e.g., "Add User Stories") appear only when applicable
- "Approve & Continue" or "Continue to Next Stage" correctly identifies the next stage
- For per-unit stages, "Generate Next Unit" appears only if more units remain

## Quality Assurance Indicators

### Red Flags (Violations)
- Plain text completion messages without structure
- Missing blockquotes or formatting elements
- Workflow instructions in the AI Summary section
- Inconsistent emoji usage
- Missing "WHAT'S NEXT?" section

### Success Indicators (Compliance)
- All completion messages use three-part structure
- Consistent visual formatting across all stages
- Clear, actionable options for users
- Professional, polished presentation
- Easy to scan and understand at a glance
