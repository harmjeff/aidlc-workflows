# AIDLC Regression Testing Suite - Requirements

## Document Information
| Attribute | Value |
|-----------|-------|
| Version | 1.0 |
| Status | Draft |
| Last Updated | 2026-01-29 |
| Related Documents | [overview.md](./overview.md) |

---

## 1. Introduction

### 1.1 Purpose
This document specifies the functional and non-functional requirements for the AIDLC Regression Testing Suite. It serves as the authoritative reference for implementation, testing, and acceptance criteria.

### 1.2 Scope
The requirements cover all components of the regression testing suite including scenario management, execution orchestration, evaluation pipelines, and reporting systems.

### 1.3 Definitions and Acronyms

| Term | Definition |
|------|------------|
| AIDLC | AI-Driven Development Life Cycle |
| Baseline | Reference metrics from a known-good AIDLC execution |
| Playbook | Pre-defined responses to AIDLC interactive questions |
| Scenario | A complete AIDLC workflow execution specification |
| SUT | System Under Test (the AIDLC rules and process) |
| LLM | Large Language Model |
| AST | Abstract Syntax Tree |
| NFR | Non-Functional Requirement |

---

## 2. Functional Requirements

### 2.1 Test Scenario Management

#### REQ-SCN-001: Scenario Definition Format
**Priority**: High  
**Description**: The system SHALL support scenario definitions in YAML format with the following structure:
```yaml
scenario:
  id: string                    # Unique identifier
  name: string                  # Human-readable name
  description: string           # Purpose and coverage
  type: greenfield | brownfield # Project type
  complexity: minimal | standard | comprehensive
  technology_stack:
    language: string            # Primary language
    framework: string           # Optional framework
  git_references:
    aidlc_rules:
      repo: string              # AIDLC workflow rules repository
      ref: string               # Git reference (branch, tag, commit)
    brownfield_source:          # Only for brownfield projects
      repo: string              # Source code repository
      ref: string               # Git reference (branch, tag, commit)
  user_request:
    prompt: string              # Initial AIDLC prompt text
    input_files:                # Optional supporting files
      - path: string            # Path to file
        type: vision_doc | environment_spec | code_template | reference_doc | other
        description: string     # Purpose of this file
  baseline:
    artifacts_path: string      # Path to baseline AIDLC output artifacts for comparison
    metrics_path: string        # Path to baseline metrics file
  expected_stages: list         # Stages expected to execute
  timeout_minutes: integer      # Maximum execution time
  playbook_ref: string          # Reference to question playbook
  functional_tests:
    path: string                # Path to functional test directory or file
    framework: pytest | jest | junit | custom
    setup_command: string       # Optional setup command before tests
    run_command: string         # Command to execute tests
```
**Acceptance Criteria**:
- Scenarios can be loaded from YAML files
- Invalid scenarios are rejected with clear error messages
- Scenario IDs must be unique within the suite
- Multiple input files can be provided for complex prompts
- Git references for both AIDLC rules and brownfield source are validated

#### REQ-SCN-002: Scenario Categories
**Priority**: High  
**Description**: The system SHALL organize scenarios into the following categories:
- Greenfield single-unit
- Greenfield multi-unit (microservices)
- Greenfield multi-unit (monolith)
- Brownfield modification
- Brownfield transformation
- Edge cases and error handling

**Acceptance Criteria**:
- Each category has at least 2 test scenarios
- Categories can be selected for targeted test runs

#### REQ-SCN-003: Technology Stack Coverage
**Priority**: Medium  
**Description**: The system SHALL support scenarios for the following technology stacks:
- Python (FastAPI, Flask, Django)
- TypeScript/JavaScript (Node.js, Express, React)
- Java (Spring Boot)
- Go

**Note**: Infrastructure-as-Code (CDK, Terraform) is explicitly excluded to minimize external impact from generated code execution.

**Acceptance Criteria**:
- At least one scenario per major language
- Scenarios include appropriate linting and testing tools
- No IaC generation or execution to prevent external resource provisioning

#### REQ-SCN-004: Complexity Level Coverage
**Priority**: Medium  
**Description**: The system SHALL include scenarios at each AIDLC depth level:
- Minimal: Simple, clear requests requiring few stages
- Standard: Normal complexity with multiple stages
- Comprehensive: Complex, high-risk projects with all stages

