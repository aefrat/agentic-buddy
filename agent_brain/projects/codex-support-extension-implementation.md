---
last_accessed: 2026-09-07
access_count: 1
created: 2026-09-07
---

# Codex Support Implementation Guide

A step-by-step guide to add OpenAI Codex support to agentic-buddy without breaking existing Claude Code usage.

## Strategy Overview

The core insight from Juanje:
- Codex reads `AGENTS.md`, not `CLAUDE.md`
- Cursor reads both, causing duplication if both exist independently
- Solution: Keep `CLAUDE.md` as primary, sync to `AGENTS.md` automatically

This guide implements a **dual-file sync strategy** with **automatic backend detection** in hooks.

## Step 1: Create AGENTS.md (Sync Point)

**What:** Create `AGENTS.md` as a copy of `CLAUDE.md`. This will be the file Codex reads.

**Why:** Codex doesn't read `CLAUDE.md`. We maintain one primary file (`CLAUDE.md`) and automatically sync to `AGENTS.md` so both tools work.

**Files to create:**
- `AGENTS.md` ← copy of `CLAUDE.md`
- `.git/hooks/pre-commit` ← auto-sync before commits

**Implementation:**

```bash
# In the repo root:

# Step 1a: Copy CLAUDE.md to AGENTS.md
cp CLAUDE.md AGENTS.md

# Step 1b: Create pre-commit hook to keep them in sync
mkdir -p .git/hooks

cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Pre-commit hook: sync AGENTS.md from CLAUDE.md

CLAUDE_FILE="CLAUDE.md"
AGENTS_FILE="AGENTS.md"

if [ ! -f "$CLAUDE_FILE" ]; then
    exit 0
fi

# If AGENTS.md doesn't exist or differs from CLAUDE.md, sync it
if [ ! -f "$AGENTS_FILE" ] || ! cmp -s "$CLAUDE_FILE" "$AGENTS_FILE"; then
    cp "$CLAUDE_FILE" "$AGENTS_FILE"
    git add "$AGENTS_FILE"
    echo "Synced AGENTS.md from CLAUDE.md"
fi

exit 0
EOF

chmod +x .git/hooks/pre-commit

# Step 1c: Commit both files
git add AGENTS.md
git commit -m "feat: add AGENTS.md for Codex support (synced from CLAUDE.md)"
```

**What the user sees:**
- Both `CLAUDE.md` and `AGENTS.md` exist in the repo
- They're always in sync (pre-commit hook ensures this)
- Claude Code users continue using `CLAUDE.md`
- Codex users can now use `AGENTS.md`

## Step 2: Add Backend Detection to Hooks

**What:** Modify hook scripts to detect which AI agent is running them (Claude Code, Cursor, or Codex) and spawn background agents appropriately.

**Why:** Currently hooks assume Claude Code is available. We need to detect the environment and use the right CLI.

**Files to modify:**
- `.cursor/hooks/session-start.py`
- `.cursor/hooks/auto-reflect.py`
- `.cursor/hooks/auto-consolidate.py`

**Implementation:**

Create a helper module `.cursor/hooks/backend.py`:

```python
#!/usr/bin/env python3
"""
backend.py — Detect and invoke the correct AI agent backend.

Supports:
- Claude Code (claude CLI)
- Codex (codex CLI)
- Cursor (cursor CLI, but runs the same agent as Claude Code)
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import Optional, List


def detect_backend() -> Optional[str]:
    """
    Detect which AI agent backend is currently running.
    
    Returns: 'claude' | 'codex' | 'cursor' | None
    """
    # Environment variables set by each tool
    if os.environ.get("CURSOR_PROJECT_DIR"):
        return "cursor"
    if os.environ.get("CLAUDE_PROJECT_DIR"):
        return "claude"
    # Codex may use CODEX_PROJECT_DIR or similar — verify with Codex docs
    if os.environ.get("CODEX_PROJECT_DIR"):
        return "codex"
    
    # Fallback: check which CLI is available
    if has_cli("claude"):
        return "claude"
    if has_cli("codex"):
        return "codex"
    
    return None


def has_cli(cli_name: str) -> bool:
    """Check if a CLI tool is available in PATH."""
    try:
        subprocess.run(
            ["which", cli_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_agent_command(skill_name: str) -> List[str]:
    """
    Get the CLI command to spawn a background agent for the detected backend.
    
    Args:
        skill_name: Name of the skill to run (e.g., "process-conversation")
    
    Returns:
        CLI command as a list (e.g., ["claude", "-p", "skill:process-conversation"])
    
    Raises:
        RuntimeError: If no supported backend is available
    """
    backend = detect_backend()
    
    if backend == "codex":
        # Adjust if Codex CLI syntax differs
        return ["codex", "agent", f"skill:{skill_name}"]
    elif backend in ("claude", "cursor"):
        # Both Claude Code and Cursor use the same CLI
        return ["claude", "-p", f"skill:{skill_name}"]
    else:
        raise RuntimeError(
            "No supported AI agent backend detected. "
            "Please ensure Claude Code or Codex is installed."
        )


def spawn_background_agent(
    skill_name: str,
    cwd: Optional[Path] = None,
    timeout: int = 300,
) -> bool:
    """
    Spawn a background agent to run a skill.
    
    Args:
        skill_name: Name of the skill to run
        cwd: Working directory for the subprocess
        timeout: Max seconds to wait for completion
    
    Returns:
        True if successful, False if failed
    """
    try:
        cmd = get_agent_command(skill_name)
        subprocess.run(
            cmd,
            cwd=cwd,
            timeout=timeout,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,  # Don't raise on non-zero exit
        )
        return True
    except Exception as e:
        # Log but don't crash the hook
        print(f"Warning: Failed to spawn background agent: {e}", file=sys.stderr)
        return False
```

