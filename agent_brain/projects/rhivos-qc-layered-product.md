---
last_accessed: 2026-06-23
access_count: 3
created: 2026-06-23
---

# RHIVOS QC Layered Product — Status & Plan

**Epic:** [AUTOBU-1076](https://redhat.atlassian.net/browse/AUTOBU-1076) — RHIVOS Layered Products for Qualcomm
**Execution epic:** [VROOM-41521](https://redhat.atlassian.net/browse/VROOM-41521) — Toolchain QC LP infrastructure setup (Kanitha Chim)
**Owner:** Petr Sabata (epic) / Kanitha Chim (execution)
**Target:** August 2026 (Whitney Chadwick, can be revised)
**Slack channel:** #rhivos-sp-qc-layered-product (C0B3MNQSYE7)
**Coordination doc:** [Google Doc](https://docs.google.com/document/d/1trd3Ud3l0J-5BkUmB5MYUJTQrRMk1TSVa7KtzPIfD_U/) (created by Hubert)
**Product config repo:** [product-service-config-auto/rhivos.yaml](https://gitlab.cee.redhat.com/sp-pv-mdm/product-service-config-auto/-/blob/main/rhel/rhivos.yaml)
**Research:** [SKU/ProductID research](rhivos-sku-productid-research.md) — architectural analysis (why new Eng Product, SKU, content sets are required)

---

## Decision: Layered Product, not Extension

Whitney Chadwick gave the go-ahead (Jun 3): "Please proceed with creating new EngIDs for the QC layered product." The extension approach (like RHEL-for-NVIDIA/Voyager) was rejected — repo-level disable isn't strong enough for QC's requirement that only approved customers get QC bits.

Full chain required: new EngIDs → new SKU → gated content sets → CDN repos → Errata configs.

---

## Architecture

| Element | RHIVOS Base | RHIVOS QC LP |
|---------|-------------|--------------|
| EngIDs | 931 (FuSa), 1031 (Core) | **1123** (Core QC LP), **1124** (FuSa QC LP) |
| SKU | Existing RHIVOS SKUs | **New QC-specific SKU** (1 SKU → 2 EngIDs) |
| CDN repos | `/content/dist/rhivos2/2.0/`, `.../2.0-core/` | TBD — proposed: `.../dist/layered/rhivos2/2.0/`, `.../2.0-core/` |
| Access | All RHIVOS subscribers | Only customers with QC LP SKU |

---

## Progress (as of Jun 24, 2026)

### Completed

| Step | Ticket | Who | Date |
|------|--------|-----|------|
| Spike — compose/pipeline | VROOM-41522 | Ozan Unsal | Closed |
| Spike — gating | VROOM-41523 | Hubert Stefanski | Closed |
| Spike — distribution | VROOM-41524 | Kanitha Chim | Closed |
| EngIDs created (1123 + 1124) | VROOM-42115 | Matt Goldman / Kanitha | Jun 22 |
| CDN product ID push fix | RHELDST-42168 | Michal | Jun 16 |
| Product listing partial fix | RHELWF-14266 | Lukas Holecek | Jun 14 |

### In Review

| Step | Ticket | Who | Notes |
|------|--------|-----|-------|
| CDN directory path naming | VROOM-42116 | Matt Goldman | **Review** — MR #149 submitted in cdn-definitions-private (Jun 23). Awaiting review/merge. |

### Not Started — Distribution chain (sequential, all unassigned)

| Order | Ticket | Summary |
|-------|--------|---------|
| 1 | VROOM-42114 | Create Pub/CDN Repositories |
| 2 | VROOM-42113 | Create Errata configs |
| 3 | VROOM-42120 | Generate product IDs |
| 4 | VROOM-42121 | Push Product IDs to CDN Repos |
| 5 | VROOM-42119 | Add Gator advisory automation for LP |
| 6 | VROOM-42118 | Request Images Repository |

### Not Started — Gating

| Ticket | Summary | Assignee |
|--------|---------|----------|
| VROOM-42050 | Generate Gator configs for LP | Hubert Stefanski |
| VROOM-42184 | WaiverDB permission config for LP | Hubert Stefanski |

### Not Started — Compose (new tickets, Jun 23)

| Ticket | Summary | Assignee |
|--------|---------|----------|
| VROOM-44910 | Create QC variant for RHIVOS Core and RHIVOS Fusa LP | Ozan Unsal |
| VROOM-44911 | Create brew tags for QC packages | Ozan Unsal |

### Not yet ticketed

- Image distribution via access.redhat.com (needs `-files`/`-isos` repos; ref: RHELDST-34953).

### Interim solution (VROOM-41496 — stalled)

Stopgap while LP isn't ready: document how customers get QC packages from Qualcomm directly. Francisco da Rocha owns. 2 of 3 tasks unassigned, no activity since May 18.

---

## Critical Path

```
CDN path MR under review (VROOM-42116) ←── GATE
        │
        ▼
Create CDN repos (VROOM-42114)
        │
        ▼
Create Errata configs (VROOM-42113)
        │
        ▼
Generate product IDs (VROOM-42120)
        │
        ▼
Push product IDs to CDN (VROOM-42121)
        │
        ▼
Gator advisory automation (VROOM-42119) ──┐
Gator configs (VROOM-42050) ──────────────┤── LP infra ready
WaiverDB perms (VROOM-42184) ─────────────┘

Parallel: SKU creation (Claude Pariz) — can proceed now
Parallel: Compose variant + brew tags (VROOM-44910, 44911) — Ozan Unsal
```

---

## Risks

1. **CDN path MR needs approval.** MR #149 submitted in cdn-definitions-private but not yet merged. All 6 distribution tasks gated on this.
2. **6 distribution tasks are unassigned.** Sequential chain, long lead time.
3. **Supplier Solicitation.** Charles Timko flagged (Jun 22) that AUTOBU-1076 needs this process.
4. **SP RHEL Workflow staffing.** Christine Freitas warned — lost release engineering expertise (China Engineering exit).
5. **Image distribution.** No process for RHIVOS qcow images via access.redhat.com. Not on Konflux.

---

## Timeline Assessment

| Milestone | Target | Status |
|-----------|--------|--------|
| EngIDs | Done | Complete |
| CDN path decision | This week | **Medium** — MR #149 submitted, awaiting review |
| CDN repos + Errata configs | ~1-2 weeks after path decision | Medium — sequential, unassigned |
| SKU creation | ~2-3 weeks | Low — Claude Pariz notified, can start |
| Gating setup | Before August | **High risk** — Hubert transitioning |
| Compose variant + brew tags | Before August | Low — Ozan Unsal assigned (VROOM-44910, 44911) |
| **LP infra ready** | **August 2026** | **At risk** — CDN path + unassigned work |

~5 weeks to August target. CDN path MR submitted — once approved, distribution chain can start. The chain (6 sequential tasks, all unassigned) could take 3-4 weeks given external team dependencies.

---

## Key People

| Person | Slack | Role | Current action |
|--------|-------|------|----------------|
| Kanitha Chim | kchim | Primary executor | Waiting on Petr for CDN path; notified Claude Pariz for SKU |
| Whitney Chadwick | | Program owner, August timeline | — |
| Petr Sabata | contyk | Release/distribution, epic assignee | **Needs to approve CDN path** |
| Claude Pariz | | SKU team | **Next: create QC-specific SKU** |
| Matt Goldman | | Distribution — EngID/CDN tickets | Submitted MR #149 for CDN path (VROOM-42116 → Review) |
| Hubert Stefanski | | Gating (transitioning to RHAS) | Owns VROOM-42050, 42184 |
| Gadi Glogowski | | PM — SKU coordination | Brought Claude Pariz in |
| Leon Kang | lekang | SP RHEL Distribution consultant | Advised on EngID/content sets |
| Archana Katarki | | SP RHEL Distribution (mgr) | Consulted on CDN issues |
| Francisco da Rocha | | Interim solution (VROOM-41496) | Stalled |
| Charles Timko | | Supplier Solicitation flag | Commented Jun 22 |

---

## Kanitha Chim (kchim) — Slack Activity Log

### Jun 22
- Announced EngIDs obtained (1123, 1124) in #rhivos-sp-qc-layered-product. CC'd Claude Pariz for SKU creation.

### Jun 16
- Filed RHELDST-42168: product IDs not pushing to `rhivos-2_DOT_0-core` CDN repo. Tagged Archana Katarki and Leon Kang. Resolved same day by Michal.

### Jun 11
- Reported product listing inconsistency across errata advisories — stale listings from 22 days ago with debuginfo RPMs that shouldn't reach customers. Tried `compose-composedb-import` and errata reload, neither worked. Leon redirected to WF team. Filed RHELWF-14266.

### Jun 4
- Asked about distributing qcow images via access.redhat.com — no existing process. Not on Konflux.
- Acknowledged Claude Pariz readiness for SKU: "Will keep you posted."

### Jun 1
- Deep architecture discussion: proposed layered repo paths, confirmed 1 SKU → 2 EngIDs mapping, clarified QC content is additive.
- Asked Leon Kang: "Is it possible to extend existing RHIVOS EngIDs to additional repos for QC with restrictions?" → Answer: no, need new EngIDs.

### May 25
- Researched Voyager/RHEL-for-NVIDIA model. Identified Voyager has no separate EngID (open access), raised access control question for QC.

### May 14
- First engagement: "Timeline is around July. Looking for experts to help with guidance."

---

## Related Files

- [SKU/ProductID Research](rhivos-sku-productid-research.md) — full SKU→CDN chain analysis, Voyager comparison
- [RHIVOS 2.0 RC3](RHIVOS_2_0_release_RC3.md) — RC3 release (CDN product ID push issue is related)
- [RHIVOS Release Approach](rhivos-release-approach.md) — Brew tag structure, STAG proposal
- [Getting Engineering ID (EngID)](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196253131/Getting+Engineering+ID+EngID) — Confluence doc by Kanitha Chim documenting the full EngID creation process, key repos (product-service-config-auto, cdn-utils, psc-lib), and PSCA team contact
