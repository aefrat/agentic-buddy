---
last_accessed: 2026-09-06
access_count: 8
created: 2026-08-02
---

# Release Blocker Dashboard Agent - PoC Plan

RHIVOS 2.0 Retro action item: "AI briefs to get a clear state of the release blockers from the RR channel." Assigned to Avi by Dana Walker (Jul 30).

**Repo:** https://gitlab.cee.redhat.com/aefrat/rhivos-release-status
**Container:** quay.io/aefrat/rhivos-release-status:latest
**Status:** Phase 3 complete + CI operational on shared runners (Aug 3). **Data correctness bug fixed (Aug 5):** cross-release ticket leakage (Slack tickets appearing in all release reports) resolved via 3-part fix: release-scoped filtering in `synthesize.py`, `untracked_lookup` passthrough in `agent.py`, exact match in `compute_stats.py`. Pushed + pipeline #16855143 triggered. **OpenAI migration complete (Sep 6):** Migrated from Vertex AI Gemini to OpenAI gpt-4o-mini. Added `openai>=1.0` to dependencies, updated CI to use `OPENAI_API_KEY`, added `pull_policy: always` to run-daily job to force fresh image pulls. Verified in pipeline #17493828. Demo to Dana/team not yet scheduled.
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
- **LLM-powered release outlook** - 3-5 sentence release health summary per release. Supports 4 backends via `--llm-backend`: OpenAI (gpt-4o-mini, now default in CI), Gemini, Claude, Vertex AI Claude. CI uses OpenAI API key (Sep 6 migration).
- **Combined program dashboard** - 4th Google Doc aggregating all releases: program-level LLM outlook, summary table, per-release condensed sections with pie charts
- **GCP project:** `rhivos-release-blockers-agent` (ID `530839756563`) with Google Docs/Drive API enabled (Vertex AI no longer used for LLM as of Sep 6)

## Container operation

Tested with podman from quay.io. Required env vars: `JIRA_API_TOKEN`, `JIRA_USER_EMAIL`, `SLACK_XOXC_TOKEN`, `SLACK_XOXD_COOKIE`. For LLM: `OPENAI_API_KEY` (or `GOOGLE_API_KEY`/`VERTEX_PROJECT_ID`/`ANTHROPIC_API_KEY` for other backends). Meeting notes require Workspace API scopes (not available via default ADC) - pipeline continues gracefully without them.

## CI/CD Pipeline

GitLab CI at `gitlab.cee.redhat.com/aefrat/rhivos-release-status`:
- **lint:** ruff check on push/MR
- **build:** buildah to quay.io on main when Containerfile/tools/agent change
- **run-daily:** weekdays 07:00 UTC (09:00 CEST), also manual trigger via web UI
- **GCP SA:** `rhivos-dashboard-agent@rhivos-release-blockers-agent.iam.gserviceaccount.com` (Vertex AI User role, Drive folder writer, meeting notes doc viewer)
- **9 CI/CD variables:** JIRA_API_TOKEN, JIRA_USER_EMAIL, SLACK_XOXC_TOKEN, SLACK_XOXD_COOKIE, OPENAI_API_KEY, QUAY_USER, QUAY_TOKEN, GOOGLE_SA_KEY_PATH (file-type), DOCKER_AUTH_CONFIG
- **DOCKER_AUTH_CONFIG** CI variable for quay.io image pull auth
- **Runner:** Shared Kubernetes runners (`itup-alm-x86` tag) - no laptop dependency. Local Podman runner also available as fallback.
- **GCP APIs enabled:** Google Docs, Google Drive

Per-release doc IDs and combined_doc_id stored in `release-config.yaml` for CI upload without `gws` CLI.

## Requested fixes - Whitney Chadwick review (Sep 2, 2026)

Feedback from Whitney Chadwick (wchadwic) via Slack thread (RR channel C04RHEEGY30, Sep 2) + comments on the Program Summary doc. All comments were on `RHIVOS Program Release Status`; the three per-release docs had none. Two concrete fixes, both rooted in the same theme - the agent does not model the Core vs non-Core (FuSa) release split correctly:

1. **Core vs non-Core (FuSa) release separation.** The agent must treat `X.Y.Z-core` and `X.Y.Z` as distinct releases, with separate info filtering, related tickets, and stats for each. Applies to `rhivos-2.0.z-core` vs `rhivos-2.0.z`, and `rhivos-2.1-core` vs `rhivos-2.1`. The `X.Y.Z` (non-core) track is the FuSa release. Avi's ACK: "going forward a split between release X.Y.Z-core and X.Y.Z (AKA FuSa) releases and separate info filtering and related tickets and stats." (This overlaps with wchadwic's Slack note to "be sure the agent is looking at rhivos -core and non core fixed versions.")
2. **Release-status ("released") logic is wrong for FuSa.** The Program doc labeled `rhivos-2.0` as "released"; wchadwic: "rhivos-2.0 has not been released. This is the FuSa submission release." The agent is inferring 2.0's released status from `2.0-core` and applying it to the non-core version. Released status must be determined per core/non-core track, not shared.

Not a fix, resolved in thread: wchadwic asked "how does this differ from our defect dashboard?" Avi's answer - the agent's differentiator is the 2 extra data sources (Slack RR channel + RR meeting notes) that catch blockers moving too fast or not yet tracked in Jira; Jira source-of-truth is already covered by the defect dashboard.

Status: acknowledged, not yet implemented. Plan is to revise and republish the docs.

## Files

- [Core/FuSa split plan](core-fusa-split-plan.md) - Implementation plan for the Core vs non-Core (FuSa) release split (fix #1 + #2). Chosen structure: sub-sections per release doc.
- [Design](design.md) - Agent architecture, data model, output format
- [Requirements](requirements.md) - Requirements extracted from retro meeting, Slack, Jira analysis
