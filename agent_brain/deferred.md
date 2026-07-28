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

- **reminder** (2026-07-28, daily): **PDR Talent Calibration happened Jul 23 (5 days ago).** Outcome still unknown. Check and document results. Action plan at `talent-architecture/active/talent-cycle-2026H2/`.
- **reminder** (2026-07-28, daily): **Aman Vishwakarma onboarding day 8 Tue Jul 29 (started Jul 18).** Still need: badge + laptop. Christine back from PTO (ended Jul 21) - coordinate on SP focal and buddy. Key for Kanitha distribution offloading.
- **reminder** (2026-07-28, daily): **Meital Arki follow-up** - meeting was Jul 20, now 8 days ago. Check outcome re: Jan Onderka move to ATC. Critical for LP and distribution work, and Kanitha retention (Ozan conversation dependency). Growing stale.
- **reminder** (2026-07-28, daily): **Hubert Stefanski transition day 28 (started Jul 1), KT plan still overdue.** CloudFront migration timeline needed (Hubert is fork maintainer). Jeff Ligon scrum master handoff not formally announced.
- **reminder** (2026-07-28, daily): **Roderick on PTO Jul 27-Aug 3.** 30-day checkpoint now 28 days overdue. Day 58 (started Jun 1). PITCREW-294 was due Jul 28 - Roderick on PTO, could not deliver. Needs timeline discussion when he returns Aug 4. SPSE development profile at `talent-architecture/active/roderick.kieley/`.
- **reminder** (2026-07-28, daily): **Kanitha retention - remaining action items:** (1) Ozan distribution offload discussion (blocked by Meital/Jan outcome), (2) absorb TPO personally. RoG proposal needs Petr + Rachel input. **Mentor finalization was due ~Jul 28 - check if done.**
- **reminder** (2026-07-28, daily): **Workday QC manager evaluations pending.** QC deadline July 10 has passed (18 days overdue). Still need to submit.
- **reminder** (2026-07-28, daily): **RHAS testing meeting rescheduled to Aug 3rd** (was this week, moved due to RH company meeting and multiple conflicts). Source: #team-pitcrew-automotive Slack.
- **review** (2026-07-28, daily): **RHAS QE deliverables draft v1.0 need review (26 days old).** Test Strategy + Release Criteria HTMLs on Drive and emailed. Review before broader sharing. OCP QE outreach not initiated. RH release terminology gap analysis (Jul 26) identified 9 TP + 9 GA gaps beyond current criteria.
- **info** (2026-07-28, daily): PITCREW-291 overdue (was target RHAS-0526). Still In Progress. 44 days in deferred - escalate or re-target.
- **info** (2026-07-28, daily): **Jumpstarter hardware regression** - new ABL causes locked Snapdragon 8650 devices to become completely unbootable. Fastboot detection failures on boards 6 and 3. Reported by pagranat in #forum-jumpstarter.
- **info** (2026-07-28, daily): **1:1 action items stale (29 days).** `user/1on1-action-items.md` last processed Jun 29. Multiple items reference expired QC deadline (Jul 10). Refresh at next 1:1 processing.
