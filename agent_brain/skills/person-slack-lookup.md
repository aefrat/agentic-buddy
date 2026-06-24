---
last_accessed: 2026-06-23
access_count: 0
created: 2026-06-23
---

# Skill: Person Slack Activity Lookup

## When to use

Triggered by: "what has [person] been doing on Slack", "check [person]'s
Slack activity", "[person] Slack messages", "search Slack for [person]",
or any request to find what a specific person posted across Slack channels.

## Procedure

### 1. Resolve the person's Slack username and user ID

Use `mcp__slack-mcp__search_messages` with the person's name to find a
recent message from them. Extract the Slack user ID (`U...`) and username.

**Purpose:** All subsequent queries depend on having the correct user ID.
Display names and real names can be ambiguous.

### 2. Search messages authored by the person

Use `mcp__slack-mcp__search_messages` with query `from:<username>` for
the target time range.

### 3. Search @mentions of the person

Use `mcp__slack-mcp__search_messages` with query `<@USER_ID>` to find
messages where others mentioned them. This captures discussions about
their work even when they didn't post.

### 4. Scan team channels for the person's activity

For key channels (team channels, project channels), use
`mcp__slack-mcp__get_channel_history` with `oldest`/`latest` ISO date
parameters for date filtering.

**Judgment call:** Scope channels based on context. For a team member,
scan their team's channels. For a stakeholder, scan channels where they
interact with the user's team.

### 5. Check thread replies

For significant messages found, use `mcp__slack-mcp__get_thread` to
fetch the full thread context. Standalone messages often lack the
working-group formation and coordination context visible in threads.

### 6. Synthesize findings

Group activity by theme, not chronologically. For each theme:
- What the person did or discussed
- Key decisions or commitments made
- Cross-team interactions

If a prior-week baseline is available (from previous lookups or reports),
note changes in activity patterns.

## Success criteria

- Person's Slack user ID confirmed (not assumed from name)
- Both authored messages and @mentions searched
- Key channels scanned for the target time range
- Findings grouped by theme with specific evidence

## Notes

- For batch lookups (multiple people), repeat steps 2-5 for each person
  before synthesizing. Keeps API calls grouped efficiently.
- This skill complements `scan-slack-channels` (channel-focused) and
  inbox check (user-focused). This one is person-focused.
- The manager report agent has a productionized version of this pattern
  via `STAKEHOLDERS` config and `render_stakeholder_slack_section()`.
