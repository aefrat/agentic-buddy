---
last_accessed: 2026-07-15
access_count: 1
created: 2026-07-15
---

# Product Workflow (Story/Bug/CVE/Weakness/Vulnerability)

Used for product work in the VROOM project. Based on DevTestDoc (RHEL in Jira
Workflow). Applies to Stories, Bugs, Weaknesses, and Vulnerabilities.

Issues must:
- Link to Epics under Features
- Link to a completed Git Pull Request if Closed as Done
- Be completed by **Dev Complete** milestone

## States and Transitions

### NEW

**Entry criteria:**
- Create ticket in **VROOM** project
- Use **Bug** type for defects and **Story** type for new functionality/RFEs
  - Regression field is required for Bug type. An existing test that fails
    should always set Regression to "Yes"
- Enter **Summary**, **Component/Package**, **Description**, **Assigned Team**
- Set **Affects Version(s)**, **Target Version**, **TestCoverage** is unset

**Side process:** FuSa Triage is a parallel process that can take place at any
time. FuSa Triaged = Set **Functional Safety Triage**, set **Fix Version**.

**Transition to Planning:**
- **Severity** field (Bugs only) is required to transition to In Progress if
  Regression field is Yes.

### Planning

**What happens here:**
- Set **Docs Impact**, **Assignee/QA Contact**, **Fix Version**, and
  **Severity** (Bugs only)
- Set appropriate **Epic Link** (optional for Bugs/Vulnerabilities/Weaknesses)
- Set estimated **Story Points**
- (OPTIONAL) **Split-Task Automation** may be used to decompose large Bug/Story
  to smaller chunks of work for sprints

**Transition to In Progress:**
- **Severity** field (Bugs only) is required to transition to In Progress if
  not previously set.

### In Progress (first phase - development)

**Decision: Fix in RHEL?**
- **YES** -> Use Automation as described in [issue-type-mapping.md](issue-type-mapping.md)
  to create appropriately linked RHEL ticket. Work is done on RHEL ticket
  created using automation. Follows the RHEL in Jira Workflow. When RHEL ticket
  is marked Integration, work transitions back to VROOM ticket for final
  testing in RHIVOS.
- **NO** -> Continue on VROOM ticket.

**What happens here (when work stays on VROOM):**
- Dev work on VROOM ticket and link Jira ticket to MR / Patch
- Maintainer marks **Preliminary Testing: Requested** and **Testable Builds**
  once finished MR review CI tests are passing
- Test is implemented and employed in CI/gating and downstream testing
- QE runs **Preliminary Testing** and sets the field to **PASS**; if it
  **FAILS**, the field gets set to **FAIL**

**Transition:** Preliminary Testing: Pass -> Maintainer picks up tickets with
Preliminary Testing: PASS and merges changes.

**If Test Failed (FailedQA):** Returns to In Progress for rework.

### In Progress (second phase - post-merge)

**What happens here:**
- If needed, set **Release Note Text**, **Release Note Type**, and
  **Release Note Status** fields
- **Fixed in Build** should be set
- When the ticket is included in an erratum, link to it in the **Errata Link** field

### Integration

**What happens here:**
- QE will run final regression and functional testing.
- OtherQA process should be completed by this point.
- QE makes sure that the Required **TestCoverage** field is set:
  - **RegressionOnly**: QE plans to run existing test coverage
  - **New Test Coverage**: A new test case was developed
- QE makes sure that the **TestLink** or **Test Plan** fields are set:
  - **Test Link**: Jira field to link one or more test cases (test script in
    git repo) for test coverage evidence for issues of type bug, vulnerability,
    or weakness. Required for "New Test Coverage".
  - **Test Plan**: Jira field to link the test specification for test coverage
    evidence for issues of type story. This field is optional.
- QE moves the ticket to **Release Pending** once satisfied with final
  verification results.

### Release Pending

**Entry requirements:**
- **Test Coverage** field is required to transition to Release Pending.
- **Severity** field will be required to transition to Release Pending if it
  has not yet been set.

**What happens here:**
- Docs team reviews **Release Notes Text** and creates Release Notes.
- PgM action: When the changes are shipped and available to customers, mark the
  **Fix Version** as *Released*.
- Once a release goes live, all issues should be **Closed** with **Resolution:
  Done-Errata**.

### Closed

**Requirements:**
- If choosing to Close as **Done**, a **Git Pull Request** must be attached.
- Otherwise, close as **Won't Do**, **Can't Reproduce**, **Duplicate**, etc.
  and provide an explanation as to why.

## Preliminary Testing Process

This is a key gate in the product workflow:

1. Developer finishes MR, CI tests pass
2. Developer sets **Preliminary Testing: Requested** and marks **Testable Builds**
3. QE runs preliminary testing
4. QE sets **Preliminary Testing: PASS** or **FAIL**
5. If PASS: Maintainer merges
6. If FAIL: Returns to developer for rework (FailedQA)

## FuSa (Functional Safety) Triage

- Parallel process that can take place at any time
- Sets **Functional Safety Triage** field
- Sets **Fix Version**
- Applies to all product issue types
