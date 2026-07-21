---
last_accessed: 2026-07-21
access_count: 1
created: 2026-07-21
---

# Skill: Confluence research

## When to use

Triggered when the user asks to research a topic across Confluence, find
information in Confluence, or when a task requires gathering content from
multiple Confluence spaces. Examples: "research X on Confluence", "find
what Confluence says about Y", "search Confluence for Z".

## Procedure

### 1. Define the research scope

Identify:
- **Topic:** what specific information is needed
- **Spaces to search:** if the user specifies spaces, use those. Otherwise,
  search broadly using CQL with `type=page` (no space filter).
- **Depth:** quick lookup (1-2 queries) vs deep research (multiple CQL
  queries across spaces, content fetching, synthesis)

### 2. Search with CQL

Use the Confluence v2 REST API with .netrc basic auth:

```bash
curl -s -n "https://docs.engineering.redhat.com/rest/api/search?cql=type%3Dpage+AND+text~%22SEARCH_TERM%22&limit=25" | jq '.results[] | {title: .title, space: .resultGlobalContainer.title, url: .url, excerpt: .excerpt}'
```

**Auth:** uses `.netrc` credentials (basic auth). The `CONFLUENCE_API_TOKEN`
env var with Bearer auth has limited space access (4 spaces). Basic auth
via .netrc has broader access.

Iterate with different search terms if initial results are thin. Confluence
CQL supports: `text~"term"`, `space="KEY"`, `label="tag"`, `ancestor=ID`.

### 3. Fetch page content

For each relevant page, fetch the full body:

```bash
curl -s -n "https://docs.engineering.redhat.com/rest/api/content/PAGE_ID?expand=body.storage" | jq -r '.body.storage.value'
```

Convert HTML to readable text. Extract key information relevant to the
research topic.

**Purpose:** CQL excerpts are too short for synthesis. Full page content
reveals the actual procedures, decisions, and context.

### 4. Synthesize findings

Combine information from all fetched pages into a coherent answer:
- Identify consensus vs conflicting information across spaces
- Note which spaces/teams own which aspects of the topic
- Flag gaps where expected documentation is missing

### 5. Deliver results

Present findings to the user with:
- Summary of what was found
- Source pages with titles and spaces
- Gaps or areas needing further investigation

If requested, capture findings in `agent_brain/` (concept, project file)
or `user/` (document, reference).

## Scaling for deep research

For broad research (5+ spaces, 20+ pages), use parallel subagents:
- Fan out 2-4 agents, each covering a subset of spaces or search terms
- Each agent fetches and summarizes its pages independently
- Synthesize across agent results in the main thread

This was applied in the RHAS QE research (Jul 20): 3 parallel agents,
15+ spaces, ~40 pages identified, ~20 fetched.

## Quality criteria

- Every claim attributed to a specific page and space
- Conflicting information between spaces explicitly noted
- Search terms documented so the research can be reproduced or extended
