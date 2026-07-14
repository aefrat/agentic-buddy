---
last_accessed: 2026-07-14
access_count: 2
created: 2026-07-14
---

# RHIVOS on GitLab (RoG)

**Initiative:** [AUTOBU-1105](https://redhat.atlassian.net/browse/AUTOBU-1105) - RHIVOS on Gitlab (Petr Sabata, created Jul 7, status: New, priority: NICETOHAVE)
**Execution epic:** [VROOM-41188](https://redhat.atlassian.net/browse/VROOM-41188) - RHIVOS Package Onboarding to RoG (Kanitha Chim, created by Hubert Stefanski May 4, focus area: Gating)
**Related OSCI ticket:** [OSCI-9642](https://redhat.atlassian.net/browse/OSCI-9642) - Support for RHIVOS components with RHEL-on-Gitlab (Patrick Talbert, Apr 17)
**Kernel automation:** [KMAINT-2296](https://redhat.atlassian.net/browse/KMAINT-2296) - Automate the automotive kernel builds
**ARB meeting notes:** [RoK Architecture Review Board](https://docs.google.com/document/d/1JKvrHVlIWEs1-F0CSJDvCJmwp-besBirsQ555VCHQ28/edit)
**RHEL dev guide (draft builds):** https://one.redhat.com/rhel-development-guide/#con_draft-builds_assembly_development

---

## Context

Infrastructure enablement to transition RHIVOS to a GitLab instance, following
the same pattern as RHEL on GitLab (RoG). This is one of the top team priorities
(per Petr, Jun 24) alongside CAIB integration and Konflux.

Originated from the RoK Architecture Review Board meeting (May 4, 2026) where
Veronika Kabatova (OSCI) indicated it should be possible to run purely RHIVOS
gating/testing and manage package lifecycle on RHIVOS's own Brew tags without
touching RHEL.

## What It Replaces / Enables

| Current state | GitLab state |
|---|---|
| Direct pushes to dist branches | Merge request workflows with reviews |
| Branch gating policies (dist-git rules) | MR-based gating via GitLab CI |
| Package gating (Gator + ResultsDB + Greenwave + WaiverDB) | Draft builds in Brew, GitLab-native test orchestration |
| One build at a time through gate | Grouped builds (tested + promoted together) |
| No formal audit trail | Full auditability (reviewer on every change) |
| Gator as test orchestrator (triggers Test Console) | OSCI pipelines integrated with GitLab MRs |

## Key Details

### From Petr (Jul 14 1:1)

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

### From Hubert (May 4, VROOM-41188 comments)

Hubert's rationale for the migration:
1. Moving to a more "native" workflow that the rest of RHEL follows
2. Dropping reliance on Gator (which Hubert calls "a poor excuse of an
   orchestrator")
3. Simplifying the entire process into a single interface (GitLab MR
   approvals/comments as provided by OSCI/RoG)

Gator's current only real purpose: trigger tests in Test Console and run
package promotion on successful Greenwave evaluation. Both would be replaced.

### From Ozan (Apr 23, VROOM-40774 comments)

**Critical gating impact:** The RoG draft tagging process (draft -> candidate
on MR approval) bypasses the current RHIVOS gating flow. Currently RHIVOS
needs builds tagged to `-gate`, tested, then promoted to `-candidate`. Draft
builds skip `-gate` and go directly to `-candidate`. This means the RHIVOS
gating workflow (Gator + Test Console) needs rethinking as part of this
migration.

Kanitha raised that RHIVOS needs extra gate tests on Test Console before
promoting from `-gate` to `-candidate`. Chris Kelley (OSCI) responded that the
old gating workflow is being decommissioned (another team removing a service it
depends on) and all builds will be tagged directly to `*-candidate` by May 15.

## Packages to Onboard

From VROOM-41188 acceptance criteria (21 packages):

- kernel-automotive
- kernel-ivos-qualcomm
- bluechi, qm
- aboot-deploy, aboot-update
- android-tools
- automotive-image-builder, automotive-image-builder-policy
- dracut-automotive
- osbuild-auto
- ukiboot, unzboot
- util-linux-automotive
- auto-boot-check
- fusa-gcc-plugin, fusa-gcc-plugin-data
- redhat-release-automotive
- downstream-dtbs, qcom-scmi
- sysboot

## Jira Structure

```
AUTOBU-1105 (Initiative) - RHIVOS on Gitlab
  |
  +-- VROOM-41188 (Epic) - RHIVOS Package Onboarding to RoG
        |
        +-- VROOM-32012 (Task) - [SPIKE] Design/Workflow document for
            OSCI-like RHIVOS RPM checks (Roni Eliezer, New)

Related:
  OSCI-9642 (Story) - Support for RHIVOS components with RHEL-on-Gitlab
    |-- blocked by VROOM-40774 - Create -draft brew build targets for RHIVOS
    |                            (Ozan Unsal, New)
    +-- relates to KMAINT-2296 - Automate the automotive kernel builds
```

## Blockers / Prerequisites

1. **Draft Brew build targets don't exist for RHIVOS** (VROOM-40774). RHEL has
   them (e.g., `rhel-10.3-z-candidate-pesign-draft`), RHIVOS does not. Ozan
   created `rhivos-2-newest-candidate-pesign` but the `-draft` variants are
   still needed. Blocks OSCI-9642.

2. **Dist-git branch naming mismatch.** RHIVOS branches don't follow RHEL
   naming conventions. Patrick Talbert has a proposed fix in osci-pipelines
   (similar to what was done for Voyager): https://gitlab.com/ptalbert/osci-pipelines/-/commit/f3062361

3. **OSCI pipeline global-tasks.yml** needs enabling for RHIVOS branches
   (Veronika Kabatova flagged this in VROOM-41188 comments):
   https://gitlab.com/redhat/centos-stream/ci-cd/dist-git-gating-tests/-/blob/latest/global-tasks.yml

4. **Layered product support not straightforward.** Michal Srb (OSCI) noted
   that layered/RHEL-based product support was tested with Voyager/RHEL4NV
   and is "not really straightforward today." Suggested creating a ticket in
   the ARR project: https://redhat.atlassian.net/browse/ARR

5. **Hubert Stefanski transition.** Hubert (who created the epic and drove the
   initial engagement with OSCI) is leaving (started transition Jul 1). His
   knowledge of the design and OSCI contacts needs to transfer.

## Key People

| Person | Role | Context |
|---|---|---|
| Petr Sabata (contyk) | Initiative owner, release/distribution | Set as AUTOBU-1105 reporter |
| Kanitha Chim | Execution lead | Assigned on VROOM-41188 (took over from Hubert) |
| Hubert Stefanski | Original epic creator | Transitioning out (started Jul 1) |
| Patrick Talbert | OSCI/kernel side | Created OSCI-9642, proposed branch naming fix |
| Veronika Kabatova | OSCI | Confirmed RoG can run RHIVOS-only gating on own Brew tags |
| Chris Kelley | OSCI | Informed that old gating workflow being decommissioned |
| Adam Samalik | PO (planning/prioritization) | OSCI side PO |
| Michal Srb | OSCI | Flagged layered product complexity |
| Ozan Unsal | Brew targets | Created build target, assigned on VROOM-40774 |
| Roni Eliezer | Spike design | Assigned on VROOM-32012 |
| Aviv Sabadra | Release engineering | Helped with draft build target info |
| Rachel Sibley | QE perspective | Referenced for testing requirements |

## Open Questions

1. Is Konflux builds part of this scope? (Hubert: "not sure, I don't think so")
2. Is code sync to dist-git included? (Hubert: "likely yes")
3. How does Test Console testing integrate with the new RoG workflow? (Kanitha's
   concern about `-gate` tag bypass)
4. What happens to Gator? Hubert proposed dropping it entirely and adding a
   small GitLab job for `-pending` to `-candidate` promotion. But Test Console
   testing needs a replacement path.
5. Can RHIVOS "shift left" some testing into RHEL's own CI/gating? (Donald
   Zickus raised this - future conversation, not current scope)

## Architecture Proposal

Full migration architecture proposal (Jul 14, 2026):
[user/documents/rhivos-rog-migration-proposal.html](../../user/documents/rhivos-rog-migration-proposal.html)

Covers: current vs target state diagrams, Brew tag restructuring, MR workflow
design, Test Console integration, Gator transition plan, 4-phase migration
schedule (Jul 2026 - Feb 2027), risk register, RACI matrix, and 7 open
stakeholder decisions.

## Related Files

- [RHIVOS Dist-Git Workflow](rhivos-distgit-workflow.md) - current dist-git
  policies, branch model, build targets
- [RHIVOS QC Layered Product](rhivos-qc-layered-product.md) - LP needs
  GitLab infrastructure
- [RHIVOS Release Tagging](rhivos-release-tagging.md) - tagging knowledge
  bottleneck (related to Brew tag structure)
