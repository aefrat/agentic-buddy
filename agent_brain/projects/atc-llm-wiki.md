---
last_accessed: 2026-07-30
access_count: 5
created: 2026-05-21
---

# ATC LLM Wiki

## Status

Active — wiki created with two content sources: codebase docs (May 2026) and Confluence Distribution FA pages (Jul 30, 2026). Hosting/deployment still open.

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
- How to keep Confluence-sourced content in sync? (re-ingest on demand vs scheduled)

## Confluence Distribution FA Ingestion (2026-07-30)

Ingested 39 pages from [Auto Toolchain Distribution Focus Area](https://redhat.atlassian.net/wiki/spaces/Automotive/pages/196262002) into `distribution-fa/` directory (13 topic files + index):

| Wiki file | Topics | Source pages |
|---|---|---|
| overview.md | What the FA does, channels, content flow | 2 |
| onboarding.md | Team structure, buddy system, Zero-to-Hero, glossary | 3 |
| access-and-permissions.md | Errata roles (6), Rover groups (4), tools | 2 |
| errata-advisories.md | Types, lifecycle, clone vs specific, scripts | 7 |
| rpm-signing.md | RADAS, manual EC2, key architecture | 3 |
| cdn-publication.md | Channels, staging, Pub CLI, verification | 5 |
| product-ids-and-engids.md | EngID lifecycle, PSCA, product listings | 3 |
| rhsm-pulp.md | Repo management, content sets, CDN paths | 2 |
| release-process.md | Full checklist, compose staging | 2 |
| repositories-and-resources.md | 14 repos, URLs, contacts, quick ref | 2 |
| principal-guide.md | Senior engineer architecture view | 1 |
| partner-distribution.md | Artifactory, download server, SFTP | 3 |
| knowledge-transfer.md | Marcel Banas, Paul offboarding notes | 2 |

Raw HTML stored in `distribution-fa/raw/` (not committed). Disconfirmation gate passed (3/3 questions answered from wiki alone).

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

## Pulp Migration — Knowledge Base Content

From Toolchain Demo/Review (Jun 24, 2026) — [meeting notes](https://docs.google.com/document/d/1HWpHwkWYZY1rlx6h8gQnlNDWPDJ7fabpIsFckrJsQ_I/edit?tab=t.2w7vbphf7en7).

### What is the migration?

Moving artifacts management (compose RPMs and images) from S3 + custom web servers to Pulp instances for both upstream and downstream builds. Currently in dual-upload phase: artifacts go to both S3 and Pulp, with S3 to be phased out later.

### Main benefits of migrating to Pulp

1. **Faster promotions** — Pulp references packages rather than copying them across the network. rsync is inefficient for directories with many small files; Pulp eliminates this bottleneck.
2. **Native OCI container support** — Pulp handles OCI containers natively, removing the need for separate container registry tooling.
3. **Eliminates custom web servers** — No need to maintain bespoke web server infrastructure for artifact serving.
4. **Reduces S3 dependency and costs** — Moves away from external S3 storage, cutting costs and reducing external dependencies.
5. **Faster uploads observed** — During testing, uploading compose data (including arch-specific RPMs) to Pulp stage was faster than the existing web server method.

### Technical implementation details

- Pulp CLI can't reach internal network for downstream — using Pulp Python libraries for uploads within each job instead.
- Changes in `pack-jobs` and `create-os-build` repos to enable dual-upload.
- Pipeline checks if Pulp is enabled before uploading.
- Product build promotion copies artifacts to public auto-sd stage once pipelines finish.
- Smoke tests and promotion logic still being finalized.

### Transition strategy

- Dual-upload (S3 + Pulp) during transition to avoid breaking dependencies.
- Existing URLs must be preserved — tools like test console and Polarium depend on them.
- Team will identify all URL/command references before cutting over.
- No rushed timeline — taking necessary time to avoid disruption (Juanje).

### Next steps (from demo)

- Ozan: summarize Pulp migration changes for review.
- Ozan: compare S3 vs Pulp upload durations once migration is functional.
- Ozan: add upload performance metrics to job logs.

### Key people (Pulp migration)

- **Ozan Unsal** — pipeline implementation, Pulp upload integration
- **Juanje Ojeda** — architecture decisions, rationale
- **Hubert Stefanski** — OCI/infrastructure context
- **Roni Eliezer** — URL consistency concerns

## Notes

<!-- Add progress, decisions, and blockers here -->
