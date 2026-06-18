---
last_accessed: 2026-06-18
access_count: 1
created: 2026-06-18
---

# Confluence REST API patterns

## Authentication

Confluence REST API uses .netrc basic auth — same credentials as Jira. No separate token needed.

## Core patterns

### CQL search across spaces

```
GET wiki/rest/api/search?cql=text~"keyword"+and+space="SPACENAME"
```

Cross-space search (no space filter) useful for finding canonical pages across the org. Targeted search with `space=SPACENAME` for focused results.

### Full page content

```
GET wiki/rest/api/content/{id}?expand=body.storage
```

Returns HTML body. Add `children.page` to traverse page trees:

```
GET wiki/rest/api/content/{id}?expand=body.storage,children.page
```

### Page tree traversal

Fetch parent with `?expand=children.page`, then read each child body, recurse. Effective for exhaustive wiki audits (tested on 25+ page trees under Auto Toolchain + Release Management).

## Known limitations

- **Attachment downloads use different auth** than API calls. The v2 pages API works with basic auth (.netrc), but `/download/attachments/` returns 401. May need cookie-based session or different token scope. (Unresolved as of 2026-06-10.)

## Instances

1. **OSCI CI Mediator research (2026-06-11):** Searched RHELPLAN, IVOS, Red Hat Catalog spaces.
2. **Brew permissions audit (2026-06-14):** Searched RCMDOC and EXDSPRHELB spaces for tagging permissions. Cross-space search found "Permissions in Brew" canonical page in EXDSPRHELB.
3. **Auto Toolchain documentation audit (2026-06-14):** Traversed full page tree (25+ pages) under Product Development and Release.

> Source: [Log 2026-06-11](../../logs/2026-06-11.md), [Log 2026-06-14](../../logs/2026-06-14.md)
