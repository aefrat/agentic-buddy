---
last_accessed: 2026-06-11
access_count: 3
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

## Rule candidates

- **2026-06-11:** Use `jira-cli` (`jira issue view`, `jira issue list`) for Jira queries, not raw `curl` API calls. The CLI is configured with auth and handles formatting. User corrected this explicitly. (seen: 1)
- **2026-06-11:** Before querying external systems, check if the data is already available in loaded context (files, earlier tool results). Only fetch what's genuinely missing. User stopped a redundant Jira fetch when data was already in the weekly report + prior query. (seen: 1)

## Concept candidates

- **2026-06-10:** Confluence attachment downloads use different auth than API calls. The v2 pages API works with basic auth (.netrc), but `/download/attachments/` returns 401. May need cookie-based session or different token scope. (seen: 1)

## Structure candidates

**Format:**

```markdown
- **YYYY-MM-DD:** Proposed directory and reasoning (seen: 1)
```

## Resolved

- **2026-06-10:** Rule — "After plan approval, execute autonomously without confirmation prompts." Explicit user correction (3x in one session). Fast-tracked to memory as `feedback_autonomous-execution.md`.
