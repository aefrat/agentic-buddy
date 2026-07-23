# RHAS Feature-to-Release Map with Testing Framework

Generated: 2026-07-22
Source: PitCrew Jira project (live data)
Purpose: Map delivered and planned features to releases, derive Spec/BDD/TDD testing approach for release criteria.

---

## 1. Delivered Work (Done through Jul 2026)

### RHAS-0226 + RHAS-0426 (Dev Preview) - SHIPPED

**Parent: Developer Experience MVP**

| Epic | Key | Status | Acceptance Criteria Summary |
|------|-----|--------|-----------------------------|
| RHIVOS Developer Story - MVP | PITCREW-208 | Closed | Code from browser (DevSpaces), build on remote ARM, test on real board (Jumpstarter), publish image, flash to board, Developer Hub portal |
| Easy-Peasy Developer Onboarding | PITCREW-200 | Closed | One-click "Onboarding" button, git repo with manifest builds RHIVOS image, no intervention required |
| Developer Flow with DevSpaces | PITCREW-195 | Closed | Inner loop (devspace + app + Jumpstarter test), inner-to-outer loop trigger, local build + push triggers outer loop |
| Automotive-dev Operator | PITCREW-196 | Closed | Operator deploys DevSpaces, build/test pipelines, Jumpstarter, Developer Hub, user accounts/secrets, Konflux support |
| Complete Product Experience | PITCREW-180 | Closed | (no AC documented) |
| Internal RHIVOS Dev Cluster | PITCREW-185 | Closed | (no AC documented) |
| RHAD Program Requirements | PITCREW-172 | Closed | Requirements gathering |
| RHAD BU/PM Requirements | PITCREW-173 | Closed | Requirements gathering |
| RHAS Engineering Requirements | PITCREW-176 | Closed | Requirements gathering |

### RHAS-0526 - SHIPPED

**Parent: Observability + Lab Reliability Foundation**

| Epic | Key | Status | Acceptance Criteria |
|------|-----|--------|---------------------|
| End-to-End Trace | PITCREW-291 | In Progress | Single trace ID connects build/deploy/boot/test; device-side events in same trace; structured JSON API; no perf degradation on constrained HW; works without internet connectivity. **Note: 10/19 children still New - telemetry correlation incomplete** |
| Lab C2 Recovery Time (24h) | PITCREW-222 | In Progress | Infra-as-code (Ansible/Terraform); runbook for rebuild from zero; external deps identified; dry-run validates 24h rebuild; alerts on total failure |
| Lab C2 Recovery Point (4h) | PITCREW-223 | In Progress | Automated backups every 4h; off-cluster storage; validated restore procedure; alerts on backup failure/replication lag |

### RHAS-0626 - SHIPPED / WRAPPING UP

**Parent: Build Pipeline + Virtual Targets**

| Epic | Key | Status | Acceptance Criteria |
|------|-----|--------|---------------------|
| Konflux Onboarding | PITCREW-335 | In Progress | All components via Konflux with signed provenance; reproducible builds; no dev workflow friction; automatic supply chain attestations; no non-Konflux pipeline. **Children: 2/6 closed** |
| Android Virtual Target Deployment | PITCREW-298 | In Progress | Cuttlefish on OpenShift via QEMU+KVM on ARM bare-metal; Jumpstarter exporter pods with start-avm sidecars; programmatic adb interaction; ADR co-authored with HATCI; upstream Apache 2.0; HATCI validates. **No children** |

---

## 2. Current Sprint (RHAS-0726 - due Jul 28)

**Theme: Internal Customer Adoption + Compliance + Platform Autonomy**

