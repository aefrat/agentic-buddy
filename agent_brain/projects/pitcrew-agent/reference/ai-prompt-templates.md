---
last_accessed: 2026-06-23
access_count: 0
created: 2026-06-23
---

# AI Prompt Templates

Synthesis prompts for generating analytical sections. Each prompt is grounded in collected data — never generate statistics; only narrate what the data shows.

## Executive Summary

Generate 3–5 sentences answering: "What's the state of PitCrew this week?"

**Inputs:** Sprint health (counts, % complete, days elapsed/remaining), epic status changes (from diff), biggest risk, biggest win.

**Constraints:**
- Every claim references a Jira key or sprint metric
- Lead with the most actionable signal (risk or win)
- End with what needs attention this week
- Daily mode: 2–3 sentences max

## Strategy ↔ Work Alignment

Analyze how actual work (Jira activity, epic movement) maps to the strategic guide and roadmap.

**Inputs:** Strategic context (from cache), epic list with statuses, sprint tickets, roadmap milestones.

**Output structure:**
- **Well-aligned** — work that directly supports strategic goals. Each item: `✅ [description] — [epic/ticket reference]`
- **Gaps & Concerns** — strategic goals with no matching work, unassigned epics, key-person risks, timeline threats. Each item: `⚠️ [description] — [evidence]`

**Constraints:**
- Minimum 4 well-aligned items, minimum 3 gaps (if fewer gaps exist, that's a positive signal — note it)
- Never editorialize ("this is concerning") — state the gap factually
- Skip in daily mode

## Looking Ahead

Split into four categories with color-coded items.

**Output structure:**
- **This week** (red items) — immediate, urgent. What must happen in the next 5 days.
- **This month** (orange items) — important, planned. Key milestones this month.
- **Strategic setup** (blue items) — forward-looking, Q3/Q4 preparation.

**Constraints:**
- 2–4 items per category
- Do not include a "Team Health" category
- Each item is one sentence with a Jira key or person name where applicable
- Skip in daily mode
