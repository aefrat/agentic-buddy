---
last_accessed: 2026-06-14
access_count: 1
created: 2026-06-14
---

# AIIL: Issue-to-Release with Closed-Loop HIL Verification

**Champion:** Michael Kuehl (Sr. Principal Ecosystem Architect — Automotive, mkuehl@redhat.com, Amsterdam/CEST)
**Targets:** ELIV (October 2026), CES27 (January 2027)
**Doc:** [Google Doc](https://docs.google.com/document/d/1G5SsFGhOUAz3pPuHJRLbelJXQp0XC0o4vwC57wr-RQM)
**Posted:** 2026-06-12 in #team-pitcrew-automotive (reply to Paul Wallrabe's telemetry thread)
**Working group forming:** Paul Wallrabe (coordinator), Roderick Kieley (PITCREW-291 owner, started Jun 11), Miguel Angel Ajo Pelayo (Jumpstarter telemetry), Michael Kuehl (vision/requirements)

## Concept

AI agent picks up a GitHub issue in vsomeip (COVESA automotive middleware), derives requirements/specs/tests, implements fix in sandbox (inner loop / SIL), then Konflux builds RPM + RHIVOS image and Jumpstarter runs test suite on virtual → physical hardware (outer loop / HIL). On failure, agent queries unified evidence store, forms hypothesis, re-enters inner loop. Iteration budget of 3-4, then human escalation.

### Evidence collection architecture

Three producers, three dialects:
- Agent harness → OTLP
- Konflux → Tekton Results + OCI attestations
- Jumpstarter (JEP-0013) → Prometheus/Loki

Unified via correlation contract:
- `image_digest` joins evidence plane (Quay, Tekton Results, signed)
- `run_id` + `lease_id` join telemetry plane (Prometheus, Loki, diagnostic)

Agent gets read-only access via MCP gateway with typed query tools. Same evidence serves agent debug loops and auditor trails ("Prove, Don't Trust").

### Stack

OpenShift, Konflux, RHAS, OpenShift Dev Spaces, GitHub (upstream + fork), Jumpstarter, Quay, Tekton Chains, Conforma, ambient-code (https://github.com/ambient-code), TI SK69 Jacinto (physical target), RPi4 (sidekick/exporter host).

## Epic alignment

| Epic | Title | Connection |
|---|---|---|
| PITCREW-290 | Agentic Platform | Full architecture for this epic |
| PITCREW-293 | Ask the Platform | Queryable evidence store via MCP gateway |
| PITCREW-294 | Autonomous Platform Reactions | Closed-loop remediation = this |
| PITCREW-291 | End-to-End Trace | Evidence collection architecture = this |
| PITCREW-396 | PitCrew AI | Foundational vision |
| PITCREW-335 | Konflux Onboarding | Hard dependency (build system) |

## Roderick Kieley's feedback (Jun 12, 6 comments)

1. Agent sandboxing — productized openshell not until OCP 5. Backport to 4.22+ unclear.
2. References **unbound-force** (Product Security, github.com/unbound-force) and **Full Send** (github.com/fullsend-ai/fullsend) as org-level agentic tools.
3. Product vs upstream: demo with productized trusted supply chain or upstream Sigstore?
4. MCP gateway: Grafana MCP server (github.com/grafana/mcp-grafana) vs custom, plus openshift-mcp-server already has OSSM/Tekton integrations.
5. Downstream fork location — GitHub?
6. Links a divestiture doc re: Full Send as current org direction.

## Dependencies / risks

- **JEP-0013 not implemented** — telemetry is a hard dependency, not optional. Paul Wallrabe asked about status same day (Jun 12).
- **OCP 5 for agent sandboxing** — may not be available for October demo.
- **Konflux RHIVOS image builds** — in progress via PITCREW-335, not yet proven.
- **MCP gateway** — not started, needs design decision (existing vs custom).
- **October is 4 months out** — ambitious timeline.

## Status

- 2026-06-12: Paul Wallrabe raised telemetry gap in #team-pitcrew-automotive thread
- 2026-06-12: Roderick replied he started PITCREW-291 (End-to-End Trace) "yesterday" (Jun 11)
- 2026-06-12: Paul asked Michael to specify demo requirements
- 2026-06-12: Michael posted AIIL concept + full spec doc (4.5h after Paul's ask)
- 2026-06-12: Roderick engaged with 6 substantive comments on the Google Doc
- 2026-06-13: Michael confirmed he'll refine further next week, expects changes/clarifications
- No Jira ticket yet for the demo itself (tracked under PITCREW-290 umbrella)

## People

- **Michael Kuehl** — Sr. Principal Ecosystem Architect, Automotive. Amsterdam/CEST. Low-volume Slack (4 msgs since May 1), high impact. Also in #hyundai-esp-1year-q2-may29 (Hyundai engagement). No email contact with Avi in last 30 days.
- **Roderick Kieley** — 2 weeks into onboarding (started Jun 1). Already self-assigned PITCREW-291 and engaged deeply with AIIL doc. 1:1 with Avi still unscheduled.
- **Paul Wallrabe** — Initiated the thread. Coordinating between Michael's vision and team's telemetry readiness.
- **Miguel Angel Ajo Pelayo** — Jumpstarter lead. Confirmed JEP-0013 not implemented in Jumpstarter, proposed exporter-based approach for device telemetry.
