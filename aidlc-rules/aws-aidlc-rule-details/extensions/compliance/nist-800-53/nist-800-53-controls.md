# NIST 800-53 Controls

**Extension**: nist-800-53 v0.2.0 | **Type**: compliance | **Framework**: NIST 800-53

> This extension provides NIST 800-53 control mappings. When installed and enabled, the AI-DLC workflow embeds these controls directly into each relevant stage (requirements, design, infrastructure, code generation, testing).

---

## AC — Access Control

### AC-3: Access Enforcement

Controls that enforce approved authorizations for logical access to information and system resources.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CONFIG.COGNITO-IDP.DT.1 | Checks if an Amazon Cognito user pool has advanced security enabled | Cognito | DETECTIVE | HIGH | Config Rule | Partially Covered |
| CONFIG.COGNITO-IDP.DT.2 | Checks if Amazon Cognito Identity Pool allows unauthenticated identities | Cognito | DETECTIVE | MEDIUM | Config Rule | Partially Covered |
| CT.APIGATEWAY.PR.5 | Checks whether Amazon API Gateway V2 API routes have an authorization type set | ApiGatewayV2 | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| CT.BACKUP.PV.1 | Limits changes to tags that AWS Control Tower applies to AWS Backup resources | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |
| CT.BACKUP.PV.2 | Limits changes to the AWS Backup report plan that AWS Control Tower manages | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |
| CT.BACKUP.PV.3 | Limits creation or modification of AWS Backup resources that AWS Control Tower manages | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |
| CT.EC2.PV.11 | Prevents the public sharing of your AMIs by configuring block public access for AMIs | EC2 | PREVENTIVE | MEDIUM | Declarative Policy | Partially Covered |
| CT.EC2.PV.3 | Disallows sharing of an EBS snapshot with all AWS accounts | EC2 | PREVENTIVE | CRITICAL | SCP | Partially Covered |
| CT.EC2.PV.5 | Disallows use of EC2 VM Import/Export APIs | EC2 | PREVENTIVE | MEDIUM | SCP | Partially Covered |
| CT.EC2.PV.7 | Blocks the public sharing of your Amazon EBS snapshots | EC2 | PREVENTIVE | MEDIUM | Declarative Policy | Partially Covered |
| CT.EC2.PV.9 | Prevents access to the EC2 serial console of all EC2 instances | EC2 | PREVENTIVE | MEDIUM | Declarative Policy | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: Mixed (SCP, Config Rule, Declarative Policy, CF Hook)
- **Status**: Elective - Not Yet Enabled (CT controls); Available (Config Rules)
- **Priority**: High

---

### AC-4: Information Flow Enforcement

