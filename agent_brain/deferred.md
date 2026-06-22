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

- **reminder** (2026-06-14, daily): Roderick Kieley 1:1 still not scheduled — he started June 1, now 17 days in. Schedule it soon.
- **info** (2026-06-14, daily): PITCREW-291 is overdue (was target RHAS-0526). Still In Progress — may need escalation or re-targeting.
- **reminder** (2026-06-18, daily): ASIL CTC starts Friday June 19 (weekend CTC for 2.0 ASIL Release + Kernel Debug for 8650). Confirm RC3 build is ready.
- **reminder** (2026-06-18, daily): Starting Thursday June 19, Z-stream becomes the right target for kernel builds (per Petr Sabata). This reduces the tagging workflow mismatch for ~1 year.
- **reminder** (2026-06-21, daily): Atlassian API token "Avi2" expires Jun 27. Needs rotation this week.
- **info** (2026-06-21, daily): BRQ ML01B power branch down since Friday evening. Fix ETA: Monday (local hands). Affects single-PSU devices on 3 PDUs.
