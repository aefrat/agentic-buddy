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

- **reminder** (2026-07-20, daily): **Aman Vishwakarma onboarding day 3.** Meeting with Aman + Kanitha was Jul 20. Welcome message sent. Still need: badge + laptop, ask Christine (OOO until Jul 27) about SP focal from RHELDST and SP buddy. Key for Kanitha distribution offloading.
- **reminder** (2026-07-20, daily): **Meital Arki meeting was scheduled Jul 20** - follow up on Jan Onderka move to ATC. Critical for LP and distribution work, and Kanitha retention (Ozan conversation dependency).
- **reminder** (2026-07-20, daily): **PDR Talent Calibration Thu Jul 23, 7-9:05am CDT (Jaime Flynn, 2 hours).** Need What/How ratings ready for all directs. Action plan at `talent-architecture/active/talent-cycle-2026H2/`.
- **reminder** (2026-07-20, daily): **Hubert Stefanski transition day 20 (started Jul 1), KT plan still overdue.** CloudFront migration timeline needed (Hubert is fork maintainer). Jeff Ligon scrum master handoff not formally announced.
- **reminder** (2026-07-20, daily): **Roderick 30-day checkpoint 20 days overdue.** Day 50 (started Jun 1). PITCREW-294 due Jul 28, Roderick PTO Jul 27-Aug 3 - needs wrap-up before leave. Use SPSE development profile at `talent-architecture/active/roderick.kieley/`.
- **reminder** (2026-07-20, daily): **Kanitha retention - remaining action items:** (1) Ozan distribution offload discussion (blocked by Meital/Jan outcome), (2) absorb TPO personally. Christine connection after Jul 21 PTO. RoG proposal needs Petr + Rachel input. Mentor finalization due ~Jul 28.
- **reminder** (2026-07-20, daily): **CloudShell home directory deletion Jul 24** - inform team if anyone uses eu-north-1.
- **reminder** (2026-07-20, daily): **Workday QC manager evaluations pending.** QC deadline July 10 has passed. Still need to submit.
- **review** (2026-07-20, daily): **RHAS QE deliverables draft v1.0 need review (18 days old).** Test Strategy + Release Criteria HTMLs on Drive and emailed. Review before broader sharing. OCP QE outreach not initiated.
- **info** (2026-07-20, daily): PITCREW-291 overdue (was target RHAS-0526). Still In Progress. 36 days in deferred - escalate or re-target.