Controls that enforce approved authorizations for controlling the flow of information within the system and between connected systems.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| AWS-GR_RESTRICTED_COMMON_PORTS | Reduces a server's exposure to risk by removing unfettered connectivity to remote console services such as RDP | EC2 | DETECTIVE | CRITICAL | Config Rule | Partially Covered |
| AWS-GR_RESTRICTED_SSH | Reduces a server's exposure to risk by removing unfettered connectivity to SSH | EC2 | DETECTIVE | HIGH | Config Rule | Partially Covered |
| CONFIG.EC2.DT.11 | Checks if non-default security groups are attached to elastic network interfaces | EC2 | DETECTIVE | MEDIUM | Config Rule | Partially Covered |
| CONFIG.EC2.DT.17 | Checks if internet gateways are attached to an authorized VPC | EC2 | DETECTIVE | HIGH | Config Rule | Partially Covered |
| CONFIG.EC2.DT.18 | Checks if all Elastic IP addresses allocated to an AWS account are attached to EC2 instances | EC2 | DETECTIVE | LOW | Config Rule | Partially Covered |
| CONFIG.EC2.DT.20 | Checks if DNS resolution from accepter/requester VPC to private IP is enabled | EC2 | DETECTIVE | MEDIUM | Config Rule | Partially Covered |
| CONFIG.EC2.DT.8 | Checks if the AWS Client VPN authorization rules authorizes connection access for all clients | EC2 | DETECTIVE | CRITICAL | Config Rule | Partially Covered |
| CT.APPSYNC.PR.2 | Checks whether an AWS AppSync GraphQL API has been configured with private visibility | AppSync | PROACTIVE | HIGH | CF Hook (Proactive) | Partially Covered |
| CT.EC2.PR.2 | Checks whether an Amazon EC2 launch template has a metadata token hop limit set to 1 | EC2 | PROACTIVE | HIGH | CF Hook (Proactive) | Partially Covered |
| CT.EC2.PR.3 | Checks whether the Amazon EC2 security group rule contains 0.0.0.0/0 or ::/0 as a source IP range | EC2 | PROACTIVE | HIGH | CF Hook (Proactive) | Partially Covered |
| CT.EC2.PR.4 | Checks whether an Amazon EC2 security group rule with 0.0.0.0/0 allows incoming traffic to high-risk ports | EC2 | PROACTIVE | CRITICAL | CF Hook (Proactive) | Partially Covered |
| CT.EC2.PR.9 | Checks whether your Amazon EC2 launch templates are configured to assign public IP addresses to network interfaces | EC2 | PROACTIVE | HIGH | CF Hook (Proactive) | Partially Covered |
| CT.EC2.PV.11 | Prevents the public sharing of your AMIs by configuring block public access for AMIs | EC2 | PREVENTIVE | MEDIUM | Declarative Policy | Partially Covered |
| SH.EC2.10 | Checks whether a service endpoint for Amazon EC2 is created for each VPC | EC2 | DETECTIVE | MEDIUM | Security Hub Control | Partially Covered |
| SH.EC2.16 | Checks to see if there are any NACLs that are unused | EC2 | DETECTIVE | LOW | Security Hub Control | Partially Covered |
| SH.EC2.18 | Checks whether the security groups allow unrestricted incoming traffic | EC2 | DETECTIVE | HIGH | Security Hub Control | Partially Covered |
| SH.EC2.19 | Checks whether unrestricted incoming traffic is accessible to high-risk ports | EC2 | DETECTIVE | CRITICAL | Security Hub Control | Partially Covered |
| SH.EC2.2 | Checks that the default security group of a VPC does not allow inbound or outbound traffic | EC2 | DETECTIVE | HIGH | Security Hub Control | Partially Covered |
| SH.EC2.21 | Checks whether a NACL allows unrestricted access to SSH/RDP ingress traffic | EC2 | DETECTIVE | MEDIUM | Security Hub Control | Partially Covered |
| SH.EC2.22 | Checks that security groups are attached to Amazon EC2 instances or to an elastic network interface | EC2 | DETECTIVE | MEDIUM | Security Hub Control | Partially Covered |
| SH.EC2.23 | Checks if EC2 Transit Gateways are automatically accepting shared VPC attachments requests | EC2 | DETECTIVE | HIGH | Security Hub Control | Partially Covered |

**Enforcement details:**
- **Scope**: Mixed (Root, Workload OU)
- **Mechanism**: Mixed (Config Rule, SCP, Declarative Policy, CF Hook, Security Hub)
- **Status**: Mixed (Mandatory, Elective)
- **Priority**: High

---

### AC-6: Least Privilege

Controls that employ the principle of least privilege, allowing only authorized accesses necessary to accomplish assigned organizational tasks.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| AWS-GR_EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK | Detects whether all AWS accounts have access to restore Amazon EBS snapshots | EC2 | DETECTIVE | CRITICAL | Config Rule | Partially Covered |
| CT.APIGATEWAY.PR.5 | Checks whether Amazon API Gateway V2 API routes have an authorization type set | ApiGatewayV2 | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| CT.APPSYNC.PR.3 | Checks that an AWS AppSync GraphQL API has been configured with an authentication type other than API_KEY | AppSync | PROACTIVE | HIGH | CF Hook (Proactive) | Partially Covered |
| CT.EC2.PV.11 | Prevents the public sharing of your AMIs by configuring block public access for AMIs | EC2 | PREVENTIVE | MEDIUM | Declarative Policy | Partially Covered |
| CT.EC2.PV.4 | Disallows usage of all EBS direct APIs | EC2 | PREVENTIVE | HIGH | SCP | Partially Covered |
| CT.EC2.PV.5 | Disallows use of EC2 VM Import/Export APIs | EC2 | PREVENTIVE | MEDIUM | SCP | Partially Covered |
| CT.EC2.PV.9 | Prevents access to the EC2 serial console of all EC2 instances | EC2 | PREVENTIVE | MEDIUM | Declarative Policy | Partially Covered |