**Acceptance Criteria**:
- Each complexity level has representative scenarios
- Stage execution patterns match AIDLC depth level behavior

#### REQ-SCN-005: Complex Input Management
**Priority**: High  
**Description**: The system SHALL support complex multi-file inputs for AIDLC prompts:
- **Vision Documents**: Product vision, requirements specifications, business objectives
- **Environment Specifications**: Technical constraints, deployment targets, existing infrastructure
- **Code Templates**: Starter code, boilerplate, coding standards
- **Reference Documentation**: API docs, architecture diagrams, design patterns
- **Other Supporting Files**: Any additional context needed for the scenario

The system SHALL:
- Copy all input files to the workspace before AIDLC execution
- Present files to AIDLC in the order specified in the scenario
- Support various file formats (markdown, JSON, YAML, images, PDFs)
- Validate that all referenced input files exist before execution

**Acceptance Criteria**:
- Scenarios can reference multiple input files with typed categories
- Input files are available in the workspace during AIDLC execution
- Missing input files cause clear error messages before execution starts
- File copy operations are logged for reproducibility

#### REQ-SCN-006: Functional Test Provisioning
**Priority**: High  
**Description**: The system SHALL allow users to supply external functional tests through multiple methods:

**Method 1: Inline in Scenario**
```yaml
functional_tests:
  path: ./tests/functional/         # Path relative to scenario directory
  framework: pytest
  run_command: pytest tests/functional -v --junitxml=results.xml
```

**Method 2: Git Repository Reference**
```yaml
functional_tests:
  git_repo: https://github.com/org/project-tests.git
  git_ref: main
  path: functional/                  # Path within the cloned repo
  framework: jest
  run_command: npm test -- --coverage
```

**Method 3: Embedded Test Files**
```yaml
functional_tests:
  framework: pytest
  files:
    - name: test_api.py
      content: |
        def test_health_endpoint():
            response = client.get("/health")
            assert response.status_code == 200
```

The system SHALL:
- Support pytest, jest, JUnit, and custom test frameworks
- Execute setup commands before test runs (e.g., `npm install`, `pip install -r requirements.txt`)
- Collect test results in standard formats (JUnit XML)
- Provide generated code/APIs to the test environment

**Acceptance Criteria**:
- All three provisioning methods are supported
- Tests can import and exercise generated code
- Test failures produce detailed diagnostic output
- Test results are included in the overall scoring

---

### 2.2 Question Playbooks

#### REQ-PLY-001: Playbook Definition Format
**Priority**: High  
**Description**: The system SHALL support playbook definitions that specify responses to AIDLC questions:
```yaml
playbook:
  id: string
  name: string
  responses:
    - stage: string               # AIDLC stage name
      file_pattern: string        # Regex for question file
      answers:
        - question_pattern: string  # Regex to match question (primary matching)
          semantic_match: string    # Optional: semantic description for AI matching
          response: string          # Letter choice or custom text
          delay_seconds: integer    # Optional simulated think time
```
**Acceptance Criteria**:
- Playbooks can match questions by regex patterns (exact matching)
- Playbooks can match questions by semantic similarity using LLM evaluation when regex fails
- Responses support both letter choices (A, B, C, D, E) and custom text
- Missing responses fall back to AI-generated answers (see REQ-PLY-004)

#### REQ-PLY-005: Semantic Question Matching
**Priority**: High  
**Description**: The system SHALL use AI-driven semantic evaluation to match questions when regex patterns fail:
- Compare generated question text against playbook semantic descriptions
- Use LLM to determine if a question semantically matches a pre-defined answer
- Calculate confidence score for the match
- Apply match only when confidence exceeds configurable threshold (default 0.85)

**Acceptance Criteria**:
- Semantic matching is attempted after regex matching fails
- Low-confidence matches are logged for review
- Semantic matching results are tracked in reports
- Users can disable semantic matching per playbook if needed

#### REQ-PLY-002: Dynamic Response Generation
**Priority**: Medium  
**Description**: The system SHALL support dynamic response generation based on:
- Previous answers in the same execution
- Detected workspace state
- Scenario-specific configuration

