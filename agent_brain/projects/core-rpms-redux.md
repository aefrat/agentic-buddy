---
last_accessed: 2026-06-23
access_count: 1
created: 2026-06-23
---

# Core RPMs Redux

**Jira:** [VROOM-31017](https://redhat.atlassian.net/browse/VROOM-31017) — Epic, In Progress
**Assignee:** Petr Sabata | **Reporter:** Petr Sabata
**Component:** distribution | **Labels:** MUSTHAVE
**Due:** Jun 3, 2026 (passed) | **Story Points (children):** 5912
**ToolChain Open Sync:** [Google Doc](https://docs.google.com/document/d/1TegJmbETVM627zvw5hj8F5NtiQvvJ40OSbgkGlz-pWw/edit?tab=t.0) (weekly Tuesday 1:00–1:30pm UTC)
**Workstreams doc:** [Google Doc](https://docs.google.com/document/d/1uakPWEkSvMksJ9XAfPHlU_h9mMVpcIr9F2uufJw4-Ek)

## Goal

Replace the ambiguously defined "core RPMs" list with several new machine-readable package lists for different purposes. Four lists:

1. **Safety List** — every package touched by file reads or execution. Monitored for CIA & Defect Triage. Included in nightly tests + validator monitoring. (Previously "core-rpm list")
2. **Runtime List** — Safety List packages still open/mapped after boot. Review/approval from Matthew/Petr (or delegates). Used during FuSa Triage.
3. **Image List** — every package in the ASIL portion of the image. Included in nightly tests + validator monitoring.
4. **Tools List** — manually curated safety-critical tool packages. Monitored for CIA & Defect Triage.

Format: JSON (`jq` is part of the product). Fields: binary package name + source RPM NVR.

## Current status (Jun 23, 2026)

### Pipeline integration — DONE
From ToolChain Open Sync (Jun 23):
- **Core RPMs redux feature already integrated into the pipelines** (Juanje)
- New generated lists: https://rhivos.auto-toolchain.redhat.com/ci-gitlab-workspaces-downstream/16092802.5248061d/data-lists/
- **Next steps:**
  - Adjust tests, add the final list (now 4 lists instead of one)
  - Lists need to be versioned by releases
- **Open question:** Do we expect so many differences when compared to "New Core-rpm list for defect cloning script (RHIVOS 2.0)"?

### Remaining work
- **VROOM-40719** — Integrate comparison test into pipeline and gate compose on failure (New, Juanje). Comparison gates on package names only (not versions). Uses canonical list repo maintained by FuSa team. Gating failure blocks compose promotion.
- **VROOM-40584** — Update FoA Lib abstractions with real data (New, unassigned)
- **VROOM-37096** — Update glibc-revdep validators (New, Asaf Rachmani)
- **VROOM-37575** — Re-enable validators accidentally removed (New, unassigned)
- **VROOM-30619** — Refine systemctl validator scope (New, unassigned)

## Juanje's execopen work chain (Toolchain team)

Juanje implemented the pipeline integration — the execopen eBPF tracer that generates the lists.

### Completed tickets

| Ticket | Summary | Closed |
|--------|---------|--------|
| VROOM-41395 | Move execopen repo to Automotive namespace (`gitlab.com/redhat/edge/ci-cd/pipe-x/execopen`) | May 20 |
| VROOM-40718 | Tracing image can run tests in pipeline (blocker: slow boot, SSHD conflict) | May 13 |
| VROOM-40716 | Create tracing image variant (static libbpf, no fusa policy changes needed) | May 30 |
| VROOM-40715 | Build execopen RPM in pipeline matching compose kernel NVR | Jun 22 |
| VROOM-40717 | Run execopen tracer in pipeline, produce JSON lists | Jun 22 |
| VROOM-37485 | pac-jobs compare-core-rpms-lists command (Ozan) — replaced by execopen | Closed |

### Output structure
Pipeline produces per-architecture JSON files:
- `min-rpms/boot-list-<arch>.json` (upstream) / `fusa-rpms/safety-list-<arch>.json` (downstream)
- `min-rpms/runtime-list-<arch>.json` / `fusa-rpms/runtime-list-<arch>.json`
- `min-rpms/image-list-<arch>.json` / `fusa-rpms/image-list-<arch>.json`
- `fusa-rpms/tools-list-<arch>.json` (downstream only, curated)

### Key technical details
- kernel-automotive hardcoded in Safety List (tracer can't detect it)
- Test infra packages filtered out
- Execopen compiled statically (no runtime libbpf dependency)
- Works for aarch64 and x86_64
- RPM built using mock in TF VM alongside image build

## Juanje's Slack trail

### DMs with Avi
- **May 14:** "Got execopen working for both arches and generating the core-rpms list in TF using the fusa-minimal image"
- **Mar 10:** "I've already spent time on execopen. Many improvements, unit/smoke-tests, built AutoSD image with pac-jobs. But image didn't start in TF — not easy. Ian hasn't responded to MR or emails."
- **Mar 5:** "I already did analysis and created MR to improve it. To me it wasn't ready for adding to our projects." Shared original repo: `gitlab.com/imcleod1/execopen` and MR #22.

### Public channels
- **Jul 2025 (#team-toolchain-automotive):** "Core-rpms going to be replaced by other lists... I wouldn't rely on that list, because it's going to be removed" (re: VROOM-31017)
- **Apr 2026 (#team-auto-follow-on-activities):** Michael Ho: "core-rpms is getting deprecated as result of VROOM-31017"
- **Jun 2026:** Active pipeline diagnoses in #alerts-auto-toolchain — downstream failures, NVR consistency checks, smoke-test timeouts

## Related epics and tickets

### Upstream
| Ticket | Summary | Status | Assignee |
|--------|---------|--------|----------|
| VROOM-37039 | RHIVOS 2.0 Canonical RPM Lists Bootstrapping | In Progress | Amanda Carter |
| VROOM-29696 | Systematically link VROOM CVEs to RHEL CVEs | In Progress | Petr Sabata |

### Historical (closed)
| Ticket | Summary |
|--------|---------|
| VROOM-30862 | core-rpm changes — reduced scope (removed 14 packages) |
| VROOM-35857 | core-rpm new scope: kernel-ivos-qualcomm |
| VROOM-33683 | RHIVOS core-rpm gating tests failures |
| VROOM-36905 | packages-not-in-core-rpm-list validator RHIVOS-2 enablement |
| VROOM-33226 | Remap validators to core-rpms subset |

### Open/New
| Ticket | Summary | Assignee |
|--------|---------|----------|
| VROOM-38899 | RHIVOS 10.2 core-rpm gating tests failures | Rachel Sibley |

## Original toolchain work (VROOM-31421)

Separate but related: the toolchain packages needed to *build* core RPMs.

**[VROOM-31421: Build toolchain base for RHIVOS](https://redhat.atlassian.net/browse/VROOM-31421)** — umbrella, In Progress, Juanje Ojeda.

Strategy (Jul 2024): tag from CentOS Stream / rebuild without changes / rebuild with RHIVOS-specific changes.

| Ticket | Summary | Status |
|--------|---------|--------|
| VROOM-31422 | Identify packages to rebuild from CS | Done |
| VROOM-31427 | Create/define RHIVOS Brew tags for toolchain | Done |
| VROOM-31428 | Rebuild/tag packages in Brew tags | Done |
| VROOM-37556 | Add RHIVOS targets for toolchain packages in Brew | In Progress |
| VROOM-37557 | Document toolchain packages and status | To Do |
| VROOM-41422 | Add RHIVOS targets for non-toolchain packages in Brew | In Progress (unassigned) |
| VROOM-41599 | Create presentation for toolchain packages | Done |
| VROOM-42073 | RHIVOS toolchain documentation on rhivos.io | In Progress (jfrancoa) |

## Key people

- **Petr Sabata** — Epic owner, distribution lead
- **Juanje Ojeda** — Toolchain team, execopen pipeline implementation
- **Amanda Carter** — PM, canonical RPM lists bootstrapping
- **Rachel Sibley** — QE, core-rpm gating tests, validator scope
- **Matthew Storr** — FuSa lead, approver
- **Michael Ho** — FoA Lib abstractions
- **Filippo Storniolo** — Possible execopen tool owner (per Petr, May 2026)
- **Ozan Unsal** — pac-jobs, release pipelines

## Key artifacts
- **Execopen repo:** `gitlab.com/redhat/edge/ci-cd/pipe-x/execopen`
- **Original execopen:** `gitlab.com/imcleod1/execopen` (Ian McLeod)
- **RHIVOS Toolchain Packages spreadsheet** (Google Sheets, from VROOM-31421)
- **Confluence checklist:** `redhat.atlassian.net/wiki/display/Automotive/core-rpm+checklist`
- **FoA Lib MR !333** (core_rpms_redux branch)

## Slack channels
- **#team-toolchain-automotive** — primary toolchain work
- **#alerts-auto-toolchain** — pipeline diagnoses, nightly failures
- **#team-auto-follow-on-activities** — FoA/validator discussions
- **#forum-qe-automotive** — cross-team testing
- **#wg-team-auto-toolchain-gating** — gating pipeline
- **#automotive-workflows** — ownership/coordination discussions