**Enforcement details:**
- **Scope**: Mixed (Root, Workload OU)
- **Mechanism**: Mixed (Config Rule, SCP, Declarative Policy, CF Hook)
- **Status**: Mixed (Mandatory, Elective)
- **Priority**: High

---

### AC-6(1): Least Privilege | Authorize Access to Security Functions

Controls that authorize access to security functions and security-relevant information.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| AWS-GR_DISALLOW_VPC_INTERNET_ACCESS | Disallow internet access for an Amazon VPC instance managed by a customer | EC2 | PREVENTIVE | MEDIUM | SCP | Partially Covered |
| CT.BACKUP.PV.1 | Limits changes to tags that AWS Control Tower applies to AWS Backup resources | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |
| CT.BACKUP.PV.2 | Limits changes to the AWS Backup report plan that AWS Control Tower manages | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |
| CT.BACKUP.PV.3 | Limits creation or modification of AWS Backup resources that AWS Control Tower manages | Backup | PREVENTIVE | CRITICAL | SCP | Partially Covered |

**Enforcement details:**
- **Scope**: Mixed (Root, Workload OU)
- **Mechanism**: CT-Managed SCP
- **Status**: Mixed (Mandatory, Elective)
- **Priority**: High

---

### AC-6(10): Least Privilege | Prohibit Non-Privileged Users from Executing Privileged Functions

Controls that prevent non-privileged users from executing privileged functions.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CT.EC2.PV.4 | Disallows usage of all EBS direct APIs | EC2 | PREVENTIVE | HIGH | SCP | Partially Covered |
| CT.EC2.PV.9 | Prevents access to the EC2 serial console of all EC2 instances | EC2 | PREVENTIVE | MEDIUM | Declarative Policy | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: Mixed (SCP, Declarative Policy)
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

### AC-12: Session Termination

Controls that automatically terminate a user session after defined conditions or trigger events.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CONFIG.COGNITO-IDP.DT.1 | Checks if an Amazon Cognito user pool has advanced security enabled | Cognito | DETECTIVE | HIGH | Config Rule | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: Config Rule (Conformance Pack)
- **Status**: Available
- **Priority**: High

---

### AC-17: Remote Access

Controls that establish and manage remote access sessions.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| AWS-GR_DISALLOW_VPN_CONNECTIONS | Disallows Virtual Private Network (VPN) connections to an Amazon VPC | EC2 | PREVENTIVE | MEDIUM | SCP | Partially Covered |

**Enforcement details:**
- **Scope**: Root OU (All Accounts)
- **Mechanism**: CT-Managed SCP
- **Status**: Mandatory - Verify Enabled in CT Console
- **Priority**: Moderate

---

### AC-17(1): Remote Access | Monitoring and Control

Controls that monitor and control remote access methods.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| AWS-GR_RESTRICTED_SSH | Reduces a server's exposure to risk by removing unfettered connectivity to SSH | EC2 | DETECTIVE | HIGH | Config Rule | Partially Covered |
| SH.EC2.21 | Checks whether a NACL allows unrestricted access to SSH/RDP ingress traffic | EC2 | DETECTIVE | MEDIUM | Security Hub Control | Partially Covered |

**Enforcement details:**
- **Scope**: Mixed (Root, Workload OU)
- **Mechanism**: Mixed (Config Rule, Security Hub)
- **Status**: Mixed (Mandatory, Available)
- **Priority**: High

---

### AC-17(3): Remote Access | Managed Access Control Points

Controls that route remote accesses through authorized and managed network access control points.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| AWS-GR_RESTRICTED_SSH | Reduces a server's exposure to risk by removing unfettered connectivity to SSH | EC2 | DETECTIVE | HIGH | Config Rule | Partially Covered |
| CT.EC2.PR.5 | Checks whether the Amazon EC2 network ACL inbound entry allows unrestricted incoming traffic for SSH or RDP | EC2 | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| SH.EC2.21 | Checks whether a NACL allows unrestricted access to SSH/RDP ingress traffic | EC2 | DETECTIVE | MEDIUM | Security Hub Control | Partially Covered |

**Enforcement details:**
- **Scope**: Mixed (Root, Workload OU)
- **Mechanism**: Mixed (Config Rule, CF Hook, Security Hub)
- **Status**: Mixed (Mandatory, Elective)
- **Priority**: High

