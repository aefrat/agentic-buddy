---
last_accessed: 2026-07-15
access_count: 1
created: 2026-07-15
---

# RHIVOS Jira Components

## Package Components

The PRODUCT workflow requires a package component when creating Bugs or Stories
(enforced via ScriptRunner Behaviour).

### Component Types

| Component | Meaning | When to Use |
|---|---|---|
| RHIVOS-specific package | A package maintained by RHIVOS | Bugs/Stories for RHIVOS-maintained packages |
| RHEL Userspace Package | Package inherited from RHEL (userspace) | Issues in RHEL-inherited userspace components |
| RHEL Kernel | Kernel changes in shared RHEL codebase, built in RHEL | Issues affecting shared kernel codebase |
| kernel-automotive | RHIVOS-specific kernel package | Kconfig changes, RHIVOS-only kernel patches |
| kernel/automotive | Shared codebase changes not built in RHEL | Kernel changes specific to RHIVOS but in shared code |
| Component Awaiting Approval | Placeholder for packages not yet approved | Work on packages pending RHIVOS Council approval |
| Toolchain Requests | Non-product toolchain work | Infrastructure, image definitions, build pipeline |
| Test Enablement | Test infrastructure work | Test framework, test tooling, test environment |

### Source of Truth

The Source of Truth for Package Components in RHIVOS is the **components repo**.

### Component Awaiting Approval

Due to the Package Process, work may be done ahead of formal RHIVOS Council
approval. The "Component Awaiting Approval" component allows work to progress
while a package is in review.

**Expectations:**
- Shows up on the Data Consistency Dashboard under "Stories/Bugs With Component
  Awaiting Approval" gadget
- Once the package is formally added to RHIVOS, the proper component will be
  added to Jira
- The team is responsible for updating Jira issues with the correct package
  component

### Kernel Component Decision Tree

```
Is it a kernel issue?
  |
  +-- Affecting Kconfig? --> kernel-automotive
  |
  +-- In shared codebase?
  |     |
  |     +-- Built in RHEL? --> RHEL kernel
  |     |
  |     +-- Not built in RHEL? --> kernel/automotive
  |
  +-- RHIVOS-only patch? --> kernel-automotive
```

## Assigned Teams

| Team ID | Area |
|---|---|
| rhivos-ft-fda | RHIVOS-specific userspace packages |
| rhivos-ft-auto-kernel | Kernel work |
| rhivos-ft-base-os-automotive | Base OS automotive |
| rhivos-ft-release-management | Release engineering, RHEL userspace triage |
| rhivos-ft-fusa-foa | FoA investigations, validator failures |
| rhivos-ft-fusa-assessment | Risk assessment |
| rhivos-ft-performance-scale | Performance assessments |
| rhivos-ft-aristocats | Customer work (presentations, demos) |
| rhivos-doc-team | Documentation |
