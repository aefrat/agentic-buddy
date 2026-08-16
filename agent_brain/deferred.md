---
created: YYYY-MM-DD
---

# Deferred queue

Communication channel from autonomous cycles to the user. Queue semantics:
write -> present at session start -> act -> remove.

Entry format: `- **type** (YYYY-MM-DD, source): description.`
Types: `reminder`, `decision`, `info`, `review`.
Sources: `daily`, `weekly`, `monthly`, `user`.

---

- **reminder** (2026-08-05, daily): **Roderick Kieley returned from PTO Aug 4.** Day 66 of onboarding (started Jun 1). 30-day checkpoint 36 days overdue. PITCREW-294 was due Jul 28, could not deliver during PTO. Timeline discussion needed (day 2 back). SPSE development profile at `talent-architecture/active/roderick.kieley/`.
- **reminder** (2026-08-05, daily): **Workday QC manager evaluations 26 days overdue** (deadline was Jul 10). 9/10 submissions done, evaluations still pending.
- **reminder** (2026-08-05, daily): **PDR Talent Calibration happened Jul 23 (13 days ago).** Outcome still unknown. Check and document results. Action plan at `talent-architecture/active/talent-cycle-2026H2/`.
- **reminder** (2026-08-05, daily): **Meital Arki follow-up** - meeting was Jul 20, now 16 days ago. Outcome re: Jan Onderka move to ATC unknown. Critical for LP, distribution work, and Kanitha retention (Ozan conversation dependency). Growing stale.
- **reminder** (2026-08-05, daily): **Kanitha mentor finalization was due ~Jul 28.** Check status (~8 days overdue). Remaining retention items: Ozan distribution offload discussion (blocked by Meital/Jan outcome), absorb TPO personally. OSCI confirmed willingness to onboard RHIVOS (Jul 30) - follow up mid-Aug with Adam Samalik tracking ticket (approaching window).
- **reminder** (2026-08-05, daily): **Hubert Stefanski transition day 36 (started Jul 1).** KT plan still overdue. CloudFront migration timeline needed (Hubert is fork maintainer). Jeff Ligon scrum master handoff not formally announced.
- **reminder** (2026-08-05, daily): **Aman Vishwakarma onboarding day 19 (started Jul 18).** Still need: badge + laptop. Christine back from PTO (ended Jul 21) - coordinate on SP focal and buddy. Key for Kanitha distribution offloading.
- **reminder** (2026-08-05, daily): **RHAS testing meeting was Aug 3.** Outcome unknown (2 days ago). Check what was discussed/decided.
- **reminder** (2026-08-05, daily): **Release blocker agent has cross-release ticket leakage bug.** VROOM-46538 appearing in all 3 release reports instead of just rhivos-2.0.z. 3-part fix proposed (synthesize.py scoping + agent.py pass-through + compute_stats.py exact match). Not yet implemented. Demo to Dana/team not yet scheduled.
- **info** (2026-08-05, daily): **1:1 action items stale (37 days).** `user/1on1-action-items.md` last processed Jun 29. Refresh at next 1:1 processing.
- **review** (2026-08-05, daily): **RHAS QE deliverables draft v1.0 need review (34 days old).** Test Strategy + Release Criteria HTMLs on Drive and emailed. Review before broader sharing. OCP QE outreach not initiated. RH release terminology gap analysis (Jul 26) identified 9 TP + 9 GA gaps beyond current criteria.
- **info** (2026-08-03, user): **Paul Wallrabe replied to AutoSD/Jumpstarter thread.** Key new info: Jumpstarter endpoint is public (no Testing Farm needed), lab not at capacity, start with any board (TI unused), strong anti-pool-sharding stance. Topic added to ATC open sync this week. Full context at `agent_brain/projects/autosd-jumpstarter-hw-testing.md`.
- **reminder** (2026-08-16, daily): **All Manager Meeting Aug 19** (Stef Walter's org), 17:00 Israel time. 3 days away.
- **reminder** (2026-08-16, daily): **Innovation Days review session Aug 20**, hackathon Sep 2.
- **reminder** (2026-08-16, daily): **Eitan Raviv 9-year anniversary Aug 21.** Acknowledge.
- **reminder** (2026-08-16, daily): **GitLab.cee upgrade downtime Aug 22.**
- **reminder** (2026-08-16, daily): **CY27 Capex requests deadline passed Aug 14.** Check if team submitted while on PTO.
- **reminder** (2026-08-16, daily): **Old RHIVOS-1/AutoSD-9 AMI removal decision needed.** Eitan + Juanje waiting for response.
- **reminder** (2026-08-16, daily): **AWS cost reduction findings ready.** HTML at `user/aws-cost-analysis.html`, Google Doc created. Coordinate with Eitan on response to Eliska's 20% reduction directive.
- **reminder** (2026-08-16, daily): **Lightwell EM screening started.** Stuart Corcoran (Chief of Staff) emailed Aug 14 that outreach from LW team leads expected soon. User's OOO auto-reply went to Stuart. Respond/prepare.
- **reminder** (2026-08-16, daily): **RHIVOS test cases gap.** Priyanka Verma flagged ~235 test cases missing from formal specs. Mandatory for QE release epics.
- **reminder** (2026-08-16, daily): **Install NetBird VPN by Aug 31.** Also: renew GitLab SSH key (expiring), Confluence Bot API token expires Sep 9.
- **reminder** (2026-08-16, daily): **ReportPortal v26.0.3 upgrade scheduling** - Roni/Daniel need input.
