---
last_accessed: 2026-05-21
access_count: 1
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

- Where does the wiki source live? → pipe-x namespace seems like the right call per Juanje
- Where does the mkdocs site get deployed? → GitLab Pages / domain / S3 (not yet decided)
- How often does the wiki get regenerated from repos? (maintenance cadence not yet defined)

## Notes

<!-- Add progress, decisions, and blockers here -->
