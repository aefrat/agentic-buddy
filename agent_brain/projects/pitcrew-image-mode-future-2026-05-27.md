---
last_accessed: 2026-05-31
access_count: 1
created: 2026-05-31
---

# PitCrew: The Future of Image Mode — 2026-05-27

**Meeting type:** PitCrew (cross-BU technical discussion)
**Organizer:** Jeff Ligon (PO, developer cluster, automotive)
**Avi's status:** Missed — captured from transcript + Gemini notes 2026-05-31

## Attendees

- Jeff Ligon — PO, automotive developer cluster (meeting host)
- Matt Micene — RHEL technical marketing
- Micah Abbott — Engineering manager, RHEL for Edge
- Ian McLeod — Architect, automotive program
- Luke Thompson — Edge portfolio product manager
- Andy Burka — Engineer
- Robert Sturla — Fedora Atomic / Universal Blue
- Sean O'Keeffe — PM, Edge Manager
- Dusty Mabe — Fedora / CoreOS

## Why the meeting existed

Jeff Ligon triggered it after Summit by noting:
1. Both automotive and edge were asking "when do we get Zstandard Chunked for faster container pulls on edge devices?" — it exists in Fedora but not RHEL.
2. He wanted to collect the broader list of what's broken or missing in image mode before proposing making Bootc the default for RHEL 11.

---

## Topics discussed

### 1. Zstandard Chunked — missing from RHEL

Both automotive and edge need it. Exists in Fedora. Jeff is working to get it "plumbed through" to RHEL so it can be put in front of customers. No decision; still an open item.

### 2. Developer experience — the core gap (Ian McLeod, Jeff Ligon)

Image mode is excellent as a **deployment model** (golden image, consistent fleet, OTA updates) but fails as a **development model**:
- Can't easily install packages interactively
- Config goes in unexpected places
- No clean story for how to "unhook" an image to develop on it

Ian McLeod framed it as two distinct needs:
- **Deploy path:** Image mode is good. Solid for automotive/edge fleet management.
- **Develop path:** Currently muddled. Customers who engage want to develop, not deploy first.

Jeff's quick-and-dirty idea: Delete the OS tree directory from a Bootc image → you get back to a package-mode system. Proposed making this the default install path for RHEL 11 (Anaconda installs from a container registry, then strips the OS tree bits → package-based system usable as normal).

### 3. Pre-built images — strong consensus

Micah Abbott, Luke Thompson, Ian McLeod all pushed for more pre-built images as a starting point:
- Luke: 6 pre-built images would cover ~80% of edge customer requests (HMI, kiosks, industrial plant floors, deterministic workloads, retail).
- Jeff: automotive has the same problem — each ARM board needs specific tuning; universal images haven't worked yet but they're getting there.
- Reference model: **Universal Blue** (Bluefin, etc.) — here's a pre-built opinionated image, play with it, then build your own.
- Ian's qualifier: the pre-built image must be one users can **interactively modify and rebuild**, not a static artifact.
- Andy Burka's counter: pre-built images accelerate *time to discovery* but don't solve the developer experience confusion.

**Tension:** Pre-built images create support burden. Current answer has been "no". Matt Micene argued: right now we're not meeting the market need, which means it goes to competitors. Support work is the upside problem.

### 4. Anaconda + Bootc graphical installer

Luke Thompson surfaced an existing RFE: install image-mode RHEL via the Anaconda graphical installer — same UX as today but pulls from a container registry instead of an RPM repo.

Jeff: Justin Cheryl (PO image mode) already built a container that enables this. Question: why isn't it prioritized?

**Next step:** Jeff to document this use case and investigate blockers with the Anaconda team.

### 5. Staged / canary deployments (Robert Sturla, Matt Micene, Dusty Mabe)

Pain point for Fedora Atomic, Universal Blue, and enterprise customers:
- No easy way to roll out to a subset of devices, gather feedback, then proceed.
- Only option is Ansible-based improvisation — no first-class canary tooling.
- Historical reference: **Zincotti** (Fedora CoreOS update mechanism) had rollout pools and timing controls. The CoreOS team can advise.

Matt Micene: this is both an internal need (for RHIVOS/image mode teams themselves) and a customer need. Connected to hardware lab segmentation Jeff mentioned (CI/CD testing pool vs. kernel dev pool).

Jeff's mention of RHEL Edge Manager as a possible solution for fleet segmentation.

**Matt stopped short of going further on autonomous updates — said to ask him offline.**

### 6. Tool integration warning (Andy Burka)

Explicit caution: avoid creating siloed, sequestered deployment tools for edge/automotive. Prior iteration of edge management failed because the inventory/tooling wasn't co-located with AAP/ACM. Don't repeat this. Any new canary/rollout tooling should integrate with Satellite, Ansible, ACM rather than standing alone.

### 7. Satellite OCI registry — undercommuicated capability (Sean O'Keeffe)

Satellite already has an OCI registry (running Pulp) that can push/pull container images. This was news to Jeff and likely many others. Large RHEL customers already use Satellite to define what their RHEL estate looks like (packages, policies, CrowdStrike inclusion, etc.). They want that definition in *one place*, not split between package mode and image mode.

Sean committed to sharing a management deck covering how RHEL + Satellite + Ansible should work together in the image mode era.

### 8. Image Builder as "front door" strategy — status check (Matt Micene)

Image Builder was positioned as the front door to RHEL for all customers. Problems encountered:
- Hosted vs. non-hosted Image Builder diverged in functionality.
- Doesn't help with Anaconda-based installs (traditional workflow).
- Created siloed experiences that "look like they should work together but don't quite."

The current push is to fix this: unify Image Builder and push image mode as the default RHEL experience.

