# RHIVOS vs. RHEL on NVIDIA (Voyager) — Engineering Comparison

**Date:** 2026-05-27  
**Sources:**
- RHEL on NVIDIA: https://gitlab.cee.redhat.com/tmlcoch/rhel-for-nvidia-knowledge
- RHIVOS: `/home/aefrat/ATC_Team_codebase_docs` (rhivos, gator, gator-run-configs, downstream-pipelines-as-code, release-definitions, rhivos)

---

## 1. Build System

| Aspect | RHIVOS | RHEL on NVIDIA (Voyager) |
|--------|--------|--------------------------|
| **Core build system** | Brew/Koji (same) | Brew/Koji (same) |
| **Tag isolation** | Per-version tags: `rhivos-{ver}-gate`, `-candidate`, `-pending`; Z-stream adds `-z-` prefix | Per-release isolated tag sets: `nv-{version}-rhel-10-{stage}` — full set per quarterly release |
| **Tag stages** | gate → candidate → pending (two separate gator runs) | build → draft → candidate → pending → release (+ et-compose, dev-compose) |
| **Buildroot strategy** | Not explicitly documented; inherits from CentOS Stream 10 base | Frozen per release: buildroot inherits from previous Voyager release (priority 15) + RHEL minor buildroot (priority 20). Never updated to a newer RHEL minor mid-lifecycle |
| **Upstream community sync** | CBS (CentOS Build System) — gator syncs packages like `hirte`, `kernel-automotive`, `bluechi` via SSL auth | None — no CBS involvement; Voyager is RHEL-only downstream |
| **Dist tag** | Standard RHEL dist tags (`.el9`, `.el10`) | Single custom dist tag `.el10nv` across all builds — distinguishes from standard RHEL RPMs |
| **Architectures** | aarch64 + x86_64 (both customer-facing) | aarch64 (customer-facing) + x86_64 (retained for developer debugging only) |
| **Kernel signing** | Not documented separately | Two-phase: standard build → pesign target pass for kernel signing |
| **Gating automation** | **Gator** — custom CLI (Python) integrating Brew, Greenwave, Test Console, ResultsDB, OSCI, Errata | **OSCI Errata Automation / RHELCMP** — standard RHEL infra; builds gate on Greenwave policies, ET sync populates `-pending` tags |
| **Z-stream tags** | Explicit: `rhivos-{ver}-z-gate → z-candidate → z-pending` | No `-z` tags; single tag set per version; quarterly pace makes parallel Y/Z unnecessary |

**Key difference:** Voyager has a rigidly defined, isolated per-quarterly-release tag set with a frozen buildroot philosophy. RHIVOS uses a more dynamic, rolling tag approach with Gator as the orchestration layer and an explicit two-stage gate/promote split.

---

## 2. Composes

| Aspect | RHIVOS | RHEL on NVIDIA (Voyager) |
|--------|--------|--------------------------|
| **Compose tool** | Pungi/ODCS (`rhivos-odcs.conf`) | Pungi/ODCS (ENGCMP team runs nightly) |
| **Compose types** | Single repo-only compose (all ISO/image phases skipped via `skip_phases`); images built separately in downstream pipeline | Two types: **Complete** (overrides RHEL packages, generates DVD ISOs + QCOW2) and **Minimal** (NVIDIA repo only, generates product listings for ET) |
| **Package source** | `rhivos-2.1-candidate` Koji tag | `nv-{ver}-rhel-10-et-compose` tag (inherits `-pending` + full RHEL release) |
| **Variant definition** | `variants.xml` fetched from `downstream-sync-compose-metadata` repo | Inline in Pungi config; Complete compose inherits RHEL packages via tag priority |
| **Comps file** | CentOS Stream 10 comps with variant names rewritten to `RHIVOS` via `sed` | Standard RHEL comps |
| **Image generation** | Done separately in the CI pipeline (osbuild, per-board images) | Complete compose generates DVD ISO + QCOW2 directly via Pungi |
| **Promotion pipeline** | CI pipeline promotes compose via `promote-compose` job (SSH/Kerberos to RCM host) | Automated: compose → tests → `nightly-requested` tag in CTS → Compose Promotion Jenkins job → copies to `/mnt/redhat`, imports product listings, registers in CTS |
| **Nightly cadence** | Nightly pipeline builds triggered by schedule | One nightly compose per day |
| **Gate dependency** | Compose is input to CI pipeline that gates packages separately | Composes start only after target RHEL minor reaches GA |
| **Config repo** | Dedicated `rhivos` config repo (pungi-config/rhivos-odcs.conf) | Managed by ENGCMP team |

