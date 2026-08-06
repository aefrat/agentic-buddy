---
last_accessed: 2026-08-06
access_count: 1
created: 2026-08-06
---

# Lightwell Principles

7 principles governing process decisions.

## 0. Focus is application dependencies, not platforms

Patches vulns in third-party open source packages, not platforms already supported
by IBM/Red Hat. Red Hat product vulns go through Product Security separately. If an
IBM/RH product patches a vuln in a product component, it may also ship in Lightwell.

## 1. Every fix goes upstream

Customer receives fix first. Upstream submission follows. Applies to every fix
unless the vuln is not present or already fixed upstream.

- Critical/Important: Red Hat coordinates upstream submission directly
- Moderate/Low: may work through designated upstream partner orgs
- Abandoned projects: vulnerability report sent to maintainer of last resort.
  Lightwell does not take on general maintenance of abandoned projects

## 2. Embargo windows are short by default

Embargo = period where known vuln is not disclosed publicly. Independent discovery
is common - assumption of exclusive knowledge is rarely sound. Longer embargo
extends exposure window under false assumption.

Different targets for different stages (discovery to upstream notification).
Extensions require documented justification tied to deployment need. No guarantee
upstream honors embargo windows. Operates under assumption other parties already
know.

## 3. Notification rights depend on membership tier

- **Clearinghouse members**: When any member reports a vuln, all other members of
  the same clearinghouse are notified simultaneously upon confirmation - before
  patch is available. Cross-clearinghouse notification follows patch embargo timeline.
- **Network members**: Receive fixes as published. Same access, same schedule.
- **Regulatory reporting**: Remains with member org. Lightwell helps understand how
  disclosure timelines interact with obligations but does not make regulatory
  submissions on behalf of members.

## 4. Reporting information is confidential

Customer identity not exposed without specific need-to-know, and absolutely no one
outside the Lightwell program.

- Within clearinghouse: members notified of vuln, not who reported it
- To upstream: reporter identity not disclosed. Only technical info provided
- Anonymity covers identity only - does not affect timelines, technical detail,
  or notification rights

## 5. Open source community is a partner

Maintainers carry long-term maintenance cost. Lightwell provides timely notification,
patches in usable form, enough technical context.

- Help communities develop embargo/disclosure policies where missing
- Document and continue engaging if upstream declines a fix
- For inactive/unmaintained projects: coordinate with maintainer of last resort
  organizations. Lightwell does not take on fork maintenance or stewardship

## 6. Product Security and Lightwell coordinate but do not wait

When a vuln affects both a Lightwell-scoped package and an RH product, both streams
notified internally and immediately. Each produces own remediation artifact.
Shorter embargo governs by default. Neither delays disclosure for the other.

Three flows:
1. **Lightwell to ProdSec**: ProdSec notified same business day on Lightwell
   discoveries/member reports. Gets vuln intel + reference patch as head start
2. **ProdSec to Lightwell**: Lightwell notified same business day when RH security
   work finds vuln in a Lightwell catalog package. Delivery obligation is Lightwell's.
   Exception: if Finder embargo prohibits disclosure to entities outside RH, ProdSec
   respects it - Lightwell stages fixes ready for disclosure without pre-disclosing
   details to members
3. **Member-reported RH product issues**: Acknowledged and routed to ProdSec within
   24 hours. Member does not need to determine the boundary
