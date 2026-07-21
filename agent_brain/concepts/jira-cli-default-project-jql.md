---
last_accessed: 2026-07-21
access_count: 1
created: 2026-07-21
---

# Jira CLI default project breaks multi-condition JQL

The `jira` CLI config (`~/.jira/.config.yml`) has `project: VROOM`, which
silently appends `AND project=VROOM` to all JQL queries.

## Problem

Single-field queries work fine, but multi-condition queries fail:

- **Multi-condition:** `jira issue list --jql "status = Open AND priority = High"`
  becomes `status = Open AND priority = High AND project=VROOM` - works.
- **ORDER BY:** `jira issue list --jql "status = Open ORDER BY created DESC"`
  becomes `status = Open ORDER BY created DESC AND project=VROOM` - parse
  error ("Expecting ',' but got 'ORDER'").
- **Cross-project:** any query targeting a project other than VROOM
  gets the default appended and returns no results or errors.

## Workarounds

1. **For ORDER BY:** remove `ORDER BY` from JQL and use CLI flags instead:
   `--order-by created --reverse`.
2. **For cross-project:** use `jira issue view <KEY>` (takes a ticket key,
   not JQL) for individual tickets.
3. **Nuclear option:** remove the default project from config, but this
   breaks all current usages relying on the default.

## Impact

Multiple skill data-sources.md files (LP status, PitCrew) document queries
with `ORDER BY` that silently fail. Any new skill using `jira issue list`
with complex JQL will hit this.

> Source: [2026-06-30 log](../../logs/2026-06-30.md), [2026-07-20 log](../../logs/2026-07-20.md)
