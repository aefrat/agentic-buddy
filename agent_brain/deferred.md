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

- **info** (2026-06-29, daily): **Jira API token "Avi2" - status unclear.** Active Context says expired Jun 27, but `jira me` and `jira issue view` both work as of Jun 29. Token may have been auto-rotated or expiration warning was premature. Verify and update Active Context.
- **reminder** (2026-06-29, daily): **CAT Day 2 today (Jun 30).** RHIVOS 2.0-Core CAT wraps up. RC3 CTC at 93% (3 tickets remaining).
- **info** (2026-06-14, daily): PITCREW-291 is overdue (was target RHAS-0526). Still In Progress — may need escalation or re-targeting.
- **review** (2026-06-23, daily): Hubert's knowledge transfer plan was due ~Jun 17 — overdue. Follow up on status. Also: discuss transition timelines (from Jun 18 meeting).
- **info** (2026-06-24, daily): VROOM-42116 CDN path MR #149 submitted by Matt Goldman — monitor for merge. LP total tasks now 18 (was 16, +2 new compose tickets).
