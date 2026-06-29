---
last_accessed: 2026-06-29
access_count: 0
created: 2026-06-29
---

# AI Task Taxonomy

Four-level classification for AI involvement in engineering management
tasks. Applied during daily capture to each observed task.

## Categories

### Autonomous

AI performs the task end-to-end. Human reviews the output for correctness
but rarely changes substance. The AI could run unattended and produce
acceptable output.

**Signals:** cron-triggered, output used as-is, review time under 2
minutes, no substantive edits.

**Sub-types:**
- Data collection and formatting (API queries, Jira fetches, Slack scans)
- Report generation from structured data (LP status, daily manager report)
- Template-based output (HTML from collected data)
- Routine notifications and summaries
- Log processing and consolidation

### Assisted

AI produces a first draft or analysis. Human reviews, restructures, adds
judgment, or rewrites portions. The AI accelerates the work but does not
complete it.

**Signals:** human edited more than 20% of content, multiple iteration
cycles, human added context AI did not have, structural changes to AI
output.

**Sub-types:**
- Report drafting with human narrative editing (QC evaluations)
- Analysis with human judgment overlay (disconfirmation gates)
- Data synthesis requiring domain knowledge the AI lacks
- Communication drafting (emails, responses, feedback)
- Document authoring (plans, proposals, strategy docs)

### Enhanced

Human drives the work. AI assists with specific sub-tasks: lookups,
formatting, calculations, search. The human would do the task without AI
but slower or with more effort.

**Signals:** human initiates and structures, AI handles mechanical parts,
human makes all judgment calls, AI contribution is speed not substance.

**Sub-types:**
- Research acceleration (Slack search, Confluence lookup)
- Formatting and styling (HTML, table generation)
- Data retrieval (Jira queries, Git history)
- Cross-referencing (comparing sources, finding connections)
- Template scaffolding (starting structures for human completion)

### Human-Only

The task requires human judgment, relationships, emotional intelligence,
or real-time presence that AI cannot provide.

**Signals:** 1:1 conversations, trust-building, conflict resolution,
political navigation, in-person coordination, ethical judgment.

**Sub-types:**
- Interpersonal (1:1s, career conversations, conflict mediation)
- Strategic judgment (team composition, priority calls, risk acceptance)
- Relationship management (stakeholder alignment, trust building)
- Presence-required (meetings, demos, live coordination)
- Emotional intelligence (morale sensing, team dynamics reading)

## Classification rules

1. Classify the **task**, not the session. One session may contain tasks
   across multiple categories.
2. When uncertain, classify conservatively (toward more human involvement).
   It is better to undercount AI autonomy than overcount it.
3. A task that is autonomous today may have been assisted last month.
   Track the trajectory, not just the current state.
4. Anti-patterns are not a category. They are observations about tasks
   where the AI output was wrong or required correction beyond normal
   iteration. A task can be "assisted" and also have an anti-pattern.
5. Confidence levels: `high` if clear from evidence (explicit user
   feedback, cron run, output used unchanged), `medium` if inferred from
   log context (no explicit signal either way).
