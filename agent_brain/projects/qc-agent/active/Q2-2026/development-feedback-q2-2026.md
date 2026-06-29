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

**Dimension assessment (Professional Track):**

- Scope [Level 3]: Works independently with minimal instruction. Delivers on enhanced processes (CTC reporting, OIDC hardening). Provides guidance within PitCrew. Occasional cross-subsystem reach (OIDC to jumpstarter) nudges toward Level 4.
- Complexity [Level 3]: Good judgment on moderately complex issues (CTC pipeline failures, certificate handling). Recognized as experienced within PitCrew. Relationships mostly within discipline. Not yet at "recognized expert leading cooperative efforts among teams" (Level 4).
- Impact [Level 3, trending 4]: CTC reporting directly impacts release certification - this touches program objectives (Level 4 territory). But scope of operational direction is still primarily within PitCrew.

**Current level fit:** Solid. Meeting Level 3 expectations across all responsibility areas. Independently designs and develops solutions (CTC reporting, OIDC patterns), owns quality of her code, provides guidance to teammates, and contributes to upstream communities.

**Already demonstrating at IC Level 4:**
- *Technical Impact (cross-component):* Extended OIDC certificate pattern from builder to jumpstarter - this crosses subsystem boundaries, a Level 4 trait
- *Quality (multi-component):* CTC reporting work touches pipeline integration, JUnit generation, and report aggregation across multiple components
- *Collaboration (cross-functional):* Opened Ford demo coordination thread bridging PitCrew with external stakeholders

**Growth areas for IC Level 4:**
- *Technical strategy across teams:* Most work stays within PitCrew scope. Level 4 expects "leading design of features that cross multiple subsystems or components" as a pattern, not just occasional reach
- *Mentoring:* Level 4 expects "across teams, coaches and mentors senior engineers." Currently collaborates well within PitCrew but no evidence of coaching others outside the team
- *Business impact visibility:* Level 4 expects "owns and delivers technical initiatives with visible business impact." CTC work has impact but she hasn't articulated or positioned it as a business-facing initiative
- *AI tools:* Level 4 expects "evaluates and introduces new AI-driven methodologies." No AI tooling evidence in Q2
- *Knowledge sharing:* Level 4 expects "blog posts, design documents, presents at conferences." No writing or presentation evidence this quarter
- *SDLC leadership:* Level 4 expects "leads the definition and implementation of the SDLC for complex multi-component systems." No evidence of defining or refining team processes

**Recommended development path:**
1. **Expand technical scope** - take on a feature that explicitly requires coordination across PitCrew and another team (ATC, QE, or upstream jumpstarter). The OIDC pattern shows she can do this - do it as a primary responsibility, not a side effect
2. **Start mentoring** - pick one junior/mid-level engineer (Muhamad could be a natural fit on the same team) and establish a regular technical mentorship
3. **Write one internal article or present at a team meeting** on a topic she owns (CTC reporting patterns, OIDC certificate architecture)
4. **Explore AI tooling** - try using AI agents or code-generation tools for testing or debugging work and share findings with the team
5. **Own a process improvement** - propose a specific SDLC improvement for PitCrew's CTC workflow and drive its adoption

---

### Eitan Raviv - Senior Software Engineer, ATC

**Dimension assessment (Professional Track):**

- Scope [Level 3]: Works independently on infrastructure and security tasks. Delivers on existing processes (AWS provisioning, CloudFront, security patching). Monitoring criticality tiers initiative hints at proposing new methods (Level 4), but hasn't scaled to functional-level impact yet.
- Complexity [Level 3, trending 4]: Navigated 5+ external organizational channels (PSCA, IT Cloud, GRC, BOA) - this breadth of relationship exceeds Level 3's "within discipline." Resolves cross-team procedural complexity. Not yet recognized as expert leading cooperative efforts.
- Impact [Level 3]: Infrastructure work contributes to team goals through operational stability. Decisions impact immediate team's ability to release. Not yet at "operational direction for functional goals" (Level 4).

