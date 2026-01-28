# AI-DLC Extensions: Why They Matter

## The Problem

AI-assisted development tools work best when given domain-specific context. Without guidance, AI models generate generic solutions that miss critical requirements:

- **Security vulnerabilities** slip through when security rules aren't explicitly provided
- **Compliance violations** occur when regulatory requirements aren't part of the conversation
- **Inconsistent quality** results when teams don't have shared standards encoded in their tooling
- **Reinventing the wheel** happens when best practices aren't systematically applied

Every team has specific standards, but manually pasting guidelines into every AI session is:
- Time-consuming
- Error-prone
- Inconsistently applied
- Hard to maintain across a team

## The Solution: AI-DLC Extensions

Extensions are **modular, reusable rule packages** that automatically inject domain-specific guidance into the AI-DLC workflow at the right moments.

```
┌─────────────────────────────────────────────────────────────────┐
│                    How Extensions Work                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   User Request                                                  │
│        │                                                        │
│        ▼                                                        │
│   ┌─────────────────────────────────────────┐                   │
│   │          AI-DLC Core Workflow           │                   │
│   │                                         │                   │
│   │  Design → Code → Test                   │                   │
│   │    ▲        ▲       ▲                   │                   │
│   │    │        │       │                   │                   │
│   │  ┌─┴────────┴───────┴─┐                 │                   │
│   │  │     Extensions     │                 │                   │
│   │  │  ┌───────────────┐ │                 │                   │
│   │  │  │ security-owasp│ │ ← "Add auth"    │                   │
│   │  │  │ compliance-pci│ │ ← "Encrypt"     │                   │
│   │  │  │ process-tdd   │ │ ← "Test first"  │                   │
│   │  │  └───────────────┘ │                 │                   │
│   │  └────────────────────┘                 │                   │
│   └─────────────────────────────────────────┘                   │
│        │                                                        │
│        ▼                                                        │
│   Generated Code + Tests + Docs                                 │
│   (with security, compliance, and process rules applied)        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Key Benefits

| Benefit | Without Extensions | With Extensions |
|---------|-------------------|-----------------|
| **Consistency** | Each session starts from scratch | Standards automatically applied |
| **Completeness** | Easy to forget requirements | Checklists ensure nothing missed |
| **Expertise** | Requires manual expert input | Expert knowledge encoded in rules |
| **Auditability** | No record of standards used | Extensions document what was applied |
| **Shareability** | Knowledge stays in individuals | Team standards in version control |

## Example: Security Without vs. With Extensions

### Without `security-baseline` Extension:
```
User: "Build a user login API"
AI: [generates basic login endpoint]
     - No input validation mentioned
     - No SQL injection prevention discussed
     - No security linting configured
     - No SAST integration planned
```

### With `security-baseline` Extension:
```
User: "Build a user login API"
AI: [generates secure login endpoint]
     ✓ Input validation with schema (Zod/Pydantic)
     ✓ Parameterized queries (no SQL injection)
     ✓ ESLint security rules configured
     ✓ Bandit SAST scan in CI/CD
     ✓ Secrets detection pre-commit hook
     ✓ Generic error messages (no info disclosure)
```

## Extension Categories

| Category | Purpose | Example Extensions |
|----------|---------|-------------------|
| **Security** | Secure coding, threat modeling | `security-baseline`, `security-owasp` |
| **Compliance** | Regulatory requirements | `compliance-hipaa`, `compliance-pci` |
| **Process** | Development methodology | `process-tdd`, `process-bdd` |
| **Quality** | Code quality standards | `quality-coverage`, `quality-docs` |
| **Architecture** | Architectural frameworks | `aws-well-architected`, `12-factor` |

## How to Use Extensions

### 1. Enable During Workflow Planning
Extensions are offered based on project characteristics:
```markdown
🔌 Suggested Extensions:
- [x] security-baseline - Linting & static analysis
- [ ] compliance-hipaa - Healthcare data handling
```

### 2. Pre-enable for All Projects
Create `aidlc-docs/enabled-extensions.md`:
```markdown
# Enabled Extensions
- security-baseline
- quality-coverage
```

### 3. Create Custom Extensions
See `EXTENSION-AUTHORING-GUIDE.md` for creating team-specific rules.

## Getting Started

1. **Use existing extensions**: Enable `security-baseline` on your next project
2. **Browse available extensions**: Check `.aidlc-rule-details/extensions/_registry.md`
3. **Create your own**: Follow `EXTENSION-AUTHORING-GUIDE.md` to encode your team's standards

---

*Extensions transform AI-DLC from a generic development assistant into a knowledgeable team member that understands your organization's specific requirements.*