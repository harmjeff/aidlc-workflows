## SECURITY_BASELINE_RULES

Cross-cutting constraints. Apply across all AI-DLC phases. Hard constraints, not guidance.

## BLOCKING_FINDING_BEHAVIOR

blocking finding:
1. List in stage completion under "Security Findings" with SECURITY rule ID + description
2. Do NOT present "Continue to Next Stage" until all blocking findings resolved
3. Present only "Request Changes" with explanation
4. Log in `aidlc-docs/audit.md` with SECURITY rule ID, description, stage context

not-applicable rule (e.g., SECURITY-01 when no data stores) → mark N/A in compliance summary, not blocking

All rules blocking by default. Verification criteria not met → blocking finding.

Verification items: plain bullet compliance checks (distinct from `- [ ]`/`- [x]` progress checkboxes).

## SECURITY-01: ENCRYPTION_AT_REST_AND_IN_TRANSIT

[REQ] Every data persistence store (databases, object storage, file systems, caches):
- Encryption at rest: managed key service or customer-managed keys
- Encryption in transit: TLS 1.2+ for all data movement

Verification:
- No storage resource without encryption configuration
- No unencrypted database connection protocol
- Object storage enforces encryption at rest, rejects non-TLS via policy
- Database instances: storage encryption enabled, TLS enforced

## SECURITY-02: ACCESS_LOGGING_NETWORK_INTERMEDIARIES

[REQ] Every network-facing intermediary handling external traffic:
- Load balancers → access logs to persistent store
- API gateways → execution + access logging to centralized log service
- CDN distributions → standard or real-time logs

Verification:
- No load balancer without access logging
- No API gateway stage without access logging
- No CDN distribution without logging configuration

## SECURITY-03: APPLICATION_LEVEL_LOGGING

[REQ] Every deployed application component:
- Logging framework configured
- Output to centralized log service
- Include: timestamp, correlation/request ID, log level, message
- Sensitive data (passwords, tokens, PII) MUST NOT appear in logs

Verification:
- Every service/function entry point has configured logger
- No ad-hoc logging as primary mechanism in production
- Log config routes to centralized service
- No secrets/tokens/PII logged

## SECURITY-04: HTTP_SECURITY_HEADERS

[REQ] All HTML-serving endpoints set these headers:

