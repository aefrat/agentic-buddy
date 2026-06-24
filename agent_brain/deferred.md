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

- **info** (2026-06-14, daily): PITCREW-291 is overdue (was target RHAS-0526). Still In Progress — may need escalation or re-targeting.
- **reminder** (2026-06-21, daily): Atlassian API token "Avi2" expires Jun 27. Needs rotation before then.
- **reminder** (2026-06-24, daily): CAT content deadline ~Jun 26 (2 days). RHIVOS 2.0-Core CAT Jun 29-30. Confirm content is on CDN/ET track.
- **review** (2026-06-23, daily): Hubert's knowledge transfer plan was due ~Jun 17 — overdue. Follow up on status. Also: discuss transition timelines (from Jun 18 meeting).
- **info** (2026-06-24, daily): VROOM-42116 CDN path MR #149 submitted by Matt Goldman — monitor for merge. LP total tasks now 18 (was 16, +2 new compose tickets).
