# AIDLC Regression Testing Suite - Overview

## Executive Summary

This document outlines the design of a comprehensive regression testing suite for the AI-Driven Development Life Cycle (AIDLC). The suite enables systematic evaluation of changes to the AIDLC process by measuring stability, output quality, and resource consumption against established baselines.

## Purpose

The AIDLC Regression Testing Suite serves to:

1. **Detect Regressions**: Identify unintended changes in output quality or behavior when modifying AIDLC rules, prompts, or workflow logic
2. **Benchmark Performance**: Measure and track resource consumption (tokens, time) across versions
3. **Ensure Quality**: Validate that generated code and documentation meet established quality standards
4. **Enable Continuous Improvement**: Provide quantitative data to guide AIDLC enhancements

## Scope

### In Scope
- Automated execution of AIDLC workflows in controlled environments
- Qualitative assessment of generated artifacts (documentation and code)
- Functional validation through external test suites
- Security and safety scanning of generated code
- Resource consumption tracking (tokens, execution time)
- Baseline comparison and scoring
- Report generation and trend analysis

### Out of Scope
- Production deployment of generated applications
- Manual review workflows
- Real-time monitoring of production AIDLC usage

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         AIDLC Regression Testing Suite                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                   │
│  │   Test       │    │  Execution   │    │  Evaluation  │                   │
│  │   Scenarios  │───>│  Engine      │───>│  Pipeline    │                   │
│  └──────────────┘    └──────────────┘    └──────────────┘                   │
│         │                   │                   │                           │
│         v                   v                   v                           │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                   │
│  │  Question    │    │  Sandboxed   │    │  Metrics     │                   │
│  │  Playbooks   │    │  Container   │    │  Collector   │                   │
│  └──────────────┘    └──────────────┘    └──────────────┘                   │
│                             │                   │                           │
│                             v                   v                           │
│                      ┌──────────────┐    ┌──────────────┐                   │
│                      │  Artifact    │    │  Report      │                   │
│                      │  Storage     │───>│  Generator   │                   │
│                      └──────────────┘    └──────────────┘                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Test Scenarios
Pre-defined AIDLC workflow executions representing diverse use cases:
- Greenfield single-unit applications
- Greenfield multi-unit microservices
- Brownfield modifications
- Various technology stacks (Python, TypeScript, Java, etc.)
- Different complexity levels (minimal, standard, comprehensive)

### 2. Question Playbooks
Automated response mechanisms for AIDLC's interactive questions:
- Pre-recorded answers for deterministic replay
- AI Created answers for new/unknown questions
- Configurable response strategies
- Support for multiple-choice and custom responses

### 3. Execution Engine
Orchestrates AIDLC workflow execution:
- Integration with Kiro CLI or Claude CLI
- Execution state management
- Error handling and recovery

### 4. Sandboxed Container
Isolated execution environment:
- Docker-based isolation
- Network restrictions
- Filesystem isolation
- Resource quotas (memory, disk)

### 5. Evaluation Pipeline
Multi-stage artifact assessment:
- Qualitative analysis (similarity scoring)
- Functional validation (test execution)
- Security scanning (static analysis)
- Resource measurement (tokens, time)

### 6. Metrics Collector
Aggregates measurements from all evaluation stages:
- Normalized scoring across categories
- Trend tracking over time
- Anomaly detection

### 7. Report Generator
Produces human and machine-readable reports:
- HTML dashboards
- JSON/CSV data exports
- Baseline comparison summaries
- Pass/fail determinations

## Measurement Categories

### 1. Qualitative Measurements
**Goal**: Assess semantic similarity and quality of generated artifacts

| Measurement | Tool | Target |
|-------------|------|--------|
| Document Similarity | DeepEval, Strands Evals | aidlc-docs/ artifacts |
| Code Similarity | DeepEval, AST comparison | Generated source code |
| Prompt Adherence | Custom LLM-as-judge | Workflow compliance |
| Coherence | DeepEval G-Eval | Documentation quality |

### 2. Hard Success Measurements
**Goal**: Binary pass/fail validation of generated code

