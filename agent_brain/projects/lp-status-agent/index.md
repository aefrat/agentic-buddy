---
last_accessed: 2026-06-23
access_count: 1
created: 2026-06-23
---

# LP Status Agent — Knowledge Base

Content map for the RHIVOS QC Layered Product daily status report agent.

## Stores

- `active/` — Most recent run's HTML report and snapshot JSON. **Overwritten each run.** Read when comparing against previous output (disconfirmation gate).
- `history/` — Past reports and snapshots, dated. **Immutable after save.** Read when answering "what did yesterday's report say?" or computing trends.

## Reference (external)

- `user/rhivos-qc-lp-status-report.html` — CSS template and section layout. **Developer-maintained.** Read when generating the HTML report.
- `agent_brain/projects/rhivos-qc-layered-product.md` — Project file: architecture, people, ticket list, Kanitha activity log. **Updated each run** with latest ticket statuses and Slack activity.

## Skill

- [rhivos-qc-lp-status.md](../../skills/rhivos-qc-lp-status.md) — The skill procedure.
