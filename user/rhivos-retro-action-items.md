# RHIVOS 2.0 Retro - Avi's Action Items

From the [RHIVOS 2.0 Retro](https://docs.google.com/document/d/17q7g2rd3-JvBy7jHn3Py85fqAPmYvN0Wwxe-uNIs7FI/edit) meeting (2026-07-30).
Full analysis and meeting notes at `agent_brain/projects/rhivos-2.0-retro.md`.

## Directly assigned to Avi

### 1. AI-powered release blocker summary (PoC)

- **What:** Containerized agent that produces a Google Doc dashboard per release showing active blockers, their status, ownership (team + focal), and next steps.
- **Deadline:** End of Q3 2026 (demo target: end of August)
- **Approach:** Agent-forge design principles. Containerized (quay.io), runnable anywhere. Phase 1 is pure script (no LLM needed). Three data sources:
  1. **Jira (source of truth):** VROOM release blocker dropdown + priority=Blocker + impediment flag, scoped by fixVersion
  2. **Release readiness Slack:** Last 7 days of activity, filtered by blocker keywords and ticket keys
  3. **RR meeting notes (Google Doc):** Latest meeting sections, action items, next steps
- **Output:** Google Doc dashboard with: active blockers table, proposed blockers, exceptions, weekly activity summary, computed stats
- **Design doc:** `agent_brain/projects/release-blocker-agent/design.md`
- **Requirements:** `agent_brain/projects/release-blocker-agent/requirements.md`
- **Notes from doc comments:** Petr raised PIA concern for AI+Slack. Avi clarified: RH-wide Slack MCP from DOL is already available and in use. Container can use Slack API directly with bot token.
- [x] Scaffold repo from agent-forge skeleton
- [x] Implement tools: query-jira, scan-slack, fetch-doc, compute-stats, render-doc
- [x] Wire orchestrator (agent.py)
- [x] Create kb/reference/ configs for RHIVOS releases (rhivos-2.0, rhivos-2.0.z, rhivos-2.1)
- [x] Containerize + push to quay.io
- [x] End-to-end test with live data (all 3 releases pass: 31/1/1 blockers)
- [ ] Demo to Dana/team
- **Start date:** 2026-08-02
- **Repo:** https://gitlab.cee.redhat.com/aefrat/rhivos-release-status
- **Container:** `quay.io/aefrat/rhivos-release-status:latest`
- **Status:** Phase 1 complete. All deliverables done except demo.

### 2. Fill out retro doc action items

- **What:** Edit the retro Google Doc's action items section with what was agreed in the meeting.
- **Deadline:** This week (Jul 30-Aug 1)
- **Status:** Done (items were filled in during/after meeting)

## Avi's follow-up items (not formally assigned but raised by Avi)

### 3. Follow up on Petr's KWF alignment meeting

- **What:** Avi raised in the retro that Petr planned a meeting with RHIVOS kernel team and RHEL KWF team to align tag workflows. No update from Petr during the retro. Pre-meeting investigation confirmed no evidence the meeting took place (Slack + Calendar search Jul 30).
- **Action:** Bring up in next Petr 1:1 (2nd Tuesday of month = Aug 11). Ask for status and whether this is still planned or has been deprioritized given Z-stream becoming the right target.
- [ ] Raise in Petr 1:1 (Aug 11)
- **Status:** Not started

### 4. Contribute to end-to-end release dashboard

- **What:** Avi proposed a live dashboard showing release status - "same URL, what's going on, where is the block, which team, who's the focal." Luigi owns the landing page action item; Avi volunteered to combine with the AI summary.
- **Action:** Coordinate with Luigi on dashboard PoC once AI summary PoC is ready. Dashboard can consume the AI-generated blocker summaries.
- [ ] Sync with Luigi on format/approach
- [ ] Integrate AI summary output into dashboard format
- **Status:** Blocked on AI summary PoC (#1)

### 5. STAG automation follow-up

- **What:** Petr's lockstep build proposal (STAG) would eliminate manual kernel companion package tagging entirely. Not implemented. Avi wrote this in the retro doc but it wasn't discussed in the meeting.
- **Action:** Track in Petr 1:1. Ask for timeline and whether this is on any roadmap.
- [ ] Raise in Petr 1:1 (Aug 11)
- **Status:** Not started

## Items to monitor (owned by others, ATC-relevant)

| Item | Owner | Deadline | Why ATC cares |
|------|-------|----------|---------------|
| Cross-functional definitions review | Whitney | End of Aug | Kernel team responsibilities clarity affects ATC daily |
| Handoff documentation | Juanje | End of Q3 | ATC is the handoff hub between kernel and release |
| Technical release Slack channel | Juanje | End of Q3 | AI summary PoC depends on this channel existing |
| SKU/CDN/errata knowledge doc | Kanitha, Gadi, Petr | End of Q3 | ATC distribution team needs this documented |
| Landing page | Luigi | End of Q3 | Avi's dashboard could integrate here |
