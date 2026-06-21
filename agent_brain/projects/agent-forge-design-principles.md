---
last_accessed: 2026-06-21
access_count: 1
created: 2026-06-21
---

# Agent Forge — Design Principles for Process-Oriented Agents

Juanje Ojeda's framework for building stateful, process-oriented AI agents. Documented in the [agent-forge repo](https://gitlab.cee.redhat.com/automotive/ai/agents/common/agent-forge) and presented at the Automotive Rollup Demo (June 17, 2026).

**NotebookLM:** [Agent Forge — Stateful Process-Oriented Agent Design Principles](https://notebooklm.google.com/notebook/7f00e410-350e-44ad-b866-9dac6df156de)

**Slides:** [Stateful Process-Oriented Agent for RHIVOS](https://drive.google.com/open?id=1wrRlV2bVv63rpYF2jyiRgsNo_-d5YWI7dWufD-yRJc0)

## Core thesis

The model is interchangeable — the harness (identity + memory + procedures + tools + permissions) is what separates a useful agent from a chatbot with API access. Process-oriented agents don't write code; they diagnose, triage, analyze, and classify. They learn from past cases via persistent file-based memory.

## The 7 principles

1. **Identity & Character** — 80% character traits (values that derive behavior in novel situations), 20% hard limits. Procedural mandate: "I always work through skills."
2. **Instruction Delivery** — Match content to channel reliability. ~150-200 instruction budget; each new instruction degrades all others uniformly. System prompt > hooks > operations guide > referenced files.
3. **Progressive Disclosure** — Three layers: always-visible identity+map (~500 lines) → on-demand skills → deep KB via index navigation. File-based navigation outperforms RAG up to ~1000 entries.
4. **Tool Design** — Two modes only (extract default + raw download). Tool output shapes behavior more reliably than written instructions. Mutation safety: dry-run + env gate + --apply flag.
5. **Skill Design** — Procedures, not tool docs. Trigger + numbered steps + success criteria. Disconfirmation gate for diagnostics. Completion checklist for 5+ steps (exploits recency bias).
6. **Memory Architecture** — Four-store model: read-only reference (developer) → episodic active (write-once) → episodic history (immutable) → semantic (consolidation only) + computed (script-only, never LLM). The #1 failure: agent rewriting its own knowledge with compounding errors.
7. **Permissions as Design** — Constraints shape capability, not just security. Deny-by-default. Skill-permission parity. Self-protection (agent can't modify own tools/permissions).

## Key concepts

- **Disconfirmation gate** — before classifying a failure as a known issue, seek evidence that contradicts the hypothesis. The stronger the match, the harder you look for counter-evidence.
- **Skill-permission parity** — tool access in skills must match what permissions allow. Update both together.
- **Computed store** — statistics must be script-derived, never LLM-computed. LLM statistics are plausible but wrong.
- **Completion checklist** — compressed step mirror at end of complex skills. Recency bias re-activates step awareness.

## Convergence with agentic-buddy

Aligned: character over rules (SOUL.md), progressive disclosure (Rule 2), episodic immutability (Rule 6, logs never deleted), skill triggers.

Gaps worth adopting:
- **Disconfirmation gate** — not formalized in our skills
- **Computed store separation** — we don't enforce script-only for metrics
- **Permissions as design** — we rely on instructions, not mechanical enforcement
- **Skill success criteria** — our skills lack explicit "done" conditions

## Repo structure

```
agent-forge/
├── CLAUDE.md              # Forge agent identity + skill triggers
├── .claude/skills/        # 10 skills: bootstrap, populate, 8 review skills
├── docs/
│   ├── principles/        # 7 principle docs (each: concept, rules, eval criteria, examples)
│   ├── anti-patterns.md   # Cross-cutting mistakes
│   ├── decision-guide.md  # Harness, memory, tool freedom decisions
│   └── glossary.md        # Terms mapped to Pi / Claude Code / Cursor
├── templates/
│   ├── skeleton/          # Copy-ready Phase 1 agent structure
│   └── fragments/         # Per-component annotated templates
└── examples/              # Annotated extracts from production agents
```

> Related: [RHIVOS AI Agents & Agentic SDLC](rhivos-ai-agents-agentic-sdlc.md) — Landscape of all AI agent initiatives in the automotive org. Agent-forge is Initiative #5.
