# PR Title

Add AI-DLC methodology as Agent Skill format

# PR Description

## What

This PR adds the AI-DLC (AI-Driven Development Life Cycle) methodology in the Agent Skills format, making it compatible with multiple editors and tools that support the specification.

## Why

The AI-DLC methodology was originally built as a Kiro Power. Converting it to the Agent Skills format brings portability and broader compatibility:

- **Editor Agnostic**: Works with any editor supporting the Agent Skills spec (Claude Desktop, Cursor, Windsurf, etc.)
- **Portable**: Same methodology works across different development environments
- **Version Controlled**: Development process changes tracked like code
- **Team Shareable**: Consistent practices distributed across organizations

## What's Included

```
skills/ai-dlc-methodology/
├── SKILL.md              # Main skill file with metadata and overview
└── references/           # Detailed workflow documentation
    ├── core-workflow.md  # Complete workflow rules
    ├── common/           # Shared guidelines (10 files)
    ├── inception/        # Planning phase steps (7 files)
    ├── construction/     # Implementation phase steps (6 files)
    └── operations/       # Deployment phase placeholder (1 file)
```

## Compatibility

This skill follows the [Agent Skills specification](https://agentskills.io) and works with any editor implementing the standard.

## About AI-DLC

AI-DLC is an adaptive software development methodology that tailors its workflow based on project complexity. Simple bug fixes get minimal process, while complex system migrations get comprehensive treatment with quality gates and documentation.

Three phases:
- **Inception**: Planning and architecture (WHAT and WHY)
- **Construction**: Design and implementation (HOW)
- **Operations**: Deployment and monitoring (placeholder for future)
