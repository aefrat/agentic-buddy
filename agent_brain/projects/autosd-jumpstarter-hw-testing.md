---
last_accessed: 2026-08-03
access_count: 1
created: 2026-08-03
---

# AutoSD Upstream HW Testing on Jumpstarter

## Status

**Active.** Paul Wallrabe proposed, Avi agreed, discussion ongoing. Topic added to ATC open sync this week.

## Context

Paul Wallrabe (PM, RHAS/Jumpstarter) reached out to Avi (Aug 2-3) asking if it makes sense to run AutoSD nightly tests on Jumpstarter directly. Prompted by Ozan's Slack post about kernel-automotive-6.12.0-251 failing on Ride4 boards - caught only downstream because AutoSD has no real HW testing. Hubert recommended Paul talk to Avi.

## The gap

AutoSD upstream nightly pipeline (GitLab CI via Testing Farm) builds images for all board variants (QC, Renesas, TI, NXP, QEMU) but only tests on QEMU VMs. No network path from upstream CI to the Jumpstarter board cluster. Not a deliberate decision - never wired up.

**Demonstrated cost:** kernel-automotive-6.12.0-251 issue on Ride4 boards was only caught downstream, breaking the RHIVOS 2.1 nightly (disk_full during kernel module signing - broken msm_hab.ko inflated to 2.6GB).

## Key points from Paul's reply (Aug 3)

1. **No Testing Farm needed.** Jumpstarter endpoint is public - upstream pipeline can reach it directly.
2. **Catch failures upstream.** "If a test can run in both RHIVOS and CentOS, why not test in CentOS?" Philosophy: test at the highest (closest to upstream) level possible.
3. **Resource starvation not a concern.** Lab is not 100% utilized. High-demand boards exist but overall no need to expand.
4. **Strong view against pool sharding.** Everything should go in one shared pool with best-effort serving. Long-term solution: associate cost per lease time unit. More sharding = less synergy = more hardware = higher cost. Quotas as middleground acceptable, but Paul would revert the whole idea of dedicated device pools if it were only his decision.
5. **Start with any board.** TI is essentially unused - adding tests there is a no-op for the cluster. (Avi had suggested QC Ride4 first given the recent miss.)

## Agreed next steps

- Topic added to this week's ATC open sync.
- Need to figure out: technical integration, which boards, who owns the integration.
- Paul's position simplifies several concerns from Avi's original analysis (no Testing Farm integration needed, no capacity worry, start anywhere).

## People

- **Paul Wallrabe** - PM for RHAS/Jumpstarter. Initiated the question. Strong opinions on shared infrastructure.
- **Ozan Unsal** - Flagged the gap (Jul 31, #team-cats-automotive). Owns pac-jobs/pipeline.
- **Hubert Stefanski** - Recommended Paul talk to Avi. AutoSD/CloudFront fork maintainer. Transitioning to PitCrew.
- **Miguel Angel Ajo Pelayo / Benny Zlotnik** - Jumpstarter team.
- **Juanje Ojeda** - Confirmed upstream pipeline has no board access.

## Related

- RHIVOS 2.0 Retro: Luigi's Testing Farm to Jumpstarter switch highlighted as success.
- Research log: `logs/2026-08-02.md` (session 1).
