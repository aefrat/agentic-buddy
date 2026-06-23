---
last_accessed: 2026-06-23
access_count: 2
created: 2026-05-21
---

# ATC LLM Wiki

## Status

Active — wiki created, working out where to host it and how to publish the docs site.

## What it is

An LLM wiki generated for the ToolChain (ATC) team from all ATC repos, created ~2026-05-14 using:
- Skill: https://gitlab.cee.redhat.com/automotive/ai/skills/common/codebase-documenter

## Juanje's feedback (Slack DM, 2026-05-21)

- The format is suited for LLM wiki / format databases
- Suggested hosting location: the toolchain namespace at https://gitlab.cee.redhat.com/automotive/pipe-x/ (where ATC project docs live)
- Also recommended deploying the mkdocs website — options: GitLab Pages, a dedicated domain, or an S3 bucket

## Open decisions

- ~~Where does the wiki source live?~~ → **DONE:** pushed to https://gitlab.cee.redhat.com/automotive/pipe-x/atc_llm_wiki
- Where does the mkdocs site get deployed? → GitLab Pages / domain / S3 (not yet decided)
- How often does the wiki get regenerated from repos? (maintenance cadence not yet defined)

## Confluence Documentation

New pages added to the Automotive Confluence space that should be indexed in the wiki:

### Getting Engineering ID (EngID)
- **Page:** [Getting Engineering ID (EngID)](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196253131/Getting+Engineering+ID+EngID)
- **Author:** Kanitha Chim (kchim@redhat.com)
- **Created:** 2024-06-10
- **Space:** Automotive (In-Vehicle OS)

**Content summary:**

Engineering ID (EngID) is correlated to a Product (e.g., RHIVOS) and can be grouped by variant/architecture (x86_64, aarch64). The internal team managing product/service configuration is **PSCA** (#psca-support on Slack).

**Key repositories:**
- Product config: [product-service-config-auto/rhivos.yaml](https://gitlab.cee.redhat.com/sp-pv-mdm/product-service-config-auto/-/blob/main/rhel/rhivos/rhivos.yaml)
- CDN directory layouts: [cdn-utils](https://gitlab.cee.redhat.com/exd-guild-distribution/cdn-utils/)
- Pre-prod config: [product-service-config-auto-preprod/rhivos.yaml](https://gitlab.cee.redhat.com/sp-pv-mdm/product-service-config-auto-preprod/-/blob/main/rhel/rhivos/rhivos.yaml)
- PSC library: [psc-lib](https://gitlab.cee.redhat.com/sp-pv-mdm/psc-lib)

**Each product needs:**
- ID (EngID, auto-generated after config merge)
- Name, Architectures, Environments (stage/prod)
- Content sets with unique IDs and CDN paths (e.g., `/content/dist/rhivos1/1.0/aarch64/os`)

**Steps to get EngID:**
1. Agree with PM on number of EngIDs needed
2. Add signing keys to cdn-definitions-private repository (if new product)
3. Add DirectoryLayout to cdn-utils (if new layout needed)
4. Wait for MRs to merge and cdn-utils release
5. Add code to psc-lib repository
6. Add product config to pre-prod repo and verify
7. Add product config to prod repo
8. EngID is created after prod MR merges

**Note:** Contact #psca-support for repository access. Additional docs: PSCA User documentation (Confluence space PVCORE).

## Notes

<!-- Add progress, decisions, and blockers here -->
