---
last_accessed: 2026-09-07
access_count: 1
created: 2026-09-07
---

# OpenAI Codex Support Extension

**Status:** Planning phase — design proposal for extending agentic-buddy to support OpenAI Codex alongside Claude Code (Vertex AI).

**Context:** Juanje Ojeda's suggestion from Slack (Sep 7) — agentic-buddy needs changes to support Codex as a backend alongside the current Vertex AI setup. He noted: "You need basically to change the hooks to support triggering codex in background for the background tasks and also renaming the CLAUDE.md to AGENTS.md."

## Problem

Currently, agentic-buddy is built exclusively for Claude Code / Vertex AI:
- `CLAUDE.md` is the single configuration entry point (loaded natively by Claude Code)
- Hooks trigger background agents via Python scripts that assume Claude Code is available
- Codex doesn't read `CLAUDE.md` — it reads `AGENTS.md` instead
- Cursor has compatibility with both `CLAUDE.md` and `AGENTS.md`, leading to duplicate loading if both exist

## Design Goals

1. **Support multiple backends:** Claude Code (Vertex AI), Codex (OpenAI), Cursor (both)
2. **No breaking changes:** Existing Claude Code users continue working without modification
3. **Single source of truth:** No content duplication across `CLAUDE.md` and `AGENTS.md`
4. **Flexible hook execution:** Background agents can be triggered via either backend
5. **Progressive adoption:** Users can opt into Codex support; existing setups remain unchanged

## Proposed Solution

### 1. Configuration Strategy: Symlink or Dual-File Pattern

