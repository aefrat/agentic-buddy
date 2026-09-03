---
last_accessed: 2026-09-03
access_count: 1
created: 2026-09-03
---

# Plan - Status legend + Jira link on Needs Attention (Program Release Status)

Two enhancements to the RHIVOS Program Release Status Google Doc
(`build_combined_dashboard_html` in `tools/render_doc.py`), requested Sep 3.

## Status (Sep 3)

- **Part 1 (status legend): SHIPPED.** `_build_status_legend_html()` +
  `_STATUS_MEANING` added; wired under the summary table in the Program dashboard
  only. Visible table (Google Docs strips tooltips), two statuses: Released
  (green) / Active (blue). Driven by `_STATUS_BANNER` so it can't drift. ruff
  clean, 9/9 pytest (added `test_combined_dashboard_has_status_legend`). Committed
  `9e54307` + pushed; Program doc republished and legend verified live.
- **Part 2 (Jira link on Needs Attention): SHIPPED.** `_needs_attention_jira_url(stats)`
  builds a Jira issue-navigator URL (`/issues/?jql=key in (...)`, url-encoded)
  from the actual triage keys (urgent + monitor + active), so the linked set
  always matches the count; zero renders a plain number. Wired into
  `_combined_track_rows` (Program dashboard). Also refined the `_bare_vroom` test
  helper to treat keys inside a tag's attributes (the JQL href) as linked. ruff
  clean, 10/10 pytest (added `test_needs_attention_cell_links_to_jira`). Committed
  `2b7c946` (code-only, 2 files) + pushed; Program doc republished, links verified
  live with real triage keys. Scope: Program dashboard only (per the request);
  per-release header cells not linked - available as a later consistency add.

### Cleanup noticed (not fixed)

`kb/active/<release>/<track>/latest.json` change-tracking state is tracked in git
but `.gitignore` only ignores `kb/active/*.json` (top-level), not the per-track
subdirs the Core/FuSa split introduced. So those state files show as dirty and
get swept into commits on every run. Fix would be `kb/active/**/*.json` in
.gitignore + `git rm --cached`, but it has CI implications (CI needs prior state
to compute diffs), so raise with user before changing.

## Part 3 - Widen main summary-table columns (no mid-word breaks) [SHIPPED - via Docs API]

**First attempt (HTML CSS) FAILED.** Commit `5db4757` added a `<colgroup>` with
per-column percentages + `white-space: nowrap` on the `<th>`s + `table-layout:
fixed`. It was correct HTML, but the **Google Docs HTML importer ignores all
table CSS** - colgroup/`<col>` widths, per-`<th>` width, `table-layout:fixed`,
and `white-space:nowrap` do NOT survive import. Docs auto-sized the 9 columns to
their short *data* content, so wider headers (Track/Status/RC/Blockers) still
broke mid-word. Diagnosed live via `gws docs documents get`.

**Real fix shipped Sep 3 (commit `d0de20f`).** Key realization: the program
page is **already wide** (pageSize width 780pt, L/R margins 15pt -> ~750pt
usable) - the problem was purely uneven auto-column-sizing, so NO orientation
change was needed. The reliable lever is the **Google Docs API**:

- `_SUMMARY_COLUMNS` now carries a **point width** per column (single source;
  also feeds the HTML colgroup as a harmless fallback). Widths (pt): Release 105,
  Track 55, Status 80, Target 100, RC 45, Blockers 75, Needs Attention 105,
  On Track 70, Slack (7d) 80. Sum 715 <= 750 usable, so no overflow.
- `_set_summary_table_column_widths(doc_id)`: fetches the doc (`gws docs
  documents get`), locates the summary table by **column count == 9** (its start
  index shifts every run - was 974, then 823 after a shorter outlook), and
  `batchUpdate`s `updateTableColumnProperties` with `widthType:FIXED_WIDTH` per
  column. Wired into `agent.py` right after a successful combined upload (gws
  only). Prints "Summary table column widths applied".