**Key difference:** RHIVOS separates compose generation (repo-only, ODCS) from image builds (per-board, osbuild in CI). Voyager uses Pungi to produce both repos and images in a single compose, distinguishing Complete (for images) from Minimal (for ET product listings).

---

## 3. Delivery

| Aspect | RHIVOS | RHEL on NVIDIA (Voyager) |
|--------|--------|--------------------------|
| **Delivery mechanism** | Red Hat CDN (subscription-manager) + internal `rhivos.auto-toolchain.redhat.com` + AWS S3 | Red Hat CDN (subscription-manager) only for customers; internal at `download.engineering.redhat.com` |
| **CDN path pattern** | `/content/dist/rhivos2/{version}/` (versioned DOT paths) | `/content/dist/layered/rhel10/aarch64/nvidia/` (version-less layered path) |
| **Repository labels** | `rhivos-2-aarch64-rpms`, `rhivos-2-x86_64-debug-rpms`, etc. | `rhel-10-for-aarch64-nvidia-rpms`, `rhel-10-for-aarch64-nvidia-debug-rpms`, etc. |
| **Eng ID (ProductID)** | 931 (RHIVOS), 1030 (RHIVOS Core) — shared across all minor releases | Shared with RHEL BaseOS Eng IDs — no separate entitlement required |
| **Shadow names** | Uses `_DOT_` encoding in shadow names (e.g., `rhivos-2_DOT_1-aarch64-rpms`) to satisfy downstream tooling | Not applicable |
| **Entitlement** | Requires RHIVOS subscription | Any valid aarch64 RHEL subscription — no separate SKU |
| **Default state** | Not documented as opt-in by default | Disabled by default; customers opt in via `subscription-manager repos --enable` |
| **Package priority** | Not documented | No elevated priority; NVR tilde suffixes (e.g., `kernel-5.6.1~nvidia`) + `.el10nv` dist-tag ensure DNF selects Voyager packages |
| **ISO/image delivery** | Released via AWS S3 / `rhivos.auto-toolchain.redhat.com` | Pushed separately via `pub push-staged` (ET does not handle ISOs/QCOW2s); naming from `compose.label` |
| **Release definitions** | YAML files in `release-definitions` repo with ProductID cert generation | Managed by ET + CDN config tooling |
| **Variants** | RHIVOS + RHIVOS Core (minimal footprint subset) | Single variant `10Base-RHEL-Nvidia` |

**Key difference:** RHIVOS uses versioned, per-minor CDN paths and requires its own subscription/Eng ID. Voyager uses version-less layered CDN paths and reuses RHEL BaseOS entitlements — simpler customer onboarding but less granular.

---

## 4. Development Workflow

| Aspect | RHIVOS | RHEL on NVIDIA (Voyager) |
|--------|--------|--------------------------|
| **Upstream source** | CentOS Stream / AutoSD (GitLab: `automotive/pipe-x/`) | CentOS Stream (`c10s-aie-nv` branch in CentOS dist-git) |
| **Workflow tool** | Custom downstream GitLab CI pipeline (`downstream-pipelines-as-code`) + Gator | RoG (RHEL on GitLab) automation |
| **Y-stream flow** | CentOS Stream/AutoSD → upstream MR → rhivos.git tag → downstream pipeline trigger → ODCS compose → image builds → hardware testing → Gator gating | CentOS Stream MR (`c10s-aie-nv`) → RoG sync to `rhel-10-nv` → Brew build → errata advisory |
| **Z-stream flow** | Same pipeline; uses Z-stream Brew tags (`z-gate`, `z-candidate`, `z-pending`) | Developer branches Z-stream from historical Y-stream commit → `nv-{ver}-rhel-10` branch → RoG detects UMB → MR against Z-stream → draft Brew build → promote → errata |
| **MR validation** | GitLab MR triggers pipeline with staging infra, staging S3 buckets, `DISABLE_PROMOTE` flags | RoG runs CI tests within the MR, validates commit policy (JIRA fixVersion) on merge |
| **Build trigger** | Tag creation on rhivos.git (`UPSTREAM_COMMIT_TAG`) triggers release pipeline | Commit merge into dist-git branch triggers RoG build |
| **Hardware testing** | Test Console (hardware: Qualcomm SA8775P/SA8650P, Renesas R-Car S4, TI AM69SK/J784S4, Raspberry Pi 4, AWS, QEMU) | Not explicitly documented in workflow; separate QE validation step before release |
| **Package gating** | Gator (`gator evaluate`): Greenwave policy check against ResultsDB test results → tag to candidate | OSCI automation + Greenwave; RHELCMP syncs builds to `-pending`; builds move to release tag on advisory shipment |
| **Direct RPM build** | Not documented (pipeline handles it) | `rhpkg build` (discouraged; use `--target TARGET` explicitly) |
| **FuSa compliance** | Explicit: FuSa jobs, Polarion integration for requirements traceability | Not applicable |

