# Security Baseline Extension

Enforces a baseline set of security rules across all AI-DLC stages. When enabled, each stage cannot complete until its applicable security rules are verified compliant.

---

## What It Covers

15 security rules (SECURITY-01 through SECURITY-15) spanning:

- Encryption at rest and in transit
- Access and network logging
- Structured application logging
- HTTP security headers
- Input validation and injection prevention
- Least-privilege IAM policies
- Restrictive network configuration
- Application-level access control (IDOR prevention)
- Security hardening and misconfiguration prevention
- Software supply chain security
- Secure design principles (rate limiting, defense in depth)
- Authentication and credential management
- Software and data integrity verification
- Security alerting and monitoring
- Exception handling and fail-safe defaults

Rules are mapped to OWASP Top 10 (2025) in the rules file.

---

## How It Works

This extension uses the standard AI-DLC opt-in mechanism. When installed, it presents a question during Requirements Analysis asking whether to enforce security rules for this project. If the user opts in, every stage completion is gated on security rule compliance. Non-compliance is a blocking finding — the stage cannot proceed until resolved.

Suitable for production-grade applications. Can be skipped for prototypes and PoCs.

---

## Installing This Extension

Copy `security-baseline.md` and `security-baseline.opt-in.md` into your project's extensions directory.

**Kiro:**
```bash
mkdir -p .kiro/aws-aidlc-rule-details/extensions/security/baseline
cp security-baseline.md security-baseline.opt-in.md .kiro/aws-aidlc-rule-details/extensions/security/baseline/
```

**Amazon Q Developer:**
```bash
mkdir -p .amazonq/aws-aidlc-rule-details/extensions/security/baseline
cp security-baseline.md security-baseline.opt-in.md .amazonq/aws-aidlc-rule-details/extensions/security/baseline/
```

**Cursor / Cline / Claude Code / GitHub Copilot:**
```bash
mkdir -p .aidlc-rule-details/extensions/security/baseline
cp security-baseline.md security-baseline.opt-in.md .aidlc-rule-details/extensions/security/baseline/
```

Then start a new AI-DLC session. During Requirements Analysis you will be asked whether to enforce security rules for this project.
