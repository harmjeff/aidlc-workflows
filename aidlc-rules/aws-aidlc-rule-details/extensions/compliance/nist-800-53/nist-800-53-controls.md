# NIST 800-53 Controls

**Extension**: nist-800-53 v0.1.0 | **Type**: compliance | **Framework**: NIST 800-53

> This extension provides NIST 800-53 control mappings. When installed and enabled, the AI-DLC workflow embeds these controls directly into each relevant stage (requirements, design, infrastructure, code generation, testing).

---

## AC — Access Control

### AC-3: Access Enforcement

Controls that enforce approved authorizations for logical access to information and system resources.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CT.BACKUP.PV.1 | Limits changes to tags that AWS Control Tower applies to AWS Backup resources | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |
| CT.BACKUP.PV.2 | Limits changes to the AWS Backup report plan that AWS Control Tower manages | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |
| CT.BACKUP.PV.3 | Limits creation or modification of AWS Backup resources that AWS Control Tower manages | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: CT-Managed SCP
- **Status**: Elective - Not Yet Enabled
- **Priority**: High

---

### AC-6(1): Least Privilege | Authorize Access to Security Functions

Controls that authorize access to security functions and security-relevant information.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CT.BACKUP.PV.1 | Limits changes to tags that AWS Control Tower applies to AWS Backup resources | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |
| CT.BACKUP.PV.2 | Limits changes to the AWS Backup report plan that AWS Control Tower manages | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |
| CT.BACKUP.PV.3 | Limits creation or modification of AWS Backup resources that AWS Control Tower manages | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: CT-Managed SCP
- **Status**: Elective - Not Yet Enabled
- **Priority**: High

---

### AC-6(9): Least Privilege | Log Use of Privileged Functions

Controls that log the execution of privileged functions.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| SH.CloudTrail.1 | Checks that there is at least one multi-region AWS CloudTrail trail | CloudTrail | DETECTIVE | HIGH | Security Hub Control | Partially Covered |

**Enforcement details:**
- **Scope**: All OUs (Security Hub)
- **Mechanism**: Security Hub
- **Status**: Available
- **Priority**: High

---

## Control Summary

| NIST 800-53 Control | Control Name | # AWS CT Controls | Types |
|---|---|---|---|
| AC-3 | Access Enforcement | 3 | Preventive (SCP) |
| AC-6(1) | Least Privilege - Authorize Access to Security Functions | 3 | Preventive (SCP) |
| AC-6(9) | Least Privilege - Log Use of Privileged Functions | 1 | Detective (Security Hub) |

## Stage Applicability

When this extension is enabled, the AI-DLC workflow applies these controls to:
- **Requirements**: Access control requirements derived from AC-3, AC-6(1), AC-6(9)
- **Design**: Architecture constraints for SCP enforcement and CloudTrail integration
- **Infrastructure**: AWS Control Tower landing zone configuration, SCP policies, Security Hub enablement
- **Code Generation**: IAM policy patterns, least-privilege examples
- **Testing**: Compliance verification for SCP enforcement and CloudTrail multi-region coverage

---

*v0.1.0 — Initial AC family controls. Future versions will add additional NIST 800-53 families.*
