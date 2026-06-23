# Projects

Active and recent project context files. Read the relevant file when a project
comes up in conversation or needs context for a decision.

## Active

- **[RHIVOS 2.0 RC3](RHIVOS_2_0_release_RC3.md)** — RC3 release tracking: go/no-go Monday 2026-06-16, CTC schedule, blocker tickets, CVE dependencies. Read when RC3, RHIVOS release, or CTC testing comes up.
- [PitCrew strategic context](pitcrew-strategic-context.md) — Team mission, Q2 priorities, product direction
- [AIIL demo — RHAS](aiil-demo-rhas.md) — Michael Kuehl's AI-in-the-Loop demo for ELIV/CES27. Addresses PITCREW-290/293/294/291/396. Read when agentic platform, demo planning, or Roderick's onboarding comes up.
- [ATC LLM wiki](atc-llm-wiki.md) — Confluence-to-wiki build project
- [ATC Scrum Meetings](atc-scrum-meetings.md) — Recurring ATC ceremony notes (backlog refinement, sprint planning). Read when catching up on missed meetings or reviewing team decisions.
- **[RHIVOS AI Agents & Agentic SDLC](rhivos-ai-agents-agentic-sdlc.md)** — Landscape of AI agent initiatives across RHIVOS/Automotive: FoA validator workflow (Gadi/Rajesh), stateful process agent (Juanje/AAA), AIIL (Michael Kuehl). Design principles, memory architectures, safety patterns. From June 17 rollup demo.
- **[Agent Forge Design Principles](agent-forge-design-principles.md)** — Juanje Ojeda's 7 principles for stateful process-oriented agents. Deep study from agent-forge repo + slides. Convergence analysis with agentic-buddy, actionable gaps identified.
- **[Infrastructure Reliability Automation](infra-reliability-automation.md)** — AUTOBU-1085 / VROOM-41550. Juanje Ojeda's pipeline debugger agent: PoC done, production-ready phase in review, generalized into agent-forge. Next: defect triage integration, documentation.

- **[Core RPMs Redux](core-rpms-redux.md)** — VROOM-31017 epic: replacing "core RPMs" list with 4 machine-readable lists (Safety, Runtime, Image, Tools). Juanje's execopen pipeline work, toolchain integration (VROOM-31421). Read when core RPMs, execopen, toolchain packages, or RPM lists come up.
- **[RHIVOS QC Layered Product](rhivos-qc-layered-product.md)** — Distribution setup for the Qualcomm Layered Product: EngIDs, content sets, CDN paths, errata, product registration. Read when LP distribution, EngIDs, QC content sets, or CDN paths come up.
- **[RHAS Team](rhas-team.md)** — PitCrew product engineering: bringup agent, Jumpstarter, QC hardware enablement, RHAS releases. Read when RHAS, bringup agent, board bring-up, or PitCrew engineering work comes up.

- **[Quarterly Connection Agent](quarterly-connection-agent.md)** — Stateful process-oriented agent for quarterly evaluation reports. Applies agent-forge design principles to rebuild the [QC report CLI](https://gitlab.cee.redhat.com/aefrat/qc_report_agent) as a Claude Code skill with memory. Knowledge base at [qc-agent/](qc-agent/index.md).
- **[Manager Report Agent](manager-report-agent.md)** — Stateful agent wrapping the daily/weekly/weekend engineering status report script. Adds identity, memory, verification, and learning to the existing Python execution engine. Knowledge base at [mr-agent/](mr-agent/index.md).
- **[Project Pulse Agent](project-pulse-agent.md)** — Post-report intelligence layer. Cross-references manager report Slack data against active project files, proposes sourced updates. Runs after each manager report (interactive) or on demand.

## Background

- [PitCrew image mode future](pitcrew-image-mode-future-2026-05-27.md) — Image mode roadmap discussion (2026-05-27)
- [RHIVOS release approach](rhivos-release-approach.md) — General release process and gating
- [RHIVOS SKU/ProductID research](rhivos-sku-productid-research.md) — Product ID mapping research
