---
last_accessed: 2026-07-14
access_count: 1
created: 2026-07-14
---

# RHIVOS on GitLab

**Epic:** [AUTOBU-1105](https://redhat.atlassian.net/browse/AUTOBU-1105)
**Source:** Petr/Avihai 1:1 (Jul 14, 2026)

## Context

Infrastructure enablement to transition RHIVOS to a GitLab instance, following
the same pattern as RHEL on GitLab. This is one of the top team priorities
(per Petr, Jun 24) alongside CAIB integration and Konflux.

## What It Replaces / Enables

| Current state | GitLab state |
|---|---|
| Direct pushes to dist branches | Merge request workflows |
| Branch gating policies | MR-based gating (draft builds in Brew) |
| Package gating (Gator promotes one at a time) | Draft builds tested before promotion, can be grouped |
| No formal audit trail | Full auditability (reviewer on every change) |

## Key Details (from Petr, Jul 14)

- **Draft builds in Brew:** When you submit a merge request, it creates a
  draft build (special type) that can be promoted to a real build after
  testing. If tests fail, the draft is discarded. Current model requires a
  real build that sits in gate.
- **Grouped builds:** Builds can be grouped (like kernel does), tested
  together, and promoted together.
- **Auditability requirement:** From earlier in 2026, everything needs a
  reviewer. The kernel team is "really unhappy" that RHIVOS does not have
  this yet.
- **Conflux dependency:** If RHIVOS uses Conflux to build, GitLab integration
  is the only way. This is a hard requirement.
- **RHEL model difference:** RHEL uses CentOS Stream GitLab and syncs into
  the main branch. RHIVOS would use GitLab for both branches (main and
  release) since there is no sync mechanism and no intent to create one.

## Related Files

- [RHIVOS Dist-Git Workflow](rhivos-distgit-workflow.md) - current dist-git
  policies, branch model, build targets
- [RHIVOS QC Layered Product](rhivos-qc-layered-product.md) - LP needs
  GitLab infrastructure
- [RHIVOS Release Tagging](rhivos-release-tagging.md) - tagging knowledge
  bottleneck (related to Brew tag structure)
