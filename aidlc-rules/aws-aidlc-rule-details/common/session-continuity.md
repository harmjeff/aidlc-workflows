# Session Continuity - Lite

## Welcome Back Prompt
When a user returns to continue work on an existing AI-DLC Lite project, present this prompt:

```markdown
**Welcome back! I can see you have an existing AI-DLC Lite project in progress.**

Based on your aidlc-state.md, here's your current status:
- **Project**: [project-name]
- **Current Stage**: [Stage Name]
- **Last Completed**: [Last completed step]
- **Next Step**: [Next step to work on]

Would you like to continue where you left off, or start fresh?
```

## Session Continuity Instructions
1. **Always read aidlc-state.md first** when detecting existing project
2. **Load Previous Artifacts** - Before resuming, read relevant artifacts:
   - **Reverse Engineering** (if brownfield): Read architecture.md, code-structure.md, technology-stack.md
   - **Requirements**: Read requirements.md
   - **Code Generation**: Read all generated code files
3. **Provide brief summary** of what was loaded for user awareness
4. **Proceed from where the user left off**
