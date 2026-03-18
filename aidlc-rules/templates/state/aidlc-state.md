# AIDLC State Tracking Template

This template defines the structure for `aidlc-docs/aidlc-state.md` which tracks workflow progress.

## Template

```markdown
# AIDLC Workflow State

**Last Updated**: [ISO 8601 timestamp]
**Project Type**: [Greenfield/Brownfield]
**Current Phase**: [INCEPTION/CONSTRUCTION/OPERATIONS]
**Current Stage**: [Stage name]

---

## Workflow Progress

### 🔵 INCEPTION PHASE

- [x] **Workspace Detection** - [Timestamp] - [Status: COMPLETED]
- [x/⏭️/  ] **Reverse Engineering** - [Timestamp] - [Status: COMPLETED/SKIPPED/PENDING]
- [x/  ] **Requirements Analysis** - [Timestamp] - [Status: COMPLETED/PENDING]
- [x/⏭️/  ] **User Stories** - [Timestamp] - [Status: COMPLETED/SKIPPED/PENDING]
- [x/  ] **Workflow Planning** - [Timestamp] - [Status: COMPLETED/PENDING]
- [x/⏭️/  ] **Application Design** - [Timestamp] - [Status: COMPLETED/SKIPPED/PENDING]
- [x/⏭️/  ] **Units Generation** - [Timestamp] - [Status: COMPLETED/SKIPPED/PENDING]

### 🟢 CONSTRUCTION PHASE

**Per-Unit Progress:**

#### Unit: [unit-name-1]
- [x/⏭️/  ] **Functional Design** - [Timestamp] - [Status]
- [x/⏭️/  ] **NFR Requirements** - [Timestamp] - [Status]
- [x/⏭️/  ] **NFR Design** - [Timestamp] - [Status]
- [x/⏭️/  ] **Infrastructure Design** - [Timestamp] - [Status]
- [x/  ] **Code Generation** - [Timestamp] - [Status]

#### Unit: [unit-name-2]
- [  ] **Functional Design** - [Status: PENDING]
- [  ] **NFR Requirements** - [Status: PENDING]
- [  ] **NFR Design** - [Status: PENDING]
- [  ] **Infrastructure Design** - [Status: PENDING]
- [  ] **Code Generation** - [Status: PENDING]

**Build and Test:**
- [  ] **Build and Test** - [Status: PENDING]

### 🟡 OPERATIONS PHASE

- [  ] **Operations** - [Status: PLACEHOLDER]

---

## Execution Plan

**Reference**: `aidlc-docs/inception/plans/execution-plan.md`

**Phases to Execute**:
- ✅ INCEPTION
- ✅ CONSTRUCTION
- ⏸️ OPERATIONS (Placeholder)

**Conditional Stages**:
- Reverse Engineering: [EXECUTE/SKIP] - [Reason]
- User Stories: [EXECUTE/SKIP] - [Reason]
- Application Design: [EXECUTE/SKIP] - [Reason]
- Units Generation: [EXECUTE/SKIP] - [Reason]
- Functional Design: [EXECUTE/SKIP per unit] - [Reason]
- NFR Requirements: [EXECUTE/SKIP per unit] - [Reason]
- NFR Design: [EXECUTE/SKIP per unit] - [Reason]
- Infrastructure Design: [EXECUTE/SKIP per unit] - [Reason]

---

## Adaptive Detail Levels

**Requirements Analysis**: [Minimal/Standard/Comprehensive]
**User Stories**: [Minimal/Standard/Comprehensive] or SKIPPED
**Application Design**: [Minimal/Standard/Comprehensive] or SKIPPED
**Functional Design**: [Minimal/Standard/Comprehensive] or SKIPPED per unit
**NFR Requirements**: [Minimal/Standard/Comprehensive] or SKIPPED per unit

---

## Notes

[Any additional notes about workflow state, decisions made, or context]

---

**Last Modified By**: AI Assistant
**Modification Reason**: [Why state was updated]
```

## Checkbox Legend

- `[x]` - Stage COMPLETED
- `[⏭️]` - Stage SKIPPED (with reason documented)
- `[  ]` - Stage PENDING (not yet started)

## Status Values

