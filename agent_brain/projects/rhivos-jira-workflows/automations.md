---
last_accessed: 2026-07-15
access_count: 1
created: 2026-07-15
---

# RHIVOS Jira Automations and Special Processes

## RHEL Mirroring (VROOM in RHEL)

### Bugs from RHEL

- **Automation:** Runs daily
- Checks for newly created Bugs in RHEL with a component in the FuSa Safety Scope
- New Bugs are **cloned into VROOM** as Bugs and linked to the original RHEL Bug
- Triage team determines next steps for the VROOM issue
- **Fields set:**
  - Functional Safety Triage: **Needs Triage**
  - Priority: inherited from linked RHEL issue
  - Security Level: inherited from linked RHEL issue
  - Severity: cleared for RHIVOS team to set
- **Patch Instructions field** populated with:
  - Components, Affects Version, FixVersion, Severity, Release Blocker, Labels
  (all from the linked RHEL issue)

### Weaknesses from RHEL

- **Automation:** Runs daily
- Checks for newly created Weaknesses in RHEL with a component in the FuSa
  Safety Scope
- Cloned into VROOM as Weaknesses, linked to original RHEL Weakness
- Triage team determines next steps

### Stories from RHEL

- TBD: Manual process for cloning (discussion in progress as of wiki snapshot)

### Vulnerabilities (CVEs) from RHEL

- **ProdSec Tooling** creates RHIVOS CVEs based on Core Safety Components
- Petr has a local script running every 6 hours that links RHEL CVEs to RHIVOS
  CVEs based on CVE ID, component, and Version (planned to move to GitLab repo
  for Workato)
- **Fields updated:**
  - Once daily: updates Patch Instructions with same fields as Bugs (for all
    open vulnerabilities where exactly one RHEL ticket is known)
  - When a Vulnerability is created with **kernel-automotive** component:
    Functional Safety Triage set to **Needs Triage**

## VROOM to RHEL Automation

When a VROOM product ticket needs to be fixed in RHEL:

### "Click here to create the issue in RHEL" (Jira Bot)

- Triggered when certain components are set (e.g., RHEL Kernel, RHEL Userspace Package)
- Automation adds a comment by RHEL Jira Bot with a link
- Clicking the link opens a pre-populated create screen in the RHEL project
- Only **Component/s** and **Target Version** need manual editing
- Automation sets: description, blocking relationship, assignee details

### "Manual Trigger" Automation

- Used for kernel-automotive and kernel/automotive components
- User manually triggers the automation from the ticket
- Creates a RHEL Bug with same Component, Priority, Description, Security
  level, Target Start/End Dates, linked to VROOM ticket
- Component auto-assignment handles RHEL ticket assignment

## Component Auto-Assignment

- Jira automation that automatically assigns tickets to correct contacts and
  teams based on the component selected
- Works for both VROOM and RHEL tickets created via automation

## Blocker and Exception Process

- RHIVOS blocker process is triggered when product work is identified as
  release-blocking
- For RHEL userspace issues: RHEL Blocker process can be triggered
- Safety-critical compose failures can propose blocking of RHEL fix release

## ScriptRunner Behaviours

- When creating a Bug or Story in VROOM, Jira requires a **package component**
  to be selected
- Valid selections: RHEL Userspace Package component or RHEL Kernel components
- Enforced via ScriptRunner Behaviour

## Split-Task Automation

- Optional automation available in Planning status
- Used to decompose large Bug/Story into smaller chunks of work for sprints
