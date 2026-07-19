---
last_accessed: 2026-07-19
access_count: 2
created: 2026-05-31
---

# RHIVOS QC LP — SKU, Product ID, and Repository Access Research

**Context:** AUTOBU-1076 — evaluating what is needed to gate the RHIVOS QC Layered
Product repositories to customers with Qualcomm partner/customer agreements.

**Sources:** RHELDST Confluence (`RHELDST/Technical Documentation` space), RHEL-for-NVIDIA
knowledge base (`/home/aefrat/rhel-for-nvidia-knowledge`), ATC codebase docs.

---

## The Full Chain: SKU → Repository Access

The access control chain flows in one direction:

```
Customer buys SKU
      ↓
Candlepin issues Entitlement Certificate  (x.509, installed at /etc/pki/entitlement/)
      ↓
Certificate lists authorized Content Sets
      ↓
CDN Authorizer checks:
  (1) Does the client's entitlement cert cover this content set?
  (2) Does the client system have the required Product ID cert?
      ↓
Access granted → client downloads from CDN
```

### 1. SKU
A commercial subscription product sold to customers (e.g., "Red Hat Enterprise Linux
for NVIDIA"). The SKU defines what a customer has purchased. It maps to entitlements
in Candlepin.

### 2. Candlepin + Entitlement Certificate
When a customer attaches a subscription, Candlepin issues an x.509 entitlement
certificate to the system. This certificate lists the **content sets** the customer
is authorized to access.

### 3. Content Set
Metadata object in Product Service. Key fields:

| Field | Example (Voyager) | Purpose |
|-------|-------------------|---------|
| Name | Red Hat Enterprise Linux 10 for ARM 64 - NVIDIA (RPMs) | Human-readable |
| Label | `rhel-10-for-aarch64-nvidia-rpms` | Machine ID; used by `subscription-manager`, Pulp |
| Download URL | `/content/dist/layered/rhel10/$basearch/nvidia/os` | CDN path template |
| Architecture | aarch64 | Supported arch |
| Required tag | e.g., `rhel-10` or `rhivos-qualcomm` | Product ID that must be present on system |

Content sets are stored in Product Service (Engineering Product Proxy) and defined
via the `product-service-config-auto` GitLab repo. Changes flow through:
`product-service-config-auto` → `engproduct-cli` / `rcm-push-dat` → Product Service
→ `cdn-utils` (creates/updates Pulp repos) → Candlepin (includes in entitlement certs).

### 4. Engineering Product (Eng Product) and Eng ID
An internal technical grouping of content sets. Each Eng Product has an integer
Eng ID (e.g., RHIVOS uses 931, 1030). Content sets under an Eng Product inherit
its Eng ID.

- The Eng ID appears in the Product ID certificate installed on customer systems.
- The CDN Authorizer checks the "required tag" on a content set against Product ID
  certificates present on the requesting system.

### 5. Product ID Certificate
An x.509 certificate installed on the customer's system (at `/etc/pki/product/`)
that identifies which Red Hat products are installed. The certificate includes a
"provides" tag (e.g., `rhivos-qualcomm-2`) that the CDN Authorizer matches against
the "required tag" field of content sets.

### 6. CDN Authorizer (edgejava/edgecert)
Runs at the Akamai edge. For each CDN request:
1. Checks the client's entitlement cert → must cover the requested content set label.
2. Checks the client's Product ID cert → must provide the "required tag" of the
   content set (if one is set).

Both checks must pass. This is how gated access works.

---

## Voyager (RHEL for NVIDIA) — What They Chose

**Decision #7:** New CDN repo under the **existing RHEL Eng Product** (option b of 4
options considered). RHELDST-36526.

**Decision #8:** **No new Eng ID, no new SKU.** Voyager repos available to all RHEL
subscribers. No separate entitlement required. RHELDST-37036.

**Why this worked for Voyager:** NVIDIA hardware enablement content is freely
distributable. There is no Qualcomm-style partner agreement gating access. Any RHEL
customer can opt into Voyager repos — they just need to enable them:
```
subscription-manager repos --enable rhel-10-for-aarch64-nvidia-rpms
```

Option (c) — "new eng product with its own SKU mappings" — was explicitly considered
and **rejected** for Voyager with the note: "This is how RHEL AI is set up." It would
have allowed access control via SKU, but that wasn't a Voyager requirement.

---

## RHIVOS QC LP — What Is Different and Why

**The critical difference:** Qualcomm packages are proprietary. Access must be gated
behind a three-way partner/customer/Red Hat agreement. This is the requirement Petr
Sabata flagged in AUTOBU-1076 and is what makes the Voyager model inapplicable.

### What RHIVOS QC LP needs

