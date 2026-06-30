---
last_accessed: 2026-06-30
access_count: 1
created: 2026-06-30
---

# Self-input integration for evaluation reports

Auto-generated reports from system sources (Jira, Slack, GitLab) provide a
strong baseline but systematically miss work that leaves no system trace:
mentoring, onboarding support, cost optimization, AI tooling adoption,
cross-team help, design thinking, conference presentations.

Team member self-authored narratives are the richest source for
accomplishments. They contain specific ticket numbers, demo dates,
cross-team coordination details, and the "how" narrative that system
data alone cannot surface.

## Pattern

1. Generate initial draft from system sources (Jira + Slack + GitLab).
2. Request member self-input (what they did + how they did it).
3. Compare section by section: identify gaps in auto-generated draft.
4. Rewrite to incorporate the member's framing and emphasis while
   preserving evidence from system sources.
5. The member's voice takes priority over pure data summarization.

## Evidence

- Juanje Q2 QC (2026-06-29): self-input surfaced CTC investigation
  agent, Pi extensions, Matt Goldman onboarding support, AAA Sprint 5
  demo - all missing from Jira/Slack data.
- Eitan Q2 QC (2026-06-29): self-assessment surfaced GitLab runner
  consolidation (budget savings), claude-code hooks/skills, Distribution
  Focus area help, Gator sessions with Hubert - invisible from tickets.

## Key insight

The gap between system-generated and self-reported is largest for "how"
(behaviors, collaboration patterns) and for work categories that routinely
have no Jira/Slack trace (cost optimization, AI tooling adoption,
mentoring, cross-team help).

Source: logs/2026-06-29.md (sessions 3, 5)
