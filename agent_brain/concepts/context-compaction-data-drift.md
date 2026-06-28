---
last_accessed: 2026-06-28
access_count: 1
created: 2026-06-28
---

# Context compaction data drift

When an LLM conversation is compacted (context window summarization), the
summary can deviate from actual data in ways that are plausible but wrong.
Numbers get rounded, intermediate and final results get mixed, and
synthesized data replaces actual values.

## Pattern

1. Agent collects precise data from external sources (APIs, tools).
2. Context window fills; the system compacts prior messages into a summary.
3. The summary introduces drift: approximate numbers, merged results,
   reordered facts.
4. Agent continues working from the summary as if it were the original data.
5. Output contains plausible but incorrect information.

## Variants

**Data drift:** Summary rounds or synthesizes numbers. E.g., "22 children,
15 Closed" becomes "19 children, 9 Closed" after compaction. The agent
doesn't notice because the summary is internally consistent.

**Idempotency trap:** Summary lists files/items as "pending" that were
already committed before compaction. Edit tool accepts no-op edits silently
(old_string matches current content), so the agent believes it made changes
when nothing happened. Mitigation: check `git log` before re-applying edits
after compaction.

## Mitigation

- After compaction, verify data from actual task notifications or tool
  results, not the conversation summary.
- For critical data (counts, statuses, file states), re-query the source
  rather than trusting compacted context.
- When editing files after compaction, check `git log`/`git diff` to see
  what's already been committed.

## Source

- [Log 2026-06-23](../../logs/2026-06-23.md) — Core RPMs Redux report data
  diverged after compaction (22→19 children, 15→9 Closed).
- [Log 2026-06-24](../../logs/2026-06-24.md) — Idempotency trap: 10 of 12
  files already committed, edit tool silently no-oped.
