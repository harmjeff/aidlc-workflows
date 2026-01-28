## Security Baseline - Security Testing Requirements

**Extension**: security-baseline v1.0.0
**Applies To**: Build and Test Stage

---

### Security Testing Requirements

#### 1. Static Application Security Testing (SAST)

**SAST tools MUST be integrated into CI/CD pipeline:**

##### Tool Configuration by Language

| Language | Primary SAST Tool | Command |
|----------|-------------------|---------|
| JavaScript/TypeScript | ESLint + Semgrep | `npx eslint . && semgrep --config auto` |
| Python | Bandit + Semgrep | `bandit -r src/ && semgrep --config auto` |
| Java | SpotBugs + FindSecBugs | `mvn spotbugs:check` |
| Go | gosec | `gosec ./...` |
| C# | Security Code Scan | `dotnet build /p:EnableNETAnalyzers=true` |
| Multi-language | SonarQube, Semgrep | `sonar-scanner` or `semgrep ci` |

##### CI/CD Integration Example (GitHub Actions)

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: auto
          
      - name: Run language-specific SAST
        run: |
          # Add language-specific commands here
```

---

#### 2. Dependency Vulnerability Scanning

**All dependencies MUST be scanned for known vulnerabilities:**

##### Tool Commands by Ecosystem

| Ecosystem | Tool | Command |
|-----------|------|---------|
| npm/Node.js | npm audit | `npm audit --audit-level=high` |
| Python | pip-audit, Safety | `pip-audit` or `safety check` |
| Java (Maven) | OWASP Dependency-Check | `mvn dependency-check:check` |
| Java (Gradle) | OWASP Dependency-Check | `gradle dependencyCheckAnalyze` |
| Go | govulncheck | `govulncheck ./...` |
| .NET | dotnet CLI | `dotnet list package --vulnerable` |
| Container | Trivy | `trivy image myapp:latest` |

##### CI/CD Integration Example

```yaml
# GitHub Actions - Dependency Scanning
- name: Run npm audit
  run: npm audit --audit-level=high
  
- name: Run Trivy vulnerability scanner
  uses: aquasecurity/trivy-action@master
  with:
    scan-type: 'fs'
    severity: 'CRITICAL,HIGH'
    exit-code: '1'
```

---

#### 3. Security Test Requirements

##### Pre-Merge Security Gates

- [ ] **SAST scan passes** with zero critical/high findings
- [ ] **Dependency scan passes** with zero critical vulnerabilities
- [ ] **Linting passes** with all security rules enabled
- [ ] **Secrets scan passes** (no hardcoded secrets detected)

##### Secrets Detection

```yaml
# Pre-commit hook for secrets detection
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
        
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

---

### Security Testing Checklist

#### Build Phase
- [ ] SAST tool integrated and configured
- [ ] Linting with security rules runs on every build
- [ ] Build fails on critical/high security findings

#### Test Phase
- [ ] Dependency vulnerability scan runs on every build
- [ ] Secrets detection runs on every commit (pre-commit hook)
- [ ] Container images scanned for vulnerabilities (if applicable)

#### CI/CD Pipeline
- [ ] Security scans block PR merges on failures
- [ ] Security reports generated and archived
- [ ] Dependency updates automated (Dependabot, Renovate)

---

### Security Scan Failure Thresholds

| Severity | Action Required |
|----------|-----------------|
| **Critical** | MUST fix before merge - blocks pipeline |
| **High** | MUST fix before merge - blocks pipeline |
| **Medium** | SHOULD fix - may be deferred with documented justification |
| **Low** | MAY fix - track in backlog |

### Suppressing False Positives

When legitimate findings need to be suppressed:

1. Document the reason in code comments or configuration
2. Get security team approval for suppressions
3. Track suppressions in security baseline document
4. Review suppressions periodically

```python
# Example: Bandit suppression with documentation
password = get_password_from_vault()  # nosec B105 - Not hardcoded, retrieved from vault
```

---

*This content is provided by the security-baseline extension.*