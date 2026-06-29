---
last_accessed: 2026-06-29
access_count: 0
created: 2026-06-29
---

# AI Methodology Agent - Knowledge Base

Evidence base for AI workflow methodology. Tracks which engineering
management tasks AI handles well, which need human judgment, and why.
Builds incrementally through daily captures; produces shareable briefs
for team, program, or manager audiences.

Read this index first, then navigate to the relevant store.

## Stores

- `reference/` - Task taxonomy, domain definitions, brief template,
  evidence source documentation. **Read-only.** Read when classifying
  tasks or generating briefs.
- `active/` - Running daily observations, structured tallies ledger,
  and latest brief. **Append/overwrite per run.** Read when doing daily
  capture or starting a synthesis.
- `history/` - Past briefs, dated. **Immutable after save.** Read when
  comparing methodology evolution over time.
- `patterns/` - Accumulated learnings: what works, what needs humans,
  what fails, what is ready for team adoption. **Consolidation only.**
  Read when generating briefs or preparing team recommendations.
- `computed/` - Script-derived statistics. **Script-only, never
  LLM-written.** Read when grounding briefs with quantitative data.

## Skill

- [ai-methodology.md](../../skills/ai-methodology.md) - The skill procedure.

## Data flow

```
Daily:  session logs -> classify tasks -> daily-observations.md + running-tallies.md
Weekly: running-tallies.md -> compute_stats.py -> period-stats.json -> brief
Monthly: same as weekly but 30-day window, deeper pattern analysis
```
