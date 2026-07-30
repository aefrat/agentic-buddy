---
last_accessed: 2026-07-30
access_count: 1
created: 2026-07-30
---

# RHIVOS 2.0 Retrospective

## Context

Retro meeting for RHIVOS 2.0 release, organized by David Walker (dawalker). For POs and Tech Leads. Meeting: 2026-07-30 17:00 IDT.

**Source doc:** [RHIVOS 2.0 Retro](https://docs.google.com/document/d/17q7g2rd3-JvBy7jHn3Py85fqAPmYvN0Wwxe-uNIs7FI/edit)

## Attendees

Accepted: Whitney Chadwick, Stephen Loranz, David Walker (organizer), Pavol Brilla, Shlok Jalgaonkar, Francisco da Rocha, Gadi Lahav, Kanitha Chim, Avihai Efrat, Petr Sabata, Charles Timko, Laura Leistner, Simo Bonazzo, Juanje Ojeda, Ozan Unsal, Eitan Benes.
Declined/PTO: Ian McLeod, Yael, Pierre-Yves Chibon (pingou), Rachel Sibley, Martin Perina.

## What Went Well

1. **Release delivered on time** despite multiple unknowns, respins, CVEs, and key people on holidays. RC1-RC3 built, tested, delivered. [Avi]
2. **Docs:** Complete downstream doc set developed, aligned with JTBD/user journey. Gaps captured as backlog. [Docs]
3. **Cross-team collaboration:** Ad-hoc collaboration between AIB, RHAS, Kernel, Toolchain resolved potential blockers quickly. [Juanje/ATC]
4. **Pipeline migration to pac-jobs:** Simpler and faster to fix issues, adjust, retry on the fly. [Juanje/ATC]
5. **Pipelines-debugger agent:** Early adoption helped with triaging pipeline errors. [Juanje/ATC]

## What Didn't Go Well

### Avi/ATC - Kernel Brew tag permissions bottleneck

Tagging kernel RPMs to 2.0 `-gate` delayed release gating and compose builds:
- Kernel folks lacked Brew tag permissions - had to wait for Sameera Kalgudi/Ozan Unsal for daily manual tagging
- No clear/updated doc from kernel or RHEL kernel maintainers on correct tag for 2.0 vs 2.0-z
- Missing program-level documentation on who (team and focals) should do what

### Juanje/ATC - NVR mismatches and kernel blockers

- NVR mismatches (kernel-ivos/dtbs/scmi chicken-egg) blocked nightlies and releases multiple times
- RC2 blocked by external kernel MR (io_uring disabling)
- Unsigned kernel-automotive packages promoted to -candidate, ODCS rejected compose
- Infra issues: Tekton lease leaks (2h+ waits for Qualcomm boards), Docker runner failure at GitLab.cee, Fastboot board detection

### Eitan/ATC - Distribution setup

Navigating distribution setup for release images was slow, time-consuming, high effort:
- Very little documentation of the process
- Many teams involved, each responsible for a small portion
- Lots of manual work by ATC and other teams

### Ozan/ATC - Late kernel changes

Late availability of last-minute changes (kernel + dependent packages) introduced risk and stress during release.

### FDA/Docs

- AutoSD vs RHIVOS format mismatch (markdown vs asciidoc)
- SME ownership/engagement gaps
- Missing engineering-to-documentation traceability
- Source information availability challenges

## Improvements Proposed

### Done (by Avi)

- **RHELBLD-18777** - Extended Brew tag permissions to RHIVOS kernel maintainers (auto-kernel-maintainers group). Resolved.
- **RHELBLD-18778** - Extended Brew tag permissions to full ATC team. Resolved.
- Communicated new permissions to both Kernel and ATC teams.

### Not Done / Unknown Status

- **Petr Sabata's KWF alignment meeting** - Petr mentioned he planned a meeting with RHIVOS kernel team and RHEL KWF team to align tag workflows. **No evidence this meeting took place** (checked Slack + Calendar Jul 30). Follow up.
- **STAG automation** (Petr's lockstep build proposal) - Would eliminate manual tagging entirely. Not implemented.

### Other Improvement Items

- [Juanje] Improve gating of IVOS kernel-automotive packages and dependencies (in progress)
- [Juanje] Document and ensure all package-building teams know the process including RPM signing
- [Juanje] Centralized Slack channel for cross-team technical release issues; improve triage visibility
- [Ozan] Define target kernel version early in release cycle; align all kernel-dependent packages before pipeline starts
- [GG] Document SKU/Repo presentation steps (CDN, staging)
- [Avi] Cross-team knowledge sharing on release process - reduce single-focal dependency (Petr S.)
- Errata Tool usage and workflow gap
- Clear ownership of end-to-end release steps
- [Docs] Establish clear feature ownership, strengthen engineering-to-docs traceability, improve doc readiness

## Action Items (from meeting)

Action items section is empty in the doc pre-meeting. To be filled during/after the retro.

**Likely ATC action items based on retro content:**

1. Follow up with Petr on KWF alignment meeting status and STAG automation timeline
2. Document the Brew tagging workflow (who tags what, when, to which tag) - currently undocumented (gap #1 from Jun 14 audit)
3. Document distribution setup process (Eitan's pain point)
4. Contribute to centralized release issue channel setup (Juanje's proposal)
5. Continue kernel gating improvements (Juanje, in progress)

---

*Post-meeting: update this file with actual action items assigned to Avi/ATC.*
