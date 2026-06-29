---
member: Muhamad Abo Ras
title: Senior Software Engineer
team: PitCrew - RHAS
ic_level: 3
job_family: Software Engineering
track: Professional
evidence_period: Q2 2026 (April 1 - June 30)
generated: 2026-06-29
---

# Development Brief - Muhamad Abo Ras

**Priority sources:** [CY26Q3 Priorities](https://docs.google.com/document/d/1uX_NBIRiDA46d_xzxCgWYkE7AaMUKoW9L1rDh-tp7kg) (Kanitha Chim, Paul Wallrabe) | [RHIVOS April 2026 All-Hands slides 17-24](https://docs.google.com/presentation/d/18b4bZ75C1c_K8KUELQRtiWibm9-Wmi1zB5Ct0HiHe0Y) | [Team priorities reference](../../../team-priorities.md)

## a. Current position snapshot

Muhamad is a Senior Software Engineer (IC Level 3) on the PitCrew team, performing within Level 3 expectations on the technical execution dimension but below expectations on visibility and cross-team engagement. His work on E2E testing infrastructure and CI/CD improvements is solid and substantive - all 5 closed tickets are Stories, indicating multi-day engineering work rather than quick fixes. However, his low Slack presence (38 messages, lowest on the team) and narrow channel spread limit his organizational impact and make it difficult to build the influence needed for Level 4 progression.

## b. Dimension assessment

| Dimension | Level 3 Expectation | Q2 Evidence | Level 4 Requirement | Rating |
|---|---|---|---|---|
| Scope | Works independently, delivers on/enhances existing processes | 5 Stories closed, 10 PRs. OIDC e2e tests, PR-triggered test tiers, CRC migration, Kind improvements. Independent work within testing domain. | Sets and achieves objectives tied to functional targets. Proposes new techniques. Coordinates team. | Developing 3 |
| Complexity | Good judgment on non-routine, moderately complex issues in own area | E2E test infrastructure requires good judgment (CRC migration, Kind improvements). ArgoCD disaster recovery (PITCREW-416) is moderately complex. Relationships mostly within own team. | Independent judgment on varied, non-routine projects. Expert within team/department. Leads cooperative efforts. | Developing 3 |
| Impact | Contributes to team goals through tasks. Decisions moderately impact immediate team. | Testing infrastructure impacts team quality, but visibility of this impact is low. 38 Slack messages limits awareness of his contributions across the team and org. | Contributes to functional goals through operational direction. Decisions impact customer, operational, or program objectives. | Developing 3 |

## c. Competency readiness

| Competency | Expected (IC3) | Assessment | Evidence |
|---|---|---|---|
| Red Hat Multiplier | Experienced | Needs Development | 38 messages across 7 channels is the lowest team visibility. Attended NHCE Brno (positive), but no evidence of community engagement beyond attendance. |
| Strategic | Experienced | Developing | Executes on assigned testing work. PR-triggered test tiers show some process improvement thinking. No evidence of connecting work to strategic objectives. |
| Influence | Experienced | Needs Development | 11 messages in team channel is very low. Limited Slack presence in cross-team channels (ocm-osd-ui: 8, forum-ciam: 4). Hard to influence when you're not visible. |
| Execution | Experienced | Experienced | 5 Stories closed, 2 active, 10 PRs (7 merged). All Stories (substantive work). Consistent delivery on testing infrastructure. |
| Team Advocate | Experienced | Developing | No mentoring or coordination evidence. Testing infrastructure work supports the team indirectly but no direct team advocacy visible. |
| Problem Solving | Experienced | Experienced | CRC migration, Kind improvements, and ArgoCD disaster recovery all require solid problem-solving. PR-triggered test tiers show process improvement thinking. |
| Customer Focus | Experienced | Needs Development | No customer-facing work visible this quarter. Testing infrastructure is internally focused. |
| Continuous Learning | Experienced | Developing | Attended NHCE Brno. No evidence of AI tool adoption or knowledge-sharing artifacts. |

## d. Strengths to leverage

1. **Testing infrastructure depth.** Muhamad is building real expertise in E2E testing, CI/CD pipelines, and test infrastructure (OIDC tests, PR-triggered tiers, CRC migration, Kind). This is a foundational capability the team depends on, and it positions him well for the "establish/monitor testing practices" expectation at Level 4 - if he makes the work visible and extends it beyond his own scope.

2. **Substantive engineering.** All 5 closed tickets are Stories, not quick tasks. This shows he takes on multi-day, complex work and delivers it. The PR-triggered test tier refactoring shows process improvement thinking - he's not just executing, he's improving how the team works.

3. **ArgoCD/C2 disaster recovery.** Active work on PITCREW-416 (ArgoCD disaster recovery) is high-impact infrastructure work that directly supports the Q2 cleanup and C2 recovery team priority. This is good alignment with team needs.

## e. Growth opportunities

1. **Visibility and communication (highest priority)** (maps to: all team priorities). 38 Slack messages is a significant gap. Muhamad's work is good, but if nobody knows about it, it can't build influence or demonstrate impact. This is the single most important growth area - not because the work is lacking, but because the work deserves to be seen. Specific actions: share testing results in team channel, post brief updates when PRs land, ask questions in cross-team forums.

2. **Cross-component testing scope** (maps to: Productization, Konflux onboarding). Muhamad's testing expertise is currently scoped to the builder domain. Extending E2E testing practices to Konflux or other team components would expand scope toward Level 4 ("establish/monitor testing practices for multiple teams") and create cross-team value.

3. **Knowledge sharing on testing practices** (maps to: driving internal adoption of builder parts). Muhamad has deep knowledge of the team's test infrastructure that exists mostly in his head and in PRs. Writing a testing guide, presenting at a team meeting, or creating a "how to write E2E tests for PitCrew" doc would build both Team Advocate and Influence competencies.

4. **Customer connection** (maps to: securing 3+ automotive customer wins). Find one way to connect testing work to customer outcomes. For example, documenting how E2E test coverage reduces customer-facing regressions, or adding test scenarios that mirror customer deployment patterns. This builds Customer Focus competency.

## f. 1:1 talking points

1. "Your testing infrastructure work this quarter has been solid - 5 Stories closed, all substantive. I want to make sure the rest of the team and org can see that value. What would make it easier for you to share updates more regularly in Slack or team meetings?"

2. "I notice you're most active in ocm-osd-ui and forum-ciam channels outside our team. What's pulling you there? Is there cross-team work we should be tracking?"

3. "The ArgoCD disaster recovery work (PITCREW-416) is important for our Q2 cleanup priority. Where does that stand, and are there blockers I can help with?"

4. "How was NHCE Brno? Were there sessions or connections that could feed back into our testing or CI/CD work?"

5. "As we onboard to Konflux, do you see an opportunity to bring your E2E testing expertise to that platform? That could be a real growth opportunity for you and high value for the team."

## g. Recommended next steps

1. **Set a minimum Slack communication cadence** (maps to: all priorities - visibility enables everything). Agree on a lightweight target: one testing update per week in team-pitcrew-automotive (test results, PR summaries, blockers). This is not about volume - it's about making good work visible.

2. **Propose a testing strategy for Konflux onboarding** (maps to: Productization, Konflux onboarding). Write a short proposal for how E2E testing should work in the Konflux environment. This builds Level 4 evidence ("proposes new techniques") and positions Muhamad as the testing authority for the migration.

3. **Document the E2E testing architecture** (maps to: driving internal adoption of builder parts). Create a testing guide that other team members or teams can use. This addresses the knowledge-sharing gap and builds Team Advocate competency. Even a well-structured README in the test repo would count.

4. **Present ArgoCD disaster recovery learnings** at a team meeting or in a Slack post (maps to: Q2 cleanup, C2 recovery). PITCREW-416 is complex, high-impact work. A 10-minute walkthrough or a written summary would build both Influence and Problem Solving visibility.

5. **Identify one customer-facing test scenario** (maps to: securing 3+ automotive customer wins). Add an E2E test case that mirrors a real customer deployment pattern. This connects testing work to business outcomes and develops Customer Focus.

---

## Disconfirmation gate

- **Promotion readiness (Level 3 to 4):** Not yet, and the primary blocker is visibility, not capability. Muhamad's technical execution is at Level 3 and his testing expertise could support Level 4 claims, but the Influence and Red Hat Multiplier competencies are significantly below Experienced. 38 Slack messages across the quarter means his contributions are largely invisible to the organization. Before assessing Level 4 readiness on technical dimensions, the communication and visibility gap needs to close. Estimated 3-4 quarters minimum, with visibility improvement as the prerequisite.
- **Risk of underrating:** Muhamad may be doing more cross-team or complex work than Slack data shows. The ocm-osd-ui and forum-ciam activity (8 and 4 messages respectively) hints at breadth we might not see in Jira. Worth exploring in 1:1.
- **Risk of overrating:** Counting all 5 Stories as substantive is based on Jira classification. Without reviewing the actual scope of each Story, some may be smaller than the label suggests.
- **Data quality:** Slack data is the weakest signal here - low volume makes it hard to distinguish "quiet contributor" from "disengaged." 1:1 conversation is essential to calibrate.
