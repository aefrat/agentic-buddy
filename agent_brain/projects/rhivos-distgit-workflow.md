---
last_accessed: 2026-07-02
access_count: 1
created: 2026-07-02
---

# RHIVOS Dist-Git Policy and Kernel Derivative Workflow

## Context

Eric Chanude raised (Jul 2, 2026) that the RHIVOS dist-git policies and kernel
derivative component workflow are undocumented and inconsistent. The discussion
spans two threads in #team-toolchain-automotive and involves Eric, contyk (Petr),
Martin Perina, Ozan Unsal, and Max Korpershoek.

## The Problem (Eric's Escalation)

Three issues were raised:

1. **Inconsistent dist-git policies.** downstream-dtbs and qcom-scmi have policy
   exceptions (no commit-level Jira enforcement), but kernel-ivos-nxp-extra-modules
   does NOT - it was missed when exceptions were added. This blocks builds.

2. **Unclear ticket requirements.** contyk confirmed tickets are needed for errata,
   but the policy doesn't enforce this for exempted repos, so it's been skipped.
   Max confirmed he wasn't aware he needed to create Jira tickets when pushing to
   rhivos-2-main.

3. **Release Pending tickets with no apparent owner.** When tickets are created,
   they sit in Release Pending and nobody acts on them.

## contyk's Clarifications (Jul 2, 2026)

Petr provided several key answers in the thread:

### Policy exception history
- Initially disabled for kernel (per Scott Weaver's request - source-git workflow gates commits differently)
- Extended to kernel-ivos-qualcomm, then qcom-scmi and downstream-dtbs (to ease repeated rebuilds)
- kernel-ivos-nxp-extra-modules was missed - **contyk will file a RHELBLD ticket to add the exception**

### Release Pending = effectively closed
- Tickets in Release Pending transition to Closed automatically when pushed to CDN
- No action required from the team on these

### Ticket granularity
- Don't need a ticket per commit
- Work should be tracked - multiple commits/NVR bumps can contribute to the same feature/bugfix
- Tickets are linked to advisories with release notes and are customer-visible
- Think in terms of: "What can be documented as a change for the consumer?" (Bug/Story/Weakness/Vulnerability)

### Branch model (current)
- `rhivos-2-main` = RHIVOS 2.1 development
- `rhivos-2.0` branch = 2.0.z updates
- 2.0 GA is done; any new work goes to 2.0.z or 2.1

### Meeting needed
- contyk himself said he's confused about the status quo and that "we all need to meet and figure it out"

### Jira workflow reference
- Diagram: https://docs.google.com/drawings/d/1A0jxGj5TG6ObPGOzmUbWYxuYlE-wbaJT4ZVSpuvVh0M/edit

## Open Question (Max)

Max asked: for routine rebuilds of qcom-scmi/downstream-dtbs triggered only by a
new kernel (no source change), should he:
1. Create a VROOM ticket for the version bump (like VROOM-44867), or
2. Skip ticket creation since it's on the dev branch (rhivos-2-main / RHIVOS 2.1)?

**This is still unanswered as of Jul 2.**

## Documentation Gap

No single document exists covering the end-to-end workflow:
- When a kernel is built, what do derivative package maintainers do?
- Which Brew tags/targets for which RHIVOS stream?
- When and how to create VROOM tickets for rebuilds?
- Who tags builds into gate/candidate tags?
- What ticket lifecycle looks like post-merge

Related references:
- Dist-git policy rules: https://pkgs.devel.redhat.com/rules.html (and stage equivalent)
- Dist-git policy management docs: https://docs.engineering.redhat.com -> "Managing dist-git policy" (Confluence EXDSPRHELB space)
- Defects/Blockers/Exceptions process: https://spaces.redhat.com/display/Automotive/Defects,+Blockers,+and+Exceptions+Process
- Gator (advisory generation): https://gitlab.cee.redhat.com/automotive/fences/gating/gator
- errata_doc_approver: https://gitlab.cee.redhat.com/gnecasov/docs-errata-approver
- OSCI errata-automation: https://gitlab.cee.redhat.com/osci/errata-automation
- VROOM workflow diagram: https://docs.google.com/drawings/d/1A0jxGj5TG6ObPGOzmUbWYxuYlE-wbaJT4ZVSpuvVh0M/edit
- RHELBLD-18043: Original RHIVOS dist-git policy exception request

## contyk's Build Guide (April 2026, #automotive-release-readiness)

Key reference for build targets and ticket requirements per release:

**Building for GA (e.g., 2.0):**
- Branch: `rhivos-2.0` (or `rhivos-1.0.0` for 1.x)
- Target: `--target rhivos-2.0-candidate`
- Requires: Approved blocker/exception Jira ticket
- Builds NOT auto-promoted; reach out to contyk/toolchain team

**Building for z-stream (e.g., 2.0.z):**
- Branch: same `rhivos-2.0`
- Target: `--target rhivos-2.0-z-candidate` (note the Z)
- Requires: VROOM ticket with z-stream fixVersion

**Building for next release (e.g., 2.1):**
- Branch: `rhivos-2-main`
- Target: `--target rhivos-2.1-candidate`
- No dist-git restrictions, but "make sure you have a product work Jira
  issue filed for future errata references"

## Current Dist-Git Policies (from pkgs.devel.redhat.com/rules.html)

Fetched Jul 2, 2026:
- `rhivos-1-main`: Anything Goes
- `rhivos-2-main`: Anything Goes
- `rhivos-2.0` (default): Strict VROOM ticket + fixVersion + blocker approval
- `rhivos-2.0` exceptions (Anything Goes): kernel-automotive, kernel-ivos-qualcomm,
  downstream-dtbs, qcom-scmi
- **Missing exception:** kernel-ivos-nxp-extra-modules

## Wiki Article

Full knowledge article written to ATC LLM wiki:
`atc_llm_wiki/repo-wiki/concepts/distgit-policy-and-errata-workflow.md`

## Action Items

- [ ] contyk: File RHELBLD ticket to add dist-git policy exception for kernel-ivos-nxp-extra-modules
- [ ] Avihai: Propose and schedule an alignment meeting with contyk, Eric, Martin, Ozan, Max
- [ ] Team: Create end-to-end workflow document (Google Doc) covering the gaps above
- [ ] Resolve Max's open question about routine rebuild ticket requirements

## Draft Reply

A reply was drafted (session Jul 2) acknowledging the gaps and proposing a
documentation effort + alignment meeting. Needs updating to incorporate contyk's
answers before posting.