Then modify `session-start.py` to use it:

```python
# At the top of session-start.py, add:

import sys
from pathlib import Path

# Add .cursor/hooks to Python path
sys.path.insert(0, str(Path(__file__).parent))

from backend import detect_backend, spawn_background_agent

# ... rest of the function ...

def main() -> None:
    # ... existing code ...
    
    # After determining the output, spawn consolidation if needed
    backend = detect_backend()
    if backend and consolidation_needed:
        spawn_background_agent("auto-consolidate", cwd=workspace)
    
    # ... rest of main ...
```

Similarly update `auto-reflect.py` and `auto-consolidate.py` to use backend detection before spawning the next phase.

**What the user sees:**
- Hooks work the same whether Claude Code or Codex is running them
- Background agents spawn correctly for each backend
- No errors about missing CLI tools

## Step 3: Add Codex Configuration (Optional)

**What:** Create `.codex/hooks.json` as a mirror of `.cursor/hooks.json`, configured for Codex's hook system.

**Why:** If Codex has its own hook system and configuration format, it needs to know where the hooks live.

**Note:** This step requires verifying Codex's documentation. The format below is a guess based on Cursor's pattern.

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "command": "python3 .cursor/hooks/session-start.py"
      },
      {
        "command": "python3 .cursor/hooks/auto-consolidate.py"
      }
    ],
    "sessionEnd": [
      {
        "command": "python3 .cursor/hooks/auto-reflect.py"
      }
    ],
    "afterAgentResponse": [
      {
        "command": "python3 .cursor/hooks/auto-reflect.py"
      }
    ]
  }
}
```

**Or:** Add Codex hook config to `.claude/settings.json` if Claude Code supports reading Codex hooks from there.

## Step 4: Create Backend Configuration File

**What:** Add `.agent-config.json` to explicitly document which backends are supported and their status.

**Why:** Makes it clear which backends are enabled and which files each backend reads.

```json
{
  "project_name": "Agentic Buddy",
  "version": "1.0",
  "backends": {
    "claude_code": {
      "name": "Claude Code (Anthropic)",
      "enabled": true,
      "cli": "claude",
      "config_file": "CLAUDE.md",
      "hook_dir": ".claude/settings.json",
      "notes": "Default, fully supported. Uses Vertex AI backend."
    },
    "cursor": {
      "name": "Cursor (GitHub Copilot + VSCode)",
      "enabled": true,
      "cli": "cursor",
      "config_file": "CLAUDE.md",
      "hook_dir": ".cursor/hooks.json",
      "notes": "Reads both CLAUDE.md and AGENTS.md; we keep them in sync."
    },
    "codex": {
      "name": "OpenAI Codex",
      "enabled": true,
      "cli": "codex",
      "config_file": "AGENTS.md",
      "hook_dir": ".codex/hooks.json (if supported)",
      "notes": "Reads AGENTS.md. Background agents work if codex CLI is available."
    }
  },
  "file_sync": {
    "strategy": "claude_to_agents",
    "description": "CLAUDE.md is primary; AGENTS.md is kept in sync via git pre-commit hook.",
    "manual_sync_command": "cp CLAUDE.md AGENTS.md && git add AGENTS.md"
  },
  "hook_backend_priority": [
    "claude",
    "codex"
  ],
  "notes": "Backend detection is automatic. Hooks detect which CLI is available and spawn agents accordingly."
}
```

## Step 5: Update Documentation

**What:** Add Codex support notes to README and CLAUDE.md.

**Changes to README.md:**

In the "Compatibility" section, update from:
```markdown
- **Cursor** — full support (CLAUDE.md + slash commands + sessionStart, auto-reflect, and auto-consolidate hooks)
- **Claude Code** — full support (CLAUDE.md + `.claude/commands/` symlinks + sessionStart, auto-reflect, and auto-consolidate hooks)
```

To:
```markdown
- **Claude Code** — full support (CLAUDE.md + `.claude/commands/` symlinks + sessionStart, auto-reflect, and auto-consolidate hooks)
- **Cursor** — full support (reads both CLAUDE.md and AGENTS.md via sync + slash commands + hooks)
- **OpenAI Codex** — full support (AGENTS.md + hooks; requires `codex` CLI available in PATH)
```

Add a new section "Multi-Agent Setup":
```markdown
### Multi-Agent Setup

