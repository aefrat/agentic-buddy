---
last_accessed: 2026-06-29
access_count: 0
created: 2026-06-29
---

# Evidence Sources

Where the methodology agent finds evidence for task classification.
Read this to understand what data is available and how to interpret it.

## Primary sources

### Session logs (`logs/YYYY-MM-DD.md`)

The richest evidence source. Each daily log contains:
- **Context:** what the user was working on, situational observations
- **Decisions:** choices made and reasoning
- **Tasks captured:** items routed to user/ or agent_brain/
- **Lessons:** things learned during the session
- **System observations:** skill candidates, rule candidates, patterns

Classification signals: look for explicit user corrections (anti-pattern),
output accepted without changes (autonomous signal), multiple iteration
cycles (assisted signal), user driving with AI helping (enhanced signal).

### Agent active stores

Check which agent skills ran and their outputs:
- `agent_brain/projects/mr-agent/active/` - manager report runs
- `agent_brain/projects/pitcrew-agent/active/` - PitCrew report runs
- `agent_brain/projects/lp-status-agent/active/` - LP status runs
- `agent_brain/projects/qc-agent/active/` - QC report runs
- `agent_brain/projects/core-rpms-redux-agent/active/` - Core RPMs runs

Cron-triggered runs are autonomous by definition but verify: did the user
review the output? Check if the log mentions reviewing it.

### AI sessions registry (`user/ai-sessions.md`)

Lists Claude and other AI tool sessions by working directory and date.
Cross-reference with logs to understand what tools were used.

### Git history

Commits show AI-assisted work patterns. Look for:
- Commit messages indicating AI involvement (report:, daily:, weekly:)
- Frequency of commits (high frequency = AI-assisted workflow)
- Files modified (agent_brain/ = tool building, user/ = content production)

## Secondary sources

### Observations journal (`agent_brain/observations.md`)

System learning signals. Not direct evidence for task classification,
but useful for detecting patterns over time (e.g., repeated corrections
indicate an anti-pattern trend).

### Reflect outputs (in daily logs)

The reflect skill captures learning observations at session end. These
are already in the daily logs but worth noting as a distinct signal:
when the reflect skill itself detects skill candidates or rule
candidates, those are meta-evidence of AI-assisted process improvement.

## Interpretation guidelines

- Absence of a log entry does not mean work did not happen. Human-only
  tasks (1:1s, meetings) often leave no trace in session logs.
- Cron runs without subsequent log mentions may mean: (a) the user
  reviewed and accepted silently, or (b) the user did not review at all.
  Classify as autonomous but note the ambiguity.
- Multiple sessions on the same day should be treated as separate task
  sources. Each may contain different categories of work.
