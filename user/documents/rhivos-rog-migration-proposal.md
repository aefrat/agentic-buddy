# RHIVOS on GitLab (RoG) - Migration Architecture Proposal

**Initiative:** [AUTOBU-1105](https://redhat.atlassian.net/browse/AUTOBU-1105) |
**Execution Epic:** [VROOM-41188](https://redhat.atlassian.net/browse/VROOM-41188) |
**OSCI Ticket:** [OSCI-9642](https://redhat.atlassian.net/browse/OSCI-9642)

**Date:** July 14, 2026
**Author:** Avihai Efrat, ATC Engineering Manager
**Audience:** Petr Sabata (PO), Kanitha Chim (Execution Lead), Jamie Flynn (Director)

---

## Contents

1. [Executive Summary](#1-executive-summary)
2. [Architecture Comparison](#2-architecture-comparison)
3. [Target State Design](#3-target-state-design)
4. [Migration Phases](#4-migration-phases)
5. [Risk Register](#5-risk-register)
6. [Open Decisions](#6-open-decisions)
7. [Timeline](#7-timeline)
8. [RACI Matrix](#8-raci-matrix)
9. [What This Solves Beyond the Migration](#9-what-this-solves-beyond-the-migration)

---

## 1. Executive Summary

This proposal describes how RHIVOS will migrate from its current custom gating stack (Gator + Greenwave + ResultsDB + WaiverDB) to the same GitLab-based merge request workflow that RHEL uses, known as RHEL on GitLab (RoG). The migration replaces direct dist-git pushes with merge-request-driven development, replaces post-build gating with pre-merge draft builds, and replaces Gator's test orchestration with OSCI GitLab CI pipelines. This is the right time because: (a) the OSCI team is decommissioning the gating-bot that Gator depends on ([OSCI-8454](https://redhat.atlassian.net/browse/OSCI-8454)), (b) Conflux integration - a stated Q3 priority - requires GitLab-native workflows as a hard dependency, (c) the RC3 release process exposed 6 process gaps in the current tagging workflow that RoG structurally eliminates, and (d) Kanitha Chim's new Toolchain Architect role positions gating redesign as her first architectural project. The migration covers 21 RHIVOS-specific packages across 4 phases, targeting completion by end of Q1 2027.

---

## 2. Architecture Comparison

### 2.1 Current State ("As-Is")

```
Developer
    |
    | git push (direct to dist-git branch)
    | [gitbzverify server-side hook: Jira ticket validation]
    |
    v
dist-git branch (rhivos-2-main or rhivos-2.0)
    |
    | rhpkg build --target <target>
    |
    v
Brew Build
    |
    | build lands in -gate tag (or -candidate for dev branches)
    |
    v
+-----------+    +------------+    +-----------+
| -gate tag |    | RHEL       |    |           |
| (RHIVOS   |--->| -pending   |--->|  Gator    |
|  builds)  |    | (inherited)|    | evaluate  |
+-----------+    +------------+    +-----------+
                                        |
                    Queries Greenwave ---+
                    Queries ResultsDB ---+
                    Triggers Test Console +
                    Triggers Contcert ----+
                                        |
                         +--------------+-----------+
                         |                          |
                    [PASS]                     [FAIL]
                         |                          |
                    auto-promote              Slack notification
                    -gate -> -candidate       with WaiverDB links
                         |
                         v
                  DPAC Pipeline (git tag trigger)
                  generate-compose (ODCS)
                  check-repoclosure
                  build-*-image (per board)
                  smoke-tests-* (Test Console)
                  promote-packages-in-brew (Gator)
                         |
                         v
                  -candidate -> -pending
                  Gator generate-advisories (Errata Tool)
```

**Key pain points in current state:**

- No audit trail on code changes (direct pushes, no reviewer required)
- Builds happen AFTER code merges - failed gates mean wasted build effort
- No grouped build capability (STAG proposed but not implemented)
- Tagging into -gate is undocumented, depends on 2 people (Sameera, Ozan)
- 11 external service integrations with fragile coupling
- Gator is stateless and single-threaded (one package at a time through gate)

### 2.2 Target State ("To-Be")

```
Developer
    |
    | Opens Merge Request in GitLab Private Namespace
    | [branch: rhivos-2-main or rhivos-2.0]
    |
    v
MR Pipeline (GitLab CI, OSCI-managed)
    |
    +---> OSCI creates draft build (Brew -draft target)
    |         rhivos-2.1-candidate-pesign-draft
    |
    +---> Draft build lands in -draft tag (sandbox)
    |
    +---> OSCI CI tests run against draft build:
    |         - RPM-level tests (rpminspect, rpmdiff)
    |         - RHIVOS-specific tests (GitLab CI calling Test Console)
    |         - Contcert continuous certification
    |
    +---> Results posted to MR as CI status
    |
    v
MR Review + Approval
    |
    +--- [APPROVE + MERGE]              [REJECT / CLOSE]
    |         |                               |
    |    Draft build promoted            Draft build discarded
    |    -draft -> -candidate            No artifact remains
    |         |
    |         v
    |    DPAC Pipeline (compose-level, largely unchanged)
    |    generate-compose (ODCS, from -candidate)
    |    check-repoclosure
    |    build-*-image (per board)
    |    smoke-tests-* (Test Console)
    |         |
    |         v
    |    Promotion: -candidate -> -pending
    |    Advisory generation (Errata Tool)
    |
    v
  CDN / Customer delivery
```

### 2.3 Side-by-Side Comparison

| Concern | Current (Gator-based) | Target (RoG) |
|---|---|---|
| Code change entry | Direct push to dist-git | Merge Request with reviewer |
| Audit trail | gitbzverify hook only | Full MR history, approvals |
| When build happens | After code merges | Before merge (draft build) |
| Build artifact on fail | Real build in -gate | Draft discarded, no trace |
| Test orchestration | Gator -> Test Console | GitLab CI -> Test Console |
| Gating evaluation | Greenwave + ResultsDB | MR pipeline CI status |
| Package promotion | Gator evaluate (auto) | MR merge (auto) |
| Grouped builds | Not supported | Side tags (native) |
| Compose-level testing | DPAC pipeline | DPAC pipeline (unchanged) |
| Advisory generation | Gator generate-advisories | Triggered post-compose |
| Branch model | rhivos-2-main, rhivos-2.0 | Same (with naming adapter) |
| FDA no-manual-tagging | Partially enforced | Structurally enforced |

---

## 3. Target State Design

### 3.1 New Brew Tag Structure

RHEL's RoG model uses `-draft` build targets that create sandbox builds. RHIVOS needs equivalent targets created for each release stream.

**Required new build targets ([VROOM-40774](https://redhat.atlassian.net/browse/VROOM-40774)):**

```
Per release stream X.Y:

  Existing:                          New (RoG):
  --------                           ---------
  rhivos-X.Y-build                   (unchanged - buildroot)
  rhivos-X.Y-gate     ----+
  rhivos-X.Y-candidate    |          rhivos-X.Y-candidate-pesign-draft
  rhivos-X.Y-pending      |          (draft builds land here)
                           |
                           +------> DEPRECATED after full migration
                                     (gate tag no longer needed)

For z-stream:
  rhivos-X.Y-z-candidate-pesign-draft
```

**Tag lifecycle in RoG:**

1. Draft build target produces a draft build in the -draft tag
2. -draft tag inherits from -build (same buildroot as today)
3. On MR merge: draft build is promoted to -candidate (real build)
4. On MR reject: draft build is untagged/discarded
5. -candidate -> -pending promotion continues as today (compose-driven)

> **QC Layered Product:** LP Brew tags (VROOM-44911, per the single-LP decision of Jul 14) will need their own -draft variants when LP work resumes. The RoG infrastructure should be designed to be LP-aware (parameterized by product/tag-set) from the start, but LP onboarding does not block Phases 0-3. LP becomes a Phase 5 activity.

### 3.2 MR Workflow Design

**Developer experience (target state):**

1. Developer creates feature branch from `rhivos-2-main` (or `rhivos-2.0`)
2. Developer opens MR in GitLab Private Namespace
3. OSCI pipeline automatically:
   - Creates draft build in Brew using -draft target
   - Runs rpminspect/rpmdiff checks
   - Triggers RHIVOS-specific tests via Test Console
   - Posts results to MR as CI job status (green/red)
4. Reviewer reviews code + test results
5. On approval + merge:
   - Draft build promoted to -candidate (automatic)
   - DPAC compose pipeline can be triggered normally
6. On rejection:
   - Draft build discarded (no cleanup needed)
   - Developer iterates on the branch, opens new MR

**Branch naming adapter:** Patrick Talbert has already implemented a fix in osci-pipelines (MR !870) similar to what was done for Voyager/RHEL4NV. This adapter maps RHIVOS branch names (`rhivos-2-main`, `rhivos-2.0`) to the corresponding Brew targets and OSCI pipeline configuration.

**Policy enforcement by branch type:**

| Branch | Dist-git policy today | RoG policy |
|---|---|---|
| rhivos-2-main | Anything Goes | MR required, reviewer required, Jira ticket encouraged |
| rhivos-2.0 | Strict (blocker/exception + fixVersion) | MR required, reviewer required, Jira ticket enforced in MR template |
| Package exceptions (kernel-automotive, etc.) | Anything Goes on release branches | MR required, reviewer required, Jira ticket optional |

> **Key shift:** Even "Anything Goes" branches now require an MR with a reviewer. This addresses the kernel team's concern that Petr flagged - "they are really unhappy that RHIVOS does not have this yet."

### 3.3 Test Console Integration in MR Pipeline

Test Console currently pushes results directly to ResultsDB via HTTP API (confirmed by Roni Eliezer's implementation, VROOM-29833). This direct integration is an advantage for the RoG migration because Test Console does not depend on the UMB/Greenwave chain that Gator uses.

```
MR Pipeline (GitLab CI)
    |
    +---> RPM-level tests (rpminspect, rpmdiff)     [OSCI-managed]
    |
    +---> RHIVOS-specific tests                      [RHIVOS-managed GitLab CI job]
    |         |
    |         +---> GitLab CI job calls Test Console API
    |         |     (same API Gator uses via run_test)
    |         |
    |         +---> Test Console runs tests on:
    |         |     - QEMU (VM smoke)
    |         |     - SA8650 (Qualcomm board)
    |         |     - SA8775 (Qualcomm board)
    |         |
    |         +---> Results reported back to GitLab CI
    |               (exit code + artifact upload)
    |
    +---> Contcert continuous certification           [Contcert-managed]
              |
              +---> Results pushed to ResultsDB
                    (unchanged from today)
```

**Key design decisions:**

1. **Test scope for MR pipeline:** Only package-level tests (not full compose/board smoke). The MR tests answer "does this package build and pass its own test suite?" Full compose and board-level smoke tests remain in the DPAC pipeline (post-merge).
2. **Hardware test budget:** Running full hardware tests on every MR is expensive (board time, power, provisioning). Proposal: run VM (QEMU) tests on every MR, hardware board tests on demand (triggered by a label or comment on the MR, e.g., `/test-hardware`). *(Decision D1 - needs stakeholder input.)*
3. **Test Console API contract:** The existing `tc-cli rhivos base-image is-complete` interface (used by Gator's `run_test` command) can be wrapped in a GitLab CI job script. Roni Eliezer ([VROOM-32012](https://redhat.atlassian.net/browse/VROOM-32012) spike) should design this API contract.
4. **ResultsDB continuity:** Test Console and Contcert continue pushing results to ResultsDB - those integrations are unchanged. What changes is that Greenwave policy evaluation is no longer the gating mechanism. The GitLab CI job status replaces it.

### 3.4 Compose-Level and Board-Level Testing

The DPAC pipeline (compose-level testing) is **largely unchanged** by the RoG migration. It continues to be triggered by git tags in rhivos.git, run ODCS composes from -candidate, check repoclosure, build images per board, run smoke tests via Test Console, and promote packages from -candidate to -pending.

The only change is the input: today, -candidate is populated by Gator's auto-promotion from -gate. In the target state, -candidate is populated by MR merges promoting draft builds. The tag contents are identical either way - ODCS does not care how builds got there.

**CTC testing** for release candidates continues as today. CTC is a release milestone activity, not a per-package gate. It runs against full compose images, not individual draft builds.

### 3.5 Gator Transition Plan

Gator has 5 major functions. Each has a specific transition plan:

| Gator Function | Disposition | Details |
|---|---|---|
| `evaluate` | **REPLACED** | RoG MR pipeline replaces Greenwave/ResultsDB evaluation. CI status on MR replaces pass/fail gating. |
| `promote` (gate -> candidate) | **REPLACED** | Draft build -> candidate on MR merge is automatic in RoG. No manual tagging. |
| `promote` (candidate -> pending) | **SURVIVES** | Post-compose promotion still needed. Triggered by DPAC pipeline stage. Could be a simple GitLab CI job or script (`brew tag-build`). |
| `run_test` | **REPLACED** | GitLab CI jobs call Test Console directly. Same API, different trigger mechanism. |
| `generate_advisories` | **SURVIVES** | Errata advisory generation is not replaced by RoG. Still needed post-compose. Trigger moves from Gator CLI to a DPAC pipeline job or OSCI errata-automation integration. *(Decision D2.)* |
| `audit` | **REPLACED** | GitLab native MR history + CI artifacts provide full audit trail. Custom audit reports can use GitLab API. |

**Advisory generation detail:** Gator's `generate_advisories` command currently finds packages that passed gating, checks for existing advisories in NEW_FILES state, attaches builds to advisories, and links Jira tickets from commit messages. This logic must survive. Two options:

- **Option A (recommended):** Evaluate whether OSCI's `errata-automation` project can handle RHIVOS directly, or with a thin wrapper.
- **Option B:** Extract the advisory-generation portion of Gator as a standalone tool, stripped of evaluate/promote logic.

**Kernel-automotive special handling:** Today, Gator checks ReportPortal for kernel-automotive triage status (if all failures have BTS links, it auto-promotes). In the RoG model, this becomes a GitLab CI job that checks ReportPortal as a required CI gate on kernel-automotive MRs. Note: ReportPortal is being decommissioned by Sep 22, 2026, so this special path may be short-lived.

### 3.6 Errata Advisory Flow

```
Current:
  Gator generate_advisories
    -> scans -candidate tag
    -> matches builds to Jira tickets (fixVersion)
    -> creates/updates Errata advisories
    -> attaches builds
    -> advisory lifecycle: NEW_FILES -> QE -> REL_PREP -> SHIPPED

Target:
  DPAC pipeline (post-compose stage)
    -> script/job scans -candidate tag (or compose manifest)
    -> matches builds to Jira tickets (fixVersion)
    -> creates/updates Errata advisories via ET API
    -> attaches builds
    -> advisory lifecycle: unchanged

  OR: OSCI errata-automation handles this natively
      (investigate OSCI-9642 scope)
```

The errata advisory flow does not fundamentally change. The trigger changes (from Gator CLI invocation to a pipeline stage), but the logic (scan tag, match Jira, create advisory) remains identical.

### 3.7 Grouped Builds / Side Tag Strategy

**Current problem (the STAG gap):** When a library has an ABI break, dependent packages cannot be built against the new version until it completes full gating. Petr proposed a STAG (staging tag) solution, but it was never implemented because RHIVOS lacks the centpkg / Distrobaker / OSCI side-tag infrastructure.

**RoG solution:** RoG natively supports grouped builds via side tags:

1. Developer requests a side tag (or GitLab CI creates one for multi-package MRs)
2. All related packages are built into the side tag
3. The side tag inherits from -build (stable buildroot) plus the new builds
4. Tests run against the side tag content as a group
5. On MR merge: all builds in the side tag are promoted to -candidate together
6. On MR reject: the side tag and all its builds are discarded

This directly solves the companion package problem (downstream-dtbs, qcom-scmi, kernel-ivos-nxp-extra-modules must be rebuilt together with each new kernel). Instead of manual sequential tagging through 2 people, a single MR with a side tag handles the entire group.

**Kernel derivative workflow in RoG:**

```
kernel-ivos-qualcomm MR opened
    |
    +---> Side tag created (inherits from -build)
    |
    +---> kernel-ivos-qualcomm draft build in side tag
    |
    +---> downstream-dtbs rebuilt in same side tag
    +---> qcom-scmi rebuilt in same side tag
    +---> kernel-ivos-nxp-extra-modules rebuilt in same side tag
    |
    +---> All 4 packages tested together (grouped)
    |
    +---> MR merge: all 4 promoted to -candidate together
```

---

## 4. Migration Phases

### Phase 0: Prerequisites (Q3 2026, July - August)

**Goal:** Remove all blockers so that the first package can onboard.

| Task | Owner | Jira | Status | Notes |
|---|---|---|---|---|
| Create -draft Brew build targets for RHIVOS | Ozan Unsal | [VROOM-40774](https://redhat.atlassian.net/browse/VROOM-40774) | New | Blocks everything. Needs targets for 2.1 and 2.0-z streams minimum. |
| Branch naming fix in osci-pipelines | Patrick Talbert | (part of OSCI-9642) | MR !870 exists | Apply same adapter used for Voyager/RHEL4NV. |
| Enable RHIVOS branches in global-tasks.yml | Veronika Kabatova | (part of OSCI-9642) | Not started | Config change in dist-git-gating-tests repo. |
| Layered product support investigation | OSCI (Michal Srb) | File ARR ticket | Not started | Understand what "not straightforward" means concretely. Non-blocking for Phase 1. |
| Spike: Test Console in GitLab CI job | Roni Eliezer | [VROOM-32012](https://redhat.atlassian.net/browse/VROOM-32012) | New | Design the API contract for calling Test Console from GitLab CI. |
| Document advisory generation extraction plan | Kanitha Chim | New ticket needed | Not started | Evaluate OSCI errata-automation vs. standalone extraction from Gator. |
| Hubert knowledge transfer (RoG context) | Kanitha Chim | Part of transition | Overdue | Hubert drove initial OSCI engagement. Capture contacts, design context, open threads. |

**Exit criteria:**

- At least one -draft Brew target exists and is functional
- OSCI pipeline can be triggered for a RHIVOS branch
- Test Console GitLab CI job design is documented (spike complete)
- Advisory generation approach is selected

### Phase 1: Pilot Packages (Q3 2026, August - September)

**Goal:** Onboard 3-5 simple packages to validate the full workflow end-to-end.

| Package | Why pilot | Risk level |
|---|---|---|
| bluechi | Simple, well-understood, active maintainer, no hardware deps | Low |
| qm | Simple, paired with bluechi, same team | Low |
| aboot-deploy | Small, focused scope | Low |
| auto-boot-check | Small, no external dependencies | Low |
| redhat-release-automotive | Config-only package, very low risk | Low |

**Phase 1 activities:**

1. First pilot package opens an MR using the new workflow
2. Validate: draft build creates correctly in Brew
3. Validate: OSCI pipeline runs RPM-level tests
4. Validate: RHIVOS-specific tests (at minimum rpminspect) execute
5. Validate: MR merge promotes draft to -candidate
6. Validate: DPAC pipeline consumes the -candidate build correctly
7. Document any gaps, iterate on CI configuration
8. Run pilot for 2-3 sprints (4-6 weeks) with dual-path: old workflow still available as fallback

**Exit criteria:**

- 3+ packages have completed full end-to-end flow via MR
- DPAC pipeline successfully consumed builds from the new path
- No regressions in compose quality
- Developer feedback collected and addressed
- Runbook written for the new workflow

### Phase 2: Kernel Packages (Q4 2026, October - November)

**Goal:** Onboard kernel-automotive and kernel-ivos-qualcomm with their companion packages, exercising grouped builds.

**Why separate:** Kernel packages have unique requirements: source-git workflow (dist-git policy exceptions), ReportPortal triage integration (being decommissioned Sep 22), companion package rebuilds, grouped build requirement, highest build frequency, and most complex test matrix.

| Package | Special handling |
|---|---|
| kernel-automotive | ReportPortal (expiring), source-git, highest test matrix |
| kernel-ivos-qualcomm | Source-git, companion package trigger |
| downstream-dtbs | Companion rebuild, Anything Goes policy |
| qcom-scmi | Companion rebuild, Anything Goes policy |
| sysboot | Kernel-adjacent |
| fusa-gcc-plugin | FuSa toolchain, tightly coupled |
| fusa-gcc-plugin-data | FuSa toolchain, tightly coupled |

**Phase 2 activities:**

1. Validate side-tag/grouped build workflow with kernel + companions
2. Implement or deprecate ReportPortal integration (depends on decommission timeline)
3. Test hardware board tests triggered from MR pipeline (SA8650, SA8775)
4. Validate Jira ticket enforcement for kernel packages (source-git has different commit patterns)
5. Ensure companion package rebuild automation works via grouped MRs

**Exit criteria:**

- kernel-automotive + companions complete full MR -> grouped build -> compose flow
- Hardware tests run from MR pipeline on at least one board type
- Companion rebuild workflow documented and exercised by kernel team

### Phase 3: Full Onboarding (Q4 2026 - Q1 2027, November - January)

**Goal:** Onboard remaining packages and declare RoG as the primary workflow.

**Remaining packages (9):** aboot-update, android-tools, automotive-image-builder, automotive-image-builder-policy, dracut-automotive, osbuild-auto, ukiboot, unzboot, util-linux-automotive

**Phase 3 activities:**

1. Batch onboarding (3-4 packages per sprint)
2. Disable direct push access to dist-git for onboarded packages
3. Update developer documentation (rhpkg workflow -> MR workflow)
4. Update FDA process docs ("no manual tagging" is now structurally enforced)
5. Train maintainers who have not yet used the MR workflow

**Exit criteria:**

- All 21 packages are onboarded
- Direct push is disabled for all RHIVOS packages
- Developer and FDA documentation updated

### Phase 4: Gator Decommission (Q1 2027, January - February)

**Goal:** Retire Gator evaluate/promote/run_test functions. Transition advisory generation.

**Phase 4 activities:**

1. Parallel running period: keep Gator available but not invoked for onboarded packages
2. Extract or replace advisory generation logic
3. Remove Gator triggers from DPAC pipeline
4. Archive Gator codebase (retain for reference)
5. Clean up -gate tags in Brew (mark as inactive, do not delete)
6. Remove Greenwave policies specific to RHIVOS packages
7. Update all documentation references to Gator

**Exit criteria:**

- Gator is not invoked in any RHIVOS pipeline
- Advisory generation works through the new mechanism
- -gate tags are deprecated
- Greenwave RHIVOS policies are archived
- Gator repository is archived

---

## 5. Risk Register

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Ozan's -draft target creation stalls (VROOM-40774 has no activity since April) | **High** | **Critical** | Escalate through Petr. Set a 2-week deadline. If Brew team is bottleneck, engage RHELBLD directly. |
| R2 | OSCI layered product support is harder than expected (Michal Srb's warning) | Medium | **High** | File ARR ticket immediately. Get concrete requirements list from OSCI. Voyager/RHEL4NV precedent helps but is not identical. |
| R3 | Hubert's departure loses institutional knowledge of RoG design | **High** | Medium | Kanitha has the Toolchain Architect role and motivation. Schedule explicit KT session this week. Capture OSCI contacts and open threads. |
| R4 | Test Console integration in GitLab CI is more complex than expected | Medium | Medium | Roni's spike (VROOM-32012) should surface complexity early. Test Console already pushes directly to ResultsDB (no UMB dependency). |
| R5 | Kernel team resistance to MR workflow (source-git workflow friction) | Medium | **High** | Engage Patrick Talbert and Scott Weaver early. The kernel team already uses MRs for RHEL - RHIVOS is the outlier. Grouped builds solve their companion package pain. |
| R6 | ReportPortal decommission (Sep 22) before Phase 2 reaches kernel | Low | Medium | If decommissioned before Phase 2, the kernel MR pipeline simply omits the ReportPortal check. Already a special case, not the primary gating mechanism. |
| R7 | DPAC pipeline breaks when -candidate is populated differently | Low | **High** | The -candidate tag contents are identical either way - ODCS does not care how builds got there. Validate in Phase 1 explicitly. |
| R8 | Conflux timeline pressure forces shortcuts | Medium | Medium | Conflux requires GitLab integration but does not require all 21 packages onboarded. Phase 1 pilot may satisfy Conflux minimum requirements. Confirm scope with Petr. |
| R9 | Kanitha's internal mobility exploration leads to departure before migration completes | Medium | **High** | Distribution offloading (Aman, Ozan) and Toolchain Architect role are active mitigations. If Kanitha leaves, Juanje (pipeline/gating expertise) or Ozan (Brew/target expertise) can carry the migration. |
| R10 | FDA "no manual tagging" policy interpreted as "no workflow change" | Low | Low | RoG strengthens FDA's policy - it structurally eliminates manual tagging. Frame as an improvement, not a disruption. Engage Martin Perina early. |

---

## 6. Open Decisions

| # | Decision | Who decides | Options | Recommendation | Deadline |
|---|---|---|---|---|---|
| D1 | Should MR-level tests include hardware board tests, or only VM/QEMU? | Petr + Rachel Sibley | (A) VM only in MR, hardware in compose pipeline. (B) VM default, hardware on-demand via label. (C) Always run hardware. | **Option B** - balances cost with coverage. Hardware on-demand for kernel packages. | Before Phase 1 |
| D2 | Should advisory generation use OSCI errata-automation or a standalone Gator extraction? | Kanitha + Petr | (A) OSCI errata-automation. (B) Extract from Gator. (C) New implementation. | **Option A** if OSCI supports RHIVOS. Option B as fallback. | Before Phase 4 |
| D3 | What is the minimum Conflux integration scope that RoG must satisfy? | Petr | (A) All 21 packages. (B) Kernel + bluechi/qm only. (C) Any single package proving the path works. | Clarify with Petr - this determines Phase 1 urgency. | Immediately |
| D4 | Should rhivos-2-main (dev branch) enforce Jira ticket linking in MRs? | Petr | (A) Enforce. (B) Encouraged but not enforced. (C) No requirement. | **Option B** - encourage for errata traceability, do not block development velocity. | Before Phase 1 |
| D5 | Who reviews kernel-automotive MRs? (RHIVOS kernel team? RHEL kernel team?) | Patrick Talbert + Petr | (A) RHIVOS kernel team only. (B) Cross-review with RHEL kernel team. | Consult Patrick - he has the most context on this boundary. | Before Phase 2 |
| D6 | Should the -gate tag be deprecated immediately or kept in parallel? | Petr | (A) Keep -gate active during migration (dual path). (B) Deprecate -gate per phase as packages onboard. | **Option A** for Phase 1-2, **Option B** for Phase 3+. | Before Phase 1 |
| D7 | Is the STAG proposal still relevant, or does RoG side-tags fully replace it? | Petr | (A) STAG is subsumed by RoG side-tags. (B) STAG is still needed for non-RoG use cases. | **Option A** - RoG side-tags are the productized version of what STAG proposed. | Before Phase 2 |

---

## 7. Timeline

```
2026
  July         Phase 0 starts (prerequisites)
  |            - VROOM-40774 (-draft targets) [CRITICAL PATH]
  |            - Branch naming fix merged
  |            - global-tasks.yml enabled
  |            - Hubert KT session (this week)
  |            - VROOM-32012 spike (Test Console in CI)
  |
  August       Phase 0 completes / Phase 1 starts
  |            - First pilot MR (bluechi or qm)
  |            - End-to-end validation
  |
  September    Phase 1 continues
  |            - 3-5 packages validated
  |            - ReportPortal decommissioned (Sep 22)
  |            - Developer runbook published
  |
  October      Phase 2 starts (kernel packages)
  |            - kernel-automotive + companions
  |            - Grouped build validation
  |            - Hardware test integration
  |
  November     Phase 2 completes / Phase 3 starts
  |            - Remaining packages batch onboard
  |
  December     Phase 3 continues
  |            - All 21 packages onboarded
  |
2027
  January      Phase 3 completes / Phase 4 starts
  |            - Direct push disabled
  |            - Gator parallel run begins
  |
  February     Phase 4 completes
               - Gator decommissioned
               - -gate tags deprecated
               - Migration complete

Total duration: ~7 months (July 2026 - February 2027)
Critical path: VROOM-40774 -> Phase 1 pilot -> Phase 2 kernel -> Phase 3 batch -> Phase 4 decommission
```

---

## 8. RACI Matrix

| Activity | Kanitha (Exec) | Petr (PO) | Ozan (Brew) | Patrick (OSCI) | Roni (TC) | Avi (Mgr) |
|---|---|---|---|---|---|---|
| Phase 0: -draft targets | C | A | **R** | I | I | I |
| Phase 0: Branch naming fix | I | I | I | **R** | I | I |
| Phase 0: global-tasks.yml | C | I | I | **R** | I | I |
| Phase 0: TC in CI spike | C | I | I | C | **R** | I |
| Phase 0: Advisory gen plan | **R** | A | I | C | I | I |
| Phase 0: Hubert KT | **R** | C | C | I | I | A |
| Phase 1: Pilot MR workflow | **R** | A | C | C | C | I |
| Phase 1: E2E validation | **R** | I | C | C | C | I |
| Phase 1: Developer runbook | **R** | A | C | I | I | I |
| Phase 2: Kernel onboarding | **R** | A | C | **R** | C | I |
| Phase 2: Grouped builds | **R** | A | **R** | C | I | I |
| Phase 2: HW test in MR | C | I | I | C | **R** | I |
| Phase 3: Batch onboarding | **R** | A | C | I | C | I |
| Phase 3: Disable direct push | C | A | **R** | I | I | I |
| Phase 4: Gator decommission | **R** | A | C | I | I | I |
| Phase 4: Advisory transition | **R** | A | I | C | I | I |
| Stakeholder communication | C | C | I | I | I | **R** |
| Risk escalation | C | C | I | I | I | **R** |

**R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed

**Additional people (Consulted/Informed as needed):**

- Adam Samalik (OSCI PO) - Consulted on OSCI priorities and capacity
- Veronika Kabatova (OSCI) - Consulted on RHIVOS-specific pipeline configuration
- Chris Kelley (OSCI) - Informed on gating-bot decommission alignment
- Rachel Sibley (QE) - Consulted on test scope decisions (D1)
- Michal Srb (OSCI) - Consulted on layered product support (R2)
- Scott Weaver / Patrick Talbert - Consulted on kernel MR workflow (D5)
- Martin Perina - Informed on FDA policy alignment

---

## 9. What This Solves Beyond the Migration

Migrating to RoG is not just a tooling change. It structurally addresses several pain points surfaced during RHIVOS 2.0 RC3:

| # | Problem | How RoG solves it |
|---|---|---|
| 1 | **Tagging knowledge bottleneck** - only Petr + Ozan know release tagging | RoG automates draft-to-candidate promotion. No manual tagging knowledge needed for per-package gating. |
| 2 | **Companion package rebuild chaos** - daily Sameera requests from Eric Chanudet | Grouped builds via side tags handle kernel + companions as a unit. |
| 3 | **Missing audit trail** - kernel team concern, no reviewer on code changes | Every code change has an MR with reviewer, test results, and approval history. |
| 4 | **FDA "no manual tagging" partially enforced** | RoG makes it structurally impossible to manually tag packages into -candidate without going through the MR pipeline. |
| 5 | **Undocumented pre-gate tagging workflow** - 6 gaps from RC3 audit | The -gate tag and its undocumented tagging process are eliminated entirely. |
| 6 | **STAG proposal never implemented** | RoG side tags are the productized, supported version of what STAG proposed. |

---

## Dependencies and Sequencing

```
External dependencies:
  [OSCI-9642]  OSCI team supports RHIVOS components ----+
  [VROOM-40774] -draft Brew targets exist ---------------+---> Phase 0 exit
  [MR !870]    Branch naming adapter merged -------------+
  [OSCI-8454]  Gating-bot decommission timeline ---------+---> Informs Phase 4
  [ReportPortal Sep 22] Decommission --------------------+---> Informs Phase 2

Internal dependencies:
  Phase 0 ---> Phase 1 (prerequisites must be met)
  Phase 1 ---> Phase 2 (pilot validation informs kernel approach)
  Phase 1 ---> Phase 3 (pilot validation informs batch onboarding)
  Phase 2 ---> Phase 4 (kernel is most complex, must be stable before decommission)

Parallel work (not blocking):
  - QC Layered Product can resume independently
  - CAIB integration is orthogonal
  - Conflux integration benefits from but does not block RoG
```

---

*Generated July 14, 2026 | Avihai Efrat, ATC Engineering Manager | Source data: Jira (AUTOBU-1105, VROOM-41188, OSCI-9642), Petr Sabata 1:1 (Jul 14), Gator source analysis, DPAC pipeline review, RHIVOS dist-git workflow documentation*
