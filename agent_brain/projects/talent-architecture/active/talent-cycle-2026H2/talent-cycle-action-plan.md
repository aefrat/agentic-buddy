---
last_accessed: 2026-07-12
access_count: 1
created: 2026-07-12
---

# Talent Cycle Action Plan - H2 2026

**Cycle:** July 2026 Talent Cycle
**Guidance source:** Tashana's email "Upcoming Talent Cycle Guidance" (July 8, 2026); Talent Management for People Managers (The Source, 6 tabs)
**Data sources:** Q2 2026 QC reports, development feedback briefs (June 29, 2026), Skill Progression Matrices
**Reference:** [Talent Management for Managers](../../reference/talent-management-for-managers.md) - full Workday process, rating scales, HiPo descriptors, calibration | [Talent Actions Guide](https://docs.google.com/presentation/d/1aZLXZbT5cmmbk_UWRmF6KfLC5BG3ZyBszs1xCGgd8Bc/) - rewards guidance, development actions by tier, HiPo high-touch requirements, movement eligibility matrix

## Framework changes applied

1. **Engineering Competencies retired** - All assessments below use the Skill Progression Matrices (Job Descriptions) and Radford dimensions (Scope, Complexity, Impact) only. Prior competency tables (Red Hat Multiplier, Strategic, etc.) are treated as supplementary context.
2. **High Potential Flag** - Top 15%, long-term potential, commitment to growth. Candidates identified below.
3. **QE-to-SE transition** - Applicable to Roni Eliezer (only QE on team).

## Workday rating framework (quick reference)

### Performance (What + How, each 0-3)

| Score | Rating | Combined |
|-------|--------|----------|
| 3+3=6 | High Impact Performer | Consistently surpassing all expectations |
| 4-5 | Successful Performer | Consistently meeting, sometimes surpassing |
| 2-3 | Evolving Performer | Meeting some but not all expectations |
| 0-1 | Low Performer | Significant gaps |

Distribution guidance: 10-20% High Impact, 60-80% Successful, 5-15% Evolving, 2-5% Low.

### HiPo descriptors (ALL four required)

| Descriptor | Key question |
|-----------|-------------|
| Aspiration | Clear desire to advance to leadership or more impactful roles? |
| Capability | Observable skills suggesting capacity for greater responsibilities? |
| Engagement | Highly committed to Red Hat's mission, going above and beyond? |
| Agility | Adapts quickly, learns from experience, leads through ambiguity? |

Eligibility: rated in last 2 cycles, typically High Impact, not on PIP.

### Movement readiness (within 6 months)

| Rating | When to use |
|--------|------------|
| Continue growing in current role | Default - in-role development |
| Ready now to be promoted (upcoming cycle) | High Impact, 12-18 months at level, business need, expanded scope |
| Ready for lateral move outside current role | Successful+, 12+ months, meets Internal Mobility Guidance |
| Ready for promotion outside current role | Ready but no business need within current team |
| Not well placed | Not thriving, role realignment needed |

---

## High Potential Flag recommendations

The flag is for **long-term potential**, not current high performance. Reserved for top 15%. Selecting someone is a commitment to provide exposure, wider scope, and more complex responsibilities.

**Recommended for High Potential Flag:**

### Juanje Ojeda - Principal Software Engineer, ATC

**Why:** Juanje demonstrates the clearest trajectory to the next level (IC-5) with multiple Level 5 behaviors already in evidence: AI innovation leadership that others adopt organically (Agent Forge), cross-team enablement through tooling, published articles, and strategic technical thinking. His long-term potential extends to Distinguished Engineer territory - he builds reusable methodology, not just solutions.

**Development actions (required with HiPo flag):**

Per Talent Actions Guide: must provide increased scope/complexity/impact within 12 months, refine 1-2 high-value skills, and select minimum 2 high-touch activities.

- Exposure to higher-level roles: Have Juanje present the agent practice as engineering methodology to P&GE leadership (beyond Automotive). This positions him for organizational-level influence
- Wider scope of influence: Establish a cross-org consulting relationship with 1-2 teams outside Automotive exploring AI agents
- More complex responsibilities: Assign Juanje as technical lead for a cross-BU initiative (e.g., agent-driven pipeline diagnosis as a reference architecture for RHEL or Ansible)

**High-touch activities (minimum 2 required):**
1. External/internal speaking engagement - Submit conference proposal (DevConf.cz / Summit) on agent methodology. Elevates personal brand, refines executive polish
2. Cross-functional project leadership - Lead cross-BU agent-driven pipeline diagnosis initiative. Tests leadership in ambiguity, demonstrates business impact

**Communication:** Inform Juanje he is identified as High Potential. Discuss the development plan and the commitment it represents.

### Roni Eliezer - Principal Software Quality Engineer, ATC

**Why:** Roni owns the Test Console platform end-to-end - a platform that IS the testing infrastructure strategy for RHIVOS. Highest individual output (32 tickets, 43 MRs), cross-team multiplier effect confirmed by BOA team feedback (Advanced-level Multiplier). His trajectory toward IC-5 is clear, with AI innovation in QE (3 Gemini model transitions) that few QEs in the org can match. Long-term potential to define how QE works across the organization, not just within Automotive.

**Development actions (required with HiPo flag):**

Per Talent Actions Guide: must provide increased scope/complexity/impact within 12 months, refine 1-2 high-value skills, and select minimum 2 high-touch activities.

- Exposure to higher-level roles: Have Roni present Test Console as an enterprise QE reference architecture to other product QE teams
- Wider scope of influence: Engage with QE leaders across P&GE to share AI-powered test analysis patterns
- More complex responsibilities: Assign ownership of a 12-month QE strategy document for RHIVOS (roadmap, AI maturity, coverage targets)

**High-touch activities (minimum 2 required):**
1. External/internal speaking engagement - Present AI-in-QE at a testing conference or DevConf. Elevates personal brand, expands professional network
2. Senior leader networking and exposure - Engage product management and QE leaders across P&GE on quality metrics and AI-powered test analysis. Builds reputation and realistic view of senior-level expectations

**Communication:** Inform Roni he is identified as High Potential. Discuss the development plan. Also discuss the QE-to-SE transition opportunity (see below).

---

## QE-to-SE transition conversation

**Applicable to: Roni Eliezer** (only QE on team)

Per Tashana's guidance, use this talent cycle to check QE interest in developing toward SE roles. Key points for the conversation:

- This is **completely optional** - focus on career growth, no impact on job security
- QE and SE job families **do not map 1:1** - transitioning to an equivalent SE role often represents a promotion in both expectations and compensation
- Roni's profile is interesting here: he already builds and maintains the Test Console platform (substantial software engineering work), writes AI integrations, manages CI/CD pipelines. His day-to-day work already overlaps significantly with SE responsibilities
- If interested, note it in the **Talent Action** section of Workday. Tashana can coordinate support and training resources
- **Reassure:** This initiative focuses on career growth and does not impact job security

**Q2 2026 evidence supporting the transition (updated with self-input and peer feedback):**

- **Self-reported top accomplishment:** Converting TC backend into an MCP server - migrated all code from Flask to FastAPI, then automatically exposed all APIs as MCP tools. This is pure software architecture and platform engineering
- **43 merged MRs in Q2:** Vast majority are feature development (API design, framework migration, performance optimization, AI pipeline engineering), not traditional QE (test planning, test strategy, test execution)
- **Key SE-aligned work:** New APIs for CPU support (AWS Graviton 3), job enable/disable, env-var updates; DPAC integration with Ozan and Juanje; JMESpath filtering; frontend SonarQube CI; UI performance optimization (lazy-loading runner_status/log); bootc-testing integration with Jumpstarter
- **Peer feedback alignment:** Rachel describes him co-leading "Test Console development work" (not test work). Meital highlights "AI knowledge," "practical solutions," and "ownership mindset." Yariv positions him as a cross-team multiplier through a platform he builds and maintains
- **SE Level 4 matrix fit:** Cross-subsystem/component features (TC spans backend, frontend, client, CI), proposes new techniques (MCP server, JMESpath, AI analysis redesign), leads cooperative efforts among teams (Ozan/DPAC, Benny+Bella/bootc, Testing Farm/CPU), recognized expert within team

**Recommendation:** Have this conversation in Roni's next 1:1. Frame it as: "Your Test Console work is already substantial software engineering. The org is offering QEs a supported path to SE if that interests you. No pressure - just want you to know the option exists."

---

## Per-member assessment and development plans

### Assessment framework (per Tashana's guidance)
- Primary: Skill Progression Matrix for their job family
- Secondary: Radford dimensions (Scope, Complexity, Impact)
- Engineering Competencies: NOT USED (retired for SE, QE, EM)

---

### ATC - Auto ToolChain

#### Juanje Ojeda - Principal SE (IC-4), targeting IC-5

**Workday ratings:**
- What: 3 (Surpasses expectations) - 28 tickets (6 Blockers), 39 MRs. Agent Forge, pipelines-debugger, execopen pipeline. Published articles.
- How: 3 (Surpasses expectations) - 711 Slack messages, transparent public-first communication, cross-team enablement, mentoring Matt Goldman
- Combined: **High Impact Performer (6)**

**High Potential assessment (4 descriptors):**
- Aspiration: YES - pursues increased scope (Agent Forge cross-team adoption), seeks visibility (published articles, demos), mentors others
- Capability: YES - strategic thinking (agent methodology), problem-solving (6 Blockers resolved), interpersonal (5+ cross-team relationships)
- Engagement: YES - goes above and beyond (built reusable tooling beyond requirements), volunteered energy on AI innovation outside core role
- Agility: YES - adapted quickly to AI tools, led through ambiguity (pipeline debugging with no playbook)
- **HiPo designation: YES**

**Movement readiness:** Continue growing in current role
- Promotion readiness (IC-4 to IC-5): not yet. 1-2 quarters. Must reach High Impact for 2 consecutive cycles.
- Gaps per SE Matrix IC-5: organizational-level strategy positioning, external conferences, cross-org networks, customer-impact articulation
- Strengths already at IC-5: AI innovation leadership, cross-team enablement, technical strategy, knowledge sharing

**Talent actions (next 6 months):**
- Rewards: Merit increase warranted (High Impact). Consider equity for role criticality + future capability
- Development (3 Es):
  - Experience: Lead a cross-BU initiative (agent-driven pipeline diagnosis as reference architecture)
  - Exposure: Present to P&GE leadership beyond Automotive; submit external conference proposal (DevConf.cz / Summit)
  - Education: N/A (self-directed learning already strong)
- Growth: Write strategic proposal positioning Agent Forge as engineering methodology. Establish 1-2 cross-org consulting relationships. Articulate customer-facing impact

**Promotion timeline:** Q4 2026 or Q1 2027. Movement readiness will shift to "Ready now to be promoted" when: (a) second consecutive High Impact rating, (b) business need documented, (c) expanded scope per IC-5 SE matrix demonstrated

---

#### Roni Eliezer - Principal QE (IC-4), targeting IC-5

**Workday ratings:**
- What: 3 (Surpasses expectations) - 32 tickets, 43 MRs. Owns Test Console. De facto CTC project lead across RC1-RC3. AI innovation (3 Gemini transitions).
- How: 3 (Surpasses expectations) - 497 Slack msgs, 199 mentions by others. Cross-team multiplier confirmed by BOA team (Advanced level). Mentoring through platform enablement.
- Combined: **High Impact Performer (6)**

**High Potential assessment (4 descriptors):**
- Aspiration: YES - pursues increased scope (Test Console as platform, not just a tool), seeks influence (cross-team enablement), mentors others into platform
- Capability: YES - strategic thinking (AI-powered test analysis), problem-solving (3 model transitions with fallback), interpersonal (BOA team feedback confirms cross-team anchor role)
- Engagement: YES - goes above and beyond (weekend CTC runs, packages.redhat.com PoC), emotional commitment to quality infrastructure
- Agility: YES - navigated 3 Gemini model transitions (external change), built fallback mechanisms, adapted testing approach for each release candidate
- **HiPo designation: YES**

**QE-to-SE transition:** Discuss in next 1:1 (see section above). Q2 evidence strongly supports: self-reported top accomplishment is MCP server conversion (pure SE); 43 MRs are overwhelmingly feature dev and platform architecture; peer feedback frames him as a developer, not a tester. If interested, note in Talent Action. This transition would formally align his job profile with the work he already does and open the SE progression path (through Senior Principal SE) for future growth.

**Movement readiness:** Continue growing in current role
- Promotion readiness (IC-4 to IC-5): not yet. 1-2 quarters.
- Gaps per QE Matrix IC-5: published mid-term QE strategy, stakeholder management beyond engineering, business acumen, external presentations
- Gaps per SE Matrix IC-5 (if QE-to-SE transition): organizational-level strategy positioning, external conferences, cross-org networks. Note: many SE IC-4 expectations are already met (cross-subsystem features, new techniques, cooperative efforts)
- Strengths already at IC-5: platform ownership, AI innovation, cross-team enablement

**Talent actions (next 6 months):**
- Rewards: Merit increase warranted (High Impact). Consider equity for platform criticality (Test Console = RHIVOS testing infrastructure)
- Development (3 Es):
  - Experience: Own 12-month QE strategy document. Formalize mentoring for cross-team Test Console contributors
  - Exposure: Present AI-in-QE externally (testing conference or DevConf). Engage product management on quality metrics
  - Education: QE-to-SE path if interested (Tashana can coordinate training resources). Evidence strongly supports transition - work profile already aligns with SE
- Growth: Write Test Console strategy doc. Increase visibility (demos, broader discussions - per Meital's feedback). Develop business acumen (connect quality to release/revenue impact). Stakeholder management beyond engineering

**Promotion timeline:** Q4 2026 or Q1 2027

---

#### Kanitha Chim - Senior SE (IC-3), targeting IC-4

**Workday ratings:**
- What: 3 (Surpasses expectations) - Distribution specialist, broadest reach (25 channels, 4 Jira projects). Serves as the ATC team's Technical/Team Product Owner (TPO) - connecting RHIVOS program priorities from the Area PO (Petr Sabata/contyk) to the team, setting 6-month priorities, leading focus area brainstorms, and representing ATC on program calls. QMS audit SME (ISO 26262 Part 8) outside core role. 18 tickets across 4 Jira projects including 5 Major-priority. TPO + QMS combined demonstrate work well beyond IC-3 SE expectations.
- How: 3 (Surpasses expectations) - De facto cross-team coordinator, proactive stakeholder communication, surfaced stale product listing issues independently. TPO coordination work bridges program and team priorities - Avi defers prioritization decisions to Kanitha and Petr ("I defer the decision to kchim and contyk - the POs"). QMS cross-team SME work further strengthens this score. Reward Zone recognition from ET team (Lu Zhang).
- Combined: **High Impact Performer (6)**

**Additional responsibility: ATC Technical Product Owner (TPO)**
Kanitha serves as the ATC team's TPO alongside Petr Sabata (contyk) as Area PO from PDR (Product Feature and Release). Key responsibilities:
- Bridges RHIVOS program priorities to ATC team execution - manages backlog, initiative organization, and sprint planning inputs
- Recognized as the "source of truth" for the team (per Avi's 5-year anniversary recognition, #team-toolchain-automotive)
- Co-decision maker with Petr on work prioritization: "I'm not the one prioritizing work but kchim and contyk" (Avi, multiple occasions)
- Completes ATC planning updates for PDR extended staff meetings, reviewed by Petr
- Balances "deep technical weeds with high-level strategy that keeps leadership happy" (Avi's characterization)
- Attends PO Feature Area Portfolio/Roadmap planning meetings representing ATC perspective

Supporting feedback:
- Avi (manager): "As our ToolChain TPO, Kanitha has become the 'source of truth' for everything in the team...she's played such a massive role in getting RHIVOS 1.X and 2.0 Core TP out the door, all while balancing the deep technical weeds with the high-level strategy...bridging program and team priorities" (#team-toolchain-automotive, 5-year anniversary)
- Sabine Vogel (peer manager): "I appreciate what and how you wrote about Kanitha's 5 year anniversary. I read great respect and value for her and her work"
- Avi consistently defers priority decisions to "kchim and contyk" across multiple channels (leads-toolchain-auto, mpdm groups, team-toolchain-automotive)
- Hubert Stefanski and Eitan Raviv (peers): "Maybe have a tech PO (TPO?) as Kanitha to push back" - team members independently recognized and named the TPO role (ATC Team meeting, Mar 10, 2026)
- ATC Team meeting notes show Kanitha setting 6-month team priorities ([kchim] "Priority for the next 6 months or more" - CAIB, Gating/Konflux, Pulp, Infra, Pipeline/release, Distribution, Test Console), 2-week sprint priorities, and leading focus area brainstorms ("[kchim] focus area priority - brainstorm from Toolchain side first as the program priority discussion will be set later on")
- Avi asks Paul to "backup Kanitha on the Program call" when she is on PTO - confirming she is the default ATC representative on program-level calls

This TPO role is a distinct leadership responsibility on top of her core SE distribution work and directly demonstrates IC-4 expectations: cross-team coordination as primary responsibility, stakeholder management, and functional-level impact on team direction.

**Cross-team contribution: QMS ISO 26262 audit SME**
Kanitha served as Subject Matter Expert for the RHIVOS QMS ISO 26262 Part 8 certification audit (TUV SUD), covering:
- **Configuration Management** - presented slides (slides 24-25), prepared audit materials, responded to auditor (Daniel/dgj) clarification requests on version analysis and CMDB configuration
- **Confidence in Tools** - co-owned tooling certification evidence
- Attended TUV SUD audit remotely (Jun 23-24, 2026), skipping regular ATC sync and toolchain team meetings to prepare
- Active in #forum-qms channel; currently addressing 4 open items from TUV SUD protocol review (Configuration Management: whether version analysis can be handled centrally vs CMDB relying on application URLs)
- Cross-team coordination with: Shir Fishbain (QMS lead), Rachel Sibley, contyk, rpaccapeli, priyverm, Sharon Metzger, Jaime Flynn

This work is beyond her core distribution role and demonstrates IC-4 signals: cross-org coordination on a critical program initiative, technical ownership of audit-facing materials, and proactive commitment (skipping team meetings to prioritize QMS preparation).

**High Potential assessment (4 descriptors):**
- Aspiration: YES - career goal is senior technical leadership; actively seeking to shape architecture and influence team direction; wants to progress from "execution partner" to "shaping partner" with the PO
- Capability: YES - TPO role demonstrates strategic thinking and cross-team coordination as primary function; QMS audit ownership shows capacity for cross-org responsibility; problem-solving across 4 Jira projects
- Engagement: YES - voluntarily took on QMS audit SME outside core role (skipped team meetings to prepare); TPO is extra leadership responsibility beyond SE job description; Reward Zone recognition from ET team validates going above and beyond
- Agility: YES - organically grew into TPO role; adapted to QMS audit domain with no prior certification experience; AI spike exploration (VROOM-40319); navigates ambiguity across distribution, gating, and program coordination
- **HiPo designation: YES**

**Development actions (required with HiPo flag):**

Per Talent Actions Guide: must provide increased scope/complexity/impact within 12 months, refine 1-2 high-value skills, and select minimum 2 high-touch activities.

- Exposure to higher-level roles: Have Kanitha present the RHIVOS release distribution architecture to other product teams. Position her TPO work as a model for how IC engineers can bridge program and team priorities
- Wider scope of influence: Formalize her distribution expertise into reusable process documentation that serves teams beyond ATC
- More complex responsibilities: Own the end-to-end CDN/Errata design for 2.0.z as a formal design initiative (requirements to design doc to implementation)

**High-touch activities (minimum 2 required):**
1. Cross-functional project leadership - Lead 2.0.z release pipeline design as a cross-team initiative spanning ATC, ET, and program stakeholders. Tests leadership in ambiguity, demonstrates business impact
2. External/internal mentorship - Formalize distribution mentoring with incoming team member. Knowledge transfer, diverse perspectives, career guidance

**Communication:** Inform Kanitha she is identified as High Potential. Discuss the development plan and the commitment it represents. Connect HiPo activities to her stated career aspiration of senior technical leadership.

**Movement readiness:** Continue growing in current role
- Promotion readiness (IC-3 to IC-4): strong trajectory, approaching readiness. TPO and QMS evidence narrow the gap to primarily technical design artifacts
- Gaps: needs to lead a formal technical design initiative (design doc, architectural decisions), formalize mentoring, produce durable knowledge artifacts
- Strengths already at IC-4: cross-component scope, cross-team coordination as primary function (TPO), stakeholder management, QMS cross-org engagement, program-level representation

**Talent actions (next 6 months):**
- Rewards: Greater rewards warranted (High Impact). Consider equity for role criticality (TPO + distribution = two critical functions) and future capability (HiPo). May progress through salary range at accelerated rate per HiPo guidance
- Development (3 Es):
  - Experience: Own CDN/Errata design for 2.0.z release - lead from requirements to design doc to implementation. Continue QMS SME role through certification completion. Lead 2.0.z release pipeline as cross-team design initiative
  - Exposure: Formalize distribution mentoring with new team member. Present release distribution architecture to other product teams. Leverage QMS and TPO cross-team networks for broader org visibility
  - Education: N/A
- Growth: Write one internal design document on RHIVOS distribution pipeline (Level 4 Knowledge Sharing differentiator). Document QMS Configuration Management approach as reusable process reference. Position for IC-4 nomination next cycle

**Promotion timeline:** Q1 2027

---

#### Eitan Raviv - Senior SE (IC-3), targeting IC-4

**Workday ratings:**
- What: 3 (Surpasses expectations) - Highest MR count (28 merged). GitLab runner consolidation with measurable cost savings. AI tooling pioneer (claude-code hooks/skills). Container vulnerability remediation (VHCL-009 closed). Infrastructure and security specialist.
- How: 2 (Meets expectations) - Technical depth is strong but visibility is significantly low (76 Slack messages). Cross-org navigation skills present (Brew permissions, external teams) but not communicated broadly.
- Combined: **Successful Performer (5)**

**High Potential:** Not at this time. Strong technical depth but visibility gap needs to close first. Reassess in 6 months.

**Movement readiness:** Continue growing in current role
- Promotion readiness (IC-3 to IC-4): addressable gap. Technical contributions already at IC-4 quality but visibility and knowledge sharing must catch up.
- Gaps per SE Matrix IC-4: documented knowledge sharing, community leadership, broader communication
- Strengths already at IC-4: runner consolidation, AI tooling, cross-org navigation, infrastructure architecture

**Talent actions (next 6 months):**
- Rewards: Standard merit (Successful Performer). Note: What score alone would warrant higher consideration - visibility is the constraint.
- Development (3 Es):
  - Experience: Formalize AI tooling work - document claude-code hooks/skills, propose team adoption (IC-4: "evaluates and introduces new AI-driven methodologies")
  - Exposure: Increase Slack visibility - share work proactively in broader channels. Mentor Matt Goldman and/or Hubert's replacement on infrastructure patterns
  - Education: N/A
- Growth: Write design doc on runner consolidation (cost savings, architecture, lessons). Channel "go deep to enhance" into documented, shared impact

**Promotion timeline:** Q1 2027 if visibility and knowledge sharing gaps addressed

---

#### Hubert Stefanski - Senior SE (IC-3) -- TRANSITIONING OUT

**Note:** Hubert's last day is approaching (transition started July 1, day 12). Talent cycle actions are limited.

**Workday ratings:**
- What: 3 (Surpasses expectations) - 29 MRs (tied highest). Infrastructure and gating innovation. AutoSD CloudFront, CentOS CI maintenance. Strong delivery until transition.
- How: 2 (Meets expectations) - Strong cross-team relationships, but knowledge was concentrated (KT risk now materialized)
- Combined: **Successful Performer (5)**

**High Potential:** N/A (transitioning out)

**Movement readiness:** Not well placed
- Transitioning out of role. If transferring within Red Hat, coordinate with receiving manager on talent assessment handoff.

**Talent actions (next 6 months):**
- Rewards: N/A (departing)
- Development: N/A
- Growth: Focus on knowledge transfer completion. Ensure gating knowledge, AutoSD CloudFront migration plan, and fork maintenance are documented before departure

---

#### Matt Goldman - Principal SRE (IC-4), ramping

**Workday ratings:**
- What: 1 (Meets some expectations) - Building toward expectations (2.5 months in role, new hire). 7 MRs, investigation spikes show initiative. Not yet delivering at full IC-4 scope - expected for ramp phase.
- How: 2 (Meets expectations) - 148 Slack messages, 15 channels. Positive engagement, asking good questions, building relationships. Appropriate for onboarding.
- Combined: **Evolving Performer (3)**

Note: Evolving rating reflects ramp-up phase, not underperformance. New hires under 6 months are expected here. Communicate clearly that this is a ramp assessment, not a deficit.

**High Potential:** Too early to assess. Revisit at 6-month mark (October 2026).

**Movement readiness:** Continue growing in current role
- Establishing IC-4 baseline. No promotion or lateral considerations applicable.

**Talent actions (next 6 months):**
- Rewards: Standard new-hire compensation. No merit action this cycle.
- Development (3 Es):
  - Experience: Own custom-images or another major infrastructure component end-to-end. Lead one reliability improvement initiative
  - Exposure: Build cross-team relationships with Eitan, Juanje, Roni. Join container vulnerability remediation efforts with Eitan (VHCL-005/007)
  - Education: Domain ramp - RHIVOS architecture, CentOS CI, Gator pipelines
- Growth: Start documenting infrastructure patterns (jinja2 investigation, Review Apps). 6-month assessment milestone: October 2026

---

### PitCrew - RHAS

#### Benny Zlotnik - Principal SE (IC-4), targeting IC-5

**Workday ratings:**
- What: 3 (Surpasses expectations) - Highest ticket throughput (30 closed), broadest community connector (897 Slack messages, 17 channels). De facto jumpstarter community first responder.
- How: 2 (Meets expectations) - Strong community leadership and breadth, but all reactive. No articulated technical vision or strategic direction-setting. Community engagement is broad but not yet shaping direction.
- Combined: **Successful Performer (5)**

**High Potential:** Consider but not recommended at this time. Strong IC-5 signals on community leadership and breadth, but the strategic gap (no articulated technical vision, all reactive) needs to close before HiPo commitment is appropriate. Reassess at next cycle.

**Movement readiness:** Continue growing in current role
- Promotion readiness (IC-4 to IC-5): 2-3 quarters away
- Gaps per SE Matrix IC-5: technical strategy/vision document, architectural roadmap, external presentations, formal mentoring, AI leadership
- Strengths already at IC-5: community leadership, technical breadth, knowledge hub role

**Talent actions (next 6 months):**
- Rewards: Standard merit (Successful Performer). Consider equity for community role criticality (jumpstarter ecosystem anchor).
- Development (3 Es):
  - Experience: Write 6-month technical strategy/roadmap for jumpstarter evolution (single most important step). Shift from reactive to directive - identify top 3 architectural improvements and drive proactively
  - Exposure: Submit conference proposal (jumpstarter community, DevConf). Convert Slack expertise into one blog post or design document
  - Education: Explore AI tooling strategy for PitCrew workflows
- Growth: Position for IC-5 nomination by demonstrating strategic direction-setting, not just broader scope of same work

**Promotion timeline:** Q2 2027 if strategic direction and knowledge formalization materialize

---

#### Bella Khizgiyaev - Senior SE (IC-3), targeting IC-4

**Workday ratings:**
- What: 2 (Meets expectations) - Solid Level 3. CTC specialization (4 of 8 closed tickets CTC-related). OIDC cross-subsystem work. Konflux integration contributions. Consistent delivery at expected scope.
- How: 2 (Meets expectations) - Reliable team contributor. Cross-component OIDC work shows initiative. Not yet demonstrating cross-team coordination as a primary pattern.
- Combined: **Successful Performer (4)**

**High Potential:** No. Solid performer developing well but not in the top 15% trajectory.

**Movement readiness:** Continue growing in current role
- Promotion readiness (IC-3 to IC-4): 2-3 quarters away
- Gaps per SE Matrix IC-4: cross-team coordination as primary responsibility, mentoring, knowledge sharing artifacts, AI tool adoption, SDLC leadership
- Strengths trending IC-4: cross-component OIDC work, CTC impact on release certification

**Talent actions (next 6 months):**
- Rewards: Standard merit (Successful Performer)
- Development (3 Es):
  - Experience: Take on a feature requiring explicit cross-team coordination (PitCrew + ATC or upstream jumpstarter). Propose a specific SDLC improvement for PitCrew's CTC workflow
  - Exposure: Start mentoring one engineer (Muhamad is a natural fit). Write one internal article on CTC reporting patterns or OIDC certificate architecture
  - Education: Explore AI tooling for testing or debugging
- Growth: Build cross-team coordination pattern. Position for IC-4 nomination Q2 2027

**Promotion timeline:** Q2 2027

---

#### Muhamad Abo Ras - Senior SE (IC-3), developing

**Workday ratings:**
- What: 2 (Meets expectations) - Solid technical execution (5 Stories, all substantive E2E testing work). Delivers reliably on assigned scope.
- How: 1 (Meets some expectations) - Significantly below expectations on visibility (38 Slack messages, 7 channels - lowest on team). IC-3 expects proactive collaboration, "enhances existing processes," and "provides guidance" - these are not present.
- Combined: **Evolving Performer (3)**

Note: This is borderline. The visibility gap is significant for IC-3, but the technical delivery is solid and the gap may be cultural/comfort rather than capability. Per Tashana's guidance: don't wait to address concerns, and document feedback. **Direct conversation needed, not formal underperformance documentation yet.**

**High Potential:** No.

**Movement readiness:** Continue growing in current role
- Not meeting full IC-3 expectations on collaboration/visibility dimension
- Requires focused development plan with 90-day checkpoint

**Talent actions (next 6 months):**
- Rewards: Standard merit (lower end of Successful range due to How score). Frame positively - technical work merits recognition, How dimension is the growth area.
- Development (3 Es):
  - Experience: Expand scope beyond builder testing - look for testing needs across PitCrew. Document the e2e testing framework (design doc)
  - Exposure: **Increase visibility** (highest priority) - target 15+ channels, share decisions/findings/status proactively. Join broader channels (#forum-jumpstarter, #forum-qe-automotive). Start contributing to team discussions more actively
  - Education: N/A
- Growth: Close visibility gap. Reassess in 90 days.

**Manager action:** Have a direct conversation about visibility expectations. Frame positively ("your technical work is solid - to grow and be recognized at this level, you need to share it more broadly"). Document the conversation and agreed actions in Workday and via email per Tashana's underperformance documentation guidance

---

#### Roderick Kieley - Principal SE (IC-4), onboarding

**Workday ratings:**
- What: 1 (Meets some expectations) - Too early to fully assess (joined June 1, 41 days). First code contribution landed. Positive early signals in AI/agent community engagement. Not yet delivering at full IC-4 scope - expected for onboarding.
- How: 2 (Meets expectations) - Engaging appropriately, building relationships, contributing to discussions. 10.5 years at Red Hat provides strong cultural alignment.
- Combined: **Evolving Performer (3)**

Note: Evolving rating reflects onboarding phase, not underperformance. Internal transfers ramping into new domain are expected here. Communicate clearly that this is an onboarding assessment.

**High Potential:** Too early. Revisit at 6-month mark (December 2026). AI/agent expertise suggests strong long-term potential - the question is delivery in PitCrew domain.

**Movement readiness:** Continue growing in current role
- Establishing IC-4 baseline in new domain. No movement considerations applicable.

**Talent actions (next 6 months):**
- Rewards: No merit action this cycle (recent transfer).
- Development (3 Es):
  - Experience: Build PitCrew domain depth - 3-5 Jira tickets across different workstreams. Establish PITCREW-161 (AIB prototyping) as project lead role
  - Exposure: Pair with Benny for domain knowledge transfer. Leverage AI/agent expertise on PitCrew-relevant problems
  - Education: PitCrew domain ramp - jumpstarter ecosystem, RHAS architecture, team workflows
- Growth: Document onboarding observations. 6-month assessment milestone: December 2026

**30-day checkpoint:** Overdue (was due July 1). Complete this week

---

## Summary: Talent cycle Workday actions

| Member | What | How | Combined | HiPo | Movement readiness | Key actions |
|--------|------|-----|----------|------|--------------------|-------------|
| Juanje Ojeda | 3 | 3 | High Impact (6) | YES | Continue growing | HiPo dev actions, IC-5 promotion plan |
| Roni Eliezer | 3 | 3 | High Impact (6) | YES | Continue growing | HiPo dev actions, QE-to-SE check, IC-5 plan |
| Kanitha Chim | 3 | 3 | High Impact (6) | YES | Continue growing | HiPo dev actions, IC-4 promotion plan, TPO + QMS |
| Eitan Raviv | 3 | 2 | Successful (5) | No | Continue growing | IC-4 plan (visibility focus) |
| Hubert Stefanski | 3 | 2 | Successful (5) | N/A | Not well placed | Knowledge transfer, transition handoff |
| Matt Goldman | 1 | 2 | Evolving (3) | Too early | Continue growing | 6-month milestone (Oct 2026) |
| Benny Zlotnik | 3 | 2 | Successful (5) | Not yet | Continue growing | IC-5 plan (strategy focus) |
| Bella Khizgiyaev | 2 | 2 | Successful (4) | No | Continue growing | IC-4 development plan |
| Muhamad Abo Ras | 2 | 1 | Evolving (3) | No | Continue growing | Visibility plan, 90-day check |
| Roderick Kieley | 1 | 2 | Evolving (3) | Too early | Continue growing | 30-day checkpoint, 6-month milestone |

### Distribution check (team of 10)
- High Impact (6): 3 (30%) - above 10-20% guidance (small team variance; all three have strong evidence)
- Successful (4-5): 4 (40%) - below 60-80% guidance (small team variance; 3 High Impact + 3 Evolving compress the middle)
- Evolving (2-3): 3 (30%) - above 5-15% guidance, but 2 of 3 are onboarding/ramping (expected)
- Low (0-1): 0 - within 2-5% guidance

## Tashana's checklist completion

- [x] Assess against Job Descriptions / Skill Progression Matrices (not retired Engineering Competencies)
- [ ] High Potential Flag decisions - Juanje, Roni, and Kanitha recommended (needs your approval)
- [ ] Underperformance documentation - Muhamad visibility gap (conversation needed, not formal PIP)
- [ ] QE-to-SE transition conversation - Roni (schedule in next 1:1)
- [ ] Promotion requirements clarification - discuss with Juanje, Roni, Benny, Kanitha, Eitan, Bella
- [ ] Enter ratings and actions in Workday
