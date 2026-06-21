---
last_accessed: 2026-06-21
access_count: 1
created: 2026-06-21
---

# Manager Report Agent — Knowledge Base

Content map for the manager report agent's memory stores. Read this index first, then navigate to the relevant store.

## Stores

- `reference/` — Report mode definitions, AI prompt templates, data source documentation. **Read-only.** Read when generating a report or troubleshooting a data source.
- `../qc-agent/team/` — Shared team roster with platform usernames, Slack channels, JQL queries, Google Docs. **Manager-maintained.** Read when collecting data or listing team members. Shared with the QC agent.
- `active/` — Most recent run's data snapshot and HTML. **Overwritten each run.** Read when comparing against previous output.
- `history/` — Past reports and data snapshots, dated by mode. **Immutable after save.** Read when computing trends or answering "what did last week's report say?"
- `computed/` — Script-derived statistics: rolling averages, week-over-week deltas, outlier flags. **Script-only, never LLM-written.** Read when grounding AI summaries with quantitative context.
- `patterns/` — Learned patterns: writing preferences, team activity baselines. **Consolidation only.** Read when tailoring report style to manager preferences.

## Project file

- [manager-report-agent.md](../manager-report-agent.md) — Architecture, plan, design decisions.

## Execution engine

- `/home/aefrat/claude/manager-report/generate_report.py` — the Python script that fetches all data and produces HTML. The agent orchestrates it; does not replicate its logic.
- `/home/aefrat/claude/manager-report/CLAUDE.md` — script-level documentation (team members, API notes, workflows).
