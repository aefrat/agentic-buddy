<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RHAS Test Release Criteria - July 21, 2026</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f6f8fa; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">

<!-- Outer wrapper table -->
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #f6f8fa;">
<tr>
<td align="center" style="padding: 20px 10px;">

<!-- Content table -->
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width: 900px; background-color: #ffffff; border: 1px solid #d0d7de;">

<!-- ============================================================ -->
<!-- HERO BANNER -->
<!-- ============================================================ -->
<tr>
<td style="background-color: #1a1a2e; padding: 40px 32px 32px 32px; text-align: center;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="text-align: center;">
<span style="display: inline-block; background-color: #8250df; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 14px; letter-spacing: 1px; text-transform: uppercase;">DRAFT</span>
</td>
</tr>
<tr>
<td style="text-align: center; padding-top: 18px;">
<span style="font-size: 28px; font-weight: 700; color: #ffffff; letter-spacing: -0.3px;">RHAS Test Release Criteria</span>
</td>
</tr>
<tr>
<td style="text-align: center; padding-top: 8px;">
<span style="font-size: 16px; color: #a8b2d1; font-weight: 400;">Red Hat Automotive Suite - Measurable Quality Gates</span>
</td>
</tr>
<tr>
<td style="text-align: center; padding-top: 14px;">
<span style="font-size: 13px; color: #8892b0;">July 21, 2026 (refreshed from July 2 draft)</span>
</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 1: PURPOSE -->
<!-- ============================================================ -->
<tr>
<td style="padding: 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #24292f; padding: 12px 32px;">
<span style="font-size: 16px; font-weight: 700; color: #ffffff;">1. Purpose</span>
</td>
</tr>
<tr>
<td style="padding: 20px 32px 12px 32px;">
<span style="font-size: 14px; color: #24292f; line-height: 1.65;">
This document defines the measurable pass/fail conditions for each RHAS release milestone. Criteria are layered progressively: each higher milestone is a strict superset of the one below it. The approach is adapted from RHIVOS CTC two-phase gating and the OCP Feature Quality Strategy.
</span>
</td>
</tr>
<tr>
<td style="padding: 8px 32px 24px 32px;">
<span style="font-size: 14px; color: #24292f; line-height: 1.65;">
Three milestones govern release readiness:
</span>
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 12px;">
<tr>
<td style="padding: 6px 0; font-size: 14px; color: #24292f; line-height: 1.5;">
<span style="font-weight: 600;">Monthly Release (RHAS-MMYY)</span> - Rolling monthly drops with baseline quality gates.
</td>
</tr>
<tr>
<td style="padding: 6px 0; font-size: 14px; color: #24292f; line-height: 1.5;">
<span style="font-weight: 600;">Tech Preview (Sep 29, 2026)</span> - First external-facing release. All monthly criteria plus integration, documentation, and pipeline readiness.
</td>
</tr>
<tr>
<td style="padding: 6px 0; font-size: 14px; color: #24292f; line-height: 1.5;">
<span style="font-weight: 600;">GA (Dec 22, 2026)</span> - General Availability. All Tech Preview criteria plus scale, security, compliance, and customer validation.
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 2: HOW TO READ THIS DOCUMENT -->
<!-- ============================================================ -->
<tr>
<td style="padding: 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #24292f; padding: 12px 32px;">
<span style="font-size: 16px; font-weight: 700; color: #ffffff;">2. How to Read This Document</span>
</td>
</tr>
<tr>
<td style="padding: 20px 32px 24px 32px;">
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="font-size: 14px; color: #24292f; line-height: 1.65;">
<tr>
<td style="padding: 4px 0;">
<span style="font-weight: 600;">ID</span> - Each criterion has a unique identifier (e.g., M-01, TP-01, GA-01) for traceability.
</td>
</tr>
<tr>
<td style="padding: 4px 0;">
<span style="font-weight: 600;">Pass Condition</span> - A specific, measurable outcome. No subjective judgment - either the condition is met or it is not.
</td>
</tr>
<tr>
<td style="padding: 4px 0;">
<span style="font-weight: 600;">Status</span> - Current state of the criterion:
</td>
</tr>
<tr>
<td style="padding: 4px 0 4px 24px;">
<table cellpadding="0" cellspacing="0" border="0">
<tr>
<td style="padding: 3px 0;">
<span style="display: inline-block; background-color: #1a7a3e; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 10px; text-transform: uppercase;">Met</span>
<span style="font-size: 13px; color: #57606a; padding-left: 8px;">Criterion satisfied with evidence.</span>
</td>
</tr>
<tr>
<td style="padding: 3px 0;">
<span style="display: inline-block; background-color: #b08800; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 10px; text-transform: uppercase;">Partially Met</span>
<span style="font-size: 13px; color: #57606a; padding-left: 8px;">Some evidence exists but gaps remain.</span>
</td>
</tr>
<tr>
<td style="padding: 3px 0;">
<span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 10px; text-transform: uppercase;">Not Met</span>
<span style="font-size: 13px; color: #57606a; padding-left: 8px;">Criterion not yet satisfied.</span>
</td>
</tr>
<tr>
<td style="padding: 3px 0;">
<span style="display: inline-block; background-color: #57606a; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 10px; text-transform: uppercase;">Not Yet Testable</span>
<span style="font-size: 13px; color: #57606a; padding-left: 8px;">Infrastructure or prerequisites not in place to evaluate.</span>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 4px 0;">
<span style="font-weight: 600;">Evidence</span> - Jira ticket, test result, or infrastructure reference supporting the status.
</td>
</tr>
<tr>
<td style="padding: 4px 0;">
<span style="font-weight: 600;">Waivable</span> - Whether the criterion can be deferred via the waiver process (Section 6). "No" means the criterion cannot be waived under any circumstances.
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 3: MONTHLY RELEASE CRITERIA -->
<!-- ============================================================ -->
<tr>
<td style="padding: 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #24292f; padding: 12px 32px;">
<span style="font-size: 16px; font-weight: 700; color: #ffffff;">3. Monthly Release Criteria (RHAS-MMYY)</span>
</td>
</tr>
<tr>
<td style="padding: 20px 32px 8px 32px;">
<span style="font-size: 14px; color: #57606a; line-height: 1.5;">
These criteria must be met for every monthly release. They represent the baseline quality bar for any RHAS drop.
</span>
</td>
</tr>
<tr>
<td style="padding: 12px 32px 28px 32px;">