| Epic | Key | Status | Acceptance Criteria | Children |
|------|-----|--------|---------------------|----------|
| CTC Adoption | PITCREW-331 | In Progress | CTC runs validation as primary workflow; accurate test results (failures/warnings/skips); timestamped logs with version info; all CTC bugs prioritized; trusted for ship/no-ship decisions | 8/19 closed, 11 open (subresult indicators, non-printable chars, AVC rollup, skipped status, missing logs) |
| RH-SDLC Compliance | PITCREW-334 | In Progress | All SDLC gates identified+owned; security reviews complete; vuln management active within SLA; secure coding documented; audit-ready at any time; continuous compliance | 3/13 closed, SOA in progress, remaining: threat model, SAST, DAST, SAR, pentest, secure signing, secure distribution |
| Lab Infrastructure | PITCREW-330 | New | Infra defined in code; versioned+reviewable changes; rebuild from scratch documented; HW inventory machine-accessible; infra-level monitoring | 4/14 closed, remaining: HW onboarding, board enablement (Renesas H5X, NXP S32N79, SA8255P) |
| Autonomous Platform Reactions | PITCREW-294 | New | Structured events with trace context; auto-isolate crashing devices + preserve artifacts; auto-correlate clustered build failures; auto-retry provisioning with backoff; all actions in trace store; engineers can stop any agent; default notify-only; works without internet connectivity | **0 children - not broken down** |

---

## 3. Planned Work (RHAS-0826 through GA)

### RHAS-0826

| Epic | Key | Status | Acceptance Criteria | Children |
|------|-----|--------|---------------------|----------|
| Virtual Target Orchestration | PITCREW-299 | New | Dynamic exporter pod creation; architecture-aware worker node selection; idle reclaim with configurable timeout; FIFO lease queue; cluster capacity as only constraint; HATCI validates 25-developer concurrent load | 13 children (ExporterSet CRDs, scaling logic, QEMU provisioner - active dev) |
| Seconds-per-Iteration | PITCREW-295 | New | Push changed files without full rebuild; service restart without reboot; clean revert to base image; seconds not minutes; actions in session trace; works virtual+physical; single-developer-per-device lock | **0 children - not broken down** |

### RHAS-0926 (Tech Preview)

| Epic | Key | Status | Acceptance Criteria | Children |
|------|-----|--------|---------------------|----------|
| Distribution | PITCREW-336 | New | All artifacts through official Red Hat channels; versioned docs per release; standard Red Hat install/update/uninstall tooling; full lifecycle support; no unsupported distribution methods | 5 children (CLI via DNF on RHEL/CentOS/Fedora, Mac/Win/Linux, Python collections) |
| External Dependency Resilience | PITCREW-329 | In Progress | Graceful degradation when external deps unavailable; clear error messages (external vs internal); critical deps documented with failure modes; caching/retries/fallbacks; monitoring detects degradation before users | 3 children (1 closed DNS bug, 2 open) |

### RHAS-1026

| Epic | Key | Status | Acceptance Criteria | Children |
|------|-----|--------|---------------------|----------|
| QE Readiness | PITCREW-337 | In Progress | QE plan with scope/strategy/release criteria; regression suites run before every release; release qualification criteria defined; full product surface covered; gaps between eng testing and QE identified | 3 children |
| Product Documentation | PITCREW-338 | New | Official docs on Red Hat channels; covers install/config/usage/troubleshooting/upgrade; versioned per release; onboarding guide zero-to-working without tribal knowledge | 0 children |
| Unified Developer Session | PITCREW-292 | New | SSO for all platform functions; fast workspace provisioning; non-interactive mode for CI/agents; on-demand virtual devices; session ID in all traces; cleanup releases resources; resource limits | 10 children |

### RHAS-1126

| Epic | Key | Status | Acceptance Criteria | Children |
|------|-----|--------|---------------------|----------|
| ATC Adoption | PITCREW-332 | New | Declarative image spec + auto-build; test against target HW (build-to-test loop); incremental CI/CD integration; all bugs as product defects; structured feedback into roadmap; go/no-go decision | 0 children |
| Virtual Interface Simulation | PITCREW-300 | New | Bluetooth via RootCanal as Jumpstarter driver; BT discovery/pairing/Android Auto handshake tests on virtual targets; scope doc co-authored with HATCI; works with auto-scaled targets; fidelity validated vs physical HW; upstream Apache 2.0 | 0 children |

### RHAS-1226 (GA)

