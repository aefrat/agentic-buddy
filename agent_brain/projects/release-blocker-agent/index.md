---
last_accessed: 2026-08-02
access_count: 2
created: 2026-08-02
---

# Release Blocker Dashboard Agent - PoC Plan

RHIVOS 2.0 Retro action item: "AI briefs to get a clear state of the release blockers from the RR channel." Assigned to Avi by Dana Walker (Jul 30).

**Repo:** https://gitlab.cee.redhat.com/aefrat/rhivos-release-status
**Container:** quay.io/aefrat/rhivos-release-status:latest
**Status:** Phase 2 enhancements complete (Aug 2). 9 commits. E2E tested on all 3 releases. Demo to Dana/team not yet scheduled.

## Features (Phase 1 + Phase 2)

- **Jira blocker query** - composite JQL for 3 blocker signals (Approved Blocker, Approved Exception, Proposed Blocker), age computation, team assignment via `customfield_10606` (AssignedTeam)
- **Workflow-aware triage** - tickets classified by urgency using RHIVOS workflow states: urgent (New), monitor (Integration blockers), active (In Progress), on_track (Release Pending + Integration exceptions). "Action Needed" column per ticket.
- **Pie chart** - all blockers including completed, grouped by 5 workflow categories (Completed/Release Pending/In QE/In Dev/Not Started). Pillow-generated PNG, base64 embedded.
- **Untracked ticket resolution** - 3-step: Jira fixVersion lookup, Slack context regex, unknown (all reports + disclaimer)
- **Potential blockers from Slack** - tickets with blocker keyword co-occurrence not yet flagged in Jira
- **Release-specific Slack digest** - messages filtered by ticket fixVersion
- **Google Doc output** - `--folder-id` creates new docs, `--doc-id` updates existing, via `gws` CLI
- **Workflow docs link** - footer links to RHIVOS Jira workflows Confluence page

## Open questions

- Should the weekly release readiness meeting Google Doc be a data source? (user asked Aug 2, unanswered). `fetch-doc` tool exists but isn't wired into the pipeline.

## Files

- [Design](design.md) - Agent architecture, data model, output format
- [Requirements](requirements.md) - Requirements extracted from retro meeting, Slack, Jira analysis
