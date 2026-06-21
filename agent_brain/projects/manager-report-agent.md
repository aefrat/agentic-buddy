---
last_accessed: 2026-06-21
access_count: 1
created: 2026-06-21
---

# Manager Report Agent

Stateful agent for the daily/weekly/weekend engineering manager status report. Wraps the existing Python script (`~/claude/manager-report/generate_report.py`) with identity, memory, verification, and learning following [Juanje's design principles](agent-forge-design-principles.md).

## Goal

Transform the stateless report pipeline into an agent that:
- Has an identity (evidence-based, pattern-aware operational intelligence)
- Accumulates history (every report is an episodic record, enabling comparison)
- Verifies itself (compares current vs previous, flags anomalies before sending)
- Learns (captures writing preferences, builds team activity baselines)
- Uses computed stats (script-derived, never LLM-generated) to ground AI summaries

## Architecture

**Harness:** Claude Code (agentic-buddy) — uses existing MCP tools + generate_report.py as execution engine.

**Execution engine:** `~/claude/manager-report/generate_report.py` — 1300-line Python script. Fetches data from 5 sources (Jira, GitLab.com, GitLab CEE, GitHub, Google Docs, Slack), makes 4 AI calls per report (2 exec summaries + 2 Slack digests via `claude -p`), produces HTML with inline CSS.

**Team config:** Shared with QC agent at `qc-agent/team/members.yaml` — single source of truth for both agents.

### Memory layout

```
agent_brain/projects/mr-agent/
├── index.md                         # Content map
├── reference/                       # Store 1 — read-only
│   ├── report-modes.md              # 3 modes, subject formats, cron schedules
│   ├── ai-prompt-templates.md       # Character-informed prompts for claude -p
│   └── data-sources.md              # API notes, known issues, env vars
├── active/                          # Store 2a — episodic active
│   ├── latest-snapshot.json         # Most recent run's data (overwritten)
│   └── latest-report.html           # Most recent HTML output (overwritten)
├── history/                         # Store 2b — episodic history (immutable)
│   └── YYYY-MM-DD-{mode}.{json,html}
├── computed/                        # Store 4 — computed (script-only, never LLM)
│   └── week-over-week.json          # Rolling averages, deltas, outliers
└── patterns/                        # Store 3 — semantic (consolidation only)
    ├── writing-preferences.md       # Learned from manager corrections
    └── team-activity-patterns.md    # Cross-week baselines
```

### Data sources

| Source | API | Auth | Env var |
|--------|-----|------|---------|
| Jira | `POST /rest/api/3/search/jql` | Basic (email:token) | `JIRA_API_TOKEN`, `JIRA_USER_EMAIL` |
| GitLab.com | REST v4 | Private token | `GITLAB_COM_TOKEN` |
| GitLab CEE | REST v4 | Private token | `GITLAB_CEE_TOKEN` |
| GitHub | REST v3 | Bearer token | `GITHUB_TOKEN` |
| Google Docs | `gws docs` CLI | OAuth | gws token cache |
| Slack | Web API | xoxc + cookie | `SLACK_XOXC_TOKEN`, `SLACK_XOXD_COOKIE` |
| AI summaries | `claude -p` | Vertex AI / API key | cron auth broken (known issue) |

## Plan — phased delivery

### Phase 1 — Harness & Identity (done)

- [x] Project file (this file)
- [x] Knowledge base structure (`mr-agent/`)
- [x] Reference store: modes, AI prompt templates, data sources
- [x] Shared team config extended (accent_color, google_docs)
- [x] Skill file rewritten with identity, steps, success criteria, checklist

### Phase 2 — Memory & Verification (done)

- [x] Extend sidecar JSON with metric counts (generated_at, mode, days, per-team metrics, Slack stats)
- [x] Add `--sidecar-output` flag to generate_report.py
- [x] Skill steps 5-6 activated: verify against previous snapshot, save to active + history
- [x] Disconfirmation gate: seek evidence report is wrong, flag anomalies with deltas

### Phase 3 — Computed Store (done)

- [x] `compute_stats.py` created — reads history snapshots, computes rolling averages, week-over-week deltas, per-member activity, anomaly detection
- [x] `--stats-file` flag added to `generate_report.py` — AI prompts enriched with computed context
- [x] AI identity injected into `_claude_summarize` and `_claude_slack_digest` prompts
- [x] Skill step 3 added: compute stats before generating report

### Phase 4 — Patterns & Learning (done)

- [x] `patterns/writing-preferences.md` — seeded with capture structure (style, emphasis, avoid, tone)
- [x] `patterns/team-activity-patterns.md` — seeded with baselines tables, seasonal/Slack patterns, member trajectories (Roderick, Matt)
- [x] `mr-capture` skill created — routes observations to correct pattern/reference file
- [x] Skill step 8 added: learn from this run (interactive mode only, update patterns when signals are clear)

## Design principles applied

| Principle | Application |
|-----------|------------|
| Identity & character | Evidence-based operational intelligence, pattern-aware, factual |
| Instruction delivery | Skill file ~100 lines; reference store for deep context |
| Progressive disclosure | index.md → skill steps → reference/data-sources.md |
| Tool design | Script is the tool; future: --dry-run for preview before send |
| Skill design | Trigger + 7 steps + success criteria + gotchas + checklist |
| Memory (4 stores) | Reference, active, history, computed, patterns |
| Permissions | History immutable; reference read-only; computed script-only |

> Related: [Agent Forge Design Principles](agent-forge-design-principles.md) — the framework this agent follows. [Quarterly Connection Agent](quarterly-connection-agent.md) — sibling agent using the same pattern.
