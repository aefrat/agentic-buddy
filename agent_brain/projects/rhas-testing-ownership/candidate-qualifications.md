---
last_accessed: 2026-06-29
access_count: 1
created: 2026-06-29
---

# RHAS Testing Ownership - Candidate Qualifications

## Must Have

1. **Kubernetes / OpenShift experience** - RHAS is built entirely on OCP.
   Operators, pods, namespaces, RBAC, multi-arch scheduling (x86/arm64),
   Tekton pipelines are daily work.

2. **Linux systems (RHEL/Fedora)** - The target OS is RHIVOS (RHEL-based).
   Needs comfort with RPM packaging, bootc, systemd, kernel modules, and
   RHEL tooling (Brew, Errata Tool).

3. **CI/CD pipeline experience** - Konflux, Tekton, or equivalent. Must
   understand pipeline-as-code, artifact signing, and automated gating.

4. **Test automation** - Python/pytest at minimum, plus shell scripting.
   Jumpstarter's test harness is pytest-based. Must be able to write and
   maintain automated test suites, not just run them.

5. **Container technologies** - OCI images, bootc, Podman/Docker, container
   registries. Builder produces container artifacts - the tester needs to
   validate them end-to-end.

6. **Git-based workflows** - GitLab and GitHub. RHAS integrates with both
   forges - CI workflows, IDE plugins, GitOps flows all need testing.

## Nice to Have

1. **Embedded / automotive testing** - Experience testing embedded systems,
   real-time constraints, or automotive-grade software. Understanding of
   hardware bring-up, firmware flashing, and board support packages.

2. **Hardware-in-the-loop (HIL)** - Familiarity with physical board testing,
   serial consoles, fastboot, DUT management. Jumpstarter is the core HIL
   platform; prior HIL experience shortens ramp-up significantly.

3. **Automotive standards** - ISO 21434 (cybersecurity), ASIL/FuSa
   (functional safety), AUTOSAR, ASPICE. Not deep certification expertise,
   but enough to understand compliance requirements and test against them.

4. **Performance testing** - Boot time measurement, build cycle benchmarks,
   scalability testing. The "Seconds-per-Iteration" epic (PITCREW-295) is
   explicitly a performance target.

5. **Security testing** - Software supply chain security, CVE management,
   penetration testing basics. RHAS has explicit security audit requirements
   before GA.

6. **Cloud infrastructure (AWS / ROSA)** - The platform runs on ROSA.
   Understanding cloud-native ops, cluster upgrades, and PVC/storage
   management helps with integration testing.

7. **Red Hat product testing experience** - Errata Tool, Brew, CTC/gating
   processes, Bugzilla/Jira workflows. Reduces onboarding time for the
   RH-specific release process.

8. **Rust or C/C++** - Builder produces Safe Rust and C/C++ binaries.
   Ability to read and debug compiled artifacts is valuable.

9. **Observability tooling** - OpenTelemetry, Prometheus, Grafana. Q3
   roadmap includes monitoring/alerting features.

10. **Virtual target experience** - QEMU, Android emulators, simulation
    frameworks. Multiple epics involve virtual target orchestration.

## Profile Summary

The ideal candidate is a **senior QE / SDET** with strong Kubernetes and Linux
systems background, who can work across the full stack - from physical boards
through OCP operators to CI/CD pipelines. Automotive domain knowledge is a
differentiator but not a prerequisite; the platform abstracts much of the
domain-specific complexity. The role is heavily integration-focused: the product
is a suite of components that must work together, not a single application.

Given the RHAS timeline (Tech Preview Sep 2026, GA Dec 2026), the candidate
needs to ramp up fast. Prior Red Hat product testing experience would be the
strongest accelerator.