**Current level fit:** Meeting expectations. Strong in infrastructure ownership, security compliance, and cross-organizational navigation. Independently manages AWS, CloudFront, and monitoring infrastructure.

**Already demonstrating at IC Level 4:**
- *Cross-team collaboration:* Navigated 5+ external channels (PSCA, IT Cloud, GRC, BOA Automotive) - this breadth of organizational reach exceeds Level 3
- *Monitoring initiative:* Criticality tiers in monitoring SLA specification is a system-design initiative that spans the team - Level 4 behavior
- *Communication:* Multi-channel incident communication pattern (advance notice, status, all-clear) demonstrates leadership communication

**Growth areas for IC Level 4:**
- *Technical scope:* Most contributions are infrastructure operations rather than "features that cross multiple subsystems." Level 4 expects leading design of cross-component features, not just maintaining infrastructure
- *Mentoring:* No evidence of coaching or mentoring others. Level 4 expects mentoring senior engineers across teams
- *Business impact articulation:* Level 4 expects "owns and delivers technical initiatives with visible business impact." Infrastructure work is critical but not positioned as business initiatives
- *Community engagement:* Level 4 expects "key representative and leader within the community." Limited upstream or community activity visible this quarter
- *AI tools:* Level 4 expects "evaluates and introduces new AI-driven methodologies." No AI tooling evidence
- *Knowledge sharing:* No design documents, blog posts, or presentations evident

**Recommended development path:**
1. **Lead a cross-component design initiative** - the monitoring criticality tiers is a great foundation. Expand it into a formal monitoring/observability strategy for ATC with documented design decisions and present it to stakeholders
2. **Mentor newer team members** on infrastructure and AWS patterns. Matt Goldman, who is new and touching similar infrastructure, would benefit from Eitan's deep operational knowledge
3. **Document infrastructure decisions** - write internal design documents for key infrastructure choices (CloudFront architecture, AWS provisioning patterns). This builds the knowledge-sharing and communication skills needed at Level 4
4. **Engage with SRE or infrastructure communities** at Red Hat - contribute patterns or tools to internal SRE forums
5. **Explore AI tools** for infrastructure management, monitoring, or incident response automation

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

- Scope [Level 3-4 boundary]: Works independently on complex distribution workflows. Broadest channel reach on team (25 channels). Cross-team coordination spanning 4 Jira projects (VROOM, RHELDST, RHELWF, PSSECAUT) - this exceeds Level 3's "within discipline" scope. The distribution/release work is functional-level, not just team-level.
- Complexity [Level 3, trending 4]: Resolves moderately complex issues (errata, CDN propagation failures, product listing). Cross-team relationships are productive and extend well beyond own team. Not yet at "recognized expert leading cooperative efforts" formally, but acts as the de facto distribution expert.
- Impact [Level 3-4 boundary]: Distribution work contributes directly to release readiness - customer-facing impact. Product listing and CDN decisions affect whether customers can download RHIVOS. This touches "customer, operational, or program objectives" (Level 4).

**Current level fit:** Strong. Broadest Slack reach on the team (25 channels). Distribution and release readiness specialist. Strong cross-organizational coordination.

**Already demonstrating at IC Level 4:**
- *Cross-component scope:* Distribution work inherently spans errata, CDN, product listing, compose, and advisory systems - multiple subsystems, Level 4 scope
- *Cross-team coordination:* Drove cross-team fix when product IDs failed to propagate, spanning VROOM, RHELDST, RHELWF, PSSECAUT. This is Level 4 collaboration
- *Communication with stakeholders:* Proactively clarified RC3 trigger conditions, surfaced stale product listing issues - leadership-level communication
- *Process understanding:* Deep understanding of release engineering processes and where they break

