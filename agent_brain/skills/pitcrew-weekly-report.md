---
last_accessed: 2026-06-08
access_count: 0
created: 2026-06-08
---

# Skill: PitCrew Weekly Report

## When to use

Triggered by:
- "generate the pitcrew report"
- "pitcrew weekly"
- "RHAS status report"
- "run the pitcrew report"
- `/pitcrew-weekly-report` or `/pitcrew-weekly-report full`

## Configuration

| Parameter | Value | Notes |
|-----------|-------|-------|
| Jira project | `PITCREW` | Board 4323 |
| Slack channels | `#team-pitcrew-automotive`, `#forum-jumpstarter` | Full mode only |
| Strategic Guide doc | `10qaHs_mfOCJtIJoJq35HjhHAeLEMJwYde51wgCKrQx8` | Refresh monthly |
| 2026 Roadmap doc | `1j4Chcv71S8Y3P8HT2wTao9ZEoHoHm-X102VmaNpk1CA` | Refresh monthly |
| Strategic context cache | `agent_brain/projects/pitcrew-strategic-context.md` | Auto-refreshed |
| Report output path | `user/reports/pitcrew-weekly-report-YYYY-MM-DD.html` | |
| Email recipients | `aefrat@redhat.com` | |
| Slack summary channel | `#team-pitcrew-automotive` | |
| HTML template reference | `user/reports/pitcrew-full-report-2026-06-01.html` | CSS lines 7–95 |

## Modes

| Mode | Sections | When |
|------|----------|------|
| **weekly** (default) | All sections except Slack Digest | Every week |
| **full** | All sections including Slack Digest (7-day window) | Bi-weekly + on demand |

If the user says "full" or the skill is invoked with argument `full`, use full mode. Otherwise default to weekly mode.

## Procedure

### 1. Determine report parameters

- Get today's date: `date +%Y-%m-%d`
- Compute the reporting week (last 7 days).
- Derive the current RHAS release from date: `RHAS-MMYY` format (e.g. June 2026 → RHAS-0626).
- Determine mode: `weekly` (default) or `full` (if argument is "full" or bi-weekly cadence).

### 2. Check strategic context cache

Read `agent_brain/projects/pitcrew-strategic-context.md`. Check `last_accessed` in frontmatter:
- If within 30 days → use the cached summaries for Strategic Guide and Roadmap sections. Skip step 3.
- If older than 30 days or file doesn't exist → proceed to step 3.

### 3. Fetch and cache strategic docs (only when cache is stale)

Use `/google:gws-docs` to read:
- Strategic Guide: doc ID `10qaHs_mfOCJtIJoJq35HjhHAeLEMJwYde51wgCKrQx8`
- 2026 Roadmap: doc ID `1j4Chcv71S8Y3P8HT2wTao9ZEoHoHm-X102VmaNpk1CA`

Extract and write to `agent_brain/projects/pitcrew-strategic-context.md`:
- Three-tier architecture summary (Tier 1 Standalone Builder, Tier 2 Automotive Suite, Tier 3 Unified IDP)
- Current quarter roadmap highlights with key milestones
- Release versioning convention (RHAS-MMYY, monthly cadence, milestone targets)
- Key strategic risks

Update `last_accessed` to today.

### 4. Fetch Jira data

Use the Jira MCP tools (`/jira:jira-task-management` or `/jira-mcp:jira-mcp-management`) to query the PITCREW project.

If MCP tools don't support the required queries, fall back to direct REST API:

```bash
source ~/.bashrc
JIRA_BASE="https://redhat.atlassian.net/rest/api/3"
AUTH="Authorization: Basic $(echo -n "${JIRA_USER_EMAIL:-aefrat@redhat.com}:${JIRA_API_TOKEN}" | base64)"
```

Queries needed:

**a. All epics with status and assignee:**
```
project = PITCREW AND issuetype = Epic ORDER BY status ASC, key ASC
```

**b. Current sprint issues:**
```
project = PITCREW AND sprint in openSprints() ORDER BY status ASC
```

**c. Issue counts by status:**
```
project = PITCREW AND status in ("In Progress", "New", "Closed", "Review", "Refinement")
```

**d. Fix versions / releases:**
List all fixVersions for PITCREW project to build the release timeline.

Extract from the data:
- Epic names, statuses, assignees, fix versions
- Sprint name, start/end dates, at-risk signals (% closed vs. % time elapsed)
- Active ticket details (key, type, summary, assignee, status)
- Issue counts by status
- Release timeline with current marker

### 5. Fetch Slack digest (full mode only)

Skip this step in weekly mode.

In full mode, use `/slack:summarize-channel` or `/slack:channel-digest` for each channel:
- `#team-pitcrew-automotive` — last 7 days
- `#forum-jumpstarter` — last 7 days

