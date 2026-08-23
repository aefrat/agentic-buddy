---
last_accessed: 2026-08-23
access_count: 2
created: 2026-07-26
---

# Red Hat Release Terminology - Reference

Authoritative definitions for Red Hat release types, extracted from internal
(The Source) and public (Customer Portal) documentation. Use this as the
reference when defining QE readiness criteria for any Red Hat product release.

## Sources

1. Common Release Terminology (The Source, internal) - PLM-managed definitions
2. General Availability (The Source, internal) - 19 GA release attributes
3. Technology Preview (The Source, internal) - 19 TP release attributes
4. Technology Preview Features - Scope of Support (Customer Portal, public)
5. Developer and Technology Previews: How they compare (Customer Portal, public)
6. Scope of Coverage Details (Customer Portal, public)

Source files saved at `~/Downloads/RH_release_defenitions/`.

---

## Release Type Taxonomy

### On-Premises / Self-Managed

| Type | Description |
|------|-------------|
| **General Availability (GA)** | Feature-complete, fully tested, fully supported. Production-ready. |
| **Beta** | Pre-release for evaluation. Not for production. |
| **Technology Preview** | Customer evaluation and feedback. NOT supported in production. On the product roadmap (with rare exceptions). |
| **Alpha** | Early pre-release. Not for production. |
| **Developer Preview** | Early evaluation. No commitment to future release. NOT supported at all. |

### Cloud Services

Service Preview -> Field Trial -> Limited Availability -> General Availability -> Service Sunset

### Key Distinction: Developer Preview vs Technology Preview

| Area | Developer Preview | Technology Preview |
|------|-------------------|-------------------|
| Future commitment | None | On product roadmap (rare exceptions) |
| Build & distribution | May use non-standard, unverified build tools | Built via Red Hat's verified secure pipelines |
| Testing | May not be fully tested by RH | More complete RH testing for supported configs |
| Support | NOT supported. No cases, bugs, or enhancements | LIMITED support. Cases accepted (Sev 3-4 only), no commercial SLA |
| Feedback | Collected, no response expected | Routed through support case system, acknowledgement expected |
| Documentation | Very limited, if any. Not in product doc set | Documented as part of product documentation set |

Both Developer Preview and Technology Preview:
- Are opt-in, fully configurable, default to disabled
- Are NOT for production environments
- Provide early exposure for feedback collection

---

## General Availability - 19 Release Attributes

These are the official requirements for any GA release:

1. **Customer Personas** - Entitled customers expecting production-ready software.
2. **Feature Status** - Feature-complete. All documented features implemented and tested. QE sign-off that no blocking/critical bugs remain. May include Tech Preview features IF labeled and disabled by default.
3. **Product Quality** - Fully tested by RH QE. QE managers signed off. All pre-GA bugs logged and prioritized. No blocker bugs. Bug reporting location clear to support org.
4. **Production Use** - Enterprise production ready. Supported in production.
5. **Productization** - Full productization process and gates (packaging, content verification, Product Security sign-off, release notes, source code). RCM ticket tracking.
6. **Life Cycle** - Review and possible update of published Life Cycle on Customer Portal. New major releases need new life cycle. Minor releases verified within existing life cycle. Product Manager + CEE/PXE responsible.
7. **Support Case Handling** - CEE ensures customers can open cases handled by capable SBR team. Most products: 24/7 coverage for Standard and Premium SLAs. May require training new support resources.
8. **CRM (Salesforce)** - Product Name and/or Version added. PXE manages via #plm-pxe.
9. **Backward Compatibility / API Stability** - Major releases may have breaks (must be documented). Minor releases must be drop-in replacements (no breaks). Changed supported configurations documented on Customer Portal.
10. **Product Security** - Completed Product Security Checklist. Pre-release security testing. No known vulnerabilities. CVE fix SLAs apply throughout life cycle.
11. **Deployment Methods** - Available via deployment channels (repos, Container Catalog, Customer Portal downloads). May be access-restricted for entitled customers only.
12. **Documentation** - Full documentation sets at production quality. All critical/blocking doc issues resolved. Red Hat written and curated (upstream docs not acceptable).
13. **Customer Portal** - Product landing page, documentation, life cycle page, supported configurations page, navigation for discoverability.
14. **Sales & Marketing** - Sales force enablement (training, materials, go-to-market). Required before GA.
15. **Announcements** - Internal and external release announcements. Product Manager responsibility.
16. **SKUs, engIDs, Entitlements** - Proper SKUs and entitlements in place for access and support.
17. **Legal Review** - Contracts contain proper language and appendix. Required for new products.
18. **Licenses Review** - Sub-component licenses documented. Product license documented for customer.
19. **Export Compliance** - Export Compliance/Certification from Legal. May not apply for minor/CP releases.

