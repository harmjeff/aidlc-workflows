# Infrastructure Design Template

Use this template to document infrastructure services and resource specifications for a unit.

## Template

```markdown
# Infrastructure Design - [unit-name]

**Unit Name:** [unit-name]
**Created:** [ISO 8601 timestamp]
**Version:** 1.0

---

## Overview

[High-level summary of infrastructure design for this unit. Explain the infrastructure services and how they support the application.]

---

## Compute Resources

### Application Servers

**Service:** [ECS, Lambda, EC2, App Service, Cloud Run, etc.]

**Configuration:**
- **Instance Type:** [Instance size/type]
- **CPU:** [CPU allocation]
- **Memory:** [Memory allocation]
- **Storage:** [Storage configuration]
- **Auto-Scaling:** [Auto-scaling configuration]

**Rationale:** [Why this compute service was chosen]

### Background Workers

[If applicable]

**Service:** [Service choice]

**Configuration:**
- [Configuration details]

---

## Storage Resources

### Database

**Service:** [RDS, DynamoDB, Cosmos DB, Cloud SQL, etc.]

**Configuration:**
- **Engine:** [PostgreSQL, MySQL, MongoDB, etc.]
- **Version:** [Version]
- **Instance Type:** [Instance size]
- **Storage:** [Storage size and type]
- **Backup:** [Backup configuration]
- **Multi-AZ:** [Yes/No]
- **Read Replicas:** [Configuration if applicable]

**Rationale:** [Why this database service was chosen]

### Object Storage

**Service:** [S3, Blob Storage, Cloud Storage, etc.]

**Configuration:**
- **Bucket/Container:** [Name and purpose]
- **Storage Class:** [Standard, Infrequent Access, Archive]
- **Versioning:** [Enabled/Disabled]
- **Lifecycle Policies:** [Lifecycle rules]
- **Encryption:** [Encryption configuration]

**Rationale:** [Why this storage service was chosen]

### Cache

**Service:** [ElastiCache, Redis, Memcached, etc.]

**Configuration:**
- **Engine:** [Redis, Memcached]
- **Version:** [Version]
- **Node Type:** [Node size]
- **Number of Nodes:** [Node count]
- **Cluster Mode:** [Enabled/Disabled]

**Rationale:** [Why this cache service was chosen]

---

## Networking Resources

### VPC/Virtual Network

**Configuration:**
- **CIDR Block:** [IP range]
- **Subnets:** [Public, private, database subnets]
- **Availability Zones:** [AZ configuration]
- **NAT Gateway:** [Configuration]
- **Internet Gateway:** [Configuration]

### Load Balancer

**Service:** [ALB, NLB, Application Gateway, Load Balancer, etc.]

**Configuration:**
- **Type:** [Application, Network, Classic]
- **Scheme:** [Internet-facing, Internal]
- **Listeners:** [Port and protocol configuration]
- **Target Groups:** [Target group configuration]
- **Health Checks:** [Health check configuration]
- **SSL/TLS:** [Certificate configuration]

**Rationale:** [Why this load balancer was chosen]

### API Gateway

[If applicable]

**Service:** [API Gateway, APIM, Kong, etc.]

**Configuration:**
- **API Type:** [REST, HTTP, WebSocket]
- **Authorization:** [Authorization configuration]
- **Throttling:** [Rate limiting configuration]
- **Caching:** [Cache configuration]
- **Custom Domain:** [Domain configuration]

**Rationale:** [Why this API gateway was chosen]

### DNS

**Service:** [Route 53, Azure DNS, Cloud DNS, etc.]

**Configuration:**
- **Hosted Zone:** [Domain]
- **Records:** [DNS records]
- **Routing Policy:** [Simple, weighted, latency-based, etc.]
- **Health Checks:** [Health check configuration]

---

## Message Queue / Event Bus

[If applicable]

**Service:** [SQS, SNS, EventBridge, Service Bus, Pub/Sub, etc.]

**Configuration:**
- **Queue/Topic Name:** [Name]
- **Message Retention:** [Retention period]
- **Visibility Timeout:** [Timeout]
- **Dead Letter Queue:** [DLQ configuration]
- **Encryption:** [Encryption configuration]

**Rationale:** [Why this messaging service was chosen]

---

## Security Resources

### Identity and Access Management

**Service:** [IAM, Azure AD, Cloud IAM, etc.]

**Configuration:**
- **Roles:** [IAM roles]
- **Policies:** [IAM policies]
- **Service Accounts:** [Service account configuration]
- **Least Privilege:** [How least privilege is enforced]

### Secrets Management

**Service:** [Secrets Manager, Key Vault, Secret Manager, etc.]

**Configuration:**
- **Secrets:** [What secrets are stored]
- **Rotation:** [Rotation policy]
- **Access Control:** [Who can access secrets]

### Encryption Keys

**Service:** [KMS, Key Vault, Cloud KMS, etc.]

**Configuration:**
- **Keys:** [Encryption keys]
- **Key Rotation:** [Rotation policy]
- **Key Usage:** [What keys encrypt]

### Web Application Firewall

[If applicable]

**Service:** [WAF, Azure WAF, Cloud Armor, etc.]

**Configuration:**
- **Rules:** [WAF rules]
- **Rate Limiting:** [Rate limiting rules]
- **IP Filtering:** [IP whitelist/blacklist]

---

## Monitoring and Logging

### Monitoring

**Service:** [CloudWatch, Azure Monitor, Cloud Monitoring, etc.]

**Configuration:**
- **Metrics:** [Key metrics to monitor]
- **Dashboards:** [Dashboard configuration]
- **Alarms:** [Alarm configuration]
- **Retention:** [Metrics retention]

### Logging

**Service:** [CloudWatch Logs, Log Analytics, Cloud Logging, etc.]

**Configuration:**
- **Log Groups:** [Log group configuration]
- **Log Retention:** [Retention period]
- **Log Aggregation:** [Aggregation strategy]
- **Log Analysis:** [Analysis tools]

### Tracing

**Service:** [X-Ray, Application Insights, Cloud Trace, etc.]

**Configuration:**
- **Sampling:** [Sampling rate]
- **Trace Retention:** [Retention period]
- **Service Map:** [Service map configuration]

---

## Backup and Disaster Recovery

### Backup Strategy

**Database Backups:**
- **Frequency:** [Backup frequency]
- **Retention:** [Retention period]
- **Backup Type:** [Full, incremental, snapshot]

**File Backups:**
- **Frequency:** [Backup frequency]
- **Retention:** [Retention period]
- **Backup Location:** [Where backups are stored]

### Disaster Recovery

**RPO:** [Recovery Point Objective]

**RTO:** [Recovery Time Objective]

**DR Strategy:**
- **Primary Region:** [Primary region]
- **DR Region:** [DR region]
- **Failover:** [Failover strategy]
- **Data Replication:** [Replication strategy]

---

## Cost Optimization

**Cost Estimates:**
- **Compute:** [Estimated monthly cost]
- **Storage:** [Estimated monthly cost]
- **Networking:** [Estimated monthly cost]
- **Other Services:** [Estimated monthly cost]
- **Total:** [Total estimated monthly cost]

**Cost Optimization Strategies:**
- [Strategy 1 - e.g., Use reserved instances]
- [Strategy 2 - e.g., Implement auto-scaling]
- [Strategy 3 - e.g., Use lifecycle policies for storage]

---

## Infrastructure as Code

**Tool:** [Terraform, CloudFormation, ARM Templates, Deployment Manager, etc.]

**Repository:** [Where IaC code is stored]

**Modules:** [IaC modules used]

**State Management:** [How state is managed]

---

## Compliance and Governance

**Compliance Requirements:**
- [Requirement 1 - e.g., GDPR, HIPAA]
- [Requirement 2]

**Governance Policies:**
- [Policy 1 - e.g., Tagging policy]
- [Policy 2 - e.g., Resource naming convention]

**Audit Trail:**
- [How infrastructure changes are audited]

---

## Notes

[Additional notes, assumptions, or considerations]

- [Note 1]
- [Note 2]
- [Continue as needed]

---

**Document Status:** [Draft/Review/Approved]
**Last Updated:** [ISO 8601 timestamp]
**Updated By:** [Name/Role]
```

## Usage Guidelines

### When to Use
- During Infrastructure Design stage for each unit
- When mapping infrastructure services
- When specifying cloud resources

### Customization
- Remove services not applicable to your unit
- Add cloud-specific services
- Adjust detail level based on complexity
- Focus on services relevant to your unit

### Best Practices
- Be specific about resource configurations
- Document rationale for service choices
- Consider cost implications
- Think about disaster recovery
- Document security configurations
- Use Infrastructure as Code

### Common Mistakes to Avoid
- ❌ Not documenting resource configurations
- ❌ Forgetting about backup and DR
- ❌ Not considering cost optimization
- ❌ Ignoring security best practices
- ❌ Not using Infrastructure as Code
- ❌ Forgetting about monitoring and logging

