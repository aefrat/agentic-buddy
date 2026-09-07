---
last_accessed: 2026-09-07
access_count: 1
created: 2026-09-07
---

# Codex Support: Architecture Diagram

Visual breakdown of the proposed multi-agent support architecture.

## Current State (Claude Code Only)

```
┌─────────────────────────────────────────┐
│         Claude Code / Cursor            │
│      (or any other AI agent)            │
└─────────────────────────────────────────┘
                    │
                    ▼
         ┌──────────────────┐
         │    CLAUDE.md     │
         │  (Configuration) │
         └──────────────────┘
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
    ┌──────────┐         ┌──────────┐
    │  Hooks   │         │ Commands │
    │(auto-*)  │         │(/daily)  │
    └──────────┘         └──────────┘
         │                    │
         └────────┬───────────┘
                  ▼
         ┌──────────────────┐
         │ agent_brain/     │
         │ logs/            │
         │ user/            │
         └──────────────────┘
```

## Proposed State (Multi-Agent Support)

```
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│   Claude Code    │   │     Cursor       │   │  OpenAI Codex    │
│  (Vertex AI)     │   │  (GitHub CoPilot)│   │   (OpenAI API)   │
└──────────────────┘   └──────────────────┘   └──────────────────┘
         │                    │                         │
         ▼                    ▼                         ▼
    ┌──────────────┐    ┌──────────────┐      ┌──────────────┐
    │  CLAUDE.md   │    │  CLAUDE.md   │      │ AGENTS.md    │
    │   (primary)  │    │  (secondary) │      │ (mirrored)   │
    └──────────────┘    └──────────────┘      └──────────────┘
         │                    │                         │
         │     (synced via pre-commit hook)             │
         │                    │                         │
         └────────┬───────────┴─────────────────────────┘
                  │
         ┌────────┴──────────────┐
         ▼                       ▼
   ┌──────────────────┐  ┌──────────────────┐
   │  Hooks (in       │  │  Commands        │
   │  .cursor/hooks)  │  │  (.claude/cmd)   │
   │                  │  │  (.cursor/cmd)   │
   │  with backend    │  │  (/setup)        │
   │  detection       │  │  (/daily)        │
   └──────────────────┘  └──────────────────┘
         │ (auto-detects     │
         │  which CLI is     │
         │  available)       │
         │                   │
    ┌────┴───────────┐       │
    ▼                ▼       ▼
┌─────────┐   ┌─────────┐
│ claude  │   │ codex   │
│ (CLI)   │   │ (CLI)   │
└─────────┘   └─────────┘
    │              │
    └──────┬───────┘
           ▼
   ┌──────────────────┐
   │ agent_brain/     │
   │ logs/            │
   │ user/            │
   │ .agent-config.json
   └──────────────────┘
```

## File Synchronization Flow

```
User edits CLAUDE.md
         │
         ▼
   ┌──────────────────┐
   │  git add         │
   │  CLAUDE.md       │
   └──────────────────┘
         │
         ▼
   ┌──────────────────────────────┐
   │  .git/hooks/pre-commit runs  │
   │  (before commit)             │
   └──────────────────────────────┘
         │
         ▼
   ┌──────────────────────────────┐
   │  Pre-commit hook checks:     │
   │  - Does AGENTS.md exist?     │
   │  - Is AGENTS.md in sync?     │
   └──────────────────────────────┘
         │
    ┌────┴─────────────────────────┐
    │                              │
   (no)                          (yes)
    │                              │
    ▼                              ▼
cp CLAUDE.md AGENTS.md         Skip
git add AGENTS.md              (already in sync)
    │                              │
    └────────────────┬─────────────┘
                     ▼
              ┌──────────────────┐
              │  git commit      │
              │ Both files now   │
              │ in same commit   │
              └──────────────────┘
```

## Hook Execution with Backend Detection

```
IDE launches session
        │
        ▼
  ┌──────────────────────────────┐
  │  Hook triggers               │
  │  (sessionStart,              │
  │   afterAgentResponse,        │
  │   sessionEnd)                │
  └──────────────────────────────┘
        │
        ▼
  ┌──────────────────────────────┐
  │  session-start.py runs       │
  │  (or auto-reflect.py, etc)   │
  └──────────────────────────────┘
        │
        ▼
  ┌──────────────────────────────┐
  │  backend.py:                 │
  │  detect_backend()            │
  │  - Check CURSOR_PROJECT_DIR? │
  │  - Check CLAUDE_PROJECT_DIR? │
  │  - Check CODEX_PROJECT_DIR?  │
  │  - Fallback: which claude?   │
  │           which codex?       │
  └──────────────────────────────┘
        │
   ┌────┼────┬────────┐
   │    │    │        │
  claude cursor codex  (none)
   │    │    │        │
   ▼    ▼    ▼        ▼
  CLI  CLI  CLI     Error
  invocation invocation invocation
   │    │    │
   │    └────┼────────┐
   │         │        │
   ▼         ▼        ▼
claude -p   codex    Warn user
skill:X   agent:X   "Install codex"
   │         │
   └────┬────┘
        ▼
  Background agent
  spawns, runs skill,
  updates brain files
```

## Configuration Loading Priority

**Claude Code:**
```
1. Load .claude/settings.json (Claude Code native)
2. Load CLAUDE.md (project rules)
3. Load .claude/commands/ (slash commands)
4. Hooks in .claude/settings.json invoke backend-aware scripts
```