<!-- Monthly criteria table -->
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="border: 1px solid #d0d7de; font-size: 13px;">
<!-- Header row -->
<tr>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 50px; text-align: center;">ID</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 140px;">Criterion</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f;">Pass Condition</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 100px; text-align: center;">Status</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 140px;">Evidence</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 55px; text-align: center;">Waivable</td>
</tr>
<!-- M-01 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">M-01</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Builder operator deploys</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Pod running on OCP, no CrashLoopBackOff for 30 min</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #b08800; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Partially Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">Builder tests exist upstream</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f;">Yes</td>
</tr>
<!-- M-02 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">M-02</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">OCI image build completes</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Image pushed to registry, pull succeeds</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; background-color: #f6f8fa;"><span style="display: inline-block; background-color: #b08800; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Partially Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px; background-color: #f6f8fa;">Builder E2E on kind</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f; background-color: #f6f8fa;">Yes</td>
</tr>
<!-- M-03 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">M-03</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">bootc image build completes</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Image boots on target board within 5 min</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #b08800; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Partially Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">RHIVOS nightly covers this</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f;">Yes</td>
</tr>
<!-- M-04 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">M-04</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Jumpstarter exporter connectivity</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">All configured exporters report healthy status</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; background-color: #f6f8fa;"><span style="display: inline-block; background-color: #1a7a3e; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px; background-color: #f6f8fa;">RHIVOS HiL monitoring</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f; background-color: #f6f8fa;">Yes</td>
</tr>
<!-- M-05 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">M-05</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Board lease/release cycle</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Lease acquired within 60s, test executed, released cleanly within 5 min</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #1a7a3e; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">RHIVOS CTC tests</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f;">Yes</td>
</tr>
<!-- M-06 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">M-06</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Smoke tests pass</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">>= 2 board families pass smoke suite (QC 8650 + QC 8775)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; background-color: #f6f8fa;"><span style="display: inline-block; background-color: #1a7a3e; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px; background-color: #f6f8fa;">RHIVOS nightly results</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f; background-color: #f6f8fa;">Yes</td>
</tr>
<!-- M-07 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">M-07</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Builder-to-Jumpstarter handoff</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">OCI artifact from Builder consumed by Jumpstarter, board provisioned</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">E2E integration not tested</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f;">Yes</td>
</tr>
<!-- M-08 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">M-08</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">No P1/P2 regressions</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Zero P1/P2 bugs introduced since previous release</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; background-color: #f6f8fa;"><span style="display: inline-block; background-color: #1a7a3e; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px; background-color: #f6f8fa;">Jira query (no new P1/P2)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #c44b00; background-color: #f6f8fa;">No</td>
</tr>
</table>