| Element | Voyager | RHIVOS QC LP |
|---------|---------|--------------|
| Eng Product | Reuses RHEL Eng Product | **New Eng Product required** |
| Eng ID | Reuses RHEL BaseOS Eng IDs | **New Eng ID required** |
| SKU | Included in all RHEL SKUs | **New SKU required** (gated access) |
| Content set "required tag" | `rhel-10` (any RHEL system) | **New tag** (e.g., `rhivos-qualcomm`) |
| Product ID on customer system | Not needed for access | **QC LP Product ID cert required** |
| Who can access | All RHEL subscribers | Only customers with QC LP SKU |

### The mechanism for gated access

1. Red Hat creates a new **Eng Product** (e.g., "RHIVOS Qualcomm Layered Product")
   with a new Eng ID.
2. New **content sets** are defined under this Eng Product with:
   - Labels: e.g., `rhivos-2-qualcomm-aarch64-rpms`
   - CDN path: e.g., `/content/dist/layered/rhivos2/aarch64/qualcomm/os`
   - Required tag: e.g., `rhivos-qualcomm` (the QC LP Product ID must be installed)
3. A new **SKU** is created and mapped to these content sets in Candlepin.
4. Customers who buy the QC SKU receive an entitlement cert including QC content sets.
5. A **QC LP Product ID cert** (installed by the QC packages themselves) is required.
   The CDN Authorizer validates both the entitlement cert AND the Product ID.
6. Customers without the SKU: no entitlement cert covering QC content sets → denied
   at the CDN Authorizer.

### The Layered Product ProductID Policy (RHELDST Confluence 175385989)

Key quote: "If the only role of Product ID 'provides' tags is permitting system
entitlement to additional content sets (those content sets requiring this tag), it
would seem that these aren't important for layered products... unless further products
layer upon them."

For RHIVOS QC LP the Product ID IS important because:
- The "required tag" on QC content sets must reference the QC Product ID
- This ensures the customer system has the QC product actually installed (not just
  entitled) before accessing the repo
- This is the standard layered product gating model (same as RHEL AI, Satellite)

Recommendation from the policy doc: the "provides" tag list for a GA layered product
should include a comma-separated list with the hyphenated LP short name and versioned
variants. E.g., `rhivos-qualcomm,rhivos-qualcomm-2` for a RHIVOS 2.x QC LP.

---

## The Overhead Whitney Is Concerned About

The SKU/Eng Product route triggers a cascade of downstream work:

| Area | Work needed |
|------|-------------|
| Product Service | New Eng Product + content sets via `product-service-config-auto` MR |
| Candlepin | SKU mapping to content sets |
| Customer portal | New product page, entitlement portal integration |
| `subscription-manager` | QC repo labels customers must enable |
| Errata Tool | Separate Product Version + Variant + Releases under QC LP Eng Product |
| RHSM Pulp | New repos per content set (via `cdn-utils`) |
| CDN Authorizer | Content set "required tag" must be set correctly |
| Partner agreements | Three-way legal setup (Red Hat / Qualcomm / customer) |

This is exactly "option (c)" that Voyager rejected. It is heavier than Voyager's
path but unavoidable given the access control requirement.

---

## Extensions Repo Route — Would It Avoid the Overhead?

Option (a) in the Voyager analysis was "Extensions repo" — pushing packages into
the existing Extensions repository with no new Eng Product or SKU.

**Why it doesn't work for RHIVOS QC LP:** The Extensions repo is open to all RHEL
subscribers. It cannot be access-gated by SKU. Any customer would be able to pull
the QC packages without the partner agreement. This is a non-starter for proprietary
Qualcomm content.

The extensions route would only work if QC packages were freely distributable —
which may apply to some packages (e.g., the kernel) but not the full audio/video stack.

---

## Open Questions for RHELDST/Distribution Team

1. **Can the "required tag" on content sets provide lighter-weight access control**
   without a full new Eng Product? I.e., could QC content sets be added under the
   existing RHIVOS Eng Product with a new required tag that only QC-subscribed
   customers get in their entitlement certs?

2. **Is there a precedent for a "lite" layered product** — content sets under an
   existing Eng ID but behind a new SKU gate — that avoids the full new Eng Product
   setup?

3. **RHEL AI** is mentioned as an example of option (c) (new eng product + own SKU).
   Worth pulling their setup as a reference if RHIVOS QC LP goes the same route.

---

## Reference Links

- RHELDST Confluence — Layered Product ProductID policy: page 175385989
- RHELDST Confluence — Accessing RHSM Content: page 175375473
- RHELDST-36526: Voyager release configuration design (option b decision)
- RHELDST-37037: Voyager CDN repository naming
- RHIVOS project file: `agent_brain/projects/rhivos-release-approach.md`
- RHIVOS vs Voyager comparison: `user/rhivos-vs-rhel-nvidia-comparison.md`
