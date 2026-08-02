---
last_accessed: 2026-08-02
access_count: 1
created: 2026-08-02
---

# Requirements - Release Blocker Dashboard Agent

## Origin

RHIVOS 2.0 Retro (Jul 30, 2026). During a 20+ minute discussion on release
communication problems, Avi proposed an AI-powered blocker summary. Dana
directly assigned: "Avi, I'm tasking you." Juanje endorsed: "I would try first
the summary thing because it's simpler and it works with the model of we want
all the information in the readiness channel."

## Problem statement

During the RHIVOS 2.0 RC release, technical discussions were scattered across
10-15 Slack channels. Nobody could get a clear, current picture of what the
active release blockers were, who was handling them, or what the next step was.
The existing Jira dashboard exists but nobody checks it (Juanje: "you forget the
URL and it's a perfect dashboard that nobody sees"). Meeting notes are structured
but weekly. Slack is real-time but noisy.

## Core requirement

A containerized agent that produces a Google Doc dashboard per release showing:
what's blocking the release, where each blocker stands, who's handling it, and
what happens next - derived from Jira (source of truth), enriched with Slack and
meeting note context.

## Data sources

### 1. Jira (source of truth for blockers)

**Project:** VROOM (team-level). AUTOBU (BU-level, limited access).

**Blocker identification - union of signals:**

| Signal | Field | JQL |
|--------|-------|-----|
| Formal blocker | `customfield_10847` (release blocker dropdown) | `"release blocker[dropdown]" IN ("Approved Blocker", "Proposed Blocker")` |
| Formal exception | `customfield_10847` | `"release blocker[dropdown]" IN ("Approved Exception", "Proposed Exception")` |
| Priority = Blocker | `priority` | `priority = Blocker` |
| Impediment flag | `flagged` | `flagged = impediment` |

**Release scoping:** `fixVersion` field determines which release a ticket targets.
Known values: `rhivos-2.0`, `rhivos-2.0-core`, `rhivos-2.0.z`, `rhivos-2.0.z-core`,
`rhivos-2.1`, `rhivos-2.1-core`.

**Composite JQL per release:**
```
project = VROOM
AND (
  "release blocker[dropdown]" IS NOT EMPTY
  OR priority = Blocker
  OR flagged = impediment
)
AND fixVersion IN ("<release>", "<release-core>")
AND status NOT IN (Closed, Done, Verified)
```

**Fields to extract per ticket:** key, summary, status, priority, assignee,
fixVersions, components, release blocker type (customfield_10847), last updated.

**Existing dashboard:** https://redhat.atlassian.net/jira/dashboards/17073
(monitors blocker CVE progress; referenced in RR meeting notes).

### 2. Release readiness Slack channel (enrichment)

**Channel:** `automotive-release-readiness` (C04RHEEGY30)

**What to extract:** Messages from the last 7 days mentioning blocker ticket
keys (VROOM-XXXXX) or containing "blocked"/"blocker"/"blocking". Thread context
for active discussions. Who posted, when, what the update was.

**Purpose:** Add "last activity" and "latest context" to each Jira blocker row.
Surface blockers discussed in Slack that may not yet have formal Jira flags.

### 3. Release readiness meeting notes (enrichment)

**Document:** Google Doc `1MjoxfCEsDWiLFy99wHsS4EWOnVzvlg91NqJcMIHBDbI`

**Structure:** Weekly meeting notes, newest at top. Each meeting has topics,
discussion, action items (prefixed with "AI:"), and "Next Steps" sections.

**What to extract:** Latest meeting's blocker-related sections, decisions,
action items, and next steps.

**Purpose:** Add program-level decisions and next steps to each blocker.

## Output

Google Doc formatted as a release status dashboard. Updated on each run.
One doc per release (or sections per release in a single doc).

### Dashboard sections

1. **Header** - Release name, target date, current RC, last updated timestamp
2. **Active Blockers** - Table: ticket, summary, team, focal, status, next step, last activity, age (days)
3. **Proposed Blockers** - Tickets needing approval decision
4. **Exceptions** - Approved exceptions with status
5. **Weekly Activity Summary** - Narrative from Slack + meeting notes: what moved, what's stuck, key decisions
6. **Upcoming Milestones** - From meeting notes: CTC dates, errata deadlines, CDN readiness

## Constraints

- **No AIA/PIA required** - Uses existing RH-wide Slack MCP (introduced at DOL)
- **Read-only Slack** - Cannot post summaries to channels
- **Containerized** - Must run as a container image deployable to quay.io
- **No LLM-computed statistics** - Counts, ages, velocities computed by script
- Petr's PIA concern acknowledged; local PoC using existing approved tools

## Timeline

- **Deadline:** End of Q3 2026 (doc comment revision; originally "End of August" per Dana verbal)
- **PoC start:** 2026-08-02
- **Demo target:** End of August (show working PoC to Dana/team)
