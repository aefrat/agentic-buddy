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

- **reminder** (2026-07-12, weekly): **Hubert transition day 12, KT plan still overdue.** Was due ~Jun 17. CloudFront migration timeline needed (Hubert is the fork maintainer). Jeff Ligon scrum master handoff not formally announced.
- **reminder** (2026-07-12, weekly): **Roderick 30-day checkpoint 12 days overdue.** Day 41 (started Jun 1). SPSE development profile ready at `talent-architecture/active/roderick.kieley/` - use as conversation framework.
- **reminder** (2026-07-12, weekly): **Workday QC manager evaluations pending.** Juanje, Eitan, and remaining team members. QC deadline July 10 may have passed for some.
- **reminder** (2026-07-13, daily): **Atlassian API token expires Jul 19.** Renew before expiry or Jira queries from manager report and skills will break.
- **reminder** (2026-07-13, daily): **Kanitha retention action items this week:** (1) Jamie sync about opportunities/mentorship, (2) Ozan distribution offloading discussion, (3) begin absorbing TPO/operational tasks personally.
- **review** (2026-07-02, daily): **RHAS QE deliverables draft v1.0 need review.** Test Strategy + Release Criteria HTMLs on Drive and emailed. Review before broader sharing. OCP QE outreach not initiated.
- **info** (2026-06-14, daily): PITCREW-291 overdue (was target RHAS-0526). Still In Progress. One month in deferred - escalate or re-target.
