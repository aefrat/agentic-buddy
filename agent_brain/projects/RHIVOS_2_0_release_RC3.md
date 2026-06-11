---
last_accessed: 2026-06-11
access_count: 1
created: 2026-06-11
---

# RHIVOS 2.0 Release — RC3

## Status

RC3 build pending — blocked on package tagging and kernel-ivos-nxp-extra-modules build.

## Context

RC2 was built and delivered on 2026-06-08 (both RHIVOS-2.0-Core and RHIVOS-2.0). A kernel config-io-uring fix landed in newer kernel builds but was not included in RC2, causing validator failures that impact FuSa. This necessitates an RC3.

Source: #automotive-release-readiness Slack channel (C04RHEEGY30), 2026-06-08 to 2026-06-10.

## Timeline

| Event | Date | Status |
|---|---|---|
| RC2 Core built | 2026-06-08 | Done |
| RC2 built | 2026-06-08 | Done |
| RC2 reduced-scope CTC scheduled | 2026-06-08 | Done |
| RC3 decision made | 2026-06-10 | Done |
| Blocker tickets approved | 2026-06-10 | Done |
| Package tagging | Pending | Blocked |
| kernel-ivos-nxp-extra-modules build | Pending | Francisco chasing Enric |
| Gating, signing, waiving | Pending | Stephen Bertram to waive |
| Errata attachment | Pending | |
| RC3 build trigger | Target: Friday 2026-06-13 | |
| RC3 reduced CTC | Target: weekend if build ready Fri, else ~Wed 2026-06-18 | |
| Release readiness sync meeting | 2026-06-11 | Moved from 2026-06-10 |

## RC3 Open Items — Resolution Plan

### 1. Build kernel-ivos-nxp-extra-modules

- **Status:** Not built. Was missed from RC2 entirely.
- **Who:** Francisco da Rocha → Enric (kernel module maintainer)
- **How:** Enric needs to trigger a Brew build of kernel-ivos-nxp-extra-modules against the new kernel (`6.12.0-211.20.1`). OOT kernel modules must be rebuilt when the base kernel changes. Once built, tag into `rhivos-2.0-gate` / `rhivos-2.0-core-gate` Brew tags.
- **Risk:** This is the critical-path blocker — nothing downstream can proceed until the build exists. If Enric is unavailable, Francisco or the kernel team (`rhivos-ft-auto-kernel`) need to own this.

### 2. Tag packages into Brew release tags

- **Status:** Builds exist for kernel-automotive, kernel-ivos-qualcomm, downstream-dtbs, qcom-scmi. Not yet tagged.
- **Who:** Francisco da Rocha (kernel packages) + Ozan Unsal / Kanitha Chim (toolchain coordination)
- **How:** Use `brew tag-build` to tag the following NVRs into the appropriate `-gate` tags:
  - `kernel-automotive-6.12.0-211.20.1.el10_2iv` → `rhivos-2.0-gate` and `rhivos-2.0-core-gate`
  - `kernel-ivos-qualcomm-6.12.0-211.20.1.43.el10_2iv` → `rhivos-2.0-gate` and `rhivos-2.0-core-gate`
  - `downstream-dtbs` (matching version) → same tags
  - `qcom-scmi` (matching version) → same tags
  - `kernel-ivos-nxp-extra-modules` (once built) → same tags
- **Note:** Tagging into `-gate` feeds Gator's automated evaluation pipeline. Gator diffs source vs. target tags and evaluates against Greenwave policies.

### 3. Gating — Greenwave policy evaluation

- **Status:** Blocked on tagging (step 2).
- **Who:** Automated (Gator) + Stephen Bertram (waiving)
- **How:** Once packages are tagged into `-gate`, Gator automatically:
  1. Evaluates new packages against Greenwave policies
  2. Checks ResultsDB for test results (Test Console hardware tests)
  3. If all pass → auto-promotes to `-candidate` tag
  4. If failures → generates WaiverDB URLs in Slack notifications
- **Waiving:** Since this is a config-only kernel change (io-uring), the kernel test results from RC2 may be referenced. Stephen Bertram can submit waivers via WaiverDB links that Gator posts to Slack. For kernel-automotive specifically, Gator has a special path: it checks ReportPortal for triage status — if all failures have BTS links, auto-promotes.
- **Risk:** If smoke tests must run fresh on new kernel builds, waiving alone won't suffice — the pipeline will need to run hardware tests. Confirm with Stephen/Rachel whether the config-only change qualifies for waiver or requires re-test.

### 4. Signing

- **Status:** Blocked on gating (step 3).
- **Who:** Automated (Brew/Errata Tool)
- **How:** Signing happens automatically when builds are attached to errata advisories via Gator's `generate-advisories` command. The Errata Tool triggers PQC (Package Signing Certificate) signing on attachment. No manual signing step is needed — but builds must be in `-candidate` tag first (i.e., gating must pass).
- **Note:** Kanitha Chim confirmed RC2 kernel builds were signed before pipeline trigger. Same flow applies to RC3.

