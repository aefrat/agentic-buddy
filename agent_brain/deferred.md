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

- **reminder** (2026-07-21, daily): **PDR Talent Calibration TOMORROW Thu Jul 23, 7-9:05am CDT (Jaime Flynn, 2 hours).** Need What/How ratings ready for all directs. Action plan at `talent-architecture/active/talent-cycle-2026H2/`.
- **reminder** (2026-07-21, daily): **Aman Vishwakarma onboarding week 1.** Started Jul 18. Still need: badge + laptop, ask Christine (OOO until Jul 27) about SP focal from RHELDST and SP buddy. Key for Kanitha distribution offloading.
- **reminder** (2026-07-21, daily): **Meital Arki follow-up** - meeting was scheduled Jul 20. Check outcome re: Jan Onderka move to ATC. Critical for LP and distribution work, and Kanitha retention (Ozan conversation dependency).
- **reminder** (2026-07-21, daily): **Hubert Stefanski transition day 21 (started Jul 1), KT plan still overdue.** CloudFront migration timeline needed (Hubert is fork maintainer). Jeff Ligon scrum master handoff not formally announced.
- **reminder** (2026-07-21, daily): **Roderick 30-day checkpoint 21 days overdue.** Day 51 (started Jun 1). PITCREW-294 due Jul 28, Roderick PTO Jul 27-Aug 3 - wrap up before leave. SPSE development profile at `talent-architecture/active/roderick.kieley/`.
- **reminder** (2026-07-21, daily): **Kanitha retention - remaining action items:** (1) Ozan distribution offload discussion (blocked by Meital/Jan outcome), (2) absorb TPO personally. Christine connection - her PTO ends Jul 21 (today), reach out this week. RoG proposal needs Petr + Rachel input. Mentor finalization due ~Jul 28.
- **reminder** (2026-07-21, daily): **CloudShell home directory deletion Jul 24** - 3 days. Inform team if anyone uses eu-north-1.
- **reminder** (2026-07-21, daily): **Workday QC manager evaluations pending.** QC deadline July 10 has passed (11 days overdue). Still need to submit.
- **review** (2026-07-21, daily): **RHAS QE deliverables draft v1.0 need review (19 days old).** Test Strategy + Release Criteria HTMLs on Drive and emailed. Review before broader sharing. OCP QE outreach not initiated.
- **info** (2026-07-21, daily): PITCREW-291 overdue (was target RHAS-0526). Still In Progress. 37 days in deferred - escalate or re-target.
