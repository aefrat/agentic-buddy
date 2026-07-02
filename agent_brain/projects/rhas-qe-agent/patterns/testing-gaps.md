---
last_accessed: 2026-07-02
access_count: 0
created: 2026-07-02
---

# RHAS Testing Gaps

Accumulated observations about testing gaps and blockers. Updated each time the test status skill runs or new information surfaces.

## Critical gaps (blocking Tech Preview)

| Gap | Blocker | Owner | Status | Impact |
|-----|---------|-------|--------|--------|
| No QE lead assigned | PITCREW-337 unassigned | (vacant) | OPEN | No one owns the QE process end-to-end |
| DS CI pipeline not operational | PITCREW-393/394 blocked by DNS (Evgeni Vakhonin) | Matt Minnich | BLOCKED | Cannot run downstream integration tests |
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

## What exists today (as of 2026-07-02)

| Area | Status | Evidence |
|------|--------|----------|
| Upstream unit tests | Operational | Per-PR via GitHub Actions + Packit |
| Upstream integration tests | Operational | Per-PR, component-level |
| RHIVOS CTC smoke tests | Operational | Nightly + release-gated, includes Jumpstarter provisioning |
| RHIVOS HiL board tests | Operational | ROSA -> Jumpstarter -> boards, 55 PASS / 4 FAIL / 6 XFAIL |
| bootc image tests | Partially operational | GitLab CEE, some coverage |
| Builder operator basic tests | Exists | OCI image build, pod lifecycle |
| DS CI pipeline | Not operational | Blocked by DNS (PITCREW-393) |
| E2E workflow tests | Does not exist | Benny's doc plans but not implemented |
| Release criteria | Does not exist | This agent is creating the first version |

## Gap closure timeline (recommended)

| Milestone | Date | Gaps that must close |
|-----------|------|---------------------|
| Monthly release (Jul) | 2026-07-31 | Builder deploys, smoke tests, board connectivity |
| Monthly release (Aug) | 2026-08-31 | DS pipeline operational, Builder-to-Jumpstarter handoff |
| Monthly release (Sep) | 2026-09-30 | E2E workflow, multi-component integration |
| Tech Preview | 2026-09-29 | All above + docs validation + security scan + upgrade test |
| GA | 2026-12-22 | All above + scale + soak + Keycloak + customer validation |
