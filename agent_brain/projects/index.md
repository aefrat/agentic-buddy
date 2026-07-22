# Projects

Active and recent project context files. Read the relevant file when a project
comes up in conversation or needs context for a decision.

## Active

- **[RHIVOS 2.0 RC3](RHIVOS_2_0_release_RC3.md)** — RC3 release tracking: composes published Jun 16, CTC at 93% (3 tickets remaining), errata at REL_PREP. Read when RC3, RHIVOS release, or CTC testing comes up.
- [PitCrew strategic context](pitcrew-strategic-context.md) — Team mission, Q2 priorities, product direction
- [AIIL demo — RHAS](aiil-demo-rhas.md) — Michael Kuehl's AI-in-the-Loop demo for ELIV/CES27. Addresses PITCREW-290/293/294/291/396. Read when agentic platform, demo planning, or Roderick's onboarding comes up.
- [ATC LLM wiki](atc-llm-wiki.md) — Confluence-to-wiki build project
- [ATC Scrum Meetings](atc-scrum-meetings.md) — Recurring ATC ceremony notes (backlog refinement, sprint planning). Read when catching up on missed meetings or reviewing team decisions.
- **[RHIVOS AI Agents & Agentic SDLC](rhivos-ai-agents-agentic-sdlc.md)** — Landscape of AI agent initiatives across RHIVOS/Automotive: FoA validator workflow (Gadi/Rajesh), stateful process agent (Juanje/AAA), AIIL (Michael Kuehl). Design principles, memory architectures, safety patterns. From June 17 rollup demo.
- **[Agent Forge Design Principles](agent-forge-design-principles.md)** — Juanje Ojeda's 7 principles for stateful process-oriented agents. Deep study from agent-forge repo + slides. Convergence analysis with agentic-buddy, actionable gaps identified.
- **[Infrastructure Reliability Automation](infra-reliability-automation.md)** — AUTOBU-1085 / VROOM-41550. Juanje Ojeda's pipeline debugger agent: PoC done, production-ready phase in review, generalized into agent-forge. Next: defect triage integration, documentation.

- **[RHIVOS Dist-Git Workflow](rhivos-distgit-workflow.md)** — Dist-git policy inconsistencies and undocumented kernel derivative rebuild workflow (downstream-dtbs, qcom-scmi, kernel-ivos-nxp-extra-modules). contyk's clarifications on policy exceptions, ticket requirements, branch model. Alignment meeting + documentation effort pending. Read when dist-git policy, kernel derivative rebuilds, Brew tagging, or errata ticket workflow comes up.
- **[Core RPMs Redux](core-rpms-redux.md)** — VROOM-31017 epic: replacing "core RPMs" list with 4 machine-readable lists (Safety, Runtime, Image, Tools). Juanje's execopen pipeline work, toolchain integration (VROOM-31421). Read when core RPMs, execopen, toolchain packages, or RPM lists come up.
- **[RHIVOS QC Layered Product](rhivos-qc-layered-product.md)** — Distribution setup for the Qualcomm Layered Product: EngIDs, content sets, CDN paths, errata, product registration. Decision: single LP with all components (Jul 14). Read when LP distribution, EngIDs, QC content sets, or CDN paths come up.
- **[RHIVOS on GitLab](rhivos-on-gitlab.md)** — AUTOBU-1105. Infrastructure enablement to transition RHIVOS to GitLab (MR workflows, draft builds, auditability, Conflux dependency). Same pattern as RHEL on GitLab. Read when GitLab migration, MR workflows, package gating replacement, or Conflux integration comes up.
- **[RHIVOS Release Tagging](rhivos-release-tagging.md)** — Knowledge bottleneck: only Petr and Ozan know how to tag RHIVOS release packages with the correct RHEL inheritance flag. Documentation sharing needed. Read when tagging, inheritance, RHEL/RHIVOS package relationship comes up.
- **[RHIVOS Jira Workflows](rhivos-jira-workflows/index.md)** — LLM-queryable knowledge base for RHIVOS Jira workflows. Covers AUTOBU/VROOM projects, Feature/Initiative/Product/Task workflows with states and field requirements, issue type mapping, kernel component decision tree, RHEL mirroring automations, milestones, FAQ. Read when any Jira workflow question comes up.
- **[RHAS Team](rhas-team.md)** — PitCrew product engineering: bringup agent, Jumpstarter, QC hardware enablement, RHAS releases. Read when RHAS, bringup agent, board bring-up, or PitCrew engineering work comes up.

- **[Quarterly Connection Agent](quarterly-connection-agent.md)** — Stateful process-oriented agent for quarterly evaluation reports. Applies agent-forge design principles to rebuild the [QC report CLI](https://gitlab.cee.redhat.com/aefrat/qc_report_agent) as a Claude Code skill with memory. Knowledge base at [qc-agent/](qc-agent/index.md).
- **[Manager Report Agent](manager-report-agent.md)** — Stateful agent wrapping the daily/weekly/weekend engineering status report script. Adds identity, memory, verification, and learning to the existing Python execution engine. Knowledge base at [mr-agent/](mr-agent/index.md).
- **[Project Pulse Agent](project-pulse-agent.md)** — Post-report intelligence layer. Cross-references manager report Slack data against active project files, proposes sourced updates. Runs after each manager report (interactive) or on demand.
- **[Team Priorities](team-priorities.md)** — ATC and PitCrew/RHAS Q3 2026 priorities + RHIVOS program priorities. Used by talent-development and manager report skills.
- **[RHAS Testing Ownership](rhas-testing-ownership/index.md)** — Testing ownership establishment for RHAS Tech Preview/GA. Candidate qualifications, features requiring testing, testing landscape report.

## Background

- [PitCrew image mode future](pitcrew-image-mode-future-2026-05-27.md) — Image mode roadmap discussion (2026-05-27)
- [RHIVOS release approach](rhivos-release-approach.md) — General release process and gating
- [RHIVOS SKU/ProductID research](rhivos-sku-productid-research.md) — Product ID mapping research
- [Claude tips - autonomous Opus](claude-tips-autonomous-opus.md) — Boris Cherny's tips for autonomous Claude Code usage (reference, single access)