| Epic | Key | Status | Acceptance Criteria | Children |
|------|-----|--------|---------------------|----------|
| Ask the Platform | PITCREW-293 | New | Natural language questions with underlying query shown; answers grounded in telemetry data; works from any trace/session/build/lease/device/test ID; structured JSON output; read-only; works without internet connectivity | 1 child |

---

## 4. Feature Grouping by Parent

| Feature | Key | Epics (by release) |
|---------|-----|-------------------|
| **Agentic Platform** | PITCREW-290 | End-to-End Trace (0526), Autonomous Reactions (0726), Seconds-per-Iteration (0826), Unified Developer Session (1026), Ask the Platform (1226). Unscheduled: Platform Web Console, Cross-Vertical Identity, Ship with Evidence |
| **Product Readiness** | PITCREW-333 | Konflux Onboarding (0626), RH-SDLC Compliance (0726), Distribution (0926 TP), QE Readiness (1026), Product Documentation (1026). Unscheduled: Python Distribution |
| **Platform Reliability** | PITCREW-328 | Recovery Time (0526), Recovery Point (0526), Lab Infrastructure (0726), External Dependency Resilience (0926 TP) |
| **Customer - HATCI** | PITCREW-297 | Android Virtual Target (0626), Virtual Target Orchestration (0826), Virtual Interface Simulation (1126) |
| **Customer - Internal** | PITCREW-340 | CTC (0726), ATC (1126) |

---

## 5. Spec/BDD/TDD Testing Framework

### Approach

Each epic's acceptance criteria maps to a **Specification** (Spec). Each spec decomposes into **BDD scenarios** (Given/When/Then). Each scenario drives **TDD test cases** (unit + integration).

### Priority Order for Test Development

Based on release timeline and dependency chain:

#### P0 - Must have for Tech Preview (Sep 29, 2026)

These are the non-waivable release criteria from the existing release criteria document that don't yet have tests:

| Release Criterion | Maps to Epic(s) | Spec |
|-------------------|-----------------|------|
| TP-01: Full workflow E2E | PITCREW-335 + PITCREW-291 | Code commit -> build -> deploy -> test-on-board completes in single pipeline |
| TP-02: Multi-component integration | PITCREW-335 + PITCREW-298 | Builder + Jumpstarter + GitOps deploy and function together |
| TP-03: No critical/high CVEs | PITCREW-334 | Zero critical/high CVEs in shipped container images |
| M-08: No P1/P2 regressions | All | Zero P1/P2 bugs introduced since previous release |

#### P1 - Critical for Tech Preview (waivable but high impact)

| Release Criterion | Maps to Epic(s) | Spec |
|-------------------|-----------------|------|
| M-07: Builder-to-Jumpstarter handoff | PITCREW-335 | OCI artifact from Builder consumed by Jumpstarter, board provisioned |
| TP-05: DS CI pipeline operational | PITCREW-337 | Ephemeral IPI SNO provisions and runs test suite |
| TP-07: Operator upgrade | PITCREW-196 (evolution) | Upgrade from previous to current version without downtime |
| Distribution (TP epic) | PITCREW-336 | All artifacts via official channels |
| External Dependency Resilience (TP epic) | PITCREW-329 | Graceful degradation under external failures |

#### P2 - GA additions (Dec 22, 2026)

| Release Criterion | Maps to Epic(s) | Spec |
|-------------------|-----------------|------|
| GA-01: Concurrent builds | PITCREW-299 (related) | >= 5 simultaneous OCI builds |
| GA-02: Multi-board HiL | PITCREW-330 | >= 4 boards simultaneously |
| GA-03: 7-day soak test | All platform | No crashes/leaks over 7 days |
| GA-04: Security audit | PITCREW-334 | Independent review, all critical findings resolved |
| GA-05: Keycloak SSO | PITCREW-292 | Login -> token -> API across all components |
| GA-06: CDN distribution | PITCREW-336 | Product via configured channels |
| GA-07: RH-SDLC compliance | PITCREW-334 | All evidence artifacts per process |
| GA-08: Customer scenario | PITCREW-331/332 | >= 1 E2E customer use case validated |

