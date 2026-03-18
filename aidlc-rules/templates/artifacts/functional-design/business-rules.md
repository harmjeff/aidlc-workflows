# Business Rules Template

Use this template to document business rules, validations, and constraints for a unit.

## Template

```markdown
# Business Rules - [unit-name]

**Unit Name:** [unit-name]
**Created:** [ISO 8601 timestamp]
**Version:** 1.0

---

## Overview

[High-level description of the business rules governing this unit. Explain the purpose and scope of these rules.]

---

## Validation Rules

### Input Validation Rules

[Rules for validating input data before processing]

**Rule 1: [Rule Name]**
- **ID:** VR-IN-001
- **Field/Data:** [What is being validated]
- **Rule:** [Specific validation rule]
- **Error Message:** "[User-facing error message]"
- **Severity:** [Critical/High/Medium/Low]
- **Example:**
  - ✅ Valid: [Example of valid input]
  - ❌ Invalid: [Example of invalid input]

[Continue for all input validation rules]

### Business Validation Rules

[Rules for validating business logic and constraints]

**Rule 1: [Rule Name]**
- **ID:** VR-BUS-001
- **Description:** [What business constraint is being validated]
- **Rule:** [Specific validation rule]
- **Rationale:** [Why this rule exists]
- **Error Message:** "[User-facing error message]"
- **Severity:** [Critical/High/Medium/Low]
- **Example:**
  - ✅ Valid: [Example of valid scenario]
  - ❌ Invalid: [Example of invalid scenario]

[Continue for all business validation rules]

---

## Business Constraints

[Hard constraints that must always be enforced]

**Constraint 1: [Constraint Name]**
- **ID:** BC-001
- **Description:** [What constraint must be maintained]
- **Type:** [Invariant/Precondition/Postcondition]
- **Enforcement:** [When and how it's enforced]
- **Violation Handling:** [What happens if violated]
- **Business Impact:** [Why this constraint matters]

[Continue for all business constraints]

---

## Calculations and Formulas

[Business calculations and their rules]

**Calculation 1: [Calculation Name]**
- **ID:** CALC-001
- **Purpose:** [What is being calculated]
- **Formula:** [Mathematical formula or algorithm]
- **Inputs:** [Required input values and their constraints]
- **Output:** [Calculation result and format]
- **Precision:** [Rounding rules, decimal places]
- **Edge Cases:** [Special cases and how they're handled]
- **Example:**
  ```
  Input: [Sample values]
  Calculation: [Show step-by-step]
  Output: [Result]
  ```

[Continue for all calculations]

---

## Business Invariants

[Conditions that must always be true]

**Invariant 1: [Invariant Name]**
- **ID:** INV-001
- **Description:** [What must always be true]
- **Scope:** [Where this invariant applies]
- **Enforcement:** [How it's maintained]
- **Violation Impact:** [What happens if violated]
- **Recovery:** [How to recover from violation]

[Continue for all invariants]

---

## Conditional Logic Rules

[Rules that apply under specific conditions]

**Conditional Rule 1: [Rule Name]**
- **ID:** CR-001
- **Condition:** [When this rule applies]
- **Rule:** [What rule is applied]
- **Alternative:** [What happens if condition is false]
- **Priority:** [If multiple rules apply, which takes precedence]
- **Example:**
  - Condition Met: [Example scenario]
  - Condition Not Met: [Alternative scenario]

[Continue for all conditional rules]

---

## Data Integrity Rules

[Rules for maintaining data consistency and integrity]

**Integrity Rule 1: [Rule Name]**
- **ID:** DIR-001
- **Description:** [What data integrity is being maintained]
- **Scope:** [What data is affected]
- **Enforcement:** [When and how it's enforced]
- **Validation:** [How integrity is validated]
- **Repair:** [How to fix integrity violations]

[Continue for all data integrity rules]

---

## Authorization Rules

[Rules for determining who can perform what actions]

**Authorization Rule 1: [Rule Name]**
- **ID:** AUTH-001
- **Action:** [What action is being authorized]
- **Roles:** [Which roles can perform this action]
- **Conditions:** [Additional conditions that must be met]
- **Denial Handling:** [What happens when authorization fails]
- **Audit:** [What is logged for this authorization]

[Continue for all authorization rules]

---

## Error Handling Rules

[Rules for handling errors and exceptions]

**Error Handling Rule 1: [Rule Name]**
- **ID:** EH-001
- **Error Type:** [What type of error]
- **Detection:** [How error is detected]
- **Handling:** [How error is handled]
- **Recovery:** [Recovery mechanism if any]
- **User Communication:** [What user sees/receives]
- **Logging:** [What is logged]
- **Escalation:** [When to escalate]

[Continue for all error handling rules]

---

## Business Rule Dependencies

[Dependencies between business rules]

**Dependency 1:**
- **Primary Rule:** [Rule ID and name]
- **Dependent Rule:** [Rule ID and name]
- **Relationship:** [How they're related]
- **Impact:** [What happens if primary rule changes]

[Continue for all dependencies]

---

## Rule Priorities

[When multiple rules apply, which takes precedence]

**Priority Order:**
1. [Highest priority rule type]
2. [Second priority rule type]
3. [Third priority rule type]
[Continue in priority order]

**Conflict Resolution:**
- [How conflicts between rules are resolved]
- [Who decides in ambiguous cases]

---

## Temporal Rules

[Rules that change based on time or state]

**Temporal Rule 1: [Rule Name]**
- **ID:** TR-001
- **Description:** [What rule changes over time]
- **Time Dependency:** [How time affects the rule]
- **Effective Period:** [When rule is active]
- **Transition:** [How rule changes at boundaries]

[Continue for all temporal rules]

---

## Compliance Rules

[Rules required for regulatory or policy compliance]

**Compliance Rule 1: [Rule Name]**
- **ID:** COMP-001
- **Regulation:** [What regulation requires this]
- **Description:** [What must be complied with]
- **Enforcement:** [How compliance is enforced]
- **Validation:** [How compliance is validated]
- **Documentation:** [What documentation is required]
- **Audit Trail:** [What audit trail is maintained]

[Continue for all compliance rules]

---

## Business Rule Exceptions

[Documented exceptions to standard rules]

**Exception 1: [Exception Name]**
- **ID:** EX-001
- **Standard Rule:** [What rule is being excepted]
- **Exception Condition:** [When exception applies]
- **Alternative Rule:** [What rule applies instead]
- **Approval Required:** [Who must approve exception]
- **Documentation:** [What must be documented]
- **Expiration:** [When exception expires if applicable]

[Continue for all exceptions]

---

## Rule Change History

[Track changes to business rules over time]

| Version | Date | Rule ID | Change Description | Reason | Approved By |
|---------|------|---------|-------------------|--------|-------------|
| 1.0 | [Date] | [ID] | [Description] | [Reason] | [Name] |

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
- During Functional Design stage for each unit
- When documenting business rules for new features
- When clarifying validation and constraint requirements

### Customization
- Remove sections not applicable to your unit
- Add sections for unit-specific rule types
- Adjust detail level based on complexity
- Use consistent ID prefixes for rule tracking

### Best Practices
- Be specific and testable - rules should be verifiable
- Include examples for complex rules
- Document the business rationale for each rule
- Keep rules atomic - one rule per entry
- Use consistent terminology
- Link rules to requirements or user stories when possible

### Common Mistakes to Avoid
- ❌ Making rules too vague or ambiguous
- ❌ Forgetting to document error messages
- ❌ Not explaining why rules exist
- ❌ Mixing technical implementation with business rules
- ❌ Not documenting rule priorities and conflicts
- ❌ Forgetting to include examples

### Rule ID Conventions
- **VR-IN-XXX:** Input Validation Rules
- **VR-BUS-XXX:** Business Validation Rules
- **BC-XXX:** Business Constraints
- **CALC-XXX:** Calculations
- **INV-XXX:** Invariants
- **CR-XXX:** Conditional Rules
- **DIR-XXX:** Data Integrity Rules
- **AUTH-XXX:** Authorization Rules
- **EH-XXX:** Error Handling Rules
- **TR-XXX:** Temporal Rules
- **COMP-XXX:** Compliance Rules
- **EX-XXX:** Exceptions

