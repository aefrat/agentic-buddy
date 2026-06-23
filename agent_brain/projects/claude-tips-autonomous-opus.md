---
last_accessed: 2026-06-23
access_count: 1
created: 2026-06-23
---

# Claude Tips — Autonomous Opus (Boris Cherny)

Source: [Boris Cherny tweet](https://x.com/bcherny/status/2063792263067754658) (Jun 2026)

Five tips for running Opus autonomously for hours/days, from the creator of Claude Code.

## Tips and enablement status

### 1. Auto mode for permissions
**What:** Remove permission prompts so Claude runs uninterrupted.
**How:** `claude --dangerously-skip-permissions` or allowlists in `.claude/settings.json`.
**Status:** Partially enabled — we have selective allowlists but not full auto mode.
**Risk:** Full auto mode removes safety guardrails. Allowlist approach is safer.

### 2. Dynamic workflows
**What:** Claude orchestrates hundreds/thousands of subagents via the `Workflow` tool.
**How:** Request "use a workflow" or invoke the Workflow tool directly.
**Status:** Available (requires Opus model, which we use).

### 3. `/goal` or `/loop`
**What:** Keep Claude going across turns until the task is done.
**How:** `/loop 5m <task>` for recurring execution; `/goal <objective>` for persistent goals.
**Status:** Available. `/loop` skill is registered.

### 4. Claude Code in the cloud
**What:** Run sessions remotely so they persist when laptop is closed.
**How:** Desktop/mobile app (built-in persistence), or SSH/tmux to a remote machine.
**Status:** Not set up. Evaluate desktop app or remote VM approach.

### 5. Self-verification
**What:** Give Claude a way to confirm its work end-to-end (browser, simulator, full server).
**How:** Claude in Chrome extension, iOS/Android sim MCP, or `/run`/`/verify` skills.
**Status:** `/verify` and `/run` skills available. Chrome extension not installed. No simulator MCP.

## Action items

- [ ] Review and expand `.claude/settings.json` allowlists for common autonomous operations
- [ ] Test `/loop` and `/goal` on a real multi-hour task
- [ ] Evaluate cloud execution options (desktop app persistence vs remote VM)
- [ ] Install Claude in Chrome extension for web app verification
- [ ] Document which workflows we've used successfully
