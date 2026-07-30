---
last_accessed: 2026-07-30
access_count: 4
created: 2026-07-14
---

# RHIVOS on GitLab (RoG)

**Initiative:** [AUTOBU-1105](https://redhat.atlassian.net/browse/AUTOBU-1105) - RHIVOS on Gitlab (Petr Sabata, created Jul 7, status: New, priority: NICETOHAVE)
**Execution epic:** [VROOM-41188](https://redhat.atlassian.net/browse/VROOM-41188) - RHIVOS Package Onboarding to RoG (Kanitha Chim, created by Hubert Stefanski May 4, focus area: Gating)
**Related OSCI ticket:** [OSCI-9642](https://redhat.atlassian.net/browse/OSCI-9642) - Support for RHIVOS components with RHEL-on-Gitlab (Patrick Talbert, Apr 17)
**Kernel automation:** [KMAINT-2296](https://redhat.atlassian.net/browse/KMAINT-2296) - Automate the automotive kernel builds
**ARB meeting notes:** [RoK Architecture Review Board](https://docs.google.com/document/d/1JKvrHVlIWEs1-F0CSJDvCJmwp-besBirsQ555VCHQ28/edit)
**RHEL dev guide (draft builds):** https://one.redhat.com/rhel-development-guide/#con_draft-builds_assembly_development
**OSCI meeting (Jul 30):** [Gemini notes + transcript](https://docs.google.com/document/d/1PZZo1nfHJtD9Aa3tnd2Jpj1bUJoWw03n2tc7cFVWOuM/edit) | [Recording](https://drive.google.com/file/d/1CfYHefCcvGcv6n8lMpHITj0frzyblpX1/view)

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

### From OSCI Team Meeting (Jul 30, 2026)

Meeting with Adam Samalik (PO) and Michal Srb (OSCI) - first direct requirements
discussion. Attendees: Avihai Efrat, Petr Sabata, Hubert Stefanski, Juanje Ojeda,
Kanitha Chim, Ozan Unsal.

**Scope confirmed:**
- ~30 RHIVOS-specific packages only. Additional RHEL package testing is out of
  scope for this initiative (runs separately, later in pipeline).
- RHIVOS stays in the private namespace in GitLab (Red Hat employees only).
  CentOS Stream sync is not on the agenda.

**Technical findings from OSCI side:**

1. **Dynamic main branch** is a known challenge. RHIVOS manages its own `main`
   branch (e.g. `rhivos-2-main` becomes `rhivos-2.2` when 2.1 releases). Draft
   builds from MRs need to dynamically resolve the correct Brew target. Michal
   confirmed Voyager has a similar situation - solvable but needs custom work.

2. **Configuration source:** OSCI uses `box-law-data` components repo as source
   of truth for onboarding. RHIVOS already has entries there - one less blocker.

3. **Repository configuration:** OSCI currently applies uniform config to all
   onboarded repos (e.g., one human approver for RHEL). RHIVOS already has an
   informal policy that satisfies audit requirements, with assignees and
   contributors defined in the components repo.

4. **Conflux deferred.** Build in Brew first. Conflux integration (workspaces,
   application component models) takes significant time. Should be invisible to
   maintainers once the Conflux team has capacity. Lookaside cache support for
   building directly from GitLab is still WIP.

5. **GitLab and dist-git are separate storage.** Not a frontend on top of
   dist-git - they sync bidirectionally. Dist-git remains source of truth
   (lookaside cache). BC check (dist-git rules) runs as an MR test in GitLab.
   Petr wants to disable direct dist-git pushes and use GitLab-only - Michal
   said this is preferable and easier for smaller teams who can mandate it.

6. **Testing: phased approach proposed by Michal.**
   - Phase 1: Onboard without tests. MR merge -> build lands in `-gate` tag ->
     existing Test Console gating continues as-is.
   - Phase 2: Plug tests into MRs (run in merge requests, provide results).
   - Phase 3: When MR merged, draft build promotes directly to `-candidate`,
     skip old gating entirely.
   - Michal: RHEL testing is also "kind of messy" - 13+ Jenkins instances,
     teams migrating at different speeds. Adding RHIVOS-specific logic
     ("if RHIVOS then do this") is "always possible."

7. **Side tags: GitLab-native workflow is Adam's top priority.** Current
   Jenkins-based sidetag workflow won't work for RHIVOS. New GitLab-native
   version is being built for RHEL and "should be reusable without any changes
   for RHIVOS." This would solve the kernel team's daily pain point (daily
   kernel builds + external kmod rebuilds in sidetags, currently manual).

**OSCI action items:**
- Adam + Michal will take requirements back to their team for feasibility
  assessment, effort estimation, and integration details.
- Adam will create an epic or Jira ticket to track the RHIVOS onboarding
  project and share estimates once formulated.
- Timeline target: H2 2026 (Petr's request, Adam acknowledged).

**Questions answered:**
- Konflux: deferred, build in Brew first (confirmed by Michal).
- Code sync: yes, GitLab -> dist-git sync happens automatically. Dist-git
  remains source of truth for now.
- Test Console integration: phased approach (see above). Can keep existing
  gating initially, replace incrementally.
- Gator: effectively replaced by GitLab MR workflow + direct promotion path.
- Shift-left testing into RHEL CI: Hubert mentioned Donald Zickus's idea.
  Juanje noted some TMT tests have been partially integrated but "not
  practical right now" due to pace of test changes. Future goal, not current.

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

1. ~~Is Konflux builds part of this scope?~~ **Answered Jul 30:** Deferred.
   Build in Brew first; Conflux integration comes later when their team has
   capacity. Should be invisible to maintainers.
2. ~~Is code sync to dist-git included?~~ **Answered Jul 30:** Yes, GitLab ->
   dist-git sync is automatic. Dist-git stays source of truth for now
   (lookaside cache).
3. ~~How does Test Console integrate?~~ **Answered Jul 30:** Phased. Start with
   existing gating (merge -> gate tag -> Test Console), then incrementally
   plug tests into MRs, then skip old gating entirely.
4. ~~What happens to Gator?~~ **Answered Jul 30:** Replaced by GitLab MR
   workflow + direct promotion. Phase 1 keeps existing gating as safety net.
5. Can RHIVOS "shift left" testing into RHEL CI? (Donald Zickus idea) -
   Juanje: partially started but "not practical right now." Future goal.
6. **NEW:** What specific changes does OSCI need for dynamic main branch
   resolution in draft builds? Michal confirmed it's solvable (Voyager
   precedent) but didn't detail the implementation.
7. **NEW:** Timeline and effort estimate from OSCI team - awaiting Adam's
   epic/ticket creation and capacity assessment.
8. **NEW:** How does the new GitLab-native sidetag workflow work, and when
   will it be available for RHIVOS to reuse?

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