**Growth areas for IC Level 4:**
- *Technical design leadership:* Level 4 expects "leads the design and development of software solutions." Kanitha excels at process execution and coordination but needs to lead a technical design initiative
- *Mentoring:* Level 4 expects "across teams, coaches and mentors senior engineers." No mentoring evidence
- *AI tools:* The "Agentic AI for advisory workflow" spike is promising but needs follow-through. Level 4 expects "evaluates and introduces new AI-driven methodologies"
- *Knowledge sharing:* Level 4 expects "blog posts, design documents, presents at conferences." No formal writing or presentations
- *SDLC ownership:* Level 4 expects "leads the definition and implementation of the SDLC for complex multi-component systems." She follows release processes expertly but hasn't led their definition

**Recommended development path:**
1. **Lead a design initiative** - the QC LP distribution workflow spike and the AI advisory workflow spike are both natural candidates. Pick one and drive it from spike to design document to implementation
2. **Document the release pipeline** - Kanitha has the deepest knowledge of RHIVOS distribution. A formal design document of the release workflow (errata, CDN, product listing, gating) would be high-value and demonstrate Level 4 knowledge sharing
3. **Follow through on AI for advisories** - the spike shows initiative. Develop it into a concrete proposal, evaluate tools, and present findings to the team
4. **Mentor someone** on release engineering - her unique expertise makes her the natural mentor for anyone touching distribution
5. **Propose process improvements** - move from executing release processes to improving them. Identify a release bottleneck and propose a systematic fix

---

### Muhamad Abo Ras - Senior Software Engineer, PitCrew

**Dimension assessment (Professional Track):**

- Scope [Level 3]: Works independently on testing infrastructure. Delivers on enhanced processes (e2e rebuild, PR-triggered test tiers). Scope stays within builder testing domain. No evidence of coordinating others or mentoring. Needs to expand reach beyond own area.
- Complexity [Level 3]: Good judgment on moderately complex issues (OIDC e2e, Kind-to-CRC migration). Productive relationships within own team. 38 Slack messages across 7 channels is the lowest visibility - relationships largely "within own team" (Level 2-3 boundary on this sub-dimension).
- Impact [Level 3]: Contributes to team goals through completion of testing tasks. Decisions impact team's testing quality. Not yet at "operational direction" or "customer/program objectives" (Level 4).

**Current level fit:** Meeting expectations. Solid engineering work on testing infrastructure. Independently designs and implements testing solutions.

**Already demonstrating at IC Level 4:**
- *Quality ownership:* E2E testing infrastructure rebuild, PR-triggered test tiers, OIDC e2e tests - demonstrates quality system thinking beyond individual features
- *Technical design:* Restructuring e2e/lanes workflow to eliminate duplication shows design judgment

**Growth areas for IC Level 4:**
- *Cross-component scope:* Level 4 expects "features that cross multiple subsystems or components." Most work is within the builder testing domain. Needs broader technical reach
- *Visibility and communication:* 38 Slack messages across 7 channels is the lowest on either team. Level 4 expects "effectively communicates with leadership and stakeholders." Need significantly more visibility
- *Mentoring:* Level 4 expects "across teams, coaches and mentors senior engineers." No mentoring evidence. Room to grow in "initiating broader design discussions" (noted in QC)
- *Community engagement:* Level 4 expects "key representative and leader within the community." Very limited Slack presence outside immediate team
- *AI tools:* Level 4 expects "evaluates and introduces new AI-driven methodologies." No AI tooling evidence
- *Knowledge sharing:* No blog posts, design documents, or presentations
- *Business impact:* Level 4 expects "technical initiatives with visible business impact." Testing work is important but not positioned as business-facing

**Recommended development path:**
1. **Increase visibility** - this is the highest-priority growth area. Post more proactively in team channels: share design decisions, debugging findings, status updates. Move from 7 to 15+ channels
2. **Expand scope beyond builder testing** - look for testing needs across PitCrew. The ArgoCD/C2 disaster recovery work is a good start - position it as a cross-cutting initiative
3. **Document testing architecture** - write a design document for the e2e testing framework. This serves triple duty: knowledge sharing, design thinking, and a promotable artifact
4. **Start mentoring** - help onboard someone on PitCrew's testing infrastructure or share testing patterns with ATC
5. **Engage in broader channels** - join #forum-jumpstarter, #forum-qe-automotive, and contribute to discussions. Level 4 expects community engagement
6. **Explore AI tools** for test generation, test result analysis, or CI optimization