### 5. Attach to Errata

- **Status:** Blocked on signing/gating (steps 3-4).
- **Who:** Automated (Gator) + manual verification using errata-distribution scripts
- **How:**
  1. **Gator auto-path:** `gator generate-advisories` finds passing packages, checks for existing advisories in `NEW_FILES` state, attaches builds. Requires valid VROOM Jira issues with correct `fixVersion`.
  2. **Manual verification:** Use `errata-distribution` scripts to confirm:
     - `fetch_batch_builds.py` — pull current batch state (FuSa batch 4254, Core batch 4576)
     - `compare_batch_compose_repos.py` — diff batch NVRs vs. RC3 compose once available
     - `sync_batch_compose_builds.py` — sync any mismatches (add/remove builds)
  3. **Important:** FuSa and Core batches are separate — never cross-contaminate. FuSa = `RHIVOS-2.0.0` (batch 4254), Core = `RHIVOS-2.0.0-Core` (batch 4576).
- **Blocker tickets to link:** VROOM-41703, VROOM-41942, VROOM-44420, VROOM-44421 must be linked to the advisories via `add_jira_issues()`.

### 6. Create RC3 release config and trigger pipeline

- **Status:** Blocked on steps 1-5.
- **Who:** Ozan Unsal (pipeline trigger) + Kanitha Chim (build coordination)
- **How:**
  1. **Create release config:** Add `RHIVOS-2.0-Core-RC3.yml` and `RHIVOS-2.0-RC3.yml` in `downstream-pipelines-as-code/.gitlab/release-configs/`. Clone from RC2 configs, update `RELEASE_NAME` and any component pins.
  2. **Create git tag:** In `rhivos.git`, create tags `RHIVOS-2.0-Core-RC3` and `RHIVOS-2.0-RC3`. This automatically triggers the GitLab CI pipeline in DPAC.
  3. **Pipeline stages:** `generate-compose` (ODCS, 10-30 min) → `check-repoclosure` → `build-*-image` (per board) → `smoke-tests-*` → `promote-packages-in-brew` (Gator).
  4. **Monitor:** Track pipeline at `https://gitlab.cee.redhat.com/automotive/pipe-x/rhivos/-/pipelines` filtered by tag.

### 7. RC3 CTC (Confidence Test Cycle)

- **Status:** Blocked on RC3 build (step 6).
- **Who:** Rachel Sibley (scheduling) + Luigi Pellecchia / Roni Eliezer (execution)
- **How:** Rachel to schedule reduced-scope CTC against RC3 compose. Based on RC2 plan:
  - **Reduced scope areas:** smoke core tests, smoke fusa-minimal, aib, fusa-gcc-plugin, auto-boot-check, qm
  - **Hardware:** 8650 + 8775 boards
  - **Timeline:** If RC3 ready by Friday → run over weekend. If Monday → results ~Wednesday.
  - Rachel should also confirm with FuSa team (Pavol Brilla) if FDA tests need to re-run given config-only change.

---

## Other Open Issues — Resolution Suggestions

### VROOM-42325 — Reboot failure on Renesas R-Car S4 (~32% success)

- **Severity:** High — affects CI reliability.
- **Who:** Dustin Black (reporter) + kernel team (`rhivos-ft-auto-kernel`)
- **Suggested resolution:** Needs root-cause analysis — is this a kernel regression, firmware issue, or Test Console infrastructure problem? If kernel: check if the 211.20.1 kernel fixes it (config-io-uring change may be unrelated). If infra: escalate to Test Console team. Either way, this should not block RC3 — but needs a decision on whether to waive Renesas reboot tests for RC3 CTC or investigate first.
- **Action:** Dustin to add findings to VROOM-42325. Stephen Bertram to decide on waiver for RC3.

### Crosscompiler errata — ppc64le/s390x debuginfo bundled

- **Who:** Kanitha Chim (investigating) + Petr Sabata (crosscompiler owner)
- **Suggested resolution:** The gcc/binutils advisories are pulling in debuginfo for architectures not relevant to RHIVOS (ppc64le, s390x). This is likely a Brew build configuration issue — the advisory is including all arches from the RHEL build, not filtering to RHIVOS-relevant arches (aarch64, x86_64). Kanitha should check if the advisory product_version filtering in Gator config is correct, or if the Brew build itself is multi-arch and needs arch-specific advisory splitting.
- **Non-blocking:** This doesn't block RC3 but needs resolution before GA.

### Crosscompiler sysroot — decision captured

