---
last_accessed: 2026-06-11
access_count: 5
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
- **2026-06-11:** "Scan Slack channel and generate project update" — source tokens from crontab, fetch via Slack API (conversations.history + conversations.replies + users.info), resolve @mentions, summarize key threads, cross-reference with project repos (ATC_Team_codebase_docs, errata-distribution, rhivos-workflows-wiki), generate actionable project file with resolution plans. Reusable for any team channel. (seen: 1)
  - 2026-06-11: seen again — Avi asked to re-scan same channel for updates. Same method, incremental scan. (seen: 2)
- **2026-06-11:** "Search Confluence for topic research" — use Confluence REST API (`wiki/rest/api/search?cql=...`) with .netrc auth to search across spaces, read full page content, extract and synthesize findings. Used to research OSCI CI Mediator across RHELPLAN, IVOS, and Red Hat Catalog spaces. Reusable for any Confluence research request. (seen: 1)

## Rule candidates

- **2026-06-11:** Use existing skills/tools for external services (Jira, Slack, Gmail, etc.) instead of raw API calls. User corrected 3x in one day: Jira curl, Slack MCP OAuth, Jira user search curl. (seen: 3) → **fast-tracked to CLAUDE.md Rule 18**
- **2026-06-11:** Before querying external systems, check if the data is already available in loaded context (files, earlier tool results). Only fetch what's genuinely missing. User stopped a redundant Jira fetch when data was already in the weekly report + prior query. (seen: 1)

## Concept candidates

- **2026-06-10:** Confluence attachment downloads use different auth than API calls. The v2 pages API works with basic auth (.netrc), but `/download/attachments/` returns 401. May need cookie-based session or different token scope. (seen: 1)
- **2026-06-11:** Cross-referencing Slack discussions against documented processes (wikis/repos) reveals process gaps. The RHIVOS tagging ownership gap was only visible because Slack showed ad-hoc behavior (Francisco/Ozan doing it manually) while the wiki showed automation (Gator handles promotion). Pattern: "compare what people do (Slack) with what's documented (wiki) to find process gaps." (seen: 1)
- **2026-06-11:** CI pipeline YAML files (`.gitlab-ci.yml`, stage includes, rules) are often the most authoritative source for understanding system architecture — more so than wikis or DETAILED.md docs. The Gator command orchestration (independent triggers vs sequential pipeline) was fully answered by reading `.gitlab/rules.yml` and the stage YAMLs, while DETAILED.md only showed the DPAC→Gator cross-project trigger. Pattern: "read the CI config to understand how components interact at runtime." (seen: 1)
- **2026-06-11:** Confluence REST API (`wiki/rest/api/search?cql=...` + `wiki/rest/api/content/{id}?expand=body.storage`) works with .netrc basic auth, same credentials as Jira. Can search across spaces by CQL, read full page HTML, extract text. Used to research OSCI CI Mediator across RHELPLAN, IVOS, and Red Hat Catalog spaces. (seen: 1)

## Structure candidates

**Format:**

```markdown
- **YYYY-MM-DD:** Proposed directory and reasoning (seen: 1)
```

## Resolved

- **2026-06-10:** Rule — "After plan approval, execute autonomously without confirmation prompts." Explicit user correction (3x in one session). Fast-tracked to memory as `feedback_autonomous-execution.md`.
