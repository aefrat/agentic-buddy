---
last_accessed: 2026-08-06
access_count: 1
created: 2026-08-06
---

# Lightwell - Targets and Metrics

Not for distribution. Supersedes prior Targets and Metrics tab.

## Commercial Targets

| Target | Date | Metric |
|--------|------|--------|
| 100 customers | Q3 2026 | Active members across all offerings |
| 1,000 customers | Q4 2026 | Cumulative member organizations |
| 100,000 package versions | Q4 2026 | Versions in catalog with active buildroots |
| 1,000,000 package versions | RH Summit 2027 | Versions in catalog with active buildroots |

**Why customers matter**: Network effect - each member brings vuln inventory and
package overlap. 100 = critical mass to validate Clearinghouse before contractual
SLAs. 1,000 = commercial scale to sustain investment.

**Why package versions matter**: Coverage is leading indicator for remediation
throughput. No buildroot = no fix possible. 100K = meaningful cross-section of any
single FSI member's SBOM. 1M = public proof point at Summit (most visible RH
external event).

## Operational Metrics

### M-Series: Are we fixing things?

| Metric | Measures | Why |
|--------|----------|-----|
| **M-0: Weekly Burn-down** | Vulns fixed and delivered per week | **North star metric**. Confirms remediation engine creates value |
| M-1: Package Version Coverage | Versions in catalog with active buildroots | Leading indicator for M-0 |
| M-2a: Backlog Age | Median age of claimed, unresolved vulns | Aged prioritized CVEs = operational failure |
| M-2b: Design Phase Burn-down | % of consensus priority list resolved | Exit gate for Design Phase, entry gate for Network GA |
| M-3: Remediation Turnaround | Median days intake to patch delivery, by severity | Basis for contractual SLA commitments at Premier GA |

### P-Series: Are partners getting value?

| Metric | Measures | Why |
|--------|----------|-----|
| P-1: Partner Remediation Throughput | Avg fixes delivered per partner per week | Confirms usable output, not just onboarding |
| P-2: Package Overlap at Intake | Overlap between partner inventory and catalog | Qualification gate; low overlap = low near-term value |
| P-3: Partner Data Delivery Compliance | SBOM, secure transfer, exploit data within 30 days | Non-compliance consumes capacity without feeding pipeline |
| P-4: Partner Engagement Rate | Check-in attendance + data request fulfillment, 30-day rolling | Persistent non-participation triggers review |

### C-Series: Can we handle more?

| Metric | Measures | Why |
|--------|----------|-----|
| C-1: Field CTO Utilization | Active design partners per Field CTO Architect | Capacity ceiling for white-glove onboarding |
| C-2: STAM Utilization | Active design partners per STAM | Premier-tier ceiling; 1:1 ratio required in design phase |
| C-3: Engineering Bandwidth | Weekly eng hours for remediation per partner | Back-calculates staffing from financial model |
| C-4: Onboarding Pipeline | Partners in each lifecycle stage | Flags pipeline pressure before delivery problems |
| C-5: Network Size | Active member orgs receiving patches, weekly | Tracks commercial growth and network scale |

## SLA/SLO

DRAFT - placeholders, will change during design phase. Authoritative terms in
Lightwell SLA/SLO Policy (linked in source doc).

## Dashboard

Internal dashboard required: near-real-time, accessible to engineering, program
mgmt, and field teams. Ownership by metric series lead (M: engineering, P: program
mgmt, C: Field CTO). Updated minimum weekly. Should surface commercial targets
alongside operational metrics and SLA/SLO performance.
