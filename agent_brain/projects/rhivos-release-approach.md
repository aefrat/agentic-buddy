---
last_accessed: 2026-05-28
access_count: 2
created: 2026-05-21
---

# RHIVOS — Release Build & Distribution Approach

## Status

Active investigation — evaluating whether the RHEL-for-NVIDIA knowledge base approach is a good fit for RHIVOS.

## Jira

- [AUTOBU-1076](https://redhat.atlassian.net/browse/AUTOBU-1076)

## What's being evaluated

Comparing the RHEL-for-NVIDIA approach (documented at `https://gitlab.cee.redhat.com/tmlcoch/rhel-for-nvidia-knowledge`) against the current RHIVOS approach for building and distributing product releases.

Current approach docs: `/home/aefrat/ATC_Team_codebase_docs`

## Key question

Is the RHEL-for-NVIDIA approach a good fit as a new direction for RHIVOS release building and distribution?

## Meeting context

**RHIVOS Release Readiness Meeting — 2026-05-20**

- Whitney (program manager) flagged that the RHEL-on-NVIDIA path might not be the correct path forward for RHIVOS
- Details not yet fully understood — Avi wants to dig deeper before drawing conclusions
- Key open question: what's the difference between what RHEL-on-NVIDIA provides vs. what RHIVOS needs as a layered product?

**Source docs:**
- Gemini notes: https://docs.google.com/document/d/12bqsWo8NvrCtZD8j9BZNTxNAJSJ9Nhnou9XqcbvMWM8/edit?tab=t.kxnqmkjla0k7
- Meeting doc: https://docs.google.com/document/d/1MjoxfCEsDWiLFy99wHsS4EWOnVzvlg91NqJcMIHBDbI/edit?tab=t.0

## Key findings from May 20 meeting

### What the team aligned on (decisions made)
- **Versioning:** Tied to RHIVOS releases — NOT separate like RHEL-for-NVIDIA does (timestamp-based)
- **Cadence:** Same cadence as RHIVOS core releases
- **Build strategy (Juanje's proposal, appeared accepted):** Build both RHIVOS and the QC layered product internally using the same pipeline infrastructure, just adding another compose [inferred — verify]. Separate them only at the CDN distribution level. Proprietary Qualcomm bits never leave the Red Hat internal network until CDN push.
- **QC content:** User space (audio, camera, graphics, display) for sure. QC kernel: TBD — pending legal approval (Jeffrey Calfman).
- **Timeline:** QC user space packaging complete end of August. QC layered product available end of September. Not linked to RHIVOS 2.0 GA.

### Why RHEL-for-NVIDIA may not be the right fit — from the meeting
Two distinct concerns surfaced:

1. **Versioning mismatch (explicit rejection):** RHEL-for-NVIDIA uses timestamp-based independent versioning. The RHIVOS team explicitly does not want this — they want the layered product tied to RHIVOS version cycles.

2. **Architectural mismatch (Juanje, 00:05:50–00:07:28):** RHEL-for-NVIDIA assumes RHEL's build toolchain — they build images during the compose process, integrated into it. RHIVOS uses the automotive image builder differently: compose first, then build images from the compose. Juanje's assessment: "I don't think it's going to fit that well that layer system because we actually don't do a lot of the stuff they do and we don't use a lot of tools they or services they do."

3. **Counter-point (Ozan, 00:10:19):** Because RHIVOS uses automotive image builder (compose → then image build), it's actually *easier* for RHIVOS to separate a layered product than it was for the RAIL team. So the layered product route is feasible — just not necessarily by copying the RHEL-for-NVIDIA approach directly.

### Whitney's framing
Whitney's concern wasn't that layered product is wrong — it's that the full layered product route (new product pages, SKUs, schedules) has high overhead. She was drawn to the extensions-repo approach that RAIL used for NVIDIA as potentially simpler. But the team still needs to understand what that means technically before deciding.

### Deep-dive: RHEL-for-NVIDIA actual architecture (from knowledge base)

Source: `/home/aefrat/rhel-for-nvidia-knowledge/docs/`

### Ozan's claim — VERIFIED TRUE
> "RHEL-for-NVIDIA builds images during compose time"

Confirmed. Voyager (RHEL-for-NVIDIA) produces ISO and QCOW2 images **as part of the Complete compose** (via Pungi/ODCS). This is architectural, not incidental. RHIVOS uses automotive image builder and builds images *after* the compose. This is a real incompatibility.

### Voyager's actual architecture

**Two compose types (key design):**
- **Complete compose** — Full RHEL BaseOS + AppStream with Voyager packages (kernel, qemu-kvm, libvirt) overriding equivalents via tag inheritance. Generates DVD ISO and QCOW2 images. Large and resource-heavy, not aligned with CDN layout.
- **Minimal compose** — Only the Voyager-specific packages (the NVIDIA repo). Aligned with what customers see on CDN. Used for product listings in Errata Tool. Cannot generate full ISOs.
Both are required because they serve different purposes.

**Build system:** Brew (Koji fork), with versioned tag sets per Voyager release (`nv-26.03-rhel-10`). Package override happens via tag inheritance, not NVR comparison.

**Versioning:** Quarterly, independent of RHEL (26.01, 26.02, 26.03...). Tied to which RHEL minor version it's *based on*, but the version number is completely separate. This is the approach the RHIVOS team explicitly rejected.

**CDN/Distribution:** New repo under existing RHEL Eng Product, under the *layered* CDN path: `/content/dist/layered/rhel10/aarch64/nvidia/os`. Disabled by default. Customers enable manually via subscription-manager. RPMs via Errata Tool, ISOs/QCOW2 via Pub separately.

### What this means for the RHIVOS decision

**What does NOT apply:**
1. Image-during-compose approach — RHIVOS builds images after compose via automotive image builder; tooling is incompatible
2. Pungi/ODCS compose tooling — RHIVOS uses its own pipeline
3. Voyager's independent versioning — explicitly rejected by the team
4. Brew tag structure specifics — RHIVOS has its own tag structure

**What DOES apply (more than the meeting suggested):**
1. **The two-compose concept is directly relevant.** A "Minimal compose" (only the QC-specific packages) for CDN alignment + product listings, separate from the full build, maps well to Juanje's proposal of building the QC layered product internally and separating at the CDN level.
2. **The CDN layered path structure.** The `/content/dist/layered/...` CDN path is what makes it a "layered product" from a distribution standpoint — not the build tooling. Juanje's proposal ("separate at CDN level") is essentially this same principle.
3. **Disabled-by-default repo.** The approach of a new repo under the same Eng Product, disabled by default, is a clean model for how the QC user space bits would be distributed.
4. **No new Eng Product needed.** Voyager didn't need a new product — it added a repo under existing RHEL. This reduces overhead (no new product pages, SKUs, etc.) — directly relevant to Whitney's concern about overhead.

### Key insight
Juanje's proposal and the RHEL-for-NVIDIA approach converge at the *distribution layer*. The difference is only in *how you get there*: Voyager builds images during compose (not applicable to RHIVOS), but the CDN separation mechanism is the same idea. The meeting made it sound like Voyager is a poor fit entirely — the reality is more nuanced: the distribution model is directly applicable; the build/image tooling is not.

## AUTOBU-1076 vs. RHEL-for-NVIDIA: requirement-by-requirement comparison

Petr's ticket breaks the work into 8 areas. Mapped against the Voyager knowledge base and the May 20 meeting decisions.

### Build system — Strong match ✅
**Petr:** Separate tag & target structure in Brew, based on standard LP solutions.
**Voyager:** Versioned Brew tags per release (`nv-26.03-rhel-10`) with full hierarchy: candidate, pending, build, et-compose, override. This is the most directly reusable part of the Voyager design.

### Compose configuration — Strong match ✅
**Petr:** New composes for LP extension repos; input resolves against base RHIVOS composes.
**Voyager:** Two composes — Minimal (LP packages only, CDN-aligned, used for product listings) + Complete (full base + LP overrides, used for images). The Minimal compose is exactly what Petr describes. Directly reusable as a design reference.

### Distribution / Errata Tool — Strong match ✅
**Petr:** LPs defined in ET for regular and Z-stream releases, targeting CDN locations; separate advisory automation.
**Voyager:** Separate ET Product, separate advisories, Jenkins job to sync `-pending` Brew tags. CDN layered path (`/content/dist/layered/rhel10/aarch64/nvidia/`) is the infrastructure pattern to follow.

### End user tooling / AIB — Pipeline changes needed, QC LP repo access TBD ⚠️
**Petr:** AIB might need extending for multiple product subscriptions (possibly transparent via librhsm).
**Voyager:** Not applicable — Voyager uses RHEL's build toolchain (Brew/Pungi), not AIB. The subscription-manager / librhsm path is a Voyager-specific answer that does not map to RHIVOS.
**What the ATC pipeline actually does today:** ODCS produces a single RHIVOS compose from the `rhivos-2.1-candidate` Koji tag. AIB then builds images from that compose — the compose URL is passed as a repo source in the AIB manifest (`content.repos`). There is no `subscription-manager` or `librhsm` in this path; repo access is by URL, with Kerberos handling ODCS-level auth upstream.
**On multiple composes:** AIB's `content.repos` is a list — adding the QC LP compose URL alongside the base RHIVOS compose URL is architecturally supported and already matches the existing pattern for Qualcomm board support repos (`@ADD_QCOM_BOARD_SUPPORT_*@` in `custom-images` manifests). This would not require AIB code changes; it would require manifest changes and a pipeline change to ensure both compose URLs are available before the AIB build stage runs.
**What remains open:** Whether the QC LP compose URL will be entitlement-gated (accessible only with Qualcomm partner credentials) or openly accessible to pipeline runners. If gated, credential handling in the pipeline would be needed — not an AIB code problem, but a pipeline and CDN access question requiring confirmation with the RHELDST/distribution team.

### Pipelines and package gating — Significant new work required ⚠️
**Petr:** Pipelines use both RHIVOS and LP repos in tandem; gating configured for LP tag structure.
**Voyager:** Has its own gating, but uses different pipeline tooling (RoG, Brew-native). RHIVOS uses pipelines-as-code. The concept (test with combined repos) is the same; the implementation will be RHIVOS-specific.

**Note on Juanje's "no pipeline changes" framing:** Juanje's statement at the RHIVOS Release Readiness Meeting of May 20 — that only distribution changes are needed, not build or pipeline changes — is directionally correct at the architectural level (the core build infrastructure doesn't change) but undersells the pipeline work. The following specific changes are required, confirmed by ATC codebase analysis:

**Pipeline changes needed (from `downstream-pipelines-as-code`):**
- New release config file in `release-configs/` (new `BUILD_BRANCH` entry) with QC LP compose URLs, separate `GATOR_CONF` path, and component pins — same pattern as existing stream configs
- The `generate-compose` stage must either run a second ODCS request for the QC LP compose, or the QC LP compose URL must be injected into the pipeline so AIB can reference it in the build stage
- Potentially a new S3 path/bucket for QC LP artifacts (pending IAM policy decision — new bucket vs. scoped policy on existing `auto-product-build-downstream`)
- A compose promotion pipeline for the QC LP Minimal compose that imports product listings into Errata Tool — this does not currently exist and is separate from the `promote-compose` SSH/RCM job used for RHIVOS

**AIB manifest changes needed (from `custom-images`):**
- New `@ADD_QCOM_LP_REPO_*@` placeholder token in `qa.aib.yml.in` and `ps.aib.yml.in` templates — following the existing `@ADD_QCOM_BOARD_SUPPORT_*@` pattern
- New `.sed` substitution entries for each QC hardware target (`ride4_sa8775p_sx_r3.sed`, `ride4_sa8650p_sx_r3.sed`) to inject the QC LP compose URL at manifest render time
- Updates to `create-qa-manifest.sh` to apply QC LP sed for RHIVOS + QC distro/flag — caution: `--require` flag means missing sed files fail hard; `ps` and `fusa-minimal` use `default.sed` fallback, so a missed substitution there emits a broken manifest silently

**Gating changes needed (resultsdb / waiverdb / greenwave / Gator):**
- Separate `GATOR_CONF` file in `automotive/fences/gating/gator` for QC LP — configures Test Console test triggers for QC packages AND evaluation/contact-point triggers on gate failure (Petr's ticket explicitly lists both)
- resultsdb: associations for QC LP package builds (separate NVRs from QC Brew tags, distinct from RHIVOS base NVRs)
- waiverdb: waiver subjects scoped to QC LP tag content
- greenwave: new policies covering QC LP Brew tag — what constitutes a passing gate for QC LP packages vs. RHIVOS base packages

**Test Console changes needed:**
- `tc_wait_for_rhivos_test()` in `functions.yml` uses `tc-cli rhivos base-image is-complete` — `rhivos` is a hardcoded product identifier. QC platform images built from dual-compose (RHIVOS + QC LP) may need a new TC pipeline request type or product identifier. Needs explicit TC team confirmation — may not be a simple config change.

### CDN / EngIDs / SKUs — Significant mismatch ❌
**Petr:** Separate SKUs; content only accessible with LP SKUs; gated by three-way partner/customer agreements.
**Voyager:** Deliberately chose NO separate Eng ID, NO separate SKU (Decision #8) — available to all RHEL subscribers. Voyager content is optional but not access-controlled.

**This is the critical difference.** Petr's requirement is stricter because Qualcomm bits are proprietary and require partner agreements. Voyager didn't need access gating — NVIDIA hardware is open enough that any RHEL customer can get it. For RHIVOS, the access control model is fundamentally different. This is where a new Eng Product + separate SKU may be unavoidable, regardless of Whitney's overhead concerns. It's also the part that drives the most downstream complexity (portal, entitlements, customer-facing setup).

### Schedule / Jira releases — Mismatch resolved by meeting ✅ (via decision)
**Petr asks:** If LPs release on a different schedule, separate Jira releases might be needed.
**Voyager:** Independent quarterly schedule, fully separate from RHEL.
**May 20 meeting decision:** Tied to RHIVOS releases, same cadence.
Petr's open question is already answered: no separate Jira releases, no independent schedule.

---

### Summary for Jira comment

> Reviewed the RHEL-for-NVIDIA (Voyager) knowledge base at https://gitlab.cee.redhat.com/tmlcoch/rhel-for-nvidia-knowledge against this ticket's requirements.
>
> **What maps well from Voyager (~5 of 8 areas):**
> - **Build system:** Voyager's versioned Brew tag structure (`nv-{ver}-rhel-10` with candidate/pending/build/et-compose hierarchy) is a direct reference for our LP tag design.
> - **Compose configuration:** Voyager uses two composes — a Minimal compose (LP packages only, CDN-aligned, generates product listings for ET) and a Complete compose (base + LP overrides, generates images). The Minimal compose design directly addresses Petr's requirement for LP extension repo composes.
> - **Distribution / ET:** Voyager's ET setup (separate product, separate advisories, Jenkins sync job for `-pending` tags, CDN layered path `/content/dist/layered/...`) is the pattern to follow.
> - **Schedule:** The RHIVOS Release Readiness Meeting of May 20 aligned on tying QC LP versioning and cadence to RHIVOS releases (not independent). This answers Petr's open question on separate Jira releases — not needed.
>
> **Where Voyager is NOT the right model (1 critical area):**
> - **SKUs / access control:** Voyager deliberately chose no separate Eng ID and no separate SKU — all RHEL subscribers can access it. Our QC LP requires gated access due to Qualcomm partner/customer agreements. This means we likely need a new Eng Product + separate SKU, which drives the portal/entitlement overhead Whitney flagged in the RHIVOS Release Readiness Meeting of May 20. This is the hardest part and the one that most diverges from the Voyager path.
>
> **Requires investigation before closing (1 area):**
> - **End user tooling / AIB:** Voyager is not applicable here — it uses RHEL's build toolchain (Brew/Pungi), not AIB. The RHIVOS pipeline today runs ODCS to produce a single RHIVOS compose, then AIB builds images from it using explicit `content.repos` URLs — no `subscription-manager` or `librhsm` involved. AIB's `content.repos` is a list, so adding a QC LP compose URL alongside the base RHIVOS compose is architecturally supported without AIB code changes; it would need manifest updates and a pipeline change to make both compose URLs available to the build stage. What is NOT yet confirmed: whether the QC LP compose URL will be entitlement-gated. If it is, pipeline-level credential handling would be needed (not an AIB code change). This needs confirmation with the RHELDST/distribution team.
>
> **Architectural note:** The RHIVOS Release Readiness Meeting of May 20 discussion suggested Voyager was a poor fit due to build tooling differences (Voyager builds images during compose; RHIVOS builds images after compose via automotive image builder). This is true for the build layer. However, Voyager's *distribution* model (CDN layered path, disabled-by-default repo, minimal compose for CDN alignment) is directly applicable and essentially what Juanje's proposal ("build internally, separate at CDN") implements. The recommended path is: don't adopt Voyager's build/compose tooling, but use its distribution model as the reference.

## Brew tag structure and Stag proposal (2026-05-28)

### RHIVOS current Brew tag pipeline

From gator config (`gator/README.md`, `gator/docs/CODEBASE.md`):

```
[rhel-9.5.0-pending] ──┐
                        union → gator evaluate (Greenwave) → rhivos-X.Y.Z-candidate
[rhivos-X.Y.Z-gate] ───┘                                          ↓
                                                        ODCS compose
                                                                   ↓
                                                        gator promote
                                                                   ↓
                                                        rhivos-X.Y.Z-pending
```

**Build target for maintainers:** uses `rhivos-X.Y.Z-build` as the buildroot (stable, gated content). New builds land in `-gate`, not immediately visible to subsequent builds.

**The lockstep problem:** when a library has an ABI break, dependent packages can't be built against the new version until it completes full gating. No group-level buildroot isolation exists. The only current workaround is Brew admin override (doesn't scale).

### Why RHEL side tags don't apply

RHEL side tags require: centpkg, Distrobaker, RHEL on GitLab (ROG) CI with `side-tag:` MR directive, OSCI, and `build-group` Jenkins job. RHIVOS has none of these.

### Stag proposal (Petr Sabata, doc: 16evZIIeBjijlJZcCbDXtwlRchzkhYOdvkDn-V6Iz9IY)

A per-version `rhivos-X.Y.Z-stag` Brew tag + build target:
- **Tag** inherits from `rhivos-X.Y.Z-build` → gets full stable buildroot
- **Target** uses stag as both build tag and destination tag → builds land in stag and are immediately visible to subsequent builds in the group
- Maintainer builds entire interdependent group into stag, then mass-tags into `-gate` when ready
- **Gap:** gator has no group-gating concept — packages gate independently once in `-gate`. Acknowledged as future work.

**Connection to LP work (AUTOBU-1076):** stag is the mechanism needed to build QC kernel + QC kernel modules in lockstep, which is a stated requirement for the QC Layered Product.

## Open questions (still to investigate)
- How would RHIVOS implement the "Minimal compose" equivalent (QC-specific packages only) for CDN alignment and product listings?
- Extensions repo approach vs. full layered product — what's the difference in overhead?
- Can the SKU/access control be done with lower overhead than a full new Eng Product? (Check with RHELDST team.)

### Action items from the meeting
- [Avi] ~~Compile list of stakeholders for async layered product discussion~~ — DONE (added to meeting doc: https://docs.google.com/document/d/1MjoxfCEsDWiLFy99wHsS4EWOnVzvlg91NqJcMIHBDbI/edit?tab=t.0#bookmark=id.3hhtxwbj9tr8)
- [Whitney] Consult with release SP team on who should be involved for the extension repo discussion
- Async discussion to be scheduled with ATC focals (Build, Distribution, Gating)

## Notes

<!-- Add findings, comparisons, blockers, and decisions here as the investigation progresses -->

## Decision

<!-- Record the outcome and reasoning once a decision is made -->
