# Unit of Work Generation Plan

**Created**: [ISO timestamp]

## Plan Overview
This plan outlines the approach for decomposing the system into manageable units of work.

---

## Context-Appropriate Questions

Please answer the following questions to help create the unit of work breakdown:

### Question 1: Unit Decomposition Strategy
How should the system be decomposed into units of work?

A) By component (one unit per major component)
B) By service (one unit per service)
C) By feature (one unit per feature or epic)
D) By layer (one unit per architectural layer)
E) By user story (one unit per story)
F) Custom boundaries (describe after [Answer]: tag)
X) Other (please describe after [Answer]: tag below)

[Answer]: 

---

### Question 2: Unit Granularity
How granular should the units be?

A) Coarse-grained (few large units, 2-3 units)
B) Medium-grained (moderate number of units, 4-6 units)
C) Fine-grained (many small units, 7+ units)
X) Other (please describe after [Answer]: tag below)

[Answer]: 

---

### Question 3: Unit Dependencies
How should unit dependencies be handled?

A) Sequential (units must be completed in order)
B) Parallel (units can be completed independently)
C) Mixed (some sequential, some parallel)
X) Other (please describe after [Answer]: tag below)

[Answer]: 

---

### Question 4: Unit Prioritization
How should units be prioritized?

A) By business value (highest value first)
B) By risk (highest risk first)
C) By dependencies (foundational units first)
D) By user stories (story priority determines unit priority)
E) All equal priority
X) Other (please describe after [Answer]: tag below)

[Answer]: 

---

### Question 5: Unit Testing Strategy
How should units be tested?

A) Unit tests only (test each unit in isolation)
B) Integration tests after each unit (test unit integration)
C) Integration tests after all units (test full system integration)
D) Mixed approach (varies by unit)
X) Other (please describe after [Answer]: tag below)

[Answer]: 

---

### Question 6: Story-to-Unit Mapping
How should user stories be mapped to units?

A) One story per unit (fine-grained)
B) Multiple stories per unit (grouped by feature)
C) Stories span multiple units (complex features)
D) No story mapping (not using user stories)
X) Other (please describe after [Answer]: tag below)

[Answer]: 

---

## Unit Generation Steps

Once questions are answered, I will:

- [ ] 1. Analyze answers and resolve any ambiguities
- [ ] 2. Identify unit boundaries based on decomposition strategy
- [ ] 3. Define each unit of work
- [ ] 4. Map components to units
- [ ] 5. Map services to units
- [ ] 6. Map user stories to units (if applicable)
- [ ] 7. Identify unit dependencies
- [ ] 8. Create unit dependency graph
- [ ] 9. Prioritize units
- [ ] 10. Generate unit-of-work.md
- [ ] 11. Generate unit-of-work-dependency.md
- [ ] 12. Generate unit-of-work-story-map.md (if using stories)
- [ ] 13. Review and validate completeness

---

## Mandatory Artifacts

The following artifacts will be created:

1. **unit-of-work.md** - Unit definitions and responsibilities
2. **unit-of-work-dependency.md** - Unit dependency relationships
3. **unit-of-work-story-map.md** - Story-to-unit mapping (if using stories)

---

**Instructions:**
1. Answer each question by entering the letter of your choice after [Answer]:
2. If you select "Other", please provide details after the [Answer]: tag
3. Let me know when you've completed all questions