</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 4: TECH PREVIEW CRITERIA -->
<!-- ============================================================ -->
<tr>
<td style="padding: 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #24292f; padding: 12px 32px;">
<span style="font-size: 16px; font-weight: 700; color: #ffffff;">4. Tech Preview Criteria (RHAS-0926)</span>
</td>
</tr>
<tr>
<td style="padding: 20px 32px 8px 32px;">
<span style="font-size: 14px; color: #57606a; line-height: 1.5;">
Tech Preview includes all 8 Monthly criteria (Section 3) plus the 7 additional criteria below. Target date: September 29, 2026.
</span>
</td>
</tr>
<tr>
<td style="padding: 12px 32px 28px 32px;">

<!-- Tech Preview criteria table -->
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="border: 1px solid #d0d7de; font-size: 13px;">
<!-- Header row -->
<tr>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 50px; text-align: center;">ID</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 140px;">Criterion</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f;">Pass Condition</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 100px; text-align: center;">Status</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 140px;">Evidence</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 55px; text-align: center;">Waivable</td>
</tr>
<!-- TP-01 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">TP-01</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Full workflow E2E</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Code commit -> build -> deploy -> test-on-board completes in single pipeline run</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">PITCREW-275 Phase 1 not implemented</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #c44b00;">No</td>
</tr>
<!-- TP-02 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">TP-02</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Multi-component integration</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Builder + Jumpstarter + GitOps deploy and function together</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; background-color: #f6f8fa;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px; background-color: #f6f8fa;">Integration tests don't exist</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #c44b00; background-color: #f6f8fa;">No</td>
</tr>
<!-- TP-03 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">TP-03</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">No critical/high CVEs</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Zero critical or high CVEs in shipped container images</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #57606a; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Yet Testable</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">Security scanning not in pipeline</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #c44b00;">No</td>
</tr>
<!-- TP-04 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">TP-04</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Documentation validated</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Installation/usage walkthrough completed by non-author</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; background-color: #f6f8fa;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px; background-color: #f6f8fa;">Docs not yet written</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f; background-color: #f6f8fa;">Yes</td>
</tr>
<!-- TP-05 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">TP-05</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">DS CI pipeline operational</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Ephemeral IPI SNO provisions and runs test suite</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #57606a; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Yet Testable</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">Blocked: DNS approach invalid for OCP ELBs (Jul 13). Needs architectural rethink.</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #c44b00;">No</td>
</tr>
<!-- TP-06 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">TP-06</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Build time baseline</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">OCI + bootc build times measured and recorded (baseline, not threshold)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; background-color: #f6f8fa;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px; background-color: #f6f8fa;">No measurement infrastructure</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f; background-color: #f6f8fa;">Yes</td>
</tr>
<!-- TP-07 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">TP-07</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Operator upgrade</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Upgrade from previous monthly to current version succeeds without downtime</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">Upgrade tests don't exist</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f;">Yes</td>
</tr>
</table>

