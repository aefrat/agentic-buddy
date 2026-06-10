---
last_accessed: 2026-06-10
access_count: 2
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

**Format:**

```markdown
- **YYYY-MM-DD:** Proposed rule and why (seen: 1)
  - YYYY-MM-DD: seen again in [context] (seen: 2) → ready to propose
```

## Concept candidates

- **2026-06-10:** Confluence attachment downloads use different auth than API calls. The v2 pages API works with basic auth (.netrc), but `/download/attachments/` returns 401. May need cookie-based session or different token scope. (seen: 1)

## Structure candidates

**Format:**

```markdown
- **YYYY-MM-DD:** Proposed directory and reasoning (seen: 1)
```

## Resolved

- **2026-06-10:** Rule — "After plan approval, execute autonomously without confirmation prompts." Explicit user correction (3x in one session). Fast-tracked to memory as `feedback_autonomous-execution.md`.