For each channel extract:
- Message count
- Top contributors (name + count)
- Key themes (5–8 bullet points: what topics dominated, what escalated, what's new)

If Slack MCP tools don't provide message counts or contributor breakdown, use `/slack:slack-search` to search for messages in date range and count manually.

### 6. Read project context

Read relevant files from `agent_brain/projects/` for supplementary context:
- `pitcrew-image-mode-future-2026-05-27.md` (if exists and recent)
- `rhivos-release-approach.md`
- Any other pitcrew-related project files

These provide background for the alignment analysis in step 7. Read selectively — only files relevant to current work.

### 7. AI synthesis

Generate three analytical sections from the collected data:

**a. Executive Summary** — 3–5 sentences answering: "What's the state of PitCrew this week?" Cover: sprint health, biggest risk, biggest win, what needs attention. This goes at the top of the report before the TOC.

**b. Strategy ↔ Work Alignment** — analyze how the week's actual work (Jira activity, epic movement) maps to the strategic guide and roadmap. Split into:
- **Well-aligned** — work that directly supports strategic goals (with specific epic/ticket references)
- **Gaps & Concerns** — strategic goals with no matching work, unassigned epics, key-person risks, timeline threats

**c. Looking Ahead** — split into:
- **This week** (immediate, urgent — red items)
- **This month** (important, planned — orange items)
- **Strategic setup** (forward-looking, Q3/Q4 — blue items)
- **Team health** (workload, morale signals — lightning bolt items)

### 8. Generate HTML report

Write self-contained HTML to `user/reports/pitcrew-weekly-report-YYYY-MM-DD.html`.

**CSS and layout:** Use the stylesheet and component patterns from `user/reports/pitcrew-full-report-2026-06-01.html` (lines 7–95). Copy the full CSS block into the generated report. Reuse these CSS classes:
- `.hero` — report header with title, date, source metadata
- `.toc` — table of contents links
- `.card` + `.card-title` — each section is a card
- `.badge .b-green/.b-blue/.b-orange/.b-purple/.b-gray/.b-red` — status badges
- `.alert .alert-warn/.alert-info/.alert-success/.alert-red` — callout boxes
- `.tier-grid` + `.tier` — three-tier architecture display
- `.roadmap-row` + `.roadmap-q` — quarterly roadmap display
- `.epic-grid` + `.epic` — epic cards in 2-column grid
- `.release-timeline` + `.rel` — release milestone badges
- `.fit-row` + `.fit-icon` — alignment analysis rows
- `table` — data tables for sprint tickets

**Report sections in order:**

0. **Hero banner** — title "PitCrew / RHAS — Weekly Status Report", date, source list, board link
1. **Executive Summary** — card with the AI-synthesized overview (from step 7a)
2. **Strategic Guide** — condensed 3-sentence summary from cache + "Changed this week: (none)" indicator. Include the 3-tier grid only if the strategic doc was refreshed this run.
3. **2026 Roadmap** — current quarter highlight only (Q2 or Q3 depending on date) + what moved since last week. Use `.roadmap-q` for the active quarter.
4. **RHAS Releases** — release timeline with `.rel` badges. Mark current with `.rel-current`. Show the epic targets table for the next 3 upcoming releases.
5. **Features & Epics** — split into "Changed this week" (status changes, new assignments) and "Unchanged" subsections. Use `.epic-grid`. Flag unassigned epics with ⚠️.
6. **Current Sprint** — sprint name and dates, at-risk alert if applicable, full ticket table with status badges, issue count summary boxes.
7. **Slack Digest** (full mode only) — two-column layout (`.cols2`), one per channel. Top contributors with `.person` badges. Key themes as bulleted list.
8. **Strategy ↔ Work Alignment** — from step 7b. Well-aligned items with ✅ `.fit-icon`, gaps with ⚠️.
9. **Looking Ahead** — from step 7c. Four subsections with color-coded items.

**Footer** — "Generated [date] · [source list with counts]"

### 9. Distribute

**a. Email:**
```bash
REPORT_DATE=$(date +%Y-%m-%d)
gws gmail +send --to aefrat@redhat.com \
  --subject "[PitCrew Weekly] RHAS Status — week of ${REPORT_DATE}" \
  --body "$(cat user/reports/pitcrew-weekly-report-${REPORT_DATE}.html)" --html
```

**b. Slack summary:**
Use `/slack:slack-messaging` to post a condensed text message to `#team-pitcrew-automotive`. Content:
- Executive summary (from step 7a)
- Sprint health: X/Y issues closed, at-risk or on-track
- Top 3 risks/blockers
- "Full report emailed — check inbox or `user/reports/`"

Keep Slack post under 2000 characters. No HTML — plain text with emoji markers.

### 10. Commit

```bash
REPORT_DATE=$(date +%Y-%m-%d)
git add user/reports/pitcrew-weekly-report-${REPORT_DATE}.html
git add agent_brain/projects/pitcrew-strategic-context.md
git commit -m "report: PitCrew weekly ${REPORT_DATE}"
```

## Scheduled runs

System crontab (`crontab -l`):
- **Weekly (alternating):** Sundays at 08:00 — alternates between `weekly` and `full` mode (even ISO weeks = full)
- **On demand:** invoke manually anytime with `/pitcrew-weekly-report` or `/pitcrew-weekly-report full`

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| Jira queries return empty | MCP tool doesn't support JQL | Fall back to `curl` with `JIRA_API_TOKEN` |
| Slack digest missing | Plugin not authenticated | Run `! slack-auth` or check Slack MCP connection |
| Google Docs read fails | Google auth expired | Run `gws auth status` then `gws auth login` if needed |
| HTML email truncated | Report too large for `--body` | Check `gws gmail +send` output; consider attachment mode |
| Strategic cache always stale | File not committed last run | Ensure step 10 commits the cache file |
