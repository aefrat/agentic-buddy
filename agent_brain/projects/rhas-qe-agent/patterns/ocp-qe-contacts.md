---
last_accessed: 2026-07-02
access_count: 0
created: 2026-07-02
---

# OpenShift QE Contacts for RHAS Alignment

Contacts identified from Jira epics, Slack channels, and Google Docs. These are OCP QE leads whose work is relevant to RHAS test strategy alignment.

## Primary contacts

| Name | Role / Area | Jira | Channel | Why relevant to RHAS |
|------|-------------|------|---------|---------------------|
| Cameron Meadors | OCP Quality Strategy owner | OCPQE-32074 | #forum-openshift-qe | Owns the overall OCP quality strategy doc. Best starting point for understanding OCP QE philosophy and adapting it to RHAS. |
| John George | Next-gen QE, test modernization | OCPQE-32073 | #wg-openshift-next-gen-quality | Leading effort to deprecate legacy QE jobs and modernize test infrastructure. Relevant for avoiding legacy patterns when building RHAS QE from scratch. |
| David Kutalek | Test Case Management | OCPQE-32075 | #forum-openshift-qe | Leading migration from Polarion to Jira/Confluence for test case management. RHAS should align with whatever OCP standardizes on. |
| Ken Zhang | Test suite levels | OCPQE-32067 | #forum-ocp-testplatform | Introducing active/stable test suite classification. Relevant model for RHAS test organization. |
| Devan Goodwin | QE strategy direction | OCPSTRAT-3352 (reporter) | | Strategic initiative reporter for "Revamp Quality Engineering". Useful for understanding where OCP QE is heading long-term. |

## Secondary contacts (discovered from Slack/Docs)

| Name | Context | Source |
|------|---------|--------|
| Almen Ng | Console-harness QE Autonomous Pipeline (ACM-36044) - 11-stage agentic test pipeline | Slack #forum-fullsend-ai |
| Roni Eliezer | Test Console AI analysis (Gemini-powered) | Internal references |

## Recommended outreach order

1. Cameron Meadors - Start here. His quality strategy doc is the most comprehensive OCP QE reference. Request a brief alignment call to discuss RHAS adoption of OCP patterns.
2. John George - Next-gen QE working group. Ask about joining #wg-openshift-next-gen-quality as an observer to stay aligned with OCP QE evolution.
3. David Kutalek - Test case management. Align RHAS test tracking with whatever OCP standardizes on (Jira/Confluence vs Polarion).
4. Almen Ng - Agentic testing. His Console-harness pipeline is the most advanced internal AI testing implementation. Could inform RHAS's agentic testing strategy.

## Notes

- OCPSTRAT-3352 ("Revamp Quality Engineering") is blocked by OCPQE-32074 (Define Quality Strategy). Both are active as of Jul 2026.
- OCP QE is moving away from Polarion toward Jira/Confluence for test case management (PLMORG-249, led by Suyun).
- The #wg-openshift-next-gen-quality channel is the best single source for OCP QE direction.
