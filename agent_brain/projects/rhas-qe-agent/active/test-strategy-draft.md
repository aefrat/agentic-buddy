<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RHAS Test Strategy - July 2, 2026</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f6f8fa; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">

<!-- Outer wrapper table -->
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #f6f8fa;">
<tr>
<td align="center" style="padding: 20px 10px;">

<!-- Content table -->
<table cellpadding="0" cellspacing="0" border="0" width="900" style="max-width: 900px; background-color: #ffffff;">

<!-- ============================================================ -->
<!-- HERO BANNER -->
<!-- ============================================================ -->
<tr>
<td style="background-color: #1a1a2e; padding: 40px 40px 30px 40px;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td>
<h1 style="margin: 0 0 8px 0; font-size: 32px; font-weight: 700; color: #ffffff; letter-spacing: -0.5px;">RHAS Test Strategy</h1>
<p style="margin: 0 0 16px 0; font-size: 16px; color: #b0b0cc; font-weight: 400;">Red Hat Automotive Suite - Quality Engineering Strategy</p>
</td>
</tr>
<tr>
<td>
<table cellpadding="0" cellspacing="0" border="0">
<tr>
<td style="padding-right: 16px;">
<span style="font-size: 13px; color: #8888aa;">Date: July 2, 2026</span>
</td>
<td>
<span style="display: inline-block; background-color: #0550ae; color: #ffffff; font-size: 12px; font-weight: 600; padding: 4px 12px; letter-spacing: 0.5px;">DRAFT</span>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 1: EXECUTIVE SUMMARY -->
<!-- ============================================================ -->
<tr>
<td style="padding: 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">1. Executive Summary</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">
<p style="margin: 0 0 14px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
RHAS is approaching two critical milestones - Tech Preview (September 29, 2026) and GA (December 22, 2026) - with no formal QE process in place. The current testing landscape has real strengths but also significant gaps that need addressing on a compressed timeline.
</p>
<p style="margin: 0 0 14px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
<strong>What works today:</strong> Upstream testing is solid. Each component runs unit and integration tests per-PR via GitHub Actions and Packit. The RHIVOS CTC model provides a proven gating framework we can adapt. HiL board testing infrastructure is operational and shared with RHIVOS via Jumpstarter.
</p>
<p style="margin: 0 0 14px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
<strong>What is missing:</strong> PITCREW-337 (QE Readiness) remains unassigned - there is no QE lead driving this work. The downstream testing pipeline is blocked by a DNS resolution issue (PITCREW-393/394). No release criteria or formal test strategy exist. Cross-component integration testing has never been attempted.
</p>
<p style="margin: 0 0 14px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
<strong>Context:</strong> OpenShift QE is simultaneously undergoing its own modernization effort (OCPQE-32074), which presents both alignment opportunities and a cautionary example of the complexity involved. RHIVOS CTC offers a closer, more directly applicable model for RHAS given the shared automotive context.
</p>

