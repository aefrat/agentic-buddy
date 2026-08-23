---
last_accessed: 2026-08-23
access_count: 4
created: 2026-06-08
---

# PitCrew / RHAS — Strategic Context Cache

Cached summary of the RHAS Strategic Guide and 2026 Roadmap. Refreshed monthly or when the source Google Docs change. Used by the `pitcrew-weekly-report` skill to avoid re-fetching quarterly docs every week.

**Sources:**
- Strategic Guide: Google Doc `10qaHs_mfOCJtIJoJq35HjhHAeLEMJwYde51wgCKrQx8`
- 2026 Roadmap: Google Doc `1j4Chcv71S8Y3P8HT2wTao9ZEoHoHm-X102VmaNpk1CA`

---

## Three-Tier Architecture

After Red Hat Summit 2025 lab preparation pain (integration instability, missing features, cross-BU dependencies), the strategy shifted from a comprehensive bundled product to a staged, incremental approach — only leading with products proven to work together. The full bundle remains the visionary end-state, not the opening pitch.

**Tier 1 — Standalone Builder:** RHEL + AIB + Language Containers. Target: systems admins, cost-sensitive orgs. Max control, portable artifacts, minimal cost. Entry point that creates the "value vacuum" selling OCP.

**Tier 2 — Automotive Suite (RHAS):** OCP + Builder Operator + Jumpstarter + Pipelines + GitOps + Keycloak. Target: Platform Engineers. Integrates existing GitForge (no rip-and-replace), hardware-in-the-loop testing via Jumpstarter. The core shipped product.

**Tier 3 — Unified Environment (IDP):** Adds Dev Spaces + Developer Hub + Quay. Target: CIO/CISO, greenfield. Single vendor, centralized governance. Long-term "north star" — lead with vision, land as Tier 2.

**Delivery model:** IaC (Ansible playbooks), Kubernetes Operators for lifecycle, persona-driven docs. Dual-track release: OS-aligned major releases tied to RHIVOS + continuous delivery for Builder/Jumpstarter via feature gates.

**Security posture:** Software supply chain review (especially Jumpstarter dependencies). Principle of least privilege — privileged containers mitigated with guidance now, removed architecturally long-term.

## 2026 Roadmap — "Stabilize and Scale"

Primary mission (Shawn Davis): ensure RHIVOS 2.0 success while maintaining Nissan and Traton commitments.

**Q1 (Done):** ADP Developer Preview, GitLab/GitHub/Keycloak integration, Builder + Jumpstarter preview, QC 8650 hardware enablement, RHEL 10.2 rebase starts.

**Q2 (Current):** RHIVOS 2.0 GA (ToolChain), OCI/bootc images, Safe Rust/C/C++ binaries, RPMs + Satellite OS updates, QC 8979/8255 + NXP S32N79, ISO 21434 cert (ToolChain), Tech Preview milestone target.

**Q3 (Target):** RHAS / ADP General Availability, Builder full release (SSO, RPMs), Jumpstarter full release, GitLab CI/IDE + GitHub CI/IDE, OpenTelemetry + Alerting + Monitoring, Infra/Docs/Example assets, Security Audit + UI in OCP.

**Q4 (Planned):** Hardware: QC 8387, NXP iMX8, Renesas R-Car X5H, NVIDIA. Driver isolation, Perf + Scale.

**Strategic risks:** exida certification scope (FuSa body) could shift Q3 timeline. Partner driver maturity (NVIDIA, NXP, QC) drives Q2/Q4 hardware targets. QNX competitive pressure on boot-time and security metrics.

## Release Versioning

**Convention:** `RHAS-MMYY` where MM = month (01-12), YY = year (last 2 digits).
Monthly releases, last week of each month.

**Reference:** See `agent_brain/projects/rhas-qe-agent/reference/release-naming-convention.md` for full convention details.

Key milestones:
- `RHAS-0426` — Developer Preview (April 2026, done)
- `RHAS-0926` — Tech Preview (September 2026)
- `RHAS-1226` — GA (December 2026)
- `1.0` — Dec 1, 2026

24 versions defined through December 2027.