---

### AC-22: Publicly Accessible Content

Controls that designate individuals authorized to make information publicly accessible and ensure procedures are in place to prevent unauthorized disclosure.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CT.EC2.PV.11 | Prevents the public sharing of your AMIs by configuring block public access for AMIs | EC2 | PREVENTIVE | MEDIUM | Declarative Policy | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: CT-Managed Declarative Policy
- **Status**: Elective - Not Yet Enabled
- **Priority**: Moderate

---

## AU — Audit and Accountability

### AU-2: Event Logging

Controls that identify events requiring logging in accordance with applicable laws, policies, and organizational guidance.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CONFIG.APPSYNC.DT.5 | Checks if an AWS AppSync API has logging enabled | AppSync | DETECTIVE | MEDIUM | Config Rule | Partially Covered |
| CONFIG.EC2.DT.7 | Checks if AWS Site-to-Site VPN connections have Amazon CloudWatch logging enabled for both tunnels | EC2 | DETECTIVE | MEDIUM | Config Rule | Partially Covered |
| CT.APIGATEWAY.PR.1 | Checks whether all methods in Amazon API Gateway stage have execution logging configured | ApiGateway | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| CT.APIGATEWAY.PR.2 | Ensures that AWS X-Ray tracing is enabled on Amazon API Gateway REST APIs | ApiGateway | PROACTIVE | LOW | CF Hook (Proactive) | Partially Covered |
| CT.APIGATEWAY.PR.4 | Checks whether Amazon API Gateway V2 stages have access logging enabled | ApiGatewayV2 | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| CT.APPSYNC.PR.1 | Checks whether an AWS AppSync GraphQL API sends logs to Amazon CloudWatch Logs | AppSync | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| CT.EC2.PR.10 | Checks whether the Amazon EC2 launch template has detailed monitoring enabled | EC2 | PROACTIVE | LOW | CF Hook (Proactive) | Partially Covered |
| SH.APIGateway.1 | Checks whether all stages of Amazon API Gateway REST and WebSocket APIs have logging enabled | ApiGateway | DETECTIVE | MEDIUM | Security Hub Control | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: Mixed (Config Rule, CF Hook, Security Hub)
- **Status**: Mixed (Available, Elective)
- **Priority**: Moderate

---

### AU-3: Content of Audit Records

Controls that ensure audit records contain sufficient information to establish what events occurred, when and where they occurred, and the sources and outcomes of events.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CONFIG.APPSYNC.DT.5 | Checks if an AWS AppSync API has logging enabled | AppSync | DETECTIVE | MEDIUM | Config Rule | Partially Covered |
| CONFIG.EC2.DT.7 | Checks if AWS Site-to-Site VPN connections have Amazon CloudWatch logging enabled for both tunnels | EC2 | DETECTIVE | MEDIUM | Config Rule | Partially Covered |
| CT.APIGATEWAY.PR.1 | Checks whether all methods in Amazon API Gateway stage have execution logging configured | ApiGateway | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| CT.APIGATEWAY.PR.4 | Checks whether Amazon API Gateway V2 stages have access logging enabled | ApiGatewayV2 | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| CT.APPSYNC.PR.1 | Checks whether an AWS AppSync GraphQL API sends logs to Amazon CloudWatch Logs | AppSync | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| SH.APIGateway.1 | Checks whether all stages of Amazon API Gateway REST and WebSocket APIs have logging enabled | ApiGateway | DETECTIVE | MEDIUM | Security Hub Control | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: Mixed (Config Rule, CF Hook, Security Hub)
- **Status**: Mixed (Available, Elective)
- **Priority**: Moderate

---

### AU-5(2): Response to Audit Logging Process Failures | Real-Time Alerts

Controls that provide alerts within defined time periods to personnel when audit logging process failures occur.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CT.EC2.PR.10 | Checks whether the Amazon EC2 launch template has detailed monitoring enabled | EC2 | PROACTIVE | LOW | CF Hook (Proactive) | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: CF Hook (Proactive)
- **Status**: Elective - Not Yet Enabled
- **Priority**: Low

---

### AU-6: Audit Record Review, Analysis, and Reporting

