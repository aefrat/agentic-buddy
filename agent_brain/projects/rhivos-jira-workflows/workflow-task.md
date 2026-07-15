---
last_accessed: 2026-07-15
access_count: 1
created: 2026-07-15
---

# Task Workflow (Non-Product Work)

Used for Tasks in the VROOM project. Tracks process or supporting work.

Tasks:
- May link to Epics under Initiatives or Features
- May continue to **Release Complete** (unless an earlier date is set based on
  internal team milestones)

## States and Transitions

### NEW

**Entry criteria:**
- Create ticket in **VROOM** project
- Use **Task** type for any non-product work
- Enter **Summary**, **Description**, and **Component** or **Assigned Team**
- Set **Target Version**

**Between NEW and In Progress (preparation):**
- **Functional Safety Triage** field gets set (Validator Failures only)
- **Description** includes clearly articulated goal and Acceptance Criteria is
  elaborated, well defined, and understood
- Set **Assignee/QA Contact**
- Task has appropriate **Epic Link** set
- Task has been estimated using **Story Points**
- Set **Docs Impact**
- Set **Fix Version**
- Priority (order of execution) set appropriately - ordered backlog

### In Progress

**What happens here:**
- **Assignee** works on ticket and links Jira ticket to completed work product
  (MR, document, etc.)
- **Assignee** moves ticket to **Review** state and tags reviewer in the
  **Contributors** field

**Transitions:**
- Forward -> **Review** (when work product is ready for review)
- Direct to **Closed** (if review is not required; see note below)

### Review

**What happens here:**
- Work product is reviewed by another team member
- Ticket moved to **Closed** with **Resolution: Done** once satisfied with
  final review/verification results

**Notes:**
- **Review** state may be skipped if generated work product or team processes
  do not require review/verification.
- If review is skipped, **Assignee** moves ticket to **Closed** with
  **Resolution: Done** once work is completed.

**Transitions:**
- Forward -> **Closed** (review passed)
- Backward -> **In Progress** (Review/Test Failed - rework needed)

### Closed

**Resolutions available:**
- **Done** - work completed successfully
- **Won't Do** - determined no work is required
- **Can't Do** - unable to complete
- **Obsolete** - no longer relevant
- **Duplicate** - duplicate of another ticket

**Note:** In cases where it is determined that no work is required for a Task,
the Assignee may move the ticket directly from NEW to **Closed** with one of
the non-Done resolutions listed above.
