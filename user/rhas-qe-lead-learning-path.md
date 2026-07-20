# RHAS QE Lead - One-Week Learning Path

Target: Ramp up from ATC engineering manager to RHAS QE lead in one week.
Approach: Product first, then testing landscape, then strategy and people. Each day has a morning block (reading/watching) and an afternoon block (hands-on/meetings).

---

## Day 1 (Mon) - Product Foundation: What is RHAS?

**Goal:** Understand what RHAS is, what it does, who it's for, and how it relates to RHIVOS.

### Morning - Read

1. **RHAS Strategic Guide** - the single most important doc for product context
   - Google Doc: `10qaHs_mfOCJtIJoJq35HjhHAeLEMJwYde51wgCKrQx8`
   - What to extract: Tier definitions, target persona (platform engineers at automotive OEMs), product positioning vs RHIVOS

2. **RHAS 2026 Roadmap** - release timeline and feature roadmap
   - Google Doc: `1j4Chcv71S8Y3P8HT2wTao9ZEoHoHm-X102VmaNpk1CA`
   - What to extract: Release dates (monthly drops, Tech Preview Sep 29, GA Dec 22), feature epics per milestone

3. **RHIVOS background on Confluence** - because RHAS builds on top of RHIVOS
   - https://spaces.redhat.com/spaces/Automotive
   - What to extract: RHIVOS architecture (ostree-based in-vehicle OS), how RHAS extends it (developer tooling layer on OCP)

### Afternoon - Hands-on

4. **PitCrew Jira board** - browse the current sprint and epics
   - Board: search for PitCrew in Jira or ask Manuel Sandino/Jeff Ligon for the board link
   - Key epics to skim: PITCREW-337 (QE Readiness), PITCREW-331 (CTC), PITCREW-335 (Konflux), PITCREW-336 (Distribution), PITCREW-334 (RH-SDLC Compliance)
   - What to extract: sprint cadence, active work, who owns what

5. **Join Slack channels** (if not already):
   - `#team-pitcrew-automotive` - primary team channel
   - `#forum-jumpstarter` - technical discussion
   - `#forum-qe-automotive` - automotive QE forum
   - `#team-auto-toolchain-qe` - ATC QE (your current team, but relevant crossover)

---

## Day 2 (Tue) - Architecture: What Does RHAS Actually Ship?

**Goal:** Understand the component architecture - what pieces make up the product and how they fit together.

### Morning - Read

1. **Benny's Testing Architecture Doc** - the team's own view of testable components
   - Google Doc: `1NEzWHE1K4CiGkEDjhL5gpQUpcnepsiBvMDWPXUxLOHQ`
   - What to extract: 3-layer model (Jumpstarter E2E, Builder E2E, black-box integration), kind vs OCP gap

2. **RHAS CI Testing Proposal** - Evgeni and Mohamad's downstream CI design
   - Google Doc: `1Txk4PQC9pGvNrNE9VViN8EMI8o94KpJa_kLMscBthAI`
   - What to extract: Pipeline architecture (install-cluster -> deploy-operators -> run-tests -> destroy-cluster), ephemeral IPI SNO on AWS, 3-phase rollout plan, trigger strategy (nightly), open questions

3. **Component map** - know the parts:

   | Component | What It Does | Upstream Repo |
   |-----------|-------------|---------------|
   | Automotive Image Builder (AIB) / Builder Operator | OCI image builds, bootc images, RPMs, ISOs | centos-automotive-suite/automotive-dev-operator |
   | Jumpstarter | Hardware-in-the-loop test framework, board management | jumpstarter-dev/jumpstarter |
   | Konflux | CI/CD pipeline (Tekton-based), artifact signing | - |
   | GitOps integration | GitLab/GitHub CI connectivity | - |
   | Keycloak / SSO | Authentication, cert management | - |
   | Platform Web Console | Developer UI (Roni Eliezer) | - |

### Afternoon - Hands-on

