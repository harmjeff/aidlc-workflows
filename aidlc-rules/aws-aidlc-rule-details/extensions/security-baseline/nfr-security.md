## Security Baseline - NFR Security Requirements

**Extension**: security-baseline v1.0.0
**Applies To**: NFR Requirements Stage

---

### Security Tooling Requirements

#### Static Analysis (SAST) Requirements

- [ ] **Linting Configuration**: Project MUST include language-appropriate linting with security rules enabled
- [ ] **Static Analysis Tool**: Project MUST integrate at least one SAST tool in CI/CD pipeline
- [ ] **Threshold Configuration**: Define acceptable thresholds for security findings (zero critical/high)

#### Dependency Security Requirements

- [ ] **Dependency Scanning**: Project MUST scan dependencies for known vulnerabilities
- [ ] **Update Policy**: Define policy for addressing vulnerable dependencies (e.g., within 7 days for critical)
- [ ] **Lock Files**: Use lock files to ensure reproducible, auditable dependency resolution

#### Code Quality Gates

- [ ] **Pre-commit Hooks**: Security checks SHOULD run before code commits
- [ ] **PR/MR Checks**: Security scans MUST pass before merge approval
- [ ] **Main Branch Protection**: Security failures MUST block merges to main/production branches

### Security Tool Recommendations by Language

| Language | Linter | SAST | Dependency Scan |
|----------|--------|------|-----------------|
| JavaScript/TypeScript | ESLint + eslint-plugin-security | Semgrep, SonarQube | npm audit, Snyk |
| Python | Ruff, pylint | Bandit, Semgrep | Safety, pip-audit |
| Java | Checkstyle, PMD | SpotBugs + FindSecBugs | OWASP Dependency-Check |
| Go | staticcheck | gosec | govulncheck |
| C# | StyleCop | Security Code Scan | dotnet list package --vulnerable |
| Rust | Clippy | cargo-audit | cargo-deny |

### Additional Security Questions

If not already captured in requirements, consider:

**Question SEC-1**: What is the target security classification for this application?
- A) Public-facing, handles sensitive user data
- B) Internal application with authenticated users
- C) Internal tool with no sensitive data
- D) Development/test tooling only

[Answer]: 

**Question SEC-2**: Are there compliance requirements that mandate specific security controls?
- A) Yes - regulatory (HIPAA, PCI-DSS, SOC2, GDPR)
- B) Yes - organizational security policies
- C) No specific compliance requirements
- D) Unknown - needs clarification

[Answer]: 

---

*This content is provided by the security-baseline extension.*