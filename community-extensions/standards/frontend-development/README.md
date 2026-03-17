# Frontend Development Extension

Adds frontend-specific design and generation rules for full-stack applications that include UI components.

---

## What It Does

This extension enhances the workflow with frontend/UI-specific guidance:
- **Functional Design**: Adds frontend component design (hierarchy, props, state, interactions)
- **Code Generation**: Includes frontend component generation and testing steps
- **UI-Specific Questions**: Asks about component structure, state management, form handling, API integration

**Without this extension:** AI-DLC focuses on backend/business logic only.

**With this extension:** AI-DLC provides comprehensive full-stack support including frontend components.

---

## When to Use

Install this extension if:
- Your project includes a web UI or mobile app
- You're building full-stack applications
- You need frontend component design guidance
- Your team wants AI assistance with UI architecture
- You're working with React, Vue, Angular, or similar frameworks

Skip this extension if:
- Your project is backend-only (APIs, services, data processing)
- You're building CLI tools or libraries
- Your team handles frontend separately
- You don't need UI design guidance from AI-DLC

---

## Installation

Copy the rule files into your project's extensions directory:

### Kiro
```bash
mkdir -p .kiro/aws-aidlc-rule-details/extensions/standards/frontend-development
cp community-extensions/standards/frontend-development/frontend-development.md .kiro/aws-aidlc-rule-details/extensions/standards/frontend-development/
cp community-extensions/standards/frontend-development/frontend-development.opt-in.md .kiro/aws-aidlc-rule-details/extensions/standards/frontend-development/
```

### Amazon Q Developer
```bash
mkdir -p .amazonq/aws-aidlc-rule-details/extensions/standards/frontend-development
cp community-extensions/standards/frontend-development/frontend-development.md .amazonq/aws-aidlc-rule-details/extensions/standards/frontend-development/
cp community-extensions/standards/frontend-development/frontend-development.opt-in.md .amazonq/aws-aidlc-rule-details/extensions/standards/frontend-development/
```

### Cursor / Cline / Claude Code / GitHub Copilot
```bash
mkdir -p .aidlc-rule-details/extensions/standards/frontend-development
cp community-extensions/standards/frontend-development/frontend-development.md .aidlc-rule-details/extensions/standards/frontend-development/
cp community-extensions/standards/frontend-development/frontend-development.opt-in.md .aidlc-rule-details/extensions/standards/frontend-development/
```

Then start a new AI-DLC session. During Requirements Analysis, you'll be asked whether your project includes frontend development.

---

## What Changes

### Functional Design Stage (per-unit)
- Adds frontend component design as a question category
- Creates `frontend-components.md` artifact when unit includes UI
- Documents:
  - Component hierarchy and structure
  - Props and state definitions for each component
  - User interaction flows
  - Form validation rules
  - API integration points (which backend endpoints each component uses)

### Code Generation Stage (per-unit)
- Adds frontend-specific generation steps:
  - Frontend Components Generation
  - Frontend Components Unit Testing
  - Frontend Components Summary
- Generates actual UI component code (React, Vue, Angular, etc.)
- Creates component tests
- Documents frontend implementation

---

## Frontend Design Artifacts

When enabled, Functional Design creates:

```markdown
aidlc-docs/construction/{unit-name}/functional-design/frontend-components.md

Contents:
- Component Hierarchy: Parent-child relationships, composition
- Component Specifications: Props, state, lifecycle, hooks
- User Interactions: Click handlers, form submissions, navigation
- Form Validations: Client-side validation rules
- API Integration: Which backend endpoints each component calls
- State Management: Local state, global state, context usage
```

---

## Code Generation Steps

Additional steps added to code generation plan:
- **Frontend Components Generation**: Create React/Vue/Angular components
- **Frontend Components Unit Testing**: Create component tests (Jest, React Testing Library, etc.)
- **Frontend Components Summary**: Document frontend implementation

---

## Trade-offs

**Advantages:**
- Comprehensive full-stack support
- Structured frontend design guidance
- UI component architecture documented
- Frontend testing included
- Clear API integration mapping

**Disadvantages:**
- Additional design overhead for backend-only projects (if mistakenly enabled)
- More artifacts to review
- Assumes familiarity with frontend frameworks
- Not applicable to CLI/library/service-only projects
