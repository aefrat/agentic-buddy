---
last_accessed: 2026-06-18
access_count: 1
created: 2026-06-18
---

# Cross-referencing Slack vs documented processes

## Pattern

Comparing what people actually do (observed in Slack conversations and threads) against what's formally documented (wikis, repos, Confluence) reveals process gaps that are invisible from either source alone.

Slack shows ad-hoc behavior, workarounds, and who's actually doing the work. Documentation shows the intended process. The delta between them is where gaps, missing automation, and undocumented responsibilities live.

## When to apply

- When investigating process failures or bottlenecks
- When auditing documentation completeness
- When a user reports that "nobody knows who does X"

## Instances

1. **RHIVOS tagging ownership gap (2026-06-11):** Slack showed Francisco/Ozan doing manual tagging; wiki showed Gator handles promotion automatically. Gap: nobody documented who tags packages INTO `-gate` before Gator picks them up.

2. **Full documentation audit (2026-06-14):** 3-repo audit + Confluence deep dive. Eric Chanudet's Slack escalation revealed 6 undocumented gaps — all invisible from repo documentation alone.

3. **Cross-documentation-layer confirmation (2026-06-14):** Pattern works across documentation layers too: git repos + Confluence + Slack + brew-confs policy files. The "RHEL & RHIVOS gating process" Confluence page acknowledged manual tagging during blocker phase but assigned no owner — confirming repo-level findings.

## Extension: check for missing automation

When a process gap is found, check whether the upstream/parent product (e.g. RHEL) has automation that makes the process self-documenting. If the downstream product (e.g. RHIVOS) lacks that automation, the gap is structural — not just a documentation oversight.

> Source: [Log 2026-06-11](../../logs/2026-06-11.md), [Log 2026-06-14](../../logs/2026-06-14.md), [RHIVOS RC3 project](../projects/RHIVOS_2_0_release_RC3.md)
