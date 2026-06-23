---
last_accessed: 2026-06-23
access_count: 1
created: 2026-06-23
---

# RHIVOS QC Layered Product — Distribution Setup

Implementation of the RHIVOS Qualcomm Layered Product distribution infrastructure: EngIDs, content sets, CDN paths, errata, and product registration.

**Research:** [SKU/ProductID research](rhivos-sku-productid-research.md) — the architectural analysis behind the approach (why new Eng Product, SKU, and content sets are required for gated access to proprietary QC packages).

## Key tickets

| Key | Summary | Status | Assignee |
|-----|---------|--------|----------|
| VROOM-42115 | Request EngIDs for RHIVOS Core and RHIVOS Fusa QC Layered Product | **Closed** | Matt Goldman |
| VROOM-42116 | Request CDN directory path for RHIVOS Core and Fusa QC LP | **In Progress** | Matt Goldman |
| VROOM-41430 | Pushing product IDs for Fusa Repo to CDN stage and CDN live | **Review** | Kanitha Chim |
| VROOM-39023 | Monitoring and moving rhivos-2.0-core advisories to correct state | **In Progress** | Kanitha Chim |

## Key activity

- **2026-06-23 (report):** VROOM-42115 closed — EngIDs assigned for RHIVOS Core and Fusa QC layered products (Matt Goldman). VROOM-42116 started — CDN directory paths, with MR !858 opened in `product-service-config-auto` to add content sets for RHIVOS QC and Fusa layered products. Kanitha shared newly assigned EngIDs in #rhivos-sp-qc-layered-product.

## Slack channels

- `#rhivos-sp-qc-layered-product` (C0B3MNQSYE7) — primary coordination channel

## People

- **Matt Goldman** — distribution infrastructure (EngIDs, CDN paths, content sets)
- **Kanitha Chim** — errata and product ID push to CDN
- **Petr Sabata** — original requirement (AUTOBU-1076, gated access for QC packages)

> Related: [RHIVOS 2.0 RC3](RHIVOS_2_0_release_RC3.md) — the release that first surfaces QC LP errata needs. [RHIVOS release approach](rhivos-release-approach.md) — general release process.
