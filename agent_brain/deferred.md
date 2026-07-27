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

- **reminder** (2026-07-27, daily): **PDR Talent Calibration happened Jul 23.** Check outcome and document results. Action plan at `talent-architecture/active/talent-cycle-2026H2/`.
- **reminder** (2026-07-27, daily): **Aman Vishwakarma onboarding day 7 Monday (started Jul 18).** Still need: badge + laptop. Christine back from PTO (ended Jul 21) - ask about SP focal from RHELDST and SP buddy. Key for Kanitha distribution offloading.
- **reminder** (2026-07-27, daily): **Meital Arki follow-up** - meeting was Jul 20, now 7 days ago. Check outcome re: Jan Onderka move to ATC. Critical for LP and distribution work, and Kanitha retention (Ozan conversation dependency).
- **reminder** (2026-07-27, daily): **Hubert Stefanski transition day 27 (started Jul 1), KT plan still overdue.** CloudFront migration timeline needed (Hubert is fork maintainer). Jeff Ligon scrum master handoff not formally announced.
- **reminder** (2026-07-27, daily): **Roderick on PTO Jul 27-Aug 3.** 30-day checkpoint now 27 days overdue. Day 57 (started Jun 1). PITCREW-294 due Jul 28 (tomorrow) - Roderick is on PTO, cannot deliver. Needs timeline discussion when he returns Aug 4. SPSE development profile at `talent-architecture/active/roderick.kieley/`.
- **reminder** (2026-07-27, daily): **Kanitha retention - remaining action items:** (1) Ozan distribution offload discussion (blocked by Meital/Jan outcome), (2) absorb TPO personally. RoG proposal needs Petr + Rachel input. **Mentor finalization due ~Jul 28 (tomorrow).**
- **reminder** (2026-07-27, daily): **Workday QC manager evaluations pending.** QC deadline July 10 has passed (17 days overdue). Still need to submit.
- **review** (2026-07-27, daily): **RHAS QE deliverables draft v1.0 need review (25 days old).** Test Strategy + Release Criteria HTMLs on Drive and emailed. Review before broader sharing. OCP QE outreach not initiated. New: RH release terminology gap analysis (Jul 26) identified 9 TP + 9 GA gaps beyond current criteria.
- **info** (2026-07-27, daily): PITCREW-291 overdue (was target RHAS-0526). Still In Progress. 43 days in deferred - escalate or re-target.
