---
last_accessed: 2026-07-16
access_count: 0
created: 2026-07-16
---

# Skill: Build LLM wiki from Confluence

## When to use

Triggered when the user asks to create a knowledge base, wiki, or LLM-queryable
reference from a Confluence page (or page tree). Examples: "build a wiki from
this Confluence page", "make this Confluence content queryable", "create a
knowledge base for [topic]".

Parameterizable by Confluence page ID and target domain/directory.

## Procedure

### 1. Fetch source content

Fetch the root Confluence page and its children via the v2 REST API:

```bash
# Root page
curl -s -n "https://redhat.atlassian.net/wiki/api/v2/pages/${PAGE_ID}?body-format=atlas_doc_format" \
  -H "Authorization: Bearer ${CONFLUENCE_API_TOKEN}"

# Child pages
curl -s -n "https://redhat.atlassian.net/wiki/api/v2/pages/${PAGE_ID}/children?body-format=atlas_doc_format&limit=100" \
  -H "Authorization: Bearer ${CONFLUENCE_API_TOKEN}"
```

Save raw responses to `raw/` directory for reference. Convert HTML/ADF
bodies to markdown using standard cleanup (strip Confluence macros, fix
heading levels, normalize links).

**Purpose:** raw content is the source of truth; markdown conversion makes
it LLM-ingestible.

### 2. Scaffold wiki structure

Create the target directory (e.g., `agent_brain/projects/<domain>/`) with:

- `index.md` - hub file with content map, source links, frontmatter
- One markdown file per logical topic (not per source page)

Structure by topic, not by source page hierarchy. A Confluence page with
6 sections may become 3 wiki files if topics cluster naturally, or 8 if
subtopics deserve separation.

**Purpose:** the wiki serves LLM queries, not human browsing. Optimize for
self-contained files that answer questions without needing cross-file context.

### 3. INGEST in rounds

Process content in thematic rounds, each adding a layer:

1. **Concepts** - definitions, project structure, terminology
2. **Workflows** - state machines, transitions, field requirements
3. **Processes** - operational procedures, automations, rules
4. **Enrichment** - diagrams (export Google Drawings as PNG via
   `gws drive files export`, read visually), tables, decision trees
5. **Onboarding** - FAQ, common questions, getting-started content

Each round reads source content and writes/updates wiki files. Later rounds
can reference earlier ones. Don't try to do everything in one pass.

**Purpose:** layered ingestion avoids information overload and lets each
round focus on accuracy within its domain.

### 4. ENRICH with visual sources

If the Confluence page references diagrams (Google Drawings, embedded images):

1. Export as PNG: `gws drive files export <FILE_ID> --mimeType image/png`
2. Read visually (Claude multimodal) to extract states, transitions, labels
3. Cross-reference extracted data against text-based wiki content
4. Update wiki files with diagram-accurate data

**Purpose:** Google Drawings export as vector paths, not text. Visual reading
is the only reliable extraction method.

### 5. LINT

Review all wiki files for:

- Internal consistency (do cross-references match?)
- Completeness (does every topic from source appear in the wiki?)
- Accuracy (do states/transitions/fields match source diagrams?)
- Self-containedness (can each file answer questions without opening others?)

Fix issues found. This is a quality gate, not optional.

### 6. Register and deliver

1. Add entry to CLAUDE.md "Where to find things" with content description
   and read trigger.
2. If the wiki is for team sharing, initialize as a standalone git repo
   (CLAUDE.md + wiki/ + raw/) and push to GitLab.
3. Commit all files.

## Success criteria

- Every topic from the source Confluence page is covered in the wiki
- Wiki files are self-contained and answer domain questions without
  needing the original Confluence page
- Cross-references between wiki files are consistent
- Visual diagram data matches text descriptions

## Disconfirmation gate

After LINT, pick 3 specific questions a team member might ask about the
domain. Answer them using only the wiki files. If any answer requires going
back to the source Confluence page, the wiki is incomplete - fix and re-LINT.
