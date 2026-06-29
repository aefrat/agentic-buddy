---
last_accessed: 2026-06-29
access_count: 0
created: 2026-06-29
---

# AI Methodology Brief Template

This template defines the structure for the shareable brief produced
during weekly and monthly synthesis. The brief is designed to be
copy-pasted into an email, Google Doc, or Slack post. It must read as
a professional methodology document, not an AI status report.

## Template

```markdown
# AI Methodology Brief - [Period: Week of YYYY-MM-DD | Month YYYY-MM]

## Summary

[3-5 sentences: what this period showed about AI's role in engineering
management work. Grounded in evidence, not aspiration. Written in first
person as the practitioner documenting methodology.]

## Distribution of AI Involvement

[Table from computed stats - NEVER LLM-generated numbers]

| Category | Count | % of Total | Trend vs Previous |
|----------|-------|------------|-------------------|
| Autonomous | N | NN% | +/-N% |
| Assisted | N | NN% | +/-N% |
| Enhanced | N | NN% | +/-N% |
| Human-Only | N | NN% | +/-N% |

## What AI Handles Well (Evidence-Backed)

[2-4 patterns with specific examples from the period]

1. **[Pattern name]** - [description with evidence from specific tasks]
2. **[Pattern name]** - [description with evidence]

## Where Human Judgment is Essential

[2-4 patterns where the evidence shows AI falls short]

1. **[Pattern name]** - [what happened, why human judgment was needed]
2. **[Pattern name]** - [what happened]

## Anti-Patterns and Lessons

[1-3 things that went wrong and what was learned]

1. **[Anti-pattern]** - [what happened, how it was caught, what to
   watch for]

## Recommendations for Team Adoption

[2-3 specific, actionable recommendations based on evidence]

1. **[Task/domain] is ready for broader adoption** - [evidence,
   suggested approach]
2. **[Task/domain] needs a human-in-the-loop** - [evidence, why]

## Methodology Notes

- Evidence period: [dates]
- Sessions analyzed: [N]
- Tasks classified: [N]
- Data sources: session logs, agent outputs, git history
- Statistics computed by: compute_stats.py (deterministic, not
  AI-generated)
```

## Writing guidelines

- Professional engineering practitioner tone. Write as someone
  documenting their methodology, not as an AI describing itself.
- Every claim traces to evidence. "The daily manager report ran
  autonomously 18 of 20 days" not "AI handles reporting well."
- No AI-tell characters: plain hyphens (-), straight quotes, simple
  punctuation. No em-dashes, curly quotes, or typographic characters.
- Recommendations must be actionable. "The LP status report pattern
  could be replicated for [specific team process]" not "AI can help
  with reporting."
- When a domain has no observations, note the gap explicitly. Absence
  of evidence is not evidence of absence.
