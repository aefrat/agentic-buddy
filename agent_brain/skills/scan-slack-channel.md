---
last_accessed: 2026-06-14
access_count: 0
created: 2026-06-14
---

# Skill: Scan Slack channel and generate project update

## When to use

Triggered by requests to scan a Slack channel or set of channels for updates.
Examples: "scan the PitCrew channel", "what happened in #forum-jumpstarter",
"check Slack for updates", "scan all team channels". Also used as a sub-step
by the weekly report and daily review when Slack context is needed.

## Procedure

### 1. Identify target channels

Determine which channels to scan:
- Single channel: user specifies by name
- Multiple channels: user lists them, or use the channel list from the
  engineering-manager-report skill
- "All channels": use the full list from the weekly report config

### 2. Fetch channel history

Use `slack:channel-digest` or `slack:summarize-channel` skill for each channel.
These handle authentication, pagination, and thread resolution automatically.

**Why use skills instead of raw API:** Rule 18 — existing skills handle auth,
pagination, and error handling. The Slack MCP tools manage tokens and rate limits.

If the skill tools are unavailable (MCP not connected), fall back to
`slack:slack-search` for keyword-based discovery across channels.

Typical time window: last 3-4 days for daily scans, last 7 days for weekly.

### 3. Resolve context

For each channel with activity:
- Identify key threads (decisions, blockers, requests, announcements)
- Note who said what — use display names, not IDs
- Flag action items directed at the user or their teams
- Note items that need a response from the user

### 4. Cross-reference with project context (judgment call)

If the scan is for a project review (not a quick check):
- Compare findings against known project files in `agent_brain/projects/`
- Identify gaps between what's documented and what's happening in Slack
- Note process deviations or new information that updates project state

**Purpose:** Slack shows what people are *doing*; project files show what's
*documented*. The gap between the two reveals process issues and stale docs.

Skip this step for quick "what happened in channel X" requests.

### 5. Generate summary

Structure the output as:
- **Per-channel summary** — key threads, message count, participants
- **Action items for user** — things needing response or acknowledgment
- **Key findings table** (for multi-channel scans) — channel, finding, priority

### 6. Capture results

Write findings to the daily log under `## Slack channel scan (date range)`.
If scanning for a specific project, also update the project file in
`agent_brain/projects/`.