</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 5: GA CRITERIA -->
<!-- ============================================================ -->
<tr>
<td style="padding: 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #24292f; padding: 12px 32px;">
<span style="font-size: 16px; font-weight: 700; color: #ffffff;">5. GA Criteria (RHAS-1226)</span>
</td>
</tr>
<tr>
<td style="padding: 20px 32px 8px 32px;">
<span style="font-size: 14px; color: #57606a; line-height: 1.5;">
GA includes all 15 Tech Preview criteria (Sections 3 + 4) plus the 8 additional criteria below. Target date: December 22, 2026.
</span>
</td>
</tr>
<tr>
<td style="padding: 12px 32px 28px 32px;">

<!-- GA criteria table -->
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="border: 1px solid #d0d7de; font-size: 13px;">
<!-- Header row -->
<tr>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 50px; text-align: center;">ID</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 140px;">Criterion</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f;">Pass Condition</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 100px; text-align: center;">Status</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 140px;">Evidence</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #24292f; width: 55px; text-align: center;">Waivable</td>
</tr>
<!-- GA-01 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">GA-01</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Concurrent builds</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">>= 5 simultaneous OCI builds complete successfully</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">Scale testing not started</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f;">Yes</td>
</tr>
<!-- GA-02 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">GA-02</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Multi-board HiL</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">>= 4 boards running tests simultaneously without interference</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; background-color: #f6f8fa;"><span style="display: inline-block; background-color: #b08800; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Partially Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px; background-color: #f6f8fa;">RHIVOS runs multi-board but not RHAS-specific</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f; background-color: #f6f8fa;">Yes</td>
</tr>
<!-- GA-03 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">GA-03</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">7-day soak test</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">System under continuous operation for 7 days, no crashes or resource leaks</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">Soak test not designed</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f;">Yes</td>
</tr>
<!-- GA-04 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">GA-04</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Security audit</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Independent security review completed, all critical findings resolved</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; background-color: #f6f8fa;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px; background-color: #f6f8fa;">Audit not started</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #c44b00; background-color: #f6f8fa;">No</td>
</tr>
<!-- GA-05 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">GA-05</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Keycloak SSO validation</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Login -> token -> API access across Builder + Jumpstarter + console</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">SSO integration not tested</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f;">Yes</td>
</tr>
<!-- GA-06 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">GA-06</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">CDN distribution</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Product available via configured distribution channels</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; background-color: #f6f8fa;"><span style="display: inline-block; background-color: #57606a; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Yet Testable</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px; background-color: #f6f8fa;">PITCREW-336 (Distribution) in progress</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #c44b00; background-color: #f6f8fa;">No</td>
</tr>
<!-- GA-07 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f;">GA-07</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">RH-SDLC compliance</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">All required evidence artifacts collected per RH-SDLC process</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px;">PITCREW-334 in progress</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #c44b00;">No</td>
</tr>
<!-- GA-08 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">GA-08</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Customer scenario</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">At least 1 end-to-end customer use case validated</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; background-color: #f6f8fa;"><span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 11px; font-weight: 700; padding: 2px 8px; text-transform: uppercase;">Not Met</span></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; font-size: 12px; background-color: #f6f8fa;">No customer validation planned yet</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; text-align: center; color: #24292f; background-color: #f6f8fa;">Yes</td>
</tr>
</table>

</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 6: WAIVER PROCESS -->
<!-- ============================================================ -->
<tr>
<td style="padding: 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #24292f; padding: 12px 32px;">
<span style="font-size: 16px; font-weight: 700; color: #ffffff;">6. Waiver Process</span>
</td>
</tr>
<tr>
<td style="padding: 20px 32px 24px 32px;">
<span style="font-size: 14px; color: #24292f; line-height: 1.65;">
Not every criterion will be fully met by every milestone. The waiver process provides a controlled way to proceed when a criterion marked "Waivable: Yes" cannot be satisfied in time.
</span>

