---
last_accessed: 2026-06-22
access_count: 12
created: 2026-06-01
---

# System observations

Raw observations detected during `/reflect`. Each entry tracks how many times
a pattern has been seen. The `/daily` cycle reviews this file and acts on
observations with 2+ occurrences (creating skills, proposing rules, etc.).
Resolved observations are moved to the bottom.

---

## Skill candidates

- **2026-06-10:** "Build LLM wiki from Confluence page" — fetch Confluence pages via v2 API (parent + children), convert HTML→markdown, scaffold Karpathy-style wiki with CLAUDE.md schema, run INGEST in rounds (concepts → workflows → processes → enrichment → onboarding), LINT, verify. Parameterizable by Confluence page ID and wiki domain. Used for RHIVOS workflows wiki. (seen: 1)
- ~~**2026-06-11:** "Scan Slack channel and generate project update"~~ → **resolved 2026-06-14:** created skill `agent_brain/skills/scan-slack-channel.md` (seen 3x, adapted to use Slack MCP tools per Rule 18)
- **2026-06-11:** "Search Confluence for topic research" — use Confluence REST API (`wiki/rest/api/search?cql=...`) with .netrc auth to search across spaces, read full page content, extract and synthesize findings. Used to research OSCI CI Mediator across RHELPLAN, IVOS, and Red Hat Catalog spaces. Reusable for any Confluence research request. (seen: 1)
- **2026-06-14:** "Check Slack activity inbox" — pull user's mentions and DMs, identify action items needing response, generate summary table. Complementary to channel scanning — channels show team activity, inbox shows what needs the user's attention. (seen: 1)
- **2026-06-22:** "Person Slack activity lookup" — search all messages by a specific person across a time range. Steps: search API (`from:<username>`) → extract user ID → scan team channels with `conversations.history` + `oldest=` → check thread replies → check DMs. Distinct from channel scanning and inbox check. (seen: 1)
  - 2026-06-22: seen again — extended with @mention search (`<@USER_ID>`), prior-week baseline comparison, and multi-person batch mode (5 people in one session). Also productionized: added `STAKEHOLDERS` config + `render_stakeholder_slack_section()` to `generate_report.py`. (seen: 2)

## Rule candidates

- **2026-06-11:** Use existing skills/tools for external services (Jira, Slack, Gmail, etc.) instead of raw API calls. User corrected 3x in one day: Jira curl, Slack MCP OAuth, Jira user search curl. (seen: 3) → **fast-tracked to CLAUDE.md Rule 18**
- **2026-06-11:** Before querying external systems, check if the data is already available in loaded context (files, earlier tool results). Only fetch what's genuinely missing. User stopped a redundant Jira fetch when data was already in the weekly report + prior query. (seen: 1)

- **2026-06-16:** Don't assume gender from names — use neutral pronouns or ask when unsure. User corrected assumption about Sameera Kalgudi (male, not female). Explicit user correction. (seen: 1)

## Concept candidates

- **2026-06-10:** Confluence attachment downloads use different auth than API calls. The v2 pages API works with basic auth (.netrc), but `/download/attachments/` returns 401. May need cookie-based session or different token scope. (seen: 1)
- ~~**2026-06-11:** Cross-referencing Slack discussions against documented processes~~ → **resolved 2026-06-18:** created concept `agent_brain/concepts/cross-referencing-slack-vs-docs.md` (seen 3x)
- **2026-06-11:** CI pipeline YAML files (`.gitlab-ci.yml`, stage includes, rules) are often the most authoritative source for understanding system architecture — more so than wikis or DETAILED.md docs. The Gator command orchestration (independent triggers vs sequential pipeline) was fully answered by reading `.gitlab/rules.yml` and the stage YAMLs, while DETAILED.md only showed the DPAC→Gator cross-project trigger. Pattern: "read the CI config to understand how components interact at runtime." (seen: 1)
- ~~**2026-06-11:** Confluence REST API patterns~~ → **resolved 2026-06-18:** created concept `agent_brain/concepts/confluence-api-patterns.md` (seen 3x)

