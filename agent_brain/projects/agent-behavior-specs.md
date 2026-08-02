---
last_accessed: 2026-08-02
access_count: 1
created: 2026-08-02
---

# Agent Behavior Specs + Agent-forge Integration

Open standard by Braintrust and Basis for defining and evaluating expected agent behavior across entire trajectories. Complements Agent-forge (which builds agents) by providing the evaluation and supervision layer Agent-forge lacks.

**Site:** [agentbehavior.dev](https://www.agentbehavior.dev/)
**Repo:** [github.com/braintrustdata/agentbehavior](https://github.com/braintrustdata/agentbehavior)
**Blog:** [Behavior specs - Braintrust blog](https://www.braintrust.dev/blog/behavior-specs)
**License:** Apache 2.0

## What behavior specs are

A behavior spec (BEHAVIOR.md) is a Markdown file with YAML frontmatter that defines what good agent conduct looks like for reviewers and evaluators - not a runtime prompt. It lives alongside agent code but is never shown to the agent. It exists to be judged against.

**Core distinction:** Agent-forge builds the harness (identity + memory + procedures + tools + permissions). Behavior specs evaluate whether the harness produced the right behavior. Agent-forge is the builder; behavior specs are the inspector.

### Format

```
.agents/behaviors/<behavior-name>/
  BEHAVIOR.md        # Required: YAML frontmatter + Markdown body
  references/        # Optional: rationale, examples, background docs
```

Frontmatter requires `name` (max 64 chars, lowercase + hyphens) and `description` (max 1024 chars).

### Six optional dimensions

| Dimension | Purpose |
|-----------|---------|
| Intent | Why the behavior matters and when it applies |
| Evidence | What the agent should inspect, retrieve, verify before deciding |
| Decision | What the agent should infer or conclude from evidence |
| Execution | The visible action taken after deciding |
| Recovery | What happens when the first path fails or evidence is incomplete |
| Failure modes | What bad behavior the spec is meant to prevent |

### Grading

Each spec gets one of three verdicts per trajectory: **true** (followed), **false** (violated), **NA** (not applicable). A judge prompt ships with the standard.

### When to write a spec

Six selection criteria:
1. **Frequent** - appears in a meaningful share of the agent's work
2. **High-impact** - mistakes affect correctness, trust, safety, cost, or UX
3. **Agent-defining** - captures design choices about what kind of agent this is
4. **Ambiguous by default** - reasonable actors might diverge without guidance
5. **Spread across context** - understanding requires reading multiple sources
6. **Useful for debugging** - naming the behavior helps explain trace failures

Philosophy: "Elevate the few you care about enough to measure." Everything else stays in prompts, skills, and tool descriptions.

## Agent-forge alignment map

| Agent-forge concept | Behavior spec concept | Relationship |
|--------------------|-----------------------|--------------|
| Identity & Character (P1) | Intent + Failure modes | Identity drives runtime behavior; specs measure whether it was achieved |
| Skill Design (P5) | Behaviors vs. skills distinction | Skills are procedures agents follow; specs define the standard those procedures should achieve |
| Disconfirmation gate | Evidence dimension | Both require seeking counter-evidence before classifying/deciding |
| Memory architecture (P6) | Trajectory evaluation | Episodic store (traces) is exactly what behavior specs judge against |
| Permissions as design (P7) | Failure modes | Both constrain the behavioral envelope - permissions mechanically, specs evaluatively |
| Completion checklist | Spec as standing eval | Both exploit recency/closure to ensure completeness |
| Tool output > instructions (P4) | Spec =/= prompt | Both recognize that what shapes behavior is different from what describes it |

## Where behavior specs fill Agent-forge gaps

1. **Evaluation layer.** Agent-forge has no formalized way to evaluate whether an agent's behavior matched expectations. Behavior specs provide exactly that - the true/false/NA grading against trajectories.
2. **Process supervision.** Agent-forge focuses on building correctly. Behavior specs focus on verifying behavior continuously at production scale. Each spec becomes a standing eval.
3. **Behavioral regression detection.** When prompts, skills, or tools change, behavior specs catch drift before it reaches users.
4. **Diagnostic signal.** A failing behavior spec tells you which specific decision pattern broke, not just "the output was wrong."

## Where Agent-forge fills behavior spec gaps

1. **Runtime framework.** Behavior specs explicitly are NOT runtime instructions. Agent-forge provides identity, skills, memory, and permissions that make agents behave in ways specs can then evaluate.
2. **Memory and state.** Behavior specs don't address how agents persist knowledge across sessions.
3. **Tool design.** Behavior specs don't cover how to build tools that shape behavior (Agent-forge P4).
4. **Skill procedures.** Behavior specs reference skills but don't define how to write them.

## Integration proposal for agentic-buddy

### Phase 1: Adopt the format
- Create `.agents/behaviors/` in agentic-buddy
- Write specs for the highest-impact behaviors our agents exhibit
- Start with behaviors that have caused problems or surprised us

### Phase 2: Candidate behaviors to spec

Based on Agent-forge principles and agentic-buddy's operational experience:

| Candidate behavior | Why it qualifies |
|-------------------|------------------|
| memory-before-external-lookup | Agents should check brain files before querying external tools (Rule 5). High-impact, ambiguous, frequent |
| capture-then-confirm | When the user brain-dumps, capture first, then confirm what was captured (Core behavior 1-2). Agent-defining |
| no-unsourced-content | Never infer facts about the user without marking (Rule 10). High-impact, safety-critical |
| skill-trigger-matching | Invoke skills only when triggers match, not preemptively (Rule 2). Frequent, debugging-useful |
| commit-after-capture | Every file change ends with a commit (character trait). Agent-defining, failure-prone |
| disconfirmation-before-classification | Before classifying a known issue, seek counter-evidence. High-impact, novel |
| context-is-not-a-task | Don't convert situation descriptions into action items unless asked (Rule 11). Frequent source of errors |

### Phase 3: Connect to evaluation
- Use behavior specs to review agent traces (conversation logs in `logs/`)
- Build a lightweight judge that grades past sessions against specs
- Track behavioral regressions when skills or identity change

## Key design principle

"Expect to remove prescription over time, not accumulate it." As models improve, retire specs for behaviors the model reliably exhibits. Surviving specs should focus on higher-level judgment. This aligns with Agent-forge's thesis that the harness, not the model, is the durable investment - but acknowledges that the harness itself should shrink as models internalize behavioral patterns.
