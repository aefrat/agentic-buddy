---
last_accessed: 2026-07-23
access_count: 1
created: 2026-07-23
---

# RHIVOS Physical AI - Project Context

## Overview

**RHIVOS+** is an extension of RHIVOS positioning Red Hat as a certified governance platform for **Physical AI** - AI agents that control physical systems in non-automotive markets (robotics, drones, industrial automation, energy systems).

Core thesis: agentic workloads are non-deterministic and untrusted by default. Application-level guardrails are insufficient - governance must be enforced at the OS level, at a privilege boundary the agent cannot cross.

## Jira

- **AUTOBU-1108** - "Establish RHIVOS as the certified governance platform for Physical AI in non-automotive markets"
  - Type: Outcome (hierarchy level 3)
  - Status: New (as of 2026-07-23)
  - Created: 2026-07-17 by Gadi Glogowski
  - No child tickets, no assignee yet
  - Effect: Growth (new markets)

## Architecture - Three-Layer Defense Model

1. **RHIVOS+ (Software Layer)** - Containment (kernel isolation via namespaces, cgroups, seccomp, LSMs), Governance (NVIDIA OpenShell agent sandboxing), Validation (Sense-Plan-Validate-Act architecture - untrusted plans never reach actuators without validation)
2. **Safety Controller (Certified Hardware)** - Dedicated MCU/ECU independent of AI software. Per-actuator current/torque/force limits, E-stop circuits, hardware watchdogs. Certified to ISO 26262 / IEC 61508 / ISO 13482
3. **Physical System (Physics)** - Motor torque limits, mechanical stops, crush zones, breakaway mechanisms, fuses. Physics as final enforcer

Key NVIDIA partnership: **OpenShell** is a joint Red Hat/NVIDIA collaboration for agent sandboxing (GitHub: NVIDIA/OpenShell). Four policy layers: Filesystem, Network, Process, Inference.

## Roadmap (from RHIVOS 2.x Planning spreadsheet)

All features under AUTOBU-1108, all MustHave priority. "JF" (Jaime Flynn) owns timeline proposals.

| Phase | Feature | Target |
|-------|---------|--------|
| HW | Enable non-automotive platforms (Jetson Thor/Orin, Intel Panther Lake, Qualcomm IoT, NXP i.MX8/9, TI) | TBD (automotive HW first) |
| Concept | Define AI governance stack (three-layer architecture) | Q3 2026 |
| Phase 1 | Prototype RHIVOS + OpenShell integration + Eclipse working groups + thought leadership | Q4 2026 / Q1 2027 |
| Phase 2 | Open source domain-specific safety policy engine (automotive, robotics, drones, industrial) | TBD (needs requirements clarity) |
| Phase 3 | Certified end-to-end AI governance stack | TBD (needs requirements clarity) |

## Target Markets and Use Cases

- **Autonomous forklifts** - warehouse/logistics (force, speed, zone limits)
- **In-vehicle voice assistants** - vehicle API access without actuator control
- **Drone fleet management** - geofencing, altitude limits, no-fly zones
- **Robotic arms in manufacturing** - torque and force envelopes
- **Quality/production control** - on-prem physical AI with cameras (Xantara/Fertig Motors SSA engagement)

## Key People and Teams

- **Gadi Glogowski** - created AUTOBU-1108
- **Jaime Flynn** - owns timeline proposals, shared the RHIVOS+ deck
- **Chris Custine** - Ecosystems Engineering, posts weekly Physical AI team status to #physical-ai-use-cases
- **Luis Arizmendi** - Published two-part Red Hat blog series on Physical AI, active in #wg-edge-robotics
- **saypaul** - Training/deploying Unitree G1 humanoid in sim, building ROS2 on Fedora, creating robotics dev toolbox
- **fzdarsky** - Coordinating with saypaul on toolbox/demo
- **Luke Thompson** - Shared architecture decks in #rockwell-team

## Key Resources

- Presentation: [RHIVOS+ Physical AI: On Device Agent Management](https://docs.google.com/presentation/d/16jAwHKNJqFGpke8hkYkSDCjtE004vVaOMMZ1UBZsqFs/edit)
- Planning spreadsheet: [RHIVOS 2.x Planning](https://docs.google.com/spreadsheets/d/1H7YviNZhrjn56_7pvs6_3xAa_gyTy9d2J5Iza4rQ2gA/edit?gid=83628794)
- Chris Custine's team status: [Physical AI Team Status - Rolling](https://docs.google.com/document/d/12SgM5etROj2VAL61wx8__fzW-qUXvdbnV9HYvKdhqtI/edit)
- Blog Part 1: [Physical AI: physical operations are broken](https://www.redhat.com/en/blog/physical-ai-physical-operations-are-broken-new-kind-intelligence-needed)
- Blog Part 2 draft: [When machines start to think and act](https://docs.google.com/document/d/1c37MmT_BJePFyr58-u2ZzwrgNTcURTvnw4pLKez-JXA/edit)
- Luke Thompson architecture decks in #rockwell-team
- Slack channels: #physical-ai-use-cases, #wg-edge-robotics, #forum-ai, #beyond-autoregressive-llms

## Observations

- Very early stage - Outcome created Jul 17, no child tickets or assignees yet
- NVIDIA partnership is central (OpenShell, Cosmos consortium, Japan market push)
- Multiple Red Hat teams already active (ecosystems eng, edge robotics WG, research/sim, SSA field)
- Cross-certification play spans ISO 26262 (automotive), IEC 61508 (industrial), ISO 13482 (robotics)
- Builds on existing RHIVOS strengths: ISO 26262 ASIL-B certified Linux, mixed-criticality container isolation, PREEMPT_RT
- AUTOBU-1108 not mentioned on Slack at all - discussion uses "Physical AI" terminology