**Key difference:** RHIVOS workflow is fully pipeline-driven and GitLab-centric, with hardware test gating before any promotion. Voyager follows the standard RHEL dist-git/RoG model, closer to classic RHEL engineering practices.

---

## 5. Dist-git

| Aspect | RHIVOS | RHEL on NVIDIA (Voyager) |
|--------|--------|--------------------------|
| **System** | GitLab (not Red Hat dist-git/Gitolite) — `gitlab.cee.redhat.com/automotive/rhivos` | Red Hat dist-git + internal GitLab via RoG |
| **Branch model** | Per-release branches: `rhivos-0.x`, `rhivos-1.x`, `rhivos-2.x` (one branch per release) | Permanent Y-stream (`rhel-10-nv`) + on-demand Z-stream branches (`nv-{ver}-rhel-10`) |
| **Commit policy** | No documented JIRA-based commit policy; upstream-first development | JIRA required: VOYAGER project, Epic type, fixVersion matching target version |
| **Z-stream branching** | Z-stream handled via Brew tag pipeline (not separate dist-git branches per package) | Developer creates Z-stream branch from historical Y-stream commit; RoG mirrors via UMB |
| **Upstream sync** | CentOS Stream/AutoSD syncs naturally via upstream-first development | RoG handles `c10s-aie-nv` → `rhel-10-nv` sync automatically |
| **Access control** | GitLab group/project permissions | Gitolite: `@devel` group has read/write/create on `rhel-10-nv` |
| **Branch naming** | `rhivos-{major}.{minor}` (e.g., `rhivos-2.1`) | Y-stream: `rhel-10-nv`; Z-stream: `nv-{YY.MM}-rhel-10` (mirrors Brew tag naming) |
| **Version targeting** | Branch is per release version — clear 1:1 mapping | Y-stream `rhel-10-nv` maps to the *current* dev version (changes on release day); developers must mentally track which version it currently targets |
| **Multi-package scope** | Compose config repo is separate from individual package repos | Each package has its own dist-git repo/branch; compose and delivery are separate concerns |

**Key difference:** RHIVOS uses GitLab-native branching with a clean per-version branch-per-release model. Voyager uses the RHEL dist-git system with RoG automation and a more complex Y/Z-stream branch management (permanent Y-stream + on-demand Z-streams), with JIRA-enforced commit policies.

---

## 6. Errata Tool

| Aspect | RHIVOS | RHEL on NVIDIA (Voyager) |
|--------|--------|--------------------------|
| **ET Product** | "RHIVOS" (product name in gator-run-configs) | "Red Hat Enterprise Linux for NVIDIA" (dedicated ET product) |
| **Product Version** | Not explicitly documented; managed via gator errata config | Single PV: `RHEL-10-Nvidia` (shared across all Voyager releases) |
| **Variant** | Not explicitly documented | Single: `10Base-RHEL-Nvidia` — CPE: `cpe:/a:redhat:enterprise_linux_nvidia:10::el10` |
| **Release structure** | Per-release errata config YAML in gator-run-configs (e.g., `errata-2.0-config.yaml`): `product`, `release`, `jira_release`, `batch_name`, `cc_list` | One Release object per quarterly cycle (e.g., "RHEL for NVIDIA 26.03"); enabled ~1 month before GA; prior release disabled at GA |
| **Advisory creation** | Gator command: `generate-advisories` — finds passing packages, checks for existing advisories, creates new or attaches builds to `NEW_FILES` state | Manual Create (not Assisted Create; JIRA support not in Assisted Create); OSCI Errata Automation handles creation and build attachment |
| **Automation level** | Gator automates advisory creation and build attachment post-gate | OSCI automation handles creation; signing happens immediately on attachment (PQC signing) |
| **Build attachment** | Gator attaches build to advisory when package passes Greenwave | ET sync (RHELCMP) populates `-pending` tags; Errata Posterity moves builds to release tag on advisory ship |
| **Batches** | Config has `batch_name` field (batch grouping supported) | Not used; RHEL phasing batches out |
| **Workflow trigger** | Package passes gating pipeline (Greenwave) → gator files advisory automatically | Advisory created at start of cycle; builds attached throughout |
| **Adding a new release** | Create new gator-run-configs YAML file (copy + update Brew tags, errata.release, jira_release) | Create new ET Release object only (no new PV, Variant, or CDN repo required) |