<table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 16px;">
<tr>
<td style="padding: 8px 0; font-size: 14px; color: #24292f; line-height: 1.65;">
<span style="font-weight: 600;">Who can approve:</span> Product Manager (Paul Wallrabe) and QE Lead must both agree. Neither can unilaterally waive a criterion.
</td>
</tr>
<tr>
<td style="padding: 8px 0; font-size: 14px; color: #24292f; line-height: 1.65;">
<span style="font-weight: 600;">Waiver request must include:</span>
</td>
</tr>
<tr>
<td style="padding: 0 0 0 24px; font-size: 14px; color: #24292f; line-height: 1.65;">
- Jira ticket link for the waiver request<br>
- Impact assessment: what risk does the gap introduce?<br>
- Timeline to fix: when will the criterion be met?<br>
- Customer impact analysis: how does this affect users?
</td>
</tr>
<tr>
<td style="padding: 8px 0; font-size: 14px; color: #24292f; line-height: 1.65;">
<span style="font-weight: 600;">Tracking:</span> Each waiver is tracked as a Jira ticket linked to the release version. This ensures visibility and accountability.
</td>
</tr>
<tr>
<td style="padding: 8px 0; font-size: 14px; color: #24292f; line-height: 1.65;">
<span style="font-weight: 600;">Limits:</span> A maximum of 3 waivers per GA release. This forces prioritization - if more than 3 criteria are unmet, the release cannot proceed.
</td>
</tr>
<tr>
<td style="padding: 8px 0; font-size: 14px; color: #24292f; line-height: 1.65;">
<span style="font-weight: 600;">Non-waivable criteria:</span> Any criterion marked "Waivable: No" cannot be waived under any circumstances. These represent hard quality gates where the risk of proceeding without meeting them is unacceptable.
</td>
</tr>
<tr>
<td style="padding: 8px 0; font-size: 14px; color: #24292f; line-height: 1.65;">
<span style="font-weight: 600;">Deferral, not removal:</span> A waiver does not remove the criterion from the release. It defers enforcement to the next release. The criterion remains on the list and must be satisfied before the subsequent milestone.
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 7: CURRENT READINESS SUMMARY -->
<!-- ============================================================ -->
<tr>
<td style="padding: 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #24292f; padding: 12px 32px;">
<span style="font-size: 16px; font-weight: 700; color: #ffffff;">7. Current Readiness Summary</span>
</td>
</tr>
<tr>
<td style="padding: 20px 32px 8px 32px;">
<span style="font-size: 14px; color: #57606a; line-height: 1.5;">
Aggregate view of how many criteria are currently met at each milestone level. Remember: each higher milestone includes all criteria from the levels below it.
</span>
</td>
</tr>
<tr>
<td style="padding: 12px 32px 28px 32px;">

<!-- Readiness summary table -->
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="border: 1px solid #d0d7de; font-size: 14px;">
<!-- Header -->
<tr>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 12px 16px; font-weight: 700; color: #24292f;">Milestone</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 12px 16px; font-weight: 700; color: #24292f; text-align: center;">Target Date</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 12px 16px; font-weight: 700; color: #24292f; text-align: center;">Criteria Met</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 12px 16px; font-weight: 700; color: #24292f; text-align: center;">Readiness</td>
</tr>
<!-- Monthly -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; font-weight: 600; color: #24292f;">Monthly Release</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; text-align: center; color: #57606a;">Rolling</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; text-align: center; font-weight: 600; color: #24292f;">4 / 8</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; text-align: center;">
<span style="display: inline-block; background-color: #b08800; color: #ffffff; font-size: 13px; font-weight: 700; padding: 4px 16px;">50%</span>
</td>
</tr>
<!-- Tech Preview -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; font-weight: 600; color: #24292f; background-color: #f6f8fa;">Tech Preview</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; text-align: center; color: #57606a; background-color: #f6f8fa;">Sep 29, 2026</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; text-align: center; font-weight: 600; color: #24292f; background-color: #f6f8fa;">4 / 15</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; text-align: center; background-color: #f6f8fa;">
<span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 13px; font-weight: 700; padding: 4px 16px;">27%</span>
</td>
</tr>
<!-- GA -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; font-weight: 600; color: #24292f;">GA</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; text-align: center; color: #57606a;">Dec 22, 2026</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; text-align: center; font-weight: 600; color: #24292f;">4 / 23</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 12px 16px; text-align: center;">
<span style="display: inline-block; background-color: #c44b00; color: #ffffff; font-size: 13px; font-weight: 700; padding: 4px 16px;">17%</span>
</td>
</tr>
</table>