4. **Look at the actual CI** - get eyes on what's running
   - GitLab RHAS CI: `gitlab.cee.redhat.com/automotive/jumpstarter/rhas-ci` (Evgeni's pipeline)
   - Upstream Builder E2E: `github.com/centos-automotive-suite/automotive-dev-operator/tree/main/test/e2e`
   - Upstream Jumpstarter E2E: `github.com/jumpstarter-dev/jumpstarter`
   - bootc tests: `gitlab.cee.redhat.com/automotive/tests/all`

5. **Clusters** - know where things run:
   - External public cluster: `console-openshift-console.apps.automotive1.ocp.automotive.sig.centos.org`
   - Internal dev cluster (ROSA): `console-openshift-console.apps.rosa.auto-devcluster.bzdx.p3.openshiftapps.com`
   - Request access if needed (Benny or Bella for permissions)

---

## Day 3 (Wed) - Testing Landscape: What Exists Today?

**Goal:** Understand what testing is already happening, what's missing, and where the gaps are.

### Morning - Read

1. **RHAS Testing Landscape Report** (your own report from Jun 30)
   - In agent brain: `agent_brain/projects/rhas-testing-ownership/testing-landscape-report.md`
   - What to extract: Upstream (operational, per-PR) vs Downstream (blocked, WIP), HiL status, QE Readiness gap, risk assessment

2. **RHAS Test Strategy - DRAFT**
   - Google Doc: `1tLAguZTTa6CKif-GBA7mM1N1rDXw3IrrjKo3218Us4U`
   - What to extract: 3-layer architecture, ownership model, timeline, critical actions

3. **RHAS Test Release Criteria - DRAFT**
   - Google Doc: `13wceO7V-q44G9mn2yWN0zYlrAaJOnD7MQBCjPKQc4hM`
   - What to extract: 3-tier progressive gates (Monthly, Tech Preview, GA), measurable thresholds, current evidence status

4. **RHAS Testing Dashboard**
   - Google Drive: "RHAS Testing Dashboard - 2026-07-20" (uploaded Jul 20)
   - What to extract: Visual overview of readiness, criteria status, risk heatmap

### Afternoon - 1:1 Meetings (schedule these)

5. **Evgeni Vakhonin** (30 min) - DS pipeline status
   - Ask: Where is the pipeline now? What's still blocking? When can we expect nightly runs?
   - He's the one building the downstream CI since March

6. **Mohamad Abo Ras** (30 min) - upstream testing coverage
   - Ask: What exactly does the upstream E2E cover? What's the gap between kind tests and OCP? What's the test coverage like?
   - He owns upstream per-PR testing

---

## Day 4 (Thu) - RHIVOS QE Patterns: What Can We Borrow?

**Goal:** Learn from RHIVOS QE (your own team's processes) and cross-product patterns that apply to RHAS.

### Morning - Read

1. **RHIVOS CTC process** - the model RHAS should adapt
   - Confluence: page 196260232 ("RHIVOS ER Release Testing Process")
   - Confluence: page 196285195 ("Pass-Fail Criteria")
   - What to extract: Two-phase CTC (Reduced vs Full ASIL), waiver discipline, Greenwave gating

2. **RHIVOS Gating Process**
   - Confluence: page 387157013 ("RHEL & RHIVOS Gating")
   - What to extract: Gator automation, ResultsDB, tag promotion flow (gate -> candidate -> pending)

3. **Cross-product comparisons** (from Confluence research Jul 20):

   | Product | Key Pattern to Borrow | Page ID |
   |---------|----------------------|---------|
   | RHOAI | TFA (Test Failure Analysis) - 7 categorization labels, Jira automation | 422150347 |
   | RHOAI | Code Freeze Blocker governance - 5-question impact assessment | 418808717 |
   | RHOAI | Component quality gates matrix - per-component sign-off | 304028544 |
   | RHEL 8 | GA Minimal Ship Criteria - measurable thresholds (100% critical, 80% important, 95% customer) | 310813093 |
   | Platform QE | Test Strategy Checklist (21 items) | 279614114 |
   | Platform QE | Release Readiness Checklist (13 items) | 279611662 |

### Afternoon - 1:1 Meetings

4. **Benny Zlotnik** (45 min) - architecture and testing vision
   - Ask: Walk me through the 3-layer testing model. What's the gap between what we have and what we need for Tech Preview? What keeps you up at night about RHAS quality?
   - He's the tech lead with the deepest product knowledge

5. **Miguel Angel Ajo** (30 min) - Jumpstarter and HiL
   - Ask: How does Jumpstarter work? What boards do we have? What's the lab health? How does HiL testing fit into the release cycle?
   - He owns the hardware-in-the-loop infrastructure

---

## Day 5 (Fri) - OCP QE and Strategy: Where Are We Heading?

**Goal:** Understand OCP QE alignment opportunities and start forming your own QE strategy for RHAS.

### Morning - Read

1. **OCP Feature Quality Strategy**
   - Google Doc: `1zuWKi9MvRVyOWn1lj-Khi47TvElUdmGWKRJhTnSVfVg` (Cameron Meadors)
   - What to extract: Four-phase model (Planning, Development, Stabilization, Maintenance), pre-merge vs periodic E2E split, Component Readiness dashboards

2. **OCP QE Jira epics** - know what OCP QE is working on:
   - OCPQE-32074: Define Overall Quality Strategy (Cameron Meadors)
   - OCPQE-32075: Test Case Management (David Kutalek)
   - OCPSTRAT-3352: Revamp Quality Engineering

3. **PITCREW-337** (QE Readiness) - read the epic description carefully
   - This is the ticket you'll likely own. Understand its scope, dependencies (blocked by PITCREW-336 Distribution), and current state (unassigned, no comments)

4. **Features requiring testing** - know your test surface
   - In agent brain: `agent_brain/projects/rhas-testing-ownership/features-requiring-testing.md`
   - 12 testing domains, feature epics by release target through GA

### Afternoon - Synthesis

5. **Write your own 1-page QE priorities doc** - now that you've read everything:
   - What are the top 3 risks for Tech Preview (Sep 29)?
   - What's the minimum viable QE process for monthly releases?
   - What do you need from the PitCrew team vs what you build yourself?
   - Who are your first 3 hires/assignments?

6. **Schedule for next week:**
   - Cameron Meadors (cmeadors@redhat.com) - OCP QE strategy alignment
   - John George - next-gen QE working group
   - Paul Wallrabe - RHAS product direction, customer priorities
   - Jeff Ligon - PO perspective on quality gates

---

## Key People Directory

| Person | Role | Why You Need Them |
|--------|------|-------------------|
| **Benny Zlotnik** | PitCrew tech lead | Deepest RHAS architecture knowledge. Wrote the testing doc |
| **Evgeni Vakhonin** | RHAS CI engineer | Building the downstream pipeline. Your primary CI contact |
| **Mohamad Abo Ras** | E2E upstream testing | Owns upstream per-PR tests. Knows test coverage |
| **Miguel Angel Ajo** | Jumpstarter lead | HiL infrastructure, board management, lab ops |
| **Martin Perina** | bootc testing | bootc test development, Jumpstarter integration |
| **Bella Khizgiyaev** | PitCrew engineer | Konflux, CTC, demos. Good for broad context |
| **Eitan Raviv** | ATC infra | AWS IAM, DNS for RHAS-CI cluster (you already know him) |
| **Rachel Sibley** | RHIVOS QE coordinator | CTC scheduling, waiver process. Model for RHAS QE |
| **Cameron Meadors** | OCP QE strategy | OCP quality strategy owner. Alignment contact |
| **Paul Wallrabe** | Engineering Director | Strategic direction, customer priorities |
| **Jeff Ligon** | Product Owner | PO perspective, feature priorities, what customers need tested |

---

## Key Resources Bookmark List

### Google Docs
- RHAS Strategic Guide: `10qaHs_mfOCJtIJoJq35HjhHAeLEMJwYde51wgCKrQx8`
- RHAS 2026 Roadmap: `1j4Chcv71S8Y3P8HT2wTao9ZEoHoHm-X102VmaNpk1CA`
- Benny's Testing Architecture: `1NEzWHE1K4CiGkEDjhL5gpQUpcnepsiBvMDWPXUxLOHQ`
- RHAS CI Testing Proposal: `1Txk4PQC9pGvNrNE9VViN8EMI8o94KpJa_kLMscBthAI`
- RHAS Test Strategy (DRAFT): `1tLAguZTTa6CKif-GBA7mM1N1rDXw3IrrjKo3218Us4U`
- RHAS Test Release Criteria (DRAFT): `13wceO7V-q44G9mn2yWN0zYlrAaJOnD7MQBCjPKQc4hM`
- RHAS Testing Landscape: `19T2hFTrEhnGpgVjFvuyUXQPiRk_p3j6VAHAQQGAX7mI`
- OCP Feature Quality Strategy: `1zuWKi9MvRVyOWn1lj-Khi47TvElUdmGWKRJhTnSVfVg`
- Hubert's Onboarding Plan (reference): `1G-iqrNyzqijEXdRqV3gscl6uxHwmnSKTjthlf3BJ44A`

### Test Infrastructure
- Test Console: `test-console.corp.redhat.com/rhivos-testing/ctc`
- Jumpstarter monitor: `monitor.ajo.es/status/jumpstarter`
- RHAS CI GitLab: `gitlab.cee.redhat.com/automotive/jumpstarter/rhas-ci`
- Prow CI: `prow.ci.openshift.org`
- Sippy (Component Readiness): `sippy-auth.dptools.openshift.org`

### Confluence
- RHIVOS home: https://spaces.redhat.com/spaces/Automotive
- RHIVOS Release Testing Process: page 196260232
- RHIVOS Pass-Fail Criteria: page 196285195
- RHEL & RHIVOS Gating: page 387157013

### Slack Channels
- `#team-pitcrew-automotive` - team channel
- `#forum-jumpstarter` - technical
- `#forum-qe-automotive` - automotive QE
- `#forum-openshift-qe` - OCP QE
- `#wg-openshift-next-gen-quality` - next-gen QE working group

### Jira
- PITCREW-337 - QE Readiness (the epic you'll own)
- PITCREW-331 - CTC adoption
- PITCREW-393/394 - DS testing pipeline
- PITCREW-335 - Konflux onboarding
- PITCREW-336 - Distribution (blocks QE Readiness)
- PITCREW-42 - Original QE plan

---

## What Success Looks Like After This Week

By Friday you should be able to:

1. **Explain RHAS** to someone who's never heard of it - what it is, who it's for, how it differs from RHIVOS
2. **Draw the component architecture** - Builder, Jumpstarter, Konflux, GitOps, Keycloak, Console - and how they connect
3. **Describe the current testing state** - what's operational (upstream per-PR, HiL), what's blocked (DS pipeline), what doesn't exist (QE process, release criteria)
4. **Name the top 3 risks** for Tech Preview and have an opinion on mitigation
5. **Know every key person** by name and what they do
6. **Have a draft priority list** for your first 30 days as QE lead