**Key difference:** Voyager has a well-defined, documented ET product hierarchy (separate Product, single PV, single Variant, per-quarter Release). RHIVOS's ET integration is abstracted through Gator with less explicit ET structural documentation — errata parameters are embedded in gator-run-configs YAML files.

---

## 7. Release Policy

| Aspect | RHIVOS | RHEL on NVIDIA (Voyager) |
|--------|--------|--------------------------|
| **Cadence** | Not explicitly time-boxed; driven by AutoSD/automotive upstream milestones | Quarterly: last day of March, June, September, December |
| **Release phases** | ER (Early Release) → TP (Tech Preview) → DevPreview → RC (Release Candidate) → GA | Development (weeks 1–9) → Stabilization (from 15th of month 2) → Release (from 15th of month 3) |
| **Version series** | 0.x (beta/ER era), 1.x (RHEL 9 base), 2.x (RHEL 10 base) | Named by calendar quarter: `YY.MM` (e.g., 26.01, 26.02, 26.03) |
| **Support model** | Both Y-stream (rolling) and Z-stream (point) actively maintained | Only latest release supported; N is immediately EOL when N+1 ships |
| **Out-of-cycle releases** | Implicit (Z-stream configs exist for urgent fixes) | Explicitly minimized to avoid upgrade fatigue; triggered only by major NVIDIA milestones or hardware SKU GA |
| **Z-stream triggers** | Not explicitly documented; Z-stream Brew tags exist | Critical CVEs (KEV + Major), significant customer bugs, urgent compat breaks from blocking RHEL updates |
| **Upstream policy** | Upstream-first (changes go to CentOS Stream/AutoSD first) | Can ship patches still in upstreaming (breaks from classic RHEL policy) |
| **RHEL base** | RHIVOS-1 = RHEL 9 (CentOS Stream 9), RHIVOS-2 = RHEL 10 (CentOS Stream 10) | RHEL 10 only (currently RHEL 10.2, targeting RHEL 10.x minors) |
| **Core variant** | Yes — RHIVOS Core (minimal footprint, different eng-id: 1030) | No — single variant |
| **FuSa requirements** | Yes — functional safety compliance is a first-class requirement | No |
| **Automotive standards** | ISO 26262 / ASIL requirements influence delivery | Not applicable |
| **Release config management** | `release-configs/` YAML files in downstream-pipelines-as-code; one per milestone | ET Release objects; Brew tag sets; Product Pages for schedule publishing |

**Key difference:** Voyager has a rigid, predictable quarterly calendar with an aggressive "latest-only supported" model. RHIVOS has a milestone-driven release model (ER → TP → RC → GA) aligned to automotive upstream readiness, maintains multiple supported versions, and carries functional safety compliance as a hard requirement.

---

## Summary Table

| Dimension | RHIVOS | RHEL on NVIDIA (Voyager) |
|-----------|--------|--------------------------|
| **Build system** | Brew + Gator (custom CLI) + CBS sync | Brew + OSCI automation + RHELCMP |
| **Compose** | ODCS repo-only + separate osbuild images | Pungi Complete (images) + Minimal (product listings) |
| **Dist-git** | GitLab-native, per-release branch, no JIRA commit policy | Red Hat dist-git + RoG, Y/Z-stream model, JIRA-enforced commit policy |
| **Errata Tool** | Abstracted via Gator, errata config in YAML | Structured ET product hierarchy, OSCI automation |
| **Delivery** | Versioned CDN paths + own subscription + S3/internal | Layered (version-less) CDN + RHEL entitlement reuse |
| **Dev workflow** | GitLab pipeline-driven, hardware-gated, FuSa-compliant | RoG-driven, dist-git-centric, standard RHEL model |
| **Release policy** | Milestone-driven, multiple active versions, FuSa | Quarterly calendar, single-version support, aggressive EOL |
| **Upstream** | CentOS Stream / AutoSD (open upstream) | CentOS Stream / RHEL (internal gate) |
| **Customer target** | Automotive OEMs (vehicles, safety-critical) | NVIDIA GPU platform customers (aarch64 HW) |