<table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top: 8px;">
<tr>
<td style="background-color: #fff8c5; padding: 16px 20px; border-left: 4px solid #b08800;">
<p style="margin: 0 0 4px 0; font-size: 14px; font-weight: 600; color: #24292f;">Critical actions needed:</p>
<ol style="margin: 8px 0 0 0; padding-left: 20px; font-size: 14px; line-height: 1.8; color: #24292f;">
<li>Assign a QE lead for RHAS (PITCREW-337) - this is the single biggest blocker</li>
<li>Unblock the downstream CI pipeline - DNS resolution for PITCREW-393</li>
<li>Define and adopt this test strategy as the guiding document</li>
<li>Establish release criteria (companion document, separate deliverable)</li>
</ol>
</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 2: SCOPE - RHAS PLATFORM COMPONENTS -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">2. Scope - RHAS Platform Components</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">
<p style="margin: 0 0 14px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
RHAS is a Tier 2 integrated platform built on OpenShift. It provides the tooling and infrastructure for building, testing, deploying, and managing automotive-grade software on vehicles and edge devices. The following components define the test scope:
</p>

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de; margin-bottom: 16px;">
<tr>
<td style="background-color: #f6f8fa; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #24292f; width: 180px; border: 1px solid #d0d7de;">Builder Operator</td>
<td style="padding: 10px 14px; font-size: 13px; color: #24292f; border: 1px solid #d0d7de;">Builds OCI and bootc images on OpenShift. Integrates with Konflux for pipeline orchestration. Core workflow entry point for most RHAS use cases.</td>
</tr>
<tr>
<td style="background-color: #f6f8fa; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Jumpstarter</td>
<td style="padding: 10px 14px; font-size: 13px; color: #24292f; border: 1px solid #d0d7de;">Hardware provisioning and testing framework. Manages physical board lifecycle - power cycling, flashing, serial console access. Shared with RHIVOS for HiL testing.</td>
</tr>
<tr>
<td style="background-color: #f6f8fa; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Konflux / Pipelines</td>
<td style="padding: 10px 14px; font-size: 13px; color: #24292f; border: 1px solid #d0d7de;">CI/CD pipeline orchestration. Replaces legacy build systems. PITCREW-335 tracks onboarding. Provides the pipeline backbone for downstream builds.</td>
</tr>
<tr>
<td style="background-color: #f6f8fa; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">GitOps</td>
<td style="padding: 10px 14px; font-size: 13px; color: #24292f; border: 1px solid #d0d7de;">Deployment automation via ArgoCD patterns. Manages fleet configuration and software updates to vehicles and edge devices.</td>
</tr>
<tr>
<td style="background-color: #f6f8fa; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Keycloak</td>
<td style="padding: 10px 14px; font-size: 13px; color: #24292f; border: 1px solid #d0d7de;">Identity and access management. Handles authentication and authorization for the RHAS platform and its APIs.</td>
</tr>
</table>

