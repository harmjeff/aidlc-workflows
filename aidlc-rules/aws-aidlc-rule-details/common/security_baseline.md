# Security Baseline Rules for AI-DLC

## Purpose

**Universal secure coding standards to steer AI-generated code towards secure-by-default outcomes across all AI-DLC phases.** This baseline integrates security best practices from OWASP Top 10 for LLMs, AWS Well-Architected Security Pillar, and OpenSSF (Open Source Security Foundation) guidelines to prevent common vulnerabilities throughout the software development lifecycle.

**Note**: This file provides foundational security guidance applicable to ALL projects. For project-specific security rules addressing known findings, see your project's dedicated security rules document.

---

## CRITICAL: Security-First Development Mandate

**MANDATORY**: All AI-DLC phases MUST incorporate security controls before proceeding to the next phase. Security is NOT optional and MUST NOT be retrofitted after code generation.

### Core Security Principles

1. **Secure by Default**: Default configurations MUST be secure; insecure options require explicit opt-in
2. **Defense in Depth**: Implement multiple layers of security controls at infrastructure, application, and data levels
3. **Least Privilege**: Grant minimum permissions necessary for functionality
4. **Input Validation**: Validate and sanitize ALL external inputs before processing
5. **Fail Securely**: Errors and exceptions MUST fail to a secure state, never exposing sensitive information
6. **Zero Trust**: Never trust, always verify - authenticate and authorize every request

---

## OWASP Top 10 for LLMs - Prevention Rules

### LLM01: Prompt Injection Prevention

**CRITICAL**: When building LLM-powered applications:

**Validation Rules**:
- [ ] Separate user input from system prompts using delimiters or structured formats
- [ ] Implement input sanitization to remove potential injection patterns
- [ ] Use allowlists for expected input formats rather than denylists
- [ ] Apply privilege separation - limit LLM access to sensitive operations
- [ ] Monitor and log unusual prompt patterns for security review

**Implementation Pattern**:
```python
# CORRECT: Structured input with clear boundaries
system_prompt = "You are a helpful assistant. Process the following user query within these constraints: [CONSTRAINTS]"
user_input = sanitize_input(raw_user_input)  # Remove injection patterns
llm_request = {
    "system": system_prompt,
    "user": user_input,  # Clearly separated
    "max_tokens": 500,
    "temperature": 0.7
}

# FORBIDDEN: Direct concatenation
# prompt = f"{system_instruction} {raw_user_input}"  # VULNERABLE
```

---

### LLM02: Insecure Output Handling

**CRITICAL**: LLM outputs MUST be treated as untrusted and validated before use.

**Validation Rules**:
- [ ] Sanitize LLM outputs before rendering in UI (prevent XSS)
- [ ] Validate outputs before executing as code or system commands
- [ ] Apply output encoding appropriate to context (HTML, JSON, SQL)
- [ ] Implement content security policies for web applications
- [ ] Never execute LLM-generated code without human review and sandboxing

**Implementation Pattern**:
```python
# CORRECT: Validate and sanitize output
llm_output = get_llm_response(prompt)
sanitized_output = html.escape(llm_output)  # Prevent XSS
validated_output = validate_against_schema(sanitized_output)

# FORBIDDEN: Direct execution or rendering
# exec(llm_output)  # NEVER execute raw LLM output
# render_html(llm_output)  # NEVER render without sanitization
```

---

### LLM03: Training Data Poisoning Awareness

**When using fine-tuned models or RAG systems**:

**Validation Rules**:
- [ ] Verify training data sources and provenance
- [ ] Implement data validation pipelines for training datasets
- [ ] Monitor model outputs for bias or malicious patterns
- [ ] Use version control for training datasets
- [ ] Document data lineage and transformations

---

### LLM06: Sensitive Information Disclosure

**CRITICAL**: Prevent leakage of sensitive data through LLM interactions.

**Validation Rules**:
- [ ] Never include secrets, credentials, or PII in prompts
- [ ] Implement data masking for sensitive information
- [ ] Use separate models for different data classification levels
- [ ] Log and monitor for accidental sensitive data exposure
- [ ] Apply data loss prevention (DLP) controls on outputs

**Implementation Pattern**:
```python
# CORRECT: Mask sensitive data before LLM processing
def process_customer_query(customer_data):
    masked_data = {
        "customer_id": customer_data["id"],
        "issue_type": customer_data["issue"],
        # Sensitive fields masked
        "email": "***@***.com",
        "phone": "***-***-" + customer_data["phone"][-4:],
        "account": "****" + customer_data["account"][-4:]
    }
    return llm_process(masked_data)

# FORBIDDEN: Sending raw sensitive data
# llm_process(customer_data)  # May expose PII
```

---

### LLM08: Excessive Agency Prevention

**When LLMs can perform actions**:

**Validation Rules**:
- [ ] Implement human-in-the-loop for high-risk actions
- [ ] Restrict LLM permissions to minimum necessary
- [ ] Use allowlists for permitted actions
- [ ] Implement rate limiting on LLM-triggered operations
- [ ] Audit and log all LLM-initiated actions

