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
- **Part 2 (Jira link on Needs Attention): NOT STARTED.** Design below stands;
  with `submission` dropped it is unaffected.

### Cleanup noticed (not fixed)

`kb/active/<release>/<track>/latest.json` change-tracking state is tracked in git
but `.gitignore` only ignores `kb/active/*.json` (top-level), not the per-track
subdirs the Core/FuSa split introduced. So those state files show as dirty and
get swept into commits on every run. Fix would be `kb/active/**/*.json` in
.gitignore + `git rm --cached`, but it has CI implications (CI needs prior state
to compute diffs), so raise with user before changing.

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
