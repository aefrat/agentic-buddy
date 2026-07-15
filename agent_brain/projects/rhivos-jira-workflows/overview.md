---
last_accessed: 2026-07-15
access_count: 1
created: 2026-07-15
---

# RHIVOS in Jira - Overview

## What is Jira used for in RHIVOS?

Jira is the bug and task tracking application used across Red Hat for agile
project management. RHIVOS uses it to plan, track, execute, and report on
product releases, including bug resolution, new feature development, and
operational activities.

## Jira Projects

RHIVOS uses **two** Jira projects:

### AUTOBU (BU-level)

- Purpose: BU-level work that decides program direction and milestones.
- Contains: Outcomes, Features, Initiatives
- Permission: Limited to key program stakeholders:
  - Product Management
  - Program Management
  - The three main Product Owners (POs)
  - Business Unit (BU) ecosystem representatives
- Access managed through Rover group: **rhivos-autobu-authors**

### VROOM (Team-level)

- Purpose: The daily driver for feature team tasking.
- Contains: Epics, Stories, Bugs, Tasks, Weaknesses, Vulnerabilities
- All product and non-product work is tracked here.

The relationship between issues in these projects is described in
[hierarchy.md](hierarchy.md).

## Definitions

**Product work**: Any code change that will land in an RPM packaged in the
RHIVOS bits delivered to a customer.

**Non-product work**: Any process or supporting work required to deliver
RHIVOS to a customer.

## Workflow Summary

| Work Type | Issue Types | Workflow | Statuses | Complete by |
|---|---|---|---|---|
| Product | Bug, Story, Weakness, Vulnerability | PRODUCT workflow | New -> Planning -> In Progress -> Integration -> Release Pending -> Closed | Dev Complete |
| Non-Product | Task | TASK workflow | New -> In Progress -> Review -> Closed | Release Complete |
| Strategic | Feature, Initiative | Feature/Initiative workflow | New -> Backlog -> Refinement -> In Progress -> Closed | N/A (can span releases) |
