# Process Overview

**Purpose:** High-level understanding of the AIDLC workflow structure

---

## Three-Phase Lifecycle

### 🔵 INCEPTION PHASE
**Purpose:** Planning, requirements gathering, and architectural decisions  
**Focus:** Determine WHAT to build and WHY  
**Outcome:** Clear understanding of requirements, architecture, and work breakdown

**Stages:**
- Workspace Detection (ALWAYS)
- Reverse Engineering (Brownfield only)
- Requirements Analysis (ALWAYS - adaptive depth)
- User Stories (Intelligent assessment)
- Workflow Planning (ALWAYS)
- Application Design (New components)
- Units Generation (Multiple units)

### 🟢 CONSTRUCTION PHASE
**Purpose:** Detailed design, NFR implementation, and code generation  
**Focus:** Determine HOW to build it  
**Outcome:** Working code with tests and deployment artifacts

**Per-Unit Loop:**
- Functional Design (New data models/logic)
- NFR Requirements (Performance/security needs)
- NFR Design (NFR patterns)
- Infrastructure Design (Infrastructure mapping)
- Code Generation (ALWAYS - two-part)

**After All Units:**
- Build and Test (ALWAYS)

### 🟡 OPERATIONS PHASE
**Purpose:** Deployment and monitoring (future)  
**Focus:** How to DEPLOY and RUN it  
**Status:** Currently placeholder

---

## Workflow Visualization

```
INCEPTION → CONSTRUCTION → OPERATIONS
    ↓            ↓             ↓
Planning     Design        Deploy
    ↓            ↓             ↓
Architect    Code          Monitor
    ↓            ↓             ↓
Breakdown    Test          Maintain
```

---

## Adaptive Execution

The workflow intelligently adapts based on:

1. **User Intent Clarity**
   - Clear request → Minimal stages
   - Vague request → More clarification stages

2. **Codebase State**
   - Greenfield → Skip reverse engineering
   - Brownfield → Include reverse engineering

3. **Complexity**
   - Simple change → Skip optional stages
   - Complex change → Include all relevant stages

4. **Risk Assessment**
   - Low risk → Lighter process
   - High risk → Comprehensive process

---

## Stage Types

### Always-Execute Stages
These stages ALWAYS run:
- Workspace Detection
- Requirements Analysis (adaptive depth)
- Workflow Planning
- Code Generation (per-unit)
- Build and Test

### Conditional Stages
These stages execute only when criteria met:
- Reverse Engineering
- User Stories
- Application Design
- Units Generation
- Functional Design (per-unit)
- NFR Requirements (per-unit)
- NFR Design (per-unit)
- Infrastructure Design (per-unit)

---

## Key Workflow Characteristics

**User-Controlled:** User approves all major decisions and can override recommendations

**Transparent:** Execution plan shown before starting, progress tracked continuously

**Traceable:** Complete audit trail of all decisions and interactions

**Resumable:** Can pause and resume at any stage

**Adaptive:** Adjusts detail level based on complexity

**Quality-Focused:** Proactive questioning prevents assumptions

---

**Unload this file:** After reading, you may release from active context until needed again.
