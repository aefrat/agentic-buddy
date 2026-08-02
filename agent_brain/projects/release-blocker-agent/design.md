---
last_accessed: 2026-08-02
access_count: 1
created: 2026-08-02
---

# Design - Release Blocker Dashboard Agent

Architecture follows [agent-forge design principles](../agent-forge-design-principles.md).
Containerized for quay.io deployment.

## Agent identity

**Name:** rhivos-release-status

**Character (80%):**
- Evidence-based: every blocker row traces to a Jira ticket or Slack message
- Verify-first: cross-references Jira state against Slack activity before reporting
- Cadence-aware: release dates create urgency gradients; stale blockers get flagged
- Direct: surfaces status, does not editorialize or assign work

**Hard limits (20%):**
- No Jira writes (read-only)
- No Slack writes (read-only)
- No ticket assignment or status changes
- Statistics computed by script, never by LLM

## Deployment model

Unlike session-based agent-forge agents that run inside Claude Code/Cursor,
this agent runs as a **containerized batch job**:

```
Container (quay.io/rhivos/release-status-agent)
  |
  +-- tools/           Python CLI tools (Jira, Slack, Google Docs)
  |     query-jira     Fetch blocker tickets per release
  |     scan-slack     Fetch RR channel activity (last 7 days)
  |     fetch-doc      Fetch RR meeting notes
  |     render-doc     Generate/update Google Doc dashboard
  |     compute-stats  Script-computed metrics (ages, counts, velocity)
  |
  +-- kb/
  |     reference/     Release definitions, team routing, JQL templates
  |     active/        Latest run snapshot (write-once per run)
  |     history/       Previous run snapshots (immutable)
  |
  +-- skills/
  |     blocker-status.md   Primary skill: end-to-end dashboard generation
  |
  +-- agent.py         Orchestrator: runs the skill steps in sequence
  +-- Containerfile
  +-- pyproject.toml
```

**Execution modes:**
1. **Manual** - `podman run quay.io/rhivos/release-status-agent --release rhivos-2.1`
2. **Scheduled** - CronJob (OpenShift) or cron (any Linux box)
3. **On-demand** - Triggered from Claude Code via a skill wrapper

**Why containerized, not session-based:**
- Runs anywhere (laptop, OpenShift, CI) without Claude Code installed
- Deterministic: same inputs produce same output (no LLM variance for data collection)
- Shareable: anyone on the team can run it, not just Avi
- Schedulable: cron job produces daily dashboard without human trigger

## Architecture: LLM vs script boundary

Agent-forge principle #6 (memory architecture): statistics must be
script-computed, never LLM-computed.

This agent applies that principle broadly. The **tools** are Python scripts
that do ALL data collection and computation. The **LLM** (optional) is used
ONLY for the narrative enrichment layer.

| Component | Runs as | LLM? | Purpose |
|-----------|---------|------|---------|
| `query-jira` | Python script | No | JQL query, extract fields, structured JSON |
| `scan-slack` | Python script | No | Fetch messages, filter by keywords/ticket keys |
| `fetch-doc` | Python script | No | Fetch Google Doc, extract latest meeting section |
| `compute-stats` | Python script | No | Blocker count, age, velocity, staleness detection |
| `render-doc` | Python script | No | Generate Google Doc from structured data |
| `enrich-narrative` | LLM call | Yes | Summarize Slack threads into "latest context" per blocker |

**Phase 1 (PoC):** No LLM at all. Pure script. Dashboard is a structured table
populated from Jira + Slack message excerpts + meeting note sections. This
removes the LLM dependency entirely for the core deliverable.

**Phase 2:** Add optional LLM enrichment for narrative summaries per blocker
(condense 15 Slack messages into a 2-sentence status update).

## Tool design (agent-forge principle #4)

Each tool follows the two-mode pattern: extract (default) vs download (--output).

### query-jira

```
bin/query-jira <release>

Input:  release name (e.g., "rhivos-2.1")
Output: JSON array of blocker tickets with fields:
  key, summary, status, priority, assignee, fix_versions,
  components, blocker_type, last_updated, age_days

Internally:
  - Maps release name to fixVersion values (e.g., rhivos-2.1 + rhivos-2.1-core)
  - Runs composite JQL (blocker dropdown + priority=Blocker + impediment flag)
  - Computes age_days from created date
  - Groups by blocker_type (Approved Blocker, Proposed Blocker, etc.)
```

### scan-slack

```
bin/scan-slack <channel-id> [--days 7]

Input:  Slack channel ID + lookback window
Output: JSON with:
  - messages mentioning "block*" keywords
  - messages mentioning known ticket keys (from query-jira output)
  - thread summaries (reply count, participants, latest reply)
  - per-ticket activity map: {VROOM-XXXXX: [messages]}

Internally:
  - Uses slack-mcp MCP server (community, read-only)
  - Filters by keyword and ticket key patterns
  - Groups messages by referenced ticket
```

### fetch-doc

```
bin/fetch-doc <doc-id>

Input:  Google Doc ID
Output: JSON with:
  - latest_meeting_date
  - sections: [{title, content, action_items, next_steps}]
  - blocker_mentions: [{ticket_key, context}]

Internally:
  - Uses gws docs API
  - Extracts newest meeting section (top of doc)
  - Parses "AI:" prefixed action items
  - Identifies ticket references (VROOM-XXXXX pattern)
```

