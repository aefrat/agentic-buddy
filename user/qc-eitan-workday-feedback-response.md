# Manager Response - Eitan Raviv - CY26 Q2 Quarterly Connection
## Feedback & Development Section (Workday copy-paste)

---

Hi Eitan,

Thank you for your honest reflection. You described your development trajectory as "continued hands-on work, with an inclination to go deep into an area in order to enhance it," and I think that is a very accurate self-read. I want to build on that with concrete feedback I have observed and collected from peers, stakeholders, and our day-to-day interactions this quarter.

**Feedback from peers and stakeholders (Q2 2026):**

Your teammates and cross-team colleagues consistently recognize you as the infrastructure expert people turn to when they need things done right.

Hubert Stefanski publicly called you "our runner expert" on Slack when Amit from the FuSa QE team needed help with runner infrastructure, and in a separate thread told the automotive-image-builder group that you have "a nice setup that we can re-use relatively easily." That is strong peer recognition - Hubert is not someone who gives compliments loosely, and the fact that he directs people to you by name tells me you have earned real credibility in this domain.

When the RHIVOS webserver security policy exception came up in May, you did something that stood out to me. Rather than just renewing the exception or escalating it, you proactively proposed decommissioning the webserver entirely, with a clear rationale: "Since enterprise authentication is complex to implement and CloudFront appears stable, I vote to decommission the rhivos webserver." Four people responded positively. Hubert confirmed the DNS already pointed to s3pi. Matt Goldman said "stopping it and waiting for a scream isn't a bad process." Juanje agreed it was safe to remove. I approved it and gave you the green light. That entire thread is a good example of what I value in your work - you did not just resolve the immediate issue, you identified and proposed the right long-term solution, engaged the right people, and drove the discussion to a decision. That is leadership behavior.

The IT Cloud team (Cesar Ortega) worked with you on the VPC networking and DNS resolution challenge for the RHAS-CI Jumpstarter environment. He trusted your Terraform-based proposal, moved your account to an unrestricted OU so you could manage networking directly, and told you "let me know how it goes." That kind of trust from an external team does not happen by accident - it comes from the technical quality of your proposals and the way you communicate them.

Amit from the QE team thanked you and Hubert for your responsiveness on runner infrastructure requests. Evgeni came to you directly for IAM and AWS pipeline access help. Sergei Gromeniuk from the ContCert team recommended you by name to another team, saying "Eitan Raviv helped us to move our EC2 instance and it worked well" - that is unsolicited peer endorsement, and it tells me your reputation extends beyond our immediate team.

Nisha Saini cited your security insight about container variable exposure as authoritative input during an ESS/SOA compliance discussion. That means your technical judgment is being used as a reference point in compliance decisions, which is meaningful.

**My observations as your manager:**

This quarter I entrusted you with expanded ownership - taking over the auto-toolchain-infrastructure CMDB service from Hubert, owning the gating domain, and becoming the primary contact (with Matt) for VHCL-009 infrastructure issues going forward. I did that because the evidence shows you are ready for it. You handle infrastructure with care, you communicate proactively during incidents (your multi-channel CloudFront outage updates were a good example), and you follow through on commitments.

The GitLab runner consolidation was the highlight of the quarter for me. Combining the SOA, Services, and Gating pipelines into shared pools, and doing the same for pipe-x-release and RHAS-CI Jumpstarter, delivered real budget savings. What made it stand out is that nobody asked you to do it - you saw an opportunity, understood the isolation requirements, validated the approach, and rolled it out without disrupting active pipelines during our release cycle. That is the kind of initiative I want to see more of.

Your adoption of claude-code was also notable. You did not just try it out - you built reusable hooks and skills (Jira ticket creator, notification hook, GitLab MR fetcher) that make your daily workflow meaningfully faster. That approach of going deep into a tool and building something practical around it is very much aligned with your self-described development style.

I also want to acknowledge the "grey work" you mentioned - token refreshes, Bitwarden housekeeping, vulnerability patching, Jira migration cleanup. This work is invisible in sprint demos but essential for keeping our infrastructure secure and operational. I see it and I appreciate it.

**Strengths (summary):**

- Infrastructure depth and reliability - you are the person the team and external stakeholders trust with AWS, runners, CloudFront, and CI/CD infrastructure
- Proactive problem-solving - the webserver decommission proposal is a clear example of identifying the right solution rather than the easy one
- Cross-team navigation - you work effectively with IT Cloud, PSCA, GRC, BOA, and other teams without needing hand-holding
- AI tooling adoption - you went beyond experimentation into building practical, reusable tools
- Honest, steady delivery - 11 tickets, 28 MRs, and consistent operational stewardship across the quarter

**Career development discussion:**

Your instinct to "go deep and enhance" is a real strength, and I want to help you channel it toward the next level of impact. Based on Red Hat's job leveling framework, you are solidly performing at IC Level 3 (Senior Software Engineer) and showing emerging signals of IC Level 4 (Principal Software Engineer) in several areas - particularly the runner consolidation (cross-subsystem scope, measurable business impact) and the AI tooling work (introducing new methodologies).

The gap between where you are and Level 4 is not about working harder or taking on more tasks. It is about making your depth visible and scalable. Here is what I mean:

1. **Formalize and share your AI tooling work.** You built claude-code hooks and skills that save you time every day. The next step is sharing these with the team, documenting the patterns, and helping others adopt them. That turns personal productivity into team-wide methodology - which is exactly what Level 4 expects ("evaluate and introduce new AI-driven methodologies"). This fits your natural style perfectly: you already went deep, now let others benefit from that depth.