<p style="margin: 16px 0 10px 0; font-size: 14px; font-weight: 600; color: #24292f;">Benny's 3-Layer Test Architecture</p>
<p style="margin: 0 0 10px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
The testing strategy follows a three-layer architecture, prioritizing speed and cost-effectiveness at the base:
</p>

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #1a1a2e; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #ffffff; width: 100px; border: 1px solid #d0d7de;">Layer 1</td>
<td style="background-color: #1a1a2e; padding: 10px 14px; font-size: 13px; color: #ffffff; border: 1px solid #d0d7de;">Jumpstarter E2E tests on kind clusters. Fastest, cheapest, primary gate. This is the foundation - most test investment goes here.</td>
</tr>
<tr>
<td style="background-color: #2d2d44; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #ffffff; border: 1px solid #d0d7de;">Layer 2</td>
<td style="background-color: #2d2d44; padding: 10px 14px; font-size: 13px; color: #ffffff; border: 1px solid #d0d7de;">Builder E2E tests on kind clusters. Less ideal per Benny's assessment, but needed for Builder Operator validation before full integration.</td>
</tr>
<tr>
<td style="background-color: #3d3d5c; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #ffffff; border: 1px solid #d0d7de;">Layer 3</td>
<td style="background-color: #3d3d5c; padding: 10px 14px; font-size: 13px; color: #ffffff; border: 1px solid #d0d7de;">Black-box downstream testing on OpenShift. PITCREW-275 Phase 1 (kind) + Phase 2 (ephemeral IPI SNO). Most realistic but slowest and most expensive.</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 3: TEST TYPES MATRIX -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">3. Test Types Matrix</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">
<p style="margin: 0 0 14px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
Coverage status by component and test type. Colors indicate maturity: green = exists and running, amber = partial coverage or work in progress, red = missing and needed, gray = not applicable.
</p>

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Component</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">Unit</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">Integration</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">E2E</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">HiL</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">Perf</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">Security</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Builder</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Partial</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; color: #57606a; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">N/A</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Jumpstarter</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Konflux</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Partial</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; color: #57606a; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">N/A</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">GitOps</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Partial</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; color: #57606a; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">N/A</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Keycloak</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Partial</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; color: #57606a; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">N/A</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Partial</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Cross-component</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; color: #57606a; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">N/A</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Missing</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 4: TEST ENVIRONMENTS -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">4. Test Environments</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Environment</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Purpose</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Infrastructure</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">Status</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Local kind clusters</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">L1/L2 tests</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Developer workstation</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Available</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Ephemeral IPI SNO</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">L3 DS tests</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Cloud provisioned</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Blocked (DNS)</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">ROSA dev cluster</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">HiL controller</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">ROSA on AWS</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Operational</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Physical board lab</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">HiL execution</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">QC 8650/8775/8979/8255, NXP S32N79/iMX8, Renesas R-Car X5H</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Operational</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Testing Farm</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">VM-based tests</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Fedora infra</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Available</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">GitHub Actions</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Upstream CI</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">GitHub</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Operational</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">GitLab CEE</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">bootc tests</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">gitlab.cee.redhat.com</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Partially operational</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 5: GATING MODEL -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">5. Gating Model</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">
<p style="margin: 0 0 14px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
Three-tier gating model aligned with release milestones. Each tier includes all requirements from the tier below. Adapted from the RHIVOS CTC two-phase model (Reduced CTC then Full ASIL Release CTC).
</p>

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #1a7a3e; padding: 12px 14px; font-size: 13px; font-weight: 700; color: #ffffff; width: 160px; border: 1px solid #d0d7de; vertical-align: top;">Monthly Release Gate</td>
<td style="padding: 12px 14px; font-size: 13px; color: #24292f; border: 1px solid #d0d7de;">
<ul style="margin: 0; padding-left: 18px; line-height: 1.8;">
<li>Smoke tests pass (all components start and respond)</li>
<li>Board connectivity verified (Jumpstarter provisioning works)</li>
<li>No P1 or P2 regressions from previous release</li>
<li>All upstream PR gates green</li>
</ul>
</td>
</tr>
<tr>
<td style="background-color: #b08800; padding: 12px 14px; font-size: 13px; font-weight: 700; color: #ffffff; border: 1px solid #d0d7de; vertical-align: top;">Tech Preview Gate<br><span style="font-weight: 400; font-size: 11px;">(Sep 29, 2026)</span></td>
<td style="padding: 12px 14px; font-size: 13px; color: #24292f; border: 1px solid #d0d7de;">
<ul style="margin: 0; padding-left: 18px; line-height: 1.8;">
<li>All Monthly gate criteria</li>
<li>E2E workflow validation (build-to-deploy on at least one board family)</li>
<li>Multi-component integration tests pass</li>
<li>Security scan with no critical or high findings</li>
<li>Documentation coverage for all user-facing features</li>
<li>Known issues documented with workarounds</li>
</ul>
</td>
</tr>
<tr>
<td style="background-color: #c44b00; padding: 12px 14px; font-size: 13px; font-weight: 700; color: #ffffff; border: 1px solid #d0d7de; vertical-align: top;">GA Gate<br><span style="font-weight: 400; font-size: 11px;">(Dec 22, 2026)</span></td>
<td style="padding: 12px 14px; font-size: 13px; color: #24292f; border: 1px solid #d0d7de;">
<ul style="margin: 0; padding-left: 18px; line-height: 1.8;">
<li>All Tech Preview gate criteria</li>
<li>Scale testing (N concurrent builds, M concurrent board targets)</li>
<li>Soak testing (72h sustained operation without degradation)</li>
<li>Security audit with formal remediation of all findings</li>
<li>Customer validation program feedback incorporated</li>
<li>Upgrade path tested (from Tech Preview to GA)</li>
<li>Performance baselines established and met</li>
</ul>
</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 6: OWNERSHIP MATRIX -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">6. Ownership Matrix</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">
<p style="margin: 0 0 14px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
Clear ownership is the most important enabler for testing. The biggest gap today is the absence of a QE lead - everything downstream of that assignment is stalled.
</p>

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Testing Area</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Current Owner</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Needed By</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">Status</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Upstream unit/integration</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Component developers</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Continuous</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Covered</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">RHIVOS CTC (includes Jumpstarter)</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Rachel Sibley (coordination), Stephen Bertram (waivers)</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Continuous</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Covered</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">HiL board tests</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">ATC QE team</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Continuous</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Covered</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">DS CI pipeline</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Matt Minnich</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Aug 2026</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Blocked</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">E2E workflow tests</td>
<td style="padding: 8px 10px; font-size: 12px; color: #57606a; font-style: italic; border: 1px solid #d0d7de;">(unassigned)</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Sep 2026</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Gap</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Release criteria validation</td>
<td style="padding: 8px 10px; font-size: 12px; color: #57606a; font-style: italic; border: 1px solid #d0d7de;">(unassigned - needs QE lead)</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Aug 2026</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Gap</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Security scanning</td>
<td style="padding: 8px 10px; font-size: 12px; color: #57606a; font-style: italic; border: 1px solid #d0d7de;">(unassigned)</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Sep 2026</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Gap</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Performance baselines</td>
<td style="padding: 8px 10px; font-size: 12px; color: #57606a; font-style: italic; border: 1px solid #d0d7de;">(unassigned)</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Dec 2026</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Gap</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 7: TOOL CHAIN -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">7. Tool Chain</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Tool</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Purpose</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">Status</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">pytest</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Unit and integration tests</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">In use</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Jumpstarter</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">HiL provisioning and testing</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">In use (upstream + RHIVOS)</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Testing Farm</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">VM-based test execution</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Available</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">CTC framework</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Release confidence testing</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">In use (RHIVOS), adapt for RHAS</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">GitHub Actions</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Upstream CI</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">In use</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Packit</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Upstream PR gating</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">In use</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Konflux</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Downstream CI/CD</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Planned (PITCREW-335)</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Greenwave + Gator</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Automated gating policy</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">In use (RHIVOS), adapt for RHAS</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Test Console</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Test result dashboard</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">In use (test-console.corp.redhat.com)</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 8: CADENCE -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">8. Testing Cadence</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; width: 120px; border: 1px solid #d0d7de;">Cadence</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Activities</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; width: 120px; border: 1px solid #d0d7de;">Current State</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Per-PR</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Upstream unit + integration tests via GitHub Actions + Packit. Linting, formatting, type checks.</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists today</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Nightly</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Downstream compose + smoke tests + board provisioning verification. Adapt from RHIVOS nightly compose model.</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Recommended</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Weekly</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Full E2E workflow validation. Builder-to-Jumpstarter handoff. Cross-component integration on OpenShift.</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Recommended</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Per-release</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">CTC-style confidence testing. Full regression suite. Security scan. Performance baseline comparison. Adapt from RHIVOS two-phase CTC model.</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Recommended</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Continuous</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">HiL board health monitoring via monitor.ajo.es. Board availability and connectivity tracking.</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Exists</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 9: RHIVOS vs OPENSHIFT COMPARISON -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">9. RHIVOS vs OpenShift - Testing Approach Comparison</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">
<p style="margin: 0 0 14px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
RHAS sits between two established testing ecosystems. RHIVOS is the closer model (shared automotive context, shared hardware, shared tooling), while OpenShift represents a mature but different scale of QE. This comparison informs where to borrow from each.
</p>

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 11px; font-weight: 600; color: #24292f; width: 100px; border: 1px solid #d0d7de;">Aspect</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 11px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">RHIVOS</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 11px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">OpenShift</td>
<td style="background-color: #e8f0fe; padding: 8px 10px; font-size: 11px; font-weight: 600; color: #0550ae; border: 1px solid #d0d7de;">RHAS Recommendation</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 11px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">CI system</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Custom compose pipeline + CTC</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Prow + ci-operator</td>
<td style="background-color: #e8f0fe; padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Adapt CTC model, leverage Konflux instead of Prow</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 11px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Gating</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Greenwave + Gator + WaiverDB</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Payload qualifying jobs (blocking/informing)</td>
<td style="background-color: #e8f0fe; padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Adopt Greenwave gating (already in ecosystem)</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 11px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Test types</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Smoke, kernel gating, HiL, systemd</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Unit, integration, E2E, conformance</td>
<td style="background-color: #e8f0fe; padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Combine: unit/integration from OCP, HiL from RHIVOS</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 11px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Hardware testing</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Physical boards via Jumpstarter</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">None (software-only)</td>
<td style="background-color: #e8f0fe; padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">RHIVOS model (Jumpstarter already shared)</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 11px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Release process</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Compose -> CTC -> tag flow</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">EC -> RC -> GA builds</td>
<td style="background-color: #e8f0fe; padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Adapt monthly + milestone model from both</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 11px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Quality monitoring</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Test Console</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Sippy + Component Readiness</td>
<td style="background-color: #e8f0fe; padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Start with Test Console, evaluate Sippy later</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 11px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Test case mgmt</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">None formal</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Polarion (migrating to Jira)</td>
<td style="background-color: #e8f0fe; padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Jira from the start (align with OCP direction)</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 11px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Agentic/AI testing</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">None</td>
<td style="padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">QualityFlow proposal, Console-harness pipeline</td>
<td style="background-color: #e8f0fe; padding: 8px 10px; font-size: 11px; color: #24292f; border: 1px solid #d0d7de;">Evaluate for RHAS v2 (post-GA)</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 10: OPENSHIFT QE CONTACTS -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">10. OpenShift QE Contacts</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">
<p style="margin: 0 0 14px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
OpenShift QE is undergoing its own modernization. These contacts are relevant for alignment and shared learnings. Prioritize by immediacy of value to RHAS.
</p>

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Name</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Role</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Jira Epic</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Relevance</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Recommended Action</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Cameron Meadors</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Quality Strategy owner</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">OCPQE-32074</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">OCP QE philosophy</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Schedule alignment call</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">John George</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Next-gen QE</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">OCPQE-32073</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Test modernization</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Join #wg-openshift-next-gen-quality</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">David Kutalek</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Test Case Management</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">OCPQE-32075</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Test tracking tooling</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Align on Jira/Confluence approach</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Ken Zhang</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Test suite levels</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">OCPQE-32067</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Test organization model</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Review active/stable classification</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Devan Goodwin</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">QE strategy direction</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">OCPSTRAT-3352</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Long-term QE vision</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Monitor strategic initiative</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 11: AGENTIC TESTING OPTIONS -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">11. Agentic Testing Options</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">
<p style="margin: 0 0 14px 0; font-size: 14px; line-height: 1.6; color: #24292f;">
AI-assisted testing is maturing rapidly but unevenly. For RHAS, the priority is establishing foundational testing first. Agentic tools can augment that foundation - they should not be the foundation itself.
</p>

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de; margin-bottom: 16px;">
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; width: 100px; border: 1px solid #d0d7de;">Adoption Phase</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Tool</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Description</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">RHAS Fit</td>
</tr>
<tr>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; font-weight: 600; border: 1px solid #d0d7de;">Adopt now</td>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Qodo Cover (TestGen-LLM)</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">AI-generated unit tests. Open source, low risk, immediate value for increasing coverage.</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Builder and Jumpstarter components. Boost unit test coverage quickly with human review.</td>
</tr>
<tr>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; font-weight: 600; border: 1px solid #d0d7de;">Trial</td>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Playwright + MCP</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">E2E web testing with AI-driven browser automation. Proven at Red Hat via Console-harness pattern.</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Good fit for RHAS web console testing. Lower priority than core component testing.</td>
</tr>
<tr>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; font-weight: 600; border: 1px solid #d0d7de;">Assess</td>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Schemathesis</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">API contract testing generated from OpenAPI specs. Finds spec violations and edge cases automatically.</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Relevant for Builder operator APIs. Evaluate once API specs are stable.</td>
</tr>
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; color: #57606a; font-weight: 600; border: 1px solid #d0d7de;">Hold</td>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Full AI-native frameworks</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">End-to-end AI-driven test generation, execution, and analysis. Maturity varies widely.</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Maturity risk too high for automotive safety context. Revisit post-GA for RHAS v2.</td>
</tr>
</table>

