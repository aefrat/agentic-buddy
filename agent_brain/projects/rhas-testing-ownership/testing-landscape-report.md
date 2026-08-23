---
last_accessed: 2026-08-23
access_count: 4
created: 2026-06-30
---

# RHAS Testing Landscape Report

Generated: June 30, 2026 | Last refreshed: July 21, 2026
Sources: PITCREW Jira, PitCrew Full Report (Jun 1), Slack (#team-pitcrew-automotive,
#team-toolchain-automotive, #automotive-image-builder, #test-validator-bot),
Benny Zlotnik verbal input (PDR Staff Meeting).

---

## Executive Summary

**Release naming:** RHAS uses RHAS-MMYY format (MM=month, YY=year). See `agent_brain/projects/rhas-qe-agent/reference/release-naming-convention.md`.

RHAS testing is split into two tracks - **upstream** and **downstream** - with
different maturity levels. Upstream testing is **operational and running per PR**
(Mohamad Abo Ras). Downstream testing **has no working pipeline yet** - Evgeni
Vakhonin has been building the infrastructure since March 2026, and as of Jun 29
the CI is failing due to infra misconfiguration. There is **no formal QE process**
(PITCREW-337 is unassigned, no comments, no test plans). The gap between "tests
exist in individual repos" and "structured QE that gates releases" is the
primary risk for Tech Preview (RHAS-0926, September 2026) and GA (RHAS-1226, December 2026).

---

## 1. Upstream Testing (US)

**Owner:** Mohamad Abo Ras
**Status:** Operational - running per PR
**What's tested:** Builder Operator and Jumpstarter Operator (upstream)

### What We Know

- US testing runs on every PR in the upstream GitHub repos
  (jumpstarter-dev, automotive-image-builder)
- Mohamad demoed E2E testing at a sprint demo; Paul Wallrabe asked whether the
  E2E test includes the OCI artifact contract with Jumpstarter (Jun 13,
  #team-pitcrew-automotive) - unclear if answered
- bootc testing is actively developed at
  `gitlab.cee.redhat.com/automotive/tests/all` (bootc-testing plans) - Martin
  Perina (mperina) is the primary contributor
- bootc tests create images and use Jumpstarter to provision and test on
  physical boards
- Packit is used to build AIB RPMs upstream
  (`gitlab.com/CentOS/automotive/src/automotive-image-builder`)
- The `test-validator-bot` fires on every MR to the tests/all repo, validating
  test plan changes (frequent activity from mperina and pbrilla)

### Infrastructure

- **GitHub Actions** for upstream PRs (Builder, Jumpstarter)
- **Packit** for upstream RPM builds (AIB)
- **Testing Farm** for test execution on VMs (external testing farm for bluechi;
  internal testing farm under discussion for RHAS)
- **Jumpstarter** for hardware-in-the-loop testing on physical boards
- **GitLab CEE** (`automotive/tests/all`) for bootc test development and CI
- Tests are **pytest-based** (Jumpstarter's test harness)

### Gaps

- No documentation of what exactly the US test suite covers
- Paul's question about OCI artifact contract coverage unanswered (as far as
  we can tell from Slack)
- Mohamad had console access issues (Jun 22) - his RH user is in the wrong
  org (11009103 instead of 6340056), blocking OpenShift cluster access

---

---

## Benny Zlotnik's Testing Architecture Doc

Source: [Google Doc](https://docs.google.com/document/d/1NEzWHE1K4CiGkEDjhL5gpQUpcnepsiBvMDWPXUxLOHQ/edit?tab=t.0)
(Title: "Jumpstarter + automotive-dev-operator Testing")

This is Benny's documentation of the RHAS testing strategy. It defines three
layers:

### Layer 1: Jumpstarter E2E Tests
- Upstream E2E tests for Jumpstarter
- Run on **kind clusters** (suitable for Jumpstarter)

### Layer 2: automotive-dev-operator (Builder) E2E Tests
- Upstream E2E tests for the Builder
- Also run on **kind clusters** - but Benny notes this is "less ideal for the
  builder, as it is tailored for OpenShift"

### Layer 3: Black-box Testing (RHAS CI - PITCREW-275)
This is the downstream integration testing, split into two phases:

**Phase 1:** Install the builder and run build, flash, and workspaces tests
against the ROSA dev cluster, using a CI Jumpstarter account on all board types.

**Phase 2:** Install a Jumpstarter instance with boards set up and perform
testing using that instance.

Additionally: run the same upstream E2E tests on OpenShift to ensure they work
on the target platform (not just kind).

### Cadence Decision (Open)
- Large volume of commits suggests **nightly** runs
- But nightly makes it harder to identify the offending commit
- No decision recorded yet

### Key Takeaway
The doc confirms the architecture: US tests run per-PR on kind, DS tests (when
operational) will run the same tests + additional integration tests on real
OpenShift with real boards. The kind-vs-OpenShift gap for Builder is explicitly
acknowledged as a risk.

---

## 2. Downstream Testing (DS)

**Owner:** Evgeni Vakhonin
**Status:** Building infrastructure - not yet operational
**What's tested:** Nothing yet (pipeline not working)

### Ticket Chain

1. **PITCREW-275** (Closed, May 18) - Research: evaluated OpenShift on AWS,
   PROW CI via Gingway API, Cluster-bot with external trigger, ROSA, and SNO
   on ATC infra. **Decision: ephemeral IPI SNO arm64 on ATC AWS infrastructure.**
2. **PITCREW-393** (Review, Jul 13) - Acquire prerequisites and credentials
   from Automotive Toolchain admins. Evgeni has been working with Eitan Raviv
   since May 18 on AWS IAM, DNS resolution, pull secrets.
   - **Latest (Jul 13):** "some progress on toolchain side. we're in contact
     to see if anything moved forward."
   - Jul 6: "checked with Eitan from toolchain - no fix yet on his side."
   - Jun 30: "Blocked waiting for the toolchain team to solve the CI worker
     permissions."
   - Jun 29: "the CI is failing, blocked by a misconfiguration on the infra
     side. working with Eitan to solve it on his side"
   - Jun 28: Working cluster install and destroy achieved (with workarounds for
     missing permissions). Pushed to CI, pipeline running.
   - Jun 21: "significant progress" - most permission issues sorted against
     ATC AWS infra
3. **PITCREW-394** (New, Jun 28) - Implement pipeline to install OpenShift with
   operators and run tests. Soft-blocked on VROOM-44573 (DNS + orphan security
   groups). Evgeni: "I'll be able to progress almost to completion while waiting."
   No updates since Jun 28.

### Infrastructure Design

- **GitLab CEE CI** (`gitlab.cee.redhat.com/automotive/jumpstarter/rhas-ci`) -
  created Mar 31 by Evgeni
- **Ephemeral IPI SNO arm64** on AWS via ATC shared account
- **Temporary credentials** via ccoctl (Service Control Policies enforced -
  cannot do single-step automated installation)
- **DNS:** Private cluster with Route 53 zone delegation from Eitan. Currently
  broken - Infoblox (redhat.com authoritative) cannot resolve
  `api.rhas-ci.jumpstarter.auto-toolchain.redhat.com` (IT Ticket UR0191597
  pending). VPC-internal resolution works.
- **Pipeline will:** Install OCP cluster -> Deploy Builder operator -> Deploy
  Jumpstarter operator -> Run E2E tests -> Destroy cluster
- **Linked ticket:** VROOM-44573 (Eitan Raviv, In Progress) - IAM user for
  RHAS CI Part 2: DNS resolution + orphan security group cleanup
- **Linked ticket:** VROOM-39718 (Closed) - Original IAM user creation

### Blockers

1. DNS resolution blocking CI pipeline - still unresolved as of Jul 13. Evgeni
   noted (Jul 13 on VROOM-44573) that the proposed DNS fix will not work with
   OpenShift clusters because the cluster API and apps run on ELBs managed by
   the cluster, not on the EC2 instance. Needs wildcard DNS for
   *.apps.rhas-ci.<domain>. The DNS approach itself is now in question.
2. VROOM-44573 still open (DNS + orphan SG) - Eitan Raviv, In Progress
3. IT Ticket UR0191597 pending for DNS record creation
4. No test cases written yet (PITCREW-394 is about the pipeline, not the tests
   themselves)

---

## 3. Hardware-in-the-Loop Testing (Jumpstarter)

**Owners:** Miguel Angel Ajo Pelayo (primary), Martin Perina (bootc tests)
**Status:** Operational for RHIVOS CTC; RHAS-specific HiL not yet separated

### Current State

- **PITCREW-384** (In Progress, Epic) - "Use Jumpstarter for testing RHIVOS" -
  owned by Miguel Angel, labeled MUSTHAVE
- RHIVOS CTC uses Jumpstarter on physical boards (8650, 8775, 8979, 8255, NXP)
- Test Console shows CTC results at `test-console.corp.redhat.com/rhivos-testing/ctc`
- Lab maintenance automated: smoke tests, firmware reflashes, device health
  monitoring (55 PASS, 4 FAIL, 6 XFAIL on Jun 23)
- **~~Flaky E2E issue (PITCREW-403):~~** CLOSED. "Connection to exporter lost"
  during lease acquisition - was fixed. Root cause was corrected (original
  analysis of race condition in listenQueues sync.Map was incorrect per ticket
  update). No longer a risk.
- Jumpstarter 0.9.0-rc.1 auto-upgraded on cluster (Jun 27) - Benny noted need
  for future gating on auto-upgrades
- External monitoring at `monitor.ajo.es/status/jumpstarter`
- Board bringup agent with CAIB and JMP at
  `gitlab.cee.redhat.com/automotive/ai/agents/hardware-enablement/board-bringup`
  (Brian Benson, Jun 22)

### HiL Testing Scope

| Board Family | Status |
|---|---|
| QC SA8650 (ES21/ES22) | Active in CTC |
| QC SA8775 (ES21/CS4/CS5) | Active in CTC |
| QC SA8979 | Enabled |
| QC SA8255 | Enabled |
| NXP S32N79 | Enabled |
| NXP iMX8 | Q4 target |
| Renesas R-Car X5H | Q4 target |
| Nissan cluster | Board shipped May 28, namespace issues Jun 1 |

---

## 4. CTC / Gating (Integration with ATC)

**Epic:** PITCREW-331 (In Progress, Unassigned, no comments)
**What:** CTC already uses RHAS/Jumpstarter for RHIVOS validation pipelines

### Current State

- CTC makes ship/no-ship decisions based on RHAS test results
- Known issues: logs lack timestamps, test results don't always roll up
  correctly, subresult indicators can be misleading, console output has
  non-printable characters
- RHAS-adapter may move to separate namespace for cleanliness and testing new
  artifact server versions (majopela discussion, Jun 22)
- CTC is the most direct proof that RHAS works under production pressure

---

## 5. QE Readiness

**Epic:** PITCREW-337 (In Progress, Unassigned, 0 comments)
**Target:** RHAS-1026 (October 2026)

### Current State (as of Jul 21)

- **No QE plan exists** for RHAS
- **No regression suites** defined
- **No release qualification criteria** defined
- Epic description explicitly states: "QE readiness is not about adding tests
  to the codebase - engineering already does that. It is about having a formal
  process that defines what 'ready to ship' means."
- Blocked by Distribution epic (PITCREW-336, New, still unassigned)
- **Still no one assigned, zero comments** - no movement since ticket creation.
  This is now 3+ months old with no activity. Tech Preview is 70 days away.
- **PITCREW-42** ("productization: QE plan for official release") is also
  unassigned, still a template with no real content. Reporter: Allison King.
  This is the original QE plan ticket predating the RHAS-era PITCREW-337.

### Related Testing Bugs (Unresolved)

These PITCREW tickets affect test result accuracy and reliability:

| Ticket | Summary | Status |
|---|---|---|
| PITCREW-413 | Oculus HTML renderer shows "Tests failed to run" despite passing subresults | New |
| PITCREW-144 | Test ended in error is not reflected in API request payload | New |
| PITCREW-129 | Failed tests are not reflected on subresults bar | New |
| PITCREW-112 | Skipped result status missing from test case summary | New |
| PITCREW-110 | AVC check failures not rolling up to main test case result | New |

These are CTC-facing bugs - CTC makes ship/no-ship decisions based on these
results (see PITCREW-331 epic description).

---

## 6. Key People

| Person | Role | Focus |
|---|---|---|
| Evgeni Vakhonin | RHAS CI engineer | DS testing pipeline (PITCREW-275/393/394) |
| Mohamad Abo Ras | E2E US testing | Upstream per-PR testing |
| Miguel Angel Ajo Pelayo | Jumpstarter lead | HiL, lab ops, cluster management |
| Martin Perina (mperina) | bootc testing | bootc test development, Jumpstarter integration |
| Benny Zlotnik | Platform/infra | Testing knowledge (doc pending), secrets migration |
| Eitan Raviv | ATC infra | AWS IAM, DNS for RHAS-CI cluster |
| Paul Wallrabe | Engineering Director | Strategic direction, HATCI engagement |

---

## 7. Infrastructure Summary

```
UPSTREAM (Operational)
  GitHub PRs --> GitHub Actions --> pytest
  Packit --> RPM builds (AIB)
  Testing Farm --> VM-based tests
  Jumpstarter --> HiL board tests
  GitLab CEE (automotive/tests/all) --> bootc tests

DOWNSTREAM (Building)
  GitLab CEE (jumpstarter/rhas-ci) --> Pipeline (WIP)
    --> Ephemeral IPI SNO arm64 on ATC AWS
    --> Deploy Builder Operator
    --> Deploy Jumpstarter Operator
    --> Run E2E tests
    --> Destroy cluster
  BLOCKED: DNS misconfiguration (Jun 29)

HARDWARE-IN-THE-LOOP (Operational)
  ROSA cluster (auto-devcluster) --> Jumpstarter controller
    --> Physical boards (QC, NXP, Renesas)
    --> Smoke tests, CTC validation
    --> Test Console reporting

CTC GATING (Operational, rough)
  RHAS/Jumpstarter --> CTC validation pipelines
    --> test-console.corp.redhat.com
    --> Ship/no-ship decisions
```

---

## 8. Risk Assessment

### Critical

1. **No DS testing pipeline yet** - Tech Preview is RHAS-0926 (September 2026). DS
   pipeline has been in development since March with persistent infra blockers.
   DNS approach itself is now questioned (Jul 13) - OpenShift ELB architecture
   incompatible with proposed DNS fix.
2. **QE Readiness epic is empty** - No plan, no owner, no test strategy. Target
   is RHAS-1026 (October 2026) but depends on Distribution (also not started). Zero comments on
   PITCREW-337 after 3+ months. This remains the single biggest blocker.
3. **Benny's testing doc is minimal** - The Google Doc exists but is only a few
   paragraphs. Covers architecture (3 layers) but no specifics on test cases,
   coverage, pass/fail criteria, or operational runbook. Needs expansion.

### High

4. **Mohamad console access blocked** - Wrong org assignment prevents cluster
   access. Basic operational blocker. (Status unknown - not re-verified Jul 21.)
5. ~~**Flaky E2E tests** (PITCREW-403)~~ - **RESOLVED.** Closed as of Jun 26.
6. **No formal test plan** for RHAS as a product - individual operator/service tests
   exist but no integration test strategy spanning Builder Operator + Jumpstarter Operator +
   Konflux + GitOps + Keycloak services.
7. **DNS resolution approach is wrong** - Evgeni's Jul 13 analysis on
   VROOM-44573 shows the proposed DNS fix won't work for OpenShift (needs
   wildcard DNS for ELBs, not static EC2 records). This may require a
   fundamentally different approach, extending the blocker timeline. Elevated
   from Medium to High.

### Medium

8. **Auto-upgrade of Jumpstarter** on production cluster without gating -
   Benny flagged, MR pending.
9. **Miguel Angel load** - carries lab ops, cluster management, customer
   escalations, and documentation. Key-person risk for HiL testing.
10. **Konflux onboarding (PITCREW-335) stalled** - unassigned, no comments,
    blocks Distribution which blocks QE Readiness. Chain of inaction.

---

## 9. Recommendations

1. **Get Benny to expand the testing doc** - The doc exists but is minimal (a
   few paragraphs). Needs: specific test cases, coverage matrix, pass/fail
   criteria, operational runbook, cadence decision (nightly vs per-PR for DS).
2. **Assign QE Readiness (PITCREW-337)** - Needs an owner immediately. Without a
   QE plan, Tech Preview and GA dates are aspirational.
3. **Unblock Evgeni's DS pipeline** - The DNS/IT blocker (UR0191597) needs
   escalation. This has been grinding since March.
4. **Fix Mohamad's org/console access** - Basic blocker, should be resolved
   in days not weeks.
5. **Create an integration test strategy** - Currently testing is per-operator/service.
   The product (RHAS) integrates multiple operators (Builder, Jumpstarter) and services (Konflux, GitOps, Keycloak) -
   integration testing across operators and services is not covered.
6. **Define what "tested" means for each RHAS release** - No release
   qualification criteria exist. Every release before GA should have explicit
   pass/fail gates.
