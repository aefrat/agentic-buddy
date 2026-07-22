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

- **reminder** (2026-07-22, daily): **PDR Talent Calibration TODAY Thu Jul 23, 7-9:05am CDT (Jaime Flynn, 2 hours).** Need What/How ratings ready for all directs. Action plan at `talent-architecture/active/talent-cycle-2026H2/`.
- **reminder** (2026-07-22, daily): **CloudShell home directory deletion Jul 24** - 2 days. Inform team if anyone uses eu-north-1.
- **reminder** (2026-07-22, daily): **Aman Vishwakarma onboarding day 5 (started Jul 18).** Still need: badge + laptop. Christine back from PTO (ended Jul 21) - ask about SP focal from RHELDST and SP buddy. Key for Kanitha distribution offloading.
- **reminder** (2026-07-22, daily): **Meital Arki follow-up** - meeting was Jul 20. Check outcome re: Jan Onderka move to ATC. Critical for LP and distribution work, and Kanitha retention (Ozan conversation dependency).
- **reminder** (2026-07-22, daily): **Hubert Stefanski transition day 22 (started Jul 1), KT plan still overdue.** CloudFront migration timeline needed (Hubert is fork maintainer). Jeff Ligon scrum master handoff not formally announced.
- **reminder** (2026-07-22, daily): **Roderick 30-day checkpoint 22 days overdue.** Day 52 (started Jun 1). PITCREW-294 due Jul 28 (6 days), Roderick PTO Jul 27-Aug 3 - wrap up before leave. SPSE development profile at `talent-architecture/active/roderick.kieley/`.
- **reminder** (2026-07-22, daily): **Kanitha retention - remaining action items:** (1) Ozan distribution offload discussion (blocked by Meital/Jan outcome), (2) absorb TPO personally. Christine back from PTO - connect this week. RoG proposal needs Petr + Rachel input. Mentor finalization due ~Jul 28.
- **reminder** (2026-07-22, daily): **Workday QC manager evaluations pending.** QC deadline July 10 has passed (12 days overdue). Still need to submit.
- **review** (2026-07-22, daily): **RHAS QE deliverables draft v1.0 need review (20 days old).** Test Strategy + Release Criteria HTMLs on Drive and emailed. Review before broader sharing. OCP QE outreach not initiated.
- **info** (2026-07-22, daily): PITCREW-291 overdue (was target RHAS-0526). Still In Progress. 38 days in deferred - escalate or re-target.
