---
last_accessed: 2026-06-21
access_count: 1
created: 2026-06-21
---

# Quarterly Connection Report Template

Structure for individual engineer evaluation reports. Three narrative sections + supporting data.

## Report structure

```
# Individual Engineer Report — {Name}
{Title} | Team: {Team}
Period: {Quarter} {Year}

## Contribution Stats
- Jira tickets resolved: N (X Story Points)
- Internal GitLab MRs merged: N
- GitLab.com MRs merged: N

## Section A — The What
Accomplishments and impact on team/organization.
- Narrative form, organized by theme (not ticket-by-ticket)
- Highlight impact, not just activity
- Connect work to team/org goals

## Section B — The How
Behavioral assessment against Red Hat Multiplier competencies.
- Pick 2-3 most demonstrated competencies
- Cite specific evidence for each
- Include manager feedback and 1:1 observations
- Growth areas framed constructively

## Section C — Summary
Concise, publishable summary for the engineer.
- 3-5 sentences
- Tone: appreciative, specific, forward-looking
- Written for the engineer to read, not for HR

## Supporting Data
- Jira tickets table (key, summary, type, story points, resolved date)
- Internal GitLab MRs (title, project, link)
- Public GitLab MRs (title, project, link)
```

## Section generation order

Generate Section A first (establishes the factual foundation), then Section B (builds on A with behavioral lens), then Section C (synthesizes both). Each section receives prior sections as context.

## Tone guidelines

- Evidence-based: every claim traceable to a ticket, MR, or observation
- Growth-oriented: strengths celebrated, development areas framed as opportunities
- Specific: "led the RHIVOS 2.0 kernel integration" not "contributed to the project"
- Fair: balanced view, not cheerleading
