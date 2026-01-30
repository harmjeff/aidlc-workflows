# AIDLC Regression Testing Suite - Project Description

## Description
The AIDLC Regression Testing Suite is an automated quality assurance framework that validates changes to the AI-Driven Development Life Cycle (AIDLC) workflow rules. It executes predefined test scenarios through the AIDLC process, measures output quality against baselines, and generates comprehensive reports identifying regressions in documentation quality, code generation, security, and resource efficiency.

---

## Working Backwards - 5 Customer Questions

### 1. Who is the customer?

**Primary Customers:**
- **AIDLC Rule Authors**: Engineers who modify AIDLC workflow rules, prompts, and stage definitions. They need confidence that their changes don't break existing functionality.
- **AIDLC Maintainers**: Teams responsible for the overall health and evolution of the AIDLC framework. They need visibility into how changes affect quality over time.

**Secondary Customers:**
- **AIDLC End Users**: Developers using AIDLC for software development. They benefit indirectly through more stable and reliable AIDLC releases.
- **Platform Teams**: Teams integrating AIDLC into their development workflows. They need assurance that AIDLC updates won't disrupt their processes.

---

### 2. What is the customer problem or opportunity?

**The Problem:**
Currently, when AIDLC rule authors make changes to the workflow (modifying prompts, adding stages, adjusting logic), they have no systematic way to verify that:
- Generated documentation maintains the same quality and structure
- Generated code is functionally equivalent and secure
- Resource consumption (tokens, time) hasn't regressed significantly
- The workflow still produces working, buildable, testable outputs

**The Pain Points:**
1. **Manual Testing is Slow**: Authors must manually run AIDLC through multiple scenarios to validate changes, which takes hours and is error-prone.
2. **Inconsistent Validation**: Different reviewers apply different standards, leading to inconsistent quality gates.
3. **Hidden Regressions**: Subtle degradations in output quality or increased resource usage go undetected until users report problems.
4. **Fear of Change**: Authors hesitate to make improvements because they can't confidently assess the impact.

**The Opportunity:**
An automated regression testing suite enables confident, rapid iteration on AIDLC rules with quantitative quality gates. This accelerates AIDLC improvement while protecting end-user experience.

---

### 3. What is the most important customer benefit?

**Confidence to Ship Changes Quickly**

Rule authors can submit changes knowing that an automated system will:
- Execute the full AIDLC workflow across representative scenarios
- Quantitatively compare outputs against known-good baselines
- Clearly report any regressions with root cause indicators
- Block merges when quality gates fail

**This means:**
- 10x faster validation cycle (minutes for smoke tests vs. hours of manual testing)
- Consistent, objective quality standards across all changes
- Early detection of regressions before they reach end users
- Documented evidence of change impact for code reviews

---

### 4. How do you know what the customer needs or wants?

**Evidence of Need:**

1. **Direct Feedback**: AIDLC authors have expressed frustration with the manual validation process and requested automated testing.

2. **Industry Best Practice**: Mature AI systems (LangChain, LlamaIndex, agent frameworks) all include evaluation suites. AIDLC lacks this standard tooling.

3. **Analogous Success**: Strands Agents Evals and DeepEval demonstrate that automated LLM output evaluation is both feasible and valuable.

4. **Development Velocity**: AIDLC development has slowed due to the overhead of manual validation. Authors delay changes or skip thorough testing.

**Validation Approach:**
- Interview AIDLC rule authors about their current validation workflow
- Prototype with 2-3 test scenarios and gather feedback on report usefulness
- Iterate on scoring model based on author input about what matters most

---

### 5. What does the customer experience look like?

**Developer Workflow:**

1. **Author makes a change** to AIDLC rules in a feature branch.

2. **Opens a Pull Request** - CI automatically triggers the smoke test suite (15-30 min).

3. **Reviews the regression report** in the PR:
   ```
   ✅ AIDLC Regression Test: PASSED
   
   📊 Scores (vs baseline):
   - Qualitative: 0.92 (baseline: 0.90) ↑ +2%
   - Hard Success: 100% (baseline: 100%) → 
   - Non-Functional: -5% tokens, -3% time ↑
   
   📁 3 scenarios executed, 0 failures
   ```

4. **If warnings/failures occur**, clicks through to detailed report:
   - Which scenarios regressed
   - Side-by-side diffs of generated artifacts
   - Specific metrics that degraded
   - Suggested investigation steps

