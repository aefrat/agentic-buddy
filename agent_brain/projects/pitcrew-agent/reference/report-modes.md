---
last_accessed: 2026-06-24
access_count: 1
created: 2026-06-23
---

# Report Modes

Three modes with increasing depth. Default: weekly.

## Daily

Sprint-focused execution snapshot. Fast to generate, low noise.

**Sections included:**
1. Hero banner (title, date, mode badge)
2. Executive Summary (3 sentences max)
3. Sprint Health (current sprint tickets, status counts, at-risk signal)
4. Epic Changes (only epics that changed status since last run)
5. Changes Since Last Report (diff from previous snapshot)
6. Footer

**Sections excluded:** Strategic Guide, Roadmap, full epic grid, Slack Digest, Strategy Alignment, Looking Ahead.

**Subject line:** `[PitCrew Daily] RHAS Sprint Status — YYYY-MM-DD`

## Weekly (default)

Full operational report with strategic alignment. Primary cadence.

**Sections included:**
1. Hero banner
2. Executive Summary
3. Changes Since Last Report (diff)
4. Strategic Guide (condensed, from cache)
5. 2026 Roadmap (current + next quarter only)
6. RHAS Releases (timeline + next 3 release targets)
7. Features & Epics (full grid, split by changed/unchanged)
8. Current Sprint (full ticket table, counts, at-risk)
9. Strategy ↔ Work Alignment (well-aligned + gaps)
10. Looking Ahead (this week / this month / strategic / team health)
11. Footer

**Sections excluded:** Slack Digest.

**Subject line:** `[PitCrew Weekly] RHAS Status — week of YYYY-MM-DD`

## Full

Weekly + Slack Digest. Bi-weekly or on demand.

**Sections included:** All weekly sections PLUS:
- Slack Digest (two-column: #team-pitcrew-automotive + #forum-jumpstarter, 7-day window)

**Subject line:** `[PitCrew Full] RHAS Status — YYYY-MM-DD`

## Team Report (auto-generated alongside full/weekly)

Lean view for sprint-focused readers, uploaded as a Google Doc to the Slack canvas. Not a standalone mode — generated automatically as part of every full or weekly run (step 11d).

**Sections included:**
1. Hero banner (compact)
2. Executive Summary
3. Changes Since Last Report
4. Current Sprint (full ticket tables — open + recently closed)
5. Slack Digest (two-column, same as full — included even when parent mode is weekly)
6. Strategy ↔ Work Alignment

**Sections excluded:** Strategic Guide, Roadmap, Releases, full Epic grid, Looking Ahead.

**Format:** Inline-styled HTML (no `<style>` block), auto-converted to Google Docs on upload. Tables OK; CSS grids/badges simplified by conversion.

**Delivery:** Google Doc overwrite (same file ID, permanent link pinned in #team-pitcrew-automotive Slack canvas).

## Mode selection logic

- User says "daily" or "pitcrew daily" → daily
- User says "full" or argument is "full" → full
- Otherwise → weekly
- Cron: weekdays 08:37 = full (generates both full + team reports)
