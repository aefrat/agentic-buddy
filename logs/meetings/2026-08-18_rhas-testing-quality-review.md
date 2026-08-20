---
date: 2026-08-18
type: meeting
topic: RHAS testing/Quality review
attendees:
  - Avihai Efrat
  - Pablo Ridolfi
  - Rachel Sibley
  - Benny Zlotnik
  - Mohamad Abo Ras
  - Miguel Angel Ajo
  - Paul Wallrabe
duration: ~30 min
sources:
  transcript: https://docs.google.com/document/d/1tLn_rLT1GnYGj3sTvxGtDgUDZSr2lXNe7jd_MgeCye8/edit?tab=t.2nf1xnvizskw
  gemini_notes: https://docs.google.com/document/d/1tLn_rLT1GnYGj3sTvxGtDgUDZSr2lXNe7jd_MgeCye8/edit?tab=t.pbgvt2hxt7
  recording: https://drive.google.com/file/d/18Nt6KErRQmX2lp1o0NR3I3G4FuX9l5Ug/view
---

# RHAS Testing/Quality Review - Aug 18, 2026

## Context

Two upcoming RHAS releases: Tech Preview (end of September) and GA (end of December). Meeting objective: review current testing, get experienced eyes (Pablo Ridolfi, Rachel Sibley) to identify gaps.

## Current state

- Ephemeral cluster established end of July for testing automotive dev operator with JumpStarter.
- One downstream test working: building image and flashing.
- All other existing tests (e2e, operator, smoke) are upstream only, running on GitHub workflows.
- No integration tests between automotive dev operator and JumpStarter yet.
- No downstream product bits exist yet - team is testing upstream code against JumpStarter.

## Infrastructure roadmap (Mohamad Abo Ras, 3 phases)

1. **Phase 1 (current):** At least one test running on ephemeral cluster (building + flashing).
2. **Phase 2:** Install JumpStarter in the same cluster - everything in one place.
3. **Phase 3:** Run all upstream testing on the cluster (future/advanced).

## Decisions

1. **Mock devices for integration testing.** Integration testing between automotive dev operator and JumpStarter will use mock devices or QEMU to avoid needing physical hardware in the testing cluster. Proposed by Miguel Angel Ajo, agreed by team.
2. **Downstream testing deferred until bits available.** Paul Wallrabe: defer downstream testing until downstream artifacts exist before GA. Most value right now is upstream testing.

## Hardware strategy

- Need to identify hardware targets for GA: Qualcomm, NXP, TI.
- A single TI board covers multiple EBBR/U-boot drivers (3 types with one board).
- Approach: start with one variant, scale to full matrix gradually.
- For GA: must provide formal evidence on actual hardware platforms customers will use (Pablo's requirement).

## QE requirements (Pablo Ridolfi, Rachel Sibley)

- **Pablo:** Requested formal test list with entry/exit criteria and specific test descriptions. For GA, need formal evidence of testing on VMs and actual hardware targets.
- **Rachel:** Recommended organizing in Jira - features as epics and stories for traceability. Standard process: validate feature-complete code at Tech Preview through CTC, re-run for GA. All test cases and results documented in Polarion. Need a specific release in Jira for Tech Preview - talk to Whitney about that.
- Both stressed the need for formalized, traceable documentation beyond just running tests.

## Action items

1. **[Mohamad Abo Ras]** Compile and share list of current tests (for TP and GA) with Pablo, Rachel, and team - serves as baseline for formalizing test strategy.
2. **[Team]** Map features to Jira - identify and document all features/functionality planned for Tech Preview and GA releases.
3. **[Miguel Angel Ajo]** Evaluate and implement mock devices for integration testing between automotive dev operator and JumpStarter.

## Key takeaways

- Gap between upstream testing reality and downstream QE requirements is significant - no downstream bits, no formal test list, no Jira feature mapping, no Polarion test cases.
- Tech Preview (Sep) will rely on upstream testing with current infrastructure.
- GA (Dec) requires downstream bits, formal CTC evidence, hardware-specific testing, and Polarion documentation.
- Rachel and Pablo offered to have follow-up meetings to share RHIVOS QE processes in more detail.
