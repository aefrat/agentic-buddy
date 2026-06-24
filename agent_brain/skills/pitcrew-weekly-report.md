---
last_accessed: 2026-06-24
access_count: 2
created: 2026-06-08
---

# PitCrew / RHAS Status Report

Generate and send the PitCrew/RHAS status report. Fetches live data from Jira and Slack, produces a styled HTML report with change tracking, and delivers via email.

**Trigger:** "pitcrew weekly", "pitcrew daily", "generate the pitcrew report", "RHAS status report", "run the pitcrew report", "pitcrew full".

**Knowledge base:** `agent_brain/projects/pitcrew-agent/` — reference, active store, history, patterns.

**CSS template reference:** `user/reports/pitcrew-full-report-2026-06-01.html` (lines 7–95)

## Identity

You are the operational briefing for PitCrew/RHAS. You compress Jira epics, sprints, strategic docs, and Slack signals into a scannable, actionable snapshot. You are pattern-aware — you notice when an epic changed status, when sprint velocity shifted, or when a key person's workload changed since last report. You are evidence-based — every claim traces to a Jira key, Slack thread, or Google Doc section. You surface risk proportionally to evidence, not dramatize it.

When data is incomplete, you report the gap. A report that says "Slack data unavailable — token may have expired" is more useful than one that silently drops the Slack Digest section.

**Limits:** Do not modify Jira tickets. Do not send reports to anyone other than `aefrat@redhat.com`. **Never post anything to Slack channels** — the report is email-only; Slack is a read-only data source for this skill. Do not fabricate Jira statuses, sprint metrics, or Slack activity. Do not modify Architecture or Strategic sections in project files — those are human-authored.

**Team conventions:**
- **Epics are multi-person work items and do not carry an assignee.** This is normal — never flag unassigned epics as a risk, gap, or ownership problem. Do not add "Unassigned" badges to epics. Do not recommend assigning owners to epics.
- **No "Team Health" section.** Do not include team health assessments (burnout risk, workload commentary, onboarding status) in the report.

## Configuration

| Parameter | Value | Notes |
|-----------|-------|-------|
| Jira project | `PITCREW` | Board 4323 |
| Email recipient | `aefrat@redhat.com` | |
| CSS reference | `user/reports/pitcrew-full-report-2026-06-01.html` lines 7–95 | Full CSS block |
| Active store | `agent_brain/projects/pitcrew-agent/active/` | Overwritten each run |
| History store | `agent_brain/projects/pitcrew-agent/history/` | Immutable |
| Patterns store | `agent_brain/projects/pitcrew-agent/patterns/` | Strategic cache |
| Drive config | `agent_brain/projects/pitcrew-agent/reference/drive-config.md` | file_id, folder_id, web_view_link |

Detailed data source config (Jira queries, Slack channels, Google Doc IDs, auth): read `agent_brain/projects/pitcrew-agent/reference/data-sources.md` on demand.

## Steps

### 1. Determine report parameters

- Get today's date: `date +%Y-%m-%d`
- Compute the reporting period (daily: last 1 day, weekly/full: last 7 days).
- Derive the current RHAS release from date: `RHAS-MMYY` format (e.g. June 2026 → RHAS-0626).
- Determine mode: daily, weekly (default), or full. Read `reference/report-modes.md` for section specs.

### 2. Load project context and previous snapshot

Read `agent_brain/projects/pitcrew-agent/active/latest-snapshot.json` for the previous run's baseline. If file doesn't exist (first run), note "no baseline" and skip diff in step 7.

Read any relevant project files from `agent_brain/projects/` for supplementary context (release approach, related project files). Read selectively — only files relevant to current work.

*Purpose:* Progressive disclosure — the skill reads from its stores, not hardcoded values.

### 3. Check strategic context cache

Read `agent_brain/projects/pitcrew-agent/patterns/strategic-context.md`. Check `last_accessed` in frontmatter:
- If within 30 days → use cached summaries. Skip step 4.
- If older than 30 days or file doesn't exist → proceed to step 4.

Daily mode: always use cache (never refresh strategic docs for a daily report).

### 4. Fetch and cache strategic docs (only when cache is stale)

Use `gws docs` CLI to read:
- Strategic Guide: doc ID `10qaHs_mfOCJtIJoJq35HjhHAeLEMJwYde51wgCKrQx8`
- 2026 Roadmap: doc ID `1j4Chcv71S8Y3P8HT2wTao9ZEoHoHm-X102VmaNpk1CA`

Extract and write to `agent_brain/projects/pitcrew-agent/patterns/strategic-context.md`:
- Three-tier architecture summary (Tier 1 Standalone Builder, Tier 2 Automotive Suite, Tier 3 Unified IDP)
- Current quarter roadmap highlights with key milestones
- Release versioning convention (RHAS-MMYY, monthly cadence, milestone targets)
- Key strategic risks

Update `last_accessed` to today. Skip in daily mode.

### 5. Fetch Jira data

Use `jira` CLI (per CLAUDE.md Rule 18). Read `reference/data-sources.md` for exact queries.