**Acceptance Criteria**:
- Dynamic responses can reference scenario variables
- Context from prior stages is available for response generation

#### REQ-PLY-004: AI-Generated Answers for Unknown Questions
**Priority**: High  
**Description**: The system SHALL use AI to generate answers for questions not covered by pre-recorded playbook responses:
- Detect when no playbook response matches a question
- Use LLM to generate contextually appropriate answer
- Log AI-generated answers for review and potential playbook inclusion
- Support both multiple-choice selection and custom text generation

**Acceptance Criteria**:
- Unknown questions do not cause test failure
- AI-generated answers are consistent with scenario intent
- All AI-generated answers are flagged in reports for review
- Generated answers can be approved and added to playbooks

#### REQ-PLY-003: Approval Response Automation
**Priority**: High  
**Description**: The system SHALL automatically provide approval responses at AIDLC stage gates:
- "Approve & Continue" for normal progression
- "Request Changes" for change request testing scenarios

**Acceptance Criteria**:
- All stage gates receive appropriate responses
- Change request scenarios can test modification loops

---

### 2.3 Execution Engine

#### REQ-EXE-001: AIDLC Execution Interface
**Priority**: Critical  
**Description**: The system SHALL execute AIDLC workflows through one of the following interfaces:
- Kiro CLI (preferred for full workflow execution)
- Claude CLI (alternative CLI-based execution)
- Cline headless mode (if supported)

**Acceptance Criteria**:
- At least one execution interface is fully implemented
- Interface can be selected via configuration
- All AIDLC stages can be executed through the interface

#### REQ-EXE-002: Automated Question Detection
**Priority**: Critical  
**Description**: The system SHALL detect when AIDLC creates question files and automatically:
1. Parse the question file for [Answer]: tags
2. Look up responses from the active playbook
3. Fill in responses in the question file
4. Signal AIDLC to continue

**Acceptance Criteria**:
- Question files are detected within 5 seconds of creation
- Responses are filled correctly for all question formats
- Detection works for all question file patterns defined in AIDLC

#### REQ-EXE-003: Stage Transition Detection
**Priority**: High  
**Description**: The system SHALL detect AIDLC stage transitions by monitoring:
- Updates to aidlc-state.md
- Creation of stage-specific artifacts
- Approval request patterns in output

**Acceptance Criteria**:
- Stage transitions are logged with timestamps
- Per-stage metrics can be collected

#### REQ-EXE-004: Timeout Handling
**Priority**: High  
**Description**: The system SHALL enforce timeouts at multiple levels:
- Overall scenario timeout (configurable, default 60 minutes)
- Per-stage timeout (configurable, default 15 minutes)
- Question response timeout (configurable, default 5 minutes)

**Acceptance Criteria**:
- Timeouts trigger graceful termination
- Timeout events are logged and reported
- Partial results are preserved for analysis

#### REQ-EXE-005: Error Recovery
**Priority**: Medium  
**Description**: The system SHALL handle execution errors gracefully:
- Capture error output and stack traces
- Attempt retry for transient failures (API rate limits)
- Continue to evaluation for analyzable partial results

**Acceptance Criteria**:
- Transient failures retry up to 3 times
- Fatal errors produce detailed diagnostics
- Partial executions can still be evaluated

---

### 2.4 Sandboxed Execution Environment

#### REQ-SBX-001: Docker Container Isolation
**Priority**: Critical  
**Description**: The system SHALL execute AIDLC workflows in isolated Docker containers with:
- Dedicated filesystem (tmpfs or volume)
- Network restrictions (no external access except LLM API)
- Resource limits (memory, disk)
- Non-root execution

**Acceptance Criteria**:
- Container cannot access host filesystem outside mounted volumes
- Network access is limited to allowlisted endpoints
- Resource limits prevent runaway execution

#### REQ-SBX-002: Network Allowlist
**Priority**: High  
**Description**: The system SHALL restrict network access to:
- Anthropic API endpoints (api.anthropic.com)
- AWS Bedrock endpoints (if configured)
- Package registries (npm, PyPI, Maven) for build testing
- No other external network access

**Acceptance Criteria**:
- Allowlist is configurable per scenario
- Non-allowlisted requests are blocked and logged