### compute-stats

```
bin/compute-stats <jira-json> <slack-json>

Input:  Output files from query-jira and scan-slack
Output: JSON with:
  - total_blockers, approved_blockers, proposed_blockers
  - avg_age_days, max_age_days, oldest_ticket
  - stale_tickets (no Slack activity in 7+ days despite being open)
  - new_since_last_run (diff against kb/active/latest.json)
  - resolved_since_last_run

No LLM. Pure arithmetic.
```

### render-doc

```
bin/render-doc <stats-json> <jira-json> <slack-json> <doc-json> --doc-id <output-doc-id>

Input:  All collected data
Output: Updates Google Doc with formatted dashboard

Sections generated:
  1. Header with release name, target date, last updated
  2. Active Blockers table
  3. Proposed Blockers table
  4. Exceptions table
  5. Weekly Activity Summary (Slack excerpts + meeting notes)
  6. Computed Stats summary
```

## Knowledge base (agent-forge principle #6)

```
kb/
  reference/
    index.md              Hub
    release-config.yaml   Release names -> fixVersion mappings, target dates
    team-routing.yaml     Component -> team + default focal mapping
    jql-templates.yaml    JQL query templates
    channel-registry.yaml Slack channel IDs
  active/
    index.md              Hub
    latest.json           Most recent run output (write-once, overwritten per run)
  history/
    index.md              Hub
    YYYY-MM-DD.json       Snapshot per run date (immutable after write)
```

**Reference store** (developer-maintained): release configurations, team routing
rules, Slack channel registry. Updated when releases change.

**Active store** (agent writes): latest run output. Compared against on next run
to compute diffs (new blockers, resolved blockers).

**History store** (immutable): daily snapshots enabling trend analysis in Phase 3.

## Skill: blocker-status (agent-forge principle #5)

```
Trigger: "release status", "blocker dashboard", "run blocker report"

Steps:
  0. Parse input: extract target release name
  1. Run query-jira <release> -> jira.json
  2. Run scan-slack C04RHEEGY30 --days 7 -> slack.json
  3. Run fetch-doc <rr-meeting-doc-id> -> doc.json
  4. Run compute-stats jira.json slack.json -> stats.json
  5. Cross-reference: flag Slack-mentioned blockers missing from Jira
  6. Cross-reference: flag Jira blockers with no recent Slack activity (stale)
  7. Run render-doc to generate/update Google Doc dashboard
  8. Archive: copy jira.json to kb/history/YYYY-MM-DD.json

Success criteria:
  - Google Doc updated with current blocker state
  - All blocker rows trace to a Jira ticket
  - Stale blockers flagged (open in Jira, no Slack activity in 7+ days)
  - Stats section shows counts and ages (script-computed)

Disconfirmation gate (step 5-6):
  - Before reporting "no blockers": verify Slack doesn't mention
    untracked blockers
  - Before reporting a blocker as "stale": verify assignee isn't on PTO
    or working in a different channel
```

## Container structure

```dockerfile
FROM registry.access.redhat.com/ubi9/python-311

WORKDIR /app
COPY pyproject.toml .
RUN pip install .

COPY tools/ tools/
COPY kb/reference/ kb/reference/
COPY bin/ bin/
COPY agent.py .

ENV JIRA_API_TOKEN=""
ENV SLACK_BOT_TOKEN=""
ENV GOOGLE_APPLICATION_CREDENTIALS=""

ENTRYPOINT ["python", "agent.py"]
CMD ["--release", "rhivos-2.1"]
```

**Image:** `quay.io/rhivos/release-status-agent:latest`

**Required env vars:**
- `JIRA_API_TOKEN` - Jira API access
- `SLACK_BOT_TOKEN` - Slack API access (read-only)
- `GOOGLE_APPLICATION_CREDENTIALS` - Google Docs API (service account)
- `OUTPUT_DOC_ID` - Target Google Doc ID for dashboard

## Phased delivery

### Phase 1 - PoC (target: end of August)

Pure script, no LLM. Containerized.

- [ ] Scaffold repo from agent-forge skeleton
- [ ] Implement query-jira tool
- [ ] Implement scan-slack tool (using slack-mcp or direct Slack API for container)
- [ ] Implement fetch-doc tool (gws or direct Google Docs API for container)
- [ ] Implement compute-stats tool
- [ ] Implement render-doc tool (Google Doc output)
- [ ] Wire orchestrator (agent.py runs steps in sequence)
- [ ] Containerize (Containerfile + quay.io push)
- [ ] Create kb/reference/ configs for RHIVOS releases
- [ ] Demo to Dana/team

### Phase 2 - Enrichment (Q4)

Add optional LLM narrative layer.

- [ ] enrich-narrative: LLM summarizes Slack threads per blocker
- [ ] Historical diff: "new since last run" / "resolved since last run"
- [ ] Trend charts (script-computed, rendered as images in the doc)

### Phase 3 - Maturity

- [ ] Consolidation skill: weekly pattern extraction from history
- [ ] Alerting: flag when a blocker crosses age thresholds
- [ ] Multi-release: single run covers all active releases
- [ ] Integration with Luigi's landing page