<table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 16px;">
<tr>
<td style="padding: 12px 16px; background-color: #fff8c5; border: 1px solid #d4a72c; font-size: 13px; color: #24292f; line-height: 1.5;">
<span style="font-weight: 700;">Assessment (Jul 21):</span> No change in readiness percentages since Jul 2. Monthly at 50%, Tech Preview at 27%, GA at 17%. The two biggest blockers - no QE lead (PITCREW-337, 3+ months unassigned with zero comments) and the DS pipeline DNS issue (PITCREW-393, DNS approach itself now identified as architecturally wrong for OpenShift ELBs) - have not improved. PITCREW-403 (flaky E2E) was closed, which is positive but does not move any criterion. With 70 days to Tech Preview, the gap between current state and target is widening.
</td>
</tr>
</table>

</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 8: CRITICAL BLOCKERS -->
<!-- ============================================================ -->
<tr>
<td style="padding: 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #24292f; padding: 12px 32px;">
<span style="font-size: 16px; font-weight: 700; color: #ffffff;">8. Critical Blockers</span>
</td>
</tr>
<tr>
<td style="padding: 20px 32px 8px 32px;">
<span style="font-size: 14px; color: #57606a; line-height: 1.5;">
These are the issues that must be resolved before significant progress can be made on the release criteria. Listed in order of impact.
</span>
</td>
</tr>
<tr>
<td style="padding: 12px 32px 28px 32px;">

<!-- Blockers table -->
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="border: 1px solid #d0d7de; font-size: 13px;">
<!-- Header -->
<tr>
<td style="background-color: #c44b00; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #ffffff;">Blocker</td>
<td style="background-color: #c44b00; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #ffffff;">Criterion Affected</td>
<td style="background-color: #c44b00; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #ffffff;">Jira</td>
<td style="background-color: #c44b00; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #ffffff;">Owner</td>
<td style="background-color: #c44b00; border-bottom: 2px solid #d0d7de; padding: 10px 8px; font-weight: 700; color: #ffffff;">Resolution Target</td>
</tr>
<!-- Blocker 1 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; font-weight: 600;">No QE lead (3+ months, 0 comments)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">All criteria</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a;">PITCREW-337</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a;">(unassigned)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Jul target missed; overdue</td>
</tr>
<!-- Blocker 2 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; font-weight: 600; background-color: #f6f8fa;">DNS blocking DS pipeline (approach invalid)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">TP-05, TP-01</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; background-color: #f6f8fa;">PITCREW-393 / VROOM-44573</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; background-color: #f6f8fa;">Evgeni Vakhonin / Eitan Raviv</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Jul target missed; needs rethink</td>
</tr>
<!-- Blocker 3 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; font-weight: 600;">Distribution incomplete</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">GA-06</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a;">PITCREW-336</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a;"></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f;">Aug 2026</td>
</tr>
<!-- Blocker 4 -->
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; font-weight: 600; background-color: #f6f8fa;">No E2E test infrastructure</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">TP-01, TP-02</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; background-color: #f6f8fa;">PITCREW-275</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #57606a; background-color: #f6f8fa;"></td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 8px; color: #24292f; background-color: #f6f8fa;">Sep 2026</td>
</tr>
</table>