#### REQ-SBX-003: Resource Quotas
**Priority**: High  
**Description**: The system SHALL enforce resource quotas:
- Memory: Configurable limit (default 4GB)
- Disk: Configurable limit (default 10GB)
- Execution time: See REQ-EXE-004

**Acceptance Criteria**:
- Quota violations terminate execution gracefully
- Resource usage is tracked and reported

#### REQ-SBX-004: Artifact Extraction
**Priority**: High  
**Description**: The system SHALL extract artifacts from the sandbox after execution:
- All files in aidlc-docs/
- Generated source code
- Build outputs and logs
- Test results

**Acceptance Criteria**:
- Artifacts are copied to persistent storage
- File permissions are preserved
- Large files can be compressed or truncated

---

### 2.5 Qualitative Evaluation

#### REQ-QUAL-001: Document Similarity Analysis
**Priority**: High  
**Description**: The system SHALL compare generated documentation against baseline using:
- Semantic similarity (embeddings-based)
- Structural similarity (section presence, order)
- Key content presence (critical terms, patterns)

**Tool**: DeepEval or Strands Evals

**Acceptance Criteria**:
- Similarity scores range from 0.0 to 1.0
- Scores are reproducible within ±0.05
- Significant deviations (>0.1) are flagged

#### REQ-QUAL-002: Code Similarity Analysis
**Priority**: High  
**Description**: The system SHALL compare generated code against baseline using:
- AST-based structural similarity
- Semantic similarity (embeddings-based)
- Functional equivalence indicators

**Acceptance Criteria**:
- Code in different styles can still match semantically
- Similarity accounts for acceptable variations (formatting, naming)
- Major structural changes are detected

#### REQ-QUAL-003: LLM-as-Judge Evaluation
**Priority**: Medium  
**Description**: The system SHALL use LLM-based evaluation for:
- Documentation coherence and completeness
- Code quality assessment
- AIDLC workflow compliance
- Best practice adherence

**Tool**: DeepEval G-Eval or custom prompts

**Acceptance Criteria**:
- Judge prompts are versioned and reproducible
- Scores include reasoning/explanation
- Evaluation cost is tracked

#### REQ-QUAL-004: Artifact Completeness Check
**Priority**: High  
**Description**: The system SHALL verify that all expected artifacts are generated:
- Required files present per stage definition
- File sizes within expected ranges
- Content structure matches templates

**Acceptance Criteria**:
- Missing artifacts are flagged as critical failures
- Unexpected artifacts are logged for review

---

### 2.6 Hard Success Measurements

#### REQ-HARD-001: Build Verification
**Priority**: Critical  
**Description**: The system SHALL verify generated code builds successfully:
- Execute language-appropriate build command
- Capture build output and errors
- Report build success/failure

**Acceptance Criteria**:
- Build commands are configurable per technology stack
- Build failures include relevant error output
- Build artifacts are preserved for inspection

#### REQ-HARD-002: Generated Unit Test Execution
**Priority**: Critical  
**Description**: The system SHALL execute unit tests generated by AIDLC:
- Run test framework (pytest, jest, JUnit, etc.)
- Collect test results in standard formats (JUnit XML)
- Calculate pass rate and coverage metrics

**Acceptance Criteria**:
- Test execution uses same environment as build
- All test results are captured
- Coverage reports are generated when possible

#### REQ-HARD-003: External Functional Test Execution
**Priority**: High  
**Description**: The system SHALL execute external functional tests defined in scenarios:
- Tests independent of AIDLC-generated tests
- Validate expected application behavior
- Support multiple test frameworks

**Acceptance Criteria**:
- External tests are stored in scenario definition
- Test failures include detailed output
- Tests can exercise generated APIs/interfaces

#### REQ-HARD-004: Linting Validation
**Priority**: High  
**Description**: The system SHALL run linters on generated code:
- Biome for JavaScript/TypeScript
- Ruff for Python
- Language-appropriate linters for other stacks

**Acceptance Criteria**:
- Linting errors are categorized by severity
- Error counts are comparable across runs
- Specific violations are logged

