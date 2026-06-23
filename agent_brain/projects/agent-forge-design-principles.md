---
last_accessed: 2026-06-23
access_count: 3
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

## Prior art analysis (2026-06-22)

Research traced all 7 principles across academic papers, Anthropic docs, frameworks, and blogs. **Overall: practitioner synthesis with novel terminology.**

| Principle | Origin | Key source |
|-----------|--------|------------|
| Identity & Character (80/20) | Anthropic's thesis; ratio is Juanje's | "Claude's Character" (Jun 2024), "Teaching Claude Why" (May 2026) |
| Instruction Budget (~150-200) | Boris Cherny (Claude Code) | HumanLayer blog; IFScale (NeurIPS 2025) |
| Progressive Disclosure | Anthropic Agent Skills (Oct 2025) + UX (Nielsen 2006) | agentskills.io, Corpus2Skill (Apr 2026) |
| Tool Output > Instructions | Known finding, reframed as design principle | JetBrains Koog (2025), arXiv:2606.14476 |
| Skill Design / Procedures | Agent Skills pattern | agentskills.io, SoK (arXiv:2602.20867) |
| Memory Architecture (4-store) | Cognitive science + CoALA (TMLR 2024) | Tulving (1972), Park et al. (UIST 2023) |
| Permissions as Design | Deny-by-default is consensus | OWASP, Claude Code, Microsoft AGT |

**Novel coinages (zero public results):** "disconfirmation gate," "computed store," "skill-permission parity," "channel reliability," "completion checklist" as recency exploit.

**Unsubstantiated claims:** "uniform degradation" (actually U-shaped per Liu et al.), "file nav > RAG up to ~1000 entries" (no source), instruction budget attributed to Boris Cherny not Juanje.

> Related: [RHIVOS AI Agents & Agentic SDLC](rhivos-ai-agents-agentic-sdlc.md) — Landscape of all AI agent initiatives in the automotive org. Agent-forge is Initiative #5.
