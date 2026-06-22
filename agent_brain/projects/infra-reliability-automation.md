---
last_accessed: 2026-06-22
access_count: 1
created: 2026-06-22
---

# Infrastructure Reliability Automation

**Jira:** [AUTOBU-1085](https://redhat.atlassian.net/browse/AUTOBU-1085) (Initiative) → [VROOM-41550](https://redhat.atlassian.net/browse/VROOM-41550) (Epic)
**Owner:** Juanje Ojeda (execution), Allison King (reporter/PM)
**Status:** Epic In Progress (5912 SP total)
**Related:** [rhivos-ai-agents-agentic-sdlc.md](rhivos-ai-agents-agentic-sdlc.md) (Initiative #2 — Juanje's stateful agent design)

## What it is

AI agents for infrastructure health, pipeline failure monitoring, diagnostics, and automated remediation. Started as a PoC pipeline debugger, now evolving into a production-ready tool with generalized patterns.

**Core repo:** https://gitlab.cee.redhat.com/automotive/ai/agents/toolchain/pipelines-debugger
**Agent harness:** [Pi](https://github.com/AshkanArabim/pi) (minimal extensible agent harness, model-agnostic)
**Meta-agent:** [agent-forge](https://gitlab.cee.redhat.com/automotive/ai/agents/common/agent-forge) — bootstrapping and quality review for new agents

## Child tickets

| Key | Summary | Status | Assignee | Notes |
|-----|---------|--------|----------|-------|
| VROOM-41536 | PoC: Infra AI agent for pipeline failure diagnostics | **Closed** (Done) | Juanje | Completed May 27. Demoed: file-based memory, incident tracking, Slack integration. Already used by Toolchain team. |
| VROOM-41808 | Make PoC production ready | **Review** | Juanje | Migrated to Pi harness. Permission model, consolidation tooling, 148 tests (84% coverage). Tiered roadmap: T1 production-ready (KB routing, CBS health checks), T2 quality (KB refresh, session hooks), T3 autonomous (Jira/Slack/pipeline re-trigger). |
| VROOM-44368 | Generalize pipeline debugger for guardrails | **Closed** (Done) | Juanje | Resulted in agent-forge meta-agent (Jun 18). |
| VROOM-44415 | Documentation for Poe-based pipeline debugger | **New** | Unassigned | Post-migration docs for team onboarding. |
| VROOM-44416 | Integrate defect triage agent with CI/CD pipeline | **New** | Unassigned | Auto-trigger on test failures instead of manual invocation. |
| VROOM-44418 | Documentation for using the Poe-based pipeline debugger | **New** | Unassigned | Duplicate of 44415? Both are sprint review items, nearly identical descriptions. |

## Key activity (from comments)

- **Jun 16:** Team agreed to close 5 duplicate tickets, consolidate into one defect triage agent implementation (VROOM-41482). Ian McLeod noted they need to select a finalized PoC version to deploy for auto-commenting on inbound defects.
- **Jun 10–11:** Juanje bootstrapping/polishing cycle — fresh bootstrapping with improved approach to understand agent behavior better. Migrated to Pi for security + token efficiency.
- **Jun 10:** Generalization task created — extract patterns from pipeline debugger into reusable guardrails framework.
- **May 27:** PoC demo and close. Agent already in production use by Toolchain team.

## Architecture highlights (from VROOM-41808)

- **9 CLI tools, 7 skills, 148 tests** (84% coverage)
- **Permission model:** config-driven (`permissions.json`), read/write split, skill-scoped tool access, secret redaction in logs
- **Consolidation tooling:** `bin/find-uncaptured` (triage-based incident cross-referencing) + `bin/validate-ki` (known-issues structural health checks)
- **Pi permission gate:** https://www.npmjs.com/package/pi-permission-gate

## Related: Defect Triage Agent (VROOM-41482)

Separate epic under same umbrella, owned by **Ian McLeod**. AI-powered defect triage with auto-generated investigation comments on inbound bugs.

**Status:** In Progress. Basic pipeline shell done (VROOM-41483, Verified). MVP comment generation in progress (VROOM-41484, Ian McLeod).

**Children (9 tasks):**
| Key | Summary | Status | Assignee |
|-----|---------|--------|----------|
| VROOM-41483 | Basic defect triage agent pipeline shell | **Verified** (Done) | Ian McLeod |
| VROOM-41484 | MVP comment functionality | **In Progress** | Ian McLeod |
| VROOM-44412 | Integrate defect triage agent with CI/CD pipeline | New | — |
| VROOM-44413 | Support multiple test frameworks | New | — |
| VROOM-44414 | Optimize token usage in bootstrapping sessions | New | — |
| VROOM-44417 | Support for analyzing flaky tests | New | — |
| VROOM-44419 | Complete remaining bootstrapping sessions for full codebase coverage | New | — |
| VROOM-44489 | Review/validate generated KB from bootstrapped defect triage data | New | Ian McLeod |
| VROOM-44490 | Strict write protection for operational vs consolidation modes | New | — |

**Jun 16 consolidation:** 5 duplicate tickets (40958, 4112, 41113, 41114, 41115) closed in favor of 41482. Team needs to select finalized PoC for deployment. Juanje plans a QE agent PoC using same patterns.

**Cross-pollination:** Juanje's pipeline debugger patterns (Pi harness, agent-forge) are being adopted for the defect triage agent. The convergence point is agent-forge as the shared bootstrapping framework.

## Slack evidence — agent in production (Jun 8–22)

The pipeline debugger agent is **actively generating structured diagnosis reports** and posting them to **#alerts-auto-toolchain**. Juanje had 66 messages across 8 channels in this period (23 in alerts-auto-toolchain alone).

**Diagnosis posts (agent-generated, posted by Juanje):**
- **Jun 16 01:42** — ODCS unsigned packages (RHIVOS-2.0-Core nightly). Agent identified missing kernel signatures on 3 packages, linked to recurring pattern from Jun 3 incident, escalated.
- **Jun 16–17** — Jumpstarter board timeouts (both RHIVOS-2.0 and 2.0-Core). Agent root-caused to recoveryinfo partition slot-trapping on Snapdragon Ride4 boards, recommended `dd` wipe, escalated to PitCrew.
- **Jun 20** — Jumpstarter lease starvation. Agent traced all 7 exporters occupied to a Python 3.14 TMT cleanup crash leaking leases from Jun 18-19 failures. Recommended lease pool audit.

**Agent cross-references in conversation:**
- Jun 15 (gating channel): "I analysed with my agent (which has context for the error and the project) and it doesn't seem to be necessary" — used the agent for Gator MR analysis.
- Jun 18: Follow-up on agent diagnosis — asked team about force-promoting nightlies since smoke tests passed despite pipeline failures.

**Other activity:**
- Shared agentic-buddy framework updates (DMs, Jun 11 & 15).
- Shared Ian McLeod's FuSa agent demo recording (Jun 10) — built on Juanje's patterns.
- RC3 release coordination (Jun 15) and Gator MR contributions (Jun 15–16).

## Open questions

- VROOM-44415 vs VROOM-44418 appear to be duplicates (both "documentation for Poe-based pipeline debugger").
- Which PoC version gets deployed for defect triage auto-commenting? (discussed Jun 16, decision pending — Ian McLeod leading selection)
- Juanje mentioned a QE agent PoC — is that a new ticket or covered under existing defect triage work?

## AI policy compliance (Jun 22 analysis)

**Pi harness:** MIT-licensed, runs locally — qualifies under Red Hat's **Open Source AI Technologies** blanket approval (no separate AI Assessment needed). Not explicitly listed on the Approved AI Tools page, but covered by the general clause.

**Model provider:** Gemini API — separately approved for code assistant use cases. Anthropic/Claude also approved (Claude Code).

**Conditions from the policy (both must be met):**
1. *"No personal, confidential, customer/partner, or third-party proprietary data"* — **Needs verification.** The pipeline debugger ingests internal CI/CD pipeline logs (gitlab.cee), GitLab artifacts, Testing Farm results, and Slack messages from internal channels. Whether internal CI pipeline logs and infra data qualify as "confidential" under this policy is ambiguous. **Action: confirm with Velocity AI team** (via Red Hat Hub or #help-rh-code-assist) that internal pipeline/CI data is acceptable input for open source AI tools.
2. *"Review, validate, and test all output"* — **Met.** Agent runs in human-assisted mode. Juanje reviews every diagnosis before posting to #alerts-auto-toolchain. No autonomous posting yet (Tier 3 roadmap).

**Risk if the team moves to Tier 3 (autonomous mode):** Condition (2) would no longer be met if the agent posts diagnoses without human review. That would likely require an AI Assessment (AIA) submission.
