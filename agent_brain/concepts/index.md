---
last_accessed: 2026-06-28
access_count: 4
created: 2026-06-18
---

# Concepts

Generalized knowledge, patterns, and lessons learned from project work.

## Agent design

- [Stateful process-oriented agents](stateful-process-oriented-agents.md) — Juanje Ojeda's agent-forge design principles: identity/character, progressive disclosure, 4-store memory, skill design, tool design, permissions as design. Read when building or reviewing agents.

## LLM operational patterns

- [Context compaction data drift](context-compaction-data-drift.md) — context window summarization introduces plausible but wrong data (rounded numbers, merged results, idempotent edit traps). Mitigation: re-query sources after compaction, check git state before re-applying edits. Read when working with long conversations or post-compaction.

## Process patterns

- [Cross-referencing Slack vs documentation](cross-referencing-slack-vs-docs.md) — comparing observed behavior (Slack) against documented processes reveals structural gaps invisible from either source alone
- [Confluence API patterns](confluence-api-patterns.md) — CQL search, page tree traversal, cross-space queries using .netrc basic auth
