---
member: Hubert Stefanski
title: Senior Software Engineer
team: ATC (Automotive Toolchain), transitioning to PitCrew/RHAS
ic_level: 3
job_family: Software Engineering
track: Professional
evidence_period: Q2 2026 (April 1 - June 30)
generated: 2026-06-29
---

# Development Brief - Hubert Stefanski

**Priority sources:** [CY26Q3 Priorities](https://docs.google.com/document/d/1uX_NBIRiDA46d_xzxCgWYkE7AaMUKoW9L1rDh-tp7kg) (Kanitha Chim, Paul Wallrabe) | [RHIVOS April 2026 All-Hands slides 17-24](https://docs.google.com/presentation/d/18b4bZ75C1c_K8KUELQRtiWibm9-Wmi1zB5Ct0HiHe0Y) | [Team priorities reference](../../../team-priorities.md)

## a. Current position snapshot

Hubert is performing at IC Level 3 with consistent Level 4 signals across scope, complexity, and impact. His combination of deep infrastructure expertise, gating innovation (dependency triggers, kernel variant handling, QC LP gating spike), and cross-team collaboration (ATC, PitCrew, CAT, ITSEC) positions him at the Level 3-4 boundary. The approved transition to PitCrew/RHAS (Jun 18) creates a unique opportunity: he can carry his infrastructure and gating expertise into a new team context, demonstrating the cross-team leadership and mentoring breadth expected at Level 4.

## b. Dimension assessment

| Dimension | Level 3 Expectation | Q2 Evidence | Level 4 Requirement | Rating |
|---|---|---|---|---|
| Scope | Works independently, delivers on existing processes | 17 tickets, 29 MRs merged; proposes new techniques (dependency triggering, QC LP gating); helped PitCrew design GitLab repo structure | Sets and achieves objectives tied to functional targets; proposes new techniques with functional impact | Stretching toward next |
| Complexity | Good judgment on moderately complex issues in own area | Independent judgment on non-routine gating issues; 18 channels; cross-team relationships (PitCrew, CAT, ITSEC); Jumpstarter CTC evaluation | Independent judgment on varied, non-routine projects; expert leading cooperative efforts | Stretching toward next |
| Impact | Contributes to team goals; decisions moderately impact immediate team | Gating improvements impact release quality; infrastructure decisions affect downstream consumers; security work (VHCL-014, Major); 3 Major-priority tickets | Contributes to functional goals; decisions impact customer/operational objectives | Stretching toward next |

## c. Competency readiness

| Competency | Expected (IC3) | Assessment | Evidence |
|---|---|---|---|
| Red Hat Multiplier | Experienced | At/above | 402 Slack messages, 18 channels; active in forum-jumpstarter(17), automotive-cat-collaboration(15); cross-team GitLab repo design for PitCrew |
| Strategic | Experienced | At level | QC LP gating spike; Jumpstarter CTC evaluation epic; dependency trigger design |
| Influence | Experienced | At/above | wg-team-auto-toolchain-infra(105 messages); cross-team engagement with PitCrew, CAT, ITSEC |
| Execution | Experienced | At/above | 17 tickets resolved, 29 MRs merged, 3 Major-priority tickets; legacy webserver decommissioning |
| Team Advocate | Experienced | At level | Infrastructure knowledge shared through wg-infra channel; pairing with Eitan on CloudFront; Gator sessions |
| Problem Solving | Experienced | At/above | Dependency triggers for gating, kernel variant handling, container vulnerability resolution (VHCL-014) |
| Customer Focus | Experienced | At level | Gating improvements directly affect release quality; infrastructure reliability supports downstream teams |
| Continuous Learning | Experienced | At level | Jumpstarter evaluation; PitCrew transition broadens domain exposure; QC LP gating spike |

## d. Strengths to leverage

1. **Infrastructure and gating innovation.** Hubert doesn't just maintain infrastructure - he proposes new approaches. Dependency triggering, kernel variant handling, and the QC LP gating spike all show the Level 4 behavior of "proposing new techniques with functional impact." This is his strongest Level 4 signal.

2. **Cross-team bridge building.** With 402 Slack messages across 18 channels and active engagement in PitCrew, CAT, Jumpstarter, and ITSEC forums, Hubert naturally builds the cooperative relationships Level 4 requires. The PitCrew transition amplifies this - he'll carry ATC context into a new team.

3. **Execution at scale.** 29 MRs merged (tied for highest on team) with 17 tickets resolved, including 3 Major-priority items and security work. Hubert delivers consistently across infrastructure, gating, and security domains simultaneously.

## e. Growth opportunities

1. **Technical strategy ownership.** Hubert tends to respond to problems rather than proactively defining technical direction. For Level 4, the shift is from "resolves complex issues" to "sets and achieves objectives tied to functional targets." The PitCrew transition is an ideal moment to own the technical strategy for AIB prototyping (PITCREW-161) rather than just executing on it. Maps to PitCrew Priority #3 (Productization).

2. **Business impact positioning.** Hubert's gating and infrastructure work directly impacts release quality and downstream consumers, but this impact isn't framed in business terms. Connecting work to customer outcomes - "this gating improvement prevented X release-blocking issues" or "this infrastructure change reduced pipeline failures by Y%" - would strengthen the Level 4 Impact dimension. Maps to Program Priority (3+ automotive customer wins).

3. **AI tooling adoption.** Compared to Eitan's AI tooling work, Hubert has less visible AI adoption in Q2. The Level 4 differentiator requires "evaluating and introducing new AI methodologies." The AIB prototyping work (PITCREW-161) on PitCrew is a natural entry point. Maps to Program Priority (Agentic SDLC transformation).

4. **Knowledge sharing formalization.** Hubert's infrastructure expertise is shared informally through Slack and pairing sessions. Formalizing this into design documents, runbooks, or presentations would address the Level 4 Knowledge Sharing differentiator and create lasting team resources. Especially important during the transition - documenting ATC infrastructure decisions ensures continuity.

## f. 1:1 talking points

1. With the PitCrew transition approved, how are you thinking about dividing your focus between wrapping up ATC infrastructure work and ramping up on PITCREW-161 (AIB prototyping)?

2. Your gating innovations (dependency triggers, kernel variants) are some of the most technically creative work on the team. Have you considered writing those up as design docs that others can reference and build on?

3. Looking at Level 4, one key shift is from "resolving complex issues" to "setting and achieving objectives." For PITCREW-161, do you see yourself defining the technical strategy, or executing on someone else's design?

4. The Jumpstarter CTC evaluation was a good example of cross-team technical leadership. How did that go, and are there similar evaluation or design review opportunities you'd want to take on at PitCrew?

5. As you transition, what ATC infrastructure knowledge do you think is most at risk of being lost? How can we make sure it's captured before you shift focus?

## g. Recommended next steps

1. **Own the AIB prototyping technical strategy** (PITCREW-161) - define the approach, write the design doc, and present it to PitCrew stakeholders. Don't just execute; set the technical direction. (PitCrew Priority #3: Productization; Level 4 Scope + Strategic competency)

2. **Document ATC infrastructure decisions** before transitioning - create runbooks or design docs for dependency triggering, gating configuration, and IAM/S3 access patterns. This ensures continuity and demonstrates knowledge sharing at Level 4. (ATC Priority #6: Infra improvements; Level 4 Knowledge Sharing differentiator)

3. **Frame gating improvements in business impact terms** - quantify how dependency triggers and kernel variant handling prevented release issues or reduced gating cycle time. Present findings to release readiness stakeholders. (Program Priority: 3+ customer wins; Level 4 Impact dimension)

4. **Explore AI tooling for infrastructure or gating automation** - evaluate Claude Code or similar tools for pipeline configuration, gating rule generation, or infrastructure provisioning. (Program Priority: Agentic SDLC transformation; Level 4 AI differentiator + Continuous Learning competency)

5. **Bridge ATC-PitCrew infrastructure patterns** - identify reusable infrastructure approaches from ATC (runners, S3, IAM) that PitCrew can adopt for Konflux and internal builds. (PitCrew Priority #3: Productization + ATC Priority #5: Konflux; Level 4 Community differentiator)

---

## Disconfirmation gate

| Item | Detail |
|---|---|
| Question | Is the PitCrew transition evidence of Level 4 cross-team leadership, or does it reset Hubert's trajectory by moving him to a new domain where he starts as a learner? |
| Contradicting evidence sought | Will Hubert carry his infrastructure expertise as a strength into PitCrew (Level 4 signal: expert leading cooperative efforts across teams), or will he need significant ramp-up time on PitCrew's domain (AIB, Konflux, Hatchi) that temporarily reduces his scope and impact? |
| Conclusion | Both are true, but the net effect is positive. Hubert's infrastructure expertise (AWS, S3, GitLab runners, IAM, gating) is directly applicable to PitCrew's Productization priority (Konflux, internal builds). He already helped PitCrew design their GitLab repo structure and has 10 messages in team-pitcrew-automotive. The AIB prototyping work (PITCREW-161) is new domain territory, but it's scoped as a spike - not a full ramp-up. The bigger risk is that Hubert defaults to reactive execution on PitCrew rather than proactive technical leadership, which would repeat the Level 3 pattern. The recommended next steps specifically target this: owning the strategy, not just the implementation. |
