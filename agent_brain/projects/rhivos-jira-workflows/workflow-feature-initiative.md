---
last_accessed: 2026-07-15
access_count: 1
created: 2026-07-15
---

# Feature/Initiative Workflow (AUTOBU)

Used for Features and Initiatives in the AUTOBU project. Facilitates refinement
and prioritization with the Business Unit in regular planning discussions.

Note: Statuses can transition to any state (global transitions allowed).

## States and Transitions

### NEW

**Entry criteria:**
- Create ticket in **AUTOBU** project (should be filed by POs / PM / TPM)
- Use **Feature** type for new product functionality/RFEs
- Use **Initiative** type for other non-product work (infra, process, etc.)
- Enter **Summary** and **Description**
- Goals and high-level use cases documented in Description
- (Features only) **TestCoverage** is set to **None**
- Set **BU_Meeting** label (if BU review is needed)

**Next step:** Issue is reviewed and prioritized at **RHIVOS Planning Review**.

**Decision: Accepted as work for RHIVOS?**
- **NO** -> **Backlog** (work is in scope but not committed to at the time)
- **YES** -> check MUSTHAVE or NICETOHAVE

### Backlog

- Work is in scope but not committed to at the time.
- Set **BU_Meeting** label when future prioritization is desired.
- Can transition back to evaluation when priorities change.

### Decision: MUSTHAVE or NICETOHAVE?

- **YES** -> Labeled with **MUSTHAVE** or **NICETOHAVE** as appropriate.
  Moves to **Refinement** once acked by the BU/Program.
- **NO** -> Returns to **Backlog** (MUSTHAVE or NICETOHAVE label removed).

### Refinement

**What happens here:**
- Work needed to deliver the feature/initiative is actively being discussed and scoped.
- MVP described, risks and dependencies outlined.
- Stakeholders, PO, SMEs identified and consulted.
- **Epics** decomposed, **Assignee**, **Priority**, and **Fix Version** set.
- Roadmaps updated.
- (Features only) QE makes sure the Required **TestCoverage** field is set:
  - **RegressionOnly**: QE plans to run existing test coverage
  - **New Test Coverage**: A new test case was developed

**Transitions:**
- Forward -> **In Progress** (when refinement is complete and work begins)
- Backward -> **Backlog** (work deprioritized, but still desired for RHIVOS)

### In Progress

**What happens here:**
- Work in progress to develop, test, and document the feature/initiative.
- Work progresses on underlying work items.
- Refinement of work occurs, as needed.

**Transitions:**
- Forward -> **Closed** (when all work is complete)
- Backward -> **Backlog** (work deprioritized, but still desired for RHIVOS)

### Closed

**Entry criteria:**
- Feature development work is completed.
- All work has been completed and acceptance criteria met.
- **Resolution** value set.
