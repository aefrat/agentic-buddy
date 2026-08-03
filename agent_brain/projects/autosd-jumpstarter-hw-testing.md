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

### Source: Juanje (Jan 14, 2026)

In #team-toolchain-automotive, Brian Grech asked "Can anyone here tell me where AutoSD images are tested?" Juanje replied:

> "Which images exactly? We test the qemu images in Testing Farm in VMs, but we don't test the board ones for AutoSD, we don't have access from the upstream pipeline to the boards."

Brian confirmed he was wondering about Ride4 specifically.

### Source: #team-cats-automotive thread (Jul 31, 2026)

Sandro Bonazzola reported ETAS having trouble booting AutoSD10 daily image on SA8650P (AVB hash mismatch - turned out to be an ABL firmware issue, not an image issue). This triggered the critical exchange:

- **Hubert:** "The nightly smoke tests passed... Are SA8650P covered in those?"
- **Ozan:** "This is for upstream, right? We are not doing board testing for upstream. Only the VMs are tested for AutoSD."
- **Paul Wallrabe:** "i would love to see those tests being executed on real hardware especially since the lab is not really maxed out in terms of capacity."
- **Hubert:** "Ah.. but TC isn't accessible upstream - it's an internal-only service, which complicates things"
- **Hubert:** "The other option is to use jmp directly for nightlies"
- **Ozan:** "We have an issue for the same kernel-automotive-6.12.0-251.el10iv version for Ride4 boards in downstream. Since AutoSD is not tested on real HW, probably we missed this failure."
- **Paul:** "exactly, jmp should be accessible"

### Technical blocker analysis

The thread reveals **two distinct systems and the gap between them:**

1. **Testing Farm** - used by the upstream GitLab CI pipeline to run QEMU VM tests. Handles virtual testing only.
2. **Test Console (TC)** - the internal service that runs smoke tests on real hardware for RHIVOS downstream. Hubert asked "is TC running those tests? I know it does for RHIVOS" - confirming TC is what drives board-level testing in the downstream pipeline. **TC is internal-only and not accessible from upstream.** This is the actual limitation Hubert identified.
3. **Jumpstarter (jmp)** - publicly accessible board management platform. Hubert immediately proposed it as the alternative: "The other option is to use jmp directly for nightlies." Paul confirmed: "exactly, jmp should be accessible."

So the situation is: upstream uses Testing Farm (VM-only), downstream uses Test Console (real HW but internal-only). Jumpstarter is the path that bridges this - it manages the same physical boards but is publicly reachable, so the upstream pipeline can call it directly without needing TC access.

**Demonstrated cost:** kernel-automotive-6.12.0-251 issue on Ride4 boards was only caught downstream, breaking the RHIVOS 2.1 nightly (disk_full during kernel module signing - broken msm_hab.ko inflated to 2.6GB). The SA8650P/ETAS issue in the same thread turned out to be ABL firmware (not an image bug), but it surfaced the testing gap discussion.

## Key points from Paul's reply (Aug 3)

1. **No Testing Farm needed.** Jumpstarter endpoint is public - upstream pipeline can reach it directly.
2. **Catch failures upstream.** "If a test can run in both RHIVOS and CentOS, why not test in CentOS?" Philosophy: test at the highest (closest to upstream) level possible.
3. **Resource starvation not a concern.** Lab is not 100% utilized. High-demand boards exist but overall no need to expand.
4. **Strong view against pool sharding.** Everything should go in one shared pool with best-effort serving. Long-term solution: associate cost per lease time unit. More sharding = less synergy = more hardware = higher cost. Quotas as middleground acceptable, but Paul would revert the whole idea of dedicated device pools if it were only his decision.
5. **Start with any board.** TI is essentially unused - adding tests there is a no-op for the cluster. (Avi had suggested QC Ride4 first given the recent miss.)

## Open discussion thread (Aug 4)

Avi opened a discussion in #team-toolchain-automotive ([thread](https://redhat-internal.slack.com/archives/C04JDFLHJN6/p1785752888798369)). Tagged Juanje, Ozan, Roni. Questions posed:

1. What is currently stopping us from running smoke tests for AutoSD upstream?
2. Can we use Test Console for upstream images (PAC), not just downstream (DPAC)?

**Awaiting answers.** Update this section once replies come in.

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
