# Infrastructure Design Stage

**Purpose:** Map infrastructure services, define deployment architecture, and specify cloud resources for a specific unit of work.

**Stage Type:** CONDITIONAL (per-unit)

**Phase:** CONSTRUCTION

**Load this file when:** Starting Infrastructure Design stage for a unit

**Unload this file after:** Infrastructure Design stage completes and user approves

---

## Execute IF

Execute this stage if ANY of the following conditions are met:
- Infrastructure services need to be mapped for this unit
- Deployment architecture needs to be defined
- Cloud resources need to be specified
- Infrastructure as Code needs to be created

## Skip IF

Skip this stage if ALL of the following conditions are met:
- No infrastructure changes required
- Infrastructure is already well-defined
- Unit uses existing infrastructure

---

## Prerequisites

Before starting this stage, ensure:
1. NFR Requirements artifacts exist (if NFR Requirements stage was executed)
2. NFR Design artifacts exist (if NFR Design stage was executed)
3. Technology stack decisions have been made
4. Unit of work is defined in `unit-of-work.md`

---

## Detailed Steps

### Step 1: Log User Input
**Action:** Log any user input during this stage in `audit.md`.

**Template:** `../../templates/audit-logs/basic-entry.md`

**Log with:**
- Stage: Infrastructure Design - [unit-name]
- Complete raw user input (never summarize)
- ISO 8601 timestamp

### Step 2: Load Context
**Action:** Read and analyze relevant artifacts:

**Required Artifacts:**
- `aidlc-docs/construction/{unit-name}/nfr-requirements/tech-stack-decisions.md` - Tech stack decisions

**Optional Artifacts (if they exist):**
- `aidlc-docs/construction/{unit-name}/nfr-requirements/nfr-requirements.md` - NFR requirements
- `aidlc-docs/construction/{unit-name}/nfr-design/` - NFR design artifacts
- `aidlc-docs/inception/application-design/unit-of-work.md` - Unit definition

### Step 3: Analyze Infrastructure Needs
**Action:** Analyze the unit to understand infrastructure requirements:
- Compute requirements (servers, containers, serverless)
- Storage requirements (database, object storage, cache)
- Networking requirements (load balancer, API gateway, VPC)
- Security requirements (IAM, secrets, encryption)
- Monitoring and logging requirements
- Backup and disaster recovery requirements

### Step 4: Create Infrastructure Design Plan
**Action:** Create detailed plan with checkboxes for tracking progress.

**File Location:** `aidlc-docs/construction/plans/{unit-name}-infrastructure-design-plan.md`

**Template:** `../../templates/plans/stage-plan-base.md`

**Customize with:**
- Infrastructure requirements summary
- Infrastructure design specific steps
- Question categories
- Expected artifacts (infrastructure-design.md, deployment-architecture.md)

**Plan Steps:**
```markdown
### Planning Phase
- [ ] 1. Analyze infrastructure requirements
- [ ] 2. Generate clarifying questions
- [ ] 3. Collect user answers
- [ ] 4. Analyze answers for ambiguities
- [ ] 5. Create follow-up questions (if needed)
- [ ] 6. Resolve all ambiguities
- [ ] 7. Get user approval to proceed

### Generation Phase
- [ ] 8. Map compute resources
- [ ] 9. Map storage resources
- [ ] 10. Map networking resources
- [ ] 11. Map security resources
- [ ] 12. Define deployment architecture
- [ ] 13. Create infrastructure-design.md
- [ ] 14. Create deployment-architecture.md
- [ ] 15. Present completion message
- [ ] 16. Get user approval
```

### Step 5: Generate Clarifying Questions
**Action:** Generate questions about infrastructure design.

**Question Categories to Evaluate:**
1. **Compute Resources** - Servers, containers, serverless, scaling
2. **Storage Resources** - Database, object storage, cache, backup
3. **Networking** - Load balancer, API gateway, VPC, DNS
4. **Security** - IAM, secrets, encryption, WAF
5. **Monitoring** - Metrics, logging, tracing, alerting
6. **Deployment** - Deployment strategy, environments, CI/CD
7. **Disaster Recovery** - Backup, failover, RPO/RTO

**Question Format:** `../../templates/questions/multiple-choice-format.md`

**Critical Requirements:**
- Use multiple choice format (A, B, C, D, E)
- **MANDATORY:** Include "Other" as LAST option
- Only include meaningful options
- Use [Answer]: tags for responses

### Step 6: Embed Questions in Plan
**Action:** Add all generated questions to the plan file's "Clarifying Questions" section.

### Step 7: Present Plan to User
**Action:** Inform user that the plan is ready and request answers.

**Message:**
```markdown
# 📋 Infrastructure Design Plan Ready - [unit-name]

Plan Location: `aidlc-docs/construction/plans/{unit-name}-infrastructure-design-plan.md`

Please review the plan and answer the infrastructure questions using [Answer]: tags.
```

### Step 8: Collect User Answers
**Action:** Once user confirms, read the plan file and extract answers after [Answer]: tags.

### Step 9: Analyze Answers for Ambiguities
**Action:** **MANDATORY** - Analyze all answers for ambiguities.

**Ambiguity Indicators:**
- "depends", "maybe", "not sure", "mix of", "somewhere between", "standard", "typical"
- Contradictions between answers
- Vague or incomplete responses

**If ambiguities found:** Create clarification file (Step 10)
**If no ambiguities:** Skip to Step 12

### Step 10: Create Follow-Up Questions
**Action:** Create clarification file if ambiguities were found.