- **2026-06-14:** Slack thread context reveals working-group formation patterns invisible from standalone messages. Michael Kuehl's AIIL doc appeared as a standalone vision post — but the thread showed it was a direct response to Paul's coordination ask, with Roderick already self-assigning PITCREW-291 and Miguel confirming Jumpstarter telemetry gaps. Pattern: "always read the parent thread, not just the broadcast message — the thread reveals who's coordinating, who's already working, and what triggered the initiative." (seen: 1)

- **2026-06-14:** PLM/ComposeDB auto-generates debuginfo listings from parent builds in Brew, regardless of compose tree contents. Known RHEL-wide issue (8+ prior occurrences per RHELWF-11979). Verified via Brew API: both RHEL 9 and RHEL 10 binutils produce `cross-binutils-{ppc64le,s390x}-debuginfo`. PLM for RHIVOS 1.x (`9Base-RHIVOS-1.0.0`) has the same ghost entries as RHIVOS 2.0 — they were never noticed until Kanitha checked 2.0's errata advisory builds. Pattern: "PLM infers RPM existence from Brew builds, not from compose trees — phantom packages appear in product listings that were never in any compose." Workaround: PLM overrides per package. Systemic fix: Kanitha's proposed delete-and-reimport. Tracked in RHELWF-14266. (seen: 1)

- **2026-06-14:** RHIVOS process gaps often trace back to missing tooling, not just missing documentation. The pre-`-gate` tagging gap exists because RHEL's build system auto-tags into `-gate` and side-tags use centpkg/Distrobaker/Jenkins — RHIVOS has none of this, so the equivalent is manual undocumented work. The developer-guide's RHIVOS maintenance section is literally a stub. Pattern: "when a process gap is found, check whether the upstream/parent product (RHEL) has automation that makes the process self-documenting — if RHIVOS lacks that automation, the gap is structural, not just a documentation oversight." (seen: 1)

- **2026-06-14:** Brew hub_policy.conf (`brew-confs` GitLab repo) is the authoritative source for all Brew tagging permissions — more authoritative than any Confluence wiki page (RCMDOC, EXDSPRHELB). Wikis document the general permission model (permission types, how to set/grant them); the policy file has the actual product-specific rules (RHIVOS: `rhivos-tagger` RHELBLD-12926, `pkglist-rhivos` RHELBLD-12234, `auto-toolchain-service-brew` RHELBLD-17225). The `-gate` tag isn't even in the standard RCM tagging structure — it was added for RHEL 9+ gating. Pattern: "for permission/policy questions about Brew, always check the raw hub_policy.conf first — wikis describe the framework, the policy file has the actual rules." (seen: 1)

