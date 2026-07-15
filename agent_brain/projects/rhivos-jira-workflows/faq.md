---
last_accessed: 2026-07-15
access_count: 1
created: 2026-07-15
---

# RHIVOS Jira Workflows - FAQ

## General

### What is the difference between AUTOBU and VROOM?

AUTOBU is the BU-level project for strategic direction (Outcomes, Features,
Initiatives). Access is restricted to POs, PM, PgM, and BU representatives.
VROOM is the team-level project where daily work happens (Epics, Stories, Bugs,
Tasks, CVEs).

### What is the difference between a Feature and an Initiative?

Both are in AUTOBU and link to Outcomes. **Feature** = product work (code
changes delivering business value). **Initiative** = non-product work
(infrastructure, process, tooling). Features have Stories/Bugs underneath;
Initiatives have Tasks.

### What is the difference between product and non-product work?

**Product work** = any code change landing in an RPM packaged in RHIVOS bits
delivered to a customer. **Non-product work** = any process or supporting work
required to deliver RHIVOS.

## Workflows

### What workflow does my issue use?

- Bug, Story, Weakness, Vulnerability -> **PRODUCT** workflow (New -> Planning
  -> In Progress -> Integration -> Release Pending -> Closed)
- Task -> **TASK** workflow (New -> In Progress -> Review -> Closed)
- Feature, Initiative -> **Feature/Initiative** workflow (New -> Backlog ->
  Refinement -> In Progress -> Closed)

### When should I use a Story vs a Bug vs a Task?

- **Story**: New product functionality or feature enhancement (RFE)
- **Bug**: Product defect
- **Task**: Non-product work (process, infrastructure, documentation, spikes, etc.)
- **Weakness/Vulnerability**: Created and managed by ProdSec

### Can a Task link to a Feature Epic?

Yes. Tasks may link to Epics under either Initiatives or Features. Stories and
Bugs should only link to Epics under Features.

### What statuses can transition to any other status?

In the Feature/Initiative workflow, statuses can transition to any state (global
transitions). The Product and Task workflows have more constrained transitions.

## Fields and Requirements

### What fields are required to move a Bug to In Progress?

**Severity** field is required if the Regression field is set to Yes.

### What fields are required to move to Release Pending?

**Test Coverage** field and **Severity** field (if not already set).

### What is Preliminary Testing?

A gate in the Product workflow. After development, the maintainer marks
"Preliminary Testing: Requested" and "Testable Builds". QE runs tests and marks
PASS or FAIL. Maintainer only merges on PASS.

### What is FuSa Triage?

Functional Safety Triage is a parallel process for product issues. It sets the
"Functional Safety Triage" field and Fix Version. It can happen at any time
during the product workflow.

### When is Regression set to Yes?

When an existing test that previously passed now fails. The Regression field is
required for Bug type issues.

### What is TestCoverage and when do I set it?

TestCoverage indicates QE's testing approach:
- **None**: Set at Feature creation (Features only)
- **RegressionOnly**: QE plans to run existing test coverage
- **New Test Coverage**: A new test case was developed
Required to transition to Release Pending.

### What are TestLink and Test Plan?

- **TestLink**: Links to test cases (scripts in git repo) for coverage evidence.
  Required for "New Test Coverage" on bugs, vulnerabilities, weaknesses.
- **Test Plan**: Links to test specification for stories. Optional.

## Components and Kernel

### What component should I use for a kernel issue?

See the kernel component decision tree:
- Affecting Kconfig -> **kernel-automotive**
- Shared codebase, built in RHEL -> **RHEL kernel**
- Shared codebase, not built in RHEL -> **kernel/automotive**
- RHIVOS-only patch -> **kernel-automotive**

### What is "Component Awaiting Approval"?

A placeholder component for packages being worked on before formal RHIVOS
Council approval. Once approved, update to the correct package component.

### What is the components repo?

The Source of Truth for Package Components in RHIVOS. Defines which packages
exist and their approved status.

## RHEL Integration

### How does a VROOM ticket get linked to RHEL?

Two mechanisms:
1. **Jira Bot link**: When RHEL Kernel or RHEL Userspace Package component is
   set, automation adds a comment with "Click here to create the issue in RHEL".
2. **Manual Trigger**: For kernel-automotive and kernel/automotive components,
   user triggers automation manually to create a linked RHEL Bug.

### How do RHEL issues appear in VROOM?

- **Bugs/Weaknesses**: Daily automation clones new RHEL issues with FuSa Safety
  Scope components into VROOM
- **Vulnerabilities**: ProdSec tooling creates RHIVOS CVEs; Petr's script links
  them to RHEL CVEs every 6 hours
- **Stories**: Manual process (TBD)

### What happens when a RHEL ticket reaches Integration?

Work transitions back to the VROOM ticket for final testing in RHIVOS.

## Milestones

### When must product work be done?

By the **Dev Complete** milestone for the given release.

### When must non-product work be done?

By the **Release Complete** milestone (unless an earlier internal deadline is set).

### How do I track progress against milestones?

- Product work: Auto-All - Stories/Bugs board (Version Report)
- All work: Auto-All - no Epics board (Version Report)
- POs may create custom filters/boards for their functional area.

## Process

### How do I report a bug against RHIVOS?

Always log a ticket in the **VROOM** project. Triage team will review and
determine whether the fix should be in RHIVOS or RHEL. The VROOM ticket
continues to exist regardless.

### How do I handle a functional test failure?

Create a Task in VROOM. If the failure is caused by a product bug, open a
separate Bug in VROOM linked with "causes" relationship, and close the Task as
Done. If it is a test issue, fix it using the Task workflow.

### How do I handle a validator failure?

Create under AUTOBU-719 with summary prefix "Validator Failure". Assigned to
rhivos-ft-fusa-foa. Follow the Validator Failure Triage Process.

### What prefix should I use for spikes?

Prefix the Task Summary with **"[SPIKE]"**.

### Who has access to create issues in AUTOBU?

Members of the **rhivos-autobu-authors** Rover group: Product Management,
Program Management, the three main POs, and BU ecosystem representatives.