#### REQ-HARD-005: Security Scanning
**Priority**: Critical  
**Description**: The system SHALL perform security scanning using:
- Semgrep for pattern-based vulnerability detection
- Bandit for Python security issues
- npm audit / pip audit for dependency vulnerabilities

**Acceptance Criteria**:
- Findings are categorized by severity (critical, high, medium, low)
- Critical/high findings fail the test
- Full scan reports are preserved

#### REQ-HARD-006: Type Checking
**Priority**: Medium  
**Description**: The system SHALL perform type checking where applicable:
- mypy or pyright for Python
- tsc for TypeScript
- Language-appropriate type checkers

**Acceptance Criteria**:
- Type errors are counted and logged
- Severe type errors fail the test
- Type coverage metrics are collected when available

---

### 2.7 Non-Functional Measurements

#### REQ-NFR-001: Token Usage Tracking
**Priority**: High  
**Description**: The system SHALL track LLM token usage:
- Input tokens per API call
- Output tokens per API call
- Total tokens per stage
- Total tokens per scenario

**Acceptance Criteria**:
- Token counts are extracted from API responses
- Token costs can be calculated using configurable rates
- Token usage compared against baseline with configurable threshold

#### REQ-NFR-002: Execution Time Tracking
**Priority**: High  
**Description**: The system SHALL track execution time:
- Total scenario execution time (wall clock)
- Per-stage execution time
- Time waiting for user input (playbook response time)
- Time in LLM API calls

**Acceptance Criteria**:
- Times are measured with millisecond precision
- Stage boundaries are clearly identified
- Time regressions >20% from baseline are flagged

#### REQ-NFR-003: API Call Counting
**Priority**: Medium  
**Description**: The system SHALL count LLM API calls:
- Total calls per scenario
- Calls per stage
- Retry calls (distinguished from primary calls)

**Acceptance Criteria**:
- Call counts are deterministic for same input
- Unusual call patterns are flagged for review

#### REQ-NFR-004: Memory Usage Tracking
**Priority**: Low  
**Description**: The system SHALL track memory usage:
- Peak memory consumption of execution container
- Memory usage timeline

**Acceptance Criteria**:
- Memory metrics collected via container stats
- Memory spikes are logged

---

### 2.8 Baseline Management

#### REQ-BASE-001: Baseline Storage Format
**Priority**: High  
**Description**: The system SHALL store baselines in structured format:
```yaml
baseline:
  id: string
  created_at: datetime
  aidlc_version: string          # Git commit or tag
  scenario_id: string
  metrics:
    qualitative:
      document_similarity: float
      code_similarity: float
      completeness_score: float
    hard_success:
      build_success: boolean
      test_pass_rate: float
      lint_error_count: integer
      security_findings:
        critical: integer
        high: integer
        medium: integer
        low: integer
    non_functional:
      total_tokens: integer
      execution_time_seconds: float
      api_calls: integer
  artifacts:
    - path: string
      hash: string               # SHA256 of content
```
**Acceptance Criteria**:
- Baselines are versioned and immutable
- Previous baselines are archived, not deleted
- Baseline metadata enables traceability

#### REQ-BASE-002: Baseline Generation
**Priority**: High  
**Description**: The system SHALL support baseline generation mode:
- Execute scenarios and record all metrics
- Store generated artifacts with hashes
- Create new baseline record

**Acceptance Criteria**:
- Baseline generation is explicitly triggered
- Confirmation required before overwriting existing baseline
- Generation produces complete baseline record

#### REQ-BASE-003: Baseline Comparison
**Priority**: High  
**Description**: The system SHALL compare current execution against baseline:
- Calculate delta for each metric
- Classify deltas as improvement, regression, or neutral
- Flag significant regressions

**Acceptance Criteria**:
- Comparison thresholds are configurable
- Comparison results are machine-readable
- Comparison explains significance of changes

---

### 2.9 Reporting

#### REQ-RPT-001: Summary Report Generation
**Priority**: High  
**Description**: The system SHALL generate summary reports including:
- Overall pass/fail determination
- Score breakdown by category
- Baseline comparison highlights
- Critical findings and regressions

**Format**: HTML and JSON

**Acceptance Criteria**:
- Reports are generated automatically after each run
- HTML reports are human-readable with visualizations
- JSON reports enable programmatic analysis

