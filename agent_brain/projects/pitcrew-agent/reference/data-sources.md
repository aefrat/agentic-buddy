---
last_accessed: 2026-06-23
access_count: 0
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
| Channel IDs | Look up via `conversations.list` if needed |
| Auth | `$SLACK_XOXC_TOKEN` + `$SLACK_XOXD_COOKIE` from `~/.bashrc` |
| Method | bash curl (per CLAUDE.md Rule 20 — never use Slack MCP) |

### Queries

**Channel search (last 7 days):**
```bash
source ~/.bashrc
curl -s "https://redhat.enterprise.slack.com/api/search.messages" \
  -H "Authorization: Bearer $SLACK_XOXC_TOKEN" \
  -H "Cookie: d=$SLACK_XOXD_COOKIE" \
  -d "query=in:%23team-pitcrew-automotive&sort=timestamp&sort_dir=desc&count=50"
```

Repeat for `%23forum-jumpstarter`.

### Known issues

- Slack tokens expire without warning. If search returns `invalid_auth`, tokens need refreshing in `~/.bashrc`.

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
