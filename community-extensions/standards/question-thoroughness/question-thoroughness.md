# Question Thoroughness Rules

## Overview
This extension prevents overconfidence by encouraging comprehensive question generation and thorough answer analysis. It modifies question generation behavior across Requirements Analysis, User Stories, Functional Design, and NFR Requirements stages to default to asking clarifying questions rather than making assumptions.

## Stage Addendums

### Requirements Analysis Addendum
When generating clarifying questions:
- **Default to asking**: When there's any ambiguity, create a question
- **Comprehensive evaluation**: Assess ALL relevant areas using the expanded question categories below
- **Thorough analysis**: Carefully analyze ALL user responses for ambiguities
- **Mandatory follow-up**: Create follow-up questions for ANY unclear responses
- **No proceeding with ambiguity**: Don't move forward until ALL ambiguities are resolved

**Expanded Question Categories** (evaluate ALL areas):
- **Functional Requirements**: Core features, user interactions, system behaviors
- **Non-Functional Requirements**: Performance, security, scalability, usability
- **User Scenarios**: Use cases, user journeys, edge cases, error scenarios
- **Business Context**: Goals, constraints, success criteria, stakeholder needs
- **Technical Context**: Integration points, data requirements, system boundaries
- **Quality Attributes**: Reliability, maintainability, testability, accessibility

Look for vague responses: "depends", "maybe", "not sure", "mix of", "somewhere between". Detect undefined terms and references to external concepts. Identify contradictory or incomplete answers.

