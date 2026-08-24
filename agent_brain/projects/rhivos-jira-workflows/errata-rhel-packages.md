---
last_accessed: 2026-08-23
access_count: 1
created: 2026-08-23
---

# Errata Workflow for RHEL Userspace Packages

Critical workflow gaps and clarifications discovered Aug 23, 2026 in Slack thread
about bug VROOM-47509. Addresses automation limitations, manual steps, and ownership
for RHEL packages in RHIVOS releases.

**Source:** https://redhat-internal.slack.com/archives/C04QNKX7RU4/p1787215739036139

**Published to (Aug 24):**
- Distribution FA wiki -> `atc_llm_wiki/distribution-fa/errata-advisories.md` (RHEL package gaps section)
- RHIVOS Workflows wiki -> `rhivos-workflows-wiki/wiki/processes/errata-rhel-packages.md` (new process page)
- Confluence -> "Claude code - wiki draft" (Automotive space, page 402130012): wiki index + full errata content

## Problem Statement

The documented workflow assumes automation works uniformly for all VROOM tickets,
but **errata automation only works for RHIVOS packages, not RHEL Userspace Package
components**. This creates confusion about:

1. Who creates advisories
2. Who links bugs to advisories
3. How bugs get closed
4. When to use manual vs automated process

## Automation Scope

**Works automatically (RHIVOS packages):**
- If ticket has RHIVOS component + FixedInBuild set + exactly one fixVersion set
- When moved to Integration, automation creates/updates advisory for that release
- Tooling moves ticket from Integration to Release Pending
- When release ships, tooling closes ticket

**Does NOT work automatically (RHEL Userspace Package):**
- No advisory creation automation
- No automatic bug-to-advisory linking
- Requires manual workflow (see below)

**Key insight from Kyle Chim:** "The automation works for rhivos packages since we
use component to identify which package+version (build) to create advisory for so
if it's not rhivos package, the automation won't happen."

## Multi-Release Bug Cloning

**Rule:** One Jira issue can link to exactly one advisory. RHIVOS has separate
advisories for:
- RHIVOS Core (each version)
- RHIVOS ASIL (each version)

Therefore bugs need clones:
- One for each affected version stream (2.0.z, 2.1, etc.)
- One for Core, one for ASIL, per version

**Example for VROOM-47509:**
- Bug found in RHIVOS Core 2.0
- Affects both 2.0.z-core and 2.0.z (ASIL)
- Needs 2 bugs: one for 2.0.z-core, one for 2.0.z
- Optionally 2 more for 2.1-core and 2.1 (to verify no regression)

**Note:** Contyk suggested alternative - instead of creating 2.1 clones, link the
RHEL 10.3 verification ticket to the RHIVOS 2.0.z tickets. "If RHEL verified they
followed this workflow, we don't really need to verify it multiple times."

## Manual Workflow for RHEL Packages

### When to use manual workflow:

1. Bug has "RHEL Userspace Package" component
2. Bug warrants VROOM ticket (not just inherited via bulk advisory clone)
3. Need fix in Z-stream or want explicit RHIVOS advisory

### Steps:

1. **Clone bugs** for affected releases:
   - 2.0.z-core, 2.0.z (required if both affected)
   - 2.1-core, 2.1 (optional, for regression verification)

2. **Set fields:**
   - Describe test coverage
   - Link to PR fixing the bug
   - Set **Fixed in Build** (use 10.2.z or 10.3 NVR as appropriate)
   - Ensure exactly one **Fix Version** is set

3. **Move to Integration**

4. **Wait for compose:**
   - For 2.0.1: Wait for RC1 compose to be built
   - Kyle Chim: "After the compose for 2.0.1 is built, we will run a script to
     create those rhel errata"

5. **Create advisories manually** (4 total if doing all releases):
   - One for 2.1 ASIL
   - One for 2.1 Core
   - One for 2.0.z ASIL
   - One for 2.0.z Core
   - Available at: https://errata.engineering.redhat.com/products/225/product_versions