#### REQ-RPT-002: Detailed Metrics Report
**Priority**: Medium  
**Description**: The system SHALL generate detailed reports including:
- Per-scenario metrics breakdown
- Per-stage metrics breakdown
- Historical trend data
- Statistical analysis

**Acceptance Criteria**:
- Detailed data exportable as CSV
- Visualizations show trends over time
- Anomalies are highlighted

#### REQ-RPT-003: Failure Analysis Report
**Priority**: High  
**Description**: The system SHALL generate failure analysis when tests fail:
- Root cause indicators
- Relevant log excerpts
- Artifact diffs (baseline vs current)
- Suggested investigation steps

**Acceptance Criteria**:
- Failure reports are actionable
- Relevant context is automatically included
- Diffs highlight significant changes

#### REQ-RPT-004: CI/CD Integration Output
**Priority**: High  
**Description**: The system SHALL produce outputs suitable for CI/CD:
- Exit codes (0=pass, 1=fail, 2=warning)
- JUnit XML format test results
- GitHub Actions annotations
- Slack/Teams notification payloads

**Acceptance Criteria**:
- CI systems can parse results automatically
- Notifications include summary and links
- Failed PRs block on regression

---

### 2.10 Configuration Management

#### REQ-CFG-001: Configuration File Format
**Priority**: High  
**Description**: The system SHALL support configuration via YAML file:
```yaml
config:
  execution:
    engine: kiro | claude_cli
    timeout_minutes: 60
    retries: 3
  sandbox:
    image: string
    memory_limit: string
    disk_limit: string
    network_allowlist: list
  evaluation:
    qualitative_threshold: 0.80
    regression_threshold: 0.20
  scoring:
    weights:
      qualitative: 0.30
      hard_success: 0.50
      non_functional: 0.20
  reporting:
    output_dir: string
    formats: list
```
**Acceptance Criteria**:
- Configuration has sensible defaults
- Configuration can be overridden via environment variables
- Invalid configuration produces clear errors

#### REQ-CFG-002: Secrets Management
**Priority**: High  
**Description**: The system SHALL handle secrets securely:
- API keys via environment variables only
- No secrets in configuration files
- Secrets not logged or reported

**Acceptance Criteria**:
- Execution fails gracefully if secrets missing
- Secrets are masked in any output
- Documentation explains secret configuration

---

## 3. Non-Functional Requirements

### 3.1 Performance

#### REQ-PERF-001: Smoke Test Execution Time
**Priority**: High  
**Description**: Quick smoke test suite SHALL complete within 30 minutes.

**Acceptance Criteria**:
- Smoke test scenarios selected for speed
- Parallelization used where possible
- Timeout enforcement prevents runaway tests

#### REQ-PERF-002: Full Suite Execution Time
**Priority**: Medium  
**Description**: Full regression suite SHALL complete within 4 hours.

**Acceptance Criteria**:
- Suite can run overnight in CI
- Progress reporting during execution
- Partial results available during run

### 3.2 Reliability

#### REQ-REL-001: Reproducibility
**Priority**: Critical  
**Description**: Same scenario with same AIDLC version SHALL produce metrics within ±5% variance.

**Acceptance Criteria**:
- Token counts are deterministic
- Similarity scores are stable
- Non-determinism sources are documented

#### REQ-REL-002: Failure Isolation
**Priority**: High  
**Description**: Failure in one scenario SHALL NOT affect other scenarios.

**Acceptance Criteria**:
- Scenarios run in isolated containers
- Shared state is minimal and managed
- Cleanup runs after each scenario

### 3.3 Maintainability

#### REQ-MAINT-001: Scenario Extensibility
**Priority**: High  
**Description**: New scenarios SHALL be addable without code changes.

**Acceptance Criteria**:
- Scenarios defined in YAML, not code
- Common patterns extractable to templates
- Documentation for scenario creation

#### REQ-MAINT-002: Tool Pluggability
**Priority**: Medium  
**Description**: Evaluation tools SHALL be pluggable.

**Acceptance Criteria**:
- Tool interfaces are abstracted
- New linters/scanners can be added via configuration
- Tool versions are pinned and documented

### 3.4 Security

