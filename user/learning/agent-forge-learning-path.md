# Agent-Forge Learning Path

Learning Juanje Ojeda's agent-forge design principles by studying the pipelines-debugger agent, then building my own.

## Status

- [x] **Module 1:** Identity & Navigation (Principles 1-3) — completed 2026-06-22
- [~] **Module 2:** Skills & Tools (Principles 4-5) — in progress, checkpoint pending
- [ ] **Module 3:** Memory & Permissions (Principles 6-7)
- [ ] **Module 4:** Pick a Candidate & Bootstrap

## Resources

- Pipelines-debugger (local): `/home/aefrat/git/pipelines-debugger`
- Agent-forge (remote): `https://gitlab.cee.redhat.com/automotive/ai/agents/common/agent-forge`
- NotebookLM: `https://notebooklm.google.com/notebook/7f00e410-350e-44ad-b866-9dac6df156de`
- Brain notes: `agent_brain/concepts/stateful-process-oriented-agents.md`, `agent_brain/projects/agent-forge-design-principles.md`

## Notes

### Module 1 — Key takeaways (2026-06-22)
- **P1 (Identity):** 80% character traits (values for novel situations) / 20% hard limits. IS/DOES/IS NOT pattern. Procedural mandate ("always work through skills").
- **P2 (Instruction Delivery):** CLAUDE.md = highest reliability channel. ~150-200 instruction budget — each added instruction degrades all others. Navigation map goes here; content does not.
- **P3 (Progressive Disclosure):** 3 layers — always-loaded identity+map → on-demand skills → deep KB via index chains. Every directory has an index.md. Frequency ordering (most likely patterns first).
- **Checkpoint answer:** KB map is in CLAUDE.md but content isn't because: (1) token waste — model processes irrelevant content every turn, (2) attention dilution — model doesn't know where to look, (3) instruction budget — content in the system prompt degrades the character traits.

### Module 2 — Covered so far (2026-06-22)
- Read `diagnose-pipeline` (331-line, 10-step core workflow) and `check-services` (4-step simpler skill).
- **P5 (Skill Design):** Trigger + numbered steps + success criteria + gotchas + completion checklist. Disconfirmation gate for diagnostic skills.
- **P4 (Tool Design):** Two modes — compact default vs `--full`. "Prefer flags over pipes." Tool output shapes behavior. Denied `curl` forces agent through designed tools.
- **P7 preview:** Permissions mirror memory stores — read=global, write=skill-scoped.
- **Pending checkpoint:** Explain the disconfirmation gate pattern and why it matters.

### Resume point
Next session: answer Module 2 checkpoint (disconfirmation gate), then Module 3 (Memory & Permissions).