### BDD Scenario Templates (Spec -> Scenarios)

#### Example: Distribution (PITCREW-336 / TP epic)

```gherkin
Feature: RHAS Distribution via Official Channels
  As a customer
  I want to install RHAS through standard Red Hat tooling
  So that I get supported, signed, updateable software

  Scenario: CLI install via DNF on RHEL
    Given a RHEL 9.x system with active subscription
    When I run "dnf install jumpstarter-cli"
    Then the package installs successfully
    And the binary is signed with Red Hat's GPG key
    And "jmp version" returns the current release version

  Scenario: CLI install via DNF on CentOS Stream
    Given a CentOS Stream 9 system
    When I run "dnf install jumpstarter-cli"
    Then the package installs successfully

  Scenario: CLI install via DNF on Fedora
    Given a Fedora 40+ system
    When I run "dnf install jumpstarter-cli"
    Then the package installs successfully

  Scenario: Upgrade from previous release
    Given RHAS RHAS-0826 is installed
    When a new monthly release RHAS-0926 is available
    And I run "dnf update jumpstarter-cli"
    Then the package upgrades without errors
    And existing configuration is preserved

  Scenario: No unsupported distribution methods required
    Given I am a production RHAS user
    Then all RHAS components are available through Red Hat channels
    And no component requires pip, GitHub releases, or upstream registries
```

#### Example: External Dependency Resilience (PITCREW-329 / TP epic)

```gherkin
Feature: Graceful Degradation Under External Failures
  As a platform operator
  I want RHAS to continue functioning when external services fail
  So that my pipelines don't stop for reasons outside my control

  Scenario: Container registry unavailable
    Given RHAS is running normally
    When the container registry becomes unreachable
    Then builds that don't need registry access continue working
    And builds that need registry access fail with a clear message
      identifying the external dependency
    And the error does not say "internal error" or "unknown failure"

  Scenario: DNS failure
    Given RHAS is running normally
    When the DNS server is unreachable
    Then Jumpstarter exporters maintain existing connections
    And new lease requests queue with a clear error message
    And monitoring alerts fire within 5 minutes

  Scenario: Authentication provider outage
    Given users are authenticated with active sessions
    When the auth provider goes down
    Then existing sessions continue working
    And new login attempts fail with "authentication service unavailable"
    And no data corruption occurs
```

#### Example: CTC Adoption (PITCREW-331 / current)

```gherkin
Feature: CTC Validation Pipeline Accuracy
  As a CTC engineer
  I want accurate test results from RHAS
  So I can make ship/no-ship decisions without cross-referencing

  Scenario: Test failure correctly reflected in summary
    Given a CTC validation pipeline runs on RHAS
    When a test case fails
    Then the subresult bar shows the failure in red
    And the summary count includes the failure
    And the results-junit.xml contains the failure

  Scenario: Skipped tests reflected in summary
    Given a CTC validation pipeline runs on RHAS
    When a test case is skipped
    Then the subresult bar shows the skip indicator
    And the summary separately counts skipped vs passed vs failed

  Scenario: Pipeline logs have timestamps
    Given a CTC validation pipeline runs on RHAS
    When the pipeline completes
    Then every log line includes a timestamp
    And logs include the Jumpstarter version
    And no non-printable characters appear in console output

  Scenario: AVC check failures roll up correctly
    Given a CTC validation pipeline with AVC checks
    When an AVC check fails
    Then the AVC failure rolls up to the main test case result
    And the overall pipeline result reflects the AVC failure
```

#### Example: Full Workflow E2E (TP-01 / non-waivable)