- **COMPLETED** - Stage finished and approved
- **SKIPPED** - Stage intentionally skipped (reason documented)
- **PENDING** - Stage not yet started
- **IN PROGRESS** - Stage currently being executed
- **BLOCKED** - Stage cannot proceed (reason documented)
- **PLACEHOLDER** - Stage not yet implemented (Operations only)

## When to Update

Update aidlc-state.md:

1. **After Workspace Detection** - Initialize state
2. **After Workflow Planning** - Set execution plan
3. **After each stage completes** - Mark [x] and add timestamp
4. **When skipping a stage** - Mark [⏭️] and document reason
5. **When starting a stage** - Update "Current Stage"
6. **When changing phases** - Update "Current Phase"

## Example: Greenfield Project

```markdown
# AIDLC Workflow State

**Last Updated**: 2026-01-28T15:30:00Z
**Project Type**: Greenfield
**Current Phase**: CONSTRUCTION
**Current Stage**: Functional Design - user-service

---

## Workflow Progress

### 🔵 INCEPTION PHASE

- [x] **Workspace Detection** - 2026-01-28T14:00:00Z - COMPLETED
- [⏭️] **Reverse Engineering** - SKIPPED (Greenfield project)
- [x] **Requirements Analysis** - 2026-01-28T14:30:00Z - COMPLETED
- [x] **User Stories** - 2026-01-28T14:45:00Z - COMPLETED
- [x] **Workflow Planning** - 2026-01-28T15:00:00Z - COMPLETED
- [x] **Application Design** - 2026-01-28T15:15:00Z - COMPLETED
- [x] **Units Generation** - 2026-01-28T15:25:00Z - COMPLETED

### 🟢 CONSTRUCTION PHASE

**Per-Unit Progress:**

#### Unit: user-service
- [x] **Functional Design** - 2026-01-28T15:30:00Z - IN PROGRESS
- [  ] **NFR Requirements** - PENDING
- [  ] **NFR Design** - PENDING
- [  ] **Infrastructure Design** - PENDING
- [  ] **Code Generation** - PENDING

#### Unit: payment-service
- [  ] **Functional Design** - PENDING
- [  ] **NFR Requirements** - PENDING
- [  ] **NFR Design** - PENDING
- [  ] **Infrastructure Design** - PENDING
- [  ] **Code Generation** - PENDING

**Build and Test:**
- [  ] **Build and Test** - PENDING

### 🟡 OPERATIONS PHASE

- [  ] **Operations** - PLACEHOLDER

---

## Execution Plan

**Reference**: `aidlc-docs/inception/plans/execution-plan.md`

**Phases to Execute**:
- ✅ INCEPTION
- ✅ CONSTRUCTION
- ⏸️ OPERATIONS (Placeholder)

**Conditional Stages**:
- Reverse Engineering: SKIP - Greenfield project, no existing code
- User Stories: EXECUTE - New user-facing features with multiple personas
- Application Design: EXECUTE - New components and services needed
- Units Generation: EXECUTE - System decomposed into 2 units
- Functional Design: EXECUTE - New data models and business logic per unit
- NFR Requirements: EXECUTE - Performance and security requirements per unit
- NFR Design: EXECUTE - NFR patterns needed per unit
- Infrastructure Design: EXECUTE - Cloud deployment architecture per unit

---

## Adaptive Detail Levels

**Requirements Analysis**: Standard
**User Stories**: Standard
**Application Design**: Standard
**Functional Design**: Standard per unit
**NFR Requirements**: Standard per unit

---

## Notes

- Project: New e-commerce platform
- Units: user-service, payment-service
- Target: AWS deployment with Lambda + API Gateway
- Timeline: 4 weeks for CONSTRUCTION phase

---

**Last Modified By**: AI Assistant
**Modification Reason**: Started Functional Design for user-service unit
```

## Usage in Detail Files

Reference this template:

```markdown
### Step X: Update State Tracking

**Action:** Update `aidlc-docs/aidlc-state.md`

**Template:** See `templates/state/aidlc-state.md`

**Update:**
- Mark current stage as [x] COMPLETED
- Add timestamp
- Update "Current Stage" to next stage
- Update "Current Phase" if changing phases
```

## Session Resumption

When resuming a workflow:

1. **Read aidlc-state.md FIRST**
2. Parse current status
3. Load artifacts from completed stages
4. Show user where they left off
5. Offer to continue or make changes
