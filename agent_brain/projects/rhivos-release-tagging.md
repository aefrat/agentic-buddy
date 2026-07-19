---
last_accessed: 2026-07-19
access_count: 2
created: 2026-07-14
---

# RHIVOS Release Package Tagging - RHEL Inheritance Flag

## Context

Only Petr Sabata (contyk) and Ozan Unsal know how to tag RHIVOS release
packages with the correct RHEL inheritance flag. This is a knowledge
bottleneck - if both are unavailable, nobody on the toolchain team can
perform the tagging.

**Source:** Petr/Avihai 1:1 (Jul 14, 2026). Juanje also flagged this
dependency in his quarterly connection conversation.

## Existing Documentation

Petr has a document from ~3 years ago covering the inheritance and tagging
structure between RHIVOS and RHEL. He shared it during the meeting
(branching strategy document with a diagram that is "almost impossible to
read"). Document covers:
- Inheritance between RHIVOS and RHEL packages
- Tagging structure (10.0, RHIVOS 2.0z, 2.1, etc.)
- What to tag and when

## Goal

At least one additional person on the toolchain team should understand the
tagging workflow well enough to perform it independently.

## Action Items

- [ ] Avihai: Review the branching strategy document Petr shared. Extract
  simple rules from the diagram. If unclear, follow up with Petr.
- [ ] Avihai: Identify a toolchain team member to learn the tagging workflow
  (candidate: someone beyond Ozan who can be trained)
- [ ] Petr: Available for questions if the document is not self-explanatory

## Related Files

- [RHIVOS Dist-Git Workflow](rhivos-distgit-workflow.md) - dist-git policies, branch model, build targets
- [RHIVOS Release Approach](rhivos-release-approach.md) - Brew tag structure
- [RHIVOS 2.0 RC3](RHIVOS_2_0_release_RC3.md) - RC3 release tracking
