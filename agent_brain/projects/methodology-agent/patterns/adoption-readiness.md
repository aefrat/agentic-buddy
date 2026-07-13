---
last_accessed: 2026-07-13
access_count: 2
created: 2026-06-29
---

# Adoption Readiness

Tasks and workflows assessed for broader team or program adoption.
Updated during weekly/monthly synthesis based on accumulated evidence
from ai-strengths.md and anti-patterns.md.

## Readiness levels

- **Ready:** proven autonomous or reliably assisted, low anti-pattern
  rate, can be documented as a replicable process
- **Promising:** works well in current setup but needs guardrails,
  training, or adaptation for others
- **Not ready:** too many anti-patterns, requires deep domain context,
  or depends on personal workflow integration
- **Not applicable:** inherently human-only, no AI acceleration path

Format per entry:
```
## [Task or workflow name]

**Domain:** [domain]
**Current category:** [autonomous|assisted|enhanced]
**Readiness:** [ready|promising|not-ready|not-applicable]
**Evidence period:** [date range]
**Tasks analyzed:** N
**Success rate:** [from computed stats]
**Key finding:** [1-2 sentences]
**Recommended approach for team:** [how to introduce this]
**Prerequisites:** [what the team needs before adopting]
```

---

## Multi-Source Status Reporting

**Domain:** reporting
**Current category:** autonomous
**Readiness:** ready
**Evidence period:** Jun 30 - Jul 12, 2026
**Tasks analyzed:** 4
**Success rate:** 4/4 autonomous, 0 anti-patterns in domain
**Key finding:** Parallel data gathering from Slack, Jira, and email into synthesized status reports runs reliably without corrections. Pattern: fan-out queries, collect, synthesize, format.
**Recommended approach for team:** Start with a single-source report (e.g., Jira-only weekly status). Validate output for two weeks. Add sources incrementally.
**Prerequisites:** Structured data sources (Jira project, Slack channels, email filters). Agent framework or cron scheduling for autonomous runs.

## Communication Drafting

**Domain:** communication
**Current category:** assisted
**Readiness:** promising
**Evidence period:** Jun 30 - Jul 13, 2026
**Tasks analyzed:** 3
**Success rate:** 3/3 required human review; output quality consistently acceptable as starting point
**Key finding:** AI produces competent first drafts for team communications, but messages involving personnel changes, feedback, or organizational politics consistently require human review and editing. This is inherent to the domain, not a limitation to overcome.
**Recommended approach for team:** Use AI for first draft and evidence gathering. Always review before sending. Frame as "draft accelerator" not "auto-sender."
**Prerequisites:** Clear communication guidelines. Human reviewer with relationship context.

## People-Management Preparation

**Domain:** people-management
**Current category:** assisted
**Readiness:** promising
**Evidence period:** Jul 13, 2026
**Tasks analyzed:** 2
**Success rate:** 2/2 preparation materials used directly in 1:1 conversations
**Key finding:** AI synthesizes career docs, development briefs, and progression frameworks into structured conversation guides and gap analyses. The human conducts the 1:1 (human-only), but prepared conversations produce better outcomes (e.g., organic role creation from structured retention discussion). AI enhances the input to human-only tasks.
**Recommended approach for team:** Build structured career data per person (development brief, career aspirations, framework positioning). Use AI to synthesize before 1:1s. Human drives the conversation.
**Prerequisites:** Structured talent architecture files (progression matrices, competency models, individual development data). Regular career data collection (QC self-input, 1:1 notes).

