# Domain Entities Template

Use this template to document domain entities, their attributes, and relationships for a unit.

## Template

```markdown
# Domain Entities - [unit-name]

**Unit Name:** [unit-name]
**Created:** [ISO 8601 timestamp]
**Version:** 1.0

---

## Overview

[High-level description of the domain model for this unit. Explain the key entities and their purpose in the business domain.]

---

## Domain Entities

### Entity 1: [Entity Name]

**Type:** [Aggregate Root/Entity/Value Object]

**Description:** [What this entity represents in the business domain]

**Attributes:**

| Attribute | Type | Required | Description | Constraints | Default |
|-----------|------|----------|-------------|-------------|---------|
| id | UUID | Yes | Unique identifier | - | Generated |
| [attribute1] | [type] | [Yes/No] | [Description] | [Constraints] | [Default] |
| [attribute2] | [type] | [Yes/No] | [Description] | [Constraints] | [Default] |

**Business Rules:**
- [Rule 1 that applies to this entity]
- [Rule 2 that applies to this entity]

**Lifecycle:**
- **Creation:** [How entity is created]
- **Updates:** [What can be updated and when]
- **Deletion:** [How/when entity is deleted]
- **States:** [If entity has states, list them]

**Invariants:**
- [Invariant 1 that must always be true]
- [Invariant 2 that must always be true]

[Continue for all entities]

---

## Value Objects

### Value Object 1: [Value Object Name]

**Description:** [What this value object represents]

**Attributes:**

| Attribute | Type | Required | Description | Constraints |
|-----------|------|----------|-------------|-------------|
| [attribute1] | [type] | [Yes/No] | [Description] | [Constraints] |
| [attribute2] | [type] | [Yes/No] | [Description] | [Constraints] |

**Validation Rules:**
- [Rule 1]
- [Rule 2]

**Immutability:** [Explain immutability characteristics]

**Equality:** [How equality is determined]

[Continue for all value objects]

---

## Aggregates

### Aggregate 1: [Aggregate Name]

**Aggregate Root:** [Entity name that is the root]

**Description:** [What this aggregate represents and its boundaries]

**Entities in Aggregate:**
- [Entity 1] - [Role in aggregate]
- [Entity 2] - [Role in aggregate]

**Aggregate Boundaries:**
- [What is inside the aggregate]
- [What is outside the aggregate]

**Consistency Rules:**
- [Rule 1 that must be maintained within aggregate]
- [Rule 2 that must be maintained within aggregate]

**Access Rules:**
- [How external entities access this aggregate]
- [What operations are allowed]

[Continue for all aggregates]

---

## Entity Relationships

### Relationship 1: [Entity A] ↔ [Entity B]

**Type:** [One-to-One/One-to-Many/Many-to-Many]

**Direction:** [Unidirectional/Bidirectional]

**Description:** [What this relationship represents]

**Cardinality:**
- **[Entity A]:** [0..1 / 1..1 / 0..* / 1..*]
- **[Entity B]:** [0..1 / 1..1 / 0..* / 1..*]

**Ownership:** [Which entity owns the relationship]

**Cascade Rules:**
- **Delete:** [What happens when parent is deleted]
- **Update:** [What happens when parent is updated]

**Business Rules:**
- [Rule 1 governing this relationship]
- [Rule 2 governing this relationship]

[Continue for all relationships]

---

## Entity Relationship Diagram

```
[Text-based entity relationship diagram]

┌─────────────────┐
│   Entity A      │
│─────────────────│
│ + id: UUID      │
│ + attr1: Type   │
│ + attr2: Type   │
└────────┬────────┘
         │ 1
         │
         │ *