**File Location:** `aidlc-docs/construction/plans/{unit-name}-infrastructure-design-clarifications.md`

**Template:** `../../templates/questions/clarification-format.md`

**For each ambiguity:**
- Quote the ambiguous answer
- Explain the issue
- Ask specific follow-up question
- Provide clear options

### Step 11: Repeat Until Resolved
**Action:** Repeat Steps 8-10 until ALL ambiguities are resolved.

**CRITICAL:** Do NOT proceed until complete clarity is achieved.

### Step 12: Get User Approval to Proceed
**Action:** Request approval to proceed with generation phase.

**Log approval prompt** in audit.md with timestamp.

### Step 13: Update Plan Progress
**Action:** Mark planning phase steps (1-7) as [x] in the plan file.

**CRITICAL:** Update in SAME interaction where work is completed.

### Step 14: Generate Infrastructure Design Document
**Action:** Create infrastructure design document.

**File Location:** `aidlc-docs/construction/{unit-name}/infrastructure-design/infrastructure-design.md`

**Template:** `../../templates/artifacts/infrastructure/infrastructure-design.md`

**Include:**
- Overview of infrastructure design
- Compute resources (application servers, workers)
- Storage resources (database, object storage, cache)
- Networking resources (VPC, load balancer, API gateway, DNS)
- Message queue/event bus (if applicable)
- Security resources (IAM, secrets, encryption, WAF)
- Monitoring and logging
- Backup and disaster recovery
- Cost optimization
- Infrastructure as Code
- Compliance and governance

**Update plan:** Mark steps 8-13 as [x] immediately after creating file.

### Step 15: Generate Deployment Architecture Document
**Action:** Create deployment architecture document.

**File Location:** `aidlc-docs/construction/{unit-name}/infrastructure-design/deployment-architecture.md`

**Template:** `../../templates/artifacts/infrastructure/deployment-architecture.md`

**Include:**
- Overview of deployment architecture
- Deployment model (single-region, multi-region)
- Deployment topology and component distribution
- Deployment environments (dev, staging, production)
- Deployment strategy (blue-green, canary, rolling)
- Zero-downtime deployment approach
- Scaling strategy (horizontal, vertical)
- High availability configuration
- Network architecture
- Deployment pipeline
- Monitoring and alerting
- Disaster recovery
- Security considerations
- Runbooks

**Update plan:** Mark step 14 as [x] immediately after creating file.

### Step 16: Update State Tracking
**Action:** Update `aidlc-docs/aidlc-state.md` to reflect completion.

**Template:** `../../templates/state/aidlc-state.md`

### Step 17: Present Completion Message
**Action:** Present standardized 2-option completion message.

**Template:** `../../templates/completion-messages/2-option-standard.md`

**MANDATORY FORMAT:**
```markdown
# 🔧 Infrastructure Design Complete - [unit-name]

Artifacts Created:
- ✅ `infrastructure-design.md` - Infrastructure services and resources
- ✅ `deployment-architecture.md` - Deployment architecture and strategy

Location: `aidlc-docs/construction/{unit-name}/infrastructure-design/`

---

What would you like to do?

🔧 **Request Changes** - Ask for modifications
✅ **Continue to Next Stage** - Approve and proceed

---
```

**CRITICAL:** Do NOT create 3-option menus or emergent navigation patterns.

### Step 18: Wait for User Response
**Action:** **WAIT FOR EXPLICIT APPROVAL** - Do NOT proceed until user confirms.

**Handle response:**
- If "Request Changes" → Make modifications and return to Step 17
- If "Continue" → Proceed to Step 19

### Step 19: Log User Approval
**Action:** Record approval in audit.md with complete raw input.

**Template:** `../../templates/audit-logs/basic-entry.md`

### Step 20: Update Final Plan Progress
**Action:** Mark all remaining steps as [x] in the plan file.

---

## Artifacts Created

1. **Plan:** `aidlc-docs/construction/plans/{unit-name}-infrastructure-design-plan.md`
2. **Infrastructure Design:** `aidlc-docs/construction/{unit-name}/infrastructure-design/infrastructure-design.md`
3. **Deployment Architecture:** `aidlc-docs/construction/{unit-name}/infrastructure-design/deployment-architecture.md`
4. **Clarifications (if needed):** `aidlc-docs/construction/plans/{unit-name}-infrastructure-design-clarifications.md`

**Artifact Templates:** See `../../templates/artifacts/infrastructure/` directory

---

## Key Principles

1. **Infrastructure as Code:** Always use IaC for infrastructure
2. **Cloud-Native Services:** Prefer managed services over self-managed
3. **Ambiguity Resolution:** MUST analyze answers and create follow-ups
4. **Immediate Progress Tracking:** Update checkboxes in SAME interaction
5. **Standardized Completion:** MUST use 2-option format (no emergent behavior)
6. **Complete Audit Trail:** Log ALL user inputs with complete raw input
7. **Explicit Approval:** WAIT for user approval before proceeding

---

## Templates Reference

All templates are located in `../../templates/` directory:

- **Audit Logs:** `audit-logs/basic-entry.md`
- **Plans:** `plans/stage-plan-base.md`
- **Questions:** `questions/multiple-choice-format.md`, `questions/clarification-format.md`
- **Artifacts:** `artifacts/infrastructure/*.md`
- **Completion:** `completion-messages/2-option-standard.md`
- **State:** `state/aidlc-state.md`

---

## Next Stage

After approval:
- **Code Generation** stage

---

**End of Infrastructure Design Stage Instructions**
