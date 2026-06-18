---
last_accessed: 2026-06-18
access_count: 5
created: 2026-06-11
---

# RHIVOS 2.0 Release — RC3

## Status

**RC3 composes built and published (2026-06-16).** CTC reduced-scope in progress, ASIL-B CTC weekend Jun 19. Errata push to CDN in progress. Z-stream becomes the right target starting Jun 19.

## Context

RC2 was built and delivered on 2026-06-08 (both RHIVOS-2.0-Core and RHIVOS-2.0). A kernel config-io-uring fix landed in newer kernel builds but was not included in RC2, causing validator failures that impact FuSa. This necessitates an RC3.

Source: #automotive-release-readiness Slack channel (C04RHEEGY30), 2026-06-08 to 2026-06-11.

## Timeline

| Event | Date | Status |
|---|---|---|
| RC2 Core built | 2026-06-08 | Done |
| RC2 built | 2026-06-08 | Done |
| RC2 reduced-scope CTC scheduled | 2026-06-08 | Done |
| RC3 decision made | 2026-06-10 | Done |
| Blocker tickets approved | 2026-06-10 | Done |
| Package tagging | 2026-06-15 | Done — kernel-automotive, qcom-scmi, kernel-nxp, downstream-dtbs tagged to rhivos-2.0-candidate (Kanitha). kernel-ivos-nxp-extra-modules tagged from sidetag (Eric → Sameera) |
| kernel-ivos-nxp-extra-modules build | 2026-06-15 | Done |
| kernel-ivos-nxp-extra-modules errata | 2026-06-15 | Done — advisory/167239 created by Francisco |
| Gating, signing, waiving | 2026-06-15 | Done |
| Errata attachment | 2026-06-15 | Done — Kanitha updated kernel errata builds from 211.18 to 211.20 |
| RC3 pipelines triggered | 2026-06-16 | Done — Core (#15973730) and full (#15974617) by Ozan |
| RC3 composes published | 2026-06-16 | Done — live on rhivos.auto-toolchain.redhat.com |
| Gator bug fix (version-release matching) | 2026-06-15 | Done — MR #248 merged (Juanje) |
| RC3 reduced CTC | 2026-06-16 | In progress — VM + 8650 done, 8775 re-triggered after provisioning failures |
| Errata push to CDN | 2026-06-17 | In progress — Kanitha re-pushing Core batch to CDN-stage → REL_PREP |
| ASIL-B CTC (weekend) | 2026-06-19 | Scheduled — Rachel Sibley |
| Release readiness sync meeting | 2026-06-11 | Done — see outcomes below |

### Release Readiness Meeting Outcomes (2026-06-11)

- **RC3 data tickets:** [VROOM-44420](https://redhat.atlassian.net/browse/VROOM-44420), [VROOM-44421](https://redhat.atlassian.net/browse/VROOM-44421)
- **Testing plan:** kernel gating + smoke testing (~2 days)
- **NXP syncing:** AI on Francisco to confirm what needs to be done
- **New CVEs:** RHEL is fixing. RHIVOS will take the fix into RC3 if RHEL resolves within 24h. Build is held until RHEL confirms.
- **Francisco:** to file RHIVOS proposed blocker tickets (Core version, 2.0 version, both kernel version tickets)
- **Decision:** go/no-go on Monday 2026-06-16

## RC3 Open Items — Resolution Plan

### 1. Build kernel-ivos-nxp-extra-modules + create its errata

- **Status:** Not built. Was missed from RC2 entirely.
- **Who:** Enric Balletbo / Francisco da Rocha (kernel module maintainers), Mattijs Korpershoek (package expert)
- **How:** Enric needs to trigger a Brew build of kernel-ivos-nxp-extra-modules against the new kernel (`6.12.0-211.20.1`). OOT kernel modules must be rebuilt when the base kernel changes. Once built, tag into `rhivos-2.0-gate` / `rhivos-2.0-core-gate` Brew tags.
- **Update 2026-06-11:** Kanitha confirmed this package is **NOT a subpackage of kernel-ivos** — it's built independently via CBS ([CBS](https://cbs.centos.org/koji/packageinfo?packageID=11920) / [Brew](https://brewweb.engineering.redhat.com/brew/packageinfo?packageID=88898)). See [RHICIL-45](https://redhat.atlassian.net/browse/RHICIL-45) for package description. Because it's independent, it **needs its own errata advisory** with the NVR attached. Mattijs confirmed this but doesn't know how to create the advisory — Enric or Francisco need to do it.
- **Risk:** This is the critical-path blocker — nothing downstream can proceed until the build exists AND its errata is created. If Enric is unavailable, Francisco or the kernel team (`rhivos-ft-auto-kernel`) need to own this.

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

- **Status:** Scheduled (Rachel Sibley, confirmed June 12 in #forum-qe-automotive).
- **Who:** Rachel Sibley (scheduling) + QE team (execution)
- **Plan (two phases):**
  - **Monday June 16** (once RC3 build available): Reduced CTC against 2.0 Core RC3 — smoke, kernel gating, systemd, a-b-c. Hardware: 8650 / 8775 / QEMU.
  - **Friday June 19** (weekend CTC): Full 2.0 ASIL Release CTC + Kernel Debug for 8650 (FuSa evidence).
- **Additional tests requested:** Stephen Bertram asked to add kselftests + LTP.
- **RC1/RC2 ticket closure:** Rachel extended deadline to mid next week (was end of this week). 100% pass not required — follow-up JIRAs for unstable tests.

---

## Slack Updates (2026-06-15 to 2026-06-18)

### Nightly Pipeline Failures

- **ODCS unsigned packages (Jun 16):** Nightly pipeline for latest-RHIVOS-2.0-Core (#15970648) failed at `generate-compose`. Root cause: newly promoted kernel packages (6.12.0-211.20.1.43) missing required signatures. ODCS rejected the config. Packages affected: kernel-ivos-qualcomm, downstream-dtbs. Flagged to Ozan.
- **Smoke test timeouts (Jun 16-17):** Multiple smoke tests timed out on ride4-sa8775p-sx-r3 (~7200s waiting for Jumpstarter/TF). Root cause: board provisioning failures. Also sa8650p affected on Core.
- **20+ pipeline failure alerts** in alerts-auto-toolchain since Jun 15 — mostly related to the same provisioning issues.

### Test Console 502 Bad Gateway — RESOLVED

- Ozan reported 502 in RC3 smoke-tests (Jun 16). Roni restarted TC to update it with RC3. Resolved.

### CTC Progress (Jun 16-17)

- Rachel triggered reduced-scope CTC (Jun 16). 8775 provisioning failures resolved, jobs re-triggered.
- Pato Brilla flagged: smoke tests in RC3 CTC only run against VM, not HW — asked if intentional. Flagged to Roni/nsimsolo.
- Ben Grech: kself and ltp tests failed to provision on 8775 (retriggered). TC was showing 502.

### aarch64 RPM Signature Issue — NOT A BLOCKER

- Petr Sabata (Jun 17): packages appear to have invalid signatures on aarch64, but reinstalling resolves it. Only affects builds signed after Jan 16. Suspects automotive-image-builder rpmdb handling. No minimal reproducer yet.

### CDN Product ID Push Issue — RESOLVED

- Kanitha (Jun 16, rhivos-sp-qc-layered-product): product IDs not pushing to CDN repo. Created RHELDST-42168. Resolved by Michal.

### RHIVOS-2.0 Label Not Yet Promoted

- Marcin Sobczyk noticed RHIVOS-2.0 still points to a Jun 8 pipeline (not yet promoted from RC3). `latest-RHIVOS-2.0` based on an older pipeline than RC3. Ozan clarified: RHIVOS-2.0 is a copy of the current RC; `latest-*` are nightly builds.

### Security Response — CI Leak for AIB

- Charles Timko asked about security response handling (Jun 16). Juanje pointed to private channel related to a CI leak for automotive-image-builder. Timko was added.

---

## Other Open Issues — Resolution Suggestions

### VROOM-42325 — Reboot failure on Renesas R-Car S4 (~32% success)

- **Severity:** High — affects CI reliability.
- **Who:** Dustin Black (reporter) + kernel team (`rhivos-ft-auto-kernel`)
- **Suggested resolution:** Needs root-cause analysis — is this a kernel regression, firmware issue, or Test Console infrastructure problem? If kernel: check if the 211.20.1 kernel fixes it (config-io-uring change may be unrelated). If infra: escalate to Test Console team. Either way, this should not block RC3 — but needs a decision on whether to waive Renesas reboot tests for RC3 CTC or investigate first.
- **Action:** Dustin to add findings to VROOM-42325. Stephen Bertram to decide on waiver for RC3.

### PLM ghost listings — cross-compiler debuginfo in errata (RHELWF-14266)

- **Who:** Kanitha Chim (reporter) + Lukas Holecek (PLM team, assigned)
- **Root cause (verified 2026-06-14):** PLM auto-generates product listings from Brew build contents, not from compose trees. The `binutils-2.41-63.el10` Brew build produces `cross-binutils-{aarch64,ppc64le,s390x}-debuginfo` sub-packages. PLM lists them for the `RHIVOS-2.0.0-Core` product even though they're not in any RHIVOS compose. This is a known RHEL-wide issue (RHELWF-11979, 8+ prior occurrences). RHIVOS 1.x (`9Base-RHIVOS-1.0.0`) has the same ghost entries — they were never noticed.
- **Fix applied:** Lukas added PLM overrides for `cross-binutils-ppc64le-debuginfo` and `cross-binutils-s390x-debuginfo` on x86_64 for `RHIVOS-2.0.0-Core`. The `aarch64` cross entry remains.
- **RC3 impact:** When RC3 compose runs product listing, new overrides should suppress the ppc64le/s390x entries. However, if new builds land (gcc, other cross-compiler packages), the same issue may recur. Kanitha is asking Lukas about a delete-and-reimport approach for a systemic fix.
- **Non-blocking:** Doesn't block RC3 build, but affects errata correctness before push to CDN.

### Z-stream tagging process conflict (Eric Chanudet, Jun 11-12)

- **Status:** Unresolved. Nightly 2.1 composes breaking as of Jun 12.
- **Who:** Eric Chanudet (downstream-dtbs, qcom-scmi, nxp-extra-modules maintainer), Sameera Kalgudi (manual tagger), Petr Sabata (release/distribution), Oleksii Baranov (kernel-ivos-qualcomm builds), Martin Perina (raised process concern from RR meeting), Francisco da Rocha (escalation path)
- **Problem:** Eric must rebuild companion packages (downstream-dtbs, qcom-scmi, kernel-ivos-nxp-extra-modules) every time a new kernel-ivos-qualcomm build lands. He doesn't control which tag the kernel uses — the kernel lands in `rhivos-2.0-z` or `rhivos-2.1` tags, and he must match. But:
  1. He has no permission to tag directly — must request Sameera daily
  2. The process is undocumented — no RACI for who tags companion packages
  3. Inconsistency across kernel maintainers, QE, and distribution
- **Escalation (Jun 12):** Eric escalated to managers via Francisco. Martin Perina cited RR meeting: "tagging is the builder's responsibility." Eric pushed back: he doesn't build the kernel, he reacts to it.
- **Petr's guidance:** Clarified 2.0 (blockers only, finalizing by Jun 18) vs 2.0-z (update channel, more visible to customers) vs 2.1 (rolling development). Needs to understand Oleksii's kernel target flow before resolving.
- **Root cause (2026-06-18):** RHEL kernel maintainers (Oleksii Baranov and/or Scott Weaver) build packages following a RHEL workflow/rules that are not aligned to RHIVOS. This causes unnecessary packages landing in the wrong RHIVOS release tags, driving the daily manual tagging burden on Eric/Sameera. The cross-product workflow mismatch is the deeper issue behind the tagging permission bottleneck.
- **Petr Sabata response (2026-06-18):** Confirmed the RHEL/RHIVOS workflow misalignment is likely the situation. Has not yet reached out to RHEL KWF team. Plans a meeting with the RHIVOS kernel team, RHEL KWF team, and himself to come up with a solution. Also noted: starting Thursday (2026-06-19), Z-stream becomes the right target, which will reduce the problem "for a year or so" (until the next major release cycle). Tagging guidance (which tag, when) is **not documented** — confirmed gap.
- **Avi's mitigation (2026-06-18):** Discussed on ATC weekly — getting broader Brew tag permissions for ATC and auto-kernel teams so others can help when Sameera/Ozan are on PTO. Filed RHELBLD-18777 and RHELBLD-18778.
- **Additional blocker:** `kernel-ivos-nxp-extra-modules` has no dist-git policy exception (unlike downstream-dtbs and qcom-scmi), requiring a VROOM ticket for every commit. Controlled by RHELBLD team (RHELBLD-18043).
- **RC3 impact:** The kernel CVE fix for RC3 will trigger companion rebuilds. If tagging isn't aligned, companion packages may be missing from RC3 compose or 2.0-z updates. STAG automation (which would fix this) is not in place.
- **Suggested resolution:** Alignment meeting between Eric, Oleksii, Petr, and Sameera to standardize tagging flow. Get dist-git policy exception for nxp-extra-modules. Prioritize STAG automation.

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

**Additional risk (2026-06-14):** Z-stream tagging process unresolved. Eric Chanudet's companion packages (downstream-dtbs, qcom-scmi, nxp-extra-modules) require manual tagging with no permissions, no automation (STAG not ready), and no dist-git policy exception for nxp-extra-modules. The RC3 kernel CVE fix will trigger companion rebuilds that depend on this broken process.

## Process Gaps Identified

### Tagging documentation audit (2026-06-14)

Audited three repos (ATC_Team_codebase_docs, errata-distribution, rhivos-workflows-wiki), the full [Product Development and Release](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196280075) Confluence tree (9 teams, 80+ pages including [Auto Toolchain](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196281018), [Release Management](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196276699), Kernel/HW Enablement, FDA, BOA QE, Base Enablement, PitCrew, PIT, Product Security), the [ATC Distribution FA wiki](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/402130012), the [developer-guide](https://gitlab.cee.redhat.com/developer-guide/developer-guide) GitLab repo, the [RCMDOC Confluence space](https://redhat.atlassian.net/wiki/spaces/RCMDOC/), and the [brew-confs hub_policy.conf](https://gitlab.cee.redhat.com/brew/brew-confs/blob/master/src/conf/hub_policy.conf) for tagging policy and permission documentation.

#### What IS documented

| Area | Where | Notes |
|---|---|---|
| Gator `-gate` → `-candidate` → `-pending` | ATC codebase docs: `gator.md` | Fully automated, Greenwave policies, kernel-automotive ReportPortal path |
| Release pipeline (git tag → compose → CDN) | Wiki: `release-planning.md` | "Fully automated from tag creation to CDN delivery" |
| Brew tag structure diagram | Wiki: `rhivos-release-approach.md:182-195` | `-gate` → evaluate → `-candidate` → compose → promote → `-pending` |
| STAG proposal (lockstep builds) | Wiki: `rhivos-release-approach.md:205-213` | Petr Sabata's proposal — **not implemented**. Would give maintainers a per-version stag tag, mass-tag to `-gate` when ready. Connected to AUTOBU-1076 (QC LP lockstep). |
| RHEL side-tags don't apply to RHIVOS | Wiki: `rhivos-release-approach.md:201-203` | RHIVOS lacks centpkg, Distrobaker, ROG CI, OSCI, build-group Jenkins |
| RHEL→RHIVOS tag inheritance | Confluence: [RHEL & RHIVOS gating process](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/387157013) | Dev phase: `-gate` inherits from `rhel-*-pending` automatically. Blocker phase: inheritance frozen, RHEL builds must be "added manually" — **no owner named**. |
| Brew tag creation for new releases | Confluence: [Release Checklist Template](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196276995) | Task 260: "Create the new tag rhivos-x.y.z in Brew" assigned to `#wg-team-auto-toolchain-release`. This is tag structure setup, not per-package tagging. |
| Release ROTA + actors | Confluence: [Release Documentation](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196269228) | ATC team rotates release coordinator + assistant. Auto Kernel Team "provides packages" but no tagging RACI. |
| Gator design principles | Confluence: [Package Gating > Design](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196273404) | Gator evaluates + promotes. Explicitly stateless — relies on Brew, ResultsDB, WaiverDB. |
| Release configs matrix | Confluence: [Release configs matrix](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196275486) | Maps RHEL/RHIVOS versions ↔ Brew tags ↔ git branches ↔ Gator configs. Reference, no ownership info. |
| Manual freeze for RHIVOS 2.0 | Confluence comment on [gating process page](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/387157013) (387292638) | "We removed the tag inheritance of rhel-10.2-pending from rhivos-2.0-gate... need to list the builds in release tag and tag the builds in rhivos-2.0-candidate and rhivos-2.0-pending." Describes the freeze but not who does it. |
| RHEL: build system tags to `-gate` | [developer-guide](https://gitlab.cee.redhat.com/developer-guide/developer-guide): `con_understanding-gating.adoc` | "The build system tags the build to the `rhel-8.x.y-gate` tag in Brew." Automatic for RHEL — no equivalent automation for RHIVOS. |
| RHEL: side-tags workflow | developer-guide: `proc_working-with-side-tags.adoc` | RHEL uses `centpkg request-gated-side-tag` → Distrobaker → `build-group-trigger` Jenkins → lands in `-candidate`. RHIVOS has **none** of this tooling. |
| RHIVOS maintenance/post-release | developer-guide: `assembly_maintenance-and-post-release-processes.adoc` | **Stub** — literally says "Placeholder waiting for info" for the RHIVOS variant. No RHIVOS-specific procedures documented. |
| ATC Distribution pipeline (Errata→CDN) | Confluence: [ATC Distribution FA wiki](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/402130012) (10+ pages) | Comprehensive docs on advisory lifecycle, signing, CDN push, automation scripts. Covers everything AFTER builds are in Brew tags — nothing about how they get into `-gate`. |
| Brew standard tag permissions | RCMDOC: [Unified Brew Tagging Structure](https://redhat.atlassian.net/wiki/spaces/RCMDOC/pages/296845952) | Canonical permission model: main tag = `admin`, `-candidate` = no perms (anyone can tag), `-pending`/`-compose`/`-override` = `trusted`. **No `-gate` tag in the standard structure** — it's a RHEL 9+/RHIVOS gating-era addition not covered by RCM docs. |
| Brew permission types | EXDSPRHELB: [Permissions in Brew](https://redhat.atlassian.net/wiki/spaces/EXDSPRHELB/pages/175083555) | Authoritative reference. Permissions govern tag access: if a tag has a perm set, users must hold it to tag/untag. `admin` = root-like, `trusted` = rel-eng ops. Custom perms can be created per tag. |
| RHEL gating bypass | EXDSPRHELB: [Bypassing OSCI gating](https://redhat.atlassian.net/wiki/spaces/EXDSPRHELB/pages/175079794) | For RHEL, builds auto-land in `-gate`; packages that can't pass OSCI use `-gate-bypass` tag. Requires `rhel8-gate-bypass` permission, requested via RHELBLD JIRA ticket with PM as watcher. Whitelist per package. **No RHIVOS equivalent documented.** |
| Brew whitelisting | RCMDOC: [Add a package to a Brew tag](https://redhat.atlassian.net/wiki/spaces/RCMDOC/pages/296845847) | Whitelisting (adding package to tag's package list) requires `package-list` or `admin` permission. Always whitelist on main tag, not `-candidate`. |
| RHIVOS package onboarding workflow | Confluence: [Package workflow for AutoSD/RHIVOS-only packages](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196270957) | Step-by-step: VROOM ticket for dist-git repo + VROOM ticket for Brew whitelist → sync git from AutoSD → `rhpkg build --target rhivos-1.0.0-gate` → build lands in `-gate` → Gator picks up → `-candidate`. **Maintainer builds against `-gate` target directly; no manual tagging needed for standard flow.** Notes DistroBaker automation "in the future." |
| FDA: "no manual tagging" policy | Confluence: [Release Process for FDA packages](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196282794) | Explicit policy: *"At any point you are not supposed to tag builds manually in brew! All tagging is done by the Toolchain automation."* Branch/target table shows 2.x targets as `-candidate` (not `-gate`). Contact ATC team if builds don't get tagged. |

#### What is NOT documented — 6 gaps

**1. Who tags packages INTO `-gate`.**
Every doc assumes packages are already in `-gate`. The wiki says "maintainer mass-tags into `-gate` when ready" (`rhivos-release-approach.md:210`) — but no RACI, no named role, no permissions guidance, no command reference. In practice: Eric requests Sameera daily; for RC scenarios, Francisco and Ozan do it ad-hoc.

**2. Brew tagging permissions — RESOLVED via hub_policy.conf.**
The actual Brew hub policy ([brew-confs repo](https://gitlab.cee.redhat.com/brew/brew-confs/blob/master/src/conf/hub_policy.conf)) defines three RHIVOS-specific permissions:

| Permission | RHELBLD ticket | What it allows |
|---|---|---|
| `rhivos-tagger` | RHELBLD-12926 | Tag builds from RHEL release/candidate tags into any `rhivos-*` tag. Move builds between RHIVOS tags. Move from `rhel-9*` to `rhivos-*`. |
| `pkglist-rhivos` | RHELBLD-12234 | Whitelist packages in any `rhivos-*` tag (package list management). |
| `auto-toolchain-service-brew` (service account) | RHELBLD-17225 | Tag/untag Konflux-built packages in any `rhivos-*` tag. |

Additionally, anyone with the general `tagger` permission (RHELBLD-8760) can tag almost anything anywhere.

Eric's "we have no permission to tag" means the kernel team lacks `rhivos-tagger`. To get it: file a RHELBLD JIRA ticket requesting `rhivos-tagger` permission for the relevant Kerberos IDs. Sameera Kalgudi presumably has `rhivos-tagger` or uses the `auto-toolchain-service-brew` account.

**Mitigation (2026-06-18):** Avi opened two RHELBLD tickets to extend tag permissions and unblock the bottleneck (only Sameera and Ozan currently have permissions to tag kernel packages in the release):
- [RHELBLD-18777](https://redhat.atlassian.net/browse/RHELBLD-18777) — Brew tag permissions for RHIVOS kernel maintainers
- [RHELBLD-18778](https://redhat.atlassian.net/browse/RHELBLD-18778) — Brew permission request for RHIVOS Auto-Toolchain team

Both tickets aim to extend tag permissions for the ATC and RHIVOS kernel maintainer teams.

The RCMDOC/EXDSPRHELB spaces document the general Brew permission system but have zero RHIVOS-specific content — the RHIVOS permissions are only discoverable by reading the raw hub_policy.conf.

**3. Side-tag workflow for companion packages.**
Eric's daily workflow (rebuild downstream-dtbs/qcom-scmi/nxp-extra-modules against each new kernel-ivos-qualcomm) is completely undocumented. He is the only person who knows it. No automation exists.

**4. dist-git policy exceptions.**
Policy at `pkgs.devel.redhat.com/rules.html`, controlled by RHELBLD team (RHELBLD-18043). Most RHIVOS repos got exceptions; `kernel-ivos-nxp-extra-modules` didn't. No RHIVOS-side documentation of which repos have exceptions. Every commit to a non-exempted repo requires an approved VROOM ticket in the commit message.

**5. 2.0 vs 2.0-z vs 2.1 tagging guidance.**
Petr explained the structure in Slack only (Jun 12): 2.0 = initial release (blockers only, finalizing Jun 18), 2.0-z = update channel (more visible to customers), 2.1 = rolling development (rhivos-2-main branch). No written guide for which kernel builds should target which tag.

**6. Companion package rebuild triggers.**
No documentation that downstream-dtbs, qcom-scmi, and nxp-extra-modules must be rebuilt for every new kernel-ivos-qualcomm build. No automation. The STAG proposal would solve this but isn't implemented.

#### Impact on RC3

The kernel CVE fix for RC3 will trigger companion package rebuilds. These rebuilds depend on gaps 1-4:
- Eric must rebuild companion packages (gap 3 — undocumented workflow)
- Someone must tag them into `-gate` (gap 1 — no documented owner)
- Eric has no tagging permissions (gap 2 — permission gap)
- nxp-extra-modules has no dist-git policy exception (gap 4 — every commit needs a VROOM ticket)

#### Recommendation

- **Immediate (before Monday go/no-go):** Ensure Sameera or Francisco can handle companion package tagging for RC3 builds. Pre-agree who will do it.
- **Short-term:** Document the pre-`-gate` tagging owner and permissions in the wiki. Add a pre-RC checklist step: "Confirm all companion NVRs are tagged into `-gate`."
- **Medium-term:** Implement STAG (Petr's proposal) to solve lockstep builds. Get dist-git policy exception for nxp-extra-modules.
- **Long-term:** Automate companion rebuilds — when kernel-ivos-qualcomm lands in a tag, trigger downstream-dtbs/qcom-scmi/nxp-extra-modules rebuilds and tagging automatically.

> **Sources audited:**
> - `ATC_Team_codebase_docs/repo-wiki/repos/gator.md` — Gator automated promotion
> - `ATC_Team_codebase_docs/repo-wiki/repos/gator-config.md` — tag/promotion config
> - `ATC_Team_codebase_docs/repo-wiki/repos/release-definitions.md` — release stream identity
> - `ATC_Team_codebase_docs/repo-wiki/repos/downstream-pipelines-as-code.md` — pipeline stages
> - `ATC_Team_codebase_docs/repo-wiki/repos/rhivos.md` — Pungi config/compose
> - `ATC_Team_codebase_docs/.agents/skills/atc-sre-debug/references/failure-taxonomy.md` — stage failures
> - `errata-distribution/README.md` — batch workflow
> - `errata-distribution/.cursor/skills/errata-distribution/reference.md` — Brew source/target tags
> - `rhivos-workflows-wiki/wiki/processes/release-planning.md` — end-to-end pipeline
> - `rhivos-workflows-wiki/raw/agentic-buddy/rhivos-release-approach.md` — Brew tag structure + STAG proposal
> - Slack thread #automotive-toolchain (Jun 11-12) — Eric Chanudet's escalation
> - Confluence: [RHEL & RHIVOS gating process](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/387157013) + comment 387292638 — manual freeze process
> - Confluence: [Release Checklist Template](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196276995) — Brew tag creation tasks
> - Confluence: [Release Documentation](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196269228) — ROTA, actors, stakeholders
> - Confluence: [ATC Distribution FA wiki](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/402130012) (10+ pages) — advisory/signing/CDN pipeline
> - developer-guide repo: `con_understanding-gating.adoc` — RHEL: build system auto-tags into `-gate`
> - developer-guide repo: `proc_working-with-side-tags.adoc` — RHEL side-tag workflow (centpkg + Distrobaker)
> - developer-guide repo: `assembly_maintenance-and-post-release-processes.adoc` — RHIVOS section is a stub
> - RCMDOC: [Unified Brew Tagging Structure](https://redhat.atlassian.net/wiki/spaces/RCMDOC/pages/296845952) — standard tag permission model (no `-gate`)
> - RCMDOC: [Add a package to a Brew tag](https://redhat.atlassian.net/wiki/spaces/RCMDOC/pages/296845847) — whitelisting process
> - EXDSPRHELB: [Permissions in Brew](https://redhat.atlassian.net/wiki/spaces/EXDSPRHELB/pages/175083555) — authoritative Brew permission reference
> - EXDSPRHELB: [Bypassing OSCI gating](https://redhat.atlassian.net/wiki/spaces/EXDSPRHELB/pages/175079794) — RHEL `-gate-bypass` workflow
> - RCMDOC: [RCM Services Overview](https://redhat.atlassian.net/wiki/spaces/RCMDOC/pages/296845840) — service catalog (Brew, rhpkg, ET, etc.)
> - [brew-confs hub_policy.conf](https://gitlab.cee.redhat.com/brew/brew-confs/blob/master/src/conf/hub_policy.conf) — **authoritative source** for all Brew tagging permissions, including RHIVOS-specific rules
> - Confluence: [Package workflow for AutoSD/RHIVOS-only packages](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196270957) — step-by-step RHIVOS package onboarding, `rhpkg build --target rhivos-1.0.0-gate`
> - Confluence: [Release Process for FDA packages](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196282794) — explicit "no manual tagging" policy, branch/target table
> - Confluence: [Product Development and Release](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196280075) — full tree (80+ pages across 9 teams) scanned for tagging content

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

FDA team scope reduced (2026-06-11, Martin Perina): review now covers "reviewed + improvements reported" only — removed "approved by QE." Follow-up tickets needed for final QE verification/approval. Dustin moved VROOM-41019 to Verified.

Original plan — FDA team (Meital Arki) first review of 6 docs by end of week 2026-06-13:
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
| Enric Balletbo i Serra | kernel-ivos-nxp-extra-modules build + errata (critical path) |
| Mattijs Korpershoek | kernel-ivos-nxp-extra-modules package expert (confirmed independent build) |
| Rachel Sibley | QE coordination, CTC scheduling |
| Jaime Flynn | Release management, blocker tracking |
| Stephen Bertram | Build waiving (Greenwave/WaiverDB) |
| Luigi Pellecchia | Crosscompiler testing |
| Petr Sabata | Release/distribution structure, crosscompiler/sysroot decisions |
| Eric Chanudet | downstream-dtbs, qcom-scmi, nxp-extra-modules — companion package rebuilds |
| Sameera Kalgudi | Manual Brew tagging (Eric's daily requests) |
| Oleksii Baranov | Kernel-ivos-qualcomm builds — controls kernel tagging |
| Whitney Chadwick | Release readiness meeting lead |
| Dustin Black | CI reboot bug reporter (VROOM-42325) |
| Meital Arki | Docs review coordination (FDA) |
| Pavol Brilla | FDA/FuSa test readiness |