<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #f6f8fa; padding: 12px 16px; border-left: 4px solid #57606a;">
<p style="margin: 0; font-size: 13px; color: #57606a; line-height: 1.5;">
<strong>Academic note:</strong> A February 2026 paper found that test-writing volume has no statistically significant effect on task resolution in autonomous coding agents. Tests serve primarily as a debugging aid in agent contexts, not as a quality gate. This reinforces the recommendation to treat AI-generated tests as coverage supplements, not reliability signals.
</p>
</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 12: GAP ANALYSIS -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">12. Gap Analysis</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Area</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">Current State</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">Tech Preview (Sep)</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">GA (Dec)</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">QE ownership</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">No QE lead</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">QE lead + 1 engineer</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">QE lead + 2 engineers</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">DS CI pipeline</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Blocked (DNS)</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Operational</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Mature</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Release criteria</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">None defined</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Defined + enforced</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Refined from TP feedback</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Test strategy</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">None (this document)</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Adopted + executing</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Refined from TP learnings</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Cross-component E2E</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Never attempted</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Core workflow covered</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Full matrix coverage</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Security scanning</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Not started</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Container + deps scanning</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Full audit completed</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Performance baselines</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Not started</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; color: #57606a; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Not required</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Baselines established</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Soak testing</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Not started</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; color: #57606a; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Not required</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">72h soak completed</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Upgrade testing</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Not started</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; color: #57606a; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Not required</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">TP -> GA path tested</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Nightly builds</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Not running</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Nightly compose + smoke</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Nightly + extended suite</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 13: TIMELINE -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">13. Timeline</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; width: 100px; border: 1px solid #d0d7de;">Month</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Deliverables</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; width: 100px; border: 1px solid #d0d7de;">Milestone</td>
</tr>
<tr>
<td style="padding: 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Jul 2026</td>
<td style="padding: 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">
<ul style="margin: 0; padding-left: 16px; line-height: 1.7;">
<li>QE lead assigned (PITCREW-337)</li>
<li>DS pipeline DNS resolved (Evgeni Vakhonin)</li>
<li>Test strategy document adopted (this document)</li>
<li>Release criteria draft started</li>
</ul>
</td>
<td style="background-color: #fff8c5; padding: 10px; font-size: 11px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Foundation</td>
</tr>
<tr>
<td style="padding: 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Aug 2026</td>
<td style="padding: 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">
<ul style="margin: 0; padding-left: 16px; line-height: 1.7;">
<li>DS CI pipeline operational (PITCREW-393/394)</li>
<li>Nightly builds running with smoke tests</li>
<li>Builder-to-Jumpstarter handoff tested end-to-end</li>
<li>Release criteria finalized</li>
<li>Greenwave gating policies configured</li>
</ul>
</td>
<td style="background-color: #fff8c5; padding: 10px; font-size: 11px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Pipeline Ready</td>
</tr>
<tr>
<td style="padding: 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Sep 2026</td>
<td style="padding: 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">
<ul style="margin: 0; padding-left: 16px; line-height: 1.7;">
<li>E2E workflow validation complete (build-to-deploy on board)</li>
<li>Multi-component integration tests running</li>
<li>Security scan with no critical/high findings</li>
<li>Documentation coverage verified</li>
<li>Known issues documented with workarounds</li>
</ul>
</td>
<td style="background-color: #c44b00; padding: 10px; font-size: 11px; color: #ffffff; text-align: center; font-weight: 700; border: 1px solid #d0d7de;">TECH PREVIEW</td>
</tr>
<tr>
<td style="padding: 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Oct 2026</td>
<td style="padding: 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">
<ul style="margin: 0; padding-left: 16px; line-height: 1.7;">
<li>Performance baselines established for all components</li>
<li>Scale testing begins (concurrent builds, concurrent boards)</li>
<li>TP feedback incorporated into test suite</li>
</ul>
</td>
<td style="background-color: #f6f8fa; padding: 10px; font-size: 11px; color: #57606a; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Hardening</td>
</tr>
<tr>
<td style="padding: 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Nov 2026</td>
<td style="padding: 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">
<ul style="margin: 0; padding-left: 16px; line-height: 1.7;">
<li>Soak testing (72h sustained operation)</li>
<li>Security audit with formal remediation</li>
<li>Upgrade testing (TP to GA path)</li>
<li>Customer validation program active</li>
</ul>
</td>
<td style="background-color: #f6f8fa; padding: 10px; font-size: 11px; color: #57606a; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Validation</td>
</tr>
<tr>
<td style="padding: 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Dec 2026</td>
<td style="padding: 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">
<ul style="margin: 0; padding-left: 16px; line-height: 1.7;">
<li>Customer validation feedback incorporated</li>
<li>Full compliance verification</li>
<li>All release criteria met</li>
<li>GA readiness sign-off</li>
</ul>
</td>
<td style="background-color: #1a7a3e; padding: 10px; font-size: 11px; color: #ffffff; text-align: center; font-weight: 700; border: 1px solid #d0d7de;">GA</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- SECTION 14: RISKS -->
<!-- ============================================================ -->
<tr>
<td style="padding: 16px 0 0 0;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="background-color: #0550ae; padding: 12px 40px;">
<h2 style="margin: 0; font-size: 18px; font-weight: 600; color: #ffffff;">14. Risks</h2>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 40px 16px 40px;">