- Because each HTML re-upload wipes native widths, the width step runs after
  **every** combined upload - not a one-off.

ruff clean, 12/12 pytest (added `test_summary_columns_carry_fixed_point_widths`).
Committed `d0de20f` (code-only) + pushed; pipeline rerun (`--all --llm`),
verified live: all 9 columns FIXED_WIDTH, sum 715, no mid-word header breaks.

Gotcha for future work: the gws command is `gws docs documents get/batchUpdate`
(service `docs`, resource `documents`), NOT `gws documents get`.

## Part 4 - Release H2 headers: add "Sum-up Below - Click here for details" [SHIPPED]

**Shipped Sep 3 (commit `d59b0ac`).** Each release section header (H2) in the
combined dashboard now displays: `{Release} Sum-up Below - Click here for
details` (where "Click here for details" links to the per-release doc). When no
doc_id, shows just `{Release} Sum-up Below`. ruff clean, 12/12 pytest. Committed
+ pushed; combined doc republished, headers verified live.



Requested Sep 3: the Program doc's main summary table breaks header words
mid-word (e.g. "Release" -> "Releas" / "e") because the first column is too
narrow. Make columns wide enough that words don't split.

### Diagnosis

The table is `width: 100%` with **no per-column widths** and no `white-space`
control (`_TH_STYLE`/`_TD_STYLE` have none). The body `max-width: 1000px` does
**not** transfer to Google Docs - Docs lays the table out on its own page
geometry (portrait US Letter, 1" margins ~ 6.5" usable). The HTML->Docs
converter then auto-distributes 9 columns, starves short-content columns, and
breaks header words mid-word. Total table width is capped by the page, so the
fix is about **allocating the fixed width per column + stopping intra-word
breaks**, not making the table arbitrarily wider.

### Fix (primary)

1. Add a `<colgroup>` with tuned **percentage** widths (percentages are the most
   reliably honored width lever on Google Docs import; they scale to the table
   width Docs sets to page width). Proposed allocation (sum 100):
   Release 14, Track 8, Status 11, Target 15 (holds "Not set in Jira"),
   RC 7, Blockers 11, Needs Attention 13, On Track 10, Slack (7d) 11.
2. Add `white-space: nowrap` to the single-word headers (Release, Status,
   Target, RC, Blockers) so they never split mid-word. Leave the genuinely
   two-word headers (Needs Attention, On Track, Slack (7d)) wrapping **between
   words** - their colgroup width gives room for a clean two-line header.
3. Keep number columns centered (optional: `text-align:center` on RC/Blockers/
   Needs Attention/On Track/Slack) for a tidier look.

### Optional levers (only if still tight after primary)

- Slightly reduce table font-size (e.g. 0.9em) to fit more per column.
- Shorten the longest headers ("Needs Attention" -> "Needs Att.",
  "Slack (7d)" -> "Slack"). This is a rename, so confirm before doing it.
- Landscape orientation would give ~9" but is **not** controllable via HTML
  upload - would need a manual Docs page-setup step; out of scope.

### Scope

Main Program summary table only (per the request). The per-release triage tables
(8 columns) likely wrap too and could get the same treatment as a follow-up -
not included unless requested.

### Verification

`--dry-run` + republish, then eyeball the live Program doc header row: "Release"
on one line, no mid-word breaks in any header, columns visually balanced.
ruff + pytest (add/adjust a test asserting the colgroup/nowrap is emitted).

### Decisions to confirm before fixing

1. Keep full header text (recommended - let two-word headers wrap between words),
   or shorten the longest ones to buy width?
2. Main summary table only (default), or also the per-release triage tables?

## 1. Status legend (not a hover tooltip)

**Constraint (must surface to user):** the doc is produced by uploading HTML to
Google Docs. Google Docs strips the HTML `title` attribute on conversion and has
no native per-word hover tooltip. A true "tooltip" is therefore not achievable.
The equivalent is a **visible legend** - a small color-coded table mapping each
status to its meaning, placed directly under the summary table.

