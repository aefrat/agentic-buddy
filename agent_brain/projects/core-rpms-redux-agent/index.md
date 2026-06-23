---
last_accessed: 2026-06-23
access_count: 0
created: 2026-06-23
---

# Core RPMs Redux Report Agent — Knowledge Base

Content map for the Core RPMs Redux (VROOM-31017) status report agent.

## Stores

- `reference/` — Data source documentation (Jira queries, Slack channels, Google Doc IDs, auth). **Read-only.** Read when generating a report or troubleshooting a data source.
- `active/` — Most recent run's HTML report and snapshot JSON. **Overwritten each run.** Read when comparing against previous output (diff computation, disconfirmation gate).
- `history/` — Past reports and snapshots, dated. **Immutable after save.** Read when computing trends or answering "what did the last report say?"
- `patterns/` — Strategic context cache and learned patterns. **Consolidation only.** Reserved for future use.

## Reference (external)

- `agent_brain/projects/core-rpms-redux.md` — Project file: goal, people, tickets, Slack trail, key artifacts. **Updated each run** with latest ticket statuses.

## Skill

- [core-rpms-redux-status.md](../../skills/core-rpms-redux-status.md) — The skill procedure.