| Measurement | Tool | Target |
|-------------|------|--------|
| External Functional Tests | pytest, jest, JUnit | Application behavior |
| Generated Unit Tests | Test framework runners | Unit test execution |
| Linting | Biome (JS/TS), Ruff (Python) | Code style/errors |
| Security Scan | Semgrep, Bandit | Vulnerabilities |
| Type Checking | mypy, tsc, pyright | Type safety |
| Build Success | Language-specific build tools | Compilation |

### 3. Non-Functional Requirements
**Goal**: Track resource consumption and efficiency

| Measurement | Method | Target |
|-------------|--------|--------|
| Token Usage | API response parsing | Input/output tokens |
| Execution Time | Wall clock measurement | Total workflow time |
| Stage Duration | Per-stage timing | Individual stage times |
| API Calls | Request counting | Number of LLM calls |
| Memory Usage | Container metrics | Peak memory consumption |

## Scoring Model

### Category Weights (Configurable)
```yaml
qualitative:
  weight: 0.30
  threshold: 0.80
  
hard_success:
  weight: 0.50
  threshold: 0.90
  
non_functional:
  weight: 0.20
  threshold: 1.20  # Max 20% regression from baseline
```

### Overall Score Calculation
```
overall_score = Σ (category_score × category_weight)

where:
  category_score = (achieved_metrics / baseline_metrics) × pass_rate
```

### Pass/Fail Criteria
- **Pass**: Overall score ≥ 0.85 AND all hard_success tests pass
- **Warning**: Overall score ≥ 0.70 OR any security findings
- **Fail**: Overall score < 0.70 OR critical security findings OR build failure

## Execution Modes

### 1. Full Regression Suite
Complete execution of all test scenarios against current AIDLC rules
- Triggered: On PR merge to main, scheduled nightly
- Duration: ~2-4 hours

### 2. Quick Smoke Test
Subset of critical test scenarios
- Triggered: On PR creation, manual trigger
- Duration: ~15-30 minutes

### 3. Focused Test
Single scenario execution for development iteration
- Triggered: Manual with scenario selection
- Duration: ~5-15 minutes per scenario

### 4. Baseline Generation
Execute scenarios to establish new baseline metrics
- Triggered: Manual after major changes
- Duration: ~2-4 hours

## Technology Stack

| Component | Technology |
|-----------|------------|
| Orchestration | Python, pytest |
| Container Runtime | Docker |
| AIDLC Execution | Kiro CLI, Claude API |
| Qualitative Eval | DeepEval, Strands Evals |
| Linting | Biome, Ruff, ESLint |
| Security Scan | Semgrep, Bandit |
| Reporting | Jinja2, Plotly |
| Data Storage | SQLite, JSON files |
| CI Integration | GitHub Actions |

## Directory Structure

```
ideas/regression_testing/
├── overview.md                    # This document
├── requirements.md                # Detailed requirements
├── architecture.md                # Technical architecture
├── scenarios/                     # Test scenario definitions
│   ├── greenfield/
│   ├── brownfield/
│   └── templates/
├── playbooks/                     # Question response playbooks
├── baselines/                     # Baseline metrics storage
├── reports/                       # Generated reports
└── tools/                         # Supporting utilities
```

## Success Criteria

The regression testing suite will be considered successful when:

1. **Automation**: AIDLC workflows can be executed without human intervention
2. **Reproducibility**: Same inputs produce consistent evaluation scores (±5%)
3. **Coverage**: All AIDLC phases and stage combinations are testable
4. **Speed**: Quick smoke tests complete within 30 minutes
5. **Actionability**: Reports clearly identify regressions and their causes
6. **Integration**: Suite integrates with CI/CD pipelines

## Next Steps

1. **Requirements Document**: Detail functional and non-functional requirements
2. **Architecture Document**: Define technical implementation details
3. **Scenario Design**: Create initial test scenario definitions
4. **Prototype**: Build minimal viable test harness
5. **Baseline**: Establish initial baseline metrics
6. **Integration**: Connect to CI/CD pipeline

## References

- [DeepEval Documentation](https://docs.confident-ai.com/)
- [Strands Agents Evals](https://github.com/strands-agents/evals)
- [Semgrep Rules](https://semgrep.dev/docs/)
- [Bandit Security Linter](https://bandit.readthedocs.io/)
- [Biome Linter](https://biomejs.dev/)
- [Ruff Linter](https://docs.astral.sh/ruff/)