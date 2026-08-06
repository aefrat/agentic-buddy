---
last_accessed: 2026-08-06
access_count: 1
created: 2026-08-06
---

# Lightwell - Charter

Last updated in source doc: June 5, 2026.
Document owners: Ben Breard, James Labocki.

## What It Is

A managed security service. Customers point existing tools (Artifactory, Nexus,
Maven) at Red Hat's secure registry. Red Hat scans, backports, tests, signs, and
delivers patched artifacts at the customer's pinned version, and contributes
patches upstream.

Launches with Java/Maven, Python/PyPI, JavaScript/npm. Other ecosystems to follow.

### Problem

Enterprises lock dependency versions for stability and compliance. AI-powered
scanners now find critical vulns in those locked versions faster than security
teams can respond. The standard fix (upgrade to latest) breaks builds, fails
audits, takes weeks.

### Durable Advantage

Operational, not technological. 30 years of upstream trust, cooperative
intelligence network, compliance certifications (FedRAMP, FIPS, DORA), SLA-backed
remediation timelines. Tooling will be open sourced under Apache 2.0 - the value
is the operated service.

## Who It Serves (Q3 2026)

### Clearinghouse Members

Large financial institutions (initial focus). Shared intelligence and remediation
network. Members contribute anonymized package inventories and prioritized vuln
lists with provable exploits. Receive SLA-backed patches. All member data is
anonymized before storage. Risk transfer: Red Hat carries the fork instead of the
customer owning it indefinitely.

Adjacent efforts (partners, not competitors): Alpha-Omega, Akrites, FS-ISAC,
CISA/ONCD Gold Eagle. Lightwell is the downstream remediation complement to
intelligence-sharing networks.

### General Market

Enterprises/mid-market outside FSI. Access to curated catalog of patched, signed
artifacts. Single config update routes dependency resolution through secure
registry. No intelligence network participation, no SLA-backed remediation, no
prioritization voice.

## Offering Structure

Two-layer model:
1. **Network** - Curated catalog access, patched artifacts, supply chain docs
2. **Clearinghouse** - Vertical membership on top of Network. FSI first, others follow

**Design Phase**: Eligible customers collaborate with Lightwell team on processes,
ceremonies, tools. Get priority on vulns and influence on offering design.

Pricing: see Offering Summary and Offering Brief (linked in source doc).

## Service Lifecycle (14 Steps)

| Step | Name | Network | Clearinghouse |
|------|------|---------|---------------|
| 1 | Onboarding | Yes | Yes |
| 2 | Scanning (planned) | - | - |
| 3 | Discovery (planned) | - | - |
| 4 | Triage (planned) | - | - |
| 5 | Intake Validation | - | Yes |
| 6 | CVE Assignment | - | Yes |
| 7 | Patch Development | - | Yes |
| 8 | Build & Sign (Konflux SLSA L3, Sigstore/cosign, SBOM, OSV) | - | Yes |
| 9 | Distribution | - | Yes |
| 10 | Embargo Initiation (14-day min before upstream disclosure) | Yes | Yes |
| 11 | Validation | Yes | Yes |
| 12 | Deployment | Yes | Yes |
| 13 | Upstream Contribution | Yes | Yes |
| 14 | Disclosure | Yes | Yes |

Steps 2-4 are planned future services, not in initial offering.

**Customer action**: Add remote repo in Artifactory/Nexus pointing at Red Hat's
secure registry. Single settings.xml update. pom.xml stays the same.

**Red Hat delivers**: Signed artifacts with SBOM (CycloneDX), VEX/CSAF advisories,
SLSA L3 build provenance, Sigstore/cosign signatures.

## Ecosystem Strategy

### Partners as Customers

SIs, MSPs, ISVs join as Network Members themselves. Use Lightwell for own products,
recommend to clients. Demand-generation engine.

### Scanning/Remediation Vendor Partnerships

- **Scanning vendors** (Snyk, Veracode, Endor Labs, Semgrep): integrate detection
  output with Lightwell intake. Makes their product more valuable (resolution, not
  just reports).
- **Remediation vendors** (HeroDevs, Mend, Sonatype, Tidelift): participate in
  Clearinghouse, contribute to upstream patches, offer Lightwell-backed remediation.

Market-making strategy: Red Hat builds trusted registry + remediation pipeline,
invites ecosystem to plug in. Network effect compounds over time.

## Adjacent Offerings

| Offering | Relationship |
|----------|-------------|
| Trusted Libraries / Project Calunga (RHADS) | Being folded into Lightwell Network's Validated Repos (mid-Aug completion) |
| ELS / Security Select | OS-layer RPMs; Lightwell covers app-layer language packages. Layer without overlap |
| RHHI / Project Hummingbird | Secures container base images; Lightwell secures libraries inside |
| Project Balor | Predecessor. Proved AI-powered scanning economics. Findings feed Lightwell triage |
| Konflux | Shared infra. Builds Lightwell's patched artifacts |
| Gov't Clearinghouse (CISA/ONCD) | Private-sector counterpart. RH positioned as implementation partner |

## Key People

| Role | Person |
|------|--------|
| Product Manager | Ben Breard |
| Product Manager | James Labocki |
| IBM Coordination | Sarwar Raza |
| Offering Manager (interim) | Brennan Dobbins |
| Business Lead | Francis Chow |
| Clearinghouse Offering Lead | Jen Cavanaugh |
| ProdSec Lead | Ian Murphy |
| Architect | Mairin Duffy |
| Field CTO/Clearinghouse Customer Lead | Brent Holden |
| Program Manager | Amanda Carter |
| Backporting Lead | TBD |
| Marketing Lead | Brian Gracely |
| Product Ops | Jen Cavanaugh |

## Slack Channels

- `#project-manhattan` - Original team channel
- `#proj-lightwell-leadership` - IBM + RH exec leadership + core team
- `#team-lightwell-maven` - Shared with IBM middleware leadership
- `#lightwell-workstream-core` - Workstream and program leads
- `#forum-lightwell` - Discussion forum, whole company
- `#forum-lightwell-interest` - Sales teams registering customer interest