- **Status:** Resolved — Carlos decided sysroot packages won't ship. Petr confirmed customers should use `dnf --installroot` from target repos.
- **Action:** Luigi Pellecchia to update internal test procedures to use `dnf --installroot` instead of relying on sysroot RPMs. Close the discussion in VROOM-39911.

---

## Critical Path Summary

```
kernel-ivos-nxp-extra-modules build (Francisco/Enric) ──┐
                                                         ├─→ Tag all packages (Francisco/Ozan)
Existing builds (kernel, dtbs, qcom-scmi) ───────────────┘         │
                                                                    ▼
                                                         Gating (Gator auto + Stephen waive)
                                                                    │
                                                                    ▼
                                                         Signing (Errata Tool auto)
                                                                    │
                                                                    ▼
                                                         Errata attachment (Gator auto + verify)
                                                                    │
                                                                    ▼
                                                         RC3 release config (Ozan/Kanitha)
                                                                    │
                                                                    ▼
                                                         Pipeline trigger (git tag → DPAC)
                                                                    │
                                                                    ▼
                                                         CTC scheduling (Rachel)
```

**Single point of failure:** kernel-ivos-nxp-extra-modules build. Everything else is ready or automated.

## Process Gaps Identified

### No documented owner for initial Brew tagging into `-gate`

The rhivos-workflows-wiki documents Gator's automated promotion (`-gate` → `-candidate` → `-pending`) thoroughly, but **who tags builds into `-gate` in the first place is undocumented**. The wiki says "maintainer builds land in `-gate`" and "maintainer mass-tags into `-gate` when ready" — but there's no RACI, no named role, no checklist for RC scenarios where existing builds need manual tagging.

In the RC3 Slack thread, this fell on Francisco (kernel maintainer) and Ozan (pipeline engineer) ad-hoc. This is tribal knowledge, not process.

**Recommendation:** Raise in the 2026-06-11 release readiness meeting. Propose:
- Document the owner for initial `-gate` tagging in the wiki (likely: package maintainer for their component, toolchain team for coordination)
- Add a pre-RC checklist step: "Confirm all required NVRs are tagged into `-gate`" with named responsible party
- Consider automating: Gator could accept a "tag these NVRs into `-gate`" command or the RC release config could include a required-NVR list that the pipeline validates before compose

## Kernel Change (RC2 → RC3)

- RC2 shipped: `kernel-automotive-6.12.0-211.18.1.el10_2iv` / `kernel-ivos-qualcomm-6.12.0-211.18.1.41.el10_2iv`
- RC3 target: `kernel-automotive-6.12.0-211.20.1.el10_2iv` / `kernel-ivos-qualcomm-6.12.0-211.20.1.43.el10_2iv`
- Only change: config-io-uring fix. No other kernel changes.

## Blocker Tickets

| Ticket | Scope | Status |
|---|---|---|
| [VROOM-41703](https://redhat.atlassian.net/browse/VROOM-41703) | rhivos-2.0-core / kernel-automotive | Approved blocker |
| [VROOM-41942](https://redhat.atlassian.net/browse/VROOM-41942) | rhivos-2.0 / kernel-ivos-qualcomm | Approved blocker |
| [VROOM-44421](https://redhat.atlassian.net/browse/VROOM-44421) | rhivos-2.0 / kernel-automotive | Approved blocker (new) |
| [VROOM-44420](https://redhat.atlassian.net/browse/VROOM-44420) | rhivos-2.0-core / kernel-ivos-qualcomm | Approved blocker (new) |

## Documentation Review

FDA team (Meital Arki) completing first review of 6 docs by end of week 2026-06-13:
- RHIVOS Core Deployment and Platform Integration (MR214)
- RHIVOS Core Platform Updates (MR212)
- RHIVOS Core Getting Started & Core Concepts (MR204)
- RHIVOS Core Application Development and Integration (MR217)
- RHIVOS Core Image Building (MR218)
- Platform Security (MR222)

## Key People

| Person | Role in RC3 |
|---|---|
| Ozan Unsal | Pipeline trigger and build execution |
| Kanitha Chim | Build coordination, crosscompiler investigation |
| Francisco da Rocha | Kernel builds, tagging, blocker tickets |
| Enric Balletbo i Serra | kernel-ivos-nxp-extra-modules build (critical path) |
| Rachel Sibley | QE coordination, CTC scheduling |
| Jaime Flynn | Release management, blocker tracking |
| Stephen Bertram | Build waiving (Greenwave/WaiverDB) |
| Luigi Pellecchia | Crosscompiler testing |
| Petr Sabata | Crosscompiler/sysroot decisions |
| Whitney Chadwick | Release readiness meeting lead |
| Dustin Black | CI reboot bug reporter (VROOM-42325) |
| Meital Arki | Docs review coordination (FDA) |
| Pavol Brilla | FDA/FuSa test readiness |
