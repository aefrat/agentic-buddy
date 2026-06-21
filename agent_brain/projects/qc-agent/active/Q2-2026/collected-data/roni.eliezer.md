---
collected: 2026-06-21
quarter: Q2 2026
period: 2026-04-01 to 2026-06-30
member: Roni Eliezer
---

# Collected Data — Roni Eliezer — Q2 2026

## Stats

- **Jira tickets closed:** 32
- **Internal GitLab MRs merged:** 43
- **GitLab.com MRs merged:** 0
- **GitHub PRs:** 0
- **Total MRs:** 43

## Jira Tickets Closed (Q2 2026)

| Key | Summary | Type | Priority |
|-----|---------|------|----------|
| VROOM-35099 | Align Containerfile-base tag to Containerfile | Task | Undefined |
| VROOM-36366 | [Test Console] RHIVOS Tests with XSTREAM 1 should use rhivos-1.0 branch | Task | Undefined |
| VROOM-40488 | Fail to upload to report-portal - got an exception | Task | Undefined |
| VROOM-39896 | [tc-cli/TC] should be able to update env-vars | Task | Undefined |
| VROOM-40277 | Remove result outcome from artifact names | Task | Undefined |
| VROOM-38614 | Kernel Polarion Test Runs do not identify the correct kernel under test | Task | Undefined |
| VROOM-40836 | AI report generation failed with '429 RESOURCE_EXHAUSTED' error | Task | Undefined |
| VROOM-38827 | Add developer-vm image definition image_names | Task | Normal |
| VROOM-40910 | TC should be able to disable upload jobs to support DPAC first run | Task | Undefined |
| VROOM-40913 | [TC-CLI] missing xstream for the 'rhivos packages' CLI | Task | Undefined |
| VROOM-41342 | test-console-db POD fail to start | Task | Undefined |
| VROOM-41358 | Change Jumpstarter URL | Task | Undefined |
| VROOM-38968 | [TC] results should not be published to the production directory if TC_BUILD_URL is provided | Task | Undefined |
| VROOM-40519 | Developer images are released to customers | Task | Normal |
| VROOM-28392 | [TC SOA] need to validate input from HTML controls and REST requests (SEC-APP-REQ-1 - medium) | Task | Blocker |
| VROOM-25409 | Remove alert message when CTC is complete | Task | Undefined |
| VROOM-41913 | Update API doc-string to improve MCP tools | Task | Undefined |
| VROOM-41921 | Change Jumpstarter artifacts URL | Task | Undefined |
| VROOM-42310 | Able to import/export DB | Task | Undefined |
| VROOM-14154 | Include n-v-r target in Polarion Brew Exports | Task | Undefined |
| VROOM-14065 | This epic is for continuous work on the Polarion test-run export mechanism | Epic | Undefined |
| VROOM-41526 | POC to show RHIVOS images at packages.redhat.com | Task | Major |
| VROOM-41908 | [TC Performance] 'runner_status' should be pulled only when opening the details window | Task | Undefined |
| VROOM-38589 | Duplicate VM runs included in the CTC reports | Task | Undefined |
| VROOM-42477 | "Fail to fetch" error in "tmt Testing" when selecting NON-RHIVOS image | Task | Undefined |
| VROOM-42530 | Gemini model "gemini-2.0-flash" stopped being supported and replaced by "gemini-3.5-flash" | Task | Undefined |
| VROOM-44397 | TC is sending the internal 'qemu_kvm' to testing-farm instead of 'qemu' | Task | Undefined |
| VROOM-41587 | Got Gemini '429 RESOURCE_EXHAUSTED' error with 'results-junit.xml' | Task | Undefined |
| VROOM-44570 | Can't run tests with NXP | Task | Undefined |
| VROOM-44576 | Prepare a reduced list of plans for RC3 CTC | Task | Undefined |
| VROOM-44591 | Add rhivos auto-qe bot api token for TC CI/CD pipeline | Task | Undefined |
| VROOM-44653 | Schedule CTC to run with RHIVOS-2 RC3 at the weekend | Task | Undefined |

### Notable patterns

- **32 closed tickets** — highest on the team
- **1 Blocker resolved** (VROOM-28392: security input validation)
- **Test Console is the primary domain** — vast majority of tickets relate to TC platform
- **AI integration work** — Gemini model updates, AI report generation fixes
- **Release support** — RC1, RC2, RC3 CTC scheduling and configuration
- **Cross-platform**: Jumpstarter URL changes, Polarion exports, packages.redhat.com POC

## Internal GitLab MRs (gitlab.cee.redhat.com) — 43 merged

