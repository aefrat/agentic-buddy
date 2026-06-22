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

## Open questions

- VROOM-44415 vs VROOM-44418 appear to be duplicates (both "documentation for Poe-based pipeline debugger").
- Defect triage agent (VROOM-44416) — which PoC version will be selected for deployment? (discussed Jun 16, decision pending)
- What's the relationship to VROOM-41482 (the consolidated defect triage ticket)?
