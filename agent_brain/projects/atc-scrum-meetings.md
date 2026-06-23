---
last_accessed: 2026-06-23
access_count: 1
created: 2026-06-23
---

# ATC Scrum Meetings

Recurring meeting notes and decisions from ATC (Automotive Toolchain) team ceremonies — backlog refinement, sprint planning, retros. Read when reviewing team status, catching up on missed meetings, or preparing for upcoming ceremonies.

## Backlog Refinement — 2026-06-18

**Source:** [Google Doc](https://docs.google.com/document/d/1WeRyqRZNhkr6eIUFb2T8c17oZiYxhP4qROIWV20__IM/edit?tab=t.dxhs2j6d9t1j) | [Recording](https://drive.google.com/file/d/1jy5OZbKstydwmDSglHfsgOqUhKckTBcZ/view)

### Updates

- **Matt Goldman** — Open MR awaiting release engineering review (Matus Boy, Michael). Eitan advised pinging PSCA support Slack channel. Also rebasing longstanding review tickets after fixing unnecessary pipeline executions.
- **Ozan Unsal** — Working on OS build (create-OS-build process changes, container pulls from MR pipelines → Pulp upload). NXP smoke test (EBBR images) implemented but pipeline blocked on **Polarion report upload** failure (Gemini mistranscribed as "Pulp"). Two stacked issues: wrong image URLs in nightly (fixed via MR !616) and Polarion upload failures causing jobs to show failed even though smoke tests pass. Second fix MR !617 posted. Polarion issue still persisting as of Jun 19. Epic VROOM-44450 and all children closed by Jun 23.
- **Eitan Raviv** — Housekeeping ticket merged/done. First MR for release pipeline onboarding (accessor.com) merged; waiting for Kanitha Chim's feedback post-DevCon. RHAS team installation ticket mostly complete but OCP installer issues remain.
- **Hubert Stefanski** — Used Claude to address Eitan's feedback on S3 + HTML ticket. Validating output on pre-prod before requesting review from Eitan.

### Action Items

| Who | Action | Status |
|-----|--------|--------|
| Matt Goldman | Ping Matus Boy & Michael on PSCA support Slack for MR review | open |
| Matt Goldman | Rebase longstanding review tickets, re-request reviews | open |
| Ozan Unsal | Update smoke test ticket → done once pipeline unblocked | done (VROOM-44450 closed) |
| Hubert Stefanski | Validate S3+HTML fix on pre-prod, request review from Eitan | open |

### Key Themes

- Pipeline and build infrastructure: OS builds, smoke testing, Polarion report upload failures
- Release engineering review bottleneck — use PSCA support Slack channel
- Onboarding/installation: accessor.com pipeline (awaiting Kanitha), RHAS team OCP installer issues
