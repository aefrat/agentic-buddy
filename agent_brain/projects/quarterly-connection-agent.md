---
last_accessed: 2026-06-21
access_count: 1
created: 2026-06-21
---

# Quarterly Connection Agent

Stateful process-oriented agent for generating quarterly evaluation reports (Red Hat "Quarterly Connections"). Applies [Juanje's design principles](../concepts/stateful-process-oriented-agents.md) to a real problem previously solved as a [Python CLI](https://gitlab.cee.redhat.com/aefrat/qc_report_agent).

## Goal

Replace the stateless `eval-agent generate` CLI with a stateful agent that:
- Accumulates observations throughout the quarter (not just end-of-quarter data dumps)
- Learns writing patterns the manager prefers over time
- Builds cross-quarter growth narratives from episodic history
- Runs as a Claude Code skill in agentic-buddy, later extractable to standalone repo

## Architecture

**Harness:** Claude Code (agentic-buddy) — uses existing MCP tools (Jira, Google Docs, Gmail, Slack).

**Identity:** Evidence-based narrator of contributions. Fair, growth-oriented. Not a judge — a narrator that helps managers surface and articulate what their team accomplished.

### Memory layout

```
agent_brain/projects/qc-agent/
├── index.md                      # Content map
├── reference/                    # Store 1 — read-only
│   ├── multiplier-competencies.md  # Red Hat Multiplier framework
│   └── report-template.md         # Section A/B/C structure
├── team/                         # Store 1 — read-only (manager-maintained)
│   └── members.yaml               # Team roster with Jira/GitLab usernames
├── active/                       # Store 2a — episodic active
│   └── Q2-2026/                   # Current quarter workspace
│       ├── collected-data/        # Fetched Jira/GitLab/Slack data
│       ├── observations.md        # Mid-quarter captures
│       └── drafts/                # Work-in-progress reports
├── history/                      # Store 2b — episodic history (immutable)
│   └── Q1-2026/                   # Past quarter reports + data
└── patterns/                     # Store 3 — semantic (consolidation only)
    ├── writing-preferences.md     # Learned manager style
    └── team-growth.md             # Cross-quarter growth patterns
```

### Skills

| Skill | Trigger | Phase |
|-------|---------|-------|
| `quarterly-connection` | "quarterly connection", "QC report", "generate evaluation" | 1 |
| `qc-capture` | "note contribution", "capture for QC", mid-quarter observations | 2 |
| `qc-compare` | "compare quarters", "growth narrative", "cross-quarter" | 3 |

### Data sources (via existing MCP tools)

| Source | Tool | What it provides |
|--------|------|------------------|
| Jira | `jira:jira-mcp-management` | Resolved tickets, story points, epics |
| Internal GitLab | GitLab events API (`curl` + `GITLAB_CEE_TOKEN`) | Merged MRs per author. Uses `/users/{id}/events?action=merged` (not `/merge_requests` which misses cross-project MRs). |
| GitLab.com | GitLab events API (`curl` + `GITLAB_COM_TOKEN`) | Public MRs per author. Same events approach. |
| Slack | Community slack-mcp MCP server (`search_messages`, `get_channel_history`) | **Search-first:** `from:{kerberos}` discovers ALL channels the member was active in — including cross-team channels not in team config. Per-channel message counts + notable messages for evidence. |
| Google Docs | `google:gws-docs` | 1:1 notes for behavioral evidence (Section B) |
| Manager feedback | Manual YAML or inline | Strengths, growth areas, rating |

### Slack search-first approach

Instead of scanning predefined channels, search `from:{member} after:{quarter_start} before:{quarter_end}` — this discovers every channel the member participated in. Cross-team channels are often the best evidence for Multiplier competencies (Connection, Courage). Team config `slack_channels` are kept as a reference but not used as a filter.

## Report structure

Matches Red Hat Quarterly Connection template:

- **Section A — The What:** Accomplishments and impact (evidence from Jira + GitLab + Slack)
- **Section B — The How:** Behavioral assessment against Red Hat Multiplier competencies (evidence from 1:1 notes, Slack, manager feedback)
- **Section C — Summary:** Concise, publishable summary for the engineer

## Plan — phased delivery

### Phase 1 — Core skill (target: this week)

- [ ] Create skill `agent_brain/skills/quarterly-connection.md` with numbered steps
- [ ] Create `agent_brain/projects/qc-agent/index.md` content map
- [ ] Populate reference store: multiplier competencies, report template
- [ ] Create `team/members.yaml` with current team
- [ ] Skill steps: collect Jira → collect GitLab → generate sections → export to Google Doc
- [ ] Test with one team member for Q2 2026

### Phase 2 — Capture & history (week 2)

- [ ] Add `qc-capture` skill for mid-quarter observations
- [ ] After generating reports, move to `history/` (episodic close)
- [ ] Add manager feedback integration (inline or YAML)

### Phase 3 — Cross-quarter intelligence (week 3–4)

- [ ] Add `qc-compare` skill for growth narratives
- [ ] Semantic patterns: writing preferences, team growth trajectories
- [ ] Consolidation from history → patterns

### Phase 4 — Extraction (when ready)

- [ ] Extract to standalone repo with Pi or Claude Code harness
- [ ] Package for other managers to use
- [ ] Consider model flexibility (Gemini for cost, Claude for quality)

## Previous work

The [original CLI](https://gitlab.cee.redhat.com/aefrat/qc_report_agent) provides:
- Data models: `JiraTicket`, `MergeRequest`, `ManagerFeedback`, `MemberData`, `Report`
- Collector patterns: Jira JQL queries, GitLab user resolution + MR fetch
- LLM prompt chains: Section A → B → C with context threading
- Report template: Jinja2 with stats table + supporting data
- Security: input validation, parameterized queries, safe YAML parsing
- 52 tests covering collectors, generators, and security

Key reusable patterns:
- JQL construction for quarterly ticket queries
- GitLab API pagination and user resolution
- Three-section chained LLM generation with growing context
- Feedback placeholder workflow (auto-create, flag, re-generate)

## Design principles applied

| Principle | Application |
|-----------|------------|
| Identity & character | Evidence-based narrator, fair, growth-oriented |
| Progressive disclosure | Team roster → member data → full reports |
| Memory (4 stores) | Reference, active quarter, history, patterns |
| Skill design | Trigger + steps + success criteria + checklist |
| Tool design | MCP tools handle auth/retry; structured output |
| Permissions | History immutable; reference read-only |
| Verify-first | Cross-reference Jira data with Slack/1:1 evidence |
