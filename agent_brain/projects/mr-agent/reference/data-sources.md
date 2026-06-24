---
last_accessed: 2026-06-21
access_count: 1
created: 2026-06-21
---

# Data Sources

API reference and known issues for each data source used by `generate_report.py`.

## Jira

| Field | Value |
|-------|-------|
| URL | `https://redhat.atlassian.net` |
| Auth | Basic (base64 of email:token) |
| Env vars | `JIRA_API_TOKEN`, `JIRA_USER_EMAIL` (default: `aefrat@redhat.com`) |
| API | `POST /rest/api/3/search/jql` (v2 removed, HTTP 410) |
| Changelog | Per-issue via `GET /rest/api/3/issue/{key}/changelog` (v3 POST doesn't support `expand=changelog`) |

**Team JQL queries** (also in shared `members.yaml`):
- ATC: `project in ("Automotive Feature Teams") AND "AssignedTeam" in (rhivos-pdr-auto-toolchain, rhivos-aaa)`
- PitCrew: `project = PITCREW`

**Active statuses:** In Progress, In Review, Code Review, Review

## GitLab (internal)

| Field | Value |
|-------|-------|
| URL | `https://gitlab.cee.redhat.com` |
| Auth | Private token |
| Env var | `GITLAB_CEE_TOKEN` |

## GitLab (public)

| Field | Value |
|-------|-------|
| URL | `https://gitlab.com` |
| Auth | Private token |
| Env var | `GITLAB_COM_TOKEN` |

## GitHub

| Field | Value |
|-------|-------|
| URL | `https://api.github.com` |
| Auth | Bearer token |
| Env var | `GITHUB_TOKEN` |

## Google Docs

Read via `gws docs` CLI. Auth via gws OAuth token cache (auto-cleared by script at startup to prevent stale-token 403s).

**Configured docs** (also in shared `members.yaml` under ATC team):

| Name | Document ID |
|------|-------------|
| ATC Continuous Planning 2026 | `1gcaIDtjdmaqaAqddqUhvby5PPUnrLj73GqFlf_BzRag` |
| ToolChain Open Sync | `1TegJmbETVM627zvw5hj8F5NtiQvvJ40OSbgkGlz-pWw` |
| ATC Team Meeting Weekly 2026 | `190K1nFRRitw5BNak4wkrrpfKbQf1M67NfdQQ-I_SDwE` |

## Slack

| Field | Value |
|-------|-------|
| Access | Community slack-mcp MCP server (read-only) |
| Config | `~/.mcp.json` |
| Notable thread threshold | 3+ replies |

Channels are configured per team in shared `members.yaml`. Slack section degrades gracefully if MCP server is unavailable.

MCP tools: `get_channel_history` (with oldest/latest date filters), `search_messages`, `search_channel_messages`, `get_thread`.

## AI summaries (claude -p)

Calls `claude -p` subprocess for exec summaries and Slack digests. 4 calls per report (2 per team).

**Known issue:** `claude -p` in cron lacks Vertex AI env vars — AI-generated sections show "Not logged in." Degraded output: "Summary unavailable." / "Digest unavailable."

**Timeouts:** 60s for exec summary, 120s for Slack digest.

## Token expiration schedule

| Token | Expiry | Rotation |
|-------|--------|----------|
| Atlassian API "Avi2" | Jun 27, 2026 | Needs rotation this week |
| Slack (MCP server) | Depends on underlying token | MCP server handles auth; check server status if Slack section degrades |
| GitLab tokens | Varies | Check periodically |
