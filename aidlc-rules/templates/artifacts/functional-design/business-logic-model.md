# Business Logic Model Template

Use this template to document the business logic flow and processing model for a unit.

## Template

```markdown
# Business Logic Model - [unit-name]

**Unit Name:** [unit-name]
**Created:** [ISO 8601 timestamp]
**Version:** 1.0

---

## Overview

[High-level description of the business logic for this unit. Explain what this unit does from a business perspective.]

---

## Business Logic Flow

### Main Processing Flow

[Describe the main business logic flow with numbered steps]

1. **Step 1: [Step Name]**
   - **Input:** [What data/events come in]
   - **Processing:** [What business logic is applied]
   - **Output:** [What data/events go out]
   - **Validation:** [Any validation performed]

2. **Step 2: [Step Name]**
   - **Input:** [What data/events come in]
   - **Processing:** [What business logic is applied]
   - **Output:** [What data/events go out]
   - **Validation:** [Any validation performed]

[Continue for all main processing steps]

### Decision Points

[Describe key decision points and branching logic in the flow]

**Decision Point 1: [Name]**
- **Condition:** [What is evaluated - be specific]
- **True Path:** [What happens if condition is true]
- **False Path:** [What happens if condition is false]
- **Business Impact:** [Why this decision matters]

**Decision Point 2: [Name]**
- **Condition:** [What is evaluated]
- **True Path:** [What happens if true]
- **False Path:** [What happens if false]
- **Business Impact:** [Why this decision matters]

[Continue for all decision points]

### Business Workflows

[Describe complete end-to-end business workflows]

**Workflow 1: [Workflow Name]**
- **Trigger:** [What initiates this workflow - user action, event, schedule, etc.]
- **Preconditions:** [What must be true before workflow starts]
- **Steps:**
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]
  [Continue for all steps]
- **Success Outcome:** [What happens when workflow completes successfully]
- **Failure Outcome:** [What happens when workflow fails]
- **Postconditions:** [What is true after workflow completes]

[Continue for all workflows]

---

## Processing Scenarios

### Success Scenarios

[Describe scenarios where processing completes successfully]

**Scenario 1: [Name]**
- **Description:** [What happens in this scenario]
- **Input:** [Sample input data]
- **Processing:** [How it's processed]
- **Output:** [Expected output]
- **Business Value:** [Why this scenario matters]

[Continue for all success scenarios]

### Failure Scenarios

[Describe scenarios where processing fails and how they're handled]

**Scenario 1: [Name]**
- **Description:** [What causes failure]
- **Detection:** [How failure is detected]
- **Handling:** [How failure is handled]
- **Recovery:** [Recovery mechanism if any]
- **User Impact:** [How this affects the user]

[Continue for all failure scenarios]

### Edge Cases

[Describe edge cases and special handling]

**Edge Case 1: [Name]**
- **Description:** [What makes this an edge case]
- **Frequency:** [How often this occurs]
- **Handling:** [How it's handled differently]
- **Rationale:** [Why special handling is needed]

[Continue for all edge cases]

---

## Data Transformations

[Describe how data is transformed through the business logic]

**Transformation 1: [Name]**
- **Purpose:** [Why this transformation is needed]
- **Input Format:** [Description of input data structure]
- **Transformation Logic:** [Step-by-step transformation process]
- **Output Format:** [Description of output data structure]
- **Example:**
  ```
  Input: [Sample input]
  Output: [Sample output]
  ```

[Continue for all transformations]

---

## Integration Points

[Describe integration with external systems or other units]

**Integration 1: [System/Unit Name]**
- **Type:** [Synchronous/Asynchronous, REST/GraphQL/Event/etc.]
- **Purpose:** [Why integration is needed]
- **Direction:** [Inbound/Outbound/Bidirectional]
- **Data Exchange:** [What data is sent/received]
- **Error Handling:** [How integration errors are handled]
- **Retry Logic:** [Retry strategy if applicable]
- **Timeout:** [Timeout settings if applicable]

[Continue for all integrations]

---

## State Management

[Describe state management if applicable]

**State Model:**
- **States:** [List all possible states]
- **Initial State:** [What state entities start in]
- **Final States:** [What states are terminal]

**State Transitions:**
- **[State 1] → [State 2]**
  - **Trigger:** [What causes this transition]
  - **Validation:** [What must be true for transition]
  - **Side Effects:** [What else happens during transition]

[Continue for all state transitions]

**State Diagram:**
```
[State 1] --[Trigger]--> [State 2]
[State 2] --[Trigger]--> [State 3]
[State 3] --[Trigger]--> [State 1]
```

---

## Business Calculations

[Describe any business calculations or algorithms]

**Calculation 1: [Name]**
- **Purpose:** [What is being calculated]
- **Formula:** [Mathematical formula or algorithm description]
- **Inputs:** [Required input values]
- **Output:** [Calculation result]
- **Precision:** [Rounding rules, decimal places, etc.]
- **Example:**
  ```
  Input: [Sample values]
  Calculation: [Show calculation]
  Output: [Result]
  ```

[Continue for all calculations]

---

## Performance Considerations

[Describe performance-critical aspects of the business logic]

**Consideration 1: [Name]**
- **Description:** [What performance aspect]
- **Impact:** [Why it matters]
- **Optimization:** [How it's optimized]
- **Metrics:** [Target performance metrics]

[Continue for all performance considerations]

---

## Security Considerations

[Describe security aspects of the business logic]

**Consideration 1: [Name]**
- **Description:** [What security aspect]
- **Risk:** [What risk it mitigates]
- **Implementation:** [How it's implemented]
- **Validation:** [How it's validated]

[Continue for all security considerations]

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
- When documenting business logic for new features
- When clarifying complex business processes

### Customization
- Remove sections not applicable to your unit
- Add sections for unit-specific concerns
- Adjust detail level based on complexity

### Best Practices
- Be specific and concrete, avoid vague descriptions
- Include examples for complex logic
- Document the "why" not just the "what"
- Keep business logic separate from technical implementation
- Focus on business rules and workflows, not code structure

### Common Mistakes to Avoid
- ❌ Including technical implementation details (belongs in code)
- ❌ Mixing business logic with infrastructure concerns
- ❌ Being too abstract or high-level
- ❌ Forgetting to document edge cases and failure scenarios
- ❌ Not explaining the business rationale for decisions
