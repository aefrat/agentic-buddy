---
last_accessed: 2026-09-09
access_count: 5
created: 2026-06-29
---

# RHAS Testing Ownership - Project

Origin: PDR Staff Meeting discussion topic (Jun 29, 2026).
Source doc: https://docs.google.com/document/d/1WvfY8ktEsn5hUb0ji7M9_hAqz1kdjvT8MVtULtuTwIU/edit?tab=t.0

## Context

RHAS (Red Hat Automotive Suite) is approaching Tech Preview (Sep 2026) and GA
(Dec 2026). Testing ownership needs to be established. The product is a Tier 2
integrated platform: OCP + Builder Operator + Jumpstarter + Pipelines + GitOps +
Keycloak, targeting platform engineers at automotive OEMs.

## Files

- `features-requiring-testing.md` - RHAS features/epics mapped to testing domains
- `candidate-qualifications.md` - Must-have and nice-to-have qualifications for testing candidates
- `testing-landscape-report.md` - Current state of RHAS testing: upstream, downstream, HiL, CTC, QE readiness, infrastructure, risks, recommendations

## Status

Phase: Landscape assessment complete (Jun 30, 2026). Refreshed Jul 21, 2026.
Key finding: DS pipeline DNS approach architecturally invalid for OCP (Jul 13).
PITCREW-337 (QE Readiness) still unassigned after 3+ months. PITCREW-403 (flaky E2E) closed.

## Recent activity

- **2026-07-28 (Slack):** RHAS testing meeting rescheduled to Aug 3rd (RH company meeting + PitCrew scrum conflicts). Evgeni noted he will be on vacation by then.