Agentic Buddy works with multiple AI agents in the same workspace:

- **Claude Code** and **Cursor** — share the same configuration (`CLAUDE.md`)
- **OpenAI Codex** — reads `AGENTS.md` (automatically kept in sync with `CLAUDE.md`)

Hooks automatically detect which agent is running them and spawn background agents with the appropriate CLI. No special configuration needed — just clone the repo and run `/setup` in your preferred editor.

If using Codex, ensure the `codex` CLI is installed and available in your PATH.
```

**Changes to CLAUDE.md:**

Add a note at the top:
```markdown
# Agentic Buddy

**Configuration files:** This file (`CLAUDE.md`) is read by Claude Code and Cursor. OpenAI Codex reads `AGENTS.md` instead. Both files are automatically kept in sync via a git hook.
```

## Step 6: Update Skills Documentation

**What:** Add notes to skills that mention configuration files.

**Example — update `agent_brain/skills/process-conversation.md`:**

From:
```markdown
## How to use
Use on "reflect", "save the conversation", or "reflect about this conversation". The agent reads the latest conversation transcript (auto-logged to `logs/`) and writes observations to `agent_brain/observations.md`, updating CLAUDE.md with any new promoted rules or skills.
```

To:
```markdown
## How to use
Use on "reflect", "save the conversation", or "reflect about this conversation". The agent reads the latest conversation transcript (auto-logged to `logs/`) and writes observations to `agent_brain/observations.md`, updating your config file (`CLAUDE.md` for Claude Code/Cursor, `AGENTS.md` for Codex) with any new promoted rules or skills.
```

**Files to update:** Any skill that mentions CLAUDE.md. Run:
```bash
grep -l "CLAUDE.md" agent_brain/skills/*.md
```

## Step 7: Test the Changes

**For Claude Code users (no change):**
```bash
# Should work exactly as before
claude -p "Run the daily cycle"
```

**For Codex users (if you have Codex CLI):**
```bash
# Verify Codex can read AGENTS.md
# Run /setup in Codex and confirm configuration loads
```

**For Cursor users:**
```bash
# Verify both CLAUDE.md and AGENTS.md are in sync
# Run /setup in Cursor and confirm configuration loads
```

## Rollback Plan

If something breaks:

```bash
# Remove AGENTS.md and pre-commit hook
rm AGENTS.md
rm .git/hooks/pre-commit

# Revert commits
git revert <commit-hash>

# Everything goes back to Claude Code only
```

## Verification Checklist

- [ ] `AGENTS.md` exists and contains the same content as `CLAUDE.md`
- [ ] Pre-commit hook runs and updates `AGENTS.md` when `CLAUDE.md` changes
- [ ] `backend.py` is syntactically correct (test with `python3 -m py_compile .cursor/hooks/backend.py`)
- [ ] `session-start.py` imports and uses `backend.detect_backend()` correctly
- [ ] `.agent-config.json` documents all backends clearly
- [ ] README.md "Compatibility" section updated
- [ ] At least 3 skills updated with Codex-aware documentation
- [ ] All changes are committed to git

## Future Enhancements

1. **Codex-specific skills:** If Codex has limitations (e.g., no background agent support), create Codex-specific variants of problematic skills.
2. **CLI wrapper:** Create a helper script that auto-detects the backend and invokes the appropriate CLI, simplifying hook code.
3. **Configuration profiles:** Allow users to create backend-specific config files (e.g., `CLAUDE.md.cursor`, `AGENTS.md.codex`) if needed.
4. **Metrics:** Track which backend is being used most, to inform future optimization decisions.

## References

- **Current backend detection:** Already implemented in release-blocker-agent (OpenAI vs Vertex AI switching)
- **Hook framework:** See `.cursor/hooks/` for existing patterns
- **Codex documentation:** https://github.com/openai/codex — verify hook format and CLI syntax
