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

- **reminder** (2026-07-19, daily): **Aman Vishwakarma onboarding - day 2 (started Jul 18).** Christine Freitas OOO until Jul 27 - you are primary onboarding contact. Aman needs badge and laptop. Also key for Kanitha distribution offloading.
- **reminder** (2026-07-19, daily): **Hubert Stefanski transition day 19 (started Jul 1), KT plan still overdue.** Was due ~Jun 17. CloudFront migration timeline needed (Hubert is fork maintainer). Jeff Ligon scrum master handoff not formally announced.
- **reminder** (2026-07-19, daily): **Roderick 30-day checkpoint 19 days overdue.** Day 49 (started Jun 1). SPSE development profile ready at `talent-architecture/active/roderick.kieley/` - use as conversation framework. PITCREW-294 due Jul 28, Roderick PTO Jul 27-Aug 3 - needs wrap-up before leave.
- **reminder** (2026-07-19, daily): **Kanitha retention - remaining action items:** (1) Ozan distribution offload discussion, (2) absorb TPO personally. Jamie sync done Jul 15 - no objections. Christine connection after Jul 21 PTO. RoG proposal needs Petr + Rachel input.
- **reminder** (2026-07-19, daily): **Workday QC manager evaluations pending.** Juanje, Eitan, and remaining team members. QC deadline July 10 may have passed.
- **review** (2026-07-02, daily): **RHAS QE deliverables draft v1.0 need review (17 days old).** Test Strategy + Release Criteria HTMLs on Drive and emailed. Review before broader sharing. OCP QE outreach not initiated.
- **info** (2026-06-14, daily): PITCREW-291 overdue (was target RHAS-0526). Still In Progress. 35 days in deferred - escalate or re-target.
