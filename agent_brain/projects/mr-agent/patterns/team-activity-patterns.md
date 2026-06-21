---
last_accessed: 2026-06-21
access_count: 1
created: 2026-06-21
---

# Team Activity Patterns

Cross-week baselines and recurring patterns derived from accumulated report history. Consolidation only — updated after runs, never during generation.

## How this file is populated

After each report run (step 9 of the skill), check `computed/week-over-week.json` for:
- Members whose activity is consistently above or below team average → update baseline
- Seasonal shifts (e.g., release week spikes, holiday drops) → note the pattern
- New members ramping up → track trajectory

Only update with patterns that have been observed across 3+ reports. Single-week deviations are not patterns.

## Team baselines

_Updated as history accumulates. Format: member, typical weekly range, notes._

### ATC — Auto ToolChain

| Member | Typical closed/week | Typical MRs/week | Notes |
|--------|--------------------:|------------------:|-------|
| _to be populated_ | — | — | — |

### PitCrew — RHAS

| Member | Typical closed/week | Typical PRs/week | Notes |
|--------|--------------------:|------------------:|-------|
| _to be populated_ | — | — | — |

## Seasonal patterns

_Recurring patterns tied to the release cycle or calendar:_
- _e.g., "Week before RC: blocker fix spike, feature work drops"_
- _e.g., "Post-release week: low ticket velocity, high review activity"_

## Slack patterns

_Communication rhythms:_
- _e.g., "ATC Slack peaks Mon-Tue, drops Thu-Fri"_
- _e.g., "alerts-auto-toolchain is quiet most weeks; spikes correlate with CI breakage"_

## Member trajectories

_Onboarding and growth signals:_
- Roderick Kieley: joined 2026-06-01, PitCrew. Track first MR, first ticket closure, Slack ramp.
- Matt Goldman: joined 2026-04-13, ATC. Track velocity stabilization.