6. **Link tickets to advisories:**
   - Manually link each Jira ticket to its corresponding advisory
   - Kyle offered potential automation: "I can add that automation, if you promise
     to add fixed-in-build correctly to all tickets"

7. **QE work:**
   - Do whatever QE does with them
   - Move to Release Pending when satisfied

8. **Automatic closure:**
   - Once advisory ships, tooling will close the ticket
   - Resolution: Done-Errata

## Bulk Advisory Creation (Non-Critical RHEL Packages)

For RHEL packages that don't warrant explicit VROOM tickets:

1. Kyle runs script after compose is built
2. Script clones RHEL advisories into RHIVOS releases
3. All RHEL 10.2.z packages that made it into latest-rhivos-2.0-core compose get
   RHIVOS advisories automatically
4. These are bulk/clone advisories - no individual VROOM tickets attached

**Key distinction:** If a RHEL package issue warrants a VROOM ticket (like
VROOM-47509), it should get explicit RHIVOS advisory, not just rely on bulk clone.

## Who Adds Bugs to Errata

**Unresolved as of thread:**

Martin's perspective:
- In FDA team: developer's responsibility (they build the package)
- In BOA team: RHEL developer builds the package
- Only RHIVOS QE knows there's a RHIVOS bug in RHEL package
- Therefore RHIVOS QE should be responsible for adding to errata + verification

Luigi/Jan's perspective:
- QE should not be adding bugs to errata

**Recommendation from Contyk:** "Feel free to raise it in PDR Staff or RHIVOS PO
meetings to clarify"

## Workflow Documentation Gaps

Issues identified in the thread that aren't clear in the documented workflow:

1. **Multi-release cloning:** Not explained that you need one bug per Core/ASIL
   release combination. Contyk: "Well, that's somehow common knowledge" - but it's
   not documented.

2. **Automatic closure:** workflow-product.md says "Once a release goes live, all
   issues should be Closed with Resolution: Done-Errata" but doesn't explain:
   - This happens automatically via tooling
   - Only works if bug properly linked to advisory
   - Only works after advisory ships

3. **Errata link field timing:** workflow-product.md says "When the ticket is
   included in an erratum, link to it in the Errata Link field" during In Progress,
   but for RHEL packages:
   - Errata doesn't exist until after compose is built
   - Can't link until bulk advisories are created
   - May need to sit in Integration waiting for RC1 compose

4. **Automation scope:** No indication that automation works differently for RHIVOS
   packages vs RHEL Userspace Package components.

## Recommendations

1. **Document automation scope** clearly in automations.md - which components get
   automatic advisory creation, which require manual workflow

2. **Multi-release cloning rule** should be explicit in workflow-product.md, not
   "common knowledge"

3. **Clarify ownership** of errata linking for RHEL packages - escalate to PDR
   Staff or RHIVOS PO meeting

4. **Wait strategy for RHEL packages:** Document that bugs with RHEL Userspace
   Package component should:
   - Move to Integration with FixedInBuild set
   - Wait for RC compose
   - Get linked to bulk-created advisories
   - Then proceed to Release Pending

5. **Consider Kyle's automation offer:** If QE commits to setting FixedInBuild
   correctly, Kyle can add automation to link bugs to bulk advisories

## Key People

- **Kyle Chim (@kchim):** Errata automation, owns bulk advisory creation script
- **Petr Contyk (@contyk):** RHIVOS Product Owner, errata process expert
- **Martin Perina (@mperina):** FDA team context, errata workflow experience
- **Luigi Pellecchia:** QE hitting these workflow gaps in practice
- **Jan Onderka (@jonderka):** QE perspective on errata responsibilities

## Open Questions

1. Is QE or Dev responsible for adding RHEL package bugs to RHIVOS errata?
2. Should Kyle's automation for linking bugs to bulk advisories be implemented?
3. Should the workflow mandate 2.1 regression clones, or is linking to RHEL 10.3
   verification sufficient?
4. When should "Downstream Component Name" field be used for RHEL packages to
   enable potential future automation?