Controls that review and analyze system audit records for indications of inappropriate or unusual activity.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CONFIG.GUARDDUTY.DT.3 | Checks if Audit Log Monitoring for EKS is enabled for an Amazon GuardDuty detector | GuardDuty | DETECTIVE | HIGH | Config Rule | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: Config Rule (Conformance Pack)
- **Status**: Available
- **Priority**: High

---

### AU-6(1): Audit Record Review, Analysis, and Reporting | Automated Process Integration

Controls that integrate audit record review, analysis, and reporting using automated mechanisms.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| SH.GuardDuty.1 | Checks whether Amazon GuardDuty is enabled in your AWS account and region | GuardDuty | DETECTIVE | HIGH | Security Hub Control | Partially Covered |

**Enforcement details:**
- **Scope**: All OUs (Security Hub)
- **Mechanism**: Security Hub Control
- **Status**: Available
- **Priority**: High

---

### AU-12: Audit Record Generation

Controls that provide audit record generation capability for defined auditable events.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CONFIG.APPSYNC.DT.5 | Checks if an AWS AppSync API has logging enabled | AppSync | DETECTIVE | MEDIUM | Config Rule | Partially Covered |
| CONFIG.EC2.DT.7 | Checks if AWS Site-to-Site VPN connections have Amazon CloudWatch logging enabled for both tunnels | EC2 | DETECTIVE | MEDIUM | Config Rule | Partially Covered |
| CT.APIGATEWAY.PR.1 | Checks whether all methods in Amazon API Gateway stage have execution logging configured | ApiGateway | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| CT.APIGATEWAY.PR.2 | Ensures that AWS X-Ray tracing is enabled on Amazon API Gateway REST APIs | ApiGateway | PROACTIVE | LOW | CF Hook (Proactive) | Partially Covered |
| CT.APIGATEWAY.PR.4 | Checks whether Amazon API Gateway V2 stages have access logging enabled | ApiGatewayV2 | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| CT.APPSYNC.PR.1 | Checks whether an AWS AppSync GraphQL API sends logs to Amazon CloudWatch Logs | AppSync | PROACTIVE | MEDIUM | CF Hook (Proactive) | Partially Covered |
| SH.APIGateway.1 | Checks whether all stages of Amazon API Gateway REST and WebSocket APIs have logging enabled | ApiGateway | DETECTIVE | MEDIUM | Security Hub Control | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: Mixed (Config Rule, CF Hook, Security Hub)
- **Status**: Mixed (Available, Elective)
- **Priority**: Moderate

---

## CA — Assessment, Authorization, and Monitoring

### CA-3: Information Exchange

Controls that approve and manage the exchange of information between systems using defined agreements.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CT.EC2.PR.6 | Checks whether Amazon EC2 transit gateways are configured to accept Amazon VPC attachment requests automatically | EC2 | PROACTIVE | HIGH | CF Hook (Proactive) | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: CF Hook (Proactive)
- **Status**: Elective - Not Yet Enabled
- **Priority**: High

---

### CA-7: Continuous Monitoring

Controls that develop a system-level continuous monitoring strategy and implement continuous monitoring.

| Control ID | Description | AWS Service | Control Type | Severity | Implementation | Coverage |
|---|---|---|---|---|---|---|
| CONFIG.GUARDDUTY.DT.10 | Checks if Runtime Monitoring is enabled for Amazon GuardDuty detector | GuardDuty | DETECTIVE | HIGH | Config Rule | Partially Covered |
| CONFIG.GUARDDUTY.DT.2 | Checks if Malware Protection is enabled for an Amazon GuardDuty detector | GuardDuty | DETECTIVE | HIGH | Config Rule | Partially Covered |
| CONFIG.GUARDDUTY.DT.3 | Checks if Audit Log Monitoring for EKS is enabled for an Amazon GuardDuty detector | GuardDuty | DETECTIVE | HIGH | Config Rule | Partially Covered |
| CONFIG.GUARDDUTY.DT.4 | Checks if S3 Protection is enabled for an Amazon GuardDuty Detector | GuardDuty | DETECTIVE | HIGH | Config Rule | Partially Covered |
| CONFIG.GUARDDUTY.DT.5 | Checks if Amazon RDS protection is enabled for an Amazon GuardDuty detector | GuardDuty | DETECTIVE | HIGH | Config Rule | Partially Covered |
| CONFIG.GUARDDUTY.DT.6 | Checks if Lambda Protection is enabled for an Amazon GuardDuty detector | GuardDuty | DETECTIVE | HIGH | Config Rule | Partially Covered |
| CONFIG.GUARDDUTY.DT.7 | Checks if Amazon EKS Runtime Monitoring with automated agent management is enabled for GuardDuty | GuardDuty | DETECTIVE | MEDIUM | Config Rule | Partially Covered |
| CONFIG.GUARDDUTY.DT.8 | Checks if ECS Runtime Monitoring with automated agent management is enabled for Amazon GuardDuty detector | GuardDuty | DETECTIVE | MEDIUM | Config Rule | Partially Covered |
| CT.GUARDDUTY.PR.1 | Checks whether Amazon S3 protection is enabled on an Amazon GuardDuty detector | GuardDuty | PROACTIVE | HIGH | CF Hook (Proactive) | Partially Covered |

