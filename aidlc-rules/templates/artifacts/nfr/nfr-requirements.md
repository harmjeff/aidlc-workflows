# NFR Requirements Template

Use this template to document non-functional requirements for a unit.

## Template

```markdown
# NFR Requirements - [unit-name]

**Unit Name:** [unit-name]
**Created:** [ISO 8601 timestamp]
**Version:** 1.0

---

## Overview

[High-level summary of NFR requirements for this unit. Explain the key non-functional concerns and priorities.]

---

## Performance Requirements

### Response Time Requirements
- **Target:** [Response time target - e.g., 200ms for 95th percentile]
- **Maximum:** [Maximum acceptable response time - e.g., 500ms]
- **Measurement:** [How response time is measured - e.g., from API gateway to response]

### Throughput Requirements
- **Target:** [Requests per second target - e.g., 1000 RPS]
- **Peak Load:** [Peak load expectations - e.g., 5000 RPS during peak hours]
- **Measurement:** [How throughput is measured]

### Latency Requirements
- **Target:** [Latency target - e.g., <50ms]
- **Maximum:** [Maximum acceptable latency - e.g., <100ms]
- **Measurement:** [How latency is measured]

### Resource Usage Constraints
- **CPU:** [CPU usage constraints - e.g., <70% average, <90% peak]
- **Memory:** [Memory usage constraints - e.g., <4GB per instance]
- **Storage:** [Storage requirements - e.g., 100GB initial, 1TB growth per year]
- **Network:** [Network bandwidth requirements - e.g., 1Gbps]

### Batch Processing Requirements
[If applicable, describe batch processing requirements]
- **Batch Size:** [Records per batch]
- **Processing Time:** [Time to process batch]
- **Frequency:** [How often batches run]

---

## Security Requirements

### Authentication Requirements
- **Mechanism:** [Authentication mechanism - e.g., OAuth 2.0, JWT, SAML]
- **Protocols:** [Authentication protocols - e.g., OpenID Connect]
- **Token Management:** [Token lifecycle and management - e.g., 1-hour expiry, refresh tokens]
- **Multi-Factor:** [MFA requirements if applicable]

### Authorization Requirements
- **Model:** [Authorization model - RBAC, ABAC, etc.]
- **Rules:** [Authorization rules - who can do what]
- **Enforcement Points:** [Where authorization is enforced - API gateway, service layer, etc.]
- **Granularity:** [Resource-level, operation-level, field-level]

### Data Protection Requirements
- **Encryption at Rest:** [Requirements for data at rest - e.g., AES-256]
- **Encryption in Transit:** [Requirements for data in transit - e.g., TLS 1.3]
- **Key Management:** [Key management strategy - e.g., AWS KMS, HashiCorp Vault]
- **Sensitive Data:** [How sensitive data is handled - masking, tokenization]

### Compliance Requirements
- **Standards:** [GDPR, HIPAA, PCI-DSS, SOC 2, etc.]
- **Audit Requirements:** [Audit logging requirements - what must be logged]
- **Data Retention:** [Data retention policies - how long data is kept]
- **Right to Erasure:** [How data deletion requests are handled]

### Privacy Requirements
- **PII Handling:** [How PII is handled - collection, storage, processing]
- **Data Anonymization:** [Anonymization requirements - when and how]
- **Consent Management:** [Consent tracking and management]
- **Data Minimization:** [Only collect necessary data]

### Security Testing Requirements
- **Vulnerability Scanning:** [Scanning frequency and tools - e.g., weekly SAST/DAST]
- **Penetration Testing:** [Penetration testing requirements - e.g., annual pen test]
- **Security Audits:** [Audit frequency and scope]
- **Dependency Scanning:** [Scan for vulnerable dependencies]

---

## Scalability Requirements

### Growth Expectations
- **User Growth:** [Expected user growth over time - e.g., 100K to 1M users in 2 years]
- **Data Growth:** [Expected data growth over time - e.g., 10TB per year]
- **Transaction Growth:** [Expected transaction growth - e.g., 2x per year]

### Geographic Distribution
- **Regions:** [Geographic regions to support - e.g., US-East, EU-West, APAC]
- **Latency Requirements:** [Latency requirements per region - e.g., <100ms within region]
- **Data Residency:** [Data residency requirements - e.g., EU data stays in EU]

### Scaling Strategy
- **Horizontal Scaling:** [Horizontal scaling approach - add more instances]
- **Vertical Scaling:** [Vertical scaling approach - increase instance size]
- **Auto-Scaling:** [Auto-scaling triggers and policies - e.g., scale at 70% CPU]
- **Database Scaling:** [Database scaling strategy - read replicas, sharding]

### Load Patterns
- **Typical Load:** [Typical load patterns - e.g., 1000 RPS during business hours]
- **Peak Load:** [Peak load patterns - e.g., 5000 RPS during promotions]
- **Seasonal Patterns:** [Seasonal or time-based patterns - e.g., holiday spikes]
- **Geographic Patterns:** [Load distribution across regions]

---

## Reliability Requirements

### Availability Requirements
- **Target Uptime:** [Uptime percentage - e.g., 99.9% (43 minutes downtime/month)]
- **Acceptable Downtime:** [Acceptable downtime per month/year]
- **Maintenance Windows:** [Planned maintenance windows - e.g., Sunday 2-4 AM]
- **SLA:** [Service level agreement commitments]

### Fault Tolerance Requirements
- **Single Point of Failure:** [SPOF elimination requirements - no SPOFs allowed]
- **Redundancy:** [Redundancy requirements - multi-AZ, multi-region]
- **Graceful Degradation:** [Degradation strategy - what features degrade first]
- **Circuit Breakers:** [Circuit breaker requirements for external dependencies]

### Disaster Recovery Requirements
- **RPO (Recovery Point Objective):** [Maximum acceptable data loss - e.g., 5 minutes]
- **RTO (Recovery Time Objective):** [Maximum acceptable downtime - e.g., 1 hour]
- **Backup Strategy:** [Backup frequency and retention - e.g., hourly backups, 30-day retention]
- **Restore Testing:** [Restore testing frequency - e.g., quarterly DR drills]
- **Failover Strategy:** [Automatic or manual failover]

### Data Consistency Requirements
- **Consistency Model:** [Strong, eventual, causal consistency]
- **Conflict Resolution:** [How conflicts are resolved - last-write-wins, custom logic]
- **Transaction Requirements:** [ACID vs. BASE - when each is needed]
- **Idempotency:** [Idempotency requirements for operations]

---

## Maintainability Requirements

### Code Quality Standards
- **Coding Standards:** [Coding standards to follow - e.g., language-specific style guides]
- **Code Review:** [Code review requirements - e.g., 2 approvals required]
- **Static Analysis:** [Static analysis tools and thresholds - e.g., SonarQube, 0 critical issues]
- **Complexity Limits:** [Cyclomatic complexity limits - e.g., <10 per function]

### Documentation Requirements
- **Code Documentation:** [Inline documentation requirements - e.g., all public APIs documented]
- **API Documentation:** [API documentation requirements - e.g., OpenAPI/Swagger]
- **Architecture Documentation:** [Architecture documentation requirements - e.g., C4 diagrams]
- **Runbooks:** [Operational runbooks for common tasks]

### Testing Requirements
- **Unit Test Coverage:** [Target coverage percentage - e.g., >80%]
- **Integration Test Coverage:** [Integration test requirements - all API endpoints]
- **E2E Test Coverage:** [End-to-end test requirements - critical user journeys]
- **Performance Test Coverage:** [Performance test requirements - load and stress tests]
- **Test Automation:** [Test automation requirements - CI/CD integration]

### Monitoring and Observability
- **Metrics:** [Key metrics to track - e.g., latency, error rate, throughput]
- **Dashboards:** [Dashboard requirements - real-time operational dashboards]
- **Alerting:** [Alerting rules and thresholds - e.g., alert on >5% error rate]
- **Tracing:** [Distributed tracing requirements - e.g., trace all requests]
- **Health Checks:** [Health check endpoints and frequency]

### Logging Requirements
- **Log Levels:** [Log level requirements - INFO for normal, DEBUG for troubleshooting]
- **Log Retention:** [Log retention policies - e.g., 30 days hot, 1 year cold]
- **Log Aggregation:** [Log aggregation strategy - e.g., centralized logging]
- **Structured Logging:** [Structured logging requirements - JSON format]
- **Sensitive Data:** [No PII or secrets in logs]

### Deployment Requirements
- **Deployment Frequency:** [Expected deployment frequency - e.g., multiple times per day]
- **Deployment Strategy:** [Blue-green, canary, rolling, etc.]
- **Rollback Requirements:** [Rollback strategy and time - e.g., <5 minutes]
- **Zero-Downtime Deployment:** [Zero-downtime requirements - yes/no]
- **Database Migrations:** [How database migrations are handled]

---

## Usability Requirements

[If applicable, document usability requirements]

### Accessibility
- **Standards:** [WCAG 2.1 Level AA, Section 508, etc.]
- **Screen Reader Support:** [Screen reader compatibility requirements]
- **Keyboard Navigation:** [Keyboard navigation requirements]

### Internationalization
- **Languages:** [Languages to support]
- **Localization:** [Localization requirements]
- **Time Zones:** [Time zone handling]
- **Currency:** [Currency handling]

---

## Compatibility Requirements

[If applicable, document compatibility requirements]

### Browser Compatibility
- **Browsers:** [Supported browsers and versions]
- **Mobile Browsers:** [Mobile browser support]

### API Compatibility
- **Versioning:** [API versioning strategy]
- **Backward Compatibility:** [Backward compatibility requirements]
- **Deprecation Policy:** [How APIs are deprecated]

### Integration Compatibility
- **External Systems:** [Systems that must integrate]
- **Protocols:** [Required protocols and versions]
- **Data Formats:** [Required data formats]

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
- During NFR Requirements stage for each unit
- When documenting non-functional requirements
- When making technology decisions

### Customization
- Remove sections not applicable to your unit
- Add sections for unit-specific NFR concerns
- Adjust detail level based on complexity
- Focus on requirements that matter for this specific unit

### Best Practices
- Be specific and measurable - use numbers and metrics
- Include rationale for requirements
- Consider trade-offs between different NFRs
- Align with business priorities
- Document assumptions and constraints

### Common Mistakes to Avoid
- ❌ Being too vague ("fast", "secure", "scalable")
- ❌ Not specifying measurable targets
- ❌ Ignoring trade-offs between requirements
- ❌ Not considering operational requirements
- ❌ Forgetting about monitoring and observability
- ❌ Not documenting compliance requirements

