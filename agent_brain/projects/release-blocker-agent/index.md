---
last_accessed: 2026-08-02
access_count: 3
created: 2026-08-02
---

# Release Blocker Dashboard Agent - PoC Plan

RHIVOS 2.0 Retro action item: "AI briefs to get a clear state of the release blockers from the RR channel." Assigned to Avi by Dana Walker (Jul 30).

**Repo:** https://gitlab.cee.redhat.com/aefrat/rhivos-release-status
**Container:** quay.io/aefrat/rhivos-release-status:latest
**Status:** Phase 3 complete (Aug 2). LLM synthesis + combined dashboard + container rebuilt with LLM deps. E2E tested on all 3 releases with 4 Google Docs output. Demo to Dana/team not yet scheduled.
**Google Docs:** [Drive folder](https://drive.google.com/drive/folders/1OwzygOZihGEPr18tJFrWS0iQY_fGGySC) | [Program Summary](https://docs.google.com/document/d/1kj6C8JIMyIQmz8WclgWPhHq54d7tvAuQV1zgtLAw5Ps/edit)

## Features (Phase 1 + Phase 2)

- **Jira blocker query** - composite JQL for 3 blocker signals (Approved Blocker, Approved Exception, Proposed Blocker), age computation, team assignment via `customfield_10606` (AssignedTeam)
- **Workflow-aware triage** - tickets classified by urgency using RHIVOS workflow states: urgent (New), monitor (Integration blockers), active (In Progress), on_track (Release Pending + Integration exceptions). "Action Needed" column per ticket.
- **Pie chart** - all blockers including completed, grouped by 5 workflow categories (Completed/Release Pending/In QE/In Dev/Not Started). Pillow-generated PNG, base64 embedded.
- **Untracked ticket resolution** - 3-step: Jira fixVersion lookup, Slack context regex, unknown (all reports + disclaimer)
- **Potential blockers from Slack** - tickets with blocker keyword co-occurrence not yet flagged in Jira
- **Release-specific Slack digest** - messages filtered by ticket fixVersion
- **Google Doc output** - `--folder-id` creates new docs, `--doc-id` updates existing, via `gws` CLI
- **Workflow docs link** - footer links to RHIVOS Jira workflows Confluence page
- **Release readiness meeting notes** - Google Doc `1MjoxfCEsDWiLFy99wHsS4EWOnVzvlg91NqJcMIHBDbI` auto-loaded from config. Parser handles dateElement smart chips. 7-day window. Content filtered against known Jira blocker set (cross-reference, not keyword heuristics).
- **Executive brief** - 3-line max summary incorporating all 3 data sources (Jira, Slack, meeting notes). Adapts to released/active/all-clear/has-urgent context.
- **Data sources footer** - lists all information sources with links + RHIVOS workflows reference
- **LLM-powered release outlook** - Gemini 2.5 Flash via Vertex AI (ADC) generates 3-5 sentence release health summary per release. Dual-mode: API key or Vertex AI. Thinking disabled (`thinking_budget=0`) for simple synthesis.
- **Combined program dashboard** - 4th Google Doc aggregating all releases: program-level LLM outlook, summary table, per-release condensed sections with pie charts
- **GCP project:** `rhivos-release-blockers-agent` (ID `530839756563`) with Vertex AI API enabled

## Container operation

Tested with podman from quay.io. Required env vars: `JIRA_API_TOKEN`, `JIRA_USER_EMAIL`, `SLACK_XOXC_TOKEN`, `SLACK_XOXD_COOKIE`. For LLM: `VERTEX_PROJECT_ID` + ADC credentials mounted with `:z` flag (SELinux). Meeting notes require Workspace API scopes (not available via default ADC) - pipeline continues gracefully without them.

## Open questions

- Service account needed for unattended container execution (currently requires `gcloud auth` for Vertex AI ADC + Workspace API scopes for meeting notes)

## Files

- [Design](design.md) - Agent architecture, data model, output format
- [Requirements](requirements.md) - Requirements extracted from retro meeting, Slack, Jira analysis
