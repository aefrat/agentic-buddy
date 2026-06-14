---
last_accessed: 2026-06-14
access_count: 7
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

## Rule candidates

- **2026-06-11:** Use existing skills/tools for external services (Jira, Slack, Gmail, etc.) instead of raw API calls. User corrected 3x in one day: Jira curl, Slack MCP OAuth, Jira user search curl. (seen: 3) → **fast-tracked to CLAUDE.md Rule 18**
- **2026-06-11:** Before querying external systems, check if the data is already available in loaded context (files, earlier tool results). Only fetch what's genuinely missing. User stopped a redundant Jira fetch when data was already in the weekly report + prior query. (seen: 1)

## Concept candidates

- **2026-06-10:** Confluence attachment downloads use different auth than API calls. The v2 pages API works with basic auth (.netrc), but `/download/attachments/` returns 401. May need cookie-based session or different token scope. (seen: 1)
- **2026-06-11:** Cross-referencing Slack discussions against documented processes (wikis/repos) reveals process gaps. The RHIVOS tagging ownership gap was only visible because Slack showed ad-hoc behavior (Francisco/Ozan doing it manually) while the wiki showed automation (Gator handles promotion). Pattern: "compare what people do (Slack) with what's documented (wiki) to find process gaps." (seen: 3)
  - 2026-06-14: Confirmed via full 3-repo documentation audit. Eric Chanudet's Slack escalation revealed 6 undocumented gaps — all invisible from repo documentation alone.
  - 2026-06-14: Confirmed again via Confluence deep dive (25+ pages under Auto Toolchain + Release Management). The "RHEL & RHIVOS gating process" page acknowledges manual tagging during blocker phase but assigns no owner. Authoritative wiki confirms repo-level audit findings. Pattern also works across documentation layers (git repos + Confluence + Slack).
- **2026-06-11:** CI pipeline YAML files (`.gitlab-ci.yml`, stage includes, rules) are often the most authoritative source for understanding system architecture — more so than wikis or DETAILED.md docs. The Gator command orchestration (independent triggers vs sequential pipeline) was fully answered by reading `.gitlab/rules.yml` and the stage YAMLs, while DETAILED.md only showed the DPAC→Gator cross-project trigger. Pattern: "read the CI config to understand how components interact at runtime." (seen: 1)
- **2026-06-11:** Confluence REST API (`wiki/rest/api/search?cql=...` + `wiki/rest/api/content/{id}?expand=body.storage`) works with .netrc basic auth, same credentials as Jira. Can search across spaces by CQL, read full page HTML, extract text. Used to research OSCI CI Mediator across RHELPLAN, IVOS, and Red Hat Catalog spaces. (seen: 2)
  - 2026-06-14: Used `?expand=body.storage,children.page` to traverse full page trees (25+ pages under Auto Toolchain + Release Management). Pattern: fetch parent with children, read each child body, recurse. Effective for exhaustive wiki audits.
  - 2026-06-14: Searched RCMDOC and EXDSPRHELB spaces for Brew tagging permissions. CQL queries with `text~"keyword"` + `space=RCMDOC` work well for targeted searches. Cross-space searches (no space filter) useful for finding canonical pages across the org (e.g. "Permissions in Brew" lives in EXDSPRHELB, not RCMDOC). (seen: 3)

- **2026-06-14:** Slack thread context reveals working-group formation patterns invisible from standalone messages. Michael Kuehl's AIIL doc appeared as a standalone vision post — but the thread showed it was a direct response to Paul's coordination ask, with Roderick already self-assigning PITCREW-291 and Miguel confirming Jumpstarter telemetry gaps. Pattern: "always read the parent thread, not just the broadcast message — the thread reveals who's coordinating, who's already working, and what triggered the initiative." (seen: 1)

- **2026-06-14:** PLM/ComposeDB auto-generates debuginfo listings from parent builds in Brew, regardless of compose tree contents. Known RHEL-wide issue (8+ prior occurrences per RHELWF-11979). Verified via Brew API: both RHEL 9 and RHEL 10 binutils produce `cross-binutils-{ppc64le,s390x}-debuginfo`. PLM for RHIVOS 1.x (`9Base-RHIVOS-1.0.0`) has the same ghost entries as RHIVOS 2.0 — they were never noticed until Kanitha checked 2.0's errata advisory builds. Pattern: "PLM infers RPM existence from Brew builds, not from compose trees — phantom packages appear in product listings that were never in any compose." Workaround: PLM overrides per package. Systemic fix: Kanitha's proposed delete-and-reimport. Tracked in RHELWF-14266. (seen: 1)

- **2026-06-14:** RHIVOS process gaps often trace back to missing tooling, not just missing documentation. The pre-`-gate` tagging gap exists because RHEL's build system auto-tags into `-gate` and side-tags use centpkg/Distrobaker/Jenkins — RHIVOS has none of this, so the equivalent is manual undocumented work. The developer-guide's RHIVOS maintenance section is literally a stub. Pattern: "when a process gap is found, check whether the upstream/parent product (RHEL) has automation that makes the process self-documenting — if RHIVOS lacks that automation, the gap is structural, not just a documentation oversight." (seen: 1)

- **2026-06-14:** Brew hub_policy.conf (`brew-confs` GitLab repo) is the authoritative source for all Brew tagging permissions — more authoritative than any Confluence wiki page (RCMDOC, EXDSPRHELB). Wikis document the general permission model (permission types, how to set/grant them); the policy file has the actual product-specific rules (RHIVOS: `rhivos-tagger` RHELBLD-12926, `pkglist-rhivos` RHELBLD-12234, `auto-toolchain-service-brew` RHELBLD-17225). The `-gate` tag isn't even in the standard RCM tagging structure — it was added for RHEL 9+ gating. Pattern: "for permission/policy questions about Brew, always check the raw hub_policy.conf first — wikis describe the framework, the policy file has the actual rules." (seen: 1)

## Structure candidates

- **2026-06-14:** Skill format migration — user has skills in two locations: old format (`agent_brain/skills/*.md`) and new agentskills.io format (`.claude/skills/<name>/SKILL.md`). User explicitly stated all new skills should use agentskills.io format. GitLab collection uses `.agents/skills/`. Consider migrating remaining old-format skills to `.claude/skills/` during a maintenance cycle and archiving the old files. (seen: 1)

## Resolved

- **2026-06-10:** Rule — "After plan approval, execute autonomously without confirmation prompts." Explicit user correction (3x in one session). Fast-tracked to memory as `feedback_autonomous-execution.md`.