**Cursor:**
```
1. Load .cursor/hooks.json (Cursor native)
2. Load CLAUDE.md (project rules) ← primary
3. Load AGENTS.md (project rules) ← secondary (kept in sync)
4. Load .cursor/commands/ (slash commands)
5. Hooks in .cursor/hooks.json invoke backend-aware scripts
```

**Codex:**
```
1. Load .codex/hooks.json (Codex native, if supported)
2. Load AGENTS.md (project rules)
3. Hooks invoke backend-aware scripts that find 'codex' CLI
```

## Backend Detection Decision Tree

```
┌─ Is CURSOR_PROJECT_DIR set?
│  ├─ YES → backend = "cursor"
│  └─ NO ─┐
│         ├─ Is CLAUDE_PROJECT_DIR set?
│         │  ├─ YES → backend = "claude"
│         │  └─ NO ─┐
│         │         ├─ Is CODEX_PROJECT_DIR set?
│         │         │  ├─ YES → backend = "codex"
│         │         │  └─ NO ─┐
│         │         │         ├─ which claude?
│         │         │         │  ├─ Found → backend = "claude"
│         │         │         │  └─ Not found ─┐
│         │         │         │                ├─ which codex?
│         │         │         │                │  ├─ Found → backend = "codex"
│         │         │         │                │  └─ Not found
│         │         │         │                │
│         │         │         │                └─ backend = None (error)
```

## Skill Invocation (Before → After)

**Before (Claude Code only):**
```python
# Hook wants to run a skill
subprocess.run(["claude", "-p", "skill:auto-reflect"])
```

**After (Multi-agent support):**
```python
# Hook detects backend, uses appropriate CLI
backend = detect_backend()  # Returns "claude", "codex", or "cursor"

if backend == "codex":
    subprocess.run(["codex", "agent", "skill:auto-reflect"])
else:  # claude or cursor
    subprocess.run(["claude", "-p", "skill:auto-reflect"])
```

## .agent-config.json Role

```
┌──────────────────────────────────────┐
│     .agent-config.json               │
│  (Human-readable documentation)      │
├──────────────────────────────────────┤
│ backends:                            │
│   - claude_code: enabled, Claude CLI │
│   - cursor: enabled, Cursor CLI      │
│   - codex: enabled, Codex CLI        │
├──────────────────────────────────────┤
│ file_sync:                           │
│   - strategy: claude_to_agents       │
│   - description: ...                 │
├──────────────────────────────────────┤
│ hook_backend_priority:               │
│   - [ "claude", "codex" ]            │
└──────────────────────────────────────┘
         │
         ├─ For humans: clarify what's supported
         │
         └─ For tools: guide backend selection
            if multiple CLIs available
```

## Data Flow: User Request → Brain Update

```
┌──────────────────────────────┐
│ User says "/daily"           │
│ (in Claude Code, Cursor,     │
│  or Codex)                   │
└──────────────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Slash command routed to:     │
│ - .claude/commands/daily     │
│ - .cursor/commands/daily     │
│ (symlinks to same script)    │
└──────────────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Agent reads config:          │
│ - CLAUDE.md (Claude/Cursor)  │
│ - AGENTS.md (Codex)          │
│ (both in sync, identical)    │
└──────────────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Agent runs /daily skill      │
│ (via backend.py)             │
│ - Reads logs/                │
│ - Consolidates              │
│ - Writes observations.md     │
│ - Updates CLAUDE.md or       │
│   AGENTS.md (whichever is    │
│   config for this backend)   │
└──────────────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Changes committed to git     │
│ Pre-commit hook syncs        │
│ CLAUDE.md ↔ AGENTS.md        │
└──────────────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Both files up-to-date,       │
│ ready for next session       │
│ regardless of backend        │
└──────────────────────────────┘
```

## Migration Path for Existing Users

```
Current Claude Code User
        │
        ├─ No action needed
        │  (CLAUDE.md still works)
        │
        ├─ Optional: upgrade when ready
        │
        └─→ Add Codex support
            - Create AGENTS.md (copy of CLAUDE.md)
            - Add pre-commit hook
            - Update hooks to use backend.py
            - Done!
              (No breaking changes)
```

## Backward Compatibility Matrix

```
┌────────────┬─────────────────────┬──────────────────────────────┐
│  Backend   │ Primary Config File │ Read Behavior                │
├────────────┼─────────────────────┼──────────────────────────────┤
│ Claude     │ CLAUDE.md           │ Reads only CLAUDE.md         │
│ Code       │                     │ (works, no AGENTS.md needed) │
├────────────┼─────────────────────┼──────────────────────────────┤
│ Cursor     │ CLAUDE.md           │ Reads both CLAUDE.md and     │
│            │ (AGENTS.md synced)  │ AGENTS.md (no duplication    │
│            │                     │ since in sync)               │
├────────────┼─────────────────────┼──────────────────────────────┤
│ Codex      │ AGENTS.md           │ Reads only AGENTS.md         │
│            │ (synced from        │ (works because synced)       │
│            │  CLAUDE.md)         │                              │
└────────────┴─────────────────────┴──────────────────────────────┘
```

Key insight: **Even if AGENTS.md doesn't exist initially (old setups),
the hooks and skills can still work for Claude Code and Cursor.
AGENTS.md is only required for Codex users. The pre-commit hook
ensures it stays in sync once created.**
