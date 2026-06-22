---
last_accessed: 2026-06-22
access_count: 2
created: 2026-06-21
---

# Stateful Process-Oriented Agent Design Principles

Distilled from Juanje Ojeda's [agent-forge](https://gitlab.cee.redhat.com/automotive/ai/agents/common/agent-forge) — a meta-agent for bootstrapping and evaluating agents. Full principle docs live in `agent-forge/docs/principles/`.

## The core insight

Process-oriented agents diagnose, triage, analyze, and narrate — they don't write software. Persistent memory makes tomorrow's agent better than today's. **The repo IS the agent** — clone it, approve trust, you have the same agent with the same memory.

## Seven principles (summary)

### 1. Identity & character — values, not rules

~80% character traits, ~20% hard limits. Character creates an inference space: the agent derives behavior in novel situations from values, not from matching rules. Include what the agent IS, DOES, and IS NOT.

### 2. Instruction delivery — channel matters

Match content to reliability channel. System prompt (highest) → injected hooks → operations guide → skills → referenced files. ~150–200 instruction budget per session; each added instruction degrades all others.

### 3. Progressive disclosure — three layers

Layer 1: always-visible identity + navigation map (~500 lines). Layer 2: on-demand skills + active context. Layer 3: deep knowledge via index navigation. **Layer 1 is the product.** Every directory needs an index file.

### 4. Tool design — two modes only

Default smart extraction + raw download. No `--tail`/`--limit`/`--timeout` flags. Tool output shapes behavior more reliably than written instructions. Errors as diagnostic evidence, not stack traces.

### 5. Skill design — procedures, not tool docs

Trigger + numbered steps + success criteria. Tools only appear inside skill steps. Disconfirmation gate for diagnostic skills. Completion checklist for 5+ step skills (exploits recency bias).

### 6. Memory architecture — four stores

| Store | Who writes | Mutability |
|-------|-----------|------------|
| Read-only reference | Developer | No agent writes |
| Episodic active | Agent | Write-once, append follow-ups |
| Episodic history | Agent | Immutable after close |
| Semantic | Agent | Consolidation skill only |

Plus computed store (script-derived, never LLM-computed) and observations scratch pad.

### 7. Permissions as design — constraints shape capability

Deny-by-default. Restrict tools that invite improvisation. Channel toward designed paths. Remove tools to channel behavior, don't just add rules.

## Phase progression

1. **Day 1:** Identity, operations guide, 1 skill, 1 tool, minimal KB, permissions
2. **Week 1–2:** Capture skill, episodic history, record template
3. **Week 2–4:** Consolidation skill, semantic knowledge, stats script
4. **Maturity:** Secondary skills, verification procedures, health checks

**Rule:** Don't skip Phase 1 validation. Complexity is earned through usage.

## Key anti-patterns

- Long rule lists instead of character traits
- KB maps in system prompt (wastes highest-reliability channel)
- Tool syntax in identity (agent bypasses skills)
- Flat patterns file rewritten incrementally (drift compounds)
- LLM-computed statistics (plausible but wrong)
- Agent self-diagnoses its own harness (post-hoc rationalization)

## Source

- **Repo:** https://gitlab.cee.redhat.com/automotive/ai/agents/common/agent-forge
- **Email:** Juanje Ojeda → automotive-devel, 2026-06-19
- **Related project:** [RHIVOS AI Agents & Agentic SDLC](../projects/rhivos-ai-agents-agentic-sdlc.md)
