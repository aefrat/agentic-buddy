---
last_accessed: 2026-07-02
access_count: 0
created: 2026-07-02
---

# Three-tier progressive criteria model

A pattern for structuring release milestones as strict supersets: each
milestone inherits all criteria from the previous one and adds new ones.
Prevents the common failure mode of defining GA criteria that are
disconnected from intermediate milestones.

## Pattern

- **Structure:** Milestone N+1 criteria = Milestone N criteria + new criteria
- **Measurability:** Every criterion has a binary pass/fail condition (not
  percentages or subjective assessments)
- **Inheritance:** Passing Milestone N+1 guarantees Milestone N criteria
  are also met
- **Naming:** Clear tier labeling (e.g., Monthly/Tech Preview/GA, or EC/RC/GA)

## Why it works

When intermediate and final milestones share no criteria, teams can pass an
intermediate checkpoint while making no progress toward GA readiness.
Superset chains force continuous progress: each milestone validates a
growing subset of what the final release requires.

## Prior art

- RHIVOS CTC: Two-phase (Reduced CAT then Full CAT), where Full is a
  superset of Reduced
- OpenShift QE: EC/RC/GA build validation tiers
- Applied: RHAS release criteria (Monthly 8 / Tech Preview +7=15 / GA +8=23)

## When to apply

Use when designing release criteria for products with multiple intermediate
milestones. Most valuable when:
- Multiple teams contribute criteria independently (prevents "my criteria
  only applies at GA" silos)
- Intermediate milestones need to provide meaningful quality signals, not
  just schedule gates
- The product has a history of GA criteria being defined late and
  disconnected from earlier milestones

> Source: [2026-07-02 log](../../logs/2026-07-02.md) - RHAS QE Expert Lead
> Agent design decisions