#### REQ-SEC-001: Execution Isolation
**Priority**: Critical  
**Description**: Generated code SHALL NOT be able to affect the host system.

**Acceptance Criteria**:
- All execution in containers
- No privileged access
- Host filesystem not accessible

#### REQ-SEC-002: Credential Protection
**Priority**: Critical  
**Description**: API credentials SHALL be protected from generated code.

**Acceptance Criteria**:
- Credentials injected at execution time only
- Not written to any filesystem in container
- Rotation supported without code changes

---

## 4. Constraints

### 4.1 Technical Constraints
- Must run on Linux-based CI systems
- Docker must be available
- Python 3.11+ required for test harness
- LLM API access required (Anthropic or AWS Bedrock)

### 4.2 Business Constraints
- Must not incur excessive LLM API costs during development
- Must support running on developer workstations for iteration
- Must integrate with GitHub Actions

---

## 5. Assumptions

1. AIDLC rules are stable enough to establish meaningful baselines
2. Kiro CLI or Claude API provides programmatic access to AIDLC execution
3. Question file patterns are consistent and detectable
4. Generated code is intended to be buildable and testable
5. Baseline artifacts can be stored in version control or artifact storage

---

## 6. Dependencies

| Dependency | Purpose | Version |
|------------|---------|---------|
| Docker | Container isolation | 24.0+ |
| Python | Test harness implementation | 3.11+ |
| DeepEval | Qualitative evaluation | Latest |
| Strands Evals | Agent evaluation | Latest |
| Semgrep | Security scanning | Latest |
| Bandit | Python security scanning | Latest |
| Biome | JS/TS linting | Latest |
| Ruff | Python linting | Latest |
| pytest | Test framework | Latest |

---

## 7. Acceptance Criteria Summary

The AIDLC Regression Testing Suite will be accepted when:

1. **Automation**: At least 3 scenarios execute end-to-end without manual intervention
2. **Measurement**: All three measurement categories produce valid metrics
3. **Baseline**: Baselines can be created and compared
4. **Reporting**: Reports are generated with pass/fail determination
5. **CI Integration**: Suite runs in GitHub Actions and blocks on failure
6. **Documentation**: All components are documented for maintenance

---

## 8. Appendix

### A. Additional Test Tools to Consider

| Tool | Purpose | Language |
|------|---------|----------|
| SonarQube | Code quality analysis | Multiple |
| CodeClimate | Technical debt tracking | Multiple |
| Snyk | Dependency vulnerability scanning | Multiple |
| SQLFluff | SQL linting | SQL |
| ShellCheck | Shell script analysis | Bash |
| Prettier | Code formatting check | JS/TS |
| Black | Code formatting check | Python |
| gofmt | Code formatting check | Go |
| Spotless | Code formatting check | Java |

**Note**: IaC scanning tools (Checkov, Trivy for IaC, tflint) are excluded as the suite does not support Infrastructure-as-Code generation.

### B. Additional Qualitative Metrics

| Metric | Description | Tool |
|--------|-------------|------|
| Faithfulness | Answer based only on provided context | DeepEval |
| Answer Relevancy | Response relevance to query | DeepEval |
| Contextual Recall | Information retrieval completeness | DeepEval |
| Hallucination Detection | Identify fabricated content | DeepEval |
| Toxicity | Detect harmful content | DeepEval |
| Bias Detection | Identify biased outputs | DeepEval |
| Task Completion | Verify requested task accomplished | Custom |
| Instruction Following | Adherence to AIDLC rules | Custom |

### C. Scenario Ideas

| Category | Scenario Name | Description |
|----------|---------------|-------------|
| Greenfield | Todo API (Python) | Simple REST API with CRUD operations |
| Greenfield | E-commerce (TypeScript) | Multi-unit microservices architecture |
| Greenfield | CLI Tool (Go) | Command-line application |
| Brownfield | Add Feature | Add new endpoint to existing API |
| Brownfield | Refactor | Improve code structure without changing behavior |
| Brownfield | Migration | Migrate from one framework to another |
| Edge Case | Ambiguous Request | Test clarifying question behavior |
| Edge Case | Invalid Input | Test error handling |
| Edge Case | Large Codebase | Test scalability with large brownfield project |