<table cellpadding="0" cellspacing="0" border="1" width="100%" style="border-collapse: collapse; border-color: #d0d7de;">
<tr>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Risk</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">Severity</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; text-align: center; border: 1px solid #d0d7de;">Likelihood</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Impact</td>
<td style="background-color: #f6f8fa; padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Mitigation</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">No QE lead assigned</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Critical</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">High</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">No ownership of QE process. Everything downstream stalls.</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Assign PITCREW-337 immediately. Interim: designate acting QE lead from existing team.</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">DS pipeline blocked</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">High</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Current</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Cannot run downstream tests. L3 testing impossible.</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Resolve DNS issue (Evgeni Vakhonin). Escalate if not resolved by mid-July.</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Timeline compression</td>
<td style="background-color: #ffebe9; padding: 8px 10px; font-size: 12px; color: #c44b00; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">High</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Medium</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Only 3 months to Tech Preview. Insufficient time for comprehensive testing.</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Prioritize L1 tests first (fastest value). Defer L3 if timeline is tight. Accept TP with known gaps and workarounds.</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">HiL flakiness</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Medium</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Known</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">False failures block releases. Erodes confidence in test results.</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">PITCREW-403 fix. Implement retry logic. Classify flaky vs. real failures in test reporting.</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Konflux onboarding delay</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Medium</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Medium</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Build pipeline not ready. Downstream builds delayed.</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Track via PITCREW-335. Maintain fallback build path until Konflux is stable.</td>
</tr>
<tr>
<td style="padding: 8px 10px; font-size: 12px; font-weight: 600; color: #24292f; border: 1px solid #d0d7de;">Single point of failure (Benny)</td>
<td style="background-color: #fff8c5; padding: 8px 10px; font-size: 12px; color: #b08800; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Medium</td>
<td style="background-color: #dafbe1; padding: 8px 10px; font-size: 12px; color: #1a7a3e; text-align: center; font-weight: 600; border: 1px solid #d0d7de;">Low</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Testing architecture knowledge concentrated in one person.</td>
<td style="padding: 8px 10px; font-size: 12px; color: #24292f; border: 1px solid #d0d7de;">Document all architecture decisions. Share ownership of test infrastructure with QE lead once assigned.</td>
</tr>
</table>
</td>
</tr>

<!-- ============================================================ -->
<!-- FOOTER -->
<!-- ============================================================ -->
<tr>
<td style="padding: 30px 40px 20px 40px;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td style="border-top: 1px solid #d0d7de; padding-top: 20px;">
<p style="margin: 0 0 4px 0; font-size: 12px; color: #57606a;">
Generated by RHAS QE Expert Lead Agent on July 2, 2026
</p>
<p style="margin: 0 0 4px 0; font-size: 12px; color: #57606a;">
Version: DRAFT v1.0
</p>
<p style="margin: 0; font-size: 11px; color: #8b949e;">
This document is a living strategy guide. Update as RHAS QE matures. Companion documents: Release Criteria (TBD), Test Plan per component (TBD).
</p>
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