| Header | Required Value |
|---|---|
| `Content-Security-Policy` | Restrictive policy (min: `default-src 'self'`) |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` |
| `X-Content-Type-Options` | `nosniff` |
| `X-Frame-Options` | `DENY` (or `SAMEORIGIN` if framing required) |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |

`X-XSS-Protection` deprecated. Use CSP instead.

Verification:
- Middleware/interceptor sets all required headers
- CSP: no `unsafe-inline`/`unsafe-eval` without documented justification
- HSTS max-age >= 31536000

## SECURITY-05: INPUT_VALIDATION

[REQ] Every API endpoint (REST, GraphQL, gRPC, WebSocket) validates all input:
- Type checking: reject unexpected types
- Length/size bounds: max lengths on strings, max sizes on arrays/payloads
- Format validation: allowlists (regex/schema) for structured inputs
- Sanitization: escape/reject HTML/script in user strings (XSS prevention)
- Injection prevention: parameterized queries only (never string concatenation)

Verification:
- Every API handler uses validation library/schema
- No raw user input concatenated into SQL/NoSQL/OS commands
- String inputs have explicit max-length
- Request body size limits configured

## SECURITY-06: LEAST_PRIVILEGE_ACCESS

[REQ] Every IAM policy/role/permission boundary:
- Specific resource identifiers (no wildcard resources unless API lacks resource-level permissions — document exception)
- Specific actions (no wildcard actions)
- Scope conditions where possible
- Separate read/write into distinct statements

Verification:
- No wildcard actions/resources without documented exception
- No role with broader permissions than actual calls
- Prefer managed policies over inline
- Trust policy scoped to specific service/account

## SECURITY-07: RESTRICTIVE_NETWORK_CONFIG

[REQ] All network configs (security groups, NACLs, route tables) deny-by-default:
- Only open specific required ports
- No inbound `0.0.0.0/0` except public LB on 80/443
- No outbound `0.0.0.0/0` all ports without justification
- Private subnets: no direct internet gateway routes
- Use private endpoints for cloud service access where available

Verification:
- No inbound `0.0.0.0/0` on any port other than 80/443 on public LB
- DB/app firewall rules restrict source to specific CIDR/security group
- Private subnets route through NAT (not IGW)
- Private endpoints for high-traffic cloud service calls

## SECURITY-08: APPLICATION_ACCESS_CONTROL

[REQ] Every endpoint accessing/mutating resources:
- Deny by default: all routes require auth unless explicitly public
- Object-level authorization: verify caller owns/has permission for resource ID (prevent IDOR)
- Function-level authorization: admin/privileged ops check role server-side
- CORS: restricted to allowed origins (no `*` on authenticated endpoints)
- Token validation: JWTs/sessions validated server-side every request (signature, expiration, audience, issuer)

Verification:
- Every handler has auth middleware/guard
- No endpoint returns data without verifying caller permission
- Admin routes have explicit server-side role checks
- CORS: no wildcard on authenticated endpoints
- Token validation server-side every request

## SECURITY-09: HARDENING_MISCONFIGURATION_PREVENTION

[REQ] All deployed components:
- No default credentials before deployment
- Remove/disable unused features, sample apps, doc endpoints
- Production errors: no stack traces, internal paths, framework versions, DB details
- Web servers: disable directory listing
- Cloud storage: block public access unless documented exception
- Runtime/frameworks/OS: current supported versions

Verification:
- No default credentials in config/env/IaC
- Production error responses: generic messages only
- Cloud storage: public access blocked unless documented
- No sample/demo apps deployed
- Current supported versions

## SECURITY-10: SUPPLY_CHAIN_SECURITY

[REQ] Every project:
- Dependency pinning: exact versions or lock files
- Vulnerability scanning configured
- No unused dependencies
- Trusted sources only: official/verified registries
- SBOM for production deployments
- CI/CD integrity: pinned tool versions, verified base images (no `latest` in production)

Verification:
- Lock file committed
- Vulnerability scanning in CI/CD or documented
- No unused/abandoned dependencies
- No `latest`/unpinned image tags in production
- Official/verified registry sources

## SECURITY-11: SECURE_DESIGN_PRINCIPLES

[REQ] Application design:
- Separation of concerns: security-critical logic (auth, authz, payments) in dedicated modules
- Defense in depth: layer controls (validation + authorization + encryption)
- Rate limiting on public-facing endpoints
- Design addresses misuse cases, not just happy-path

Verification:
- Security logic encapsulated in dedicated modules/services
- Rate limiting on public APIs
- Design docs address at least one misuse/abuse scenario

## SECURITY-12: AUTHENTICATION_CREDENTIAL_MANAGEMENT

[REQ] Every app with user auth:
- Password policy: min 8 chars, check against breached lists
- Credential storage: adaptive hashing algorithms (never weak/non-adaptive)
- MFA: supported for admin accounts, should be available for all users
- Session management: server-side expiration, invalidated on logout, secure/httpOnly/sameSite cookies
- Brute-force protection: lockout, progressive delays, or CAPTCHA
- No hardcoded credentials: use secrets manager

Verification:
- Adaptive password hashing
- Session cookies: `Secure`, `HttpOnly`, `SameSite`
- Brute-force protection on login
- No hardcoded credentials in source/config
- MFA for admin accounts
- Sessions invalidated on logout with defined expiration

## SECURITY-13: SOFTWARE_DATA_INTEGRITY

[REQ] Systems verify integrity:
- Deserialization safety: no untrusted deserialization without validation (safe libraries/allowlists)
- Artifact integrity: verify downloads via checksums/signatures
- CI/CD pipeline security: restrict pipeline definition modification, separate code authors from deployment approvers
- CDN/external resources: SRI hashes
- Data integrity: critical modifications auditable (who, what, when)

Verification:
- No unsafe deserialization of untrusted input
- External scripts include SRI integrity attributes
- CI/CD definitions access-controlled and auditable
- Critical data changes logged with actor, timestamp, before/after

## SECURITY-14: ALERTING_AND_MONITORING

[REQ] Beyond logging (SECURITY-02, SECURITY-03):
- Security event alerting: repeated auth failures, privilege escalation, unusual access locations, authz failures
- Log integrity: append-only/tamper-evident storage; app code cannot delete/modify own audit logs
- Log retention: min period per compliance (default 90 days)
- Monitoring dashboard/alarm config for key operational + security metrics

Verification:
- Alerting for auth failures and authz violations
- Log retention policies set (min 90 days)
- App roles cannot delete own log groups/streams
- Security events generate alerts

## SECURITY-15: EXCEPTION_HANDLING_FAIL_SAFE

[REQ] Every application:
- Catch and handle: all external calls (DB, API, file I/O) have explicit error handling
- Fail closed: on error, deny access/halt operation (never fail open)
- Resource cleanup: error paths release resources (try/finally, using, equivalent)
- User-facing errors: generic messages only
- Global error handler: catches unhandled exceptions, logs per SECURITY-03, returns safe response

Verification:
- All external calls have explicit error handling
- Global error handler at app entry point
- Error paths do not bypass auth/validation (fail closed)
- Resources cleaned up in error paths
- No unhandled promise rejections/uncaught exceptions

## ENFORCEMENT_INTEGRATION

At each stage:
- Evaluate all SECURITY rule verification criteria against produced artifacts
- Include "Security Compliance" section in stage completion: each rule as compliant, non-compliant, or N/A
- non-compliant → blocking finding → follow blocking behavior
- Include security rule references in design docs and test instructions

## OWASP_REFERENCE_MAPPING

| SECURITY Rule | OWASP Category |
|---|---|
| SECURITY-08 | A01:2025 Broken Access Control |
| SECURITY-09 | A02:2025 Security Misconfiguration |
| SECURITY-10 | A03:2025 Software Supply Chain Failures |
| SECURITY-11 | A06:2025 Insecure Design |
| SECURITY-12 | A07:2025 Authentication Failures |
| SECURITY-13 | A08:2025 Software or Data Integrity Failures |
| SECURITY-14 | A09:2025 Logging & Alerting Failures |
| SECURITY-15 | A10:2025 Mishandling of Exceptional Conditions |