### 9. Bootc as default for RHEL 11 — the main strategic question

**Scott McCarty has a RABU item:** Bootc by default for RHEL 11.

He doesn't yet have a concrete work list for what that means. Jeff is collecting that list.

**Dusty Mabe's recommendation:**
1. Start with Fedora. The community will surface everything that sucks — but only if you *actually promote* it (not just leave it in a corner).
2. Engage early and publicly: state the intention and direction even without a timeline.
3. Easy switch back: if the default install is image mode, there must be a simple command to revert to package mode or people will revolt.
4. Don't repeat the Hummingbird announcement failure (Scott McCarty emailed Fedora Devel 2 weeks before Summit announcing Hummingbird — felt decided, not community-driven).

Matt Micene: image mode as default is the right direction but there are "pretty big pitfalls" in the onboarding experience today that need to be fixed first.

### 10. CoreOS + Bootc unification — stalled working group

Dusty Mabe mentioned a working group from last year exploring how CoreOS and Bootc could collaborate or merge. It stalled. He thinks it's worth revisiting.

### 11. ELN build of Bootc (Jeff Ligon)

Jeff is co-maintaining an ELN (Extra Packages for Enterprise Linux Next) build of Bootc with Steven Gallagher. Primary goal: get Bootc into Fedora and ELN as the delivery mechanism for Anaconda. Neil (GMPA) is interested if it works as an Anaconda delivery mechanism.

---

## Decisions

| Decision | Status |
|---|---|
| Pre-built images as strategy to reduce onboarding friction | **ALIGNED** |
| Validate Bootc in Fedora before defaulting RHEL 11 | **ALIGNED** (Dusty's rec, no pushback) |
| Bootc as default for RHEL 11 is the target direction | **ALIGNED** (work list TBD) |

---

## Next steps (as captured in meeting notes)

- **[Jeff Ligon]** Document Anaconda BootC installation use case in product requirements
- **[Matt Micene]** Investigate and unblock template Bootc image creation for Edge team
- **[Jeff Ligon]** Follow up offline on autonomous update mechanisms for automotive rail
- **[Sean O'Keeffe]** Share management deck (RHEL + Satellite + Ansible integration)
- **[Sean O'Keeffe]** Schedule follow-up discussion on product roadmaps and identified gaps
- **[Jeff Ligon]** Create comprehensive task list for "bootc as default for RHEL 11"

---

## Impact on RHIVOS and RHAS

### What directly affects RHIVOS

**1. Zstandard Chunked gap**
Jeff explicitly flagged this as a priority for automotive (alongside edge). RHIVOS is an automotive Linux product; faster container pulls on edge/vehicle hardware is a direct requirement. This is blocked on RHEL getting it from Fedora. Jeff is actively working on it.

**2. Developer experience — critical failure mode for RHIVOS OEM engagement**
Ian McLeod (automotive architect) explicitly said: the moment they engage with genuine OEM customers, they need a system those customers can *develop on*, not just deploy. RHIVOS's image mode is good for deployment but fails for interactive development. This is a barrier to converting demos into paying customers. The "unhook for development" story needs to be concrete — currently it's muddled.

**3. Pre-built RHIVOS images for automotive customers**
Jeff noted automotive has the same ARM board fragmentation problem as edge (each board needs specific tickling). Pre-built images per board/use-case are needed. The Universal Blue model (here's an opinionated base, go modify it) is the reference. This hasn't been delivered for automotive yet.

**4. Canary/staged deployments — automotive has higher stakes than edge**
You can't push an unchecked update to a fleet of vehicles the way you might push to a server fleet. The staged update gap is critical for automotive. No current first-class tooling. RHEL Edge Manager is a candidate solution for fleet segmentation. Jeff referenced this for the hardware lab use case, but it maps directly to OEM fleet management needs.

**5. Bootc as default for RHEL 11**
RHIVOS is already bootc-based. If RHEL 11 ships bootc-by-default with a good developer story and pre-built images, the ecosystem around RHIVOS's foundation gets stronger. The inverse is also true: if the RHEL 11 bootc default ships with the current gaps, automotive OEM customers who encounter it will have a bad experience and associate it with RHIVOS.

**6. Satellite OCI registry under-utilization**
If RHIVOS fleet management eventually involves Satellite (as large RHEL customers already use it), the OCI registry capability in Satellite is already there — just not communicated. The Sean O'Keeffe management deck will be relevant to RHIVOS fleet operations.

**7. Tool integration risk**
Andy Burka's caution is directly relevant: any automotive-specific deployment tooling built for RHIVOS should integrate with Ansible/Satellite/ACM rather than standing alone. The prior edge management failure is the cautionary tale.

**8. CoreOS + Bootc unification**
If this working group reconvenes and produces results, it could affect RHIVOS's OS foundation (CoreOS tooling + Bootc capabilities merged). Worth monitoring.

### What does NOT yet directly affect RHIVOS

- The ELN build of Bootc / Anaconda graphical installer is upstream/community work — indirect benefit to RHIVOS but not a direct dependency
- The Fedora community validation approach for Bootc-as-default — this is RHEL 11 scope; RHIVOS is already past this decision

---

## References

- [Meeting transcript (Google Doc)](https://docs.google.com/document/d/1i55InS-Z8I0vhocqhNgZjWd1ZeBGe-MB6qfbSyTh6as/edit?tab=t.ed1gxebsco09)
- [Meeting Gemini notes (Google Doc)](https://docs.google.com/document/d/1i55InS-Z8I0vhocqhNgZjWd1ZeBGe-MB6qfbSyTh6as/edit?tab=t.9xrwukbcevtk)
- Related: [[rhivos-release-approach]] — the layered product / Bootc infrastructure work in parallel
