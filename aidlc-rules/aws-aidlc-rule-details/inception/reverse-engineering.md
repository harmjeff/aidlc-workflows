# Reverse Engineering

**Purpose:** Understand existing codebase structure, architecture, and components before making changes.

**Stage Type:** CONDITIONAL

**Phase:** INCEPTION

**Load this file when:** Starting Reverse Engineering stage for brownfield project

**Unload this file after:** Reverse Engineering completes and user approves

---

## Execute IF

- Existing codebase detected (brownfield project) **AND**
- No previous reverse engineering artifacts found **OR**
- Previous artifacts are incomplete or outdated

## Skip IF

- Greenfield project (no existing code) **OR**
- Previous reverse engineering artifacts already exist and are complete

---

## Steps

### Step 1: Log Start of Reverse Engineering
**Action:** Log start of reverse engineering in audit.md.

**Template:** `../../templates/audit-logs/basic-entry.md`

**Log with:**
- Stage: Reverse Engineering
- Context: Starting reverse engineering of existing codebase

### Step 2: Analyze Codebase
**Action:** Perform comprehensive codebase analysis:

**Analysis Areas:**
1. **Multi-Package Discovery** - Identify all packages, modules, components
2. **Business Context** - Understand business domain, transactions, workflows
3. **Infrastructure Discovery** - Identify IaC files, cloud resources, deployment patterns
4. **Build System Discovery** - Identify build tools, configurations, dependencies
5. **Service Architecture** - Identify service boundaries, communication patterns, APIs
6. **Code Quality** - Assess code organization, patterns, test coverage, technical debt

### Step 3: Generate Reverse Engineering Artifacts
**Action:** Create 9 mandatory artifacts in `aidlc-docs/inception/reverse-engineering/`:

**Artifacts to Create:**
1. **business-overview.md** - Business domain, transactions, terminology
2. **architecture.md** - System architecture, components, patterns
3. **code-structure.md** - Directory structure, packages, modules
4. **api-documentation.md** - APIs, endpoints, contracts
5. **component-inventory.md** - All components with responsibilities
6. **interaction-diagrams.md** - Component interactions, data flow
7. **technology-stack.md** - Languages, frameworks, tools, versions
8. **dependencies.md** - Internal and external dependencies
9. **reverse-engineering-timestamp.md** - Timestamp and metadata

**Each artifact should:**
- Document findings from codebase analysis
- Be comprehensive and detailed
- Include examples from actual code
- Provide context for future changes

### Step 4: Update State Tracking
**Action:** Update `aidlc-docs/aidlc-state.md` to reflect completion.

**Template:** `../../templates/state/aidlc-state.md`

### Step 5: Present Completion Message
**Action:** Present completion message to user.

**Message:**
```markdown
# 🔍 Reverse Engineering Complete

I've analyzed your existing codebase and created comprehensive documentation.

**Artifacts Created:**
- ✅ business-overview.md - Business domain and transactions
- ✅ architecture.md - System architecture
- ✅ code-structure.md - Code organization
- ✅ api-documentation.md - API documentation
- ✅ component-inventory.md - Component catalog
- ✅ interaction-diagrams.md - Component interactions
- ✅ technology-stack.md - Technology stack
- ✅ dependencies.md - Dependencies
- ✅ reverse-engineering-timestamp.md - Analysis metadata

**Location:** `aidlc-docs/inception/reverse-engineering/`

---

**What would you like to do?**

🔧 **Request Changes** - Ask for modifications to the analysis

✅ **Continue to Next Stage** - Approve and proceed to Requirements Analysis

---

Please choose one of the options above.
```

### Step 6: Wait for User Response
**Action:** **WAIT FOR EXPLICIT APPROVAL** - Do NOT proceed until user confirms.

**Handle response:**
- If "Request Changes" → Make modifications and return to Step 5
- If "Continue" → Proceed to Step 7

### Step 7: Log User Approval
**Action:** Record approval in audit.md with complete raw input.

**Template:** `../../templates/audit-logs/basic-entry.md`

---

## Artifacts Created

1. **business-overview.md** - Business domain understanding
2. **architecture.md** - System architecture documentation
3. **code-structure.md** - Code organization documentation
4. **api-documentation.md** - API documentation
5. **component-inventory.md** - Component catalog
6. **interaction-diagrams.md** - Component interaction documentation
7. **technology-stack.md** - Technology stack documentation
8. **dependencies.md** - Dependency documentation
9. **reverse-engineering-timestamp.md** - Analysis metadata

All artifacts in: `aidlc-docs/inception/reverse-engineering/`

---

## Key Principles

1. **Comprehensive Analysis:** Analyze all aspects of the codebase
2. **Business Context:** Understand business domain and transactions
3. **Technical Detail:** Document architecture, components, APIs
4. **Reusable Artifacts:** Create artifacts that inform future stages
5. **Complete Audit Trail:** Log all user inputs
6. **Explicit Approval:** WAIT for user approval before proceeding

---

## Templates Reference

All templates are located in `../../templates/` directory:

- **Audit Logs:** `audit-logs/basic-entry.md`
- **State:** `state/aidlc-state.md`

---

## Next Stage

After approval:
- **Requirements Analysis** stage

---

**End of Reverse Engineering Stage Instructions**
