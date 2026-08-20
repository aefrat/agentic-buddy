---
last_accessed: 2026-08-20
access_count: 1
created: 2026-07-02
---

# RHAS Testing Gaps

Accumulated observations about testing gaps and blockers. Updated each time the test status skill runs or new information surfaces.

## Critical gaps (blocking Tech Preview)

| Gap | Blocker | Owner | Status | Impact |
|-----|---------|-------|--------|--------|
| No QE lead assigned | PITCREW-337 unassigned | (vacant) | OPEN | No one owns the QE process end-to-end |
| DS CI pipeline not operational | PITCREW-393 resolved (Aug 17). PITCREW-394 pipeline implementation | Matt Minnich | RESOLVED | DS pipeline now operational |
| No release criteria defined | No ticket | (vacant) | NOT STARTED | No measurable definition of "ready to ship" |
| No test strategy document | No ticket | (vacant) | NOT STARTED | No systematic plan for what/how/when to test |
| Distribution not complete | PITCREW-336 blocks PITCREW-337 | | IN PROGRESS | QE Readiness blocked by Distribution epic |

## Significant gaps (needed before GA)

| Gap | Notes | Target |
|-----|-------|--------|
| No E2E workflow test | Full code-commit to test-on-board pipeline not tested end-to-end | Tech Preview |
| No multi-component integration tests | Builder + Jumpstarter + GitOps not tested together | Tech Preview |
| No performance baselines | Build times, provisioning times not measured | GA |
| No security scanning in pipeline | CVE scanning not integrated into CI | GA |
| No scale testing | Concurrent builds, multi-board HiL not validated | GA |
| No upgrade testing | Operator upgrade path not tested | Tech Preview |
| No Keycloak SSO integration tests | Auth flow across components not validated | GA |

## Meeting observations (2026-08-18 Quality Review)

Attendees: Avihai, Pablo Ridolfi, Rachel Sibley, Benny Zlotnik, Mohamad Abo Ras, Miguel Angel Ajo, Paul Wallrabe.

**Decisions:**
- Integration testing will use mock devices/QEMU (avoids physical hardware in test cluster).
- Downstream testing deferred until downstream bits exist (expected before GA, not for TP).

**New gaps identified:**
- No downstream product bits exist yet - cannot test downstream at all.
- No formal test list with entry/exit criteria (Pablo's requirement).
- No Jira feature mapping for TP or GA releases (Rachel's recommendation).
- No Polarion test cases or results tracking (Rachel's standard process).
- No hardware-specific test evidence (GA requirement per Pablo - must test on actual customer platforms).

**Infrastructure progress:**
- Ephemeral cluster operational (end of Jul), one test working (build + flash).
- 3-phase infrastructure roadmap: (1) one test on cluster [done], (2) install JumpStarter in cluster, (3) all upstream tests on cluster.

**Action items assigned:**
- Mohamad: compile and share test list with Pablo, Rachel, and team.
- Team: map features to Jira for TP and GA.
- Miguel: implement mock devices for dev operator + JumpStarter integration testing.

## What exists today (as of 2026-07-02, updated 2026-08-18)

| Area | Status | Evidence |
|------|--------|----------|
| Upstream unit tests | Operational | Per-PR via GitHub Actions + Packit |
| Upstream integration tests | Operational | Per-PR, component-level |
| RHIVOS CTC smoke tests | Operational | Nightly + release-gated, includes Jumpstarter provisioning |
| RHIVOS HiL board tests | Operational | ROSA -> Jumpstarter -> boards, 55 PASS / 4 FAIL / 6 XFAIL |
| bootc image tests | Partially operational | GitLab CEE, some coverage |
| Builder operator basic tests | Exists | OCI image build, pod lifecycle |
| DS CI pipeline | Operational | PITCREW-393 DNS resolved (Aug 17) |
| Ephemeral cluster tests | Operational (1 test) | Build + flash via dev operator + JumpStarter on ephemeral cluster (Jul 31) |
| E2E workflow tests | Does not exist | Benny's doc plans but not implemented |
| Integration tests (dev operator + JumpStarter) | Does not exist | Decision: use mock devices/QEMU (Aug 18 meeting) |
| Formal test list with criteria | Does not exist | Pablo Ridolfi requested; Mohamad to produce |
| Jira feature mapping (TP/GA) | Does not exist | Rachel recommended; needed for traceability |
| Polarion test cases | Does not exist | Rachel's standard; needed for CTC evidence |
| Hardware-specific testing | Does not exist | GA requirement: evidence on customer platforms (Qualcomm, NXP, TI) |
| Release criteria | Does not exist | This agent is creating the first version |

## Gap closure timeline (recommended)

| Milestone | Date | Gaps that must close |
|-----------|------|---------------------|
| Monthly release (Jul) | 2026-07-31 | Builder deploys, smoke tests, board connectivity |
| Monthly release (Aug) | 2026-08-31 | DS pipeline operational, Builder-to-Jumpstarter handoff |
| Monthly release (Sep) | 2026-09-30 | E2E workflow, multi-component integration |
| Tech Preview | 2026-09-29 | All above + docs validation + security scan + upgrade test |
| GA | 2026-12-22 | All above + scale + soak + Keycloak + customer validation |
