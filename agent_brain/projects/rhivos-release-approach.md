---
last_accessed: 2026-05-21
access_count: 1
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
- **Build strategy (Juanje's proposal, appeared accepted):** Build both RHIVOS and the QC layered product internally using the same pipeline infrastructure, just adding another compose. Separate them only at the CDN distribution level. Proprietary Qualcomm bits never leave the Red Hat internal network until CDN push.
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

## Open questions (still to investigate)
- How would RHIVOS implement the "Minimal compose" equivalent (QC-specific packages only) for CDN alignment and product listings?
- Extensions repo approach vs. full layered product — what's the difference in overhead?

### Action items from the meeting
- [Avi] ~~Compile list of stakeholders for async layered product discussion~~ — DONE (added to meeting doc: https://docs.google.com/document/d/1MjoxfCEsDWiLFy99wHsS4EWOnVzvlg91NqJcMIHBDbI/edit?tab=t.0#bookmark=id.3hhtxwbj9tr8)
- [Whitney] Consult with release SP team on who should be involved for the extension repo discussion
- Async discussion to be scheduled with ATC focals (Build, Distribution, Gating)

## Notes

<!-- Add findings, comparisons, blockers, and decisions here as the investigation progresses -->

## Decision

<!-- Record the outcome and reasoning once a decision is made -->
