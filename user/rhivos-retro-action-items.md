# RHIVOS 2.0 Retro - Avi's Action Items

From the [RHIVOS 2.0 Retro](https://docs.google.com/document/d/17q7g2rd3-JvBy7jHn3Py85fqAPmYvN0Wwxe-uNIs7FI/edit) meeting (2026-07-30).
Full analysis and meeting notes at `agent_brain/projects/rhivos-2.0-retro.md`.

## Directly assigned to Avi

### 1. AI-powered release blocker summary (PoC)

- **What:** Build a PoC that uses AI to scan the release technical Slack channel and produce clear blocker status summaries for the release readiness channel.
- **Deadline:** End of August 2026
- **Approach:** Local PoC using existing RH-wide Slack MCP (no AIA/PIA needed). Already have working Slack MCP integration in agentic-buddy. Can extend scan-slack-channels skill or build a dedicated release-status skill.
- **Notes from doc comments:** Petr raised PIA concern for AI+Slack. Avi clarified: RH-wide Slack MCP from DOL is already available and in use. PoC runs locally.
- **Stretch:** Combine with Luigi's dashboard idea - feed AI summary into a static HTML dashboard (same URL per release).
- [ ] Design the skill/agent (what channels to scan, what format to output, cadence)
- [ ] Build PoC
- [ ] Demo to Dana/team
- **Status:** Not started

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
