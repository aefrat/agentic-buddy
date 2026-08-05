# Development Feedback & Growth Paths - Q2 2026 (v2)

**Period:** Q2 2026 (April 1 - June 30)
**Generated:** 2026-08-05
**Sources:**
- [Software Engineer (IC) Progression Matrix - April 2026](https://docs.google.com/spreadsheets/d/1OAjiTMCBJ4YkBqfh69JwEgW81BJLbAeU8GWanYYCE_4/edit?gid=798132925)
- [SRE (IC) Progression Matrix - April 2026](https://docs.google.com/spreadsheets/d/1Fcr_ZMjT1hq7CANLFYSRE_9gp0Qcs897rfB-8kpx5PI/edit?gid=1708656902)
- [Quality Engineer (IC) Progression Matrix - April 2026](https://docs.google.com/spreadsheets/d/11MXcG53p9k6ncsRtxLSF3LuWfne3Z4PL35t1Svps3AM/edit?gid=1630329910)
- [Red Hat Job Leveling Framework - February 2025](file:///home/aefrat/Downloads/Job%20Leveling%20Framework%20PDF_version%20Feb%202025.pdf) (Radford-based, 3 dimensions: Scope, Complexity, Impact)
- [Job Architecture - The Source](https://source.redhat.com/career_and_benefits/red_hats_rewards_portfolio/global_compensation/job_architecture) (June 2026, career track pathway, promotion criteria)
- [Global Engineering Talent Architecture](https://source.redhat.com/departments/products_and_global_engineering/p_and_ge_content/talent_architecture) (skill progression matrices by job family)
- SE Level 3 Job Description Gap Analysis (Section D assessments - August 2026)
- SE Level 4 Job Description Gap Analysis (Section D assessments - August 2026)
- SRE Level 4 / QE Level 4 Job Description Gap Analysis (Section D assessments - August 2026)

---

## Framework

Red Hat uses the Radford leveling methodology. All IC engineers are on the **Professional track**, assessed across three dimensions that increase with level:

- Scope: Functional reach, breadth of responsibility, guidance provided to others
- Complexity: Judgment required, expertise depth, nature of relationships
- Impact: Accountability for results, contribution to strategy, decision consequence

The IC Progression Matrices (per job family) add **10 role-specific responsibilities and skills** on top of these dimensions. Both lenses are used below.

### Job description gap analysis (new in v2)

This version adds a second assessment lens: the **job description gap analysis**. For each team member, responsibilities and skills from their current-level job description are evaluated against Q2 evidence. This complements the Radford dimension assessment by grounding development feedback in the specific expectations of each role, not just the abstract level framework. Where Radford dimensions answer "where are you on the career ladder," the job description analysis answers "are you fully meeting what your current role requires."

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
1. **Dimension assessment (Scope / Complexity / Impact)** - where they sit on each Radford dimension relative to their current and next level
2. **Responsibilities assessment** - how they perform against each responsibility in their current-level job description, with evidence citations
3. **Skills assessment** - how they perform against each skill in their current-level job description, with evidence citations
4. **Already demonstrating at next level** - where Q2 evidence shows next-level behaviors
5. **Growth areas for next level** - specific gaps between current performance and next-level expectations
6. **Recommended development path** - concrete actions to close those gaps

---

## Senior Software Engineers (IC Level 3 - next: Principal SE, IC Level 4)

### Bella Khizgiyaev - Senior Software Engineer, PitCrew

*Updated 2026-07-12 with self-assessment input. Bella's stated growth area: increasing visibility ("speaking up more in team meetings, planning sessions, community meetings, presenting more during sprint demos"). Self-identified strengths: ownership, collaboration, supporting the team. Career aspiration: grow into senior technical leadership role (long-term 3-5 years).*

**Dimension assessment (Professional Track):**

- Scope [Level 3, trending 4]: Works independently with minimal instruction. Delivers on enhanced processes (CTC reporting, OIDC hardening, Konflux onboarding). Provides guidance within PitCrew. Cross-subsystem reach is becoming a pattern, not occasional: OIDC certificates extended to jumpstarter, Konflux onboarding requires coordination with Release Engineering, demo environment required cross-team hardware negotiation. Helped with Jumpstarter 0.9.0 release (release notes, reviews). Nudging toward Level 4 scope.
- Complexity [Level 3, trending 4]: Good judgment on moderately complex issues (CTC pipeline failures, certificate handling, Konflux productization pipeline adaptation). Recognized as experienced within PitCrew. Konflux onboarding required learning a new system end-to-end and adapting build pipelines - creative problem-solving on non-routine issues. Relationships extending beyond discipline through hardware negotiations, Konflux/RelEng coordination. Approaching Level 4.
- Impact [Level 3-4]: CTC reporting directly impacts release certification - program objectives (Level 4). Konflux onboarding is foundational to RHAS GA - this is business-facing impact. Demo environment enabled customer-facing engagements (Ford, Summit, CES). Operational direction expanding beyond PitCrew scope.

**Responsibilities assessment (SE Level 3):**

| # | Responsibility | Rating | Evidence |
|---|---------------|--------|----------|
| 1 | Technical Impact: Leads design and development for a subsystem or component | Met | Leads CTC pipeline component (4 of 8 closed tickets), builder operator features (OIDC, observability, metrics), and drove Konflux onboarding as biggest effort of the quarter. Spans three distinct subsystems: CTC, builder operator, and Konflux productization. ~18 GitHub PRs. |
| 2 | Quality: Owns code quality and contributes to testing frameworks | Met | Fixed CTC junit report generation across multiple dimensions (PITCREW-433, PITCREW-377, PITCREW-365, PITCREW-441). Built sample observability dashboard (PITCREW-370) and metrics for sealed operations (PITCREW-368). Quality work spans testing infrastructure and operational monitoring. |
| 3 | Community: Recognized active contributor, serves as reviewer or maintainer | Met | Active code reviewer across all new PRs on automotive-dev-operator (self-reported maintainer role). Reviews across 2 repos (operator + jumpstarter core). Helped prepare Jumpstarter 0.9.0 release notes. Supported demos for Ford, Summit, and CES. |
| 4 | Mentoring: Mentors and coaches other engineers | Partially met | Active code reviewer who helps maintain repo quality. General team support. However, no evidence of structured mentoring or coaching relationships with specific engineers. Self-identified visibility as growth area suggests this is an area for development. |
| 5 | Business Impact: Owns and delivers features with clear business impact | Met | Konflux onboarding is directly tied to RHAS productization (GA readiness). Ford customer demo support (PITCREW-353 - x86_64 qemu lab). OIDC security features required for production authentication. Builder observability enables customer-facing reliability monitoring. |
| 6 | Technical Practices: Supports and implements adoption of new tools | Met | Drove Konflux adoption for the team - learned staging environment, onboarded automotive builder upstream project, adapted build pipeline to product requirements. Release process support for Jumpstarter 0.9.0. |
| 7 | AI Tools: Implements AI-powered agents to automate non-routine workflows | Gap | No evidence of AI tool adoption or agent implementation this quarter. Neither ticket data nor self-assessment mention AI tooling exploration or automation through AI agents. |
| 8 | SDLC: Champions and refines team SDLC, mentors junior engineers | Partially met | Active code reviewer maintaining quality standards. Supported release process (0.9.0 notes, change review). However, no evidence of proposing SDLC improvements or mentoring junior engineers on best practices. |

**Skills assessment (SE Level 3):**

| # | Skill | Rating | Evidence |
|---|-------|--------|----------|
| 1 | Technical Acumen | Strong | Works across CTC pipelines, Kubernetes operators (builder), Jumpstarter, Konflux, OIDC authentication, and observability. Breadth of technical areas is notable - few engineers operate across this many distinct systems simultaneously. |
| 2 | Quality Management | Strong | CTC junit improvements across multiple failure modes (generation on pipeline fail, content length, missing fields, multiple plans). Observability dashboard and metrics for sealed operations. Systematic approach to quality - finds and fixes patterns, not just individual bugs. |
| 3 | System Design | Adequate | Builder features demonstrate component-level design (OIDC certificates, observability, metrics). Konflux pipeline adaptation for product requirements. However, no design documents produced - design decisions are embedded in PRs rather than documented for broader consumption. |
| 4 | Communication | Developing | 79 Slack messages in only 3 channels - highly concentrated. Self-identified "increasing visibility" as growth area and is actively working on it (speaking up more in team meetings, presenting in sprint demos). Communication is effective when present but limited in reach. |
| 5 | Collaboration | Adequate | Code reviews across repos, team support, release preparation, demo support. However, narrow channel presence (3 channels) limits cross-team collaboration visibility. Collaboration is strong within the immediate team but does not extend broadly. |
| 6 | Leadership | Developing | Takes strong ownership of her areas. Active maintainer role. However, self-identified visibility gap and limited coaching evidence suggest leadership is exercised through code quality rather than through influence on people and direction. |
| 7 | Business Impact | Strong | Konflux productization directly enables RHAS GA timeline. Ford/Summit/CES demo support shows direct customer engagement. OIDC and observability features are production requirements - this work is on the critical path for business outcomes. |
| 8 | Continuous Learning | Adequate | Learned Konflux staging environment from scratch and onboarded the project. However, learning scope is primarily within the immediate RHAS ecosystem. AI tools and broader technology exploration are not evidenced. |
| 9 | Influence | Developing | Influences through code reviews and maintainer role. However, limited evidence of shaping technical direction of the team or adjacent teams. Influence is exercised through quality gates rather than through strategic proposals. |
| 10 | Knowledge Sharing | Developing | Code reviews provide implicit knowledge sharing. Release notes preparation for 0.9.0. However, no design documents, blog posts, or formal knowledge transfer activities evidenced. The Konflux onboarding experience is exactly the kind of knowledge that should be documented and shared. |

**Already demonstrating at IC Level 4:**
- *Cross-component ownership:* Spans CTC, builder operator, and Jumpstarter simultaneously - L4 expects impact across multiple subsystems, and Bella already operates this way
- *Productization leadership:* Driving Konflux onboarding bridges upstream to downstream - an L4-level initiative requiring understanding both engineering and business requirements
- *Maintainer role:* Active code review across all new PRs shapes project standards through review - characteristic of L4 engineers
- *Technical Impact (cross-component):* Extended OIDC certificate pattern from builder to jumpstarter - crosses subsystem boundaries. Konflux onboarding spans upstream project, GitOps resources, and Red Hat Release Engineering
- *End-to-end ownership:* Demo environment from hardware procurement through configuration to demo readiness. Konflux onboarding from staging experimentation through GitOps setup to pipeline adaptation

**Growth areas for IC Level 4:**
- *Visibility and communication breadth (self-identified):* L4 requires broad influence, which depends on being seen and heard beyond the immediate team (3 Slack channels is too narrow). Bella recognizes this and is actively working on it
- *Design documentation:* The Konflux onboarding, OIDC architecture, and observability strategy deserve written design documents that can influence how adjacent teams approach similar problems
- *AI tools adoption:* L4 requires championing new technology adoption. Starting with personal AI tooling and expanding to team-level automation would address both this gap and the visibility goal simultaneously
- *Structured mentoring:* Move from implicit knowledge sharing through code reviews to explicit coaching relationships with junior engineers
- *Business impact articulation:* Konflux and CTC work have significant business impact (RHAS GA, release certification) but she hasn't explicitly positioned them as business-facing initiatives

**Recommended development path:**
1. **Continue increasing visibility** (self-identified priority) - the sprint demo presentations and team meeting participation are the right approach. Next step: present a technical topic to a broader audience (community meeting, cross-team forum) - the Konflux onboarding experience or CTC pipeline architecture would be strong topics
2. **Document the Konflux onboarding and OIDC architecture** - write a design document for at least one area she owns. This makes the work visible, shareable, and promotable
3. **Position Konflux and CTC as business-facing initiatives** - the impact is there but not articulated. Frame Konflux onboarding as "enabling RHAS GA through productization infrastructure" when presenting to leadership
4. **Start mentoring** - pick one junior/mid-level engineer (Muhamad could be a natural fit on the same team) and establish a regular technical mentorship
5. **Explore AI tooling** - try using AI agents or code-generation tools for testing or debugging work and share findings with the team

---

### Eitan Raviv - Senior Software Engineer, ATC

*Updated 2026-06-29 with self-assessment input. Eitan's stated development trajectory: "continued hands-on work, with an inclination to go deep into an area in order to enhance it."*

**Dimension assessment (Professional Track):**

- Scope [Level 3, with Level 4 signals]: Works independently across broad infrastructure domain (AWS, CloudFront, CI/CD, monitoring, security). GitLab runner consolidation is a clear Level 4 behavior - proposed a new technique (pipeline pooling) based on business context (cost reduction) with impact within the function. AI tooling adoption (claude-code hooks/skills) shows "proposing new methods." Gator sessions with Hubert and Distribution Focus area help show cross-scope willingness.
- Complexity [Level 3, trending 4]: Navigated 5+ external organizational channels (PSCA, IT Cloud, GRC, BOA) - this breadth of relationship exceeds Level 3's "within discipline." Built reusable AI tools (hooks, skills) rather than one-off usage - creative problem-solving characteristic of Level 4. Not yet recognized as expert leading cooperative efforts.
- Impact [Level 3, with Level 4 data points]: Runner consolidation delivered measurable budget savings - impacts operational objectives beyond immediate team (Level 4). CPPX ticket affects customer-facing outcomes. Monitoring SLA criticality tiers shape how the broader team prioritizes incident response. Infrastructure work keeps release pipeline secure and operational.

**Responsibilities assessment (SE Level 3):**

| # | Responsibility | Rating | Evidence |
|---|---------------|--------|----------|
| 1 | Technical Impact: Leads design and development for a subsystem or component | Met | Leads infrastructure components: s3pi (performance improvements, integration tests, tech debt reduction), CloudFront multi-distribution module (VROOM-41214), GitLab runner consolidation reducing EC2 count and budget. 28 merged MRs across infrastructure, s3pi, and monitoring projects. |
| 2 | Quality: Owns code quality and contributes to testing frameworks | Partially met | Created s3pi integration tests (VROOM-41073). Resolved container vulnerabilities (VHCL-009, Major). However, test contributions are limited to one project - no broader testing framework design or team-level quality strategy. |
| 3 | Community: Recognized active contributor, serves as reviewer or maintainer | Partially met | Helped distribution focus area with urgent work. Engaged with BOA team (5 msgs), psca-support (6), cloud-publiccloud (5). However, limited upstream or broader community visibility - 76 Slack messages is the lowest on the ATC team. |
| 4 | Mentoring: Mentors and coaches other engineers | Gap | No mentoring evidence this quarter. Participated in learning sessions with Hubert about Gator (as learner, not mentor). This is a clear gap against the L3 expectation of mentoring and coaching others. |
| 5 | Business Impact: Owns and delivers features with clear business impact | Met | GitLab runner consolidation produced direct budget savings by reducing EC2 count. CloudFront upgrades resolved multiple infrastructure issues. Monitoring SLA spec with criticality tiers (VROOM-38184) improves service reliability. |
| 6 | Technical Practices: Supports and implements adoption of new tools | Met | Active claude-code adoption: built hooks (completion notification) and skills (Jira ticket creation, GitLab MR fetching, feature design). Monitoring criticality tiers introduce operational maturity tooling. |
| 7 | AI Tools: Implements AI-powered agents to automate non-routine workflows | Met | Built multiple claude-code skills: create Jira ticket without UI (auto-fills defaults), fetch GitLab MRs, fetch Jira tickets, design a new feature. Built hooks for session management. Applies AI across all tasks (self-reported). |
| 8 | SDLC: Champions and refines team SDLC, mentors junior engineers | Gap | No evidence of SDLC championing, process improvement proposals, or mentoring junior engineers on best practices. Housekeeping work (Jira migration, Bitwarden, token refresh) is maintenance, not SDLC leadership. |

**Skills assessment (SE Level 3):**

| # | Skill | Rating | Evidence |
|---|-------|--------|----------|
| 1 | Technical Acumen | Adequate | Strong depth in infrastructure (s3pi, CloudFront, GitLab runners, AWS). Self-described inclination to "go deep into a subject matter and enhance it to production-level grade." However, breadth is narrower than peers - primarily infrastructure-focused. |
| 2 | Quality Management | Developing | s3pi integration tests and vulnerability resolution. No evidence of designing automated testing frameworks or driving team-level quality strategy. Quality work is limited to individual project scope. |
| 3 | System Design | Adequate | CloudFront multi-distribution module design. GitLab runner consolidation architecture (combining multiple pipeline pools). Makes trade-offs within infrastructure domain. Design scope is contained rather than cross-cutting. |
| 4 | Communication | Developing | 76 Slack messages across 14 channels - lowest on the ATC team. Self-identified preference for depth over breadth. Communication is effective within scope but limited in volume and reach. Technical concepts may not reach stakeholders who need them. |
| 5 | Collaboration | Adequate | Cross-team engagement with BOA (5 msgs), psca-support (6), cloud-publiccloud (5). Helped distribution focus area with urgent work. Conducted Gator learning sessions with Hubert. Collaboration is responsive rather than proactive. |
| 6 | Leadership | Developing | Depth-first approach drives strong individual execution, but no evidence of coaching others or setting team-level engineering standards. Leadership is through personal contribution, not through multiplying others. |
| 7 | Business Impact | Adequate | Budget savings from runner consolidation are real and measurable. However, impact articulation could be stronger - the business value of deep infrastructure work deserves better framing and visibility. |
| 8 | Continuous Learning | Strong | Most active AI adopter on the team - claude-code hooks, skills, and session management. Applies AI "across all tasks." Sees himself as future "overseer" directing AI implementation. Forward-thinking technology adoption. |
| 9 | Influence | Developing | Limited evidence of influencing team or adjacent team technical direction. The depth-first approach produces strong results but does not yet translate into directional influence on how the team works. |
| 10 | Knowledge Sharing | Developing | AI skills built for personal productivity but not yet shared with the team. No evidence of design documents, blog posts, or formal knowledge transfer activities. The claude-code work represents valuable knowledge that could be multiplied if shared. |

**Already demonstrating at IC Level 4:**
- *AI adoption leadership:* Most advanced AI tooling usage on the team (claude-code hooks and skills), with a forward-thinking vision of the engineer-as-overseer model
- *Production-grade depth:* The inclination to enhance systems to production-level grade (s3pi performance, monitoring SLA tiers) aligns with L4's expectation of architectural excellence
- *Business impact:* GitLab runner consolidation delivered measurable EC2 cost savings - "visible business impact initiative" (Level 4 SE progression)
- *Cross-team collaboration:* Navigated 5+ external channels, jumped into Distribution Focus area for urgent work, conducted Gator sessions with Hubert

**Growth areas for IC Level 4:**
- *Communication and visibility:* L4 requires clearly communicating complex technical concepts to broad audiences. 76 Slack messages and 14 channels limit the reach of strong technical work
- *Mentoring:* Clear gap - L4 requires coaching and growing other engineers. The AI skills and infrastructure depth are exactly the knowledge that should be shared through mentoring
- *Knowledge sharing through written artifacts:* Design documents for runner consolidation, CloudFront decisions, and AI workflow methodology would demonstrate L4-level influence. Channel the depth-first inclination into shareable, scalable knowledge
- *Broader collaboration and cross-team influence:* Move from responsive collaboration (helping when asked) to proactive influence on team and adjacent team technical direction
- *SDLC leadership:* No evidence of process improvement proposals. Level 4 expects leading SDLC definition for multi-component systems

**Self-assessment alignment:** Eitan identifies his trajectory as "continued hands-on work, with an inclination to go deep into an area in order to enhance it." This aligns naturally with the infrastructure depth he already demonstrates. The recommended development path channels this depth-oriented inclination toward Level 4 impact by ensuring his deep-dive improvements are formalized, shared, and positioned as functional-level contributions.

**Recommended development path:**
1. **Formalize and share the AI tooling work** - the claude-code hooks and skills are exactly Level 4's "evaluate and introduce new methodologies." Share with the team, document workflow improvements, propose adoption patterns. This turns personal depth into team-wide methodology introduction
2. **Lead a cross-component design initiative** - expand the runner consolidation into a formal CI/CD optimization strategy with documented design decisions and cost impact analysis. Present to stakeholders
3. **Mentor newer team members** on infrastructure and AWS patterns. Matt Goldman and Hubert Stefanski, who touch similar infrastructure, would benefit from Eitan's deep operational knowledge
4. **Document infrastructure decisions** - write internal design documents or blog posts for key infrastructure choices (runner consolidation cost savings, CloudFront architecture, s3pi optimization patterns)
5. **Engage with SRE or infrastructure communities** at Red Hat - contribute patterns or tools to internal SRE forums

---

### Hubert Stefanski - Senior Software Engineer, ATC (transitioning to PitCrew)

**Dimension assessment (Professional Track):**

- Scope [Level 3, trending 4]: Works independently with deep expertise. Gating work proposes new techniques (dependency triggering, QC LP gating workflow) - this is Level 4 "proposes new methods based on business context." Helped PitCrew design GitLab repo structure (cross-team scope).
- Complexity [Level 3-4 boundary]: Independent judgment on non-routine gating issues. Recognized as experienced across infrastructure and gating. Productive relationships across multiple teams (PitCrew, CAT, ITSEC) - moving beyond "within discipline." 18 channels. Min 5 years met.
- Impact [Level 3, trending 4]: Gating improvements impact team's release quality (team goals). Infrastructure decisions affect multiple downstream consumers. Starting to impact functional objectives through gating reliability.

**Responsibilities assessment (SE Level 3):**

| # | Responsibility | Rating | Evidence |
|---|---------------|--------|----------|
| 1 | Technical Impact: Leads design and development for a subsystem or component | Met | Owns the infrastructure subsystem (AWS, S3, CloudFront, GitLab runners, IAM). Designed the architectural pivot from path-prefix routing to per-bucket CloudFront distributions. 29 merged MRs across infrastructure, gator, and s3pi projects. Shipped Gator depends_on feature (VROOM-41530) with follow-up bug fixes. |
| 2 | Quality: Owns code quality and contributes to testing frameworks | Met | Container vulnerability remediation for gator images (VHCL-014, Major priority). Shipped two critical bug fixes after depends_on merge (MR 241 NVR lookup, MR 245 evaluation guard). Proactive follow-through on quality issues rather than waiting for escalation. |
| 3 | Community: Recognized active contributor, serves as reviewer or maintainer | Met | Cross-team connector working with 12+ stakeholders across ATC, Kernel, QE, Build, PAC, Test Console, PIT, MPP, CAT. 17 messages in forum-jumpstarter. Attended RoK ARB call where RHIVOS gating proposal was well received. |
| 4 | Mentoring: Mentors and coaches other engineers | Met | Conducted formal gating knowledge transfer sessions with Eitan (June 11, 18). Documented decisions in tickets and sprint notes for continuity. Proactive KT planning ahead of RHAS transition rather than reactive handoff. |
| 5 | Business Impact: Owns and delivers features with clear business impact | Met | Resolved multi-team CloudFront/S3PI outage within 24 hours (May 6), unblocking 4+ engineers. Same-day AWS security incident response (April 10). Ferrous S3 bucket migration. PIT Yocto builder provisioning. Direct unblocking of customer-facing work. |
| 6 | Technical Practices: Supports and implements adoption of new tools | Met | Set up CRC (OpenShift Local) for RHAS transition (June 22-26) alongside Jumpstarter and pac-jobs. Gator depends_on feature introduced new dependency management capability. Evaluated Jumpstarter CTC runs (Epic VROOM-34179). |
| 7 | AI Tools: Implements AI-powered agents to automate non-routine workflows | Gap | No evidence of AI tool adoption or agent implementation this quarter. The self-assessment and ticket data show no AI-related work. This is a clear gap against the L3 JD. |
| 8 | SDLC: Champions and refines team SDLC, mentors junior engineers | Partially met | Proactive incident response pattern (same-day resolution, stakeholder notification). Knowledge transfer sessions demonstrate SDLC continuity awareness. However, no evidence of formal SDLC process championing or improvement proposals. |

**Skills assessment (SE Level 3):**

| # | Skill | Rating | Evidence |
|---|-------|--------|----------|
| 1 | Technical Acumen | Strong | Go-to person for infrastructure challenges spanning AWS, S3, CloudFront, EC2, GitLab runners, IAM, Kubernetes operators. 29 merged MRs. Diagnosed and resolved the CloudFront outage through architectural analysis. |
| 2 | Quality Management | Adequate | Vulnerability remediation (VHCL-014), follow-up bug fixes after feature merge. Quality-conscious in execution, but no testing framework design or quality strategy work this quarter. |
| 3 | System Design | Strong | CloudFront architecture pivot: recognized path-prefix approach was fundamentally non-viable after 3 weeks and 6 MR iterations, pivoted to per-bucket distributions. Gator depends_on feature design. Trade-off decisions are well-evidenced. |
| 4 | Communication | Strong | Coordinated with 12+ stakeholders during CloudFront outage, notified all affected parties, confirmed resolution. 402 Slack messages. Clear incident communication and follow-up patterns. |
| 5 | Collaboration | Strong | Worked across 9 teams (ATC, Kernel, QE, Build, PAC, TC, PIT, MPP, CAT). Coordinated the CloudFront resolution with Eitan. Supported PIT Yocto builder request. Active in 18 channels. |
| 6 | Leadership | Strong | Led CloudFront outage resolution. Proactive ownership pattern - AWS security alert same-day response without waiting for escalation. Knowledge transfer initiative ahead of team transition. Sets a standard for incident response. |
| 7 | Business Impact | Strong | CloudFront resolution unblocked 4+ engineers across multiple teams. Same-day incident response prevents cascading delays. Ferrous migration enabled nightly builds for a key program. |
| 8 | Continuous Learning | Adequate | Ramping on CRC, OpenShift operators, Tekton, and Jumpstarter for RHAS transition. Demonstrated willingness to pivot domains entirely. However, AI tools gap is notable given industry trajectory. |
| 9 | Influence | Adequate | RoK ARB call where RHIVOS gating proposal was "very well received" by Veronika and Don Zickus. Influences infrastructure decisions within the team. Cross-team influence is more through execution than strategic direction. |
| 10 | Knowledge Sharing | Adequate | Conducted KT sessions with Eitan. Documented decisions in tickets and sprint notes. Self-identified growth area: documentation could have been created earlier in the quarter rather than retrospectively during transition. |

**Already demonstrating at IC Level 4:**
- *Architectural decision-making under pressure:* The CloudFront pivot (abandoning 3 weeks of sunk effort for the right solution) shows the judgment L4 requires
- *Cross-team impact at scale:* Unblocked 12+ individuals across 9 teams, showing the organizational breadth expected at L4
- *Incident leadership pattern:* Same-day response, stakeholder coordination, resolution confirmation - demonstrates operational maturity beyond L3
- *Knowledge transfer initiative:* Proactive KT sessions with Eitan ahead of transition rather than reactive handoff

**Growth areas for IC Level 4:**
- *AI tools adoption:* Clear gap - L4 requires not just using AI but championing its adoption across the team and adjacent teams
- *Decision velocity:* The 3-week CloudFront path-prefix investment before pivoting suggests establishing clearer "stop-loss" criteria when approaches show fundamental limitations
- *Proactive documentation:* Architecture decisions and runbooks should be created at decision time, not retrospectively during transitions. L4 expects knowledge to scale through written artifacts
- *Strategic initiative ownership:* Level 4 expects "leads the design and development of software solutions for features that cross multiple subsystems." Hubert does this reactively (fixing gating gaps) but needs to own a strategic initiative proactively
- *SDLC process championing:* No evidence of formal SDLC improvement proposals

**Recommended development path:**
1. **Own a strategic initiative** - as he transitions to PitCrew, lead the design of a cross-team capability (e.g., gating strategy for RHIVOS LP, or infrastructure patterns for jumpstarter). Frame it as a technical initiative with business impact
2. **Formalize knowledge sharing** - convert his deep gating and infrastructure knowledge into design documents or internal blog posts. He already communicates well in Slack; writing it up makes it durable and counts toward Level 4
3. **Establish mentoring relationships** - with the PitCrew transition, he can mentor PitCrew members on infrastructure patterns and gating expertise. Formalize this
4. **Explore AI tooling** for infrastructure operations, gating, or pipeline automation
5. **Create documentation at decision time** - establish the habit of writing architecture decision records alongside the work, not after

---

### Kanitha Chim - Senior Software Engineer, ATC

**Dimension assessment (Professional Track):**

- Scope [Level 3-4 boundary, strong]: Works independently on complex distribution workflows. Broadest channel reach on team (25 channels). Cross-team coordination spanning 4 Jira projects (VROOM, RHELDST, RHELWF, PSSECAUT) - this exceeds Level 3's "within discipline" scope. The distribution/release work is functional-level, not just team-level. Additionally serves as ATC Technical Product Owner (TPO) - setting 6-month team priorities, leading focus area brainstorms, and representing ATC on program calls alongside Area PO Petr Sabata.
- Complexity [Level 3, trending 4]: Resolves moderately complex issues (errata, CDN propagation failures, product listing). Cross-team relationships are productive and extend well beyond own team. QMS ISO 26262 Part 8 audit SME work (Configuration Management, Confidence in Tools) demonstrates capacity for cross-org responsibility in an unfamiliar domain. Acts as de facto distribution expert and TPO - team independently named the role.
- Impact [Level 3-4 boundary, strong]: Distribution work contributes directly to release readiness - customer-facing impact. Product listing and CDN decisions affect whether customers can download RHIVOS. TPO role directly shapes team direction and program alignment. QMS audit work impacts organizational certification. This touches "customer, operational, or program objectives" (Level 4).

**Responsibilities assessment (SE Level 3):**

| # | Responsibility | Rating | Evidence |
|---|---------------|--------|----------|
| 1 | Technical Impact: Leads design and development for a subsystem or component | Met | Owns the distribution/errata subsystem end-to-end. Took over Core and Fusa release after Marcel's departure (Errata prep + CDN). Mapped the QC Layered Product path for Qualcomm based on RHEL documentation research (VROOM-41524). Led FuSa-to-Core package separation (Epic VROOM-39032). |
| 2 | Quality: Owns code quality and contributes to testing frameworks | Partially met | Delivered compose-level and package-level gating improvements (VROOM-41424, VROOM-36323). Fixed workflow rules for Errata release (VROOM-41920). However, no evidence of testing framework design or contribution this quarter - quality work is operational, not framework-level. |
| 3 | Community: Recognized active contributor, serves as reviewer or maintainer | Met | Broadest channel presence on the team (25 channels). Active in forum-distribution-guild (16 msgs), cross-project work spanning 4 Jira projects (VROOM, RHELDST, RHELWF, PSSECAUT). 54 messages in automotive-release-readiness. Recognized cross-team distribution expert. |
| 4 | Mentoring: Mentors and coaches other engineers | Partially met | Plans to onboard new associate to distribution area next quarter. Identified onboarding buddy role as development goal. Limited evidence of active mentoring or coaching during Q2 itself - this is forward-looking rather than demonstrated. |
| 5 | Business Impact: Owns and delivers features with clear business impact | Met | Release distribution is directly business-critical - product listing for CDN repositories (VROOM-40773, VROOM-41432), Errata advisory preparation, and builds verification (VROOM-39025) are gate items for customer-visible releases. Enabled Openscanhub for RHIVOS-2 (PSSECAUT-1578). |
| 6 | Technical Practices: Supports and implements adoption of new tools | Met | Set up agentic AI tooling for Errata/distribution workflow to reduce repetitive process work (self-reported). Conducted Agentic AI spike for advisory workflow (VROOM-40319). Active adoption of automation to improve team processes. |
| 7 | AI Tools: Implements AI-powered agents to automate non-routine workflows | Met | VROOM-40319 spike on using Agentic AI for advisory workflow. Built and deployed agent for Errata/distribution process (self-reported accomplishment). Directly addresses this responsibility with practical team-level automation. |
| 8 | SDLC: Champions and refines team SDLC, mentors junior engineers | Partially met | Stepped in to improve poorly formed gating processes. Drives team prioritization aligned with POs/program/BU. However, limited evidence of explicitly mentoring junior engineers on SDLC best practices or formally championing process improvements. |

**Skills assessment (SE Level 3):**

| # | Skill | Rating | Evidence |
|---|-------|--------|----------|
| 1 | Technical Acumen | Strong | Go-to person for distribution, errata, and CDN workflows. Designed the LP distribution path for Qualcomm from RHEL documentation. Operates across Errata, Gator, advisory automation, and CDN systems. |
| 2 | Quality Management | Adequate | Gating workflow improvements at compose and package level. Verified build consistency between Errata and compose. However, no automated testing framework design this quarter - quality work is process-oriented rather than test-engineering. |
| 3 | System Design | Strong | Designed distribution workflow for QC Layered Product based on RHEL documentation analysis. Architectural decisions for Core/Fusa package separation. Makes trade-off decisions within the existing release infrastructure. |
| 4 | Communication | Strong | 423 Slack messages across 25 channels - broadest presence on the team. Active in release-readiness (54), distribution guild (16), signing (8). Effective cross-team coordination with POs, program, and BU stakeholders. |
| 5 | Collaboration | Strong | Work spans 4 Jira projects. Active in distribution guild, release readiness, and cross-team channels. Close coordination with POs and program on prioritization and timeline alignment. |
| 6 | Leadership | Adequate | Drives team prioritization aligned with program. Took ownership of Core and Fusa release after Marcel's departure. However, coaching evidence is thin this quarter - leadership is more execution-oriented than people-development. |
| 7 | Business Impact | Strong | Distribution and Errata work directly gates customer-visible releases. CDN product listing, advisory generation, and build verification are on the critical path for RHIVOS delivery. |
| 8 | Continuous Learning | Adequate | AI exploration (VROOM-40319), RHEL documentation study for LP path, GitLab/Konflux awareness. Learning breadth could expand beyond the immediate distribution domain. |
| 9 | Influence | Adequate | Influences within the team through PO-like prioritization role. Cross-team coordination in distribution guild. However, architectural influence on adjacent teams is limited - influence is operational rather than directional. |
| 10 | Knowledge Sharing | Developing | Plans for knowledge sharing and onboarding buddy role are forward-looking (Q3 priorities). Limited evidence of design documents, written knowledge artifacts, or formal knowledge transfer activities this quarter. |

**Already demonstrating at IC Level 4:**
- *Cross-project impact:* Spanning 4 Jira projects and 25 Slack channels - operates well beyond team boundaries
- *Domain ownership:* Distribution/errata subsystem with end-to-end accountability from Errata prep through CDN publication
- *Strategic technical exploration:* Mapped the LP path for Qualcomm by researching RHEL's approach and adapting it, showing the architectural thinking L4 requires
- *TPO leadership:* Bridges RHIVOS program priorities to ATC team execution, sets 6-month team priorities, leads focus area brainstorms
- *AI initiative:* Built and deployed agent for Errata/distribution workflow (VROOM-40319)

**Growth areas for IC Level 4:**
- *Design documentation:* Produce design documents that capture architectural decisions (e.g., the LP distribution path, Core/Fusa separation rationale) - L4 requires persuasive written communication that scales knowledge beyond 1:1 conversations
- *Mentoring track record:* The onboarding buddy plan for Q3 is a good start, but L4 expects demonstrated coaching impact over time
- *Technical influence beyond distribution:* Expand to shape team-level architectural direction (pipelines, infrastructure) aligned with long-term career aspirations
- *Knowledge sharing formalization:* Distribution expertise is currently held in Slack threads and tribal knowledge - needs durable artifacts

**Recommended development path:**
1. **Lead a design initiative** - the QC LP distribution workflow spike and the AI advisory workflow spike are both natural candidates. Pick one and drive it from spike to design document to implementation. The 2.0.z CDN/Errata design is the strongest option given her TPO role
2. **Document the release pipeline** - Kanitha has the deepest knowledge of RHIVOS distribution. A formal design document of the release workflow (errata, CDN, product listing, gating) would be high-value and demonstrate Level 4 knowledge sharing
3. **Follow through on AI for advisories** - the spike shows initiative. Develop it into a concrete proposal, evaluate tools, and present findings to the team
4. **Formalize distribution mentoring** - with new team member joining distribution area, structure knowledge transfer sessions
5. **Propose process improvements** - move from executing release processes to improving them. Leverage TPO perspective to identify and drive systematic fixes to release bottlenecks

---

### Muhamad Abo Ras - Senior Software Engineer, PitCrew

*Updated 2026-07-12 with self-assessment input. Muhamad's self-identified strengths: execution consistency (10/12 PRs merged), end-to-end ownership (filing issues to closing the loop), cross-team collaboration (reviewing jumpstarter core alongside operator work).*

**Dimension assessment (Professional Track):**

- Scope [Level 3, with Level 4 signals]: Works independently on testing infrastructure. Delivers on enhanced processes (production-grade e2e architecture, smoke lane, composite GH Actions). Self-input reveals broader scope than initially captured: active code reviewer across two repos (automotive-dev-operator + jumpstarter core), cross-team review contribution. ArgoCD/GitOps work expands beyond testing domain. The e2e testing architecture is effectively a platform initiative (lane architecture, log collection, CI observability) - approaching "proposes new methods" (Level 4).
- Complexity [Level 3]: Good judgment on moderately complex issues (OIDC e2e, Kind-to-CRC migration, multi-lane test architecture design). Productive relationships within own team + jumpstarter core reviewers. 38 Slack messages across 7 channels remains the lowest visibility, though GitHub-based cross-team activity (jumpstarter core reviews) is more significant than Slack alone suggests. Approaching "recognized as experienced" but needs broader relationship network.
- Impact [Level 3, trending 4]: Contributes to team goals through completion of testing tasks. Self-input reveals greater impact than initially assessed: production-grade e2e suite reduced contributor friction (shortening PR feedback loops), eliminated test coverage blind spots in auth and bootc paths, made CI failures significantly easier to diagnose. The smoke lane as default PR gate directly impacts developer productivity across the project.

**Responsibilities assessment (SE Level 3):**

| # | Responsibility | Rating | Evidence |
|---|---------------|--------|----------|
| 1 | Technical Impact: Leads design and development for a subsystem or component | Partially met | Leads e2e testing infrastructure for the builder operator - refactored from monolithic to multi-lane architecture with smoke, operator, bootc, and auth lanes. However, scope is limited to one component's test suite rather than a full subsystem or feature area. |
| 2 | Quality: Owns code quality and contributes to testing frameworks | Met | Strongest area. Designed and built the e2e test architecture from minimal coverage to a structured, parallelized, multi-lane suite. OIDC auth e2e tests with Dex (PITCREW-424) eliminated silently-skipped auth tests. PR-triggered test tiers (PITCREW-383). Centralized log collection for CI diagnostics. |
| 3 | Community: Recognized active contributor, serves as reviewer or maintainer | Partially met | Active reviewer across 2 repos (automotive-dev-operator + jumpstarter core). 10 of 12 authored PRs merged (83% merge rate). However, limited broader community engagement - 38 Slack messages is the quietest presence on either team. |
| 4 | Mentoring: Mentors and coaches other engineers | Gap | No mentoring evidence this quarter. Attended NHCE (new hire event). The e2e test architecture knowledge is valuable but not yet being transferred to other engineers through coaching or pairing. |
| 5 | Business Impact: Owns and delivers features with clear business impact | Partially met | E2e test improvements reduce contributor friction and improve CI reliability, which are business-enabling. ArgoCD/C2 recovery work (PITCREW-416) is disaster recovery. However, the connection between test infrastructure and end-user value is indirect and not explicitly articulated. |
| 6 | Technical Practices: Supports and implements adoption of new tools | Met | Introduced reusable composite GitHub Actions (setup, collect-logs, cleanup). PR-triggered test tiers with smoke lane as default gate. CRC OpenShift alignment for local dev. These are concrete tooling improvements adopted by the team. |
| 7 | AI Tools: Implements AI-powered agents to automate non-routine workflows | Gap | No evidence of AI tool adoption or agent implementation this quarter. Neither ticket data nor self-assessment mention AI tooling. This is a clear gap against L3 expectations. |
| 8 | SDLC: Champions and refines team SDLC, mentors junior engineers | Partially met | PR-triggered test tiers and smoke lane as default gate directly improve the SDLC. CI/CD improvements (reusable actions, artifact collection) refine the development workflow. However, no evidence of mentoring others on these practices or championing them beyond the immediate project. |

**Skills assessment (SE Level 3):**

| # | Skill | Rating | Evidence |
|---|-------|--------|----------|
| 1 | Technical Acumen | Adequate | Strong depth in e2e testing, CI/CD, GitHub Actions, Kubernetes multi-environment testing, OIDC integration. However, technical breadth is narrow - primarily focused on test infrastructure for one project. L3 expects being the go-to person for challenges across the team. |
| 2 | Quality Management | Strong | Standout area. Designed multi-lane e2e architecture from scratch. Eliminated auth test blind spot. Introduced smoke lane for fast PR feedback. Centralized log collection for diagnosis. Systematic approach to coverage gaps rather than ad hoc fixes. |
| 3 | System Design | Adequate | Test architecture design (lane isolation, namespace separation, tiered execution) is well-structured. However, design scope is limited to testing domain. No evidence of feature design or architectural trade-off decisions in production code. |
| 4 | Communication | Developing | 38 Slack messages across 7 channels - quietest presence on either team. Let the code speak (10/12 PRs merged), but L3 requires clearly communicating technical concepts to both technical and non-technical audiences. The e2e architecture redesign deserves written communication beyond PR descriptions. |
| 5 | Collaboration | Adequate | Reviews across 2 repos (operator + jumpstarter). Cross-team jumpstarter engagement. End-to-end ownership from issue filing to fix to close. However, limited evidence of fostering collaborative environments or leading group design discussions. |
| 6 | Leadership | Developing | Owns the e2e domain with high execution quality. However, no evidence of coaching others, setting team standards, or leading engineers. Leadership is through individual contribution quality rather than team multiplication. |
| 7 | Business Impact | Developing | CI reliability and contributor friction reduction are real but indirect business impacts. The ArgoCD/C2 recovery work (PITCREW-416) has disaster recovery value. Growth opportunity: explicitly frame test infrastructure work in terms of release velocity and product quality. |
| 8 | Continuous Learning | Adequate | Learned OIDC/Dex integration, GitHub Actions composability, CRC/OpenShift alignment. Learning is applied and practical. However, AI tools gap is notable and learning scope stays within the testing domain. |
| 9 | Influence | Developing | Limited evidence of influencing team or adjacent team technical direction. The e2e architecture improvements are influential in practice (contributors use them daily) but this influence is not actively communicated or leveraged to shape broader team practices. |
| 10 | Knowledge Sharing | Developing | No design documents, blog posts, or formal knowledge sharing evidenced. The e2e test architecture redesign - from monolithic to multi-lane - is a textbook case for a design document or tech talk that would benefit the broader engineering community. |

**Already demonstrating at IC Level 4:**
- *Test architecture ownership:* Designed the e2e framework from minimal coverage to structured multi-lane suite, showing the systematic design thinking L4 requires
- *High execution quality:* 10 of 12 PRs merged (83% merge rate) with end-to-end ownership from issue to fix to close
- *CI/CD engineering:* Extracted reusable CI patterns, built downloadable diagnostic artifacts, implemented PR-triggered test tiers - Level 4 "proposes new methods based on business context"

**Growth areas for IC Level 4:**
- *Technical breadth beyond e2e testing:* L4 requires being a go-to person across the team, not just within one domain. Expanding into production feature development or infrastructure would broaden impact
- *Communication and visibility:* Most critical gap - 38 Slack messages limits influence. The e2e architecture work deserves a design document, tech talk, or blog post to establish technical leadership reputation
- *Mentoring:* Prerequisite for L4 - start with pairing on the e2e framework with another engineer, documenting patterns for others to follow
- *AI tools adoption:* L4 requires championing new technology. Exploring AI for test generation, flaky test diagnosis, or coverage analysis would combine the testing domain strength with this requirement
- *Business impact framing:* Learn to articulate how test infrastructure improvements translate to release velocity, customer quality, and team productivity in business terms

**Recommended development path:**
1. **Increase visibility** - this remains the highest-priority growth area. Post more proactively in team channels: share design decisions, debugging findings, testing architecture improvements. Present the e2e lane architecture at a sprint demo or team meeting
2. **Document the e2e testing architecture** - write a design document for the production-grade e2e framework (lane architecture, smoke gate, composite actions, log collection). This is the single highest-leverage action: it makes the work visible, shareable, and promotable
3. **Position testing work as business impact** - frame the e2e infrastructure as "reduced contributor friction by X%, eliminated auth/bootc blind spots, cut CI debugging time" when presenting to leadership
4. **Expand scope beyond builder testing** - the ArgoCD/GitOps work is a good start. Look for testing needs across PitCrew that require coordination with other teams
5. **Start mentoring** - the testing architecture documentation is a natural mentoring vehicle. Help onboard someone on PitCrew's testing infrastructure or share testing patterns with ATC
6. **Engage in broader channels** - join #forum-jumpstarter, #forum-qe-automotive, and contribute to discussions
7. **Explore AI tools** for test generation, test result analysis, or CI optimization

---

## Principal Software Engineers (IC Level 4 - next: Senior Principal SE, IC Level 5)

### Juanje Ojeda - Principal Software Engineer, ATC

**Dimension assessment (Professional Track, Radford + Enterprise Competencies):**

- Scope [Stretching toward Level 5]: Sets and achieves objectives tied to functional targets (Level 4 - met). Agent Forge proposes new techniques adopted cross-team. Execopen pipeline spanned 5 repos with FoA coordination. Mentored Matt Goldman. Led pipelines-debugger from PoC to production adoption. Published articles on Red Hat Source and LinkedIn. Level 5 expects "mid-term objectives aligned to RH business goals, drives vision with cross-functional impact, leads professional staff as expert resource" - he's demonstrating most of this but hasn't yet positioned work as organizational strategy.
- Complexity [Stretching toward Level 5]: Independent judgment on complex, non-routine issues (6 Blockers resolved, creative agent solutions). Recognized as expert within team and increasingly across department. Leads cooperative efforts among 5+ teams for execopen. Cross-team relationships with FoA, QE, AIB. Engaged across #forum-ambient-code-platform, #forum-qe-automotive. Level 5 expects "formal networks across Red Hat to influence priorities and objectives both internally and with customers" - the #forum engagement is a start, not yet an established cross-org network.
- Impact [Gaps to address]: Contributes to functional goals through operational direction (release pipeline, agent infrastructure). Decisions impact customer and program objectives (RC1-RC3, CTC). Agent Forge emerging as reusable methodology. 28 tickets, 39 MRs. Level 5 expects "activities directly impact function's medium-to-long-term results and strategy, decisions significantly impact resource allocation" - impact remains primarily functional/tactical, not yet organizational-level strategic direction.

**Responsibilities assessment (SE Level 4):**

| # | Responsibility | Rating | Evidence |
|---|---------------|--------|----------|
| 1 | Technical Impact: Leads design for features crossing multiple subsystems | Met | 39 MRs across 7+ repositories (pac-jobs, custom-images, create-osbuild, downstream-pipelines-as-code, gator, s3pi, AI code review). Owns the pipe-x pipeline architecture spanning multiple subsystems. Led refactoring of AIB build parameter pre-computation across pac-jobs and create-osbuild (May 12 MRs). |
| 2 | Quality: Establishes and monitors testing practices across components | Met | Generalized pipeline debugger for guardrails (VROOM-44368). Fixed smoke-test infrastructure across multiple repos (VROOM-41869, 40623). Testing Farm SSL cert and timeout fixes (VROOM-41586). Repoclosure false-positive filtering for dnf4 rich deps. |
| 3 | Community: Acts as key representative advocating for customer needs | Partially met | Active on GitLab.com with 27 public MRs in the redhat/edge/ci-cd namespace. AI code review tool is publicly accessible. However, no evidence of conference talks, blog posts, or formal community advocacy during Q2. |
| 4 | Mentoring: Coaches and mentors senior engineers across teams | Partially met | Created codebase documentation skill (VROOM-40980) and applied it to gator and s3pi repos - enabling team self-service. Shared multi-agent research findings (VROOM-41514). No direct evidence of structured cross-team mentoring or coaching sessions. |
| 5 | Business Impact: Owns and delivers initiatives with visible business impact | Met | Owned RHIVOS 2.0-Core Tech Preview release work (VROOM-37951 epic). Resolved 6 Blocker tickets that were gating release and pipeline execution. Delivered RCX directory structure for releases (VROOM-38717), a structural improvement to the release process. |
| 6 | Technical Practices: Drives adoption of new tools within teams | Met | Built and deployed AI code review tool (multiple MRs in ai-code-review repo). Created wiki-kb Agent Skill for portable knowledge bases (VROOM-40491). Introduced codebase documentation agent skill used across repos. Webserver-based artifact checking replacing S3 (VROOM-40521). |
| 7 | AI Tools: Evaluates and introduces AI-driven methodologies | Met | Strongest performer on this dimension. PoC infra AI agent for pipeline diagnostics (VROOM-41536). Multi-agent memory research and documentation (VROOM-41514). Identified candidate QE multi-agent workflow (VROOM-41513). AI code review tool with internal-note filtering and synthesis suppression. AI chatbot pod deployed to Test Console infrastructure. |
| 8 | SDLC: Leads definition and implementation for complex multi-component systems | Met | Defines and maintains the pac-jobs SDLC (v0.4.0 docs sync). Architected the release promotion workflow (promote-release job with rcN directories). Owns the custom-images templating system (fusa-minimal, ps, qa templates). Manages downstream-pipelines-as-code lifecycle. |

**Skills assessment (SE Level 4):**

| # | Skill | Rating | Evidence |
|---|-------|--------|----------|
| 1 | Technical Acumen | Strong | Expert across the full pipe-x ecosystem: pac-jobs, custom-images, create-osbuild, downstream-pipelines-as-code, infrastructure, gator, s3pi. Additionally proficient in AI/agent tooling (code review, chatbot, multi-agent patterns). 39 MRs spanning 7+ repos demonstrates multi-area mastery. |
| 2 | Quality Management | Adequate | Builds quality tooling for the pipeline ecosystem (debugger, smoke tests, repoclosure). However, evidence of architecting frameworks adopted by teams outside ATC is limited. Quality work is deep but scoped primarily to the pipe-x/RHIVOS pipeline. |
| 3 | System Design | Strong | Designed the AIB parameter pre-computation architecture across pac-jobs and create-osbuild. Architected the templated manifest system for custom-images (GPT/non-GPT differentiation, board-specific generators). Pipeline debugger generalization for guardrails shows system-level design thinking. |
| 4 | Communication | Adequate | Documentation MRs for pac-jobs v0.4.0 and CLAUDE.md optimization. Codebase documentation generated for gator and s3pi. No evidence of presentations to leadership or stakeholders, or external communication (blog posts, talks) during Q2. |
| 5 | Collaboration | Strong | Cross-repo work on both internal GitLab (12 MRs) and public GitLab.com (27 MRs). Contributions span ATC toolchain (pipe-x), QE (gator), and infrastructure. Work on Testing Farm integration and Test Console shows cross-team touchpoints. |
| 6 | Leadership | Adequate | Sets technical direction for the pipe-x ecosystem and drives AI innovation for the team. However, structured coaching of senior engineers is not evidenced. Leadership is demonstrated through technical output rather than explicit mentoring or direction-setting for others. |
| 7 | Business Impact | Strong | RHIVOS 2.0-Core TP release ownership. 6 Blocker tickets resolved, directly unblocking product delivery. Release infrastructure improvements (rcN directories, promote-release fixes) with lasting business value. |
| 8 | Continuous Learning | Strong | Leading the team in AI agent adoption: multi-agent memory research, QE agent workflows, infra AI agent PoC. Self-directed learning in agentic patterns and applying them to engineering problems. Active adoption of new tooling patterns across repos. |
| 9 | Influence | Adequate | Influences the pipe-x technical roadmap and AI adoption direction within ATC. Less evidence of influence on broader organizational roadmaps or cross-BU decision-making during Q2. |
| 10 | Knowledge Sharing | Adequate | Codebase documentation skill and its application to multiple repos. pac-jobs v0.4.0 documentation. Multi-agent research sharing (VROOM-41514). No evidence of conference presentations, blog posts, or formal training during Q2. |

**Disconfirmation gate (assessed 2026-06-29):**

Question: Is Juanje ready for promotion to IC Level 5?

Contradicting evidence sought and found:
- Impact remains primarily functional/tactical, not yet organizational-level strategic direction. Agent Forge has organizational potential but hasn't been positioned or recognized as organizational strategy
- Customer Focus at Advanced is unmet - no external customer engagement evidence
- External conference presentations are missing - internal demos are strong but Level 5 expects external visibility
- Cross-org influence is emerging but not yet "formal networks across Red Hat to influence priorities." The #forum-ambient-code-platform engagement is a start, not an established network
- Sustained consistency is unproven - Level 5 behaviors emerged in Q2 but need to be demonstrated consistently over multiple quarters

Conclusion: Not yet ready for promotion. Juanje is on a clear trajectory from Level 4 to Level 5, with multiple Level 5 behaviors already demonstrated. The gaps are specific and addressable: organizational-level impact positioning, external visibility, cross-org network formalization, and customer-impact articulation. With deliberate action on 2-3 of these areas over the next 1-2 quarters, the promotion case would be substantially stronger.

**Already demonstrating at IC Level 5:**
- *AI methodology innovation:* Infra AI agent PoC (VROOM-41536), multi-agent QE workflow identification (VROOM-41513), and AI code review tool represent next-level technical vision applied across teams
- *Release pipeline ecosystem ownership:* Pipe-x with architectural decisions that shape how multiple teams build, test, and ship - L5-scope system stewardship
- *Cross-team enablement through tooling:* Agent Forge, codebase-documenter skill, wiki-kb skill, Pi npm packages, CI job templates - builds things others pick up and extend
- *Technical strategy across teams:* Agent Forge is a reusable framework adopted cross-team. Execopen pipeline integration spanned 5 repositories with FoA coordination

**Growth areas for IC Level 5:**
- *External visibility:* L5 expects recognized technical leadership beyond the immediate organization. Conference talks, blog posts, or upstream community leadership would strengthen this dimension
- *Cross-team mentoring:* L5 requires coaching principal-level engineers across teams. Formalizing the knowledge sharing (documentation skills, AI patterns) into structured mentoring would close this gap
- *Organizational influence:* L5 expects influencing roadmaps at the BU or product level. Translating technical insights into strategic proposals for leadership would demonstrate this
- *Customer-facing impact articulation:* Connect infrastructure work to customer outcomes - pipeline reliability enabling faster customer-facing releases, FuSa traceability meeting automotive compliance

**Recommended development path:**
1. **Write a strategic proposal for the agent practice** - 2-3 page document positioning Agent Forge and the pipelines-debugger as an engineering methodology for the organization. Include business metrics (incident resolution time before/after, engineering hours saved). Present to leadership
2. **Submit a conference proposal** - DevConf.cz or Red Hat Summit. Topic: "AI Agents for CI/CD Pipeline Diagnosis: From Idea to Production in One Quarter"
3. **Establish a cross-org consulting relationship** - identify 1-2 teams outside Automotive exploring AI agents. Offer to consult on their agent design
4. **Connect technical work to customer outcomes** - explicitly articulate how pipeline reliability enables faster customer-facing releases, how FuSa traceability meets automotive compliance
5. **Document SDLC methodology change** - short internal article on how agent-driven pipeline diagnosis changes the SDLC. Position as methodology innovation

*Full development brief with 1:1 talking points: `agent_brain/projects/talent-architecture/active/juanje.ojeda/2026-06-29-development-brief.md`*

---

### Benny Zlotnik - Principal Software Engineer, PitCrew

**Dimension assessment (Professional Track):**

- Scope [Level 4]: Works independently to achieve objectives across all PitCrew workstreams. De facto first responder in jumpstarter community (281 messages in #forum-jumpstarter). Proposes and delivers new methods (CA support for u-boot, OCI flashing, Vault migration). Coordinates others reactively through community engagement. Needs to shift from reactive to directive to reach Level 5 "drives vision and innovation."
- Complexity [Level 4, trending 5]: Independent judgment on complex, varied issues spanning every PitCrew workstream. Recognized as expert within PitCrew and the jumpstarter ecosystem. Leads cooperative efforts among teams (897 msgs, 17 channels). Cross-team relationships are strong. Approaching Level 5's "formal networks across Red Hat to influence priorities" - already acts as a connective hub.
- Impact [Level 4]: Contributes to functional goals through broad operational delivery. Decisions impact program objectives (jumpstarter releases, security, CTC). Not yet at Level 5 "directly impacts function's medium-to-long-term results and strategy" - his impact is tactical breadth rather than strategic direction.

**Responsibilities assessment (SE Level 4):**

| # | Responsibility | Rating | Evidence |
|---|---------------|--------|----------|
| 1 | Technical Impact: Leads design for features crossing multiple subsystems | Met | Dual ownership of jumpstarter AND builder (automotive-dev-operator) - two distinct subsystems. CTC integration work (PITCREW-443, 444) bridges testing infrastructure with both. OCI flashing for qemu (PITCREW-356) spans jumpstarter core and virtualization layer. Ford PaaC workflow (PITCREW-349) crosses build and flash subsystems. |
| 2 | Quality: Establishes and monitors testing practices across components | Met | Manifest validation (PITCREW-446), shellcheck validation for build scripts (PITCREW-447), cosign signature verification for Tekton Bundles (PITCREW-380). These are quality gates applied across the builder pipeline. CTC autobump tmt (PITCREW-443) keeps testing framework aligned. |
| 3 | Community: Acts as key representative advocating for customer needs | Met | 281 messages in forum-jumpstarter - de facto community leader for the jumpstarter project. 88 messages in forum-rhivos-dut supporting hardware lab users. GitHub upstream contributions to jumpstarter-dev/jumpstarter. Active cross-team presence in ATC and QE channels. |
| 4 | Mentoring: Coaches and mentors senior engineers across teams | Partially met | De facto team focal point with 366 messages in team-pitcrew-automotive (highest volume). 64 messages responding to alerts across channels suggests coaching-through-doing. README improvements (PITCREW-375) enable self-service. However, no explicit evidence of structured cross-team mentoring. |
| 5 | Business Impact: Owns and delivers initiatives with visible business impact | Met | Ford customer enablement (PITCREW-349 PaaC workflow). NXP hardware support in TC pipelines (PITCREW-444). EBBR images for Renesas RCar S4 (VROOM-38945). Highest ticket throughput on the team (30 closed). Each of these directly enables customer or product delivery. |
| 6 | Technical Practices: Drives adoption of new tools within teams | Met | Vault secrets migration (PITCREW-373) - organizational security tooling. Prometheus metrics integration (PITCREW-361). Tracing and log ingestion setup (PITCREW-364). Private registry support for workspaces (PITCREW-392). Each introduces new tooling to the PitCrew/RHAS ecosystem. |
| 7 | AI Tools: Evaluates and introduces AI-driven methodologies | Gap | No evidence of AI tool evaluation or adoption during Q2. No tickets or MRs related to AI-driven methodologies, LLM tooling, or AI-assisted workflows. This is the primary gap against the L4 job description. |
| 8 | SDLC: Leads definition and implementation for complex multi-component systems | Met | Builder operator lifecycle management (container build expiration, format validation, quiet mode, error improvements). Jumpstarter release processes (token rotation, lease management, exporter access policies). Ford PaaC workflow defines a build-flash SDLC for a customer. |

**Skills assessment (SE Level 4):**

| # | Skill | Rating | Evidence |
|---|-------|--------|----------|
| 1 | Technical Acumen | Strong | Expert across jumpstarter (core platform, exporter, leasing, flashing), builder/automotive-dev-operator (Kubernetes operator, Tekton, container builds), CTC/Testing Farm integration, and hardware enablement (NXP, RCar S4, RIDE4, qemu). Rare breadth across firmware, platform, and cloud-native stacks. |
| 2 | Quality Management | Adequate | Introduced validation tooling (shellcheck, manifest validation, cosign verification) within PitCrew scope. These are solid quality gates but scoped to PitCrew projects rather than frameworks adopted by multiple teams. |
| 3 | System Design | Strong | Observability stack architecture (Prometheus + tracing + log ingestion) for the builder platform. Jumpstarter exporter access policy with CA support. OCI flashing architecture for qemu virtualization. Each demonstrates multi-component system design. |
| 4 | Communication | Strong | 897 Slack messages across 17 channels - highest volume on the team. Sustains active presence in team, community, and alert channels simultaneously. README improvements show written communication investment. Responsive communication pattern (64 alert channel messages). |
| 5 | Collaboration | Strong | Active across ATC channels (toolchain, test-console, image-builder), QE channels, DUT lab, and PitCrew. 17-channel Slack footprint shows broad cross-team relationships. Ford customer work requires external collaboration. Alert responsiveness (35+29 messages) shows reliability as a cross-team partner. |
| 6 | Leadership | Adequate | De facto technical leader for jumpstarter and builder. Drives direction through high-volume output (30 tickets, highest Slack). However, leadership is demonstrated primarily through individual contribution rather than explicit direction-setting or delegation to others. |
| 7 | Business Impact | Strong | Ford customer enablement is direct revenue-adjacent work. NXP and EBBR hardware support expand the RHIVOS platform footprint. 30 closed tickets is the highest throughput on the team, directly enabling product velocity. |
| 8 | Continuous Learning | Adequate | Adopted new tools (Vault, Prometheus, tracing) within Q2. However, the AI Tools gap indicates an area where learning investment has not yet been directed. Continuous learning is strong in infrastructure tooling but narrow in emerging methodology. |
| 9 | Influence | Adequate | Jumpstarter community influence (281 forum messages). Technical decisions in builder and jumpstarter shape those projects' direction. Less evidence of influencing broader organizational or product-level roadmaps during Q2. |
| 10 | Knowledge Sharing | Adequate | README improvements (PITCREW-375). Community support in forum-jumpstarter and forum-rhivos-dut. Error message improvements (PITCREW-421, 431) are a form of knowledge sharing. No evidence of design documents, blog posts, or conference presentations during Q2. |

**Already demonstrating at IC Level 5:**
- *Cross-subsystem ownership:* Jumpstarter + builder + CTC with breadth and depth expected at L5 - few engineers span firmware flashing, Kubernetes operators, and cloud-native testing infrastructure simultaneously
- *Community leadership:* Forum-jumpstarter (281 messages) and forum-rhivos-dut (88 messages) positions him as a recognized go-to expert beyond his immediate team
- *Customer-facing delivery:* Ford PaaC workflow demonstrates business impact awareness that L5 requires

**Growth areas for IC Level 5:**
- *AI Tools adoption:* L5 expects championing AI-driven methodologies across the organization. This is currently a gap at L4 level that needs to be addressed before L5 readiness. Start with evaluating AI-assisted testing or code review tools for jumpstarter/builder workflows
- *External visibility:* L5 requires recognized technical leadership beyond the organization. Conference talks, blog posts about jumpstarter/builder architecture, or upstream community governance roles would strengthen this dimension
- *Formal mentoring:* L5 requires coaching principal engineers across teams. The high Slack volume suggests informal mentoring is happening - formalizing it with structured sessions would make it visible and scalable
- *Strategic technical direction:* Benny delivers across all areas but hasn't articulated or led a technical strategy. His work is responsive (fixing, building, supporting) rather than directive (setting direction)
- *Written knowledge sharing:* Benny's knowledge sharing is all real-time in Slack. He needs durable artifacts - design documents, blog posts, conference presentations

**Recommended development path:**
1. **Write a technical strategy document** - Benny has the deepest knowledge of jumpstarter and PitCrew systems. Write a 6-month technical roadmap or architecture proposal for jumpstarter evolution. This is the single most important step for Level 5
2. **Formalize knowledge sharing** - convert his Slack expertise into blog posts or design documents. Even one article on jumpstarter architecture or the builder security model would be significant
3. **Present at a conference** - DevConf, Red Hat Summit, or jumpstarter community events. His deep jumpstarter expertise makes him a natural speaker
4. **Establish cross-org mentoring** - mentor someone outside PitCrew on jumpstarter or builder patterns
5. **Explore AI tooling strategy** - evaluate how AI tools could improve PitCrew's workflows (test automation, builder diagnostics) and propose an adoption strategy
6. **Shift from reactive to directive** - instead of responding to all requests, identify and propose the top 3 architectural improvements for PitCrew and drive them proactively

---

### Roderick Kieley - Principal Software Engineer, PitCrew

**Note:** Roderick joined the PitCrew/RHAS team on June 1, 2026. This assessment covers approximately 3 weeks of onboarding (June 1-21). Many dimensions have insufficient evidence due to this limited period, which should not be interpreted as gaps - it reflects the expected ramp-up phase for a new team member.

**Dimension assessment (Professional Track):**

- Scope [Too early]: 21 working days. First code contribution landed. Community engagement in AI/agent forums suggests he will quickly establish Level 4 scope once domain depth is built.
- Complexity [Too early]: Prior career level suggests principal-level judgment and expertise, but RHIVOS domain expertise is still developing. Broad AI/agent community connections signal he will bring cross-functional relationships.
- Impact [Too early]: No Jira tickets yet (expected for onboarding). Impact assessment deferred to Q3.

**Responsibilities assessment (SE Level 4):**

| # | Responsibility | Rating | Evidence |
|---|---------------|--------|----------|
| 1 | Technical Impact: Leads design for features crossing multiple subsystems | Insufficient evidence | One GitHub PR merged (agentic-collections) during onboarding. No Jira tickets resolved - expected for the first 3 weeks. Too early to assess cross-subsystem design leadership in the new role. |
| 2 | Quality: Establishes and monitors testing practices across components | Insufficient evidence | No testing-related contributions during the onboarding period. Assessment deferred to next quarter when ramped up. |
| 3 | Community: Acts as key representative advocating for customer needs | Insufficient evidence | Self-input references 10 years of Red Hat impact, Gaming Development CoP (arcade.redhat.com), O3DE investment, and Fedora SIG-Robotics interest. These indicate community orientation, but no Q2 evidence in the PitCrew/RHAS context yet. |
| 4 | Mentoring: Coaches and mentors senior engineers across teams | Insufficient evidence | Currently in learning mode as a new team member. Self-input mentions prior management track experience, which suggests mentoring capability. No evidence of mentoring in the new role during Q2. |
| 5 | Business Impact: Owns and delivers initiatives with visible business impact | Insufficient evidence | Onboarding phase - no initiative ownership yet. Self-input shows strong business awareness: long-term goal to grow RHAS with customer backlog from large, medium, and smaller customers. |
| 6 | Technical Practices: Drives adoption of new tools within teams | Insufficient evidence | agentic-collections PR suggests interest in AI/agent tooling space. Too early to assess tool adoption leadership in the team. |
| 7 | AI Tools: Evaluates and introduces AI-driven methodologies | Insufficient evidence | First contribution was to agentic-collections - a positive early signal of AI/agentic tooling interest. Self-input does not mention AI tools explicitly, but the contribution direction is encouraging. |
| 8 | SDLC: Leads definition and implementation for complex multi-component systems | Insufficient evidence | No SDLC-related contributions during onboarding. Assessment deferred to next quarter. |

**Skills assessment (SE Level 4):**

| # | Skill | Rating | Evidence |
|---|-------|--------|----------|
| 1 | Technical Acumen | Insufficient evidence | Self-input references 10 years of technical growth at Red Hat and interest in O3DE, robotics simulation, and edge computing. No technical contributions in the new role during Q2 beyond one PR. Prior background suggests capability; current role evidence pending. |
| 2 | Quality Management | Insufficient evidence | No quality-related work observed during onboarding period. |
| 3 | System Design | Insufficient evidence | No system design contributions during onboarding. Self-input mentions interest in O3DE as robotics simulation platform and Fedora SIG-Robotics business case, suggesting systems-level thinking. |
| 4 | Communication | Developing | 19 Slack messages in 3 weeks, with 18 in the team channel. Appropriate onboarding communication pattern - present and engaged but still absorbing. Self-input response is articulate and strategic in framing career goals. |
| 5 | Collaboration | Developing | Focused on team-pitcrew-automotive channel (18/19 messages). Good engagement rate for a new joiner - actively participating rather than silently observing. 1:1 meetings with manager documented (Jun 1, Jun 11). |
| 6 | Leadership | Insufficient evidence | Self-input mentions transition from a management track ("seemed like a sensible plan to soon be senior manager") to PSE role. Leadership capability is implied but not yet demonstrated in the new team context. |
| 7 | Business Impact | Insufficient evidence | Strong business awareness in self-input: identifies RHAS customer growth as long-term goal, sees Fedora SIG-Robotics as industrial edge expansion opportunity. Impact delivery pending ramp-up completion. |
| 8 | Continuous Learning | Developing | agentic-collections contribution within first 3 weeks shows initiative to learn and contribute quickly. O3DE and robotics simulation interests indicate active learning outside immediate role scope. Currently in the steepest learning curve phase. |
| 9 | Influence | Insufficient evidence | No evidence of roadmap influence in the new team during Q2. Self-input mentions prior influence trajectory. Assessment requires more time in the role. |
| 10 | Knowledge Sharing | Insufficient evidence | No knowledge sharing contributions during onboarding. Self-input mentions Gaming Development CoP and arcade.redhat.com - prior knowledge sharing vehicles. Assessment deferred. |

**Already demonstrating strengths:**
- *Strategic thinking:* Visible in the self-input - connecting O3DE to robotics simulation, identifying Fedora SIG-Robotics as a business case for industrial edge expansion, and framing RHAS growth in terms of customer segment diversity. This is the kind of business-technical synthesis L5 requires
- *Community engagement:* Already in #forum-mcp, #forum-ai-agent-builders, #wg-agent-eval-harness, #appeng-ai5-marketplace, #lounge-homelab - broader AI community engagement than most established engineers
- *Collaborative approach:* 29/44 messages are thread replies (deep engagement, not broadcast). Verifies claims with citations

**Growth areas (focus on establishing Level 4 baseline first):**
- *Establish L4 baseline:* The immediate priority is completing onboarding, resolving first tickets, and demonstrating cross-subsystem technical impact in the PitCrew/RHAS context. L5 readiness assessment is premature before L4 competencies are demonstrated in the new role
- *Translate prior experience:* Self-input references 10 years of Red Hat impact and management-track experience. Channeling that organizational knowledge into visible technical leadership (design documents, architecture proposals, community engagement) in the RHAS space will be the path to L5
- *AI Tools:* No evidence yet. Given the team's direction toward agentic testing and AI-assisted workflows, early engagement with AI tooling during ramp-up would position well for both L4 requirements and L5 readiness

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

**Responsibilities assessment (SRE Level 4):**

| # | Responsibility | Rating | Evidence |
|---|---------------|--------|----------|
| 1 | Lead the development of code and automation scripts to optimize scalability, reliability, and performance of services | Demonstrated | 4 internal GitLab MRs merged (pipe-x/infrastructure, toolchain-chatbot, auto-toolchain-dashboard) and 3 GitLab.com MRs (custom-images CI/CD, automotive-image-builder). VROOM-41378 updated CI testing and logic for custom-images. VROOM-41213 spike investigating sed-to-jinja2 migration shows initiative toward maintainable automation. |
| 2 | Conduct thorough code reviews and implement best practices in software development | Limited Evidence | The jinja2 migration investigation (VROOM-41213) demonstrates best-practices thinking - moving from fragile sed scripts to templating. MR activity across 3 projects implies code review participation, but no direct review metrics available in this period. |
| 3 | Mentor and guide junior engineers, fostering continuous learning and improvement | Not Yet Observable | As a new team member (~2.5 months), mentoring is not expected yet. Matt is still in onboarding and learning the team's systems. This will become assessable in future quarters. |
| 4 | Design and implement advanced monitoring and alerting systems to proactively detect and resolve issues | Developing | 12 messages in alerts-auto-toolchain channel show active engagement with existing alerting. VROOM-41383 addressed critical container vulnerabilities detected through monitoring. No evidence yet of designing new monitoring systems, which is expected given tenure. |
| 5 | Coordinate and lead complex incident response procedures with thorough postmortems | Developing | VROOM-41192 (AIB CI is failing, Major priority) shows incident response capability - identified and fixed a CI system failure. VROOM-41383 critical vulnerability response (VHCL-005) demonstrates urgency-appropriate action. No postmortem evidence yet. |
| 6 | Interface with internal stakeholders and external cloud providers to architect fault-tolerant systems | Developing | VROOM-40737 (CloudFront domain configuration for download.rhivos.auto-toolchain.redhat.com) is direct cloud provider interface work. Infrastructure MRs in pipe-x suggest stakeholder coordination. Early stage but relevant contributions. |
| 7 | Manage large-scale, distributed systems, focusing on minimizing downtime and improving resilience | Limited Evidence | Infrastructure contributions to pipe-x and toolchain services (chatbot, dashboard) touch distributed system components. 88 messages in wg-team-auto-toolchain-infra (59% of all Slack activity) confirm infrastructure is the primary focus area. Specific resilience improvements not yet documented. |
| 8 | Participate in on-call rotation and provide leadership during critical incidents for 24x7x365 support | Limited Evidence | Alert channel activity (12 messages in alerts-auto-toolchain) suggests awareness and responsiveness. On-call rotation participation not directly evidenced in available data. The two Major-priority fixes (VROOM-41192, VROOM-41383) show willingness to handle urgent issues. |
| 9 | Lead the continuous enhancement of the SRE team's processes, tools, and methodologies | Developing | VROOM-40779 spike investigating GitLab Review Apps for Test Console shows process improvement thinking. The jinja2 migration spike (VROOM-41213) targets tooling modernization. Both are investigative contributions appropriate for onboarding phase - the "lead" aspect will grow with tenure. |

**Skills assessment (SRE Level 4):**

| # | Skill | Rating | Evidence |
|---|-------|--------|----------|
| 1 | Linux Systems Management | Demonstrated | Contributions to automotive-image-builder (GitLab.com MRs), custom-images work (VROOM-41378), and infrastructure projects all require Linux systems expertise. Image building and CI work are Linux-native activities. |
| 2 | Infrastructure as Code (IaC) | Demonstrated | pipe-x/infrastructure MRs, custom-images CI/CD contributions, and the jinja2 templating investigation (moving from imperative sed to declarative templating) directly exercise IaC skills. |
| 3 | Enterprise Monitoring and Observability | Developing | Active in alerts-auto-toolchain (12 messages). Responded to critical vulnerability alerts (VHCL-005). Consumer of monitoring systems; not yet evidence of designing or extending observability infrastructure. |
| 4 | Distributed Systems Engineering | Developing | Work spans multiple services (toolchain-chatbot, auto-toolchain-dashboard, infrastructure, image-builder) - understands the distributed landscape. CloudFront configuration (VROOM-40737) is a distributed systems concern. Deeper architectural contributions expected as tenure grows. |
| 5 | Incident Management | Demonstrated | Two Major-priority incidents resolved: AIB CI failure (VROOM-41192) and critical container vulnerabilities (VROOM-41383/VHCL-005). Both required diagnosis, prioritization, and timely resolution. |
| 6 | Cloud Architecture | Developing | CloudFront domain configuration (VROOM-40737) is direct cloud architecture work. Custom-images CI/CD touches cloud build infrastructure. Still early in demonstrating end-to-end cloud architecture ownership. |
| 7 | Programming and Scripting | Demonstrated | 7 MRs merged across internal GitLab and GitLab.com in 2.5 months. Contributions span Python services (toolchain-chatbot), CI scripts (custom-images), and infrastructure automation. Productive output for onboarding period. |
| 8 | Security Best Practices | Demonstrated | VROOM-41383 directly addressed critical container vulnerabilities in toolchain-chatbot and auto-toolchain-dashboard running in MP+. Proactive security response within the first months on the team. |

**Already demonstrating strengths:**
- *Fast ramp-up and multi-domain impact:* 6 tickets resolved across 5 different domains (custom-images, chatbot, dashboard, CI, CloudFront) in 2.5 months, including 2 Major-priority items. This breadth is characteristic of senior-level engineers who quickly map a new landscape
- *Investigation-driven improvements:* Two spikes (jinja2 migration, Review Apps) show the habit of questioning existing approaches rather than just maintaining them - a Level 5 trait of driving architectural evolution
- *Transparency:* "Thinks out loud during debugging sessions, narrates full investigation in real time including dead ends" - exceptional Level 4+ communication pattern
- *Collaboration quality:* "Gracefully withdraws proposals when stronger arguments presented" - mature collaborative behavior

**Growth areas for SRE Level 5:**
- *Mentoring and knowledge sharing:* Expected to develop as Matt moves past the onboarding phase. Level 5 requires actively guiding others and establishing team practices
- *Monitoring and observability design:* Current engagement is responsive (alert channels). Level 5 expects designing and implementing monitoring strategies, not just consuming them
- *Incident leadership with postmortems:* Matt has resolved incidents; the next step is leading the postmortem process and turning incidents into systemic improvements
- *Cloud architecture ownership:* CloudFront work is a good start. Level 5 expects architecting fault-tolerant systems end-to-end, including capacity planning and disaster recovery design
- *Cross-team visibility:* Slack activity is heavily concentrated in infra (59%). Expanding engagement with gating, pipelines, and QE channels would demonstrate the broader influence expected at Level 5

**Recommended development path (Q3-Q4 focus):**
1. **Deepen domain expertise** - own a major infrastructure component end-to-end (custom-images is a natural fit based on Q2 work). Understand the full pipeline from build to release
2. **Lead one reliability improvement** - pick an operational pain point (CI reliability, monitoring gaps, deployment process) and drive it from diagnosis to solution
3. **Build cross-team relationships** - engage more with Eitan (shared infrastructure domain), Juanje and Roni (pipeline/testing intersections)
4. **Document infrastructure patterns** - the jinja2 investigation and Review Apps spike suggest architectural thinking. Write these up as formal proposals
5. **Establish mentoring** - once domain expertise is solid (Q4), start mentoring newer team members on SRE patterns
6. **Start contributing to SRE community** - join Red Hat internal SRE forums, share learnings from automotive infrastructure

---

## Principal Quality Engineer (IC Level 4 - next: Senior Principal QE, IC Level 5 or SE transition)

### Roni Eliezer - Principal Software Quality Engineer, ATC

**Note:** Using the Quality Engineer IC Progression Matrix and the Professional Track dimensions for Roni's development path. However, Roni's actual work aligns more closely with the SE progression matrix (see QE-to-SE transition section below).

**Dimension assessment (Professional Track - QE):**

- Scope [Level 4-5]: Works independently to set and achieve objectives (Test Console platform, CTC pipeline, AI analysis). Proposes new techniques (AI-powered test analysis, Gemini transitions, packages.redhat.com PoC) with impact within the function. Coordinates CTC activities for RC1-RC3 as functional team lead. 199 mentions by others - acts as expert resource. Cross-team feedback from Yariv (BOA team) explicitly recognizes Roni as a "vital collaborative anchor" across Toolchain, Jumpstarter, and BoA, with Multiplier behaviors at the Advanced level. Willing to mentor and assist others to begin contributing to Test Console. Approaching Level 5 "drives vision and innovation with cross-functional impact" through Test Console's central role and cross-team enablement.
- Complexity [Level 4, trending 5]: Independent judgment on complex, non-routine issues (3 Gemini model transitions, fallback mechanisms, long-standing Blocker-level security fix). Recognized as expert within team - primary Test Console owner. Productive relationships within function (QE automotive, testing-farm, PitCrew). Leading cooperative efforts across QE teams. BOA team feedback confirms cross-team expert recognition beyond immediate team. Approaching "subject matter expert advising on strategy" (Level 5).
- Impact [Level 4, trending 5]: Contributes to functional goals through operational direction of testing infrastructure. Decisions impact program objectives (CTC certification timeline, release readiness). Serves as de facto project lead for Test Console and CTC pipeline. Through Test Console, scales individual Multiplier behaviors to elevate multiple teams (Yariv: "scales these behaviors to elevate the effectiveness of multiple teams integrated under one product"). Approaching Level 5 "directly impacts function's medium-to-long-term results" - Test Console IS the testing infrastructure strategy.

**Responsibilities assessment (QE Level 4):**

| # | Responsibility | Rating | Evidence |
|---|---------------|--------|----------|
| 1 | Lead the design and development of complex test automation frameworks and testing strategies | Strong | Test Console is a full-stack test automation platform that Roni co-leads (confirmed by Rachel Sibley). 43 MRs merged this quarter across backend, frontend, and CLI. Key framework advances: Flask-to-FastAPI migration (modern async architecture), JMESpath-based CTC advanced filtering (VROOM-44576 area), and TC-as-MCP-server conversion enabling AI-driven test orchestration. CTC scheduling for RC1, RC2, RC3 releases demonstrates strategic test planning at the program level. |
| 2 | Coordinate the activities of a team of engineers to ensure successful test delivery and bug resolution | Strong | Yariv Rachmani describes Roni as a "collaborative anchor across three distinct teams: Toolchain, Jumpstarter, and BoA." Coordinated DPAC integration with Ozan and Juanje (env-var APIs, enable/disable jobs). Coordinated bootc-testing requirements with Martin Perina and implementation with Benny and Bella. Scheduled and configured CTC runs for RC1, RC2, RC3 releases (VROOM-44653). 40 messages in team-pitcrew-automotive show active cross-team coordination. |
| 3 | Apply creative problem-solving to resolve complex bugs and system integration issues | Strong | AI report improvement is a standout example: discovered junit_results.xml contains script output missing from pipeline.log, converted XML to JSON for better Gemini processing, built failover logic when files are missing or too large (VROOM-41587). Fixed Testing Farm qemu_kvm vs qemu mismatch (VROOM-44397). Resolved report-portal upload exception (VROOM-40488). Fixed CTC duplicate VM runs (VROOM-38589). 32 tickets closed - highest on the team. |
| 4 | Mentor and provide guidance to new team members on advanced testing practices | Demonstrated | Yariv Rachmani: "Roni is willing to mentor and assist others to begin contributing to TestConsole." The MCP server conversion and API docstring improvements (VROOM-41913) lower the barrier for others to interact with TC programmatically. Meital Arki development feedback suggests increasing visibility through demos - indicating mentoring is present but could scale further. |
| 5 | Collaborate with cross-functional teams to enhance test coverage and ensure product quality | Strong | Cross-functional work is a defining characteristic: worked with Akhil Kohli on AWS Graviton 3 CPU support; with Ozan/Juanje on DPAC integration; with Martin Perina, Benny, and Bella on bootc-testing/Jumpstarter; with Testing Farm team on hardware target APIs. Slack presence across 17 channels including testing-farm (16 msgs), forum-dno-datarouter (8), forum-qe-automotive (43). Rachel Sibley and Yariv Rachmani both highlight cross-team impact. |
| 6 | Design, implement, and manage CI/CD pipelines and best practices | Demonstrated | Added SonarQube to frontend CI pipeline. Configured container-base auto-build on merge to main. Added auto-qe bot API token for TC CI/CD pipeline (VROOM-44591). Managed CI pipeline behavior: skipping SonarQube issues post-FastAPI merge, disabling CTC during Polarion maintenance. These are practical CI/CD management actions, though not large-scale pipeline architecture. |
| 7 | Advocate and ensure customer-focused testing by incorporating real-world usage scenarios | Demonstrated | AWS Graviton 3 CPU support was driven by a direct stakeholder requirement from Akhil Kohli. NXP support (VROOM-44570) fixed a regression affecting a real hardware partner. RHIVOS images at packages.redhat.com POC (VROOM-41526) addresses customer-facing distribution. Developer-vm image definitions (VROOM-38827) improve internal developer experience. Developer images release fix (VROOM-40519) prevented incorrect customer-facing releases. |
| 8 | Identify risks and contribute to mitigation planning | Demonstrated | Resolved a Blocker-priority security input validation issue (VROOM-28392: SEC-APP-REQ-1). Prepared reduced test plan list for RC3 CTC (VROOM-44576) - a risk-based scoping decision. Disabled CTC during Polarion maintenance to prevent false failures. Added DB import/export scripts for production debugging and future backup. Fixed developer images being released to customers (VROOM-40519) - caught a distribution risk. |
| 9 | Proactively leverage AI technologies to streamline workflows and enhance efficiency | Strong | Standout area. Converted TC backend to an MCP server by migrating Flask to FastAPI and using FastAPI add-on to auto-export APIs as MCP tools. Improved AI log analysis accuracy through three innovations: using junit_results.xml instead of pipeline.log, XML-to-JSON conversion for Gemini, and failover logic (VROOM-41587). Migrated from gemini-2.5-flash to gemini-3.5-flash (VROOM-42530). Handled Gemini 429 rate-limiting with retry logic (VROOM-40836). Updated API docstrings specifically to improve MCP tool quality (VROOM-41913). Collaborated on BOA/TC AI Chatbot initiative with Meital Arki. |
| 10 | Proactively utilize AI-assisted tools for code generation, test design, automation, and peer review | Strong | The MCP server conversion makes the entire Test Console platform accessible to AI agents for automated test orchestration. API docstring improvements (VROOM-41913) were specifically aimed at improving LLM tool usage. The AI log analysis pipeline (Gemini-based) automates failure root cause analysis. Meital Arki confirms "strong AI knowledge and curiosity" from their AI Chatbot collaboration. |

**Skills assessment (QE Level 4):**

| # | Skill | Rating | Evidence |
|---|-------|--------|----------|
| 1 | Problem Solving | Strong | Multiple instances of creative, multi-layered problem solving. The AI report improvement combined three insights (better input source, format conversion, failover) into one solution. The qemu_kvm/qemu mismatch fix (VROOM-44397) required understanding the gap between internal naming and Testing Farm's API contract. JMESpath adoption for CTC filtering found the "simplest and best" tool for flexible test selection. Meital Arki: "ability to look at problems from multiple angles and propose constructive approaches." |
| 2 | Team Leadership | Demonstrated | Rachel Sibley: "technical leader and fantastic teammate," "co-leading the Test Console development work." Yariv Rachmani: "collaborative anchor across three distinct teams" with "Advanced level Multiplier" competency. 497 Slack messages across 17 channels with heavy presence in team coordination channels. Active in forum-qe-automotive (43 msgs) contributing to the broader QE community. Development area per Meital: could increase visibility of work through demos and broader discussions. |
| 3 | Performance Tuning | Demonstrated | VROOM-41908: Identified and fixed TC UI performance issue by excluding runner_status and log from default data fetches, loading them on demand only. XML-to-JSON conversion for Gemini API calls improved both processing reliability and response quality. SonarQube integration in frontend CI catches performance-related code quality issues. |
| 4 | System Debugging | Strong | 32 tickets closed, many involving system-level debugging: report-portal upload exception (VROOM-40488), test-console-db pod startup failure (VROOM-41342), VM provisioning "fail to fetch" errors (VROOM-42477), AutoSD flow not running, missing return in MR 737. The DB import/export scripts were created specifically to enable local reproduction of production issues. Debugging spans backend, frontend, CI, and integration boundaries. |
| 5 | Automation Frameworks | Strong | Test Console is itself a comprehensive automation framework: backend (Flask-to-FastAPI migration), frontend, CLI client (tc-cli), CTC scheduling, Jumpstarter integration, Testing Farm integration, Polarion exports, and now MCP server capability. 43 MRs merged, predominantly in the test-console project. The platform serves as infrastructure for the entire RHIVOS test automation workflow. |
| 6 | CI/CD Frameworks | Demonstrated | SonarQube addition to frontend CI. Container-base auto-build on main merge. TC CI/CD pipeline management (auto-qe bot token, Polarion maintenance handling). CTC scheduling for release candidates. Practical CI/CD expertise applied to the Test Console platform's own delivery pipeline. |

**QE-to-SE career track transition note:** Roni's Q2 work is overwhelmingly software engineering: Flask-to-FastAPI migration, MCP server architecture, API design (enable/disable jobs, CPU support, env-var update), frontend performance optimization, AI pipeline engineering. His self-input confirms this - his top accomplishment is converting TC into an MCP server through a full framework migration. Peer feedback reinforces it: Rachel calls him "an absolute powerhouse" co-leading "Test Console development work"; Meital highlights "AI knowledge" and "practical solutions." The July 2026 talent cycle guidance from Tashana explicitly opens a QE-to-SE transition path (QE and SE do not map 1:1; transitioning often represents a promotion in expectations and compensation). His work already aligns with the SE Level 4 progression matrix.

**Already demonstrating at QE Level 5:**
- *Cross-team technical influence:* Yariv Rachmani rates Roni at "Advanced level Multiplier" - elevating multiple teams (Toolchain, Jumpstarter, BoA) through TestConsole as a platform. This cross-organizational impact is characteristic of Level 5 scope
- *AI innovation leadership:* The MCP server conversion, AI log analysis pipeline, and Gemini integration are not incremental improvements - they represent architectural decisions that change how the team and AI agents interact with the test infrastructure. This is Level 5 strategic technical thinking
- *Platform ownership with architectural vision:* The Flask-to-FastAPI migration was a deliberate architectural choice that enabled MCP tool auto-export. Chaining architectural decisions toward a larger goal (AI-accessible test infrastructure) is Level 5 behavior
- *Stakeholder-driven feature delivery:* Independently gathered requirements from Akhil Kohli (CPU support), Martin Perina (bootc-testing), and coordinated implementation across teams without requiring management direction

**Growth areas for QE Level 5:**
- *Visibility and broader communication:* Both Meital Arki and the Slack data suggest Roni's impact exceeds his visibility. Meital specifically recommends sharing demos and speaking up in broader discussions. Level 5 requires the work to be seen and understood beyond the immediate team
- *Formal mentoring and knowledge transfer:* Yariv notes willingness to mentor, but evidence of structured mentoring (onboarding plans, pairing sessions, documentation for contributors) is limited. Level 5 expects systematically growing others' capabilities
- *Testing strategy at the program level:* Roni excels at Test Console platform development, but Level 5 expects defining testing strategy across the program - owning test coverage models, release readiness criteria, and quality metrics that go beyond CTC pass rates
- *External community engagement:* Zero GitLab.com or GitHub contributions this quarter. Level 5 in an open-source-oriented organization typically includes upstream contributions, conference talks, or community leadership beyond the internal team

**Recommended development path:**
1. **Discuss QE-to-SE career track transition** - if interested, note in Workday Talent Action for Tashana to coordinate support
2. **Increase visibility across broader RHIVOS** - consistent peer feedback theme. Demo the MCP server and AI analysis improvements to a broader audience
3. **Write a Test Console strategy document** - position TC as an enterprise platform with a 12-month roadmap: MCP server evolution, LLM capabilities, security hardening, performance targets, integration points. Present to leadership
4. **Present externally** - the MCP server conversion and the AI-powered test analysis story are compelling conference talk material for DevConf or testing conferences
5. **Expand stakeholder engagement** - engage more with product management and customers on quality metrics
6. **Formalize mentoring** - structure regular mentoring sessions for cross-team contributors to Test Console

---

## Summary

### Dimension-based view

| Member | Level | Scope | Complexity | Impact | Strongest Dimension | JD Strongest | JD Weakest |
|--------|-------|-------|------------|--------|---------------------|-------------|------------|
| Bella | SE L3 | 3, trending 4 | 3, trending 4 | 3-4 | Impact (CTC + Konflux) | Technical Acumen, Quality Mgmt, Business Impact | Communication, Influence, Knowledge Sharing |
| Eitan | SE L3 | 3, with L4 signals | 3, trending 4 | 3, with L4 data points | Scope (runner consolidation, AI tooling) | Continuous Learning | Communication, Knowledge Sharing, Leadership |
| Hubert | SE L3 | 3, trending 4 | 3-4 boundary | 3, trending 4 | Complexity (gating + cross-team) | Technical Acumen, System Design, Leadership, Business Impact | AI Tools (gap) |
| Kanitha | SE L3 | 3-4 boundary, strong | 3, trending 4 | 3-4 boundary, strong | Scope (25 channels, TPO, 4 Jira projects) | Technical Acumen, Communication, Collaboration, Business Impact | Knowledge Sharing |
| Muhamad | SE L3 | 3, with L4 signals | 3 | 3, trending 4 | Scope (e2e platform architecture) | Quality Management | Communication, Business Impact, Influence, Knowledge Sharing |
| Juanje | SE L4 | Stretching toward 5 | Stretching toward 5 | 4, trending 5 | Scope (cross-functional vision) | Technical Acumen, System Design, Continuous Learning, Business Impact | Communication (external), Leadership (mentoring) |
| Benny | SE L4 | 4 | 4, trending 5 | 4 | Complexity (connective hub, community expert) | Technical Acumen, System Design, Communication, Collaboration, Business Impact | AI Tools (gap) |
| Roderick | SE L4 | Too early | Too early | Too early | N/A (onboarding) | N/A (insufficient evidence) | N/A (insufficient evidence) |
| Matt | SRE L4 | 4 (building) | 3-4 | 3 | Scope (improvement initiative) | Linux Systems Mgmt, IaC, Incident Mgmt, Security | Enterprise Monitoring, Cloud Architecture |
| Roni | QE L4 | 4-5 | 4, trending 5 | 4, trending 5 | Impact (TC platform, cross-team multiplier) | Problem Solving, System Debugging, Automation Frameworks, AI Tools | External visibility, formal mentoring |

### Common themes

- **Knowledge sharing (articles, design docs)** - Who: Bella, Eitan, Benny, Muhamad, Kanitha. Dimension: Scope + Complexity (expert recognition). Action: Write at least one internal article or design doc per quarter.
- **AI tools exploration** - Who: Bella, Hubert, Muhamad, Benny. Dimension: Scope (proposing new methods). Action: Try AI tools for daily work; share findings in team channel. (Note: Eitan has already progressed past exploration - built reusable claude-code hooks and skills. Kanitha has run a spike. Roni and Juanje are leading in this area.)
- **Mentoring relationships** - Who: Bella, Eitan, Muhamad, Benny. Dimension: Scope (guidance to others). Action: Establish at least one formal mentoring pair.
- **External presentations** - Who: Juanje, Benny, Roni. Dimension: Complexity (industry recognition). Action: Submit conference talks; internal demos are a stepping stone.
- **Business impact articulation** - Who: All. Dimension: Impact (strategy contribution). Action: Frame technical work in terms of business value when presenting to leadership.
- **Strategic thinking (roadmaps)** - Who: Benny, Kanitha, Roni. Dimension: Impact (medium-to-long-term direction). Action: Write one forward-looking strategy/architecture document per half.
- **Visibility and communication** - Who: Muhamad, Bella, Roni (peer feedback). Dimension: Complexity (broader relationships). Action: Increase Slack engagement, present at sprint demos and team meetings, share work proactively.
- **Cross-team coordination** - Who: Bella, Eitan, Muhamad. Dimension: Scope (functional-level reach). Action: Lead at least one initiative requiring coordination with another team.
