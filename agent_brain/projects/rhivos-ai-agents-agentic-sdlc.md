---
last_accessed: 2026-06-18
access_count: 1
created: 2026-06-18
---

# RHIVOS AI Agents & Agentic SDLC — State of the Art

Landscape of AI agent initiatives across the RHIVOS / Automotive org, surfaced during the **Automotive Rollup Demo** (June 17, 2026) and related work. Tracks who is building what, design philosophies, and convergence opportunities.

**NotebookLM:** [RHIVOS AI Agents & Agentic SDLC](https://notebooklm.google.com/notebook/759e6ff3-c3f9-40eb-9393-a0439cbe163e)

## Active initiatives

### 1. Agentic Workflow for Config Validators (FoA) — Gadi Glogowski / Rajesh Srivastava

**Goal:** End-to-end automation from Jira ticket to merged MR — no human intervention in the implementation loop.

**Architecture:**
- Jira → Claude Code → GitLab pipeline
- `CLAUDE.md` controls behavior; `AGENT.md` acts as project brain (architectural constraints, skill references)
- 9 specialized skills as executable runbooks
- 6-phase triage: fetch ticket → extract fields → derive missing info (target packages, architecture) → classify new vs. modify

**Safety — 5-layer defense in depth:**
1. Agent MD rulebook (non-negotiable constraints)
2. Branch verification
3. Credential scoping (least privilege)
4. GitLab server-side protections
5. 8 presubmit quality checks (format, lint, types, security) with auto-fix on failure

**Human oversight:** Agent creates structured MR with reviewer checklist. Agent verifies metadata/docs/tests; humans verify test case IDs, CI evidence, run correctness. No merge without human approval.

**Cost strategy:** Mix frontier models (reasoning) with cheaper models (implementation heavy-lifting).

**Status:** Working in personal fork. Next steps: move to shared repo, run in CI with Claude sandbox, demonstrate improvements in next iteration.

**Sources:**
- Recording: [Google Drive](https://drive.usercontent.google.com/download?id=1T5QTF34VMtKvWBzC1BEA2aFCjRm0iQv_&export=download&authuser=0&confirm=t&uuid=d55132ea-13fb-4652-b335-6afad355b17e&at=AAINaILBv31G_oHCPu7cqPGCvrBJ%3A1781766445139) (~14 min video)
- Rajesh Srivastava's presentation: [Google Drive](https://drive.google.com/file/d/1Zmesls60OuBzjbEK1RFlJmvHkuQe84KJ/view) (needs access)
- Code (current fork): [GitLab](https://gitlab.cee.redhat.com/rajsriva/config-files/-/tree/ci/ai-agent-poc/)

### 2. Stateful Process-Oriented Agent for RHIVOS (AAA) — Juanje Ojeda

**Goal:** Agents that diagnose failures, triage defects, analyze test results, classify vulnerabilities — not write software. Persistent memory makes tomorrow's agent better than today's.

**Key concept: "The repo IS the agent."** Clone it, approve trust, you have the same agent with the same memory. Reproducible and auditable.

**Why Pi over Claude Code:**
- Model-agnostic (Gemini Flash for cost, local models for privacy, Claude for power)
- Full system prompt control — `SYSTEM.md` replaces default prompt entirely
- Minimal harness: 4 base tools (read, write, edit, bash), nothing software-dev-oriented
- MIT, fully auditable, programmatic hooks

**6 Design Principles:**
1. **Character over rules** — define *who* the agent is, not a list of instructions. Good character covers dozens of rules and reasons in new cases.
2. **Progressive disclosure** — 3 layers: identity + map → full skill → deep KB. More context ≠ better output.
3. **Memory architecture (4 stores)** — separated by who writes and drift tolerance: read-only, episodic, semantic, computed.
4. **Verify before classifying** — the stronger the match to a known pattern, the harder you look for counter-evidence (disconfirmation gate).
5. **Skills as procedures** — entry point is always a skill (numbered steps, checklists). Tools are invisible implementation details.
6. **Constraints shape behavior** — remove tools to channel behavior toward desired procedures.

**Demo:** Full pipeline failure diagnosis with progressive disclosure, disconfirmation gate, and episodic memory capture.

**Sources:**
- Slides: [Google Slides](https://docs.google.com/presentation/d/1wrRlV2bVv63rpYF2jyiRgsNo_-d5YWI7dWufD-yRJc0/edit)
- Code: [GitLab](https://gitlab.cee.redhat.com/automotive/ai/agents/toolchain/pipelines-debugger)

### 3. AIIL: Issue-to-Release with Closed-Loop HIL Verification — Michael Kuehl

See [aiil-demo-rhas.md](aiil-demo-rhas.md) for full details. Presented overview at rollup demo (5 min).

**Connection:** AIIL is the outer-loop counterpart — where Gadi's and Juanje's agents handle the inner loop (code/debug), AIIL orchestrates the full issue → build → test-on-hardware cycle with AI-driven remediation.

### 4. Automotive AI GitLab Namespace

**URL:** https://gitlab.cee.redhat.com/automotive/ai

Houses shared AI agent work including:
- `codebase-documenter` — agent skill
- `wiki-kb` — agent skill
- AIB + Automotive SIG docs wiki
- RHIVOS docs wiki

Mentioned during rollup demo as live demo (no recording).

## Cross-cutting themes from the rollup demo discussion

### Memory architecture consensus
- **File-based, transparent memory (markdown) > opaque memory** — human-readable, manually interventionable.
- **Hooks are essential** — end-of-session triggers or interaction-count triggers force the agent to capture/save. Relying on model autonomy doesn't work.
- **Compaction prevents contradictions** — without scheduled consolidation (daily → weekly → monthly), agents struggle with shifted preferences (e.g., PDM → UV).
- Claude Code's auto-shrinking is early-stage. Build your own with prompts and hooks.
- Ian McLeod: "The memory structure is deeply intertwined with the tasks the agent performs."

### Agent identity and harness
- Claude Code creates an "illusion of memory" through harness + prompts + skills, not model changes.
- Internal hooks (leaked) can be replicated using public hooks.
- The harness (identity, memory, procedures, controlled tools, permissions) is what separates a useful agent from a chatbot.

### Safety patterns
- Defense in depth (Gadi): multiple independent safety layers, no single point of failure.
- Constraints as design (Juanje): removing tools channels behavior, doesn't limit capability.
- Human-in-the-loop at merge point (both): agent proposes, human approves.

## People

| Person | Role | Initiative |
|---|---|---|
| Gadi Glogowski | Agent developer | FoA concert validator workflow |
| Rajesh Srivastava | Agent developer | FoA agentic workflow, moving to shared repo |
| Juanje Ojeda | Toolchain, AAA | Stateful process-oriented agent, Pi-based |
| Michael Kuehl | Sr. Principal Ecosystem Architect | AIIL vision |
| Ian McLeod | (moderator/reviewer) | Cross-cutting observations on memory + harness |
| Tomas Golembiovsky | (participant) | Raised memory instruction question |

## Sources index

| # | Source | Type | Access |
|---|---|---|---|
| 1 | [Recording](https://drive.usercontent.google.com/download?id=1T5QTF34VMtKvWBzC1BEA2aFCjRm0iQv_&export=download&authuser=0&confirm=t&uuid=d55132ea-13fb-4652-b335-6afad355b17e&at=AAINaILBv31G_oHCPu7cqPGCvrBJ%3A1781766445139) | Video | Google Drive download |
| 2 | [Gemini Notes](https://docs.google.com/document/d/1fEF9uo8H5h7qD35_uOSulzMNNMgoCC4aBBgEJTxyYh4/edit?tab=t.7jrm9n9egojh) | Google Doc | OK |
| 3 | [Meeting Notes](https://docs.google.com/document/d/1_DsyRxX0DtZJuHbEvDRsNmBb6kX-NlYyUWMpwfzchPI/edit) | Google Doc | OK (Jun 17 section) |
| 4 | [Juanje Slides](https://docs.google.com/presentation/d/1wrRlV2bVv63rpYF2jyiRgsNo_-d5YWI7dWufD-yRJc0/edit) | Google Slides | OK |
| 5 | [Juanje Code](https://gitlab.cee.redhat.com/automotive/ai/agents/toolchain/pipelines-debugger) | GitLab | Internal |
| 6 | [Rajesh Presentation](https://drive.google.com/file/d/1Zmesls60OuBzjbEK1RFlJmvHkuQe84KJ/view) | Google Drive | Needs sharing |
| 7 | [Rajesh Code](https://gitlab.cee.redhat.com/rajsriva/config-files/-/tree/ci/ai-agent-poc/) | GitLab | Internal |
