---
last_accessed: 2026-07-02
access_count: 0
created: 2026-07-02
---

# OpenShift QE Reference - Patterns and Contacts for RHAS Alignment

OCP QE practices, strategy epics, contacts, and internal agentic testing initiatives relevant to RHAS QE planning.

## OCP Feature Quality Strategy

Source: Google Doc 1zuWKi9MvRVyOWn1lj-Khi47TvElUdmGWKRJhTnSVfVg

Core principle: quality is a shared responsibility of the entire feature team, not a QE-only concern.

### Four Phases

1. **Planning** - sizing, Definition of Ready, test plans
2. **Development** - parallel code + test writing, pre-merge validation, Sippy/Component Readiness monitoring
3. **Stabilization** - EC/RC/GA builds, Component Readiness dashboards
4. **Ongoing Maintenance** - z-stream releases, bug escape analysis, support feedback loops

### Testing Approach

- Pre-merge: unit + integration tests (fast, cheap)
- E2E: run in periodics only (expensive, use sparingly)
- Component Readiness and Sippy for release quality monitoring
- Test case management migrating from Polarion to Jira/Confluence (Suyun leading, PLMORG-249)

### Future Direction

- Agentic SDLC: AI-generated test plans, AI context files
- QualityFlow proposal for design-layer upstream quality

## CI Infrastructure

- **Prow** - core CI system (same as Kubernetes upstream)
- **ci-operator** - builds and tests OCP components
- **Step registry** - reusable test workflow definitions
- **Payload qualifying jobs** - blocking and informing categories
- **Release gating** - jobs attached to release-X.Y branches
- **Build pipeline** - nightly payloads -> EC -> RC -> GA

## Key OCP QE Jira Epics

| Epic | Summary | Owner |
|------|---------|-------|
| OCPQE-32074 | Define Overall Quality Strategy for OCP | Cameron Meadors (reporter: Devan Goodwin) |
| OCPQE-32075 | Test Case Management for OCP | David Kutalek |
| OCPQE-32073 | Deprecate QE jobs | John George |
| OCPQE-32067 | Introduce new test suite levels (active/stable) | Ken Zhang |
| OCPSTRAT-3352 | Revamp Quality Engineering | (blocked by OCPQE-32074) |

## QE Contacts for RHAS Alignment

| Person | Email/Handle | Role |
|--------|-------------|------|
| Cameron Meadors | cmeadors@redhat.com | OCP Quality Strategy owner |
| John George | jgeorge | Next-gen QE working group |
| David Kutalek | - | Test Case Management lead |
| Ken Zhang | - | Test suite levels lead |
| Devan Goodwin | - | OCPSTRAT reporter, QE strategy direction |

## Relevant Slack Channels

- `#forum-openshift-qe` - general OCP QE discussion
- `#forum-ocp-testplatform` - CI/test platform topics
- `#wg-openshift-next-gen-quality` - next-gen QE working group (John George)

## Red Hat Internal Agentic Testing Initiatives

### Console-harness QE Autonomous Pipeline (ACM-36044)
- Owner: Almen Ng
- 11-stage pipeline: JIRA -> BDD scenarios -> Polarion test cases -> Playwright E2E tests -> PR
- Most mature internal example of agentic test generation

### QualityFlow Proposal
- Channels: `#cnv-quality-flow-pilot`, `#forum-fullsend-ai`
- Design-layer upstream approach: requirement analysis -> test plan -> QE review -> test specs -> test code generation
- Focused on shifting quality left into design phase

### CNV vme-devops-bot
- Automated gating job results processing
- RootCoz classification for test failures
- Operational automation, not test generation

### Test Console AI Analysis
- Owner: Roni Eliezer
- Uses Gemini for AI-powered test result analysis
- Focused on result interpretation rather than test creation

## Relevance to RHAS

RHAS can align with OCP QE patterns in several areas:
- Adopt the four-phase quality strategy model
- Reuse the pre-merge vs periodic E2E split
- Track OCPQE-32074 outcomes for QE strategy alignment
- Learn from Console-harness and QualityFlow for agentic test generation
- Connect with Cameron Meadors and John George for cross-team alignment