### User Stories Addendum
When creating story planning questions:
- Evaluate ALL question categories (don't skip entire categories)
- **When in doubt, ask the question** - overconfidence leads to poor stories
- Strengthen answer analysis requirements
- Create follow-up questions for ANY ambiguous responses
- Don't proceed until ALL unclear responses are clarified

**Question Categories to Evaluate** (consider ALL categories):
- **User Personas**: User types, roles, characteristics, and motivations
- **Story Granularity**: Appropriate level of detail, story size, and breakdown approach
- **Story Format**: Format preferences, template usage, and documentation standards
- **Breakdown Approach**: Organization method, prioritization, and grouping strategies
- **Acceptance Criteria**: Detail level, format, testing approach, and validation methods
- **User Journeys**: User workflows, interaction patterns, and experience flows
- **Business Context**: Business goals, success metrics, and stakeholder needs
- **Technical Constraints**: Technical limitations, integration requirements, and system boundaries

**Mandatory Answer Analysis** - Before proceeding, carefully review all user answers for:
- **Vague or ambiguous responses**: "mix of", "somewhere between", "not sure", "depends", "maybe", "probably"
- **Undefined criteria or terms**: References to concepts without clear definitions
- **Contradictory answers**: Responses that conflict with each other
- **Missing generation details**: Answers that lack specific guidance for implementation
- **Answers that combine options**: Responses that merge different approaches without clear decision rules
- **Incomplete explanations**: Answers that reference external factors without defining them
- **Assumption-based responses**: Answers that assume knowledge not explicitly stated

**Required Follow-up Examples**:
- "You mentioned 'mix of A and B' - what specific criteria should determine when to use A vs B?"
- "You said 'somewhere between A and B' - can you define the exact middle ground approach?"
- "You indicated 'not sure' - what additional information would help you decide?"
- "You mentioned 'depends on complexity' - how do you define complexity levels and thresholds?"
- "You chose 'hybrid approach' - what are the specific rules for when to use each method?"
- "You said 'probably X' - what factors would make it definitely X vs definitely not X?"
- "You referenced 'standard practice' - can you define what that standard practice is?"

### Functional Design Addendum
When generating design questions:
- Evaluate ALL design aspects comprehensively (don't use "only if" conditions)
- **When in doubt, ask the question** - overconfidence leads to poor designs
- Strengthen ambiguity detection and resolution requirements
- Ask questions wherever clarification would improve quality
- Default to inclusion rather than exclusion of questions

**Question Categories to Consider** (evaluate ALL categories):
- **Business Logic Modeling**: Core entities, workflows, data transformations, and business processes
- **Domain Model**: Domain concepts, entity relationships, data structures, and business objects
- **Business Rules**: Decision rules, validation logic, constraints, and business policies
- **Data Flow**: Data inputs, outputs, transformations, and persistence requirements
- **Integration Points**: External system interactions, APIs, and data exchange
- **Error Handling**: Error scenarios, validation failures, and exception handling
- **Business Scenarios**: Edge cases, alternative flows, and complex business situations

**Mandatory Answer Analysis** - Before proceeding, carefully review ALL responses for:
- **Vague or ambiguous responses**: "depends", "maybe", "not sure", "mix of", "somewhere between"
- **Undefined criteria or terms**: References to concepts without clear definitions
- **Contradictory answers**: Responses that conflict with each other
- **Missing design details**: Answers that lack specific guidance
- **Answers that combine options**: Responses that merge different approaches without clear decision rules

**Required Follow-ups**:
- Create clarification questions file if ANY ambiguities are detected
- Add specific follow-up questions for each unclear response
- Do not proceed until ALL ambiguities are resolved
- Examples:
  - "You mentioned 'mix of A and B' - what specific criteria should determine when to use A vs B?"
  - "You said 'somewhere between A and B' - can you define the exact middle ground approach?"
  - "You indicated 'not sure' - what additional information would help you decide?"
  - "You mentioned 'depends on complexity' - how do you define complexity levels?"

### Application Design Addendum
When generating application design questions:
- Analyze requirements and stories to generate ONLY questions relevant to this specific application design
- Focus on ambiguities and missing information specific to this context
- Generate questions only where user input is needed for design decisions
- **When in doubt, ask the question**

**Question Categories** (adapt as needed based on context):
- **Component Identification**: Component boundaries or organization (only if unclear)
- **Component Methods**: Method signatures needing clarification (detailed business rules come later)
- **Service Layer Design**: Service orchestration or boundaries (only if ambiguous)
- **Component Dependencies**: Communication patterns or dependency management (only if unclear)
- **Design Patterns**: Architectural style or pattern choice (only if needs user input)

**Mandatory Answer Analysis** - Before proceeding, carefully review all user answers for:
- **Vague or ambiguous responses**: "mix of", "somewhere between", "not sure", "depends"
- **Undefined criteria or terms**: References to concepts without clear definitions
- **Contradictory answers**: Responses that conflict with each other
- **Missing design details**: Answers that lack specific guidance
- **Answers that combine options**: Responses that merge different approaches without clear decision rules

**Required Follow-ups**:
- Add specific follow-up questions to the plan document using [Answer]: tags if ANY ambiguities detected
- Do not proceed to approval until all ambiguities are resolved

### NFR Requirements Addendum
When assessing NFR requirements:
- Expand beyond basic NFRs to include reliability, maintainability, and usability considerations
- Evaluate ALL NFR categories, don't skip any
- Enhance answer analysis for technical ambiguities
- Create follow-up questions for ANY unclear technical responses
- Be thorough — better to over-clarify than under-clarify

## Rules

### RULE-QT-01: Question Generation Philosophy
**Rule**: When in doubt about user intent, requirements, or design decisions, always create a clarifying question. Overconfidence leads to poor outcomes.

**Verification**:
- Questions are generated for ANY ambiguity in requirements, design, or technical decisions
- All relevant question categories are evaluated (none skipped without clear justification)
- Questions are asked proactively, not reactively

### RULE-QT-02: Comprehensive Category Evaluation
**Rule**: ALL relevant question categories must be evaluated for each stage. Don't skip entire categories unless genuinely not applicable to the specific context.

**Verification**:
- Requirements Analysis evaluates: functional requirements, non-functional requirements, user scenarios, business context, technical context, quality attributes
- User Stories evaluates: user personas, story granularity, story format, breakdown approach, acceptance criteria, user journeys, business context, technical constraints
- Application Design evaluates: component identification, component methods, service layer design, component dependencies, design patterns (context-appropriate)
- Functional Design evaluates: business logic modeling, domain model, business rules, data flow, integration points, error handling, business scenarios
- NFR Requirements evaluates: performance, security, scalability, reliability, maintainability, usability

### RULE-QT-03: Answer Analysis Thoroughness
**Rule**: ALL user responses must be carefully analyzed for vague language, undefined terms, contradictions, or incompleteness before proceeding.

**Verification**:
- Each answer is checked for vague indicators: "depends", "maybe", "not sure", "mix of", "somewhere between"
- Undefined terms and external references are identified
- Contradictory or incomplete answers trigger follow-up questions
- No stage proceeds with unresolved ambiguities

### RULE-QT-04: Mandatory Clarification
**Rule**: When ambiguities are detected in user responses, create a separate clarification questions file and wait for user responses before proceeding.

**Verification**:
- Clarification file is created when ANY ambiguity is detected
- File includes specific questions to resolve each ambiguity
- Workflow does not proceed until clarifications are provided
- After clarifications, responses are re-validated for consistency

### RULE-QT-05: No Assumptions
**Rule**: Never make assumptions about user intent, requirements, or design decisions. Always ask for clarification instead.

**Verification**:
- No design or implementation decisions are made based on assumptions
- When information is missing, questions are asked rather than gaps being filled with assumptions
- All critical decisions have explicit user confirmation

## Quality Assurance Indicators

### Red Flags (Violations)
- Stages completing without asking any questions on complex projects
- Proceeding with vague or ambiguous user responses
- Skipping entire question categories without justification
- Making assumptions instead of asking for clarification

### Success Indicators (Compliance)
- Appropriate number of clarifying questions for project complexity
- Thorough analysis of user responses with follow-up when needed
- Clear, unambiguous requirements before proceeding to implementation
- Reduced need for changes during later stages due to better upfront clarification

## Key Takeaway

**It's better to ask too many questions than to make incorrect assumptions.** The cost of asking clarifying questions upfront is far less than the cost of implementing the wrong solution based on assumptions.
