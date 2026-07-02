---
last_accessed: 2026-07-02
access_count: 0
created: 2026-07-02
---

# RHIVOS Testing Patterns - Reference for RHAS QE

Patterns, infrastructure, and processes from RHIVOS QE that RHAS can learn from or reuse.

## Confidence Test Cycle (CTC)

Two-phase approach:

1. **Reduced CTC** - smoke tests, kernel gating, systemd, a-b-c on SA8650/8775/QEMU
2. **Full ASIL Release CTC** - comprehensive validation for release candidates

Key roles:
- Rachel Sibley coordinates QE/CTC scheduling
- Stephen Bertram makes waiver decisions via Greenwave/WaiverDB

## Release Pipeline

Sequential stages:

```
generate-compose -> check-repoclosure -> build-image (per board) -> smoke-tests -> promote-packages-in-brew
```

Tag flow:

```
-gate -> Greenwave -> ResultsDB -> -candidate -> compose -> -pending
```

- Gator automates Greenwave policy evaluation
- Waiving via WaiverDB requires all failures to have BTS links (no silent waivers)

## Nightly Pipelines

Two nightly builds:
- `latest-RHIVOS-2.0-Core`
- `latest-RHIVOS-2.0`

Nightly test coverage:
- Smoke tests
- Board provisioning
- Kernel gating

Known recurring issues:
- Unsigned packages from ODCS
- Board timeout failures
- Jumpstarter provisioning failures (transient)

## Hardware-in-the-Loop (HiL) Testing

Architecture:

```
ROSA cluster -> Jumpstarter controller -> Physical boards
```

Supported boards:
- Qualcomm: SA8650, SA8775, SA8979, SA8255
- NXP: S32N79, iMX8
- Renesas: R-Car X5H

Lab health (Jun 23 snapshot): 55 PASS, 4 FAIL, 6 XFAIL

Known flaky issue: PITCREW-403 "Connection to exporter lost"

Lab maintenance is automated - boards are provisioned and health-checked on a recurring basis.

## Test Infrastructure

| Tool | Purpose |
|------|---------|
| Test Console (test-console.corp.redhat.com) | Central test result dashboard |
| Testing Farm | VM-based test execution |
| Jumpstarter | Hardware-in-the-loop test execution |
| GitHub Actions + Packit | Upstream PR testing |
| GitLab CEE | bootc test execution |

## Patterns Worth Adopting for RHAS

1. **Gated promotion with Greenwave** - automated policy evaluation before tag promotion. Removes human bottleneck from go/no-go decisions.

2. **Nightly pipeline with known-issue tracking** - nightly builds catch regressions early. Known issues are tracked explicitly rather than silently waived.

3. **HiL automation via Jumpstarter** - physical board testing without manual intervention. RHAS can reuse this for RHAS-specific hardware validation.

4. **Two-phase CTC** - reduced CTC for fast feedback, full CTC for release confidence. RHAS could adopt a similar reduced/full split for its own test cycles.

5. **WaiverDB discipline** - all waivers require BTS links. Prevents "waive and forget" anti-pattern.
