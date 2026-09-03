---
last_accessed: 2026-09-03
access_count: 1
created: 2026-07-22
---

# Source authority hierarchy

For any factual question, there is a hierarchy of data sources where the most
authoritative one is often not the most obvious one. The principle: prefer the
source closest to runtime behavior or richest synthesis over the source closest
to human readability.

**Primary/runtime sources** (config files, CI YAML, policy files, code) contain
actual rules and behavior. **Secondary/documentary sources** (wikis, READMEs,
Confluence pages) describe frameworks and intent but may lag reality. For
assessments, the richest available synthesis (narrative reports) outranks raw
data (ticket counts, API output).

## When to apply

- Looking up how a system actually behaves: read CI config, not the wiki
- Checking permissions or policy: read the policy file, not the documentation
- Generating assessments from multiple data sources: use the richest synthesis
- Debugging a discrepancy between "how it should work" and "how it works"

## Specific instances

- CI pipeline YAML as architecture source (2026-06-11): `.gitlab-ci.yml` and
  stage includes reveal independent trigger mechanisms that wikis and DETAILED.md
  docs omit. Gator's command orchestration was fully answered by reading
  `.gitlab/rules.yml`.
- Brew hub_policy.conf as permissions source (2026-06-14): the raw policy file
  has product-specific rules (RHIVOS tagger, pkglist, auto-toolchain); Confluence
  wikis describe the general permission model only.
- Upstream vs downstream CI boundary (2026-06-22): documentation covers what you
  own and consume, but dependencies' CI is their concern. Go to the upstream
  source directly.
- Data source hierarchy for assessments (2026-06-29): QC draft reports (narrative
  synthesis) > collected-data files (raw stats) > raw API output for evaluation
  quality.
- Source authority over mapping tables (2026-08-02): use the authoritative Jira
  custom field (`customfield_10606` AssignedTeam) directly instead of a
  locally-maintained component-to-team YAML that drifts and needs manual upkeep.
- Live source over duplicated config, with explicit gaps (2026-09-03): drive a
  displayed value from the authoritative external system (Jira fixVersion
  `releaseDate`) rather than a hand-copied config field that drifts (the
  release-blocker Core/FuSa split had one stale date duplicated onto both
  tracks). When the source is empty, render the gap explicitly ("Not set in
  Jira") — never fall back silently to a plausible-but-stale value. A visible gap
  prompts a fix; a silent fallback hides one.
