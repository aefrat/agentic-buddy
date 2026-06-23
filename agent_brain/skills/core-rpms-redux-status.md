---
last_accessed: 2026-06-23
access_count: 0
created: 2026-06-23
---

# Core RPMs Redux Status Report

Generate and send the Core RPMs Redux (VROOM-31017) status report. Fetches live data from Jira, Slack, and Google Docs, produces a styled HTML report with change tracking, and delivers via email.

**Trigger:** "core rpms report", "core rpms redux status", "run the core rpms report", "VROOM-31017 status", "core rpms redux report", "run redux report".

**Knowledge base:** `agent_brain/projects/core-rpms-redux-agent/` — reference, active store, history.

## Identity

You are the operational briefing for the Core RPMs Redux initiative (VROOM-31017). You track the transition from a single ambiguous "core RPMs" list to four machine-readable JSON package lists (Safety, Runtime, Image, Tools). You are completion-aware — the pipeline integration is done (Juanje's execopen work) and you focus attention on what remains: comparison gating, validators, FoA Lib updates. You are evidence-based — every claim traces to a Jira key, Slack message, or Google Doc section. You distinguish between the execopen pipeline work (Toolchain team, largely complete) and the downstream consumer work (FoA, validators, still open).

When data is incomplete, you report the gap. A report that says "Slack data unavailable — token may have expired" is more useful than one that silently drops the Pipeline Health section.

**Limits:** Do not modify Jira tickets. Do not send reports to anyone other than `aefrat@redhat.com`. Do not fabricate Jira statuses or invent Slack activity. Do not modify the project file's Key artifacts, Key people, or Slack channels sections — those are human-authored.

## Configuration

| Parameter | Value | Notes |
|-----------|-------|-------|
| Main epic | VROOM-31017 | Core RPMs Redux |
| Toolchain umbrella | VROOM-31421 | Build toolchain base |
| Email recipient | `aefrat@redhat.com` | |
| Subject format | `[Core RPMs Redux] Status — YYYY-MM-DD` | Prefix with `[VERIFY]` if anomalies |
| Output path | `user/reports/core-rpms-redux-YYYY-MM-DD.html` | |
| Active store | `agent_brain/projects/core-rpms-redux-agent/active/` | Overwritten each run |
| History store | `agent_brain/projects/core-rpms-redux-agent/history/` | Immutable |
| Semantic store | `agent_brain/projects/core-rpms-redux.md` | Updated with latest statuses |

Data source config (Jira queries, Slack channels, Google Doc IDs, auth): read `agent_brain/projects/core-rpms-redux-agent/reference/data-sources.md` on demand.

## Steps

### 1. Load project context and previous snapshot

Read `agent_brain/projects/core-rpms-redux.md` — extract goal, 4-list structure, current status, completed tickets (Juanje's execopen chain), remaining work, toolchain work (VROOM-31421), related epics, key people, Slack channels.

Read `agent_brain/projects/core-rpms-redux-agent/active/latest-snapshot.json` for the previous run's baseline. If file doesn't exist (first run), note "no baseline" and skip diff in step 4.

### 2. Fetch Jira data

Use `jira` CLI (per CLAUDE.md Rule 18). Read `reference/data-sources.md` for exact queries.

Five queries:
- **(a)** VROOM-31017 epic details
- **(b)** All children/linked issues of VROOM-31017
- **(c)** Known open work tickets (VROOM-40719, VROOM-40584, VROOM-37096, VROOM-37575, VROOM-30619)
- **(d)** VROOM-31421 subtasks (toolchain)
- **(e)** Related epics (VROOM-37039, VROOM-29696, VROOM-38899)

For each ticket capture: key, summary, status, assignee. Note any blockers.

### 3. Fetch Slack activity and Google Docs context

**Slack:** Use bash curl with `$SLACK_XOXC_TOKEN` and `$SLACK_XOXD_COOKIE` from `~/.bashrc` (per CLAUDE.md Rule 20 — never Slack MCP plugin). Read `reference/data-sources.md` for exact queries.

Four searches:
- **(a)** #team-toolchain-automotive (primary work, 30 messages)
- **(b)** #alerts-auto-toolchain (pipeline failures, 20 messages)
- **(c)** #team-auto-follow-on-activities (FoA/validators, 20 messages)
- **(d)** Cross-channel keyword search ("core-rpms" OR execopen OR VROOM-31017)

From #alerts-auto-toolchain: extract pipeline failure count, most recent failure, whether resolved.

**Google Docs:** Use `gws docs` CLI. Read `reference/data-sources.md` for fetch pattern.
- ToolChain Open Sync (doc ID `1TegJmbETVM627zvw5hj8F5NtiQvvJ40OSbgkGlz-pWw`) — extract latest meeting notes on core-rpms/execopen.
- Workstreams doc (doc ID `1uakPWEkSvMksJ9XAfPHlU_h9mMVpcIr9F2uufJw4-Ek`) — extract workstream status.

Check `gws auth status` first; if expired, flag and skip (don't error out).

### 4. Compute diff against previous snapshot

Compare current data against `latest-snapshot.json`. Identify:
- Tickets that changed status
- Newly completed tickets
- Newly blocked tickets
- Assignee changes
- Toolchain ticket status changes
- Pipeline alert count delta

If no previous snapshot exists, note "first run — no baseline comparison" and skip.

### 5. Disconfirmation gate

Before generating the report, seek evidence the data is wrong:

| Check | Condition | Action |
|-------|-----------|--------|
| Empty result set | Jira query (b) returns 0 tickets when previous had 6+ | Flag `[VERIFY]` — probable auth failure |
| Ticket regression | Any ticket moved backward (In Progress → New) | Flag for review in report |
| Zero-change detection | All statuses identical to previous + no Slack activity + weekday | Note as suspicious |
| Completed-to-open regression | Any of Juanje's 6 closed execopen tickets now non-Closed | Flag `[VERIFY]` — probable data error |
| Token failures | Jira CLI errors or Slack `invalid_auth` | Report degraded mode, note which sources failed |
| Toolchain data mismatch | VROOM-31421 returns 0 subtasks when previous had 7+ | Flag `[VERIFY]` |

Interactive mode: present anomalies and wait for user decision.
Cron mode: prefix subject with `[VERIFY]` and note anomalies in the report header.

### 6. AI synthesis

Generate analytical sections from collected data:

- **Executive summary** (2–3 sentences): Pipeline integration status, biggest open risk, what needs attention next. Every claim references a Jira key, Slack message, or Google Doc section. Never generate numbers from inference.
- **Pipeline health assessment** (from #alerts-auto-toolchain): recent failures, patterns, current status.

### 7. Generate HTML report

Write self-contained HTML to `/tmp/core-rpms-redux-YYYY-MM-DD.html`.

**CSS:** Use the Red Hat design system CSS variables and component classes. The report must be email-safe: all CSS in `<style>` block, no JavaScript, no external images, explicit table widths for Outlook.

Additional classes for this report:
```css
.list-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin: 14px 0; }
.list-card { border-radius: 8px; padding: 14px 16px; border: 1px solid #ddd; background: #fff; }
.list-card h4 { font-size: 0.9rem; font-weight: 700; margin-bottom: 6px; }
.list-card .desc { font-size: 0.82rem; color: #6a6e73; }
.pipeline-ok { border-left: 4px solid #3e8635; }
.pipeline-warn { border-left: 4px solid #f0ab00; }
.pipeline-fail { border-left: 4px solid #c9190b; }
```

**Sections (14 total):**

1. **Hero banner** — Title "Core RPMs Redux (VROOM-31017)", date, overall status badge. Badge logic:
   - All remaining tickets closed + pipeline passing → `Complete` (green)
   - Any remaining ticket blocked >5 days → `Blocked` (red)
   - All remaining tickets New/unstarted → `Stalled` (amber)
   - Otherwise → `In Progress` (blue)

2. **Meta row** — Epic link, owner (Petr Sabata), pipeline lead (Juanje Ojeda), due date, Slack channel.

3. **Executive summary** — 2–3 sentences from step 6, highlighted box.

4. **4-List overview** — `.list-grid` with 4 `.list-card` items: Safety List, Runtime List, Image List, Tools List. Each shows: name, description, generation status (Pipeline-generated / Curated / TBD).

5. **Summary cards** — 4 cards: Completed (green), In Progress (blue), Not Started (gray), Total. Counts from Jira query (b).

6. **Progress bar** — Done/progress/remaining segments, percentage from counts.

7. **Changes since last report** — Status change highlights: green for completed, red for newly blocked, neutral for status updates. Skip section if first run.

8. **Completed work table** — Juanje's closed execopen tickets + other closed children. Columns: Ticket (linked), Summary, Assignee, Closed Date. Green badge.

9. **Open/remaining work table** — Open tickets from queries (b) and (c). Columns: Ticket, Summary, Status (badge), Assignee, Blockers. Color badges per status.

10. **Toolchain work (VROOM-31421)** — Subtask table from query (d). Columns: Ticket, Summary, Status, Assignee. Separate section — sibling epic, not child of VROOM-31017.

11. **Pipeline health** — From #alerts-auto-toolchain: failure count (7 days), most recent failure, current status. Left-border styling: `.pipeline-ok`, `.pipeline-warn`, `.pipeline-fail`. If no alerts: "No pipeline alerts in the last 7 days."

12. **Risks & blockers** — Numbered risk list. Sources: unassigned tickets, blocked tickets, overdue epic (VROOM-31017 due Jun 3), validator re-enablement (VROOM-37575) not started.

13. **Key references** — Links table: Jira epic, execopen repo, ToolChain Open Sync doc, Workstreams doc, Confluence checklist.

14. **Footer** — Generated date, data sources queried.

### 8. Send and save

**a. Send email:**
```bash
REPORT_DATE=$(date +%Y-%m-%d)
gws gmail +send --to aefrat@redhat.com \
  --subject "[Core RPMs Redux] Status — ${REPORT_DATE}" \
  --body "Core RPMs Redux (VROOM-31017) status report for ${REPORT_DATE}. See attached HTML." \
  -a user/reports/core-rpms-redux-${REPORT_DATE}.html
```
If disconfirmation gate flagged anomalies, prefix subject with `[VERIFY]`.

**b. Save snapshot JSON** to `/tmp/core-rpms-redux-snapshot-YYYY-MM-DD.json`.

Snapshot schema:
```json
{
  "generated_at": "YYYY-MM-DD",
  "overall_status": "In Progress|Complete|Blocked|Stalled",
  "epic": { "key": "VROOM-31017", "status": "...", "assignee": "..." },
  "tickets": [
    { "key": "...", "summary": "...", "status": "...", "assignee": "...", "blockers": [], "category": "remaining|validator|foa" }
  ],
  "completed_tickets": [
    { "key": "...", "summary": "...", "assignee": "...", "closed_date": "..." }
  ],
  "toolchain_tickets": [
    { "key": "...", "summary": "...", "status": "...", "assignee": "..." }
  ],
  "related_epics": [
    { "key": "...", "summary": "...", "status": "...", "assignee": "..." }
  ],
  "counts": { "completed": 0, "in_progress": 0, "not_started": 0, "blocked": 0 },
  "pipeline_health": { "alert_count_7d": 0, "latest_failure": "...", "status": "passing|failing|degraded" },
  "slack_activity_count": 0,
  "google_docs_accessed": true,
  "anomalies": []
}
```

**c. Save to stores:**
```bash
REPORT_DATE=$(date +%Y-%m-%d)
# Active (overwritten)
cp /tmp/core-rpms-redux-${REPORT_DATE}.html agent_brain/projects/core-rpms-redux-agent/active/latest-report.html
cp /tmp/core-rpms-redux-snapshot-${REPORT_DATE}.json agent_brain/projects/core-rpms-redux-agent/active/latest-snapshot.json
# History (immutable — never overwrite a dated file; append sequence number on re-runs)
cp /tmp/core-rpms-redux-${REPORT_DATE}.html agent_brain/projects/core-rpms-redux-agent/history/${REPORT_DATE}.html
cp /tmp/core-rpms-redux-snapshot-${REPORT_DATE}.json agent_brain/projects/core-rpms-redux-agent/history/${REPORT_DATE}.json
# User-facing copy
cp /tmp/core-rpms-redux-${REPORT_DATE}.html user/reports/core-rpms-redux-${REPORT_DATE}.html
```

**d. Update project file:** Update `agent_brain/projects/core-rpms-redux.md`:
- Update "Current status" section date
- Update ticket statuses in Remaining work and Toolchain tables
- Do NOT modify Goal, Key people, Key artifacts, or Slack channels sections

**e. Git commit:**
```bash
git add agent_brain/projects/core-rpms-redux-agent/ agent_brain/projects/core-rpms-redux.md user/reports/core-rpms-redux-*.html
git commit -m "core-rpms-redux-report: $(date +%Y-%m-%d)"
```

### 9. Report outcome

Confirm to the user:
- Report generated and sent (or anomalies flagged)
- Summary of changes since last run
- Current overall status
- Any new risks or blockers detected

## Success criteria

- HTML report generated with all 14 sections populated from live data
- Email sent successfully to `aefrat@redhat.com`
- Snapshot saved to active and history stores
- Project file updated with current ticket statuses
- Changes committed to git

## Checklist

- [ ] Project file read for context
- [ ] Previous snapshot loaded (or noted as first run)
- [ ] Jira data queried (5 queries)
- [ ] Slack searched (4 searches)
- [ ] Google Docs read (2 documents)
- [ ] Diff computed against previous run
- [ ] Disconfirmation gate passed (or anomalies flagged)
- [ ] AI synthesis complete (executive summary + pipeline health)
- [ ] HTML generated with all 14 sections
- [ ] Email sent
- [ ] Active store updated
- [ ] History store updated (dated, immutable)
- [ ] User reports copy saved
- [ ] Project file statuses updated
- [ ] Git committed

## Gotchas

- **Slack tokens expire.** If Slack searches return `invalid_auth`, the `$SLACK_XOXC_TOKEN` in `~/.bashrc` needs refreshing. Flag in report, don't silently skip.
- **Jira CLI auth.** Atlassian API token "Avi2" expires Jun 27, 2026.
- **History immutability.** Never overwrite a dated file in `history/`. If re-running same day, append sequence number (e.g., `2026-06-23-2.html`).
- **Email attachment.** HTML sent as attachment (`-a`), not inline body.
- **VROOM-31017 due date passed.** Epic due Jun 3. Known condition — disconfirmation gate should not flag it repeatedly, only if overdue status changes.
- **Juanje's completed chain.** 6 tickets are historically closed (VROOM-41395, 40718, 40716, 40715, 40717, 37485). If Jira shows any as open, that's a data error. Flag `[VERIFY]`.
- **Google Docs auth.** Can expire silently. `gws docs` returns empty on 403. Run `gws auth status` first.
