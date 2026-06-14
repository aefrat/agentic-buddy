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

- **reminder** (2026-06-14, daily): RC3 go/no-go meeting is Monday 2026-06-16. Depends on RHEL CVE fix, Francisco's blocker tickets, and NXP confirmation. Check status before the meeting.
- **reminder** (2026-06-14, daily): Roderick Kieley 1:1 still not scheduled — he started June 1, now 2 weeks in. Schedule it this week.
- **info** (2026-06-14, daily): PITCREW-291 is overdue (was target RHAS-0526). Still In Progress — may need escalation or re-targeting.
