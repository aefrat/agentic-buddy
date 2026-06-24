---
name: scan-slack-channels
description: Scan Slack channels and generate activity summaries with key findings and action items. Use when asked to scan Slack, check channels, summarize channel activity, or get a Slack update. Supports single channel, channel group (ATC, PitCrew), or all monitored channels.
compatibility: Uses community slack-mcp MCP server (read-only). No tokens or credentials needed — configured in ~/.mcp.json.
---

## Channel registry

### ATC channels

| Channel | ID |
|---|---|
| automotive-release-readiness | C04RHEEGY30 |
| automotive-toolchain | C04JDFLHJN6 |
| alerts-auto-toolchain | C04QLT849KN |
| automotive-image-builder | C0801T4TEQP |
| forum-rhivos-dut | C08GBTD1YG2 |
| test-console | C08CRGE1LKZ |
| wg-team-auto-toolchain-infra | C05BYR06B0V |
| wg-team-auto-toolchain-pulp | C06TM9U1FRQ |
| wg-team-auto-toolchain-tc | C06Q5BK3C4T |
| wg-team-auto-toolchain-gating | C065P1C6XB4 |
| wg-team-auto-toolchain-pipelines | C0672KC5RDH |
| wg-team-auto-toolchain-ai | C0910QFKTSN |
| wg-team-auto-toolchain-errata | C064MPL86N6 |
| team-auto-toolchain-qe | C04NFCZ892B |
| rhivos-sp-qc-layered-product | C0B3MNQSYE7 |

### PitCrew channels

| Channel | ID |
|---|---|
| team-pitcrew-automotive | C08SRMMGDK2 |
| forum-jumpstarter | C064EKCGEF8 |
| forum-rhivos-dut | C08GBTD1YG2 |

### QE channels

| Channel | ID |
|---|---|
| forum-qe-automotive | C04QYR4CBFB |

## Procedure

### 1. Determine scope and time window

Parse the user's request to determine:
- **Which channels:** a single channel by name, a group (`atc`, `pitcrew`, `qe`, `all`), or a custom list
- **Time window:** default is last 3 days for ad-hoc scans, 7 days for weekly scans. User can override with "since Monday", "last week", etc.

Compute the Unix timestamp for the start of the window.

### 2. Fetch channel history

For each target channel, use the community slack-mcp MCP server:

```
mcp__slack-mcp__get_channel_history(channel_id=<CHANNEL_ID>, oldest=<ISO_DATE>, latest=<ISO_DATE>, limit=200)
```

Filter messages by timestamp (>= computed oldest). Exclude `channel_join`, `channel_leave` subtypes.

For channels with threaded discussions (reply_count > 0), fetch key threads:

```
mcp__slack-mcp__get_thread(channel_id=<CHANNEL_ID>, thread_ts=<THREAD_TS>)
```

Only fetch threads with 3+ replies or threads that contain decisions, blockers, or action items.

### 3. Resolve user IDs to names

The slack-mcp MCP server resolves usernames automatically in message output. No separate user lookup step needed.

### 4. Check user's activity inbox

If the scan is comprehensive (all channels or weekly), also search for messages directed at the user:

```
mcp__slack-mcp__search_messages(query="to:me after:<YYYY-MM-DD>", limit=50, sort="timestamp")
```

This surfaces DMs, mentions, and threads the user is part of.

### 5. Generate summary

Structure the output as:

**Per-channel summary** (active channels only, sorted by message count descending):
- Channel name, message count, date range
- Key threads with participants (use real names)
- Decisions made, blockers raised, requests posted

**Quiet channels** — list channels with 0 messages (one line each).

**Action items for user** — things needing response or acknowledgment, pulled from the activity inbox and channel mentions.

**Key findings table** (for multi-channel scans):

| Priority | Item | Owner | Channel |
|----------|------|-------|---------|

### 6. Capture results

Write findings to the daily log (`logs/YYYY-MM-DD.md`) under a `## Slack channel scan` section.

If scanning for a specific project, also update the relevant project file in `agent_brain/projects/`.

## Gotchas

- **MCP date filtering.** `get_channel_history` accepts ISO 8601 dates (e.g., `"2024-01-15"`) or Unix timestamps for `oldest`/`latest`. If date filtering returns unexpected results, fetch without filters and post-filter by timestamp.
- **Bot messages.** Filter out `subtype: bot_message` unless specifically relevant (e.g., CI notifications in alerts channels).
- **Enterprise Grid usernames.** Slack `from:` search only works with usernames (e.g., `matgoldm`), not display names.
- **Thread depth.** Don't fetch threads with 50+ replies in full — summarize from the parent message + first few replies. Very long threads are usually live debugging sessions where the conclusion matters more than the play-by-play.
- **Read-only.** The slack-mcp server is read-only. Never attempt to post messages or perform write operations.