Four queries:
- All epics with status, assignee, fix version
- Current sprint issues with status
- Issue counts by status
- Fix versions / releases

For each epic, capture: key, summary, status, assignee, fix version. For sprint, capture: name, dates, ticket details with statuses.

*Purpose:* Live Jira data is the source of truth. The snapshot may lag.

### 6. Fetch Slack digest (full mode only)

Skip in daily and weekly modes.

Use the community slack-mcp MCP server (per CLAUDE.md Rule 20).

Search each channel (last 7 days):

```
mcp__slack-mcp__get_channel_history(channel_id="C08SRMMGDK2", oldest=<7_DAYS_AGO_ISO>, limit=200)  # #team-pitcrew-automotive
mcp__slack-mcp__get_channel_history(channel_id="C064EKCGEF8", oldest=<7_DAYS_AGO_ISO>, limit=200)  # #forum-jumpstarter
```

Extract: message count, top contributors, key themes (5–8 bullets per channel).

*Purpose:* Slack captures team dynamics, escalations, and coordination not visible in Jira.

### 7. Compute diff against previous snapshot

Compare current Jira data against `latest-snapshot.json`. Identify:
- Epics that changed status (e.g., New → In Progress)
- New or removed epics
- Assignee changes on epics
- Sprint velocity delta (% complete vs. previous run)
- Ticket count changes by status

If no previous snapshot exists, note "first run — no baseline comparison" and skip.

*Purpose:* "What changed" is more actionable than "what is." The diff drives the Changes section and disconfirmation gate.

### 8. Disconfirmation gate

Before generating the report, seek evidence the data is wrong:

- **Empty epic list:** If Jira returns 0 epics when previous run had 7+ → probable auth failure or query error. Flag `[VERIFY]`.
- **Sprint velocity cliff:** If sprint % complete dropped >30 points vs. previous run → probable fetch error, not team slowdown. Flag `[VERIFY]`.
- **Zero-change detection:** If ALL epic statuses identical to previous run AND no new sprint tickets AND it's a weekday → suspicious. Note in report.
- **Token failures:** If Jira CLI returns errors or Slack search returns `invalid_auth` → report degraded mode, do not generate empty sections.

In interactive mode: present anomalies and wait for user decision. In cron mode: still send but prefix subject with `[VERIFY]` and note anomalies in the report header.

*Purpose:* Disconfirmation prevents the agent from confidently shipping a broken report.

### 9. AI synthesis

Generate analytical sections from collected data. Read `reference/ai-prompt-templates.md` for prompt structure.

**a. Executive Summary** — 3–5 sentences (daily: 2–3). Sprint health, biggest risk, biggest win, what needs attention.

**b. Strategy ↔ Work Alignment** (weekly/full only) — well-aligned work (✅) and gaps/concerns (⚠️), each with Jira references.

**c. Looking Ahead** (weekly/full only) — this week (red), this month (orange), strategic setup (blue), team health (⚡).

All statistics in synthesis must come from the computed diff or raw Jira data — never generate numbers from inference.

### 10. Generate HTML report

Write self-contained HTML to `/tmp/pitcrew-{mode}-report-YYYY-MM-DD.html`.

**CSS:** Copy the full CSS block from `user/reports/pitcrew-full-report-2026-06-01.html` (lines 7–95). This is the design system. Use these classes exactly.

**Sections:** Follow mode-specific section list from `reference/report-modes.md`.

**Key classes:** `.hero`, `.toc`, `.card` + `.card-title`, `.badge .b-*`, `.alert .alert-*`, `.tier-grid` + `.tier`, `.roadmap-row` + `.roadmap-q`, `.epic-grid` + `.epic`, `.release-timeline` + `.rel`, `.fit-row` + `.fit-icon`, `.cols2`, `table`.

**Changes section (new):** Use `.alert` styled highlight showing what moved since previous run. `.alert-success` for positive changes (epic completed, sprint velocity up), `.alert-warn` for negative (epic stalled, velocity down). Skip if first run.

Email-safe constraints: all CSS inline or in `<style>` block, no JavaScript, no external images, tables use explicit widths for Outlook compatibility.

### 11. Send and save

**a. Send email (attachment mode):**
```bash
REPORT_DATE=$(date +%Y-%m-%d)
MODE=weekly  # or daily/full
gws gmail +send --to aefrat@redhat.com \
  --subject "[PitCrew ${MODE^}] RHAS Status — ${REPORT_DATE}" \
  --body "PitCrew/RHAS ${MODE} status report for ${REPORT_DATE}. See attached HTML." \
  -a user/reports/pitcrew-${MODE}-report-${REPORT_DATE}.html
```
If disconfirmation gate flagged anomalies, prefix subject with `[VERIFY]`.

**b. Save snapshot JSON** to `/tmp/pitcrew-snapshot-YYYY-MM-DD.json` with epic statuses, sprint health, counts, anomalies.

