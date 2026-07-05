---
last_accessed: 2026-07-05
access_count: 7
created: 2026-06-18
---

# Concepts

Generalized knowledge, patterns, and lessons learned from project work.

## Agent design

- [Stateful process-oriented agents](stateful-process-oriented-agents.md) — Juanje Ojeda's agent-forge design principles: identity/character, progressive disclosure, 4-store memory, skill design, tool design, permissions as design. Read when building or reviewing agents.
- [Agent chaining by hook](agent-chaining-by-hook.md) — embedding agent triggers inside other agents' procedures (step 8b pattern). Composable, independently testable. Read when integrating agents into existing workflows.
- [Accumulation mechanism](accumulation-mechanism.md) — frequent captures -> accumulation file -> periodic synthesis. Includes computed store separation variant. Read when designing report agents with periodic rollups.

## LLM operational patterns

- [Context compaction data drift](context-compaction-data-drift.md) — context window summarization introduces plausible but wrong data (rounded numbers, merged results, idempotent edit traps). Mitigation: re-query sources after compaction, check git state before re-applying edits. Read when working with long conversations or post-compaction.

## Assessment and evaluation

- [Self-input integration](self-input-integration.md) — auto-generated reports miss work without system traces (mentoring, cost optimization, AI tooling). Member self-input is essential for complete coverage. Read when generating QC or evaluation reports.
- [Multi-source framework synthesis](multi-source-framework-synthesis.md) — combining IC progression matrix + JLF + competency proficiency + career architecture produces richer assessments than any single source. Read when doing talent assessments or development feedback.
- [Career aspirations grounding](career-aspirations-grounding.md) — ground career aspiration responses in evidence from recent work, not generic advice. Read when preparing career conversation responses or 1:1 development discussions.

## Release engineering

- [Three-tier progressive criteria](three-tier-progressive-criteria.md) — release milestones as strict supersets (Monthly subset TP subset GA), with binary pass/fail conditions. Prevents disconnected GA criteria. Read when designing release criteria for multi-milestone products.

## Google Workspace patterns

- [Google Docs as rendering proxy](google-docs-rendering-proxy.md) — upload HTML with mimeType in request body to convert to native Docs format. Enables permanent-URL live dashboards. Key: mimeType in `--json`, not `--params`. Read when uploading HTML reports to Drive or troubleshooting conversion.

## Process patterns

- [Cross-referencing Slack vs documentation](cross-referencing-slack-vs-docs.md) — comparing observed behavior (Slack) against documented processes reveals structural gaps invisible from either source alone
- [Confluence API patterns](confluence-api-patterns.md) — CQL search, page tree traversal, cross-space queries using .netrc basic auth
