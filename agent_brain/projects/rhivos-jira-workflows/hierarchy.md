---
last_accessed: 2026-07-15
access_count: 1
created: 2026-07-15
---

# Mapping Work to Strategic Goals (Features vs Initiatives)

RHIVOS uses standard Red Hat Jira issue types, with additional refinement for
Features and Initiatives in the AUTOBU project.

## Hierarchy Overview

```
Outcome (AUTOBU)
  |
  +-- Feature (AUTOBU) -- product work (code changes)
  |     |
  |     +-- Epic (VROOM) -- scoped to one milestone/release
  |           |
  |           +-- Story / Bug / Weakness / Vulnerability / Task
  |
  +-- Initiative (AUTOBU) -- non-product work (infrastructure/process)
        |
        +-- Epic (VROOM) -- scoped to one milestone/release
              |
              +-- Task
```

## Feature (AUTOBU)

- A capability or well-defined set of functionality that delivers business value.
- Indicates **code-level changes** against the product (product work).
- Can include additions or changes to existing functionality.
- Can span multiple teams and multiple releases.
- All contributing POs should be actively engaged in elaborating and validating
  goal definition and acceptance criteria.
- Hierarchy: Outcome -> Feature -> Epic -> Story/Bug/Weakness/Vulnerability/Task

## Initiative (AUTOBU)

- A larger product/portfolio goal or business priority broken into achievable,
  incremental deliveries as goal-based Epics.
- Used for all **non-product work** (infrastructure/process).
- Can span multiple teams and multiple releases/milestones.
- All contributing POs should be actively engaged in elaborating and validating
  goal definition and acceptance criteria.
- Hierarchy: Outcome -> Initiative -> Epic -> Task

## Epic (VROOM)

- Goal-based, scoped for a **single milestone/release** (roughly 2-3 sprints, 3-9 stories).
- Groups bugs, stories, and tasks to show progress of a larger effort.
- Description and acceptance criteria describe scope and expected outcomes.
- Best approach: scope the Epic for delivery by a **single Feature Area/Team**.
- If an Epic needs multiple Feature Teams in "Assigned Team", it is probably too
  large or not well defined - break it down further.
- Area POs, Delivery Owners, and Team members actively engaged in elaborating and
  validating the goal definition and acceptance criteria.

## Key Rules

1. Features link down to Epics with product work (Stories, Bugs, etc.)
2. Initiatives link down to Epics with non-product work (Tasks)
3. Epics should be scoped to one release/milestone
4. Epics should be owned by a single team
5. Features and Initiatives can span multiple releases
