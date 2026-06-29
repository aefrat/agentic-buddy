---
last_accessed: 2026-06-29
access_count: 0
created: 2026-06-29
---

# Anti-Patterns

Recurring AI failures, limitations, and mistakes. Updated during
weekly/monthly synthesis when an anti-pattern appears 3+ times.

Distinguishes between:
- **AI failure:** output was wrong, fabricated, or misleading
- **Design gap:** the workflow did not account for a known AI limitation
- **Boundary violation:** AI attempted something outside its competence

Format per entry:
```
## [Anti-pattern name]

**Type:** [failure|design-gap|boundary-violation]
**Domain:** [domain]
**First observed:** YYYY-MM-DD
**Instances:** N
**What happened:** [specific examples with evidence]
**How it was caught:** [human review, disconfirmation gate, user correction]
**Root cause:** [why the AI fails at this]
**Mitigation:** [what to do about it - guardrails, human-in-loop, avoid]
```

---