---

### LLM09: Overreliance - Validation Required

**MANDATORY**: Always validate LLM outputs before critical decisions.

**Validation Rules**:
- [ ] Implement verification steps for LLM recommendations
- [ ] Never use LLM outputs for security decisions without validation
- [ ] Provide confidence scores and uncertainty indicators
- [ ] Require human review for high-stakes decisions
- [ ] Test LLM outputs against known-good test cases

---

## AWS Well-Architected Security Pillar - Implementation Rules

### Identity and Access Management (IAM)

**CRITICAL**: Implement least privilege access controls at all levels.

**Validation Rules**:
- [ ] Use IAM roles instead of long-term credentials
- [ ] Apply principle of least privilege to all IAM policies
- [ ] Enable MFA for human users and privileged operations
- [ ] Rotate credentials regularly (max 90 days)
- [ ] Use IAM policy conditions to restrict access by IP, time, or MFA
- [ ] Never use root account for daily operations
- [ ] Audit IAM policies quarterly for excessive permissions

**Implementation Pattern**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::specific-bucket/specific-prefix/*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        },
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    }
  ]
}
```

**FORBIDDEN Patterns**:
```json
// NEVER use wildcards for production
{
  "Effect": "Allow",
  "Action": "*",  // TOO BROAD
  "Resource": "*"  // TOO BROAD
}
```

---

### Detection and Response

**CRITICAL**: Implement comprehensive logging and monitoring.

**Validation Rules**:
- [ ] Enable AWS CloudTrail in all regions and accounts
- [ ] Configure AWS Config for configuration compliance monitoring
- [ ] Set up CloudWatch alarms for security events
- [ ] Enable VPC Flow Logs for network monitoring
- [ ] Implement centralized log aggregation
- [ ] Configure automated incident response playbooks
- [ ] Enable GuardDuty for threat detection

**Logging Requirements**:
- ALL API calls must be logged (CloudTrail)
- ALL authentication attempts must be logged
- ALL authorization failures must be logged
- ALL configuration changes must be logged
- Logs must be immutable and centrally stored
- Log retention minimum 90 days (1 year recommended)

---

### Infrastructure Protection

**CRITICAL**: Implement defense in depth for infrastructure.

**Validation Rules**:
- [ ] Use VPCs with private subnets for application tiers
- [ ] Implement security groups with least privilege rules
- [ ] Use AWS WAF for web application protection
- [ ] Enable AWS Shield for DDoS protection
- [ ] Implement network segmentation and isolation
- [ ] Use AWS Systems Manager Session Manager instead of SSH/RDP
- [ ] Enable encryption in transit (TLS 1.2+) for all communications

**Implementation Pattern**:
```python
# CORRECT: Defense in depth with multiple layers
vpc = ec2.Vpc(self, "SecureVPC",
    max_azs=3,
    nat_gateways=3,
    subnet_configuration=[
        ec2.SubnetConfiguration(
            name="Public",
            subnet_type=ec2.SubnetType.PUBLIC,
            cidr_mask=24
        ),
        ec2.SubnetConfiguration(
            name="Private",
            subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
            cidr_mask=24
        ),
        ec2.SubnetConfiguration(
            name="Isolated",
            subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
            cidr_mask=24
        )
    ]
)

# Application in private subnet
app_security_group = ec2.SecurityGroup(
    self, "AppSG",
    vpc=vpc,
    description="Application security group",
    allow_all_outbound=False  # Explicit egress rules
)

# Only allow specific inbound traffic
app_security_group.add_ingress_rule(
    peer=alb_security_group,
    connection=ec2.Port.tcp(8080),
    description="Allow traffic from ALB only"
)
```

---

### Data Protection

**CRITICAL**: Encrypt data at rest and in transit.

**Validation Rules**:
- [ ] Enable encryption at rest for all data stores (S3, EBS, RDS, DynamoDB)
- [ ] Use AWS KMS for key management with automatic rotation
- [ ] Enable encryption in transit (TLS 1.2+) for all communications
- [ ] Implement data classification and handling procedures
- [ ] Use AWS Secrets Manager or Parameter Store for secrets
- [ ] Enable S3 bucket versioning and MFA delete for critical data
- [ ] Implement backup and recovery procedures with encryption

**Implementation Pattern**:
```python
# CORRECT: Encryption at rest and in transit
bucket = s3.Bucket(
    self, "DataBucket",
    encryption=s3.BucketEncryption.KMS,  # Customer-managed key
    encryption_key=kms_key,
    enforce_ssl=True,  # CRITICAL: Enforce TLS
    versioned=True,
    block_public_access=s3.BlockPublicAccess.BLOCK_ALL
)

# Database with encryption
database = rds.DatabaseInstance(
    self, "Database",
    engine=rds.DatabaseInstanceEngine.postgres(),
    storage_encrypted=True,  # CRITICAL
    storage_encryption_key=kms_key,
    deletion_protection=True,
    backup_retention=Duration.days(30)
)

# FORBIDDEN: Unencrypted storage
# bucket = s3.Bucket(self, "Bucket")  # No encryption specified
```

---

## OpenSSF (Open Source Security Foundation) Baseline

### Secure Software Development Fundamentals

**CRITICAL**: Follow secure development lifecycle practices.

**Validation Rules**:
- [ ] Implement threat modeling for new features
- [ ] Conduct security design reviews before implementation
- [ ] Perform code reviews with security focus
- [ ] Use static application security testing (SAST) tools
- [ ] Implement dynamic application security testing (DAST)
- [ ] Perform software composition analysis (SCA) for dependencies
- [ ] Maintain software bill of materials (SBOM)

---

### Dependency Management

**CRITICAL**: Manage third-party dependencies securely.

**Validation Rules**:
- [ ] Pin dependency versions explicitly (no wildcards in production)
- [ ] Scan dependencies for known vulnerabilities (CVEs)
- [ ] Update dependencies regularly (monthly minimum)
- [ ] Verify package integrity using checksums/signatures
- [ ] Use package managers with security scanning (npm audit, pip-audit)
- [ ] Implement automated dependency update PRs
- [ ] Review dependency licenses for compliance

**Implementation Pattern**:
```python
# requirements.txt - CORRECT: Pinned versions with hashes
boto3==1.34.0 \
    --hash=sha256:abc123...
requests==2.31.0 \
    --hash=sha256:def456...

# package.json - CORRECT: Exact versions
{
  "dependencies": {
    "express": "4.18.2",  // Exact version
    "helmet": "7.1.0"
  }
}

# FORBIDDEN: Wildcards in production
# "dependencies": {
#   "express": "^4.0.0",  // Too permissive
#   "helmet": "*"  // NEVER use wildcards
# }
```

**Automated Scanning**:
```yaml
# .github/workflows/security.yml
name: Security Scan
on: [push, pull_request]
jobs:
  dependency-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run dependency scan
        run: |
          npm audit --audit-level=high
          pip-audit --strict
```

---

### Supply Chain Security

**CRITICAL**: Verify software supply chain integrity.

**Validation Rules**:
- [ ] Verify digital signatures of downloaded packages
- [ ] Use trusted package registries only
- [ ] Implement package provenance verification
- [ ] Scan container images for vulnerabilities
- [ ] Use minimal base images (distroless when possible)
- [ ] Sign container images and artifacts
- [ ] Implement reproducible builds

**Implementation Pattern**:
```dockerfile
# CORRECT: Minimal, security-focused container
FROM gcr.io/distroless/python3:nonroot
# Non-root user, minimal attack surface

# Copy only necessary files
COPY --chown=nonroot:nonroot app/ /app/
WORKDIR /app

USER nonroot
CMD ["python", "app.py"]

# FORBIDDEN: Full OS images with root
# FROM ubuntu:latest  # Too much attack surface
# RUN apt-get install ...  # Unnecessary packages
# USER root  # Never run as root
```

---

## Input Validation Rules (OWASP Foundation)

**CRITICAL**: Validate ALL external inputs before processing.

### General Input Validation Principles

**Validation Rules**:
- [ ] Use allowlists (positive validation) instead of denylists
- [ ] Validate input type, length, format, and range
- [ ] Sanitize inputs before use in dangerous contexts (SQL, OS commands, HTML)
- [ ] Reject invalid input rather than attempting to sanitize
- [ ] Validate at multiple layers (client-side for UX, server-side for security)
- [ ] Use parameterized queries for database operations
- [ ] Encode outputs appropriate to context

**Implementation Pattern**:
```python
# CORRECT: Comprehensive input validation
import re
from typing import Optional

def validate_email(email: str) -> Optional[str]:
    """Validate email format using allowlist approach."""
    # Type check
    if not isinstance(email, str):
        raise ValueError("Email must be string")
    
    # Length check
    if not (5 <= len(email) <= 254):
        raise ValueError("Email length invalid")
    
    # Format validation (allowlist pattern)
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        raise ValueError("Invalid email format")
    
    return email.lower()

def validate_numeric_input(value: str, min_val: int, max_val: int) -> int:
    """Validate numeric input with range checking."""
    try:
        num = int(value)
    except ValueError:
        raise ValueError("Input must be numeric")
    
    if not (min_val <= num <= max_val):
        raise ValueError(f"Value must be between {min_val} and {max_val}")
    
    return num

# Usage in API handler
def create_user(request):
    try:
        email = validate_email(request.get('email'))
        age = validate_numeric_input(request.get('age'), 13, 120)
    except ValueError as e:
        return {"error": str(e)}, 400
    
    # Safe to use validated inputs
    user = User(email=email, age=age)
    user.save()

# FORBIDDEN: No validation
# def create_user(request):
#     user = User(email=request.get('email'))  # VULNERABLE
```

---

### SQL Injection Prevention

**CRITICAL**: Never concatenate user input into SQL queries.

**Validation Rules**:
- [ ] ALWAYS use parameterized queries or prepared statements
- [ ] Use ORM frameworks with proper escaping
- [ ] Never concatenate user input into SQL strings
- [ ] Apply least privilege to database user accounts
- [ ] Disable unnecessary database features (e.g., xp_cmdshell)

**Implementation Pattern**:
```python
# CORRECT: Parameterized queries
def get_user(user_id: str):
    # Using parameterized query
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))  # Safe
    return cursor.fetchone()

# Using ORM (SQLAlchemy)
def get_users_by_status(status: str):
    return session.query(User).filter(User.status == status).all()

# FORBIDDEN: String concatenation
# def get_user(user_id):
#     query = f"SELECT * FROM users WHERE id = {user_id}"  # VULNERABLE TO SQL INJECTION
#     cursor.execute(query)
```

---

### Cross-Site Scripting (XSS) Prevention

**CRITICAL**: Encode outputs based on context to prevent XSS.

**Validation Rules**:
- [ ] Encode HTML entities when rendering user input in HTML
- [ ] Use Content Security Policy (CSP) headers
- [ ] Validate and sanitize rich text inputs
- [ ] Use frameworks with automatic escaping (React, Vue, Angular)
- [ ] Never use eval() or innerHTML with user input
- [ ] Set HttpOnly and Secure flags on cookies

**Implementation Pattern**:
```python
# Backend - CORRECT: Output encoding
import html

def render_comment(comment_text: str) -> str:
    # HTML entity encoding
    safe_comment = html.escape(comment_text)
    return f"<div class='comment'>{safe_comment}</div>"

# CSP headers
response.headers['Content-Security-Policy'] = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline' https://trusted-cdn.com; "
    "style-src 'self' 'unsafe-inline'; "
    "img-src 'self' data: https:; "
    "object-src 'none'; "
    "base-uri 'self'"
)

# Frontend - CORRECT: React auto-escapes
function CommentDisplay({ comment }) {
    return <div className="comment">{comment}</div>;  // Auto-escaped
}

// FORBIDDEN: Direct HTML injection
// element.innerHTML = userInput;  // VULNERABLE TO XSS
// eval(userInput);  // NEVER use eval with user input
```

---

### Command Injection Prevention

**CRITICAL**: Never execute shell commands with user input.

**Validation Rules**:
- [ ] Avoid shell command execution when possible (use libraries)
- [ ] If shell execution required, use allowlists for permitted commands
- [ ] Never concatenate user input into shell commands
- [ ] Use subprocess with argument lists, not shell=True
- [ ] Run commands with least privilege
- [ ] Validate and sanitize all command arguments

**Implementation Pattern**:
```python
# CORRECT: Use libraries instead of shell commands
import boto3
import subprocess

# Good: Use SDK
def upload_to_s3(file_path: str, bucket: str):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket, os.path.basename(file_path))

# If shell required: Use argument lists
def process_file(filename: str):
    # Validate filename (allowlist approach)
    if not re.match(r'^[a-zA-Z0-9_.-]+$', filename):
        raise ValueError("Invalid filename")
    
    # Use argument list (not shell=True)
    result = subprocess.run(
        ['convert', filename, 'output.png'],
        capture_output=True,
        timeout=30,
        shell=False  # CRITICAL: Do not use shell=True
    )
    return result

# FORBIDDEN: Command injection vulnerable
# def process_file(filename):
#     os.system(f"convert {filename} output.png")  # VULNERABLE
#     subprocess.run(f"convert {filename} output.png", shell=True)  # VULNERABLE
```

---

## Error Handling and Logging

**CRITICAL**: Fail securely without exposing sensitive information.

### Secure Error Handling

**Validation Rules**:
- [ ] Never expose stack traces to end users
- [ ] Never include sensitive data in error messages
- [ ] Log detailed errors internally, show generic messages externally
- [ ] Implement centralized error handling
- [ ] Return appropriate HTTP status codes
- [ ] Use correlation IDs for error tracking

**Implementation Pattern**:
```python
# CORRECT: Secure error handling
import logging
import uuid

logger = logging.getLogger(__name__)

def api_handler(request):
    correlation_id = str(uuid.uuid4())
    
    try:
        # Business logic
        result = process_request(request)
        return {"status": "success", "data": result}, 200
        
    except ValidationError as e:
        # Client error - safe to return
        logger.warning(f"[{correlation_id}] Validation error: {e}")
        return {
            "error": "Invalid input provided",
            "correlation_id": correlation_id
        }, 400
        
    except DatabaseError as e:
        # Server error - don't expose details
        logger.error(f"[{correlation_id}] Database error: {e}", exc_info=True)
        return {
            "error": "An internal error occurred. Please contact support.",
            "correlation_id": correlation_id
        }, 500
        
    except Exception as e:
        # Unexpected error - log everything, return generic message
        logger.critical(f"[{correlation_id}] Unexpected error: {e}", exc_info=True)
        return {
            "error": "An unexpected error occurred. Please contact support.",
            "correlation_id": correlation_id
        }, 500

# FORBIDDEN: Exposing sensitive information
# except Exception as e:
#     return {"error": str(e), "stack": traceback.format_exc()}, 500  # NEVER expose stack traces
```

---

### Security Logging Requirements

**CRITICAL**: Log security-relevant events for detection and response.

**Validation Rules**:
- [ ] Log all authentication attempts (success and failure)
- [ ] Log all authorization failures
- [ ] Log all input validation failures
- [ ] Log all administrative actions
- [ ] Log all data access (especially sensitive data)
- [ ] NEVER log sensitive data (passwords, tokens, PII, credit cards)
- [ ] Use structured logging (JSON) for parsing
- [ ] Include correlation IDs for request tracing

**Implementation Pattern**:
```python
# CORRECT: Security logging
import logging
import json

# Structured logger
class SecurityLogger:
    def __init__(self):
        self.logger = logging.getLogger('security')
    
    def log_auth_attempt(self, user_id: str, success: bool, ip: str, method: str):
        event = {
            "event_type": "authentication",
            "user_id": user_id,
            "success": success,
            "ip_address": ip,
            "auth_method": method,
            "timestamp": datetime.utcnow().isoformat()
        }
        level = logging.INFO if success else logging.WARNING
        self.logger.log(level, json.dumps(event))
    
    def log_authz_failure(self, user_id: str, resource: str, action: str):
        event = {
            "event_type": "authorization_failure",
            "user_id": user_id,
            "resource": resource,
            "action": action,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.logger.warning(json.dumps(event))
    
    def mask_sensitive_data(self, data: dict) -> dict:
        """Mask sensitive fields before logging."""
        masked = data.copy()
        sensitive_fields = ['password', 'token', 'api_key', 'ssn', 'credit_card']
        for field in sensitive_fields:
            if field in masked:
                masked[field] = '***REDACTED***'
        return masked

# Usage
security_log = SecurityLogger()
security_log.log_auth_attempt(
    user_id="user123",
    success=True,
    ip="203.0.113.42",
    method="api_key"
)

# FORBIDDEN: Logging sensitive data
# logger.info(f"User login: {username} with password {password}")  # NEVER log passwords
# logger.debug(f"API request headers: {headers}")  # May contain API keys
```

---

## AI-DLC Phase-Specific Security Requirements

### INCEPTION PHASE

#### Workspace Detection Stage
**Security Actions**: None specific to this stage.

#### Requirements Analysis Stage
**CRITICAL**: Security requirements MUST be defined during this stage.

**Validation Rules**:
- [ ] Identify data classification levels (public, internal, confidential, restricted)
- [ ] Define authentication and authorization requirements
- [ ] Specify encryption requirements (at rest and in transit)
- [ ] Document compliance requirements (GDPR, HIPAA, PCI-DSS, SOC2)
- [ ] Identify security boundaries and trust zones
- [ ] List sensitive data handling requirements
- [ ] Define logging and monitoring requirements

**Security Requirements Template**:
```markdown
## Security Requirements

### Data Classification
- User PII: CONFIDENTIAL (encryption required)
- Application logs: INTERNAL (no PII)
- Public API responses: PUBLIC

### Authentication & Authorization
- Authentication: OAuth 2.0 / API Keys with rotation
- Authorization: Role-based access control (RBAC)
- Session management: 30-minute timeout, secure cookies

### Encryption
- Data at rest: AES-256 via AWS KMS
- Data in transit: TLS 1.2+ (prefer TLS 1.3)
- Database: Encrypted with customer-managed keys

### Compliance
- GDPR: Right to deletion, data portability
- SOC2: Audit logging, access controls

### Security Boundaries
- Public: CloudFront, ALB
- Private: Application servers, databases
- Isolated: Security tools, bastion hosts

### Logging & Monitoring
- CloudTrail: All API calls
- Application logs: Auth attempts, errors, admin actions
- Retention: 1 year minimum
```

---

#### User Stories Stage (Conditional)
**Security Actions**: Include security-focused user stories.

**Validation Rules**:
- [ ] Create user stories for authentication flows
- [ ] Create user stories for authorization checks
- [ ] Create user stories for data encryption
- [ ] Create user stories for audit logging
- [ ] Include abuse cases (negative testing scenarios)

**Security User Stories Template**:
```markdown
### Authentication Stories
- As a user, I need to authenticate with MFA so that my account is protected from unauthorized access
- As an admin, I need failed login attempts logged so that I can detect brute force attacks

### Authorization Stories
- As a system, I need to verify user permissions before allowing data access so that data remains protected
- As a user, I should only see data I'm authorized to access

### Data Protection Stories
- As a system, I need to encrypt sensitive data at rest so that it's protected from disk theft
- As a compliance officer, I need audit logs of data access for compliance reporting

### Abuse Cases
- As an attacker, I might try SQL injection in the search field [System must prevent this]
- As an attacker, I might try to access other users' data via API manipulation [System must prevent this]
```

---

#### Workflow Planning Stage
**Security Actions**: Include security validation gates in workflow.

**Validation Rules**:
- [ ] Plan security code review checkpoints
- [ ] Schedule SAST/DAST scanning stages
- [ ] Include dependency vulnerability scanning
- [ ] Plan penetration testing phase
- [ ] Define security approval gates before deployment

---

### CONSTRUCTION PHASE

#### Functional Design Stage (Conditional, Per-Unit)
**CRITICAL**: Design security controls into functionality.

**Validation Rules**:
- [ ] Design input validation for all inputs
- [ ] Design authentication checks for protected endpoints
- [ ] Design authorization logic for resource access
- [ ] Design secure session management
- [ ] Design rate limiting and throttling
- [ ] Design error handling without information leakage

---

#### NFR Requirements Stage (Conditional, Per-Unit)
**CRITICAL**: Define security non-functional requirements.

**Validation Rules**:
- [ ] Define performance requirements for security controls
- [ ] Define encryption algorithm requirements (AES-256, RSA-2048)
- [ ] Define password complexity requirements
- [ ] Define session timeout requirements
- [ ] Define audit log retention requirements
- [ ] Define availability requirements for security services

---

#### NFR Design Stage (Conditional, Per-Unit)
**CRITICAL**: Design security architecture patterns.

**Validation Rules**:
- [ ] Design layered security architecture (defense in depth)
- [ ] Design secure communication channels (TLS termination)
- [ ] Design secrets management strategy (Secrets Manager, KMS)
- [ ] Design certificate management and rotation
- [ ] Design security group and network ACL rules
- [ ] Design WAF rules for application protection

---

#### Infrastructure Design Stage (Conditional, Per-Unit)
**CRITICAL**: Design secure infrastructure components.

**Validation Rules**:
- [ ] Design VPC with public/private/isolated subnets
- [ ] Design security groups with least privilege rules
- [ ] Design IAM roles with least privilege policies
- [ ] Design encrypted storage (EBS, S3, RDS)
- [ ] Design encrypted data transit paths
- [ ] Design backup and disaster recovery with encryption
- [ ] Design security monitoring and alerting

**Secure Infrastructure Pattern**:
```python
# CORRECT: Multi-layered secure infrastructure
from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_kms as kms,
    aws_s3 as s3,
    aws_rds as rds,
    aws_logs as logs,
    Stack, Duration
)

class SecureInfrastructureStack(Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        # KMS key for encryption
        kms_key = kms.Key(
            self, "AppKey",
            enable_key_rotation=True,  # CRITICAL
            removal_policy=RemovalPolicy.RETAIN
        )
        
        # VPC with network segmentation
        vpc = ec2.Vpc(
            self, "SecureVPC",
            max_azs=3,
            nat_gateways=3,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="Isolated",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=24
                )
            ],
            enable_dns_hostnames=True,
            enable_dns_support=True
        )
        
        # Enable VPC Flow Logs
        log_group = logs.LogGroup(
            self, "VPCFlowLogs",
            retention=logs.RetentionDays.ONE_YEAR
        )
        
        ec2.FlowLog(
            self, "FlowLog",
            resource_type=ec2.FlowLogResourceType.from_vpc(vpc),
            destination=ec2.FlowLogDestination.to_cloud_watch_logs(log_group)
        )
        
        # Application security group (least privilege)
        app_sg = ec2.SecurityGroup(
            self, "AppSecurityGroup",
            vpc=vpc,
            description="Application security group",
            allow_all_outbound=False  # Explicit egress
        )
        
        # Only allow HTTPS outbound
        app_sg.add_egress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="HTTPS outbound"
        )
        
        # Encrypted S3 bucket
        bucket = s3.Bucket(
            self, "DataBucket",
            encryption=s3.BucketEncryption.KMS,
            encryption_key=kms_key,
            enforce_ssl=True,  # CRITICAL
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            lifecycle_rules=[
                s3.LifecycleRule(
                    enabled=True,
                    noncurrent_version_expiration=Duration.days(90)
                )
            ],
            server_access_logs_bucket=logs_bucket,
            server_access_logs_prefix="s3-access-logs/"
        )
        
        # Encrypted database in isolated subnet
        db_sg = ec2.SecurityGroup(
            self, "DatabaseSG",
            vpc=vpc,
            description="Database security group",
            allow_all_outbound=False
        )
        
        # Only allow app tier access
        db_sg.add_ingress_rule(
            peer=app_sg,
            connection=ec2.Port.tcp(5432),
            description="PostgreSQL from app tier"
        )
        
        database = rds.DatabaseInstance(
            self, "Database",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_15
            ),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
            security_groups=[db_sg],
            storage_encrypted=True,  # CRITICAL
            storage_encryption_key=kms_key,
            backup_retention=Duration.days(30),
            deletion_protection=True,
            cloudwatch_logs_exports=["postgresql"],
            monitoring_interval=Duration.seconds(60)
        )
        
        # IAM role with least privilege
        app_role = iam.Role(
            self, "AppRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            description="Application role with least privilege"
        )
        
        # Grant specific permissions only
        bucket.grant_read_write(app_role)
        kms_key.grant_encrypt_decrypt(app_role)
```

---

#### Code Planning Stage
**CRITICAL**: Plan security implementations before code generation.

**Validation Rules**:
- [ ] Plan input validation functions for all inputs
- [ ] Plan authentication middleware/decorators
- [ ] Plan authorization checks for each protected resource
- [ ] Plan secrets retrieval from Secrets Manager
- [ ] Plan security headers configuration
- [ ] Plan CSRF token generation and validation (for web apps)
- [ ] Plan SQL parameterization approach
- [ ] Plan error handling and logging patterns

---

#### Code Generation Stage (ALWAYS, Per-Unit)
**CRITICAL**: Generated code MUST implement security controls.

**Validation Rules - Before Accepting Generated Code**:
- [ ] NO hardcoded secrets (API keys, passwords, tokens)
- [ ] ALL inputs validated before processing
- [ ] SQL queries use parameterization (no string concatenation)
- [ ] Authentication checks present on protected endpoints
- [ ] Authorization checks present before resource access
- [ ] Security headers configured (CSP, HSTS, X-Frame-Options)
- [ ] Error messages don't expose sensitive information
- [ ] Logging doesn't include sensitive data
- [ ] Dependencies pinned to specific versions
- [ ] TLS/HTTPS enforced for external communications
- [ ] CORS restricted to specific origins (no wildcards)

**Code Generation Security Checklist**:
```markdown
## Pre-Acceptance Security Validation

### Secrets Management
- [ ] No hardcoded credentials in code
- [ ] Secrets loaded from AWS Secrets Manager or Parameter Store
- [ ] Database connection strings use environment variables

### Input Validation
- [ ] All API inputs validated (type, length, format, range)
- [ ] File uploads validated (size, type, content)
- [ ] SQL queries use parameterized statements
- [ ] User input never passed directly to eval() or exec()

### Authentication & Authorization
- [ ] Authentication middleware applied to protected routes
- [ ] JWT tokens validated (signature, expiration, issuer)
- [ ] API keys validated against secure storage
- [ ] Authorization checks before resource access

### Data Protection
- [ ] Sensitive data encrypted at rest
- [ ] TLS enforced for data in transit
- [ ] PII masked in logs
- [ ] Passwords hashed with bcrypt/argon2 (never plaintext)

### Error Handling
- [ ] Generic error messages to users
- [ ] Detailed errors logged internally only
- [ ] Stack traces never exposed
- [ ] Correlation IDs for error tracking

### Logging & Monitoring
- [ ] Authentication events logged
- [ ] Authorization failures logged
- [ ] No sensitive data in logs
- [ ] Structured logging format (JSON)

### Infrastructure
- [ ] Security groups with least privilege rules
- [ ] IAM roles with least privilege policies
- [ ] Encryption enabled on storage resources
- [ ] VPC configuration with proper network segmentation
```

---

#### Build and Test Stage (ALWAYS)
**CRITICAL**: Run security tests before accepting build.

**Validation Rules**:
- [ ] Run SAST (Static Application Security Testing)
- [ ] Run dependency vulnerability scanning
- [ ] Run DAST (Dynamic Application Security Testing) if applicable
- [ ] Perform security unit tests (authentication, authorization)
- [ ] Test input validation with malicious inputs
- [ ] Test error handling doesn't expose sensitive data
- [ ] Verify secrets not committed to repository
- [ ] Test HTTPS/TLS enforcement

**Security Testing Patterns**:
```python
# Security unit tests
import pytest

def test_authentication_required():
    """Test that protected endpoint requires authentication."""
    response = client.get('/api/protected')
    assert response.status_code == 401
    assert 'authentication required' in response.json()['error'].lower()

def test_sql_injection_prevention():
    """Test that SQL injection attempts are blocked."""
    malicious_input = "'; DROP TABLE users; --"
    response = client.post('/api/search', json={'query': malicious_input})
    # Should not cause error, should return empty or sanitized result
    assert response.status_code in [200, 400]
    
    # Verify table still exists
    result = db.execute("SELECT COUNT(*) FROM users")
    assert result.scalar() >= 0

def test_xss_prevention():
    """Test that XSS attempts are escaped."""
    xss_payload = '<script>alert("XSS")</script>'
    response = client.post('/api/comment', json={'text': xss_payload})
    assert response.status_code == 200
    
    # Retrieve and verify escaped
    comment = db.query(Comment).first()
    assert '<script>' not in comment.rendered_html
    assert '&lt;script&gt;' in comment.rendered_html or \
           xss_payload not in comment.rendered_html

def test_authorization_enforcement():
    """Test that users can only access their own data."""
    # User A creates resource
    token_a = get_auth_token('user_a')
    response = client.post('/api/resource', 
                          json={'data': 'secret'},
                          headers={'Authorization': f'Bearer {token_a}'})
    resource_id = response.json()['id']
    
    # User B tries to access
    token_b = get_auth_token('user_b')
    response = client.get(f'/api/resource/{resource_id}',
                         headers={'Authorization': f'Bearer {token_b}'})
    assert response.status_code == 403

def test_rate_limiting():
    """Test that rate limiting is enforced."""
    for i in range(101):  # Assuming 100 requests/min limit
        response = client.get('/api/endpoint')
    
    assert response.status_code == 429  # Too Many Requests

def test_no_secrets_in_logs(caplog):
    """Test that sensitive data is not logged."""
    api_key = "sk_test_123456789"
    password = "SuperSecret123"
    
    # Trigger logging
    response = client.post('/api/login',
                          json={'username': 'test', 'password': password},
                          headers={'X-API-Key': api_key})
    
    # Verify secrets not in logs
    log_content = caplog.text
    assert api_key not in log_content
    assert password not in log_content
    assert '***' in log_content or 'REDACTED' in log_content
```

---

### OPERATIONS PHASE (Placeholder - Future)

**Security Monitoring & Response** (when implemented):
- Continuous security monitoring
- Automated incident response
- Security metrics and dashboards
- Compliance reporting
- Vulnerability management
- Security patch management

---

## Security Validation Gates

**MANDATORY**: All phases must pass security validation before proceeding.

### Gate 1: Requirements Phase Exit
- [ ] Security requirements documented
- [ ] Data classification defined
- [ ] Compliance requirements identified
- [ ] Threat model created (for complex features)

### Gate 2: Design Phase Exit
- [ ] Security architecture reviewed
- [ ] Secrets management strategy defined
- [ ] Encryption strategy defined
- [ ] Least privilege access designed
- [ ] Security design review completed

### Gate 3: Code Generation Phase Exit
- [ ] SAST scan passed (no HIGH/CRITICAL issues)
- [ ] Dependency scan passed (no HIGH/CRITICAL CVEs)
- [ ] Code review completed (security focus)
- [ ] No hardcoded secrets detected
- [ ] Input validation implemented
- [ ] Authentication/authorization implemented

### Gate 4: Build & Test Phase Exit
- [ ] Security unit tests passing
- [ ] DAST scan passed (if applicable)
- [ ] Penetration test passed (for production releases)
- [ ] Security acceptance criteria met
- [ ] Security sign-off obtained

---

## Quick Reference: Security Checklist by Type

### Web Application Security
- [ ] Use HTTPS/TLS 1.2+ for all communications
- [ ] Implement Content Security Policy (CSP)
- [ ] Set Secure and HttpOnly flags on cookies
- [ ] Implement CSRF protection for state-changing operations
- [ ] Encode outputs based on context (HTML, JavaScript, URL)
- [ ] Validate and sanitize all inputs
- [ ] Implement rate limiting
- [ ] Use security headers (HSTS, X-Frame-Options, X-Content-Type-Options)

### API Security
- [ ] Implement authentication (API keys, OAuth 2.0, JWT)
- [ ] Validate API keys/tokens on every request
- [ ] Implement authorization checks before resource access
- [ ] Use API Gateway with request validation
- [ ] Implement rate limiting and throttling
- [ ] Log all API access attempts
- [ ] Version APIs and deprecate insecure versions
- [ ] Document API security requirements

### Database Security
- [ ] Use parameterized queries (never string concatenation)
- [ ] Apply least privilege to database users
- [ ] Enable encryption at rest
- [ ] Enable encryption in transit (TLS)
- [ ] Implement database access logging
- [ ] Regular backup with encryption
- [ ] Disable unnecessary database features
- [ ] Use connection pooling with authentication

### AWS Infrastructure Security
- [ ] Use IAM roles (not access keys)
- [ ] Implement least privilege IAM policies
- [ ] Enable MFA for human users
- [ ] Enable CloudTrail in all regions
- [ ] Configure VPC with network segmentation
- [ ] Use security groups with least privilege
- [ ] Enable encryption on S3, EBS, RDS
- [ ] Enforce SSL/TLS on all resources
- [ ] Enable AWS Config for compliance monitoring
- [ ] Configure CloudWatch alarms for security events

### Container Security
- [ ] Use minimal base images (distroless)
- [ ] Run containers as non-root user
- [ ] Scan images for vulnerabilities
- [ ] Sign container images
- [ ] Use secrets management (not environment variables)
- [ ] Implement resource limits
- [ ] Use network policies to restrict communication
- [ ] Regular image updates and patching

---

## Summary

This security baseline provides universal secure coding standards drawn from:
- **OWASP Top 10 for LLMs**: Prompt injection, insecure output handling, sensitive information disclosure
- **AWS Well-Architected Security Pillar**: IAM, detection, infrastructure protection, data protection
- **OpenSSF**: Secure development, dependency management, supply chain security
- **OWASP Foundation**: Input validation, SQL injection, XSS, command injection prevention

**Key Principles**:
1. Security is mandatory, not optional
2. Secure by default, explicit opt-in for insecure
3. Defense in depth - multiple layers
4. Least privilege everywhere
5. Validate all inputs, sanitize all outputs
6. Fail securely without information leakage
7. Log security events, never log secrets

**Application Across AI-DLC**:
- **INCEPTION**: Define security requirements, include security stories
- **CONSTRUCTION**: Design and implement security controls
- **OPERATIONS**: Monitor, detect, respond to security events

**Success Criteria**: AI-generated code following this baseline will be secure by default and pass security testing without critical/high findings.