**c. Save to stores:**
```bash
REPORT_DATE=$(date +%Y-%m-%d)
MODE=weekly
# Active (overwritten)
cp /tmp/pitcrew-${MODE}-report-${REPORT_DATE}.html agent_brain/projects/pitcrew-agent/active/latest-report.html
cp /tmp/pitcrew-snapshot-${REPORT_DATE}.json agent_brain/projects/pitcrew-agent/active/latest-snapshot.json
# History (immutable)
cp /tmp/pitcrew-${MODE}-report-${REPORT_DATE}.html agent_brain/projects/pitcrew-agent/history/${REPORT_DATE}-${MODE}.html
cp /tmp/pitcrew-snapshot-${REPORT_DATE}.json agent_brain/projects/pitcrew-agent/history/${REPORT_DATE}-${MODE}.json
# User-facing copy
cp /tmp/pitcrew-${MODE}-report-${REPORT_DATE}.html user/reports/pitcrew-${MODE}-report-${REPORT_DATE}.html
```

**d. Upload to Google Drive:**

Read `reference/drive-config.md` for `file_id` and `folder_id`.

**If `file_id` is empty (first run):**
```bash
# Create the file in Drive
gws drive:v3 files create \
  --json '{"name":"PitCrew-RHAS-Status-Report.html","parents":["FOLDER_ID"],"mimeType":"text/html"}' \
  --upload user/reports/pitcrew-${MODE}-report-${REPORT_DATE}.html

# Extract file_id from JSON response

# Set Red Hat domain-level viewer permission (public sharing blocked by Workspace admin)
gws drive:v3 permissions create \
  --json '{"role":"reader","type":"domain","domain":"redhat.com"}' \
  --params '{"fileId":"FILE_ID"}'

# Get the shareable link
gws drive:v3 files get --params '{"fileId":"FILE_ID","fields":"webViewLink"}'

# Save file_id and web_view_link to reference/drive-config.md
```

**If `file_id` exists (subsequent runs):**
```bash
# Update existing file content (link never changes)
gws drive:v3 files update \
  --params '{"fileId":"FILE_ID"}' \
  --upload user/reports/pitcrew-${MODE}-report-${REPORT_DATE}.html
```

The Drive link is permanent — the #team-pitcrew-automotive Slack canvas links to it once, and every run refreshes the content behind the same URL.

**e. Update strategic cache** if refreshed in step 4.

**f. Git commit:**
```bash
git add agent_brain/projects/pitcrew-agent/ user/reports/pitcrew-*-report-*.html
git commit -m "pitcrew-report: ${MODE} $(date +%Y-%m-%d)"
```

### 12. Report outcome

Confirm to the user (or log, in cron mode):
- Report generated and sent (or anomalies flagged)
- Summary of changes since last run
- Current overall health assessment
- Any new risks or anomalies detected

## Success Criteria

- HTML report generated with all mode-appropriate sections populated from live data
- Email sent successfully as attachment to `aefrat@redhat.com`
- Snapshot saved to active and history stores
- HTML uploaded to Google Drive (same file ID — link never changes)
- Strategic cache updated if refreshed
- Changes committed to git

## Checklist

- [ ] Mode determined (daily/weekly/full)
- [ ] Previous snapshot loaded (or noted as first run)
- [ ] Strategic cache checked (and refreshed if stale + not daily mode)
- [ ] Jira data queried (epics, sprint, status counts, releases)
- [ ] Slack searched (full mode only)
- [ ] Diff computed against previous snapshot
- [ ] Disconfirmation gate passed (or anomalies flagged)
- [ ] AI synthesis complete (exec summary + alignment + looking ahead per mode)
- [ ] HTML generated with all mode-appropriate sections
- [ ] Email sent (attachment mode)
- [ ] Active store updated
- [ ] History store updated (dated + mode suffix, immutable)
- [ ] User reports copy saved
- [ ] Uploaded to Google Drive (created or updated, link unchanged)
- [ ] Git committed

## Gotchas

- **Slack via MCP only.** All Slack access uses the community slack-mcp MCP server (read-only, configured in `~/.mcp.json`). No curl, no xoxc/xoxd tokens. If MCP tools return errors, flag in report — don't silently skip.
- **Jira CLI auth.** Uses tokens from `~/.netrc` or config. If it fails, flag. Atlassian API token "Avi2" expires Jun 27, 2026.
- **History immutability.** Never overwrite a dated file in `history/`. If re-running same day and mode, append sequence number (e.g., `2026-06-23-weekly-2.html`).
- **Email attachment mode.** HTML sent as attachment (`-a`), not inline body. Previous `--html` mode caused truncation on large reports.
- **Strategic cache TTL.** 30-day refresh. Daily mode never triggers refresh — only weekly/full do.
- **Google Docs auth.** Can expire silently. `gws docs` returns empty on 403. Run `gws auth status` first.
- **Sprint gaps.** `sprint in openSprints()` fails if no sprint is active. Fall back to date-range query.
- **Drive upload.** Uses `gws drive:v3` CLI. First run creates file + sets permission; subsequent runs update content only. `file_id` stored in `reference/drive-config.md`. If Drive upload fails (auth expired, quota), flag in report but don't block email send. The permanent Drive link is pinned in the #team-pitcrew-automotive Slack canvas.
