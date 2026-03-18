# NFR Design Patterns Template

Use this template to document NFR design patterns and their implementation for a unit.

## Template

```markdown
# NFR Design Patterns - [unit-name]

**Unit Name:** [unit-name]
**Created:** [ISO 8601 timestamp]
**Version:** 1.0

---

## Overview

[High-level summary of NFR design patterns for this unit. Explain how NFR requirements are addressed through design patterns.]

---

## Performance Patterns

### Caching Strategy

**Pattern:** [Caching pattern - cache-aside, write-through, write-behind, read-through]

**Implementation:**
- **Cache Location:** [Where cache is implemented - application, distributed, CDN]
- **Cache Key Strategy:** [How cache keys are generated]
- **Cache Invalidation:** [How cache is invalidated - TTL, event-based, manual]
- **TTL Strategy:** [Time-to-live settings for different data types]

**Cached Data:**
- **[Data type 1]:** TTL: [duration], Invalidation: [strategy]
- **[Data type 2]:** TTL: [duration], Invalidation: [strategy]

**Cache Miss Handling:** [What happens on cache miss]

### Asynchronous Processing

**Pattern:** [Async pattern - message queue, event-driven, async/await]

**Implementation:**
- **Async Operations:** [Which operations are async - e.g., email sending, report generation]
- **Message Queue:** [Queue technology and configuration]
- **Error Handling:** [How async errors are handled]
- **Retry Strategy:** [Retry logic for failed operations]
- **Dead Letter Queue:** [DLQ configuration]

### Database Optimization

**Pattern:** [Optimization patterns - connection pooling, query optimization, caching]

**Implementation:**
- **Connection Pooling:** [Pool size, timeout, configuration]
- **Query Optimization:** [Indexing strategy, query patterns, N+1 prevention]
- **Batch Operations:** [Batch processing approach]
- **Read Replicas:** [Read replica strategy if applicable]
- **Pagination:** [Pagination strategy for large result sets]

### Response Compression

**Pattern:** [Compression strategy]

**Implementation:**
- **Compression Algorithm:** [gzip, brotli, etc.]
- **Compression Threshold:** [Minimum size for compression]
- **Content Types:** [Which content types are compressed]

### Other Performance Patterns

[Additional performance patterns as needed]

---

## Security Patterns

### Authentication Pattern

**Pattern:** [Auth pattern - JWT, OAuth 2.0, session-based, API keys]

**Implementation:**
- **Authentication Flow:** [Detailed auth flow - login, token generation, validation]
- **Token Management:** [Token generation, validation, refresh, revocation]
- **Session Management:** [Session handling if applicable]
- **Multi-Factor Authentication:** [MFA implementation if required]
- **Password Policy:** [Password requirements and hashing]

### Authorization Pattern

**Pattern:** [Authorization pattern - RBAC, ABAC, ACL]

**Implementation:**
- **Authorization Model:** [Detailed authorization model]
- **Permission Checking:** [Where and how permissions are checked]
- **Role Management:** [How roles are defined and assigned]
- **Policy Enforcement:** [Policy enforcement points - API gateway, service layer]
- **Resource-Level Authorization:** [Fine-grained authorization]

### Encryption Pattern

**Pattern:** [Encryption approach]

**Implementation:**
- **Data at Rest:** [Encryption for stored data - algorithm, key size]
- **Data in Transit:** [TLS/SSL configuration - version, cipher suites]
- **Key Management:** [How encryption keys are managed - KMS, Vault]
- **Sensitive Data:** [Which data is encrypted - PII, credentials, etc.]
- **Field-Level Encryption:** [If applicable]

### Input Validation Pattern

**Pattern:** [Validation approach]

**Implementation:**
- **Validation Points:** [Where validation occurs - API gateway, service layer]
- **Validation Rules:** [Validation rule implementation]
- **Sanitization:** [Input sanitization approach - XSS prevention, SQL injection]
- **Error Handling:** [Validation error handling and messaging]
- **Whitelist vs Blacklist:** [Validation strategy]

### Audit Logging Pattern

**Pattern:** [Audit logging approach]

**Implementation:**
- **Logged Events:** [What events are logged - authentication, authorization, data changes]
- **Log Format:** [Structured logging format - JSON]
- **Log Storage:** [Where logs are stored - centralized logging]
- **Log Retention:** [Retention policy]
- **Sensitive Data:** [How sensitive data is handled in logs - masking, redaction]

### Rate Limiting Pattern

**Pattern:** [Rate limiting strategy]

**Implementation:**
- **Rate Limit Algorithm:** [Token bucket, leaky bucket, fixed window, sliding window]
- **Limits:** [Rate limits per user, IP, API key]
- **Enforcement Point:** [Where rate limiting is enforced]
- **Response:** [How rate limit violations are communicated]

### Other Security Patterns

[Additional security patterns as needed]

---

## Scalability Patterns

### Load Balancing Pattern

**Pattern:** [Load balancing approach]

**Implementation:**
- **Load Balancer Type:** [Application, network, DNS]
- **Balancing Algorithm:** [Round-robin, least connections, weighted, IP hash]
- **Health Checks:** [Health check configuration - endpoint, frequency, timeout]
- **Session Affinity:** [Sticky sessions if needed]
- **SSL Termination:** [Where SSL is terminated]

### Stateless Design Pattern

**Pattern:** [Stateless design approach]

**Implementation:**
- **State Management:** [How state is externalized - Redis, database]
- **Session Storage:** [External session storage]
- **Request Context:** [How request context is managed]
- **Horizontal Scaling:** [How stateless design enables scaling]
- **Shared Nothing:** [Shared nothing architecture]

### Data Partitioning Pattern

**Pattern:** [Partitioning strategy - sharding, partitioning, federation]

**Implementation:**
- **Partition Key:** [How data is partitioned - user ID, tenant ID, geographic]
- **Partition Strategy:** [Range, hash, list partitioning]
- **Cross-Partition Queries:** [How cross-partition queries are handled]
- **Rebalancing:** [Partition rebalancing strategy]
- **Hotspot Prevention:** [How hotspots are avoided]

### Auto-Scaling Pattern

**Pattern:** [Auto-scaling strategy]

**Implementation:**
- **Scaling Triggers:** [CPU, memory, request count, custom metrics]
- **Scaling Policy:** [Target tracking, step scaling, scheduled]
- **Scale-Out:** [How instances are added]
- **Scale-In:** [How instances are removed]
- **Cooldown Period:** [Cooldown between scaling actions]

### Other Scalability Patterns

[Additional scalability patterns as needed]

---

## Reliability Patterns

### Retry Pattern

**Pattern:** [Retry strategy]

**Implementation:**
- **Retry Logic:** [When and how retries occur]
- **Retry Count:** [Maximum retry attempts]
- **Backoff Strategy:** [Exponential backoff, fixed delay, jitter]
- **Idempotency:** [How idempotency is ensured]
- **Retry Conditions:** [Which errors trigger retries]

### Circuit Breaker Pattern

**Pattern:** [Circuit breaker implementation]

**Implementation:**
- **Failure Threshold:** [When circuit opens - error rate, error count]
- **Timeout:** [Circuit breaker timeout]
- **Half-Open State:** [How circuit transitions to half-open]
- **Fallback:** [Fallback behavior when circuit is open]
- **Reset Strategy:** [How circuit resets to closed]

### Fallback Pattern

**Pattern:** [Fallback strategy]

**Implementation:**
- **Fallback Triggers:** [When fallback is activated]
- **Fallback Behavior:** [What happens in fallback mode - cached data, default values]
- **Degraded Functionality:** [What functionality is degraded]
- **Recovery:** [How system recovers from fallback]

### Timeout Pattern

**Pattern:** [Timeout strategy]

**Implementation:**
- **Timeout Values:** [Timeout configuration per operation]
- **Timeout Handling:** [How timeouts are handled]
- **Cascading Timeouts:** [How timeouts propagate through call chain]
- **Timeout Budget:** [Total timeout budget for request]

### Health Check Pattern

**Pattern:** [Health check approach]

**Implementation:**
- **Health Endpoints:** [Health check endpoints - /health, /ready, /live]
- **Health Checks:** [What is checked - database, cache, dependencies]
- **Health Status:** [Health status reporting - healthy, degraded, unhealthy]
- **Dependency Checks:** [Checking dependent services]
- **Startup Probes:** [Startup health checks]

### Bulkhead Pattern

**Pattern:** [Bulkhead isolation strategy]

**Implementation:**
- **Resource Pools:** [Separate resource pools for different operations]
- **Thread Pools:** [Thread pool configuration]
- **Connection Pools:** [Connection pool isolation]
- **Failure Isolation:** [How failures are isolated]

### Other Reliability Patterns

[Additional reliability patterns as needed]

---

## Integration Patterns

[Patterns for integrating with external systems or other units]

### Integration 1: [Name]

**Pattern:** [Integration pattern - REST, GraphQL, gRPC, messaging, event-driven]

**Implementation:**
- **Communication Style:** [Synchronous, asynchronous]
- **Data Format:** [JSON, XML, Protobuf, Avro]
- **Error Handling:** [How integration errors are handled]
- **Retry Logic:** [Retry strategy for integration]
- **Timeout:** [Integration timeout]
- **Circuit Breaker:** [Circuit breaker for integration]

[Repeat for all integrations]

---

## Observability Patterns

### Logging Pattern

**Pattern:** [Logging strategy]

**Implementation:**
- **Log Levels:** [DEBUG, INFO, WARN, ERROR]
- **Structured Logging:** [JSON structured logging]
- **Correlation IDs:** [Request correlation across services]
- **Log Aggregation:** [Centralized logging]

### Metrics Pattern

**Pattern:** [Metrics collection strategy]

**Implementation:**
- **Metrics Types:** [Counter, gauge, histogram, summary]
- **Key Metrics:** [Latency, error rate, throughput, saturation]
- **Metrics Aggregation:** [How metrics are aggregated]
- **Dashboards:** [Key dashboards]

### Tracing Pattern

**Pattern:** [Distributed tracing strategy]

**Implementation:**
- **Trace Context:** [How trace context is propagated]
- **Span Creation:** [When spans are created]
- **Sampling:** [Sampling strategy]
- **Trace Aggregation:** [Centralized tracing]

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
- During NFR Design stage for each unit
- When documenting how NFR requirements are implemented
- When defining design patterns for the unit

### Customization
- Remove patterns not applicable to your unit
- Add unit-specific patterns
- Focus on patterns that address your NFR requirements
- Document rationale for pattern choices

### Best Practices
- Link patterns to specific NFR requirements
- Be specific about implementation details
- Document trade-offs and alternatives
- Consider operational complexity
- Think about monitoring and debugging

### Common Mistakes to Avoid
- ❌ Applying patterns without understanding trade-offs
- ❌ Over-engineering with unnecessary patterns
- ❌ Not documenting implementation details
- ❌ Forgetting about operational complexity
- ❌ Not considering monitoring and observability

