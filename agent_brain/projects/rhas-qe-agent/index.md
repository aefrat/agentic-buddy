---
last_accessed: 2026-08-23
access_count: 2
created: 2026-07-02
---

# RHAS QE Expert Lead Agent - Knowledge Base

Content map for the RHAS QE Expert Lead agent. This agent generates
test strategies, release criteria, and testing status assessments for
RHAS (Red Hat Automotive Suite). Read this index first, then navigate
to the relevant store.

## Stores

- `reference/` - Data source documentation, RHIVOS testing patterns,
  OpenShift QE reference, agentic testing tools analysis. **Read-only.**
  Read when generating deliverables or answering testing questions.
- `active/` - Working drafts of test strategy, release criteria,
  research cache. **Overwritten each run.** Read when generating or
  updating a deliverable.
- `history/` - Past deliverables, dated. **Immutable after save.**
  Read when comparing versions or answering "what was the last strategy?"
- `patterns/` - Accumulated testing gap observations, OCP QE contacts.
  **Consolidation only.** Read when building context for new deliverables.

## Related project files

- [RHAS Testing Ownership](../rhas-testing-ownership/index.md) -
  Features requiring testing, candidate qualifications, testing
  landscape report. Pre-existing analysis.
- [PitCrew Agent](../pitcrew-agent/index.md) - Strategic context cache
  (shared).
- [RHIVOS 2.0 RC3](../RHIVOS_2_0_release_RC3.md) - CTC patterns,
  Greenwave gating, release pipeline structure.

## Key Google Docs

- Benny's Testing Architecture (`1NEzWHE1K4CiGkEDjhL5gpQUpcnepsiBvMDWPXUxLOHQ`) - 3-layer test architecture, cadence decisions.
- RHAS CI Testing Proposal (`1Txk4PQC9pGvNrNE9VViN8EMI8o94KpJa_kLMscBthAI`) - 3-phase rollout, DS pipeline design, ephemeral IPI SNO specs, upstream E2E suite scope (40/61 tests, 47 Ginkgo specs), prerequisites, trigger strategy, open questions.

## Skills

- [rhas-test-strategy](../../skills/rhas-test-strategy.md)
- [rhas-release-criteria](../../skills/rhas-release-criteria.md)
- [rhas-test-status](../../skills/rhas-test-status.md)
