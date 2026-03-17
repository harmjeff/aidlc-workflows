# Comprehensive Assessment Rules

## Overview
This extension provides detailed, structured assessment frameworks for Requirements Analysis, User Stories, and Workflow Planning stages. It replaces simpler heuristics with comprehensive evaluation criteria to ensure informed decision-making.

## Stage Addendums

### Requirements Analysis Addendum

**Apply Thorough Completeness Analysis**:

**MANDATORY**: Use comprehensive analysis to evaluate requirements completeness. Default to asking questions when there is ANY ambiguity or missing detail.

**MANDATORY**: Evaluate ALL of these areas and ask questions for ANY that are unclear:
- **Functional Requirements**: Core features, user interactions, system behaviors
- **Non-Functional Requirements**: Performance, security, scalability, usability
- **User Scenarios**: Use cases, user journeys, edge cases, error scenarios
- **Business Context**: Goals, constraints, success criteria, stakeholder needs
- **Technical Context**: Integration points, data requirements, system boundaries
- **Quality Attributes**: Reliability, maintainability, testability, accessibility

**When in doubt, ask questions** - incomplete requirements lead to poor implementations.

### User Stories Addendum

**Apply Intelligent Assessment Guidelines**:

**WHEN TO EXECUTE USER STORIES**: Use this enhanced assessment before proceeding:

#### High Priority Execution (ALWAYS Execute)
- **New User Features**: Any new functionality users will directly interact with
- **User Experience Changes**: Modifications to existing user workflows or interfaces
- **Multi-Persona Systems**: Applications serving different types of users
- **Customer-Facing APIs**: Services that external users or systems will consume
- **Complex Business Logic**: Requirements with multiple scenarios or business rules
- **Cross-Team Projects**: Work requiring shared understanding across multiple teams

#### Medium Priority Execution (Assess Complexity)
- **Backend User Impact**: Internal changes that indirectly affect user experience
- **Performance Improvements**: Enhancements with user-visible benefits
- **Integration Work**: Connecting systems that affect user workflows
- **Data Changes**: Modifications affecting user data, reports, or analytics
- **Security Enhancements**: Changes affecting user authentication or permissions

#### Complexity Assessment Factors
For medium priority cases, execute user stories if ANY of these apply:
- **Scope**: Changes span multiple components or user touchpoints
- **Ambiguity**: Requirements have unclear aspects that stories could clarify
- **Risk**: High business impact or potential for misunderstanding
- **Stakeholders**: Multiple business stakeholders involved in requirements
- **Testing**: User acceptance testing will be required
- **Options**: Multiple valid implementation approaches exist

#### Skip Only For Simple Cases
- **Pure Refactoring**: Internal code improvements with zero user impact
- **Isolated Bug Fixes**: Simple, well-defined fixes with clear scope
- **Infrastructure Only**: Changes with no user-facing effects
- **Developer Tooling**: Build processes, CI/CD, or development environment changes
- **Documentation**: Updates that don't affect functionality

#### Default Decision Rule
**When in doubt, include user stories AND ask clarifying questions.** The overhead of creating comprehensive stories with proper clarification is typically outweighed by the benefits of:
- Clearer requirements understanding
- Better team alignment
- Improved testing criteria
- Enhanced stakeholder communication
- Reduced implementation risks
- Fewer costly changes during development
- Better user experience outcomes

#### Mandatory Assessment Documentation
Before executing User Stories stage, create `aidlc-docs/inception/plans/user-stories-assessment.md` with:

```markdown
# User Stories Assessment

## Request Analysis
- **Original Request**: [Brief summary]
- **User Impact**: [Direct/Indirect/None]
- **Complexity Level**: [Simple/Medium/Complex]
- **Stakeholders**: [List involved parties]

## Assessment Criteria Met
- [ ] High Priority: [List applicable criteria]
- [ ] Medium Priority: [List applicable criteria with complexity justification]
- [ ] Benefits: [Expected value from user stories]

## Decision
**Execute User Stories**: [Yes/No]
**Reasoning**: [Detailed justification]

## Expected Outcomes
- [List specific benefits user stories will provide]
- [How stories will improve project success]
```

### Workflow Planning Addendum

**Apply Detailed Scope and Impact Analysis**:

Once all context is loaded (requirements + stories), perform detailed analysis:

#### Change Impact Assessment

**Impact Areas**:
1. **User-facing changes**: Does this affect user experience?
2. **Structural changes**: Does this change system architecture?
3. **Data model changes**: Does this affect database schemas or data structures?
4. **API changes**: Does this affect interfaces or contracts?
5. **NFR impact**: Does this affect performance, security, or scalability?

**Application Layer Impact** (if applicable):
- **Code changes**: New entry points, adapters, configurations
- **Dependencies**: New libraries, framework changes
- **Configuration**: Environment variables, config files
- **Testing**: Unit tests, integration tests

**Infrastructure Layer Impact** (if applicable):
- **Deployment model**: Lambda→ECS, EC2→Fargate, etc.
- **Networking**: VPC, security groups, load balancers
- **Storage**: Persistent volumes, shared storage
- **Scaling**: Auto-scaling policies, capacity planning

**Operations Layer Impact** (if applicable):
- **Monitoring**: CloudWatch, custom metrics, dashboards
- **Logging**: Log aggregation, structured logging
- **Alerting**: Alarm configurations, notification channels
- **Deployment**: CI/CD pipeline changes, rollback strategies

#### Risk Assessment

Evaluate risk level:
1. **Low**: Isolated change, easy rollback, well-understood
2. **Medium**: Multiple components, moderate rollback, some unknowns
3. **High**: System-wide impact, complex rollback, significant unknowns
4. **Critical**: Production-critical, difficult rollback, high uncertainty

## Rules

### RULE-CA-01: Mandatory Requirements Completeness Analysis
**Rule**: Requirements Analysis must evaluate ALL six completeness areas (functional, NFR, user scenarios, business context, technical context, quality attributes) before proceeding.

**Verification**:
- All six areas are explicitly evaluated
- Questions are generated for ANY unclear areas
- No assumptions are made about missing information

### RULE-CA-02: Structured User Stories Assessment
**Rule**: Before executing User Stories stage, perform intelligent assessment using the priority matrix and complexity factors, and document the decision with justification.

**Verification**:
- Assessment follows High/Medium/Skip priority evaluation
- Complexity factors are applied for medium-priority cases
- Assessment documentation file is created with decision rationale
- User Stories execute only if justified by assessment

### RULE-CA-03: Multi-Layer Impact Assessment
**Rule**: Workflow Planning must assess change impact across all applicable layers (Impact Areas, Application, Infrastructure, Operations) before creating execution plan.

**Verification**:
- All applicable layers are evaluated
- Impact assessment is documented in workflow planning artifacts
- Risk level is determined using 4-level matrix

### RULE-CA-04: Risk-Based Planning
**Rule**: Execution plan must reflect the assessed risk level, with higher-risk changes receiving more comprehensive workflow coverage.

**Verification**:
- Risk level is explicitly documented
- Higher-risk projects execute more workflow stages
- Risk assessment informs stage depth determination

## Quality Assurance Indicators

### Red Flags (Violations)
- Requirements proceeding without evaluating all six completeness areas
- User Stories executing without documented assessment justification
- Workflow planning proceeding without impact/risk assessment
- Simple heuristics used instead of structured frameworks

### Success Indicators (Compliance)
- All assessment areas explicitly evaluated and documented
- Clear justification for all major workflow decisions
- Risk and impact comprehensively analyzed
- Stakeholders can review structured assessment rationale
