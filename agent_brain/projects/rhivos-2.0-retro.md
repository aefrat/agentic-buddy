---
last_accessed: 2026-07-30
access_count: 2
created: 2026-07-30
---

# RHIVOS 2.0 Retrospective

## Context

Retro meeting for RHIVOS 2.0 release, organized by David Walker (dawalker). For POs and Tech Leads. Meeting: 2026-07-30 17:00 IDT (58 minutes).

**Source doc:** [RHIVOS 2.0 Retro](https://docs.google.com/document/d/17q7g2rd3-JvBy7jHn3Py85fqAPmYvN0Wwxe-uNIs7FI/edit)
**Transcript:** [Meeting transcript](https://docs.google.com/document/d/1DjzZOkaYddX0X2_tMkIOGxBW8iDDX7pte1QcIx3st2o/edit)

## Attendees (actual)

Alex McLeod, Avihai Efrat, Kanitha Chim (Brno-Enclave-1c250), Dana Walker, Dustin Black, Eduard Benes, Francisco da Rocha, Gadi Glogowski, Juanje Ojeda, Luigi Pellecchia, Ozan Unsal, Pavol Brilla, Petr Sabata, Ryan Smith, Sandro Bonazzola, Sharon Metzger, Whitney Chadwick, Lucie Leistnerova.

## What Went Well

1. **Release delivered on time** despite multiple unknowns, respins, CVEs, and key people on holidays. RC1-RC3 built, tested, delivered. Most upvoted item. [Avi]
2. **Cross-team collaboration** - ad-hoc collaboration between AIB, RHAS, Kernel, Toolchain resolved potential blockers quickly. Second most upvoted. [Juanje/ATC]
3. **Pipelines-debugger agent** - early adoption helped with triaging pipeline errors. [Juanje/ATC]
4. **Luigi switching from Testing Farm to Jumpstarter** - risky but worked well. [Luigi]
5. **Pipeline migration to pac-jobs** - simpler and faster to fix issues, adjust, retry on the fly. [Juanje/ATC]
6. **Separate cycles for regular and debug testing.** [mentioned]
7. **Docs:** Complete downstream doc set developed, aligned with JTBD/user journey. Gaps captured as backlog. [Docs]

## What Didn't Go Well

### Kernel tagging and late package changes (most discussed)

- Kernel RPM tagging to 2.0 `-gate` delayed release gating and compose builds. Kernel folks lacked Brew permissions, no clear doc on correct tag (2.0 vs 2.0-z), missing program-level ownership documentation. [Avi]
- **Ozan expanded:** Unclear which kernel version was in which RC build until last minute. Dependent packages also unclear. Signing added stress. Wished for early definition of exact builds for the release.
- **Juanje expanded:** Sometimes mid-build they realized wrong version was being used. Need to know all versions (AIB, kernel, etc.) ahead of time before starting release build.
- **Avi connected to tagging:** "If you put the right ones in the gate tag, what's going in is right. It's also related to how we tag them correctly and who can do that."
- **Juanje clarified two separate issues:** (1) Knowing the expected package versions (manifest/contract), and (2) knowing the tagging process (who tags, where, handoff).

### NVR mismatches (kernel-ivos/dtbs/scmi)

Chicken-egg dependency blocked nightlies and releases multiple times. [Juanje]

### Distribution setup pain

Very little documentation, many teams involved each with small portion, lots of manual work. [Eitan/Kanitha]

### RHEL tribal knowledge gap

CDN, SKU, errata, repository setup - had to ask 3-4 different Slack channels to find the right people. Petr confirmed: "It's not just RHIVOS, it's everything. Lack of documentation, tribal knowledge, outdated stuff." [Kanitha, Gadi, Petr]

### Kernel team didn't know their responsibilities

Francisco: "The whole errata thing was something we didn't know we were responsible for. We didn't know people expected that from us." Kernel team was unaware of errata responsibilities, user space repo creation, and other downstream expectations. [Francisco]

### Francisco/Enablement (new in updated doc)

- Lack of clarity, fluid scope, major pivots a few sprints before dev complete
- Jira processing effort is one order of magnitude higher than MR effort - "not sustainable wrt morale and capacity"
- Exception/blocker process misused to add features to the release
- Last-minute review request of "very poor quality, suspiciously AI generated documentation that required major rewriting"

### Luigi/BOA (new in updated doc)

- Lack of information sharing between teams - had to learn kernel command line editing alone, many colleagues had similar issues. Suggested program tech talks.
- Clear access to kernel source code unclear - repository, branching confusion. Found it under an associate user profile.
- Need process to build gcov-enabled kernel (error-prone manual process currently)

### Other items

- RC2 blocked by external kernel MR (io_uring disabling) [Juanje]
- Unsigned kernel-automotive packages promoted to -candidate, ODCS rejected compose [Juanje]
- Infra issues: Tekton lease leaks, Docker runner failure, Fastboot detection [Juanje]
- AutoSD vs RHIVOS format mismatch (markdown vs asciidoc) [Docs]
- SME gaps, engineering-to-docs traceability gaps [Docs]
- Lack of awareness of RHIVOS/RHEL workflow ties; blockers/exceptions monitoring gaps [Program]
- Lack of trained backups [Program]

## Meeting Discussion - Key Topics

### 1. Release communication channel (20+ min discussion)

**Problem:** During RC release, technical discussions were scattered across 10-15 Slack channels. Hard to follow, hard to know the current blocker.

**Proposals debated:**
- **Juanje:** Dedicated ephemeral technical channel per release (e.g., `rhivos-2.1-technical`). Deep technical debugging there. Progress summaries posted back to release-readiness channel. Archived after release.
- **Whitney pushed back:** Release readiness channel was designed for exactly this. Another channel means looking in two places. People get frustrated when discussions happen in channels they didn't know about.
- **Avi:** War room with focals. Not too noisy. Pull people in when needed.
- **Whitney counter:** War room connotes emergency. Release readiness + threads could work.
- **Luigi:** Dashboard/checklist showing where release is blocked, linking to conversations.

**Compromise direction:**
- Release readiness channel stays as the program-level status channel
- Ephemeral technical channel per release for deep debugging
- **AI-powered summary** scanning the technical channel and posting blocker summaries to readiness channel (Avi's proposal, enthusiastically received)
- Dashboard as secondary - could be auto-populated, combined with AI summary

**Dana directly assigned Avi** the AI summary action item: "I'm tasking you."

### 2. End-to-end process documentation and handoffs (15+ min)

**Problem:** No documented end-to-end release process with clear ownership at each step. Teams discover responsibilities by surprise.

**Key quotes:**
- **Juanje:** "What we need to define is the handoff - when a team finishes, what they need to deliver to who."
- **Luigi:** POs should collaboratively document expectations (what we deliver, what we expect from other teams), then negotiate during PO planning.
- **Dana:** "I'm hearing process documentation end-to-end, negotiating contracts during PO planning, and leveraging AI on a live dashboard."
- **Avi:** "End-to-end should include folks not specifically in RHIVOS - starting with RHEL kernel. Petr was intending to do a talk with them, can you update where that stands?" (Raised KWF meeting status directly in meeting)
- **Avi:** Dashboard with live status - "same URL you go to, what's going on with the release, where is the block, which team, who's the focal, updated live or as close to live as possible."

### 3. Cross-functional responsibility clarity (5 min)

**Problem:** Teams don't know what other teams expect from them.

**Whitney:** Existing cross-functional definitions exist on Confluence. Teams should check their charters. What Francisco described (kernel team unaware of errata responsibilities) is a gap in communication, not definition.

**Action:** Whitney owns review of cross-functional definitions with the 3 POs (Whitney, Francisco, Gadi). Deadline: end of August.

### 4. CDN/SKU/Errata documentation (5 min)

**Problem:** Kanitha and team had to go through 3-4 Slack channels to figure out CDN, repo, errata process. Petr confirmed lack of documentation is universal.

**Action:** Document what was learned. Kanitha takes CDN/repo/errata portion. Gadi takes SKU portion.

### 5. GA transition (2 min)

**Luigi asked:** What changes when moving from TP to GA?

**Petr:** Not much process-wise. Main change is SLA enforcement - defects and CVEs need to be addressed within deadlines instead of best-effort. Customer requests will have response requirements.

## Action Items (finalized in meeting + doc)

| # | Action | Owner | Deadline | Status |
|---|--------|-------|----------|--------|
| 1 | **AI briefs for release blocker status** - PoC using AI to get clear state of release blockers from RR channel. Local PoC first (no AIA needed - uses existing RH-wide Slack MCP from DOL). | **Avi** | End of August | Not started |
| 2 | **Fill out retro doc action items section** | **Avi** | This week | Done |
| 3 | **Landing page** - single remote entry point for all RHIVOS resources. Collaborate with POs to collect tools/URLs. | **Luigi** | End of Q3 | Not started |
| 4 | **Cross-functional definitions review** - three POs review existing definitions, ensure teams are clear on responsibilities. | **Whitney** | End of August | Not started |
| 5 | **Handoff documentation** - define each team's handoff and document it so every team knows expectations. | **Juanje** | End of Q3 | Not started |
| 6 | **Technical release Slack channel** - create a release-specific technical channel for working on blockers. | **Juanje** | End of Q3 | Not started |
| 7 | **SKU/CDN/errata knowledge doc** - write down tribal knowledge from painful discovery process. Each owner covers their portion. | **Kanitha** (CDN/repo/errata), **Gadi** (SKU), **Petr** | End of Q3 | Not started |

### Comment thread notes (from doc)

- **PIA concern on AI + Slack:** Someone noted AI access to Slack channels was "historically problematic" and may require PIA. Petr flagged that AIA might take long or be NACKed.
- **Avi's response:** RH-wide Slack MCP was introduced in the last DOL, already in use. PoC can run locally without AIA.
- **Francisco on Jira:** "Enablement team should just follow the RHEL Jira process, any additional VROOM Jira process is responsibility of release team." And: "Jira processing effort is one order of magnitude higher than MR effort. Not sustainable wrt morale and capacity."

## Pre-meeting items (from doc, not explicitly discussed)

### Done (by Avi, pre-retro)

- **RHELBLD-18777** - Extended Brew tag permissions to RHIVOS kernel maintainers. Resolved.
- **RHELBLD-18778** - Extended Brew tag permissions to full ATC team. Resolved.
- Communicated new permissions to both Kernel and ATC teams.

### Not Done / Status Unknown

- **Petr's KWF alignment meeting** - Avi raised this in the meeting ("Petr was intending to do a talk with them"). No update from Petr during the retro. **No evidence this meeting took place** (checked Slack + Calendar Jul 30).
- **STAG automation** (Petr's lockstep build proposal) - not implemented.

### Other improvement items from doc (not discussed in meeting)

- [Juanje] Improve gating of kernel-automotive packages and dependencies (in progress)
- [Juanje] Document RPM signing process for all package-building teams
- [Ozan] Define target kernel version early in release cycle
- [Docs] Feature ownership, engineering-to-docs traceability, doc readiness improvements