5. **Merges with confidence** when all checks pass, or iterates if regressions found.

**For Nightly Full Regression:**
- Full suite runs automatically each night
- Dashboard shows trend lines over time
- Slack notification if regressions detected
- Historical data informs capacity planning

---

## FAQs

### How will you measure the success of this idea?

**Summary (< 460 chars):**
> Primary: validation time <30 min (smoke), regression detection >95%, 2x increase in rule change velocity. Secondary: false positive rate <5%, test coverage >80%. At 6 months: CI running for all PRs, 10+ scenarios, zero escaped regressions, author NPS >40.

**Primary Metrics:**

| Metric | Target | How Measured |
|--------|--------|--------------|
| **Change Validation Time** | <30 min (smoke), <4 hr (full) | CI pipeline duration |
| **Regression Detection Rate** | >95% of regressions caught before merge | Compare pre-merge vs post-merge issues |
| **Author Confidence** | >80% of authors report increased confidence | Quarterly survey |
| **Change Velocity** | 2x increase in AIDLC rule changes per month | PR merge frequency |

**Secondary Metrics:**

| Metric | Target | How Measured |
|--------|--------|--------------|
| **False Positive Rate** | <5% of test runs | Manual review of flagged regressions |
| **Test Coverage** | >80% of AIDLC stages tested | Stage execution tracking |
| **Baseline Freshness** | <30 days old | Baseline creation timestamps |
| **Report Actionability** | >90% of failures have clear next steps | Author feedback |

**Success Criteria at 6 Months:**
1. Suite running in CI for all AIDLC PRs
2. At least 10 test scenarios covering major use cases
3. Zero regressions shipped to production that would have been caught by suite
4. Author NPS >40 for the testing experience

---

### What resources are needed for building this idea?

**Summary (< 460 chars):**
> Team: 2 person-months (Lead 50%/3mo, Engineer 100%/2mo, Domain Expert 20%/3mo). Open source tools: DeepEval, Strands Evals, Semgrep, Ruff/Biome, pytest. Timeline: MVP in 3 weeks, full system in 8 weeks.

**Team:**

| Role | Effort | Responsibilities |
|------|--------|------------------|
| **Lead Engineer** | 50% for 3 months | Architecture, core implementation, CI integration |
| **Engineer** | 100% for 2 months | Scenario creation, evaluation pipeline, reporting |
| **AIDLC Domain Expert** | 20% for 3 months | Scenario design, baseline validation, quality criteria |

**Infrastructure:**

| Resource | Cost Estimate | Purpose |
|----------|---------------|---------|
| **LLM API Credits** | $500-1000/month | AIDLC execution, qualitative evaluation |
| **CI Compute** | $100-200/month | Docker containers, test execution |
| **Artifact Storage** | $20-50/month | Baseline storage, report archives |

**Tools (Open Source):**

| Tool | License | Purpose |
|------|---------|---------|
| DeepEval | Apache 2.0 | Qualitative evaluation |
| Strands Evals | Apache 2.0 | Agent evaluation |
| Semgrep | LGPL | Security scanning |
| Ruff/Biome | MIT | Linting |
| pytest | MIT | Test orchestration |

**Timeline:**

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| **Phase 1: Foundation** | 3 weeks | Core harness, 3 scenarios, basic reporting |
| **Phase 2: Evaluation** | 2 weeks | Full evaluation pipeline, baseline system |
| **Phase 3: Integration** | 1 weeks | CI integration, notifications, dashboards |
| **Phase 4: Expansion** | 2 weeks | 10+ scenarios, documentation, handoff |

**Total Estimated Investment:**
- **Engineering**: ~4 person-months
- **Time to Value**: MVP in 3 weeks, full system in 8 weeks

---

### What are the main risks and how will you mitigate them?

**Summary (< 460 chars):**
> Key risks: (1) LLM non-determinism causing flaky tests - mitigate with similarity thresholds and multiple runs; (2) High API costs - mitigate with smoke test subset and caching; (3) AIDLC changes breaking harness - mitigate with abstraction layer; (4) Low adoption - mitigate with CI integration and clear reports. Risk reviews monthly.

