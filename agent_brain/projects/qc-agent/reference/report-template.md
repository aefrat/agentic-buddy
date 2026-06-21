---
last_accessed: 2026-06-21
access_count: 1
created: 2026-06-21
---

# Quarterly Connection Report Template

Structure for individual engineer evaluation reports. Based on the reference format from Q4 2025 (doc: 181zwHE6bq4Gw2WW4jYkFs5dArF8buQz0ubsX7N-nIdA).

## Report structure

```
# Individual Engineer Report — {Name}
{Title} | Team: {Team}
Period: {Quarter} {Year}

## Contribution Stats
- Jira tickets resolved: N (X Story Points)
- Internal GitLab MRs merged: N
- GitLab.com MRs merged: N
- GitHub PRs: N
- Slack messages: N across M channels

## Key Deliveries (by Story Point weight)
Top 3-5 deliverables organized by story point weight:
- {Deliverable title} ({N} pts): Brief impact description with ticket keys
- Highlight the WHAT and WHY, not just the ticket summary
- Group related tickets under a single deliverable theme

## Other Notable Contributions
- Bullet list of remaining work not covered above
- Include cross-project, upstream, and community contributions

## Feedback from Peers
### Strengths
- Specific behavioral strengths with evidence from 1:1s, peer feedback, Slack
### Opportunities
- Growth areas framed constructively
- "Could..." not "Should..." — forward-looking, not corrective

## Summary
3-5 sentences. Tone: appreciative, specific, forward-looking.
Written for the engineer to read.

## Supporting Data
- Jira tickets table (key, summary, type, story points)
- Internal GitLab MRs (title, project)
- Public GitLab MRs / GitHub PRs (title, project)
- Slack channel activity breakdown
```

## Aggregated team doc (separate Google Doc)

A companion document with:
- Team Performance Summary table (Name, Title, Team, Tickets, Story Points, Key Impact one-liner)
- Q vs previous Q comparison (tickets, SP, delta)
- Key observations narrative
- Individual ticket details per member

## Section generation order

Generate Key Deliveries first (establishes the factual foundation, ordered by SP weight), then Feedback (builds on deliveries with behavioral lens), then Summary (synthesizes both). Each section receives prior sections as context.

## Tone guidelines

- Evidence-based: every claim traceable to a ticket, MR, or observation
- Growth-oriented: strengths celebrated, development areas framed as opportunities
- Specific: "led the RHIVOS 2.0 kernel integration" not "contributed to the project"
- Fair: balanced view, not cheerleading
- Story points drive the hierarchy — highest-SP work gets the most narrative space