---

## Technology Preview - 19 Release Attributes

These are the official requirements for any Tech Preview release:

1. **Customer Personas** - Customers willing to evaluate before GA. May or may not be entitled. Any Customer Portal account holder can provide feedback via support cases.
2. **Feature Status** - May NOT be feature-complete. Documented features must be functional enough to evaluate. Limitations noted in Release Notes.
3. **Product Quality** - RECOMMENDED (not required) that QE teams test and QE managers sign off. May not be fully functionally tested across all supported configurations. MAY ship with known Blocker bugs IF documented in Release Notes AND no security/data loss implications. Bug reporting location must be clear to support org.
4. **Production Use** - NOT for production. Tech Preview features within GA releases must be configurable and default to disabled.
5. **Productization** - Generally goes through productization process but certain criteria may be waived (e.g., full localization). RCM ticket tracking.
6. **Life Cycle** - Does NOT conform to product's life cycle. At GA, Tech Preview becomes unsupported (60-day transition typical).
7. **Support Case Handling** - Must be set up with capable SBR. Cases accepted at Severity 4 only (Sev 3-4 per public portal). No time-based SLAs guaranteed.
8. **CRM (Salesforce)** - Product Name/Version added. Version string should indicate TP or Beta.
9. **Backward Compatibility / API Stability** - NOT expected to maintain full backward compatibility. No guarantee of patch migration from TP to GA. Full reinstallation may be required.
10. **Product Security** - MUST conform to Product Security requirements (same as GA). Checklist may be abbreviated with agreement from PM + Product Security + product team. CVE fix SLAs apply, but discontinuing the TP release is an alternative to fixing CVEs.
11. **Deployment Methods** - Available via deployment channels. MUST be clearly labeled as "Tech Preview". No patch migration guarantee.
12. **Documentation** - "Preview" documentation addressing TP features. Must be Red Hat written/curated (upstream docs not acceptable).
13. **Customer Portal** - Existing products: presented as any release but labeled "Tech Preview". New products: may use a support article instead of full Portal presence.
14. **Sales & Marketing** - Generally no special activities.
15. **Announcements** - Recommended (not required). Internal and external.
16. **SKUs, engIDs, Entitlements** - Existing products should already have them. New products: CEE engaged to ensure case handling works.
17. **Legal Review** - NOT covered by customer contracts. No review needed (unless noted, e.g., export compliance). Red Hat does not allow TP for production.
18. **Licenses Review** - Should undergo license review for sub-component and product licenses.
19. **Export Compliance** - Must be reviewed. May not apply for TP of existing products.

---

## Scope of Coverage Details

**Technology Preview within supported products:**
- NOT fully supported under Subscription Level Agreements
- May not be functionally complete
- NOT intended for production use
- No stability guarantee
- No seamless upgrade path guarantee from TP to GA
- May only be available for specific hardware architectures
- Customer cases limited to Severity 3-4
- Bug reports forwarded to Engineering as proposed for inclusion in future releases

---

## RHAS QE Readiness Gap Analysis

### How to use this section

The current RHAS release criteria (release-criteria-draft.md, Jul 21, 2026)
define 8 Monthly, 7 Tech Preview, and 8 GA criteria focused on technical
verification (build, deploy, test, security scan). The official RH release
terminology reveals additional organizational and process criteria that our
current document does not cover.

Below: criteria from the official definitions that are **not represented**
in the current RHAS release criteria, grouped by milestone.

### Missing from Tech Preview Criteria