┌────────┴────────┐
│   Entity B      │
│─────────────────│
│ + id: UUID      │
│ + entityA_id    │
│ + attr1: Type   │
└─────────────────┘
```

**Diagram Legend:**
- 1 = One
- * = Many
- 0..1 = Zero or One
- 1..* = One or Many

---

## Domain Events

[Events that occur within this domain]

### Event 1: [Event Name]

**Description:** [What this event represents]

**Trigger:** [What causes this event]

**Payload:**
```json
{
  "eventId": "UUID",
  "eventType": "[EventType]",
  "timestamp": "ISO 8601",
  "data": {
    "[field1]": "[type]",
    "[field2]": "[type]"
  }
}
```

**Consumers:** [Who/what consumes this event]

**Business Impact:** [What business effect this event has]

[Continue for all domain events]

---

## Persistence Considerations

### Entity Persistence

**Entity 1: [Entity Name]**
- **Storage:** [Database table/collection name]
- **Primary Key:** [Key field(s)]
- **Indexes:** [Required indexes]
- **Partitioning:** [Partitioning strategy if applicable]
- **Archival:** [Archival strategy if applicable]

[Continue for all entities]

### Relationship Persistence

**Relationship 1: [Relationship Name]**
- **Storage:** [How relationship is stored]
- **Foreign Keys:** [Foreign key constraints]
- **Join Strategy:** [How entities are joined]

[Continue for all relationships]

---

## Data Migration Considerations

[Considerations for migrating data to/from this domain model]

**Migration 1: [Migration Name]**
- **Source:** [Where data comes from]
- **Target:** [Where data goes to]
- **Transformation:** [How data is transformed]
- **Validation:** [How migration is validated]
- **Rollback:** [Rollback strategy]

[Continue for all migrations]

---

## Domain Model Patterns

[Design patterns used in this domain model]

**Pattern 1: [Pattern Name]**
- **Type:** [Repository/Factory/Specification/etc.]
- **Purpose:** [Why this pattern is used]
- **Implementation:** [How it's implemented]
- **Entities Affected:** [Which entities use this pattern]

[Continue for all patterns]

---

## Bounded Context

[Define the bounded context for this domain model]

**Context Name:** [Name of bounded context]

**Boundaries:**
- **Inside Context:** [What is inside]
- **Outside Context:** [What is outside]

**Context Mapping:**
- **Upstream Contexts:** [Contexts this depends on]
- **Downstream Contexts:** [Contexts that depend on this]
- **Integration Patterns:** [How contexts integrate]

**Ubiquitous Language:**
- **[Term 1]:** [Definition in this context]
- **[Term 2]:** [Definition in this context]

---

## Entity Validation

[Validation rules for entities]

**Entity 1: [Entity Name]**

**Attribute Validation:**
- **[attribute1]:** [Validation rules]
- **[attribute2]:** [Validation rules]

**Entity-Level Validation:**
- [Cross-attribute validation rule 1]
- [Cross-attribute validation rule 2]

**Validation Timing:**
- **On Creation:** [What is validated]
- **On Update:** [What is validated]
- **On Delete:** [What is validated]

[Continue for all entities]

---

## Entity Lifecycle States

[If entities have lifecycle states, document them]

**Entity 1: [Entity Name]**

**States:**
1. **[State 1]** - [Description]
2. **[State 2]** - [Description]
3. **[State 3]** - [Description]

**State Transitions:**
```
[State 1] --[Event/Action]--> [State 2]
[State 2] --[Event/Action]--> [State 3]
[State 3] --[Event/Action]--> [State 1]
```

**State Rules:**
- **[State 1]:** [What is allowed/not allowed in this state]
- **[State 2]:** [What is allowed/not allowed in this state]

[Continue for all entities with states]

---

## Entity Security

[Security considerations for entities]

**Entity 1: [Entity Name]**

**Access Control:**
- **Read:** [Who can read]
- **Create:** [Who can create]
- **Update:** [Who can update]
- **Delete:** [Who can delete]

**Sensitive Attributes:**
- **[attribute1]:** [Encryption/masking requirements]
- **[attribute2]:** [Encryption/masking requirements]

**Audit Requirements:**
- [What changes must be audited]
- [What information must be logged]

[Continue for all entities]

---

## Entity Performance

[Performance considerations for entities]

**Entity 1: [Entity Name]**

**Query Patterns:**
- [Common query pattern 1]
- [Common query pattern 2]

**Optimization:**
- [Optimization strategy 1]
- [Optimization strategy 2]

**Caching:**
- **Strategy:** [Caching strategy]
- **TTL:** [Time to live]
- **Invalidation:** [When cache is invalidated]

[Continue for all entities]

---

## Domain Model Assumptions

[Assumptions made in this domain model]

1. [Assumption 1]
2. [Assumption 2]
3. [Continue as needed]

---

## Domain Model Constraints

[Constraints and limitations of this domain model]

1. [Constraint 1]
2. [Constraint 2]
3. [Continue as needed]

---

## Future Considerations

[Potential future changes or extensions to the domain model]

1. [Future consideration 1]
2. [Future consideration 2]
3. [Continue as needed]

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
- When documenting domain model for new features
- When clarifying entity structures and relationships

### Customization
- Remove sections not applicable to your unit
- Add sections for unit-specific concerns
- Adjust detail level based on complexity
- Use consistent naming conventions

### Best Practices
- Use ubiquitous language from the domain
- Be specific about types and constraints
- Document business rules that apply to entities
- Include relationship cardinality and ownership
- Consider persistence and performance implications
- Document security and audit requirements

### Common Mistakes to Avoid
- ❌ Using technical database terms instead of domain language
- ❌ Forgetting to document relationships between entities
- ❌ Not specifying required vs optional attributes
- ❌ Mixing domain entities with DTOs or view models
- ❌ Not documenting entity lifecycle and states
- ❌ Forgetting to specify validation rules
- ❌ Not considering aggregate boundaries

### Entity Type Guidelines

**Aggregate Root:**
- Entry point to an aggregate
- Has global identity
- Enforces aggregate invariants
- Controls access to entities within aggregate

**Entity:**
- Has identity that persists over time
- Can be part of an aggregate
- Mutable

**Value Object:**
- No identity, defined by attributes
- Immutable
- Can be shared
- Equality based on attribute values

