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

- **reminder** (2026-06-30, daily): **Container vulnerability remediation deadline (~Jul 1).** VHCL-005/007/009 delegated to Eitan/Matt, Ozan/Matt, Ryan Smith. Follow up on remediation status.
- **reminder** (2026-06-30, daily): **Hubert Stefanski transition to RHAS/PitCrew starts Jul 1.** Discuss remaining knowledge transfer and onboarding plan.
- **info** (2026-06-14, daily): PITCREW-291 is overdue (was target RHAS-0526). Still In Progress — may need escalation or re-targeting.
- **review** (2026-06-23, daily): Hubert's knowledge transfer plan was due ~Jun 17 — overdue. Follow up on status. Also: discuss transition timelines (from Jun 18 meeting).
- **reminder** (2026-07-01, daily): **Roddie Kieley 30-day checkpoint.** Day 30 today (started Jun 1). Biweekly 1:1 cadence active, but 30-day checkpoint conversation due.
- **info** (2026-07-01, daily): **Workday evaluations still open.** Juanje Ojeda and Eitan Raviv QC manager evaluations pending - user discussing with them today (Jul 1). Hubert transfer approval and Bella time/HR approvals also pending.
- **info** (2026-06-24, daily): VROOM-42116 CDN path MR #149 submitted by Matt Goldman — monitor for merge. LP total tasks now 18 (was 16, +2 new compose tickets).