```gherkin
Feature: End-to-End Build-Deploy-Test Pipeline
  As a developer
  I want to go from code commit to test results in one pipeline
  So that I get fast feedback on my changes

  Scenario: Happy path - commit to test results
    Given a git repository with a valid Containerfile
    And a Jumpstarter-managed target board is available
    When I push a commit to the repository
    Then an OCI image build is triggered automatically
    And the built image is deployed to the target board
    And the smoke test suite runs against the deployed image
    And I receive a pass/fail result with a trace ID

  Scenario: Build failure stops pipeline
    Given a git repository with an invalid Containerfile
    When I push a commit
    Then the build fails with a clear error message
    And no deployment is attempted
    And the trace captures the build failure

  Scenario: Board unavailable - graceful queueing
    Given all target boards are in use
    When I push a commit and the build succeeds
    Then the deployment request is queued
    And I receive a notification that the deployment is waiting
    And when a board becomes available, deployment proceeds
```

### TDD Test Structure

```
tests/
  unit/
    builder/
      test_oci_build.py          # M-01, M-02
      test_bootc_build.py        # M-03
      test_concurrent_builds.py  # GA-01
    jumpstarter/
      test_exporter_health.py    # M-04
      test_lease_cycle.py        # M-05
      test_virtual_target.py     # PITCREW-298, 299
    trace/
      test_trace_correlation.py  # PITCREW-291
      test_structured_output.py  # PITCREW-291
    distribution/
      test_package_signing.py    # PITCREW-336
  integration/
    test_builder_jumpstarter_handoff.py  # M-07
    test_e2e_pipeline.py                 # TP-01
    test_multi_component.py              # TP-02
    test_operator_upgrade.py             # TP-07
    test_sso_flow.py                     # GA-05
  resilience/
    test_registry_failure.py        # PITCREW-329
    test_dns_failure.py             # PITCREW-329
    test_auth_provider_failure.py   # PITCREW-329
  scale/
    test_concurrent_builds.py    # GA-01
    test_multi_board_hil.py      # GA-02
    test_soak_7day.py            # GA-03
    test_virtual_scaling.py      # PITCREW-299
  security/
    test_cve_scan.py             # TP-03
    test_signed_provenance.py    # PITCREW-335
  customer/
    test_ctc_pipeline.py         # PITCREW-331
    test_atc_image_build.py      # PITCREW-332
    test_hatci_virtual_target.py # PITCREW-298
```

---

## 6. Gaps and Risks

### Epics with zero children (no breakdown = no testable stories)
- PITCREW-294: Autonomous Platform Reactions (due Jul 28 - 6 days)
- PITCREW-295: Seconds-per-Iteration (due Aug)
- PITCREW-300: Virtual Interface Simulation (due Nov)
- PITCREW-332: ATC Adoption (due Nov)
- PITCREW-338: Product Documentation (due Oct)

### Incomplete shipped work
- PITCREW-291 (End-to-End Trace): Marked 0526 but 10/19 children still New (telemetry correlation stories)
- PITCREW-335 (Konflux Onboarding): 4/6 children still open
- PITCREW-222/223 (Recovery objectives): Still "In Progress" despite 0526 target

### Missing from release criteria but present in epics
- Virtual target scaling validation (PITCREW-299) - no release criterion maps to it
- Autonomous platform reactions (PITCREW-294) - no release criterion
- Seconds-per-iteration developer velocity (PITCREW-295) - no release criterion
- Air-gapped operation (mentioned in 3 epics) - no release criterion
- HATCI customer validation (PITCREW-297 children) - GA-08 is generic

### Existing release criteria without epic mapping
- TP-06 (Build time baseline) - measurement, not a feature
- GA-03 (7-day soak test) - cross-cutting, not one epic
- These are valid release criteria that need test infrastructure but don't map to feature delivery

---

## 7. Recommended Next Steps

1. **Update release criteria document** to include feature-specific criteria derived from epic ACs (especially Distribution, External Dependency Resilience, Virtual Target Orchestration, Unified Developer Session)
2. **Break down zero-children epics** - PITCREW-294 is due in 6 days with nothing to test
3. **Create BDD feature files** starting with P0 non-waivable criteria (TP-01, TP-02, TP-03)
4. **Reconcile shipped-but-incomplete work** - decide if 0526 epics are actually done or need retagging
5. **Add air-gapped testing criterion** - 3 epics require it, no release gate covers it
6. **Add virtual target criteria** - HATCI work (PITCREW-297 children) has specific AC but no release criteria