---

## Principal Software Engineers (IC Level 4 - next: Senior Principal SE, IC Level 5)

### Juanje Ojeda - Principal Software Engineer, ATC

**Dimension assessment (Professional Track):**

- Scope [Level 4-5]: Sets and achieves objectives tied to functional targets (Level 4 - met). Agent Forge and the pipelines-debugger propose new techniques with cross-functional impact - others across teams adopt the patterns. This is Level 5 "drives vision and innovation with cross-functional impact." Mentors Matt Goldman (Level 4), and cross-team adoption of agent patterns is effectively mentoring colleagues in own discipline (Level 5). Published articles and AAA Sprint 5 demo show emerging expert-resource behavior.
- Complexity [Level 4-5]: Independent judgment on complex, non-routine issues (6 Blockers resolved, creative agent solutions). Recognized as expert within team and increasingly across department. Leads cooperative efforts among 5+ teams for execopen. Cross-team relationships are productive and include FoA, QE, AIB upstream. Approaching "formal networks across Red Hat to influence priorities" (Level 5) through forum engagement.
- Impact [Level 4, trending 5]: Contributes to functional goals through operational direction (release pipeline, agent infrastructure). Decisions impact customer and program objectives (RC1-RC3, CTC). Agent Forge is starting to impact medium-term results. Not yet "consistently serves as project lead and SME for highly complex issues" at the organizational level (Level 5), but the trajectory is clear.

**Current level fit:** Exceeds expectations. Comfortably operating at Level 4 with multiple areas of Level 5 behavior already evident. 28 tickets (6 Blockers), 39 MRs, 711 Slack messages - output and influence significantly exceed Level 4 norms.

**Already demonstrating at IC Level 5:**
- *Technical strategy across teams:* Agent Forge is a reusable framework adopted across teams. Execopen pipeline integration spanned 5 repositories with FoA coordination. This is Level 5 "drives the technical strategy and design of software solutions across multiple subsystems, influencing the overall architecture"
- *AI leadership:* Pipelines-debugger, CTC agent, Agent Forge, Pi extensions for CI - this is Level 5 "drives the strategy and best practices for integrating advanced AI ecosystems." He isn't just using AI tools; he's building the strategy and infrastructure
- *Knowledge sharing:* Published articles on Red Hat Source and LinkedIn, presented at AAA Sprint 5 and Rollup Demo. Level 5 expects "frequently presents at technical conferences." Internal demos aren't conferences, but the trajectory is clear
- *Mentoring:* Matt Goldman onboarding with cheatsheets, wiki generation, MR reviews. Cross-team adoption of agent patterns (Ian, Kanitha building their own). This is Level 5 "coaches and mentors principal engineers and role models mentorship for the organization"
- *Community building:* Shared articles in #forum-ambient-code-platform, #wg-team-auto-toolchain-ai. Engaged across organizational boundaries. Building a community of practice around AI agents
- *Innovation:* Level 5 expects "drives innovation by leading significant product-area initiatives with a community-first mindset." Agent Forge and the AAA agent practice is exactly this

**Growth areas for IC Level 5:**
- *Organizational-level strategy:* Level 5 expects "drives the technical strategy... influencing the overall architecture" at an organizational level (not just team/product). Juanje's influence is growing but still primarily within the Automotive vertical
- *Conference presentations:* Level 5 expects "frequently presents at technical conferences, often to larger audiences." Internal demos and team meetings are strong but external conference presentations would strengthen the case
- *Cross-org mentoring:* Level 5 expects "across organizations, coaches and mentors principal engineers." His mentoring is currently within ATC/Automotive. Expanding to mentor or consult across other engineering organizations would strengthen the profile
- *SDLC evolution:* Level 5 expects "drives the evolution of the SDLC within the organization, introducing new methodologies." The agent-driven pipeline diagnosis is changing how the team works, but hasn't been positioned as an SDLC methodology change
- *Business impact articulation:* Level 5 expects "owns and drives technical initiatives across the organization recognizing which pieces flow together to deliver value to the end user." Juanje delivers enormous value but could improve at articulating business impact to leadership audiences
- *Industry engagement:* Level 5 expects "participates across multiple communities, fosters and monitors community health, engages in industry and internal working groups." Some gaps in formal industry engagement

