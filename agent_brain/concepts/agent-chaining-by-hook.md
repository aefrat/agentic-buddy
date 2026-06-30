---
last_accessed: 2026-06-30
access_count: 1
created: 2026-06-30
---

# Agent chaining by hook

Embedding one agent's trigger inside another agent's procedure (typically
as a "step 8b" or similar post-processing step). The triggering agent
does not know about the chained agent's internals - it just invokes.

## Pattern

1. Agent A completes its primary procedure.
2. A final step in Agent A calls Agent B by trigger (skill invocation,
   not direct function call).
3. Agent B runs independently with its own identity, memory, and success
   criteria.
4. Both agents remain independently testable and modifiable.

## Instances

- **Project Pulse as step 8b of manager report** (2026-06-23): manager
  report gathers Slack data; project-pulse cross-references findings
  against project files.
- **PitCrew report step 8b pattern** (2026-06-29): same hook-based
  integration approach in the PitCrew weekly report skill.
- **AI Methodology daily capture as step 8b of daily consolidation**
  (2026-06-29): daily cycle runs its own steps; methodology capture
  classifies tasks from the day's log independently.

## Design advantages

- **Composability:** agents can be added or removed from chains without
  rewriting the parent procedure.
- **Independent testing:** each agent works standalone; the chain is an
  integration convenience.
- **Failure isolation:** if the chained agent fails, the parent's output
  is still valid.

## Contrast

Different from monolithic multi-phase agents where all logic lives in one
skill file. Chaining keeps agent boundaries clean - each agent owns its
own identity, memory stores, and success criteria.

Source: logs/2026-06-23.md, logs/2026-06-29.md (sessions 11)
