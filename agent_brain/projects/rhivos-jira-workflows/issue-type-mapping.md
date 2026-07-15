---
last_accessed: 2026-07-15
access_count: 1
created: 2026-07-15
---

# Issue Type to Workflow Mapping

Detailed mapping of every issue category to its workflow, assigned team,
component, and special process considerations.

## Product Work

### RHIVOS-specific userspace package bugfix or feature enhancement

- **Workflow:** PRODUCT
- **Assigned Team:** rhivos-ft-fda
- **Component:** Select appropriate RHIVOS-specific userspace package
- **Process:**
  1. RHIVOS package component set
  2. RHIVOS blocker process triggered, if needed
  3. Worked on by RHIVOS team on VROOM ticket
  4. RHIVOS QE tests on VROOM ticket
  5. Fix in RHIVOS Compose
  6. Fix attached to RHIVOS Erratum
  7. Customer receives fix

### RHIVOS kernel bugfix or feature enhancement

- **Workflow:** PRODUCT
- **Assigned Team:** rhivos-ft-auto-kernel

Four sub-scenarios depending on what is affected:

#### Affecting Kconfig

- **Component:** kernel-automotive
- **Process:**
  1. Worked on by RHIVOS team on VROOM ticket
  2. Once solution available: 'kernel-automotive' component set
  3. Automation adds comment to use "Manual Trigger" automation
  4. Manual trigger creates a RHEL Bug with same Component, Priority,
     Description, Security level, Target Start/End Dates, linked to VROOM ticket
  5. Component auto-assignment assigns RHEL ticket to correct contacts
  6. RHEL QE tests on RHEL ticket
  7. RHEL Compose
  8. If compose has safety critical fixes and does not pass: proposed block of
     RHEL fix release
  9. Check if fix is in RHIVOS Compose
  10. Check if new package passes gating
  11. Set RHIVOS approval flag in Errata tool
  12. Attach fix to RHIVOS Erratum -> Customer receives fix
  13. Attach fix to RHEL erratum -> Release using RHEL processes (KWF, Errata,
      OSCI, etc.) -> Customer receives fix

#### Affecting the shared codebase, built in RHEL

- **Component:** RHEL kernel
- **Process:**
  1. Worked on by RHIVOS team on VROOM ticket
  2. RHIVOS kernel team determines issue is in RHEL Kernel
  3. 'RHEL Kernel' component set
  4. Automation adds comment by RHEL Jira Bot with link: "Click here to create
     the issue in RHEL"
  5. Click link to open associated issue in RHEL project - only Component/s and
     Target Version need editing in create screen
  6. Automation sets description, blocking relationship, assignee details
  7. Solution/type determines whether RHEL or RHIVOS kernel team fixes, but
     work is done on RHEL ticket with tight coordination
  8. RHIVOS completes pre-verification on "KWF Variant" tickets created by
     RHEL QE Automation
  9. RHIVOS QE tests final integration into RHIVOS on VROOM ticket
  10. RHEL QE tests, RHEL Compose
  11. Safety critical compose blocking, gating, errata process (same as above)

#### Affecting the shared codebase, not built in RHEL

- **Component:** kernel/automotive
- **Process:**
  1. RHIVOS determines issue is a RHIVOS-specific kernel change
  2. 'kernel / automotive' component set
  3. Automation adds comment to use "Manual Trigger" automation
  4. Manual trigger creates RHEL Bug with same component, linked to VROOM ticket
  5. Component auto-assignment assigns RHEL ticket
  6. RHIVOS kernel team works on issue in RHEL ticket
  7. RHIVOS completes pre-verification on "KWF Variant" tickets
  8. RHIVOS QE tests on VROOM ticket
  9. RHEL QE tests, RHEL Compose
  10. Safety critical compose blocking, gating, errata process (same as above)

#### RHIVOS-only patch

