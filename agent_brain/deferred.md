---
created: YYYY-MM-DD
---

# Deferred queue

Communication channel from autonomous cycles to the user. Queue semantics:
write → present at session start → act → remove.

Entry format: `- **type** (YYYY-MM-DD, source): description.`
Types: `reminder`, `decision`, `info`, `review`.
Sources: `daily`, `weekly`, `monthly`, `user`.

---

- **reminder** (2026-06-28, daily): **URGENT — Atlassian API token "Avi2" expired yesterday (Jun 27).** Jira CLI, Confluence API, and any Atlassian-dependent skills will fail until rotated. Rotate immediately.
- **reminder** (2026-06-28, daily): **CAT starts tomorrow (Jun 29-30).** RHIVOS 2.0-Core CAT content deadline was ~Jun 26. Verify content is on CDN/ET. RC3 CTC at 93% (3 tickets remaining).
- **info** (2026-06-14, daily): PITCREW-291 is overdue (was target RHAS-0526). Still In Progress — may need escalation or re-targeting.
- **review** (2026-06-23, daily): Hubert's knowledge transfer plan was due ~Jun 17 — overdue. Follow up on status. Also: discuss transition timelines (from Jun 18 meeting).
- **info** (2026-06-24, daily): VROOM-42116 CDN path MR #149 submitted by Matt Goldman — monitor for merge. LP total tasks now 18 (was 16, +2 new compose tickets).
