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

### Open questions (still to investigate)
- What exactly does the RHEL-for-NVIDIA knowledge base propose technically? What parts are reusable vs RHEL-specific?
- Can Juanje's "same pipeline + separate at CDN" approach work without adopting any of the RHEL-for-NVIDIA tooling?
- Extensions repo approach vs. full layered product — what's the difference in overhead?

### Action items from the meeting
- [Avi] Compile list of stakeholders for async layered product discussion
- [Whitney] Consult with release SP team on who should be involved for the extension repo discussion
- Async discussion to be scheduled with ATC focals (Build, Distribution, Gating)

## Notes

<!-- Add findings, comparisons, blockers, and decisions here as the investigation progresses -->

## Decision

<!-- Record the outcome and reasoning once a decision is made -->