| Gap | Official Attribute | Impact | Suggested Action |
|-----|--------------------|--------|------------------|
| **QE sign-off process** | TP attr 3: "recommended that QE managers have signed off" | No formal sign-off gate exists. Who signs off for RHAS? QE lead position is still vacant (PITCREW-337). | Add criterion: QE lead/manager sign-off on release. Resolve PITCREW-337 first. |
| **Support case handling (SBR)** | TP attr 7: "Case handling must be set up and handled by a capable SBR" | No criterion for CEE readiness. If customers can't open cases against RHAS TP, it fails the definition. | Add criterion: SBR team identified and trained. CEE confirms case routing works. |
| **Product Security checklist** | TP attr 10: "must conform to Product Security requirements" | TP-03 covers CVE scanning in images but not the formal Product Security Checklist. TP allows abbreviated checklist but it must exist. | Expand TP-03 or add new criterion: Product Security Checklist completed (abbreviated acceptable with PM + ProdSec agreement). |
| **Release Notes with known issues** | TP attr 3: "MAY ship with Blocker bugs IF documented in Release Notes" | No criterion for release notes existence or completeness. Official definition allows shipping with known blockers if documented. | Add criterion: Release Notes published covering known issues, limitations, and TP feature scope. |
| **Clear Tech Preview labeling** | TP attr 11: "MUST be clearly labeled as Tech Preview" | No criterion ensuring the product is labeled correctly in deployment channels, docs, and portal. | Add criterion: All distribution channels and documentation clearly label RHAS as Tech Preview. |
| **CRM/Salesforce representation** | TP attr 8: "CRM must be updated with Product Name/Version indicating TP" | Not covered. PXE team needs to configure. | Add criterion or capture as productization prerequisite. |
| **Feedback collection mechanism** | TP attr 1: Purpose is "collection of feedback back to product development" | No criterion for how customer feedback reaches engineering. The entire purpose of TP is feedback. | Add criterion: Feedback path documented (support case -> Jira -> engineering). |
| **License review** | TP attr 18: "should undergo a license review" | Not covered in any current criterion. | Add criterion or capture as productization prerequisite. |
| **SKUs/Entitlements** | TP attr 16: "CEE should be engaged to ensure case handling works" | Not covered. Required for customers to access the product and open cases. | Coordinate with CEE/PXE. |

### Missing from GA Criteria

All Tech Preview gaps above carry forward to GA (superset). Additional GA-specific gaps:

| Gap | Official Attribute | Impact | Suggested Action |
|-----|--------------------|--------|------------------|
| **Life cycle definition** | GA attr 6: "must include review and possible updating of Life Cycle" | No criterion. Life cycle must be published on Customer Portal before GA. | Add criterion: Product Life Cycle published on Customer Portal. |
| **24/7 support readiness** | GA attr 7: "24/7 coverage for Standard and Premium SLAs" | GA-level support is a hard escalation from TP's Sev-4-only. SBR training may be needed. | Add criterion: CEE confirms 24/7 SBR coverage for Standard/Premium SLAs. |
| **Backward compatibility policy** | GA attr 9: "Minor releases must be drop-in replacements" | No criterion defining compatibility guarantees between RHAS releases. | Add criterion: API/CLI compatibility policy documented for minor releases. |
| **Full documentation (not just validated)** | GA attr 12: "full documentation sets at production quality, Red Hat curated" | TP-04 is "documentation validated" (walkthrough by non-author). GA requires production-quality full doc sets. | Add GA-level criterion: Complete documentation set published, all critical doc issues resolved. |
| **Customer Portal presence** | GA attr 13: "landing page, documentation, life cycle, supported configs, navigation" | No criterion. Required for customer discoverability. | Add criterion: Customer Portal product pages live with full navigation. |
| **Sales & Marketing enablement** | GA attr 14: "enabling the Red Hat sales force before GA" | Not QE's direct responsibility, but GA cannot happen without it. | Capture as productization prerequisite. Flag to Product Management. |
| **Legal review** | GA attr 17: "contracts contain proper language" | Required for new products at GA. | Capture as productization prerequisite. |
| **Export Compliance** | GA attr 19: "Export Compliance/Certification from Legal" | Required for GA. | Capture as productization prerequisite. |
| **QE blocker-free sign-off** | GA attr 3: "A blocker bug will stop a GA release" | No explicit non-waivable criterion for zero blocker bugs. M-08 covers P1/P2 regressions but not the formal blocker definition. | Add non-waivable criterion: Zero open Blocker bugs. QE lead sign-off required. |

### Summary

The current RHAS release criteria are **engineering-focused** - they measure
whether technical components work. The official RH release terminology reveals
that release readiness is a **cross-functional** concern spanning QE, CEE
(support), PXE (portal), Product Security, Legal, Sales, and Product Management.

**Key insight:** The biggest gaps are not technical but organizational:
1. No QE lead to sign off (PITCREW-337, 3+ months unresolved)
2. No SBR/support readiness criteria at all
3. No feedback collection mechanism (the entire purpose of Tech Preview)
4. No productization prerequisites tracked (CRM, SKUs, Portal, Legal)

**Recommendation:** Split RHAS release criteria into two tracks:
- **QE Technical Gates** (current criteria) - owned by QE/engineering
- **Release Readiness Checklist** (new) - cross-functional checklist covering
  support, security, documentation, portal, legal, sales prerequisites

This separation lets QE focus on what they own while ensuring nothing falls
through the cracks on the organizational side.

---

## Governance

Changes to the Common Release Term definitions are managed through PLM's
PLMCORE Jira project. To request a change, use the PLM Support Request Form,
selecting "Provide tooling support on Product Pages, Support Exceptions, etc."

Contact for CRM/Portal configuration: #plm-pxe Slack channel (PXE team in
PLM Product Experience Engineering).
