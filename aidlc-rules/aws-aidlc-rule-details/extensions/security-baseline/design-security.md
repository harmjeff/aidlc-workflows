## Security Baseline - Secure Design Principles

**Extension**: security-baseline v1.0.0
**Applies To**: Functional Design Stage

---

### Secure Design Patterns to Follow

#### Input Validation

- [ ] **Validate all input**: Never trust user input, API parameters, or external data
- [ ] **Allowlist over denylist**: Define what IS allowed rather than what is NOT
- [ ] **Validate at boundaries**: Perform validation at system entry points
- [ ] **Type-safe parsing**: Use strong typing for all external data

#### Authentication & Authorization

- [ ] **Principle of least privilege**: Grant minimum necessary permissions
- [ ] **Defense in depth**: Multiple layers of security controls
- [ ] **Fail secure**: Default to deny access on errors
- [ ] **Separation of concerns**: Keep auth logic separate from business logic

#### Data Protection

- [ ] **Encrypt sensitive data**: At rest and in transit
- [ ] **Minimize data exposure**: Only collect/store necessary data
- [ ] **Secure deletion**: Properly sanitize data when deleted
- [ ] **Audit logging**: Log security-relevant events (without sensitive data)

---

### Anti-Patterns to Avoid

#### ❌ Security Anti-Patterns

| Anti-Pattern | Why It's Bad | What to Do Instead |
|--------------|--------------|-------------------|
| Hardcoded secrets | Secrets in code get committed to repos | Use environment variables or secret managers |
| SQL string concatenation | SQL injection vulnerability | Use parameterized queries/prepared statements |
| Eval/exec of user input | Remote code execution | Never execute user-provided strings |
| Storing passwords in plaintext | Data breach exposure | Use bcrypt, Argon2, or similar hashing |
| Verbose error messages | Information disclosure | Return generic errors to users, log details internally |
| Disabling SSL verification | Man-in-the-middle attacks | Always verify SSL certificates |
| Using deprecated crypto | Weak encryption can be broken | Use modern algorithms (AES-256, SHA-256+) |

#### ❌ Common Vulnerable Patterns

```
# AVOID: String interpolation in queries
query = f"SELECT * FROM users WHERE id = {user_id}"

# AVOID: Hardcoded credentials
password = "admin123"

# AVOID: Disabling security checks
verify_ssl = False

# AVOID: Exec/eval of external input
eval(user_input)
```

---

### Design Review Checklist

Before finalizing design, verify:

- [ ] All external inputs have defined validation rules
- [ ] Authentication/authorization boundaries are clearly defined
- [ ] Sensitive data flows are documented and protected
- [ ] Error handling doesn't leak sensitive information
- [ ] Logging strategy excludes sensitive data (passwords, tokens, PII)
- [ ] Third-party integrations use secure communication
- [ ] Secrets management approach is defined

---

*This content is provided by the security-baseline extension.*