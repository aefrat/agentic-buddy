---
last_accessed: 2026-06-29
access_count: 2
created: 2026-06-23
---

# Data Sources

API reference, queries, and known issues for each data source.

## Jira

| Field | Value |
|-------|-------|
| Project | `PITCREW` |
| Board | 4323 |
| CLI | `jira` (preferred, per CLAUDE.md Rule 18) |
| Fallback | REST API v3 (`POST /rest/api/3/search/jql`) |
| Auth | `JIRA_API_TOKEN` + `JIRA_USER_EMAIL` (default: `aefrat@redhat.com`) |

### Queries

**a. All epics with status and assignee:**
```bash
jira issue list -q 'project = PITCREW AND issuetype = Epic ORDER BY status ASC, key ASC' --plain --columns key,summary,status,assignee,type
```

**b. Current sprint issues:**
```bash
jira issue list -q 'project = PITCREW AND sprint in openSprints() ORDER BY status ASC' --plain --columns key,summary,status,assignee,type
```

**c. Issue counts by status:**
```bash
jira issue list -q 'project = PITCREW AND status in ("In Progress", "New", "Closed", "Review", "Refinement")' --plain --columns status
```

**d. Fix versions / releases:**
```bash
jira issue list -q 'project = PITCREW AND fixVersion is not EMPTY ORDER BY fixVersion ASC' --plain --columns key,summary,status,fixVersion
```

**Active statuses:** In Progress, In Review, Code Review, Review, New, Refinement, Closed.

### Known issues

- `jira issue list` with `sprint in openSprints()` may fail if no sprint is active. Fallback: query by date range.
- Atlassian API token "Avi2" expires Jun 27, 2026. Needs rotation.

## Slack

| Field | Value |
|-------|-------|
| Channels | `#team-pitcrew-automotive`, `#forum-jumpstarter` |
| Channel IDs | C08SRMMGDK2, C064EKCGEF8 |
| Access | Community slack-mcp MCP server (read-only, configured in `~/.mcp.json`) |
| Method | MCP tool calls (per CLAUDE.md Rule 20) |

### Queries

**Channel history (last 7 days):**
```
mcp__slack-mcp__get_channel_history(channel_id="C08SRMMGDK2", oldest=<7_DAYS_AGO_ISO>, limit=200)
```

Repeat for `C064EKCGEF8` (#forum-jumpstarter).

**Channel search:**
```
mcp__slack-mcp__search_channel_messages(channel_id="C08SRMMGDK2", query="*", limit=50, sort="timestamp")
```

### Known issues

- MCP server is read-only. Never attempt write operations.
- If MCP tools return errors, flag in the report — don't silently skip.

## Google Docs

| Field | Value |
|-------|-------|
| CLI | `gws docs` |
| Auth | gws OAuth (run `gws auth status` to check) |

### Documents

| Name | Document ID | Refresh cadence |
|------|-------------|-----------------|
| RHAS Strategic Guide | `10qaHs_mfOCJtIJoJq35HjhHAeLEMJwYde51wgCKrQx8` | Monthly |
| 2026 Roadmap | `1j4Chcv71S8Y3P8HT2wTao9ZEoHoHm-X102VmaNpk1CA` | Monthly |

### Known issues

- Google auth tokens can expire silently. `gws docs` returns empty content on 403. Check `gws auth status` first.
