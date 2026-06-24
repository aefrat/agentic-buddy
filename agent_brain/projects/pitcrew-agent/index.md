---
last_accessed: 2026-06-24
access_count: 1
created: 2026-06-23
---

# PitCrew Report Agent — Knowledge Base

Content map for the PitCrew/RHAS status report agent's memory stores. Read this index first, then navigate to the relevant store.

## Stores

- `reference/` — Report mode definitions, data source documentation, AI prompt templates. **Read-only.** Read when generating a report or troubleshooting a data source.
- `active/` — Most recent run's HTML report and snapshot JSON. **Overwritten each run.** Read when comparing against previous output (diff computation, disconfirmation gate).
- `history/` — Past reports and snapshots, dated by mode. **Immutable after save.** Read when computing trends or answering "what did last week's report say?"
- `patterns/` — Strategic context cache (refreshed monthly), learned patterns. **Consolidation only.** Read when building report context or grounding strategic alignment analysis.

## Reference (external)

- `user/reports/pitcrew-full-report-2026-06-01.html` — CSS template and section layout. **Developer-maintained.** Read when generating the HTML report (lines 7–95 for the full CSS block).

## Skill

- [pitcrew-weekly-report.md](../../skills/pitcrew-weekly-report.md) — The skill procedure.