2. **Document the runner consolidation as a CI/CD optimization strategy.** You have a story with real numbers: reduced EC2 count, budget savings, no disruption during a release cycle. Write it up as a design document or internal blog post. Present it at a demo or tech talk. This builds your visibility as an expert and demonstrates Level 4 knowledge sharing. Your depth-first approach produces exactly the kind of detailed, practical content that engineers value.

3. **Expand infrastructure mentoring.** The Gator sessions with Hubert were a good start. With Matt Goldman ramping up on SRE and you taking over more infrastructure ownership, there is a natural opportunity to establish regular knowledge-sharing sessions on AWS patterns, runner architecture, and operational practices. Level 4 expects mentoring that goes beyond onboarding new members - it is about coaching peers and shaping how the team approaches infrastructure decisions.

4. **Scale your quality practices.** The s3pi integration tests show you value test coverage. The next step is proposing integration testing patterns or templates that other ATC services can adopt. This moves you from "own code quality" (Level 3) to "establish and monitor testing practices for multiple teams" (Level 4).

5. **Lead a cross-team initiative end to end.** You already contribute across teams (Distribution Focus, PSCA, BOA, IT Cloud). The Level 4 shift is from contributing to owning - driving alignment between teams, coordinating decisions, and being the person others come to for infrastructure strategy, not just infrastructure help.

I want to be clear: these are growth opportunities, not gaps. You are performing well at your current level and the feedback from peers confirms that. The question is how to position the depth you naturally bring so it creates impact at the next level. Let us discuss specific goals and timelines in our next 1:1 so we can turn these into a concrete plan for the second half of the year.

**Impact/Career Growth:**

Eitan, I appreciate you being direct about where you want to go. You said you want to "continue with hands-on software engineering," that you like to "go deep into a subject matter and enhance it to production-level grade," that you see yourself moving toward an AI "overseer" role where you direct AI to do implementation work, and that you would like to reach Principal Software Engineer at some point in the future. That is a clear and honest self-assessment, and I want to help you get there.

The good news is that your natural working style - going deep, designing new functionality, creating efficiencies, and implementing them - is exactly what the Principal SE role values. The path from Senior to Principal is not about changing what you do. It is about expanding the reach and visibility of how you do it.

*Skills most relevant to your current role (Senior SE) that you are strong in:*

- Infrastructure engineering (AWS, CloudFront, CI/CD pipelines, Terraform) - this is your core and you are performing well here
- Security and compliance awareness - you handle vulnerability remediation and compliance decisions with good judgment
- Troubleshooting and root cause analysis - the VPC/DNS resolution work and CloudFront debugging show strong diagnostic skills
- Cross-team collaboration - you navigate external teams (IT Cloud, PSCA, GRC) effectively and independently
- AI-assisted development - your claude-code adoption with custom hooks and skills puts you ahead of most engineers in practical AI tooling

*Skills you need to grow for Principal Software Engineer (IC Level 4):*

- Technical leadership and influence - moving from "the person who fixes infrastructure" to "the person who shapes how the team thinks about infrastructure." You are already showing this with the runner consolidation and the webserver decommission proposal. The next step is doing it more deliberately and consistently
- Knowledge formalization - your depth produces real expertise, but right now it lives mostly in your head and in Slack threads. Writing design documents, blog posts, or presenting at tech talks turns that expertise into something durable and visible. This is one of the clearest differentiators between Level 3 and Level 4
- Strategic thinking - connecting your technical work to business outcomes. The runner consolidation is a perfect example: you reduced EC2 costs. At Level 4, you would frame that proactively as a CI/CD optimization strategy, present the cost impact to stakeholders, and propose the next round of improvements. The technical work is the same - the framing and communication change
- Mentoring and coaching - not just onboarding new members (which you already do well with the Gator sessions), but shaping how more experienced colleagues approach problems. With Matt Goldman joining and Hubert transitioning, you have a natural opportunity here
- AI workflow design - your vision of becoming an AI "overseer" is forward-thinking and aligns with where the industry is heading. To get there at Level 4, you should move from building tools for yourself to evaluating and introducing AI methodologies for the team. Document which tasks AI handles well in your workflow, which ones still need human judgment, and share those patterns. That positions you as a leader in AI-augmented engineering, not just a user of it

*Concrete next steps for H2 2026:*

1. Pick one piece of your deep work this quarter (runner consolidation or claude-code skills) and write it up as an internal blog post or design document. Present it at a team demo or broader tech talk. This is the single highest-leverage action for Level 4 visibility
2. Explore Red Hat Core Skills in Workday and update your skills profile. This will improve your recommendations in Career Hub for projects, contacts, and internal opportunities that match where you want to grow. Focus on adding your infrastructure, CI/CD, and AI tooling skills so the system can surface relevant opportunities
3. Set up a recurring knowledge-sharing session (monthly or bi-weekly) on infrastructure patterns with Matt and other interested team members. This builds the mentoring track naturally
4. In our next 1:1, let us map out a timeline for when you want to target Principal SE and work backward to identify which Level 4 differentiators to focus on first. Based on this quarter, I would suggest starting with knowledge sharing and AI methodology leadership - they align most closely with your stated inclination and require the least change to how you already work

Your aspiration to reach Principal Software Engineer is realistic and well-grounded. You are not starting from scratch - you already have Level 4 signals in business impact (runner consolidation), AI methodology (claude-code tooling), and cross-team scope. The work ahead is about consistency and visibility: doing what you already do naturally, but making sure it is seen, shared, and scaled. I am here to support that journey and I look forward to discussing a concrete plan together.

I am proud of your work this quarter, Eitan. Keep going deep - and let us work together on making that depth more visible.

Avihai
