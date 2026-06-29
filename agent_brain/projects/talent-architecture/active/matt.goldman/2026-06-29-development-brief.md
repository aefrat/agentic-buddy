---
member: Matt Goldman
title: Principal SRE
team: ATC - Auto ToolChain
ic_level: 4
job_family: SRE
track: Professional
evidence_period: Q2 2026 (April 1 - June 30)
generated: 2026-06-29
time_in_role: ~2.5 months
time_at_red_hat: ~2.5 months
---

# Development Brief - Matt Goldman

**Priority sources:** [CY26Q3 Priorities](https://docs.google.com/document/d/1uX_NBIRiDA46d_xzxCgWYkE7AaMUKoW9L1rDh-tp7kg) (Kanitha Chim, Paul Wallrabe) | [RHIVOS April 2026 All-Hands slides 17-24](https://docs.google.com/presentation/d/18b4bZ75C1c_K8KUELQRtiWibm9-Wmi1zB5Ct0HiHe0Y) | [Team priorities reference](../../../team-priorities.md)

**Tenure:** ~2.5 months in current role (Principal SRE) | ~2.5 months at Red Hat

## a. Current position snapshot

Matt joined the ATC team on April 13, 2026, giving him approximately 2.5 months in role during this evidence period. He is building toward IC Level 4 (Principal) expectations in a new domain - automotive toolchain SRE - and showing healthy ramp signals: independent investigation (2 spikes), security responsiveness (VHCL-005 critical fix), and broad relationship-building (148 messages across 15 channels). The assessment below reflects a ramp period, not a steady-state evaluation. Gaps are primarily domain-driven, not skill-driven.

## b. Dimension assessment

| Dimension | Level 4 Expectation | Q2 Evidence | Level 5 Requirement | Rating |
|---|---|---|---|---|
| Scope | Works independently; proposes new techniques; coordinates as team lead; mentors new members | Works independently on assigned work. Jinja2 migration and Review Apps spikes show initiative to propose new techniques. Not yet coordinating as team lead or mentoring - expected for ramp period. | Sets mid-term objectives aligned to RH business goals. Drives vision with cross-functional impact. | Building toward level |
| Complexity | Independent judgment on varied, non-routine projects. Expert within team. Leads cooperative efforts. | Good judgment on moderately complex issues (VHCL-005, AIB CI fix). Still developing domain expertise across automotive toolchain. 15 channels shows healthy relationship breadth for 2.5 months. | SME advising functional leaders on strategy. Formal networks across RH. | Building toward level |
| Impact | Contributes to functional goals. Decisions impact customer/operational/program objectives. Begins to serve as project lead. | Contributes through task completion: 6 tickets resolved including 2 Major. Custom-images, toolchain-chatbot, dashboard, CI, CloudFront - meaningful breadth. Impact is task-level, appropriate for ramp. | Directly impacts medium-to-long-term results and strategy. | Building toward level |

## c. Competency readiness

| Competency | Expected | Assessment | Evidence |
|---|---|---|---|
| Red Hat Multiplier | Experienced | Building toward level | NHCE participant (Raleigh). 15 channels shows engagement. Still establishing community presence in new domain |
| Strategic | Experienced | Building toward level | 2 spikes (jinja2, Review Apps) show strategic investigation instinct. Needs domain depth before strategic contribution is possible |
| Influence | Experienced | Building toward level | 148 Slack messages across 15 channels in 2.5 months - good relationship building. "Gracefully withdraws proposals when stronger arguments presented" shows collaborative influence style |
| Execution | Advanced | Building toward level | 6 tickets resolved, 4 internal + 3 external MRs. Solid for ramp period. Not yet at the sustained high-volume delivery expected at Advanced |
| Team Advocate | Experienced | Solidly at level | Alert channel monitoring (12 msgs in alerts-auto-toolchain). NHCE participation. Collaborative investigation style |
| Problem Solving | Advanced | Building toward level | VHCL-005 critical container vulnerability fix demonstrates security problem-solving. "Thinks out loud during debugging, narrates full investigation including dead ends" - thorough diagnostic approach |
| Customer Focus | Advanced | Building toward level | Work touches customer-facing infrastructure (CloudFront, custom-images) but no direct customer engagement visible yet |
| Continuous Learning | Experienced | Solidly at level | Multi-domain ramp across custom-images, chatbot, dashboard, CI, CloudFront in 2.5 months. Absorbing new domain actively |

## d. Strengths to leverage

1. **Investigative thoroughness.** Matt "thinks out loud during debugging, narrates full investigation including dead ends." This transparency is valuable for SRE work where understanding the full problem space matters more than the first plausible fix. It also builds team knowledge passively.
2. **Collaborative influence style.** "Gracefully withdraws proposals when stronger arguments presented" signals intellectual honesty and ego-free collaboration. This is a strong foundation for the cross-team influence Level 4 SRE requires.
3. **Breadth of engagement.** 15 channels and work spanning custom-images, toolchain-chatbot, dashboard, CI, and CloudFront in 2.5 months shows a healthy appetite for domain breadth. This is the right ramp behavior for an SRE building system-wide understanding.

## e. Growth opportunities

1. **Deepen domain expertise in one critical system.** Pick one of custom-images, CI pipeline, or infrastructure monitoring and become the team's go-to expert. Level 4 SRE expects "expert within team." Maps to: Infra and monitoring improvements priority.
2. **Own the Review Apps investigation end-to-end.** The spike was a good start - turn it into a proposal, implementation plan, and delivery. This builds the Level 4 "proposes new techniques and methods" signal with concrete follow-through. Maps to: Test Console improvements priority.
3. **Build alert response runbooks.** Matt's 12 messages in alerts-auto-toolchain and his diagnostic narration style are a natural fit for creating SRE runbooks. This documents institutional knowledge and builds Level 4 "mentors new members" signal. Maps to: Infra and monitoring improvements priority.
4. **Increase ticket volume and complexity.** 6 tickets in 2.5 months is appropriate for ramp, but Q3 should show acceleration toward the sustained delivery Level 4 expects. Target 10-15 tickets with at least 2-3 at Major/Critical complexity.

## f. 1:1 talking points

1. You've been here about 2.5 months now. What parts of the ATC infrastructure feel clear to you, and where do you still feel like you're mapping the territory?
2. The jinja2 and Review Apps spikes show good investigative instinct. Which of those (or something else) would you want to own as a full project?
3. Your debugging narration style is something the team benefits from. Have you thought about turning that into written runbooks or incident documentation?
4. What's your sense of the biggest reliability risks in our infrastructure right now? (Testing SRE instinct and domain absorption)
5. What would help you ramp faster - more pairing, more independent exploration, or something else?

## g. Recommended next steps

1. **Select a primary system to own** - recommend infrastructure monitoring or CI pipeline as the deepest-engagement area for Q3. Build expert-level knowledge and become the team's first call for that system. Maps to: Infra and monitoring improvements priority.
2. **Convert the Review Apps spike into an implementation proposal** with scope, timeline, and success criteria. Present to the team. Builds Level 4 "proposes new techniques" signal. Maps to: Test Console improvements priority.
3. **Create SRE runbooks for the top 3 alert types** in alerts-auto-toolchain. Documents Matt's diagnostic approach and builds mentoring artifacts. Maps to: Infra and monitoring improvements priority.
4. **Target 10-15 tickets in Q3** with deliberate complexity escalation - seek out at least 2-3 Major/Critical items to demonstrate independent judgment on non-routine problems.
5. **Shadow a CTC release cycle** end-to-end to build understanding of how SRE infrastructure supports the release process. Builds cross-functional awareness needed for Level 4 Impact. Maps to: Prepare CDN repo and Errata config for 2.0.z priority.

---

## Disconfirmation gate

- **What would change this assessment?** If Matt has significant prior SRE experience in adjacent domains (e.g., container platforms, CI/CD at scale) that transfers directly, the "Building toward level" ratings may understate his readiness. The 1:1 should explore his prior role depth. If the VHCL-005 fix required deep container security expertise rather than straightforward patching, Problem Solving may deserve a higher rating.
- **Critical note:** Assessment gaps are primarily domain ramp, not skill gaps. Matt is a new hire building context in a specialized domain. The trajectory matters more than the snapshot. A follow-up assessment at 6 months (October 2026) would provide a more meaningful baseline.
- **Blind spots:** No visibility into Matt's prior career depth, conference talks, open-source contributions, or mentoring history from previous roles. These could significantly change the competency readiness picture. Ask in 1:1.
