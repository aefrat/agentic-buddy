---
last_accessed: 2026-07-22
access_count: 0
created: 2026-07-22
---

# Invisible enforcement gaps

When automated enforcement, monitoring, or alerting is absent or removed, the
underlying business requirement becomes invisible and will eventually be missed.
The requirement still exists - it just lost its mechanism for surfacing.

This pattern appears across CI gates, compliance deadlines, manual pipeline steps,
and any process that depends on human memory rather than system prompts. The
failure mode is always the same: something critical gets forgotten because nothing
reminds anyone it exists.

## When to apply

- Evaluating whether disabling a CI gate or enforcement mechanism is safe
- Reviewing processes with manual steps embedded in automated pipelines
- Auditing compliance or renewal tracking systems
- Designing agent skills that monitor for recurring requirements

## Specific instances

- Policy enforcement vs process requirement separation (2026-07-02): RHIVOS
  kernel derivative packages had dist-git policy exceptions (no server-side commit
  hooks), but still needed Jira tickets for errata advisories. Disabling the gate
  made the ticket requirement voluntary, turning it into tribal knowledge.
- Manual step in automated pipeline (2026-07-02): `update-docs.sh` automated
  repo pulls and CODEBASE.md regeneration daily, but wiki ingest was manual.
  Result: 11 days of stale wiki files. The manual step was invisible to the
  person who needed to do it.
- Compliance deadlines in spreadsheets (2026-07-19): 4 ATC SOAs expired (oldest:
  69 days) without anyone noticing because the tracking spreadsheet has no
  automated expiry notifications. Discovered only by agent reading the contents.