**Recommended development path:**
1. **Present externally** - submit a talk to DevConf, Red Hat Summit, or an open source conference on AI agents for CI/CD pipeline diagnosis. The pipelines-debugger story is compelling and original
2. **Position Agent Forge as organizational strategy** - write a proposal positioning the agent practice as an engineering methodology for the broader organization, not just Automotive. Frame it in business terms: incident resolution time, engineering velocity, knowledge capture
3. **Expand mentoring across organizations** - offer to consult with teams outside Automotive who are exploring AI agents. The #forum-ambient-code-platform engagement is a start; deepen it
4. **Articulate SDLC impact** - document how the agent-driven approach changes the SDLC (pipeline diagnosis, CTC triage, code review). Position it as a methodology innovation, not just tooling
5. **Develop business acumen** - partner with product or business leadership to connect technical innovations to revenue/customer impact. Level 5 expects this connection

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

- Scope [Level 4-5]: Works independently to set and achieve objectives (Test Console platform, CTC pipeline, AI analysis). Proposes new techniques (AI-powered test analysis, Gemini transitions, packages.redhat.com PoC) with impact within the function. Coordinates CTC activities for RC1-RC3 as functional team lead. 199 mentions by others - acts as expert resource. Approaching Level 5 "drives vision and innovation with cross-functional impact" through Test Console's central role.
- Complexity [Level 4, trending 5]: Independent judgment on complex, non-routine issues (3 Gemini model transitions, fallback mechanisms, long-standing Blocker-level security fix). Recognized as expert within team - primary Test Console owner. Productive relationships within function (QE automotive, testing-farm, PitCrew). Leading cooperative efforts across QE teams. Approaching "subject matter expert advising on strategy" (Level 5).
- Impact [Level 4, trending 5]: Contributes to functional goals through operational direction of testing infrastructure. Decisions impact program objectives (CTC certification timeline, release readiness). Serves as de facto project lead for Test Console and CTC pipeline. Approaching Level 5 "directly impacts function's medium-to-long-term results" - Test Console IS the testing infrastructure strategy.

**Current level fit (QE Level 4):** Exceeds expectations. Highest individual output (32 tickets, 43 MRs). Owns the Test Console platform end-to-end. Leads test automation framework design, coordinates team activities for CTC delivery, and applies creative problem-solving (AI-powered test analysis, Gemini model transitions).

**Current QE Level 4 responsibilities and Roni's alignment:**
- *Test automation frameworks:* Test Console IS the automation framework. Roni designs, builds, and maintains it. Fully meets "lead the design and development of complex test automation frameworks"
- *Team coordination:* Configured TC for RC1/RC2/RC3, prepared reduced test plans, scheduled weekend CTC runs. Meets "coordinate the activities of a team of engineers to ensure successful test delivery"
- *Creative problem-solving:* AI-powered test analysis with 3 Gemini model transitions, fallback mechanisms. Exceeds "apply creative problem-solving to resolve complex bugs"
- *Mentoring:* Introduced Test Console MCP server to colleagues with examples. Some mentoring but could be more structured
- *CI/CD:* Designs and manages Test Console CI/CD pipeline. Meets Level 4

**Already demonstrating at QE Level 5:**
- *Platform ownership:* Test Console is the central testing platform for RHIVOS. Owning it is effectively "setting mid-term strategic direction of quality assurance activities"
- *AI innovation:* Navigated 3 Gemini model transitions and built intelligent fallback mechanisms. This approaches Level 5 "leverage AI technologies to streamline workflows"
- *Cross-team enablement:* 199 mentions by others - confirms he's a central enabler. Level 5 "subject matter expert" behavior
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
5. **Formalize mentoring** - structure mentoring of QE practices for team members. Help Bella with her CTC reporting work as a natural extension
6. **Develop business acumen** - understand how quality metrics connect to product release decisions, customer satisfaction, and revenue impact