| Date | Project | Title |
|------|---------|-------|
| 2026-04-01 | automotive/services/test-console-frontend | Rename 'Retry' to 'Update' and 'Reuse' to 'Clone' |
| 2026-04-02 | automotive/services/test-console-frontend | Fix "Multihost testing" button in "Run a tmt Test" |
| 2026-04-13 | automotive/services/test-console | Fix exception when upload to report-portal |
| 2026-04-15 | automotive/services/test-console-client | Support update of env-vars |
| 2026-04-15 | automotive/services/test-console | Update data-router URL and fix an exception when zero output |
| 2026-04-16 | automotive/services/test-console | Remove results from artifact link names |
| 2026-04-16 | automotive/services/test-console | docs(openapi): align Flasgger specs with REST handlers |
| 2026-04-26 | automotive/services/test-console | Retry on Gemini '429 RESOURCE_EXHAUSTED' error |
| 2026-04-26 | automotive/services/test-console-client | Support query using --param |
| 2026-04-29 | automotive/services/test-console | Support env-var update through API |
| 2026-04-29 | automotive/services/test-console-client | Add CLI to enable/disable jobs on create and update |
| 2026-04-29 | automotive/services/test-console | Add new API to enable/disable jobs |
| 2026-05-02 | automotive/services/test-console | Fix AutoSD flow is not running |
| 2026-05-06 | automotive/services/test-console-client | Fix 'rhivos packages' CLI command missing xstream param |
| 2026-05-10 | automotive/pipe-x/infrastructure | Change to use quay postgres image |
| 2026-05-10 | automotive/services/test-console | Change Jumpstarter URL |
| 2026-05-11 | automotive/services/test-console | Change Jumpstarter URL to HTTPS |
| 2026-05-13 | automotive/services/test-console | Force TC_BUILD_URL for build and results |
| 2026-05-14 | automotive/services/test-console | Use pure FastAPI code |
| 2026-05-14 | automotive/services/test-console | Regression fix: disable upload-to-results-DB if package does not have NVR |
| 2026-05-15 | automotive/services/test-console | Change CTC plans to 'release_debug' |
| 2026-05-15 | automotive/services/test-console | Always build the container-base when merged to the main |
| 2026-05-15 | automotive/services/test-console | Add new checkpolicy package |
| 2026-05-15 | automotive/services/test-console | Skip SonarQube issues that appear after the merge of FastAPI |
| 2026-05-17 | automotive/services/test-console | Fix error message when run Update |
| 2026-05-18 | automotive/services/test-console | Retry Gemini analysis with pipeline.log if results-junit.xml fails |
| 2026-05-20 | automotive/services/test-console | Add TMT_CONNECT_TIMEOUT env-var used by Jumpstarter |
| 2026-05-20 | automotive/services/test-console | Add 'RHIVOS-2.0-Core-RC1' and 'RHIVOS-2.0-RC1' to releases list |
| 2026-05-26 | automotive/services/test-console | Update API doc-string to improve MCP tools |
| 2026-05-27 | automotive/services/test-console | Change Jumpstarter artifacts URL |
| 2026-05-29 | automotive/services/test-console | Disable CTC because Polarion is down for maintenance |
| 2026-05-31 | automotive/services/test-console | Adding testing-farm qemu inventories |
| 2026-06-01 | automotive/services/test-console | Add import and export DB bash scripts |
| 2026-06-03 | automotive/services/test-console | Fix VM provisioning "fail to fetch" error |
| 2026-06-04 | automotive/services/test-console | Fix "Failed to fetch" error in "tmt Testing" for NON-RHIVOS image |
| 2026-06-05 | automotive/services/test-console | Fix for MR 737 - missing return |
| 2026-06-08 | automotive/services/test-console | Add 'RHIVOS-2.0-RC2' and 'RHIVOS-2.0-Core-RC2' to releases list |
| 2026-06-09 | automotive/services/test-console | Replace 'gemini-2.5-flash' with 'gemini-3.5-flash' |
| 2026-06-10 | automotive/services/test-console | Convert XML to JSON before sending to Gemini |
| 2026-06-10 | automotive/services/test-console | Fix: Testing Farm does not accept 'qemu_kvm' as hardware target |
| 2026-06-16 | automotive/services/test-console | Add RHIVOS-2 RC3 to the releases list |
| 2026-06-17 | automotive/services/test-console | Schedule CTC to run with RHIVOS-2 RC3 at the weekend |
| 2026-06-17 | automotive/services/test-console | Add CONFLUENCE_EMAIL env-var |