### Design

- New helper `_build_status_legend_html()` in `render_doc.py`, driven by the
  existing `_STATUS_BANNER` dict (single source of truth for label + colors, so
  the legend can never drift from the status cells it explains).
- Renders a compact 3-row table (or definition list), each row: a color chip
  (bg + text color from `_STATUS_BANNER`) + the status name + a one-line meaning.
- Status vocabulary is two values only (`submission` was dropped Sep 3 - it was
  an unsourced coinage; see [core-fusa-split-plan](core-fusa-split-plan.md)):
  - **released** - the track has shipped / reached its release milestone
    (e.g. Core track completed). Green.
  - **active** - in active development; not yet released. A FuSa track still in
    progress is "active" (its not-released state is carried by not being
    released). Blue.
- Placement: emit right after `summary_table` in `build_combined_dashboard_html`,
  under a small "Status legend" heading.

### Optional consistency extension

Also render the legend once in each per-release doc (`build_release_doc_html`),
under the release title, so a reader who only opens one release doc still sees
the key. Costs one extra call; keeps docs self-explanatory.

## 2. Embedded Jira URL on the Needs Attention cell

Today the "Needs Attention" cell in the combined summary table
(`_combined_track_rows`, ~line 748-765) is a bare number. Make the number a link
to a Jira issue-navigator view of exactly those tickets.

### URL strategy (two options)

- **(A) Exact ticket keys (recommended).** Build JQL from the ticket keys already
  in `stats["triage"]` (`urgent` + `monitor` + `active` = the needs-attention
  set), e.g.
  `https://redhat.atlassian.net/issues/?jql=key in (VROOM-1,VROOM-2,...)`.
  Guarantees the linked set exactly matches the displayed count; no need to
  re-express triage logic as JQL.
- **(B) fixVersion + criteria JQL.** e.g.
  `project = VROOM AND fixVersion in (rhivos-2.0-core) AND <blocker/attention
  criteria> AND statusCategory != Done`. More "durable" (survives re-triage) but
  the result count can drift from the displayed number because the triage
  heuristics (age, blocker type, RC gating) are hard to reproduce faithfully in
  JQL.

Recommendation: **(A)** - correctness/consistency beats durability here, and the
doc is regenerated each run anyway.

### Design (option A)

- New helper `_needs_attention_jira_url(triage: dict) -> str | None`:
  collect `key` from `triage["urgent"] + triage["monitor"] + triage["active"]`;
  return `None` if empty; else URL-encode `key in (<comma-joined>)` into the
  issue-navigator URL (`urllib.parse.quote`).
- In `_combined_track_rows`, wrap the attention number in `<a href=...>` when the
  URL is non-None; keep the existing red-bold `att_style`. When `attention == 0`,
  render the plain number (no link).
- Same treatment optionally in `_build_track_header_html` "Needs Attention:" cell
  (per-release docs) for consistency.

## Files touched

- `tools/render_doc.py` - add `_build_status_legend_html`,
  `_needs_attention_jira_url`; wire legend into `build_combined_dashboard_html`
  (and optionally `build_release_doc_html`); link the attention cell in
  `_combined_track_rows` (and optionally `_build_track_header_html`).
- `tests/test_render_doc.py` - add: legend renders all three statuses with their
  meanings; attention cell links to a `key in (...)` Jira URL when >0 and stays a
  bare number when 0; existing `_bare_vroom` link tests still pass.
- No config, agent.py, or pipeline changes - both features are pure render-layer.

## Verification

- `ruff` clean; full pytest green.
- `--dry-run` inspect combined HTML: legend under summary table; attention cells
  are links to the correct ticket sets.
- Republish Program doc (and per-release docs if the optional scope is chosen).

## Open decisions (ask user)

1. Jira URL strategy: (A) exact ticket keys [recommended] vs (B) fixVersion JQL.
2. Scope: combined Program dashboard only, or also the per-release docs
   (legend under each release title + linked attention cell in each header).