**Option A: Symlink (Juanje's initial approach)**
- `AGENTS.md` is the primary file (canonical configuration)
- `CLAUDE.md` → `AGENTS.md` (symlink)
- Pros: Single source of truth
- Cons: Git may not track symlinks well; some tools don't follow symlinks; Codex/Cursor needs to read from `AGENTS.md` path explicitly

**Option B: Dual-file with CI sync (recommended for this project)**
- `CLAUDE.md` is the primary file
- `AGENTS.md` is a generated copy, kept in sync via git hook or CI automation
- Pros: Both files are real files (no symlink issues), clear primary source
- Cons: Requires maintenance (pre-commit hook or manual sync)

**Option C: Runtime fallback**
- Codex uses `AGENTS.md`; Claude Code uses `CLAUDE.md`
- Both files exist independently, but hooks sync them automatically at each invocation
- Pros: Flexible, each tool reads its preferred file
- Cons: Duplication risk if out of sync

**Recommendation:** Start with **Option B** — `CLAUDE.md` is primary, `AGENTS.md` is kept in sync via a pre-commit hook. This requires minimal changes, avoids symlink fragility, and works with Git.

### 2. Hook Execution Strategy

**Current state:**
```python
# .cursor/hooks/session-start.py
# Runs via .cursor/hooks.json (Cursor) or .claude/settings.json (Claude Code)
# Assumes Claude Code CLI (`claude`) is available for background agents
```

**Goal:** Hooks should detect which backend is active and spawn the appropriate background agent.

**Implementation:**
1. **Detect the calling environment:**
   - If `CURSOR_PROJECT_DIR` is set → running in Cursor
   - If `CLAUDE_PROJECT_DIR` is set → running in Claude Code
   - If `CODEX_PROJECT_DIR` or similar → running in Codex (TBD — Codex hook format)
   - Fallback: check if `claude` CLI is available; if not, try `codex` CLI

2. **Spawn background agents conditionally:**
   ```python
   def get_agent_command(agent_type: str) -> List[str]:
       """Return CLI command for the detected backend."""
       if has_claude_cli():
           return ["claude", "-p", f"<skill:{agent_type}>"]
       elif has_codex_cli():
           return ["codex", "agent", f"<skill:{agent_type}>"]
       else:
           raise RuntimeError("No supported AI agent CLI found")
   ```

3. **Codex hook integration:** Create `.codex/hooks.json` (mirror of `.cursor/hooks.json`) configured for Codex's hook system. Codex likely has a similar hook system; verify Codex documentation.

**Files to create/modify:**
- `agent_brain/skills/` → add new skill `_backend-detection.md` for the pattern
- `.cursor/hooks/session-start.py` → add backend detection
- `.cursor/hooks/auto-reflect.py` → add backend detection
- `.cursor/hooks/auto-consolidate.py` → add backend detection
- `.codex/hooks.json` → mirror of `.cursor/hooks.json` (if Codex supports hooks)
- `.claude/settings.json` → add Codex CLI path as optional fallback

### 3. File Synchronization Strategy

**Option B implementation:**

Create a **pre-commit hook** that syncs `AGENTS.md` from `CLAUDE.md` before commits:

```bash
#!/bin/bash
# .git/hooks/pre-commit

if [ -f CLAUDE.md ] && [ ! -f AGENTS.md ]; then
    cp CLAUDE.md AGENTS.md
    git add AGENTS.md
elif [ -f CLAUDE.md ]; then
    if ! cmp -s CLAUDE.md AGENTS.md; then
        cp CLAUDE.md AGENTS.md
        git add AGENTS.md
    fi
fi
```

**Alternative:** Include the sync in a skill or manual command (less automatic but more transparent):
```
/sync-agents-files  — keeps CLAUDE.md and AGENTS.md in sync
```

### 4. Project-Level Configuration

Add a new file `.agent-config.json` to track which backends are enabled:

```json
{
  "backends": {
    "claude_code": {
      "enabled": true,
      "cli_path": "claude",
      "config_file": "CLAUDE.md"
    },
    "cursor": {
      "enabled": true,
      "cli_path": "cursor",
      "config_file": "CLAUDE.md"
    },
    "codex": {
      "enabled": false,
      "cli_path": "codex",
      "config_file": "AGENTS.md"
    }
  },
  "hook_backend_priority": ["claude", "codex"],
  "sync_strategy": "claude_to_agents"
}
```

This allows:
- Users to enable/disable backends per project
- Explicit priority if multiple CLIs are available
- Clear documentation of which file each backend reads

### 5. Skill Changes

**Skills referencing CLAUDE.md need updates:**

Current pattern:
```markdown
## How to use
Use when the user asks you to run the daily report. The agent reads from CLAUDE.md...
```

Updated pattern:
```markdown
## How to use
Use when the user asks you to run the daily report. The agent reads from CLAUDE.md (Claude Code) or AGENTS.md (Codex)...
```

Files affected:
- Any skill that mentions CLAUDE.md in documentation (no functional change needed)
- Look for grep: `grep -r "CLAUDE\.md" agent_brain/skills/ docs/`

### 6. Documentation Changes

**README.md updates:**
- Add new "Multi-Agent Support" section explaining Cursor, Claude Code, and Codex compatibility
- Document the `AGENTS.md` symlink/sync strategy
- Add troubleshooting: "My Codex isn't seeing configuration" → check `AGENTS.md` exists

**CLAUDE.md updates:**
- Clarify that the file is loaded by Claude Code; Codex users read `AGENTS.md` instead
- Add note about synchronization

### 7. Implementation Phases

**Phase 1: File Setup (non-breaking)**
- Create `AGENTS.md` as copy of `CLAUDE.md`
- Add git pre-commit hook for sync
- Update README with multi-backend support note
- No functional changes; both files exist, sync maintained

**Phase 2: Hook Detection (opt-in)**
- Modify `.cursor/hooks/session-start.py` to detect backend
- Modify hook spawn logic to use appropriate CLI
- Create `.codex/hooks.json` (if Codex supports hooks)
- Add `.agent-config.json` with backend configuration

**Phase 3: Codex-Specific Tuning (optional)**
- If Codex has limitations (no hook support, different skill syntax), create Codex-specific versions of problematic skills
- Update skill documentation with Codex-specific notes

**Phase 4: Documentation & Examples**
- Add example `.agent-config.json` with different scenarios
- Create setup guide for Codex users
- Add Codex troubleshooting section

## Open Questions

1. **Does Codex have hook support?** Need to verify Codex documentation for session-start, session-end, and periodic hooks.

2. **What is Codex's file discovery?** Does it read `.codex/` directory? Or does config live elsewhere?

3. **Codex CLI availability:** Is `codex` installed as a CLI? How do background agents invoke it?

4. **Skill syntax differences:** Are there any skill syntax differences between how Claude Code and Codex parse instructions?

5. **Hook invocation timing:** Does Codex trigger hooks at the same lifecycle points (session start, session end, periodic)?

## Success Criteria

- [x] Existing Claude Code users unaffected
- [ ] Codex users can add agentic-buddy to their workspace and have it work without modification
- [ ] Both `CLAUDE.md` and `AGENTS.md` stay synchronized
- [ ] Background agents (auto-reflect, auto-consolidate) work in both environments
- [ ] Documentation clearly explains multi-backend support
- [ ] Setup flow (`/setup`) can detect and configure for either backend

## References

- **Slack discussion:** https://redhat-internal.slack.com/archives/D04RWM2D1M2/p1788362668606279
- **Juanje's note:** "I had the CLAUDE.md as symlink to AGENTS.md at first. The reason I changed it was because Cursor support both files and it was loading both to the context, but I don't think codex load CLAUDE.md"
- **Related:** [[agent-forge-design-principles.md]] — principles for progressive disclosure and file-based navigation apply here