**Enforcement details:**
- **Scope**: Workload OU
- **Mechanism**: Mixed (Config Rule, CF Hook)
- **Status**: Mixed (Available, Elective)
- **Priority**: High

---

## Control Summary

| NIST 800-53 Control | Control Name | # AWS Controls | Types |
|---|---|---|---|
| AC-3 | Access Enforcement | 11 | Preventive (SCP, Declarative Policy), Proactive (CF Hook), Detective (Config Rule) |
| AC-4 | Information Flow Enforcement | 22 | Preventive (Declarative Policy), Proactive (CF Hook), Detective (Config Rule, Security Hub) |
| AC-6 | Least Privilege | 7 | Preventive (SCP, Declarative Policy), Proactive (CF Hook), Detective (Config Rule) |
| AC-6(1) | Least Privilege - Authorize Access to Security Functions | 4 | Preventive (SCP) |
| AC-6(10) | Least Privilege - Prohibit Non-Privileged Users | 2 | Preventive (SCP, Declarative Policy) |
| AC-6(9) | Least Privilege - Log Use of Privileged Functions | 1 | Detective (Security Hub) |
| AC-12 | Session Termination | 1 | Detective (Config Rule) |
| AC-17 | Remote Access | 1 | Preventive (SCP) |
| AC-17(1) | Remote Access - Monitoring and Control | 2 | Detective (Config Rule, Security Hub) |
| AC-17(3) | Remote Access - Managed Access Control Points | 3 | Proactive (CF Hook), Detective (Config Rule, Security Hub) |
| AC-22 | Publicly Accessible Content | 1 | Preventive (Declarative Policy) |
| AU-2 | Event Logging | 8 | Proactive (CF Hook), Detective (Config Rule, Security Hub) |
| AU-3 | Content of Audit Records | 6 | Proactive (CF Hook), Detective (Config Rule, Security Hub) |
| AU-5(2) | Response to Audit Logging Process Failures | 1 | Proactive (CF Hook) |
| AU-6 | Audit Record Review, Analysis, and Reporting | 1 | Detective (Config Rule) |
| AU-6(1) | Audit Record Review - Automated Process Integration | 1 | Detective (Security Hub) |
| AU-12 | Audit Record Generation | 7 | Proactive (CF Hook), Detective (Config Rule, Security Hub) |
| CA-3 | Information Exchange | 1 | Proactive (CF Hook) |
| CA-7 | Continuous Monitoring | 9 | Proactive (CF Hook), Detective (Config Rule) |

## Stage Applicability

When this extension is enabled, the AI-DLC workflow applies these controls to:
- **Requirements**: Access control (AC family), audit/logging (AU family), and continuous monitoring (CA family) requirements
- **Design**: Architecture constraints for SCP enforcement, network segmentation (AC-4), VPC flow controls, and GuardDuty integration
- **Infrastructure**: AWS Control Tower landing zone configuration, SCP policies, Security Hub enablement, GuardDuty protection settings, CloudWatch logging
- **Code Generation**: IAM policy patterns, least-privilege examples, security group rules, API authorization patterns
- **Testing**: Compliance verification for SCP enforcement, network isolation, logging coverage, and GuardDuty detector configuration

---

*v0.2.0 — Expanded AC family controls (AC-3 through AC-22), added AU family (Audit and Accountability), added CA family (Assessment, Authorization, and Monitoring). Future versions will add additional NIST 800-53 families (SC, SI, IA, etc.).*