---

## Summary: Dimension-based view

### Where the team sits on Scope / Complexity / Impact

- Bella [Level 3] - Scope: 3 / Complexity: 3 / Impact: 3, trending 4. Strongest: Impact (CTC affects release certification). Biggest gap: Scope - needs cross-team coordination as primary responsibility.
- Eitan [Level 3] - Scope: 3 / Complexity: 3, trending 4 / Impact: 3. Strongest: Complexity (navigates 5+ external orgs). Biggest gap: Impact - infrastructure work not positioned as functional direction.
- Hubert [Level 3] - Scope: 3, trending 4 / Complexity: 3-4 boundary / Impact: 3, trending 4. Strongest: Complexity (gating expertise + cross-team relationships). Biggest gap: Impact - needs to own a strategic initiative with functional-level accountability.
- Kanitha [Level 3] - Scope: 3-4 boundary / Complexity: 3, trending 4 / Impact: 3-4 boundary. Strongest: Scope (25 channels, 4 Jira projects, broadest reach). Biggest gap: Complexity - needs formal recognition as expert and team lead role.
- Muhamad [Level 3] - Scope: 3 / Complexity: 3 / Impact: 3. Strongest: Scope (independent, well-structured testing work). Biggest gap: Complexity - low visibility, needs broader relationships.
- Juanje [Level 4] - Scope: 4-5 / Complexity: 4-5 / Impact: 4, trending 5. Strongest: Scope (cross-functional vision + innovation, approaching Level 5). Biggest gap: Impact - needs to consistently serve as organizational-level SME and project lead.
- Benny [Level 4] - Scope: 4 / Complexity: 4, trending 5 / Impact: 4. Strongest: Complexity (connective hub, community expert). Biggest gap: Impact - tactical breadth, needs strategic direction-setting.
- Roderick [Level 4] - Scope: Too early / Complexity: Too early / Impact: Too early. Strongest: N/A (onboarding). Biggest gap: Domain depth - establish Level 4 baseline first.
- Matt [Level 4] - Scope: 4 (building) / Complexity: 3-4 / Impact: 3. Strongest: Scope (initiative to propose improvements). Biggest gap: Complexity + Impact - domain expertise and delivery cadence still ramping.
- Roni [Level 4] - Scope: 4-5 / Complexity: 4, trending 5 / Impact: 4, trending 5. Strongest: Impact (Test Console decisions directly affect CTC/release). Biggest gap: Complexity - needs to be recognized as SME advising functional leaders.

### Common themes

- Knowledge sharing (articles, design docs) - Who: Bella, Eitan, Benny, Muhamad, Kanitha. Dimension: Scope + Complexity (expert recognition). Action: Write at least one internal article or design doc per quarter.
- AI tools exploration - Who: Bella, Eitan, Hubert, Kanitha, Muhamad. Dimension: Scope (proposing new methods). Action: Try AI tools for daily work; share findings in team channel.
- Mentoring relationships - Who: Bella, Eitan, Muhamad, Benny. Dimension: Scope (guidance to others). Action: Establish at least one formal mentoring pair.
- External presentations - Who: Juanje, Benny, Roni. Dimension: Complexity (industry recognition). Action: Submit conference talks; internal demos are a stepping stone.
- Business impact articulation - Who: All. Dimension: Impact (strategy contribution). Action: Frame technical work in terms of business value when presenting to leadership.
- Strategic thinking (roadmaps) - Who: Benny, Kanitha, Roni. Dimension: Impact (medium-to-long-term direction). Action: Write one forward-looking strategy/architecture document per half.
- Visibility and communication - Who: Muhamad. Dimension: Complexity (broader relationships). Action: Increase Slack engagement, share work proactively, join 8+ more channels.
- Cross-team coordination - Who: Bella, Eitan, Muhamad. Dimension: Scope (functional-level reach). Action: Lead at least one initiative requiring coordination with another team.
