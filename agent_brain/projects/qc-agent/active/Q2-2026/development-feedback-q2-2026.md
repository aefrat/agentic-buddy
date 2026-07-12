# Development Feedback & Growth Paths - Q2 2026

**Period:** Q2 2026 (April 1 - June 30)
**Generated:** 2026-06-29
**Sources:**
- [Software Engineer (IC) Progression Matrix - April 2026](https://docs.google.com/spreadsheets/d/1OAjiTMCBJ4YkBqfh69JwEgW81BJLbAeU8GWanYYCE_4/edit?gid=798132925)
- [SRE (IC) Progression Matrix - April 2026](https://docs.google.com/spreadsheets/d/1Fcr_ZMjT1hq7CANLFYSRE_9gp0Qcs897rfB-8kpx5PI/edit?gid=1708656902)
- [Quality Engineer (IC) Progression Matrix - April 2026](https://docs.google.com/spreadsheets/d/11MXcG53p9k6ncsRtxLSF3LuWfne3Z4PL35t1Svps3AM/edit?gid=1630329910)
- [Red Hat Job Leveling Framework - February 2025](file:///home/aefrat/Downloads/Job%20Leveling%20Framework%20PDF_version%20Feb%202025.pdf) (Radford-based, 3 dimensions: Scope, Complexity, Impact)
- [Job Architecture - The Source](https://source.redhat.com/career_and_benefits/red_hats_rewards_portfolio/global_compensation/job_architecture) (June 2026, career track pathway, promotion criteria)
- [Global Engineering Talent Architecture](https://source.redhat.com/departments/products_and_global_engineering/p_and_ge_content/talent_architecture) (skill progression matrices by job family)

---

## Framework

Red Hat uses the Radford leveling methodology. All IC engineers are on the **Professional track**, assessed across three dimensions that increase with level:

- Scope: Functional reach, breadth of responsibility, guidance provided to others
- Complexity: Judgment required, expertise depth, nature of relationships
- Impact: Accountability for results, contribution to strategy, decision consequence

The IC Progression Matrices (per job family) add **10 role-specific responsibilities and skills** on top of these dimensions. Both lenses are used below.

### Level 3 to 4 shift (Senior to Principal)

Level 3 (Senior) to Level 4 (Principal):

- Scope: From "works independently, enhances existing processes, mentors new members" to "sets objectives tied to functional targets, proposes new methods, coordinates team activities"
- Complexity: From "good judgment on moderately complex issues, experienced professional, relationships within discipline" to "independent judgment on complex issues with creative solutions, recognized expert, leads cooperative efforts among teams, min 8 years"
- Impact: From "contributes to team goals through tasks, moderate impact on immediate team" to "contributes to functional goals through operational direction, decisions impact customer/program objectives, begins to serve as project lead"

### Level 4 to 5 shift (Principal to Senior Principal)

Level 4 (Principal) to Level 5 (Senior Principal):

- Scope: From "objectives tied to functional targets, new techniques within function, mentors new members" to "mid-term objectives aligned to RH business goals, drives vision with cross-functional impact, leads professional staff as expert resource, mentors colleagues in own discipline"
- Complexity: From "expert within team/department, leads cooperative efforts among teams, interacts with senior colleagues" to "subject matter expert advising functional leaders and customers on strategy, formal networks across RH to influence priorities, min 12 years"
- Impact: From "functional goals through operational direction, decisions impact program objectives, begins as project lead" to "directly impacts function's medium-to-long-term results and strategy, decisions significantly impact resource allocation, consistently serves as project lead and SME"

## How to read this document

For each team member:
1. **Scope / Complexity / Impact assessment** - where they sit on each dimension relative to their current and next level
2. **Current level expectations** - key responsibilities and skills at their IC level per the progression matrix
3. **Already demonstrating at next level** - where Q2 evidence shows next-level behaviors
4. **Growth areas for next level** - specific gaps between current performance and next-level expectations
5. **Recommended development path** - concrete actions to close those gaps

---

## Senior Software Engineers (IC Level 3 - next: Principal SE, IC Level 4)

### Bella Khizgiyaev - Senior Software Engineer, PitCrew

*Updated 2026-07-12 with self-assessment input. Bella's stated growth area: increasing visibility ("speaking up more in team meetings, planning sessions, community meetings, presenting more during sprint demos"). Self-identified strengths: ownership, collaboration, supporting the team. Career aspiration: grow into senior technical leadership role (long-term 3-5 years).*

**Dimension assessment (Professional Track):**

- Scope [Level 3, trending 4]: Works independently with minimal instruction. Delivers on enhanced processes (CTC reporting, OIDC hardening, Konflux onboarding). Provides guidance within PitCrew. Cross-subsystem reach is becoming a pattern, not occasional: OIDC certificates extended to jumpstarter, Konflux onboarding requires coordination with Release Engineering, demo environment required cross-team hardware negotiation. Helped with Jumpstarter 0.9.0 release (release notes, reviews). Nudging toward Level 4 scope.
- Complexity [Level 3, trending 4]: Good judgment on moderately complex issues (CTC pipeline failures, certificate handling, Konflux productization pipeline adaptation). Recognized as experienced within PitCrew. Konflux onboarding required learning a new system end-to-end and adapting build pipelines - creative problem-solving on non-routine issues. Relationships extending beyond discipline through hardware negotiations, Konflux/RelEng coordination. Approaching Level 4.
- Impact [Level 3-4]: CTC reporting directly impacts release certification - program objectives (Level 4). Konflux onboarding is foundational to RHAS GA - this is business-facing impact. Demo environment enabled customer-facing engagements (Ford, Summit, CES). Operational direction expanding beyond PitCrew scope.

**Current level fit:** Strong. Meeting Level 3 expectations and showing clear Level 4 signals. Independently designs and develops solutions (CTC reporting, OIDC patterns, Konflux pipeline adaptation), owns quality of her code, provides guidance to teammates, contributes to upstream communities, and increasingly takes on cross-component and customer-facing initiatives.

**Already demonstrating at IC Level 4:**
- *Technical Impact (cross-component):* Extended OIDC certificate pattern from builder to jumpstarter - crosses subsystem boundaries. Konflux onboarding spans upstream project, GitOps resources, and Red Hat Release Engineering - multiple components and teams
- *Quality (multi-component):* CTC reporting work touches 9 items spanning pipeline integration, JUnit generation, artifact handling, lease handling, and report aggregation
- *Collaboration (cross-functional):* Opened Ford demo coordination thread bridging PitCrew with external stakeholders. Negotiated hardware loans from kernel-hw team. Koordinated Konflux pipeline with Release Engineering
- *End-to-end ownership:* Demo environment from hardware procurement through configuration to demo readiness. Konflux onboarding from staging experimentation through GitOps setup to pipeline adaptation
- *Release support:* Helped ship Jumpstarter 0.9.0 - release notes, change reviews, general support

**Growth areas for IC Level 4:**
- *Visibility (self-identified):* Bella recognizes this as a growth area and is actively working on it - speaking up more in team meetings, planning sessions, and community meetings, presenting more during sprint demos. Continue this trajectory
- *Mentoring:* Level 4 expects "across teams, coaches and mentors senior engineers." Currently collaborates well within PitCrew but no evidence of coaching others outside the team
- *Business impact articulation:* Level 4 expects "owns and delivers technical initiatives with visible business impact." Konflux and CTC work have significant business impact (RHAS GA, release certification) but she hasn't explicitly positioned them as business-facing initiatives
- *AI tools:* Level 4 expects "evaluates and introduces new AI-driven methodologies." No AI tooling evidence in Q2
- *Knowledge sharing:* Level 4 expects "blog posts, design documents, presents at conferences." Sprint demo presentations are a good start - expand to written artifacts
- *SDLC leadership:* Level 4 expects "leads the definition and implementation of the SDLC for complex multi-component systems." The Konflux productization pipeline work is adjacent to this - formalize it

**Recommended development path:**
1. **Continue increasing visibility** (self-identified priority) - the sprint demo presentations and team meeting participation are the right approach. Next step: present a technical topic to a broader audience (community meeting, cross-team forum) - the Konflux onboarding experience or CTC pipeline architecture would be strong topics
2. **Position Konflux and CTC as business-facing initiatives** - the impact is there but not articulated. Frame Konflux onboarding as "enabling RHAS GA through productization infrastructure" when presenting to leadership
3. **Start mentoring** - pick one junior/mid-level engineer (Muhamad could be a natural fit on the same team) and establish a regular technical mentorship. Share Konflux knowledge with teammates as the pipeline matures
4. **Write one internal article or design document** on a topic she owns (Konflux onboarding journey, CTC reporting architecture). This makes her expertise durable and visible
5. **Explore AI tooling** - try using AI agents or code-generation tools for testing or debugging work and share findings with the team
6. **Formalize the Konflux pipeline work as SDLC leadership** - document the build pipeline standards and productization requirements as a process that others can follow

---

### Eitan Raviv - Senior Software Engineer, ATC

*Updated 2026-06-29 with self-assessment input. Eitan's stated development trajectory: "continued hands-on work, with an inclination to go deep into an area in order to enhance it."*

**Dimension assessment (Professional Track):**

- Scope [Level 3, with Level 4 signals]: Works independently across broad infrastructure domain (AWS, CloudFront, CI/CD, monitoring, security). GitLab runner consolidation is a clear Level 4 behavior - proposed a new technique (pipeline pooling) based on business context (cost reduction) with impact within the function. AI tooling adoption (claude-code hooks/skills) shows "proposing new methods." Gator sessions with Hubert and Distribution Focus area help show cross-scope willingness.
- Complexity [Level 3, trending 4]: Navigated 5+ external organizational channels (PSCA, IT Cloud, GRC, BOA) - this breadth of relationship exceeds Level 3's "within discipline." Built reusable AI tools (hooks, skills) rather than one-off usage - creative problem-solving characteristic of Level 4. Not yet recognized as expert leading cooperative efforts.
- Impact [Level 3, with Level 4 data points]: Runner consolidation delivered measurable budget savings - impacts operational objectives beyond immediate team (Level 4). CPPX ticket affects customer-facing outcomes. Monitoring SLA criticality tiers shape how the broader team prioritizes incident response. Infrastructure work keeps release pipeline secure and operational.

**Current level fit:** Meeting expectations and showing emerging Level 4 signals. Strong in infrastructure ownership, security compliance, cross-organizational navigation, cost optimization, and AI tooling adoption.

**Already demonstrating at IC Level 4:**
- *Business impact:* GitLab runner consolidation delivered measurable EC2 cost savings - "visible business impact initiative" (Level 4 SE progression)
- *AI methodology:* Built reusable claude-code hooks and skills (Jira ticket creator, GitLab MR fetcher, notification hook) - approaching "evaluate and introduce new methodologies" (Level 4)
- *Cross-team collaboration:* Navigated 5+ external channels, jumped into Distribution Focus area for urgent work, conducted Gator sessions with Hubert
- *Monitoring initiative:* Criticality tiers in monitoring SLA specification is a system-design initiative that spans the team
- *Communication:* Multi-channel incident communication pattern (advance notice, status, all-clear) demonstrates leadership communication

**Growth areas for IC Level 4:**
- *Technical scope:* Runner consolidation touched cross-subsystem (SOA + Services + Gating + pipe-x + Jumpstarter), but most work remains subsystem-level infrastructure. Level 4 expects leading design of cross-component features
- *Quality practices:* Added integration tests for s3pi (own code quality). Level 4 expects establishing/monitoring testing practices for multiple teams
- *Mentoring breadth:* Gator sessions with Hubert (new member) meet Level 3. Level 4 expects coaching/mentoring senior engineers across teams
- *Community engagement:* Active contributor across 14 Slack channels but not yet a recognized community leader
- *Knowledge sharing:* No blog posts, design documents, or conference presentations evident this quarter
- *SDLC leadership:* Champion for infra practices within team. Level 4 expects leading SDLC definition for multi-component systems

**Self-assessment alignment:** Eitan identifies his trajectory as "continued hands-on work, with an inclination to go deep into an area in order to enhance it." This aligns naturally with the infrastructure depth he already demonstrates (s3pi performance + testing + debt reduction, CloudFront module extensions, monitoring SLA tiers). The recommended development path below channels this depth-oriented inclination toward Level 4 impact by ensuring his deep-dive improvements are formalized, shared, and positioned as functional-level contributions.

**Recommended development path:**
1. **Formalize and share the AI tooling work** - the claude-code hooks and skills are exactly Level 4's "evaluate and introduce new methodologies." Share with the team, document workflow improvements, propose adoption patterns. This turns personal depth into team-wide methodology introduction - directly aligned with Eitan's stated inclination to "go deep and enhance"
2. **Lead a cross-component design initiative** - the monitoring criticality tiers and runner consolidation are strong foundations. Expand the runner consolidation into a formal CI/CD optimization strategy with documented design decisions and cost impact analysis. Present to stakeholders
3. **Mentor newer team members** on infrastructure and AWS patterns. Matt Goldman and Hubert Stefanski, who touch similar infrastructure, would benefit from Eitan's deep operational knowledge. The Gator sessions are a good start - expand to regular knowledge-sharing sessions
4. **Document infrastructure decisions** - write internal design documents or blog posts for key infrastructure choices (runner consolidation cost savings, CloudFront architecture, s3pi optimization patterns). This builds the knowledge-sharing and expert recognition needed at Level 4
5. **Engage with SRE or infrastructure communities** at Red Hat - contribute patterns or tools to internal SRE forums. Eitan's depth-first approach would produce valuable, detailed content

---

### Hubert Stefanski - Senior Software Engineer, ATC (transitioning to PitCrew)

**Dimension assessment (Professional Track):**

- Scope [Level 3, trending 4]: Works independently with deep expertise. Gating work proposes new techniques (dependency triggering, QC LP gating workflow) - this is Level 4 "proposes new methods based on business context." Helped PitCrew design GitLab repo structure (cross-team scope).
- Complexity [Level 3-4 boundary]: Independent judgment on non-routine gating issues. Recognized as experienced across infrastructure and gating. Productive relationships across multiple teams (PitCrew, CAT, ITSEC) - moving beyond "within discipline." 18 channels. Min 5 years met.
- Impact [Level 3, trending 4]: Gating improvements impact team's release quality (team goals). Infrastructure decisions affect multiple downstream consumers. Starting to impact functional objectives through gating reliability.

**Current level fit:** Strong. Exceeds Level 3 expectations in several areas. 400+ Slack messages across 18 channels shows exceptional transparency. Infrastructure anchor for ATC with deep gating expertise.

**Already demonstrating at IC Level 4:**
- *Technical Impact (cross-component):* Gating work inherently crosses subsystems - dependency triggering, multiple kernel variants, QC LP gating workflow. This is Level 4 scope
- *Communication:* "Approaches Advanced" transparency per QC assessment. Proactive @channel notices, openly narrates debugging, candidly acknowledges mistakes. This exceeds Level 3 and meets Level 4
- *Collaboration (cross-team):* Helped PitCrew design GitLab repo structure, shared terraform modules with other teams, fielded S3 access questions from CAT
- *Mentoring indicators:* Shares recommendations proactively (ITSEC, terraform), though not formalized as mentoring

**Growth areas for IC Level 4:**
- *Technical strategy ownership:* Level 4 expects "leads the design and development of software solutions for features that cross multiple subsystems." Hubert does this reactively (fixing gating gaps) but needs to own a strategic initiative proactively
- *Business impact:* Level 4 expects "owns and delivers technical initiatives with visible business impact, enabling the entire team to deliver value." His gating work enables this but isn't positioned strategically
- *AI tools:* Level 4 expects "evaluates and introduces new AI-driven methodologies." No AI tooling evidence in Q2
- *Knowledge sharing formalization:* Level 4 expects "blog posts, design documents." His knowledge sharing is real-time (Slack) but not durable (no articles/docs)
- *Community leadership:* Level 4 expects "key representative and leader within the community." Active across channels but not in a formal community leadership role

**Recommended development path:**
1. **Own a strategic initiative** - as he transitions to PitCrew, lead the design of a cross-team capability (e.g., gating strategy for RHIVOS LP, or infrastructure patterns for jumpstarter). Frame it as a technical initiative with business impact
2. **Formalize knowledge sharing** - convert his deep gating and infrastructure knowledge into design documents or internal blog posts. He already communicates well in Slack; writing it up makes it durable and counts toward Level 4
3. **Establish mentoring relationships** - with the PitCrew transition, he can mentor PitCrew members on infrastructure patterns and gating expertise. Formalize this
4. **Explore AI tooling** for infrastructure operations, gating, or pipeline automation
5. **Position for business impact** - when proposing gating improvements, explicitly tie them to release velocity or quality metrics that leadership cares about

---

### Kanitha Chim - Senior Software Engineer, ATC

**Dimension assessment (Professional Track):**

- Scope [Level 3-4 boundary, strong]: Works independently on complex distribution workflows. Broadest channel reach on team (25 channels). Cross-team coordination spanning 4 Jira projects (VROOM, RHELDST, RHELWF, PSSECAUT) - this exceeds Level 3's "within discipline" scope. The distribution/release work is functional-level, not just team-level. Additionally serves as ATC Technical Product Owner (TPO) - setting 6-month team priorities, leading focus area brainstorms, and representing ATC on program calls alongside Area PO Petr Sabata.
- Complexity [Level 3, trending 4]: Resolves moderately complex issues (errata, CDN propagation failures, product listing). Cross-team relationships are productive and extend well beyond own team. QMS ISO 26262 Part 8 audit SME work (Configuration Management, Confidence in Tools) demonstrates capacity for cross-org responsibility in an unfamiliar domain. Acts as de facto distribution expert and TPO - team independently named the role.
- Impact [Level 3-4 boundary, strong]: Distribution work contributes directly to release readiness - customer-facing impact. Product listing and CDN decisions affect whether customers can download RHIVOS. TPO role directly shapes team direction and program alignment. QMS audit work impacts organizational certification. This touches "customer, operational, or program objectives" (Level 4).

**Current level fit:** Strong, approaching IC-4. Broadest Slack reach on the team (25 channels). Distribution and release readiness specialist. ATC Technical Product Owner (TPO). QMS ISO 26262 audit SME. Strong cross-organizational coordination.

**Already demonstrating at IC Level 4:**
- *Cross-component scope:* Distribution work inherently spans errata, CDN, product listing, compose, and advisory systems - multiple subsystems, Level 4 scope
- *Cross-team coordination:* Drove cross-team fix when product IDs failed to propagate, spanning VROOM, RHELDST, RHELWF, PSSECAUT. This is Level 4 collaboration
- *Communication with stakeholders:* Proactively clarified RC3 trigger conditions, surfaced stale product listing issues - leadership-level communication
- *Process understanding:* Deep understanding of release engineering processes and where they break
- *TPO leadership (added 2026-07-12):* Bridges RHIVOS program priorities to ATC team execution. Sets 6-month team priorities, leads focus area brainstorms, represents ATC on program calls. Manager defers prioritization to "kchim and contyk (The POs)." Team members independently recognized and named the TPO role. This is a leadership function beyond IC-3 SE job description
- *QMS cross-org coordination (added 2026-07-12):* Voluntarily served as SME for TUV SUD certification audit outside core role. Prepared and presented audit materials, coordinated with 6+ stakeholders across RHIVOS teams. Demonstrates cross-org ownership on a critical program initiative

**Growth areas for IC Level 4:**
- *Technical design leadership:* Level 4 expects "leads the design and development of software solutions." Kanitha excels at process execution, coordination, and TPO-level prioritization but needs to lead a formal technical design initiative (design doc, architectural decisions)
- *Mentoring:* Level 4 expects "across teams, coaches and mentors senior engineers." Mentoring opportunity exists with new team member joining distribution
- *AI tools:* The "Agentic AI for advisory workflow" spike is promising but needs follow-through. Level 4 expects "evaluates and introduces new AI-driven methodologies"
- *Knowledge sharing:* Level 4 expects "blog posts, design documents, presents at conferences." No formal writing or presentations yet - distribution expertise is currently held in Slack threads and tribal knowledge
- *SDLC ownership:* Level 4 expects "leads the definition and implementation of the SDLC for complex multi-component systems." She follows release processes expertly but hasn't led their definition

**Recommended development path:**
1. **Lead a design initiative** - the QC LP distribution workflow spike and the AI advisory workflow spike are both natural candidates. Pick one and drive it from spike to design document to implementation. The 2.0.z CDN/Errata design is the strongest option given her TPO role
2. **Document the release pipeline** - Kanitha has the deepest knowledge of RHIVOS distribution. A formal design document of the release workflow (errata, CDN, product listing, gating) would be high-value and demonstrate Level 4 knowledge sharing
3. **Follow through on AI for advisories** - the spike shows initiative. Develop it into a concrete proposal, evaluate tools, and present findings to the team
4. **Formalize distribution mentoring** - with new team member joining distribution area, structure knowledge transfer sessions. Her unique expertise makes her the natural mentor
5. **Propose process improvements** - move from executing release processes to improving them. Leverage TPO perspective to identify and drive systematic fixes to release bottlenecks

---

### Muhamad Abo Ras - Senior Software Engineer, PitCrew

*Updated 2026-07-12 with self-assessment input. Muhamad's self-identified strengths: execution consistency (10/12 PRs merged), end-to-end ownership (filing issues to closing the loop), cross-team collaboration (reviewing jumpstarter core alongside operator work).*

**Dimension assessment (Professional Track):**

- Scope [Level 3, with Level 4 signals]: Works independently on testing infrastructure. Delivers on enhanced processes (production-grade e2e architecture, smoke lane, composite GH Actions). Self-input reveals broader scope than initially captured: active code reviewer across two repos (automotive-dev-operator + jumpstarter core), cross-team review contribution. ArgoCD/GitOps work expands beyond testing domain. The e2e testing architecture is effectively a platform initiative (lane architecture, log collection, CI observability) - approaching "proposes new methods" (Level 4).
- Complexity [Level 3]: Good judgment on moderately complex issues (OIDC e2e, Kind-to-CRC migration, multi-lane test architecture design). Productive relationships within own team + jumpstarter core reviewers. 38 Slack messages across 7 channels remains the lowest visibility, though GitHub-based cross-team activity (jumpstarter core reviews) is more significant than Slack alone suggests. Approaching "recognized as experienced" but needs broader relationship network.
- Impact [Level 3, trending 4]: Contributes to team goals through completion of testing tasks. Self-input reveals greater impact than initially assessed: production-grade e2e suite reduced contributor friction (shortening PR feedback loops), eliminated test coverage blind spots in auth and bootc paths, made CI failures significantly easier to diagnose. The smoke lane as default PR gate directly impacts developer productivity across the project. High execution quality (10/12 PRs merged) demonstrates consistent delivery impact.

**Current level fit:** Meeting expectations and showing emerging Level 4 signals. Solid engineering work on testing infrastructure with strong execution consistency. Self-input reveals a more complete picture: end-to-end ownership pattern, cross-team review activity, and CI/CD engineering skills (composite GH Actions, log collection, observability) that go beyond testing into platform engineering.

**Already demonstrating at IC Level 4:**
- *Quality ownership:* Production-grade e2e testing infrastructure - multi-lane architecture, smoke PR gate, centralized log collection, OIDC e2e tests - demonstrates quality system thinking well beyond individual features
- *Technical design:* Lane architecture (operator, bootc, auth), composite GitHub Actions (setup, collect-logs, cleanup), centralized observability - this is platform design, not just test writing
- *Cross-team contribution:* Active reviewer on jumpstarter core PRs alongside operator work. End-to-end ownership from filing issues (#322) to writing fixes (#323) to closing the loop
- *CI/CD engineering:* Extracted reusable CI patterns, built downloadable diagnostic artifacts, implemented PR-triggered test tiers - Level 4 "proposes new methods based on business context"

**Growth areas for IC Level 4:**
- *Visibility and communication:* 38 Slack messages across 7 channels remains the lowest on either team. Level 4 expects "effectively communicates with leadership and stakeholders." The technical work is strong - but if people don't know about it, it can't influence decisions or inspire adoption. Need significantly more visibility
- *Cross-component scope beyond reviews:* Jumpstarter core code reviews are a good signal but Level 4 expects "leading design of features that cross multiple subsystems or components" as a primary contribution, not just review participation
- *Mentoring:* Level 4 expects "across teams, coaches and mentors senior engineers." No mentoring evidence. Room to grow in "initiating broader design discussions" (noted in QC)
- *Community engagement:* Level 4 expects "key representative and leader within the community." Very limited Slack presence outside immediate team
- *AI tools:* Level 4 expects "evaluates and introduces new AI-driven methodologies." No AI tooling evidence
- *Knowledge sharing:* No blog posts, design documents, or presentations. The e2e testing architecture is exactly the kind of work that deserves a design doc
- *Business impact articulation:* The testing work has real business impact (contributor productivity, CI reliability, coverage gaps eliminated) but hasn't been articulated or positioned as business-facing

**Recommended development path:**
1. **Increase visibility** - this remains the highest-priority growth area. The self-input reveals impressive technical work that deserves more visibility. Post more proactively in team channels: share design decisions, debugging findings, testing architecture improvements. Present the e2e lane architecture at a sprint demo or team meeting
2. **Document the e2e testing architecture** - write a design document for the production-grade e2e framework (lane architecture, smoke gate, composite actions, log collection). This is the single highest-leverage action: it makes the work visible, shareable, and promotable. It also enables mentoring (others can learn from the document)
3. **Position testing work as business impact** - frame the e2e infrastructure as "reduced contributor friction by X%, eliminated auth/bootc blind spots, cut CI debugging time" when presenting to leadership. The self-input has the right language - use it
4. **Expand scope beyond builder testing** - the ArgoCD/GitOps work is a good start. Look for testing needs across PitCrew that require coordination with other teams. Position the composite GitHub Actions as reusable across repos
5. **Start mentoring** - the testing architecture documentation (point 2) is a natural mentoring vehicle. Help onboard someone on PitCrew's testing infrastructure or share testing patterns with ATC
6. **Engage in broader channels** - join #forum-jumpstarter, #forum-qe-automotive, and contribute to discussions. Level 4 expects community engagement
7. **Explore AI tools** for test generation, test result analysis, or CI optimization

---

## Principal Software Engineers (IC Level 4 - next: Senior Principal SE, IC Level 5)

### Juanje Ojeda - Principal Software Engineer, ATC

**Dimension assessment (Professional Track, Radford + Enterprise Competencies):**

- Scope [Stretching toward Level 5]: Sets and achieves objectives tied to functional targets (Level 4 - met). Agent Forge proposes new techniques adopted cross-team. Execopen pipeline spanned 5 repos with FoA coordination. Mentored Matt Goldman. Led pipelines-debugger from PoC to production adoption. Published articles on Red Hat Source and LinkedIn. Level 5 expects "mid-term objectives aligned to RH business goals, drives vision with cross-functional impact, leads professional staff as expert resource" - he's demonstrating most of this but hasn't yet positioned work as organizational strategy.
- Complexity [Stretching toward Level 5]: Independent judgment on complex, non-routine issues (6 Blockers resolved, creative agent solutions). Recognized as expert within team and increasingly across department. Leads cooperative efforts among 5+ teams for execopen. Cross-team relationships with FoA, QE, AIB. Engaged across #forum-ambient-code-platform, #forum-qe-automotive. Level 5 expects "formal networks across Red Hat to influence priorities and objectives both internally and with customers" - the #forum engagement is a start, not yet an established cross-org network.
- Impact [Gaps to address]: Contributes to functional goals through operational direction (release pipeline, agent infrastructure). Decisions impact customer and program objectives (RC1-RC3, CTC). Agent Forge emerging as reusable methodology. 28 tickets, 39 MRs. Level 5 expects "activities directly impact function's medium-to-long-term results and strategy, decisions significantly impact resource allocation" - impact remains primarily functional/tactical, not yet organizational-level strategic direction.

**Enterprise Competency Readiness (IC Level 4 expectations, source: Competency Proficiency Levels by Job Levels, March 2022):**

| Competency | Expected | Assessment | Evidence |
|-----------|----------|------------|----------|
| Red Hat Multiplier | Experienced | At/above | 711 Slack messages, cross-team community building around AI agents, articles published, demos to broader org |
| Strategic | Experienced | At/above | Agent Forge as reusable strategy, technical vision for AI-driven engineering, execopen architecture decisions |
| Influence | Experienced | At/above | Cross-team adoption of agent patterns (Ozan, Ian, Kanitha), articles on Red Hat Source, AAA and Rollup Demo presentations |
| Execution | Advanced | At level | 28 tickets (6 Blockers), RC1-RC3 release pipeline kept operational, pac-jobs Phase 3 completed. Not yet driving execution at multi-team/department scope |
| Team Advocate | Experienced | At level | Matt Goldman onboarding, cheatsheets, wiki generation, MR reviews. Connecting colleagues to domain experts |
| Problem Solving | Advanced | At level | Complex pipeline diagnoses, AI agent solutions to systemic problems. Approaches Advanced in creative problem-solving but "building through programs and systems" (Expert-level) still emerging |
| Customer Focus | Advanced | Below expected | No direct customer-facing evidence this quarter. Internal stakeholder coordination is strong, but external customer engagement is not visible |
| Continuous Learning | Experienced | Above expected | Multi-agent memory research (VROOM-41514), Agent Forge design principles research with prior art analysis, published articles - approaches Advanced |

Summary: 5 of 8 competencies at or above expected proficiency. Customer Focus (Advanced expected) is the main gap.

**Current level fit:** Exceeds expectations. Comfortably operating at Level 4 with multiple areas of Level 5 behavior already evident. 28 tickets (6 Blockers), 39 MRs, 711 Slack messages - output and influence significantly exceed Level 4 norms.

**Already demonstrating at IC Level 5:**
- *AI innovation leadership:* Pipelines-debugger, CTC agent, Agent Forge, Pi extensions, CI infrastructure for agent skills. Cross-team adoption happened organically. This is the strongest evidence of Level 5 "drives the strategy and best practices for integrating advanced AI ecosystems at scale"
- *Transparent, public-first communication:* 711 Slack messages with a consistent pattern of surfacing reasoning, blockers, and context in open channels. In #alerts-auto-toolchain he narrates his diagnostic process so others can learn. This teaches the team how to think about problems, not just what the answer is - a force multiplier
- *Cross-team enablement through tooling:* Agent Forge, codebase-documenter skill, wiki-kb skill, Pi npm packages, CI job templates - Juanje builds things others pick up and extend. This "build once, multiply across the org" instinct is exactly what Level 5 demands for organizational impact
- *Technical strategy across teams:* Agent Forge is a reusable framework adopted cross-team. Execopen pipeline integration spanned 5 repositories with FoA coordination. Level 5: "drives the technical strategy and design of software solutions across multiple subsystems, influencing the overall architecture"
- *Knowledge sharing and mentoring:* Published articles, AAA Sprint 5 and Rollup Demo. Matt Goldman onboarding with cheatsheets, wiki generation, MR reviews. Cross-team adoption of agent patterns (Ian, Kanitha building their own). Level 5: "coaches and mentors principal engineers and role models mentorship for the organization"

**Disconfirmation gate (assessed 2026-06-29):**

Question: Is Juanje ready for promotion to IC Level 5?

Contradicting evidence sought and found:
- Impact remains primarily functional/tactical, not yet organizational-level strategic direction. Agent Forge has organizational potential but hasn't been positioned or recognized as organizational strategy
- Customer Focus at Advanced is unmet - no external customer engagement evidence
- External conference presentations are missing - internal demos are strong but Level 5 expects external visibility
- Cross-org influence is emerging but not yet "formal networks across Red Hat to influence priorities." The #forum-ambient-code-platform engagement is a start, not an established network
- Sustained consistency is unproven - Level 5 behaviors emerged in Q2 but need to be demonstrated consistently over multiple quarters

Conclusion: Not yet ready for promotion. Juanje is on a clear trajectory from Level 4 to Level 5, with multiple Level 5 behaviors already demonstrated. The gaps are specific and addressable: organizational-level impact positioning, external visibility, cross-org network formalization, and customer-impact articulation. With deliberate action on 2-3 of these areas over the next 1-2 quarters, the promotion case would be substantially stronger.

**Growth areas for IC Level 5:**
- *Position AI work as organizational strategy (Impact):* Level 5 expects "activities directly impact function's medium-to-long-term results and strategy." Agent Forge and the pipelines-debugger have real organizational value but are currently framed as team-level tooling. A proposal positioning the agent practice as an engineering methodology for the broader organization - with business impact language (incident resolution time reduction, engineering velocity, knowledge capture ROI) - would shift impact from functional-level to organizational-level
- *Build formal networks beyond Automotive (Complexity):* Level 5 expects "formal networks across Red Hat to influence priorities and objectives both internally and with customers." Deepening relationships with engineering leaders in other BUs (RHEL Platforms, Ansible, Hybrid Platforms) who might adopt agent patterns would strengthen this. Current influence sphere is primarily Automotive
- *Present at external conferences (Scope):* Level 5 expects "frequently presents at technical conferences, often to larger audiences." An external talk - DevConf, Red Hat Summit, or an open source CI/CD conference - would demonstrate the "expert regional or functional resource" scope expected at Level 5
- *Articulate customer-facing impact (Customer Focus):* The one competency below expected proficiency for IC Level 4. Connecting infrastructure work to customer outcomes - pipeline reliability enabling faster customer-facing releases, FuSa traceability meeting automotive compliance - would address this gap
- *Document SDLC methodology change (Scope):* Level 5 expects "drives the evolution of the SDLC within the organization." Write a design doc describing how agent-driven pipeline diagnosis changes the SDLC: from manual log reading to agent-first triage, from tribal knowledge to file-based KB. Position as methodology innovation

**Recommended development path:**
1. **Write a strategic proposal for the agent practice** - 2-3 page document positioning Agent Forge and the pipelines-debugger as an engineering methodology for the organization. Include business metrics (incident resolution time before/after, engineering hours saved). Present to leadership. Addresses: Impact dimension, Strategic competency, business acumen
2. **Submit a conference proposal** - DevConf.cz or Red Hat Summit. Topic: "AI Agents for CI/CD Pipeline Diagnosis: From Idea to Production in One Quarter." Addresses: Scope dimension, Influence competency
3. **Establish a cross-org consulting relationship** - identify 1-2 teams outside Automotive exploring AI agents. Offer to consult on their agent design. Addresses: Complexity dimension, cross-org mentoring
4. **Connect technical work to customer outcomes** - explicitly articulate how pipeline reliability enables faster customer-facing releases, how FuSa traceability meets automotive compliance, how agent-driven triage improves SLAs. Addresses: Customer Focus competency, Impact dimension
5. **Document SDLC methodology change** - short internal article or design doc on how agent-driven pipeline diagnosis changes the SDLC. Position as methodology innovation. Addresses: Scope dimension (Level 5: "drives the evolution of the SDLC within the organization")

*Full development brief with 1:1 talking points: `agent_brain/projects/talent-architecture/active/juanje.ojeda/2026-06-29-development-brief.md`*

---

### Benny Zlotnik - Principal Software Engineer, PitCrew

**Dimension assessment (Professional Track):**

- Scope [Level 4]: Works independently to achieve objectives across all PitCrew workstreams. De facto first responder in jumpstarter community (281 messages in #forum-jumpstarter). Proposes and delivers new methods (CA support for u-boot, OCI flashing, Vault migration). Coordinates others reactively through community engagement. Needs to shift from reactive to directive to reach Level 5 "drives vision and innovation."
- Complexity [Level 4, trending 5]: Independent judgment on complex, varied issues spanning every PitCrew workstream. Recognized as expert within PitCrew and the jumpstarter ecosystem. Leads cooperative efforts among teams (897 msgs, 17 channels). Cross-team relationships are strong. Approaching Level 5's "formal networks across Red Hat to influence priorities" - already acts as a connective hub.
- Impact [Level 4]: Contributes to functional goals through broad operational delivery. Decisions impact program objectives (jumpstarter releases, security, CTC). Not yet at Level 5 "directly impacts function's medium-to-long-term results and strategy" - his impact is tactical breadth rather than strategic direction.

**Current level fit:** Strong. Highest ticket throughput (30 closed), broadest community connector on PitCrew (897 Slack messages, 17 channels). "Connect" behavior at Advanced level per QC assessment.

**Already demonstrating at IC Level 5:**
- *Community leadership:* De facto first responder in #forum-jumpstarter (281 messages). Active across #forum-rhivos-dut, #forum-qe-automotive. Level 5 expects "drives innovation by leading significant product-area initiatives with a community-first mindset." Benny IS the community connective node
- *Technical breadth:* Spans every PitCrew workstream: jumpstarter platform, builder tooling, security, CTC, customer work. Level 5 expects "drives the technical strategy... across multiple subsystems"
- *Knowledge sharing:* Real-time knowledge sharing through Slack (897 messages) - he is the team's knowledge hub

**Growth areas for IC Level 5:**
- *Strategic technical direction:* Level 5 expects "drives the technical strategy and design of software solutions across multiple subsystems, influencing the overall architecture." Benny delivers across all areas but hasn't articulated or led a technical strategy. His work is responsive (fixing, building, supporting) rather than directive (setting direction)
- *Organizational influence:* Level 5 expects influence "across the organization." Benny's influence is strong within PitCrew and the jumpstarter ecosystem but needs to expand to other engineering teams
- *Architecture vision:* Level 5 expects "architects scalable, and fault-tolerant systems that anticipate customer needs." Benny builds and fixes systems but hasn't led an architectural redesign or evolution
- *Written knowledge sharing:* Level 5 expects "design documents, blog posts, frequently presents at technical conferences." Benny's knowledge sharing is all real-time in Slack. He needs durable artifacts
- *Mentoring:* Level 5 expects "across organizations, coaches and mentors principal engineers." Benny pulls others into problem-solving (good) but doesn't have formal mentoring relationships
- *AI leadership:* Level 5 expects "drives the strategy and best practices for integrating advanced AI ecosystems." No AI tooling initiative visible
- *SDLC methodology:* Level 5 expects "drives the evolution of the SDLC within the organization." No evidence of process methodology innovation

**Recommended development path:**
1. **Write a technical strategy document** - Benny has the deepest knowledge of jumpstarter and PitCrew systems. Write a 6-month technical roadmap or architecture proposal for jumpstarter evolution. This is the single most important step for Level 5
2. **Formalize knowledge sharing** - convert his Slack expertise into blog posts or design documents. Even one article on jumpstarter architecture or the builder security model would be significant
3. **Present at a conference** - DevConf, Red Hat Summit, or jumpstarter community events. His deep jumpstarter expertise makes him a natural speaker
4. **Establish cross-org mentoring** - mentor someone outside PitCrew on jumpstarter or builder patterns
5. **Explore AI tooling strategy** - evaluate how AI tools could improve PitCrew's workflows (test automation, builder diagnostics) and propose an adoption strategy
6. **Shift from reactive to directive** - instead of responding to all requests, identify and propose the top 3 architectural improvements for PitCrew and drive them proactively

---

### Roderick Kieley - Principal Software Engineer, PitCrew

**Dimension assessment (Professional Track):**

- Scope [Too early]: 21 working days. First code contribution landed. Community engagement in AI/agent forums suggests he will quickly establish Level 4 scope once domain depth is built.
- Complexity [Too early]: Prior career level suggests principal-level judgment and expertise, but RHIVOS domain expertise is still developing. Broad AI/agent community connections signal he will bring cross-functional relationships.
- Impact [Too early]: No Jira tickets yet (expected for onboarding). Impact assessment deferred to Q3.

**Current level fit:** Too early to assess (joined June 1, 21 working days). Early signals are positive: first code contribution within 3 weeks, notably broad Slack presence in AI/agent communities. QC assessment notes trajectory toward Advanced on "Connect."

**Already demonstrating strengths:**
- *Community engagement:* Already in #forum-mcp, #forum-ai-agent-builders, #wg-agent-eval-harness, #appeng-ai5-marketplace, #lounge-homelab - broader AI community engagement than most established engineers
- *Collaborative approach:* 29/44 messages are thread replies (deep engagement, not broadcast). Verifies claims with citations

**Growth areas (focus on establishing Level 4 baseline first):**
- *Domain expertise:* Needs to build deep RHIVOS/automotive domain knowledge. Level 4 expects "expert in multiple areas of the tech stack"
- *Technical delivery:* No Jira tickets yet (expected for onboarding). Needs to establish delivery cadence
- *Cross-component design:* Level 4 expects "leads the design of complex systems that involve multiple components and teams." First need to understand the existing systems

**Recommended development path (Q3 priorities):**
1. **Build domain depth** - take on 3-5 Jira tickets covering different PitCrew workstreams to build breadth
2. **Leverage AI/agent expertise** - Roderick's community presence suggests deep AI/agent knowledge. Apply this to PitCrew-relevant problems (PITCREW-161 AIB prototyping is already assigned)
3. **Establish regular technical contributions** - target a steady cadence of MRs and ticket closures
4. **Find a mentoring partner** - pair with Benny or another senior PitCrew member for domain knowledge transfer
5. **Document as you learn** - onboarding discoveries are valuable. Write up architectural observations for the team

---

## Principal SRE (IC Level 4 - next: Senior Principal SRE, IC Level 5)

### Matt Goldman - Principal SRE, ATC

**Note:** Matt joined April 13 (2.5 months in quarter). Using the SRE IC Progression Matrix and the Professional Track dimensions for his development path.

**Dimension assessment (Professional Track - SRE):**

- Scope [Level 4 (building)]: Works independently on assigned infrastructure and security tasks. Delivers on existing processes (container vulnerabilities, CI fixes). The jinja2 and Review Apps investigation spikes show initiative to "propose new techniques" (Level 4 behavior). Still building domain breadth to fully "set and achieve objectives tied to functional targets."
- Complexity [Level 3-4]: Good judgment on moderately complex issues (security fixes, CI pipeline debugging). Still developing domain expertise to be "recognized as expert." Productive relationships across 15 channels spanning team and broader Red Hat - healthy relationship breadth for ramp period. "Thinks out loud during debugging" shows transparency but also that he's learning publicly - a strength that maps to Level 4 collaborative style.
- Impact [Level 3]: Contributes through completion of tasks. 6 tickets (2 Major) - meaningful but scope is still task-level. Not yet at "operational direction for functional goals" (Level 4). Expected for 2.5 months in role.

**Current level fit (SRE Level 4):** Building toward expectations. Strong start for a new hire. Level 4 SRE expects "managing complex systems and solving intricate problems" and "expert judgment and decision-making." Matt is demonstrating competence but still ramping on domain knowledge.

**Current SRE Level 4 responsibilities and Matt's alignment:**
- *Code and automation:* 7 MRs (4 internal + 3 GitLab.com). Security fixes and CI improvements are good. Meets "lead the development of code and automation scripts" for his ramp period
- *Code reviews and best practices:* Reviews code outside primary expertise, opens companion MRs. Good Level 4 behavior
- *Mentoring:* Too new to mentor others. Level 4 expects "mentor and guide junior engineers"
- *Incident management:* CloudFront domain configuration work shows operational capability
- *Distributed systems:* Still building understanding of RHIVOS/automotive distributed build and test infrastructure

**Already demonstrating strengths:**
- *Transparency:* "Thinks out loud during debugging sessions, narrates full investigation in real time including dead ends" - exceptional Level 4+ communication pattern
- *Collaboration quality:* "Gracefully withdraws proposals when stronger arguments presented" - mature collaborative behavior
- *Initiative:* Jinja2 investigation spike and Review Apps investigation show he's looking to improve, not just learn

**Growth areas for SRE Level 5:**
- *Strategic goals:* Level 5 expects "set strategic goals for the SRE team, aligning with Red Hat's business objectives." Too early for this - needs domain depth first
- *Technical leadership in incident response:* Level 5 expects "provide technical leadership in incident response, root cause analysis, and implementation of long-term solutions." Needs more incidents under his belt
- *Cross-functional liaison:* Level 5 expects "act as a liaison between SRE teams and other engineering groups." Needs deeper relationships across teams
- *Best practices leadership:* Level 5 expects "lead the adoption of industry best practices in site reliability, automation, and operational excellence." Needs to establish track record first
- *Continuous improvement at scale:* Level 5 expects "oversee the continuous improvement of monitoring, alerting, and response systems"

**Recommended development path (Q3-Q4 focus):**
1. **Deepen domain expertise** - own a major infrastructure component end-to-end (custom-images is a natural fit based on Q2 work). Understand the full pipeline from build to release
2. **Lead one reliability improvement** - pick an operational pain point (CI reliability, monitoring gaps, deployment process) and drive it from diagnosis to solution
3. **Build cross-team relationships** - engage more with Eitan (shared infrastructure domain), Juanje and Roni (pipeline/testing intersections)
4. **Document infrastructure patterns** - the jinja2 investigation and Review Apps spike suggest architectural thinking. Write these up as formal proposals
5. **Establish mentoring** - once domain expertise is solid (Q4), start mentoring newer team members on SRE patterns
6. **Start contributing to SRE community** - join Red Hat internal SRE forums, share learnings from automotive infrastructure

---

## Principal Quality Engineer (IC Level 4 - next: Senior Principal QE, IC Level 5)

### Roni Eliezer - Principal Software Quality Engineer, ATC

**Note:** Using the Quality Engineer IC Progression Matrix and the Professional Track dimensions for Roni's development path.

**Dimension assessment (Professional Track - QE):**

- Scope [Level 4-5]: Works independently to set and achieve objectives (Test Console platform, CTC pipeline, AI analysis). Proposes new techniques (AI-powered test analysis, Gemini transitions, packages.redhat.com PoC) with impact within the function. Coordinates CTC activities for RC1-RC3 as functional team lead. 199 mentions by others - acts as expert resource. Cross-team feedback from Yariv (BOA team) explicitly recognizes Roni as a "vital collaborative anchor" across Toolchain, Jumpstarter, and BoA, with Multiplier behaviors at the Advanced level. Willing to mentor and assist others to begin contributing to Test Console. Approaching Level 5 "drives vision and innovation with cross-functional impact" through Test Console's central role and cross-team enablement.
- Complexity [Level 4, trending 5]: Independent judgment on complex, non-routine issues (3 Gemini model transitions, fallback mechanisms, long-standing Blocker-level security fix). Recognized as expert within team - primary Test Console owner. Productive relationships within function (QE automotive, testing-farm, PitCrew). Leading cooperative efforts across QE teams. BOA team feedback confirms cross-team expert recognition beyond immediate team. Approaching "subject matter expert advising on strategy" (Level 5).
- Impact [Level 4, trending 5]: Contributes to functional goals through operational direction of testing infrastructure. Decisions impact program objectives (CTC certification timeline, release readiness). Serves as de facto project lead for Test Console and CTC pipeline. Through Test Console, scales individual Multiplier behaviors to elevate multiple teams (Yariv: "scales these behaviors to elevate the effectiveness of multiple teams integrated under one product"). Approaching Level 5 "directly impacts function's medium-to-long-term results" - Test Console IS the testing infrastructure strategy.

**Current level fit (QE Level 4):** Exceeds expectations. Highest individual output (32 tickets, 43 MRs). Owns the Test Console platform end-to-end. Leads test automation framework design, coordinates team activities for CTC delivery, and applies creative problem-solving (AI-powered test analysis, Gemini model transitions).

**Current QE Level 4 responsibilities and Roni's alignment:**
- *Test automation frameworks:* Test Console IS the automation framework. Roni designs, builds, and maintains it. Fully meets "lead the design and development of complex test automation frameworks"
- *Team coordination:* Configured TC for RC1/RC2/RC3, prepared reduced test plans, scheduled weekend CTC runs. Meets "coordinate the activities of a team of engineers to ensure successful test delivery"
- *Creative problem-solving:* AI-powered test analysis with 3 Gemini model transitions, fallback mechanisms. Exceeds "apply creative problem-solving to resolve complex bugs"
- *Mentoring:* Introduced Test Console MCP server to colleagues with examples. Yariv (BOA team) confirms willingness to mentor and assist others to begin contributing to Test Console. Mentoring is present but could be more structured and formalized
- *CI/CD:* Designs and manages Test Console CI/CD pipeline. Meets Level 4

**Already demonstrating at QE Level 5:**
- *Platform ownership:* Test Console is the central testing platform for RHIVOS. Owning it is effectively "setting mid-term strategic direction of quality assurance activities"
- *AI innovation:* Navigated 3 Gemini model transitions and built intelligent fallback mechanisms. This approaches Level 5 "leverage AI technologies to streamline workflows"
- *Cross-team enablement:* 199 mentions by others - confirms he's a central enabler. Level 5 "subject matter expert" behavior. Cross-team feedback from Yariv (BOA) rates Roni at Advanced Multiplier level, recognizing him as a "vital collaborative anchor" who scales behaviors to elevate Toolchain, Jumpstarter, and BoA through the Test Console platform
- *Mentoring and onboarding:* Willing to mentor and assist others to begin contributing to Test Console (Yariv feedback), lowering barriers for cross-team engagement. This is Level 5 "coaches and mentors" behavior extending through platform enablement
- *Business impact:* Kept CTC pipeline operational across all three release candidates. Explored new distribution channels (packages.redhat.com PoC). This is strategic QA impact

**Growth areas for QE Level 5:**
- *Strategic direction:* Level 5 expects "develop and implement mid-term quality engineering strategies aligned with business goals." Roni delivers excellence tactically but needs to articulate a quality strategy - where should testing go next quarter and next year?
- *Leading professional staff:* Level 5 expects "lead the activities of professional staff in resolving critical quality issues." Roni enables others but needs to formally lead QE staff and guide their work
- *Business acumen:* Level 5 expects "apply business acumen to prioritize and resolve highly complex testing and product quality challenges." Roni prioritizes by engineering judgment - needs to connect more explicitly to business priorities
- *Stakeholder management:* Level 5 expects "stakeholder management" as a core skill. Roni communicates well technically but could expand engagement with product, program management, and customers
- *Knowledge sharing outside the team:* Level 5 expects broader knowledge sharing. 199 mentions shows he's valued, but formal presentations, blog posts, or conference talks would strengthen the case
- *Enterprise CI/CD:* Level 5 expects "design and implement robust CI/CD pipelines that meet enterprise-level standards." Test Console CI/CD is solid but could be positioned as a reference architecture

**Recommended development path:**
1. **Write a quality engineering strategy** - document where RHIVOS testing should go: AI-powered analysis maturity, Test Console evolution, new test types, coverage targets. Present to leadership
2. **Position Test Console as enterprise reference** - the platform is mature enough to be a reference architecture. Document it, present it at internal forums, offer it as a pattern for other products
3. **Present externally** - the AI-powered test analysis story (3 model transitions, fallback mechanisms) is a compelling conference talk for DevConf or testing conferences
4. **Expand stakeholder engagement** - engage more with product management and customers on quality metrics. Translate testing results into business language
5. **Formalize mentoring** - Yariv's feedback confirms Roni's willingness to mentor others into Test Console. Structure this into regular mentoring sessions for cross-team contributors. Help Bella with her CTC reporting work as a natural extension
6. **Develop business acumen** - understand how quality metrics connect to product release decisions, customer satisfaction, and revenue impact

---

## Summary: Dimension-based view

### Where the team sits on Scope / Complexity / Impact

- Bella [Level 3, trending 4] - Scope: 3, trending 4 / Complexity: 3, trending 4 / Impact: 3-4. Strongest: Impact (CTC + Konflux affect release certification and RHAS GA). Already showing Level 4 signals across all dimensions. Biggest gap: Visibility (self-identified), knowledge sharing.
- Eitan [Level 3, with L4 signals] - Scope: 3, with L4 signals (runner consolidation, AI tooling) / Complexity: 3, trending 4 / Impact: 3, with L4 data points (budget savings). Strongest: Business impact (runner consolidation), AI methodology (claude-code skills). Biggest gap: Knowledge sharing, community leadership.
- Hubert [Level 3] - Scope: 3, trending 4 / Complexity: 3-4 boundary / Impact: 3, trending 4. Strongest: Complexity (gating expertise + cross-team relationships). Biggest gap: Impact - needs to own a strategic initiative with functional-level accountability.
- Kanitha [Level 3, approaching 4] - Scope: 3-4 boundary, strong (TPO + distribution) / Complexity: 3, trending 4 (QMS audit SME) / Impact: 3-4 boundary, strong (TPO shapes team direction). Strongest: Scope (25 channels, 4 Jira projects, TPO, broadest reach). Biggest gap: technical design artifacts (design docs, architecture decisions).
- Muhamad [Level 3, with L4 signals] - Scope: 3, with L4 signals / Complexity: 3 / Impact: 3, trending 4. Strongest: Scope (production-grade e2e platform architecture, cross-repo reviews, high execution consistency 10/12 PRs). Biggest gap: Visibility (38 Slack messages, lowest on team) and knowledge sharing.
- Juanje [Level 4] - Scope: 4-5 / Complexity: 4-5 / Impact: 4, trending 5. Strongest: Scope (cross-functional vision + innovation, approaching Level 5). Biggest gap: Impact - needs to consistently serve as organizational-level SME and project lead.
- Benny [Level 4] - Scope: 4 / Complexity: 4, trending 5 / Impact: 4. Strongest: Complexity (connective hub, community expert). Biggest gap: Impact - tactical breadth, needs strategic direction-setting.
- Roderick [Level 4] - Scope: Too early / Complexity: Too early / Impact: Too early. Strongest: N/A (onboarding). Biggest gap: Domain depth - establish Level 4 baseline first.
- Matt [Level 4] - Scope: 4 (building) / Complexity: 3-4 / Impact: 3. Strongest: Scope (initiative to propose improvements). Biggest gap: Complexity + Impact - domain expertise and delivery cadence still ramping.
- Roni [Level 4] - Scope: 4-5 / Complexity: 4, trending 5 / Impact: 4, trending 5. Strongest: Impact (Test Console decisions directly affect CTC/release) and cross-team multiplier effect (Yariv/BOA: Advanced-level Multiplier through platform enablement). Biggest gap: Complexity - needs to be recognized as SME advising functional leaders; strategic direction articulation.

### Common themes

- Knowledge sharing (articles, design docs) - Who: Bella, Eitan, Benny, Muhamad, Kanitha. Dimension: Scope + Complexity (expert recognition). Action: Write at least one internal article or design doc per quarter.
- AI tools exploration - Who: Bella, Hubert, Kanitha, Muhamad. Dimension: Scope (proposing new methods). Action: Try AI tools for daily work; share findings in team channel. (Note: Eitan has already progressed past exploration - built reusable claude-code hooks and skills. His next step is formalizing and sharing with team.)
- Mentoring relationships - Who: Bella, Eitan, Muhamad, Benny. Dimension: Scope (guidance to others). Action: Establish at least one formal mentoring pair.
- External presentations - Who: Juanje, Benny, Roni. Dimension: Complexity (industry recognition). Action: Submit conference talks; internal demos are a stepping stone.
- Business impact articulation - Who: All. Dimension: Impact (strategy contribution). Action: Frame technical work in terms of business value when presenting to leadership.
- Strategic thinking (roadmaps) - Who: Benny, Kanitha, Roni. Dimension: Impact (medium-to-long-term direction). Action: Write one forward-looking strategy/architecture document per half.
- Visibility and communication - Who: Muhamad, Bella. Dimension: Complexity (broader relationships). Action: Increase Slack engagement, present at sprint demos and team meetings, share work proactively. (Both self-identified this as a growth area.)
- Cross-team coordination - Who: Bella, Eitan, Muhamad. Dimension: Scope (functional-level reach). Action: Lead at least one initiative requiring coordination with another team.
