# Frontend Development Rules

## Overview
This extension adds frontend-specific design and code generation support for full-stack applications that include user interface components. It enhances Functional Design and Code Generation stages with UI-specific guidance.

## Stage Addendums

### Functional Design Addendum

**Add Frontend Components Question Category**:

When generating design questions, include this additional category:

**Frontend Components** (if unit includes UI):
- Ask about UI component structure
- Ask about user interactions
- Ask about state management
- Ask about form handling

**Generate Frontend Components Artifact**:

If unit includes frontend/UI, create `aidlc-docs/construction/{unit-name}/functional-design/frontend-components.md` with:

```markdown
# Frontend Components Design - [unit-name]

## Component Hierarchy
[Document parent-child relationships and component composition]

## Component Specifications

### [Component Name]
- **Purpose**: [What this component does]
- **Props**: [List of props with types and descriptions]
- **State**: [Local state variables and their purpose]
- **Lifecycle/Hooks**: [Key lifecycle methods or React hooks used]
- **User Interactions**: [Click handlers, form submissions, navigation]
- **Validation Rules**: [Client-side validation logic]
- **API Integration**: [Which backend endpoints this component calls]

[Repeat for each component]

## State Management
- **Local State**: [Components managing their own state]
- **Global State**: [Shared state across components]
- **Context/Store**: [Redux, Context API, Vuex, etc.]

## Form Handling
- **Forms**: [List of forms in this unit]
- **Validation**: [Client-side validation rules]
- **Submission**: [How form data is submitted to backend]
- **Error Handling**: [How validation errors are displayed]

## API Integration Map
| Component | Backend Endpoint | Method | Purpose |
|-----------|------------------|--------|---------|
| [Component] | `/api/endpoint` | GET/POST | [Purpose] |
```

### Code Generation Addendum

**Add Frontend-Specific Generation Steps**:

When creating the code generation plan for a unit that includes frontend components, add these steps to the plan:

**Frontend Components Generation**:
- [ ] Generate UI component files (React, Vue, Angular, etc.)
- [ ] Implement component hierarchy as designed
- [ ] Implement props and state management
- [ ] Implement user interaction handlers
- [ ] Implement form validation logic
- [ ] Integrate with backend API endpoints
- [ ] Apply styling (CSS, styled-components, etc.)

**Frontend Components Unit Testing**:
- [ ] Create component unit tests
- [ ] Test component rendering
- [ ] Test user interactions (clicks, form submissions)
- [ ] Test form validation
- [ ] Test API integration (mocked)
- [ ] Test edge cases and error states

**Frontend Components Summary**:
- [ ] Document generated frontend components
- [ ] List component files created
- [ ] Document testing coverage
- [ ] Note any manual setup required (routing, state management configuration)

**Generated Frontend Artifacts Location**:
- Component files: `[workspace-root]/src/components/` (or framework-appropriate location)
- Component tests: `[workspace-root]/src/components/__tests__/` (or framework-appropriate location)
- Documentation: `aidlc-docs/construction/{unit-name}/code/frontend-summary.md`

## Rules

### RULE-FE-01: Frontend Component Design Required
**Rule**: When a unit includes frontend/UI functionality, Functional Design stage must create the `frontend-components.md` artifact documenting component architecture.

**Verification**:
- Units with UI have `frontend-components.md` in their functional-design directory
- Backend-only units do not have this artifact
- Artifact includes component hierarchy, specifications, state management, and API integration

### RULE-FE-02: Frontend Generation Steps Included
**Rule**: Code generation plans for units with frontend components must include frontend-specific generation and testing steps.

**Verification**:
- Code generation plan includes "Frontend Components Generation" section
- Code generation plan includes "Frontend Components Unit Testing" section
- Code generation plan includes "Frontend Components Summary" section
- Steps are executed in correct sequence (after backend logic, before build/test)

### RULE-FE-03: API Integration Documentation
**Rule**: Frontend components that interact with backend APIs must document which endpoints they call and for what purpose.

**Verification**:
- `frontend-components.md` includes API Integration Map
- Each component's API calls are documented
- Backend endpoint paths are specified
- HTTP methods and purposes are clear

### RULE-FE-04: Frontend Testing Coverage
**Rule**: Generated frontend components must include unit tests for rendering, interactions, validation, and API integration.

**Verification**:
- Component test files are created
- Tests cover component rendering
- Tests cover user interactions
- Tests cover form validation (if applicable)
- Tests cover API integration with mocks

## Quality Assurance Indicators

### Red Flags (Violations)
- UI functionality present but no `frontend-components.md` artifact
- Code generation plan missing frontend-specific steps
- Frontend components generated without tests
- API integration not documented

### Success Indicators (Compliance)
- All UI units have comprehensive frontend component design
- Code generation plans include complete frontend steps
- Frontend components are tested
- Clear mapping between frontend components and backend APIs
- State management strategy is documented
