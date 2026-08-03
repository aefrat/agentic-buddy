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

- **reminder** (2026-08-03, daily): **Roderick Kieley returns from PTO tomorrow (Aug 4).** Day 65 of onboarding (started Jun 1). 30-day checkpoint 34 days overdue. PITCREW-294 was due Jul 28, could not deliver during PTO. Needs timeline discussion first day back. SPSE development profile at `talent-architecture/active/roderick.kieley/`.
- **reminder** (2026-08-03, daily): **RHAS testing meeting was today (Aug 3).** Check outcome - was rescheduled from earlier due to RH company meeting.
- **reminder** (2026-08-03, daily): **Release blocker PoC - pipeline partially working.** lint/build stages green after Podman executor fix + 56 ruff lint fixes. run-daily blocked on quay.io auth (repo private). Decision needed: make repo public vs configure DOCKER_AUTH_CONFIG. Shared runners (`itup-alm-x86`) available as alternative to local laptop runner.
- **reminder** (2026-08-03, daily): **PDR Talent Calibration happened Jul 23 (11 days ago).** Outcome still unknown. Check and document results. Action plan at `talent-architecture/active/talent-cycle-2026H2/`.
- **reminder** (2026-08-03, daily): **Workday QC manager evaluations 24 days overdue** (deadline was Jul 10). 9/10 submissions done, evaluations still pending.
- **reminder** (2026-08-03, daily): **Meital Arki follow-up** - meeting was Jul 20, now 14 days ago. Check outcome re: Jan Onderka move to ATC. Critical for LP and distribution work, and Kanitha retention (Ozan conversation dependency). Growing stale.
- **reminder** (2026-08-03, daily): **Kanitha mentor finalization was due ~Jul 28.** Check status (~6 days overdue). Remaining retention items: Ozan distribution offload discussion (blocked by Meital/Jan outcome), absorb TPO personally. OSCI confirmed willingness to onboard RHIVOS (Jul 30) - follow up mid-Aug with Adam Samalik tracking ticket.
- **reminder** (2026-08-03, daily): **Hubert Stefanski transition day 34 (started Jul 1).** KT plan still overdue. CloudFront migration timeline needed (Hubert is fork maintainer). Jeff Ligon scrum master handoff not formally announced.
- **reminder** (2026-08-03, daily): **Aman Vishwakarma onboarding day 17 (started Jul 18).** Still need: badge + laptop. Christine back from PTO (ended Jul 21) - coordinate on SP focal and buddy. Key for Kanitha distribution offloading.
- **info** (2026-08-03, daily): **1:1 action items stale (35 days).** `user/1on1-action-items.md` last processed Jun 29. Multiple items reference expired QC deadline (Jul 10). Refresh at next 1:1 processing.
- **review** (2026-08-03, daily): **RHAS QE deliverables draft v1.0 need review (32 days old).** Test Strategy + Release Criteria HTMLs on Drive and emailed. Review before broader sharing. OCP QE outreach not initiated. RH release terminology gap analysis (Jul 26) identified 9 TP + 9 GA gaps beyond current criteria.
- **info** (2026-08-03, user): **Paul Wallrabe replied to AutoSD/Jumpstarter thread.** Key new info: Jumpstarter endpoint is public (no Testing Farm needed), lab not at capacity (resource starvation not a concern), start with any board (TI unused), strong anti-pool-sharding stance. Topic added to ATC open sync this week. Full context at `agent_brain/projects/autosd-jumpstarter-hw-testing.md`.