- **Component:** kernel-automotive
- **Process:**
  1. RHIVOS determines issue is a RHIVOS-specific kernel change
  2. 'kernel-automotive' component set
  3. Automation adds comment to use "Manual Trigger" automation
  4. Manual trigger creates RHEL Bug with same component, linked to VROOM ticket
  5. Component auto-assignment assigns RHEL ticket
  6. Worked on by RHIVOS team on RHEL ticket
  7. RHEL QE tests on RHEL ticket, RHEL Compose
  8. Safety critical compose blocking, gating, errata process (same as above)

### RHEL userspace package bugfix or feature enhancement

- **Workflow:** PRODUCT
- **Assigned Team:** rhivos-ft-release-management
- **Component:** RHEL Userspace Package
- **Process:**
  1. Issues with this component assigned to PDR team PO/backup for triage
  2. If determined to be a RHEL issue during triage: find comment added by RHEL
     Jira Bot with link "Click here to create the issue in RHEL"
  3. Click link - only Component/s and Target Version need editing
  4. Automation sets description, blocking relationship, assignee details
  5. If blocker for RHIVOS release: RHEL Blocker process triggered
  6. Worked on by RHEL team on RHEL ticket
  7. RHEL completes pre-verification on "Blocked by" tickets created by RHIVOS
     automation
  8. RHEL QE tests, RHEL Compose
  9. Safety critical compose blocking, gating, errata process

### Package Vulnerability report

- **Workflow:** PRODUCT
- Created and managed by ProdSec following the Vulnerability Management Workflow
- Considered product work - follows same workflow as other product work

### Package Weakness report

- **Workflow:** PRODUCT
- Created and managed by ProdSec following the Vulnerability Management Workflow
- Considered product work - follows same workflow as other product work

## Non-Product Work

### General infrastructure outage problem

- **Workflow:** TASK
- **Component:** Toolchain Requests
- Automotive Toolchain team will triage and update component

### Image definition changes

- **Workflow:** TASK
- **Component:** Toolchain Requests
- Automotive Toolchain team will triage and update component

### Build pipeline setup changes (including new package setup)

- **Workflow:** TASK
- **Component:** Toolchain Requests
- Automotive Toolchain team will triage and update component

### Various release engineering trackers

- **Workflow:** TASK
- **Assigned Team:** rhivos-ft-release-management

### Process documentation creation or updates

- **Workflow:** TASK
- **Assigned Team:** rhivos-ft-release-management

### Functional test failures

- **Workflow:** TASK
- **Assigned Team:** rhivos-ft-auto-kernel OR rhivos-ft-base-os-automotive OR rhivos-ft-fda
- **Process:**
  - Assigned Team investigates test failure
  - If caused by a product bug: open a Bug in VROOM, link with "causes"
    relationship, close test failure Task as Done
  - If test issue: fix using Task workflow

### Validator failures

- **Workflow:** TASK
- **Assigned Team:** rhivos-ft-fusa-foa
- **Naming convention:** Created under AUTOBU-719 with summary prefix
  "Validator Failure"
- Follows Validator Failure Triage Process

### Test enablement work

- **Workflow:** TASK
- **Assigned Team:** rhivos-ft-auto-kernel OR rhivos-ft-base-os-automotive OR rhivos-ft-fda
- **Component:** Test Enablement

### Spikes

- **Workflow:** TASK
- **Assigned Team:** Select team needing to do the work
- **Component:** Select based on work to be investigated
- Prefix Task Summary with **"[SPIKE]"**

### FoA investigations

- **Workflow:** TASK
- **Assigned Team:** rhivos-ft-fusa-foa

### Risk assessment investigations

- **Workflow:** TASK
- **Assigned Team:** rhivos-ft-fusa-assessment

### Performance assessments

- **Workflow:** TASK
- **Assigned Team:** rhivos-ft-performance-scale

### Customer work (presentations, demos)

- **Workflow:** TASK
- **Assigned Team:** rhivos-ft-aristocats

### Product documentation

- **Workflow:** TASK
- **Assigned Team:** rhivos-doc-team
- Work ready for review by end of CTC

### Other documentation requests

- **Workflow:** TASK
- **Assigned Team:** rhivos-doc-team