</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 9: CRITERION DEPENDENCY MAP -->
<!-- ============================================================ -->
<tr>
<td style="padding: 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #24292f; padding: 12px 32px;">
<span style="font-size: 16px; font-weight: 700; color: #ffffff;">9. Criterion Dependency Map</span>
</td>
</tr>
<tr>
<td style="padding: 20px 32px 8px 32px;">
<span style="font-size: 14px; color: #57606a; line-height: 1.5;">
Some criteria cannot be satisfied until prerequisites are in place. Understanding these dependencies is critical for planning the work sequence.
</span>
</td>
</tr>
<tr>
<td style="padding: 12px 32px 28px 32px;">

<table cellpadding="0" cellspacing="0" border="0" width="100%" style="border: 1px solid #d0d7de; font-size: 13px;">
<tr>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 12px; font-weight: 700; color: #24292f; width: 200px;">Criterion</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 12px; font-weight: 700; color: #24292f;">Depends On</td>
<td style="background-color: #f6f8fa; border-bottom: 2px solid #d0d7de; padding: 10px 12px; font-weight: 700; color: #24292f;">Implication</td>
</tr>
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #24292f; font-weight: 600;">M-07 (Builder-to-Jumpstarter)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #24292f;">TP-05 (DS pipeline)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #57606a;">Cannot test the handoff without a working pipeline to run it in.</td>
</tr>
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #24292f; font-weight: 600; background-color: #f6f8fa;">TP-01 (Full workflow E2E)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #24292f; background-color: #f6f8fa;">M-07 + TP-05</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #57606a; background-color: #f6f8fa;">E2E workflow requires both the handoff mechanism and the CI pipeline.</td>
</tr>
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #24292f; font-weight: 600;">TP-02 (Multi-component)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #24292f;">TP-01</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #57606a;">Multi-component integration is a superset of the E2E workflow.</td>
</tr>
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #24292f; font-weight: 600; background-color: #f6f8fa;">GA-06 (CDN distribution)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #24292f; background-color: #f6f8fa;">PITCREW-336 (Distribution)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #57606a; background-color: #f6f8fa;">Distribution channels must be configured before CDN delivery can be validated.</td>
</tr>
<tr>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #24292f; font-weight: 600;">GA-07 (RH-SDLC compliance)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #24292f;">GA-04 (Security audit) + GA-06 (CDN)</td>
<td style="border-bottom: 1px solid #d0d7de; padding: 10px 12px; color: #57606a;">SDLC evidence collection requires completed security audit results and distribution artifacts.</td>
</tr>
</table>

<table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 16px;">
<tr>
<td style="padding: 12px 16px; background-color: #ddf4ff; border: 1px solid #54aeff; font-size: 13px; color: #24292f; line-height: 1.5;">
<span style="font-weight: 700;">Critical path:</span> The longest dependency chain runs TP-05 (DS pipeline) -> M-07 (handoff) -> TP-01 (E2E) -> TP-02 (multi-component). Unblocking TP-05 remains the single highest-leverage action, but as of Jul 13 the DNS approach itself is invalid for OpenShift (needs wildcard DNS for ELBs). This requires an architectural rethink, not just an IT ticket resolution.
</td>
</tr>
</table>

</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- FOOTER -->
<!-- ============================================================ -->
<tr>
<td style="padding: 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #f6f8fa; border-top: 1px solid #d0d7de; padding: 20px 32px; text-align: center;">
<span style="font-size: 12px; color: #57606a; line-height: 1.6;">
Generated by RHAS QE Expert Lead Agent on July 2, 2026. Refreshed July 21, 2026. Version: DRAFT v1.1.<br>
Companion document: RHAS Test Strategy (rhas-test-strategy-2026-07-21.html)
</span>
</td>
</tr>
</table>
</td>
</tr>

</table>
<!-- End content table -->

</td>
</tr>
</table>
<!-- End outer wrapper table -->

</body>
</html>