- **2026-06-18:** Three complementary AI agent archetypes emerging in RHIVOS org — (1) SDLC automation (Gadi: Jira→MR), (2) process/diagnostic (Juanje: pipeline debugging), (3) outer-loop orchestration (Michael: issue→release→HIL). Each has different model requirements, safety models, and memory needs. Could generalize into a classification framework. (seen: 1)
- **2026-06-18:** Juanje Ojeda's agent design principles (character over rules, progressive disclosure, 4-store memory architecture, constraints shape behavior) closely mirror agentic-buddy's design (SOUL.md character, progressive disclosure, file-based memory with metadata). Independent convergence on similar patterns — worth tracking as potential org-wide standard. (seen: 1)
- **2026-06-21:** "Agent-as-wrapper" pattern — wrapping an existing stateless script with agent harness (identity, memory, verification, learning) without rewriting the execution engine. The script handles data fetching/formatting; the agent adds context, comparison, and accumulation. Applied to manager report (`generate_report.py` stays, agent wraps with 4-store memory + disconfirmation gates). Generalizable to any existing automation that works but doesn't learn. (seen: 1)
- **2026-06-21:** "Shared config, additive extension" — when two agents need overlapping team data, extend the existing config file with new fields rather than duplicating. Each agent ignores fields it doesn't use. Prevents config drift. Applied: QC agent's `members.yaml` extended with `accent_color` and `google_docs` for the manager report agent. (seen: 1)
- **2026-06-21:** Google Docs `replaceAllText` uses substring matching — "Software Engineer" matches inside "Senior Software Engineer". When doing targeted text replacements, qualify with surrounding context (e.g., `"Name | Title"`) to prevent double-prefixing. Tested: no garbling occurred in this batch because title strings appeared only once per doc in non-overlapping positions. (seen: 1)
- **2026-06-21:** "Behavioral evidence vs deliverable evidence" — when evaluating how someone works (behaviors), Slack interaction patterns (tone, helpfulness, thread participation, cross-team engagement) are better evidence than ticket/MR metrics. Deliverable-based behavioral claims are unfalsifiable and interchangeable between people. Applied: QC Section B methodology rewrite from deliverable-based to Slack-behavioral. (seen: 1)
- **2026-06-21:** "Accumulation mechanism for periodic reports" — daily/weekly reports should extract and accumulate signals into a dedicated file for quarterly consumption. Applied: manager report → `multiplier-observations.md` → quarterly QC Section B. Pattern: "frequent captures → accumulation file → periodic synthesis." (seen: 1)
- **2026-06-22:** Slack search API `after:YYYY-MM-DD` date filter returns 0 results with xoxc tokens even when messages exist. Workaround: omit date filter, post-filter by timestamp in code. The `conversations.history` API `oldest=` unix timestamp works correctly. (seen: 1)
- **2026-06-22:** "Stakeholder visibility in team reports" — adding non-team-member activity tracking to automated reports fills the gap of cross-team context that affects the team's work. AI-synthesized digest keeps it low-noise. Pattern: "track the people who influence your team's work, not just the people who do it." (seen: 1)
- **2026-06-22:** "AI policy compliance checklist for internal agent tools" — when evaluating whether an AI tool/harness is compliant, check: (1) license (Red Hat Approved Open Source?), (2) execution environment (local/approved infra?), (3) model provider (approved?), (4) data classification (personal/confidential/customer?), (5) human review of output (required by policy). Applied to Pi harness analysis for pipeline debugger. Generalizable to any team building with open-source AI tools. (seen: 1)
- **2026-06-22:** "Production use evidence from Slack" — structured diagnosis posts in team channels are strong evidence that an AI agent has moved beyond PoC to genuine operational use. The diagnosis format (summary → failed jobs → root cause → resolution → context → recommendations) and cross-incident reasoning (e.g., tracing lease starvation to a cleanup crash 2 days earlier) demonstrate production-grade quality beyond what metrics like "148 tests, 84% coverage" show. (seen: 1)
- **2026-06-22:** "Upstream vs downstream CI boundary" — ATC codebase docs correctly stop at external dependency boundaries. AIB's CI infrastructure (Duffy/CentOS CI) is invisible from ATC's docs because ATC consumes AIB as a pre-built tool via Testing Farm. Questions about upstream CI require going directly to the upstream source (AIB `.gitlab-ci.yml`). Pattern: documentation covers what you own and consume, but the CI of your dependencies is their concern. Relevant for onboarding (where does ATC's responsibility end vs CentOS Automotive SIG's?). (seen: 1)

## Structure candidates

- **2026-06-14:** Skill format migration — user has skills in two locations: old format (`agent_brain/skills/*.md`) and new agentskills.io format (`.claude/skills/<name>/SKILL.md`). User explicitly stated all new skills should use agentskills.io format. GitLab collection uses `.agents/skills/`. Consider migrating remaining old-format skills to `.claude/skills/` during a maintenance cycle and archiving the old files. (seen: 1)
  - 2026-06-18: Second new skill (`process-1on1s`) built in agentskills.io format. Pattern is now established — all new skills go to `.claude/skills/`. (seen: 2)

## Structure candidates (tools)

- ~~**2026-06-21:** `manager-report/` directory is not a git repo~~ → **resolved 2026-06-21:** initialized git, pushed to `gitlab.cee.redhat.com:aefrat/manager-report` with .gitignore excluding secrets

## Reference candidates

- **2026-06-15:** Rover MCP server (`https://github.com/redhat-community-ai-tools/rover-mcp`) — queries Red Hat internal groups API via client certificate auth. Currently only has `rover_group` tool (no people/profile lookups). Requires `sa-cert.crt` + `privkey.pem` (not present on user's machine). Not viable without certificate provisioning from Red Hat IAM team. Could be extended with a `rover_people` tool for username resolution. (seen: 1)

## Resolved

- **2026-06-10:** Rule — "After plan approval, execute autonomously without confirmation prompts." Explicit user correction (3x in one session). Fast-tracked to memory as `feedback_autonomous-execution.md`.
