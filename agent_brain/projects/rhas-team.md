---
last_accessed: 2026-07-28
access_count: 1
created: 2026-06-23
---

# RHAS — Red Hat Automotive Solutions

PitCrew team's product engineering work on RHAS (Automotive Development Platform, Builder, Jumpstarter, bringup agent). Distinct from [AIIL demo](aiil-demo-rhas.md) (Michael Kuehl's concept) and [PitCrew strategic context](pitcrew-strategic-context.md) (roadmap cache).

## Key areas

- **Bringup agent** — CAIB + Jumpstarter integration for automated board bring-up. Bruce Benson lead.
- **Jumpstarter** — Hardware-in-the-loop testing framework. Miguel Angel Ajo Pelayo lead.
- **QC hardware enablement** — Snapdragon 8650, 8979, 8255 board support.
- **RHAS releases** — Monthly `RHAS-MMYY` cadence. TP target Sep 29, GA target Dec 22.

## Key activity

- **2026-07-28 (Slack):** QC 8650 boards 03, 06, 10 hit fastboot detection failures - Benny recovering. New ABL reported to cause locked devices to become unbootable (pagranat, #forum-jumpstarter). ExporterSet controller sidecar mechanism (PITCREW-487) and QEMU provisioner (PITCREW-477) moved to Review (Miguel).
- **2026-06-23 (Slack):** Bruce Benson shared updated bringup agent integrating CAIB and Jumpstarter functionality — committed during RHAS program meeting. Sergei reported QC 8650 board flashing issue with RHIVOS 2.0-Core TP RC1 (26 replies, workaround applied). (#team-pitcrew-automotive, #forum-jumpstarter)

## Slack channels

- `#team-pitcrew-automotive` — primary team channel
- `#forum-jumpstarter` — Jumpstarter cross-team discussions

## People

- **Bruce Benson** — bringup agent development
- **Sergei** — QC hardware bring-up, board testing
- **Miguel Angel Ajo Pelayo** — Jumpstarter lead
- **Shawn Davis** — RHAS program lead

> Related: [PitCrew strategic context](pitcrew-strategic-context.md) — roadmap and tiers. [AIIL demo](aiil-demo-rhas.md) — Michael Kuehl's closed-loop HIL concept (uses RHAS stack but is a separate initiative).