**Risk Details:**

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| **LLM output non-determinism** | Flaky tests, false positives | High | Use similarity thresholds (not exact match), run scenarios multiple times, statistical confidence |
| **High LLM API costs** | Budget overrun | Medium | Smoke test subset for PRs, caching responses, cost tracking per run |
| **AIDLC interface changes** | Harness breaks frequently | Medium | Abstract execution interface, version pinning, integration tests for harness |
| **Baseline drift** | False regressions from stale baselines | Medium | Baseline freshness alerts, automated baseline refresh process |
| **Low team adoption** | Investment wasted | Low | CI integration (mandatory), clear actionable reports, training sessions |
| **Complex scenario maintenance** | Technical debt | Medium | Scenario templates, inheritance, documentation |

---

### What are the dependencies on other teams or systems?

**Summary (< 460 chars):**
> Dependencies: (1) AIDLC team for rule file stability; (2) Kiro/Claude CLI teams for execution interface; (3) CI/CD team for pipeline integration; (4) Security team for Semgrep rule approval. External: Anthropic API availability. No hard blockers identified; can start with Claude CLI while Kiro integration develops.

**Dependency Details:**

| Dependency | Owner | Type | Risk Level |
|------------|-------|------|------------|
| AIDLC rule file format stability | AIDLC Team | Input format | Low - documented schema |
| Kiro CLI or Claude CLI availability | CLI Teams | Execution engine | Medium - fallback options exist |
| CI/CD pipeline access | Platform Team | Integration | Low - standard GitHub Actions |
| LLM API (Anthropic/Bedrock) | External | Service | Medium - rate limits, costs |
| Security scanning rules (Semgrep) | Security Team | Configuration | Low - use defaults initially |
| Test scenario content | AIDLC Domain Experts | Knowledge | Medium - requires domain input |

**Coordination Plan:**
- Weekly sync with AIDLC team during development
- Early engagement with CLI teams on interface requirements
- Security review before production deployment

---

### What alternative approaches did you consider?

**Summary (< 460 chars):**
> Alternatives: (1) Manual testing checklist - rejected: slow, inconsistent; (2) Unit tests for rules only - rejected: misses integration issues; (3) Production monitoring only - rejected: reactive not preventive; (4) Third-party eval platform - rejected: doesn't understand AIDLC workflow. Chose custom suite for full workflow coverage.

**Alternatives Analysis:**

| Approach | Pros | Cons | Decision |
|----------|------|------|----------|
| **Manual testing checklist** | Low initial cost, flexible | Slow, inconsistent, doesn't scale, human error | ❌ Rejected |
| **Unit tests for rule files** | Fast, deterministic | Misses workflow integration, can't test LLM behavior | ❌ Rejected (partial use) |
| **Production monitoring + rollback** | Real user feedback, low upfront cost | Reactive not preventive, poor UX for users hit by bugs | ❌ Rejected |
| **Third-party eval platform (Braintrust, etc.)** | Ready-made, maintained | Doesn't understand AIDLC workflow, limited customization | ❌ Rejected |
| **Custom regression suite** | Full control, workflow-aware, comprehensive | Development investment, maintenance burden | ✅ Selected |

**Why Custom Suite Wins:**
- AIDLC's multi-stage workflow requires specialized automation (question answering, stage detection)
- Baseline comparison needs AIDLC-specific artifact understanding
- Integration with existing CI/CD is critical for adoption

---

### Who will maintain this after initial development?

**Summary (< 460 chars):**
> Ownership: AIDLC Core Team (primary), Platform Team (CI integration). Maintenance: ~0.5 FTE ongoing for scenarios, baselines, tooling updates. Runbook and on-call rotation for failures. Handoff includes documentation, training, and 2-week shadowing period. Long-term: community contributions for new scenarios.

**Ownership Model:**

| Component | Owner | Maintenance Effort |
|-----------|-------|-------------------|
| Core test harness | AIDLC Core Team | ~0.2 FTE - bug fixes, improvements |
| Test scenarios | AIDLC Authors | ~0.2 FTE - new scenarios, updates |
| Baselines | AIDLC Authors | ~0.1 FTE - refresh monthly |
| CI/CD integration | Platform Team | Minimal - stable after setup |
| Evaluation tools | AIDLC Core Team | Minimal - update tool versions |

**Handoff Plan:**
1. Documentation: Architecture, runbooks, troubleshooting guides
2. Training: 2 sessions for maintainers (technical deep-dive, scenario creation)
3. Shadowing: 2-week period where builder supports maintainers
4. On-call: Rotation for test failures with escalation path

**Long-term Sustainability:**
- Scenario contributions from AIDLC users
- Automated baseline refresh to reduce manual burden
- Self-healing for transient failures

