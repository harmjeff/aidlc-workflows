# Security Baseline Extension

## Purpose

This extension establishes baseline code security rules for linting, static analysis, and security scanning. It provides consistent security practices across all projects regardless of programming language or framework.

## What This Extension Provides

### Design Phase
- Security-first design principles
- Secure coding patterns to follow
- Anti-patterns to avoid

### Code Generation Phase
- Language-specific linting configurations
- Secure coding guidelines
- Input validation patterns
- Error handling security considerations
- Dependency security requirements

### Testing Phase
- Static Application Security Testing (SAST) integration
- Dependency vulnerability scanning
- Security-focused code review checklist
- CI/CD security gate recommendations

## When to Use This Extension

**Recommended for:**
- All production applications
- Any application handling user data
- APIs and web services
- Backend services
- Libraries published for external use

**May not be necessary for:**
- Proof-of-concept projects
- Internal-only documentation tools
- One-time scripts

## Key Security Tools Referenced

| Category | Tools |
|----------|-------|
| **JavaScript/TypeScript** | ESLint (security plugins), npm audit, Snyk |
| **Python** | Bandit, Safety, pylint, Ruff |
| **Java** | SpotBugs, FindSecBugs, OWASP Dependency-Check |
| **Go** | gosec, staticcheck, govulncheck |
| **General** | SonarQube, Semgrep, Trivy, Dependabot |

## Integration with AI-DLC Workflow

This extension automatically adds security considerations to:
1. **NFR Requirements** - Security tool selection and configuration requirements
2. **Functional Design** - Secure design patterns and anti-patterns
3. **Code Generation** - Language-specific secure coding guidelines
4. **Build and Test** - Security scanning and testing requirements

---

*Extension: security-baseline v1.0.0*