---

### What is the minimum viable product (MVP)?

**Summary (< 460 chars):**
> MVP (4 weeks): 3 test scenarios (greenfield Python, TypeScript, brownfield), basic playbook automation, build/lint/security checks, token/time tracking, HTML report with pass/fail. Excludes: qualitative similarity scoring, full baseline system, dashboards. Validates core hypothesis with minimal investment.

**MVP Scope:**

| Feature | MVP | Full |
|---------|-----|------|
| Test scenarios | 3 (Python, TypeScript, Brownfield) | 10+ |
| Question automation | Basic regex playbooks | AI-driven matching |
| Execution engine | Single CLI (Kiro or Claude) | Multiple options |
| Build verification | ✅ Yes | ✅ Yes |
| Linting/Security | ✅ Yes | ✅ Yes |
| Token/Time tracking | ✅ Yes | ✅ Yes |
| Qualitative similarity | ❌ No | ✅ Yes (DeepEval) |
| Baseline comparison | Simple hash comparison | Full metrics comparison |
| Reporting | Basic HTML | Dashboard + trends |
| CI Integration | Manual trigger | Full PR automation |

**MVP Success Criteria:**
1. Execute 3 scenarios end-to-end without manual intervention
2. Produce pass/fail report with actionable details
3. Detect intentionally introduced regression in test scenario
4. Complete in <30 minutes

**MVP Timeline:** 3 weeks with 1 engineer full-time

---

### How does this integrate with existing CI/CD infrastructure?

**Summary (< 460 chars):**
> Integration: GitHub Actions workflow triggered on PR (smoke) and nightly (full). Docker container execution for isolation. Outputs: JUnit XML for test results, PR comments with summary, Slack notifications for failures. Standard patterns - no custom CI infrastructure required. Works with existing branch protection rules.

**Integration Architecture:**

```
┌────────────────────────────────────────────────────────────┐
│                     GitHub Repository                      │
├────────────────────────────────────────────────────────────┤
│  PR Created/Updated          │  Scheduled (Nightly)        │
│         │                    │         │                   │
│         v                    │         v                   │
│  ┌─────────────────┐         │  ┌─────────────────┐        │
│  │  Smoke Tests    │         │  │  Full Suite     │        │
│  │  (15-30 min)    │         │  │  (2-4 hours)    │        │
│  └────────┬────────┘         │  └────────┬────────┘        │
│           │                  │           │                 │
│           v                  │           v                 │
│  ┌─────────────────────────────────────────────────┐       │
│  │              Docker Container                   │       │
│  │  - AIDLC execution (Kiro/Claude CLI)            │       │
│  │  - Build, lint, test                            │       │
│  │  - Evaluation pipeline                          │       │
│  └──────────────────────┬──────────────────────────┘       │
│                         │                                  │
│           ┌─────────────┴─────────────┐                    │
│           v                           v                    │
│  ┌─────────────────┐         ┌─────────────────┐           │
│  │  PR Comment     │         │  Slack Alert    │           │
│  │  (summary)      │         │  (failures)     │           │
│  └─────────────────┘         └─────────────────┘           │
│                                                            │
│           │                                                │
│           v                                                │
│  ┌─────────────────┐                                       │
│  │  Branch         │                                       │
│  │  Protection     │  ← Blocks merge if tests fail         │
│  └─────────────────┘                                       │
└────────────────────────────────────────────────────────────┘
```

**CI/CD Outputs:**
- JUnit XML test results (parsed by GitHub)
- PR comment with summary and links
- Exit codes: 0=pass, 1=fail, 2=warning
- Artifacts: full reports, logs, generated code

**Requirements:**
- GitHub Actions (or similar CI system)
- Docker available on runners
- Secrets: LLM API keys
- No custom infrastructure needed

---

## Summary for Project Submission

**One-Line Description:**
> Automated regression testing for AIDLC that compares generated code and documentation against baselines, ensuring rule changes don't degrade quality.

**Problem Statement:**
> AIDLC authors cannot confidently validate that rule changes don't regress output quality, leading to slow iteration and escaped defects.

**Solution:**
> A test suite that automatically executes AIDLC scenarios, measures qualitative and functional metrics against baselines, and gates CI merges on quality thresholds.

**Success Metric:**
> Catch 95% of regressions before merge, reduce validation time from hours to <30 minutes.

**Resource Ask:**
> 4 person-months engineering + ~$500/month ongoing infrastructure.