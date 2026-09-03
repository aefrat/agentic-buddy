---
last_accessed: 2026-09-03
access_count: 2
created: 2026-09-02
---

# Implementation plan - Core vs non-Core (FuSa) split

## Implementation status (Sep 3)

Rollout steps 1-6 **done and verified locally**. Code changes landed in `rhivos-release-status` (uncommitted working tree): config restructured into `tracks: {core, fusa}` per release; `track` threaded through `query_jira` (`--track` option, per-track `run`/`run_all_statuses`); `agent.py` split into shared-per-release (Slack scan on union of active keys, meeting fetch on union of all-status keys, untracked lookup on union) + per-track `run_track` (per-track chart, `compute_stats` with previous state at `kb/active/<release>/<track>/latest.json`, `synthesize` with per-track config); `render_doc` reworked (per-track status banner, `build_track_section_html`, `build_release_doc_html`, combined dashboard one row/block per track, new `run(release_label, tracks, release_slug, ...)`); `synthesize._build_program_prompt` reads flattened per-track results. `compute_stats.py` needed **no change** (it already partitions on `release`/`fix_versions` from `jira_data`).

Verification: `ruff` clean; 7/7 pytest pass (added `test_core_and_fusa_render_as_separate_sections` and `test_fusa_2_0_is_not_labelled_released`). Dry runs confirm the split - 2.0 Core = 7 active blockers (rhivos-2.0-core, banner "Released"), FuSa = 27 (rhivos-2.0, banner "FuSa submission (not released)"); single h1/footer per doc; combined dashboard shows 6 rows (3 releases x 2 tracks) with correct per-track status.

**Target dates - Jira is the single source of truth (user decision, Sep 3).** Dates were hand-maintained per-release in config; the split duplicated one date onto both tracks, and the values were stale. Fixed: `query_jira.resolve_target_date(fix_versions)` reads each track's target live from the Jira **fixVersion `releaseDate`** (VROOM project versions, `_get('/project/VROOM/versions')`, lru_cached). No config fallback for display - when a fixVersion has no `releaseDate` set, the doc states **"Not set in Jira"** (render `_target_display`). Current Jira dates: 2.0-core 2026-06-30, 2.0 (FuSa) 2026-10-30, 2.0.z-core 2026-12-15, 2.1-core 2027-06-29; **rhivos-2.0.z and rhivos-2.1 (FuSa versions) have no releaseDate in Jira** -> shown as "Not set in Jira" until someone sets them in Jira. Config `target_date` fields now vestigial (only the standalone render-doc CLI still reads them).

**Shipped (Sep 3) - all outward steps done.** Code committed + pushed to `main` (commit e240100, gitlab.cee.redhat.com/aefrat/rhivos-release-status). All 4 live docs republished with per-track LLM outlooks (gemini via Vertex, `VERTEX_PROJECT_ID` in .env): Program `1kj6C8JIMyIQmz8WclgWPhHq54d7tvAuQV1zgtLAw5Ps`, 2.0 `1pGTw_-8ewLyMcOAWkg5IRmOZBQoQfelFCSs26Unc_7w`, 2.0.z `1_cOY9mag91_1NseTL9zdE_Sh5vL0pxm8LqRO-aQR_bI`, 2.1 `12AmIotP7Y-cl9LOtzexzme82YWWGbOG7XZgCOWVDv8U`. Whitney pinged via comment on VROOM-49388 (reported both fixes + the live-target-date change, with doc links). The temporary `[REVIEW]` copies were deleted.

**Still open (not part of this fix):** RHIVOS 2.0 retro demo to Dana/team not yet scheduled; FuSa fixVersions rhivos-2.0.z and rhivos-2.1 have no releaseDate in Jira (docs show "Not set in Jira" until set).

# Implementation plan - Core vs non-Core (FuSa) split

Addresses Whitney Chadwick review fix #1 (Core/FuSa separation) and, as a side effect, fix #2 (per-track released status). See [index](index.md) "Requested fixes" section.

**Chosen structure (user decision, Sep 2):** Sub-sections per release doc. Keep the 3 release docs (2.0, 2.0.z, 2.1); each doc renders a **Core** section and a **FuSa** section, each with its own blockers, stats, chart, Slack digest, outlook, and per-track released status. Combined dashboard shows 3 releases, each split into the two tracks.

## Root cause

The pipeline is parameterized by `release -> fix_versions -> JQL`. Today each release entry **bundles both tracks** into one JQL (`rhivos-2.0` maps to `[rhivos-2.0, rhivos-2.0-core]`, `fixVersion IN (...)`) and carries one shared `status: released`. That merge is why Core and FuSa are indistinguishable and why FuSa 2.0 inherited "released" from Core.

## Design: track as a sub-unit of release

Introduce a **track** dimension (`core`, `fusa`) under each release. Data gathering runs per track; Slack scan and meeting-notes fetch stay **once per release** (channel/doc-level) and are partitioned per track via exact fix_version matching (the cross-release-leakage fix already uses exact match, so `rhivos-2.0` vs `rhivos-2.0-core` and `rhivos-2.0` vs `rhivos-2.0.z` do not collide despite substring overlap - watch-item: keep matching exact, never `startswith`/`in`).

### Config restructure - `kb/reference/release-config.yaml`

```yaml
releases:
  rhivos-2.0:
    label: "RHIVOS 2.0"
    doc_id: "1pGTw_-8ewLyMcOAWkg5IRmOZBQoQfelFCSs26Unc_7w"
    tracks:
      core:
        fix_versions: [rhivos-2.0-core]
        status: released
        current_rc: RC3
        target_date: "2026-06-30"
      fusa:
        fix_versions: [rhivos-2.0]
        status: submission        # NOT released - FuSa submission (fixes #2)
        target_date: "2026-06-30"
  rhivos-2.0.z: { core/fusa tracks, both active }
  rhivos-2.1:   { core/fusa tracks, both active }
```

Track order: core then fusa. `order` (release order) unchanged.

## File-by-file changes

1. **`tools/query_jira.py`** - add `track` param.
   - `resolve_fix_versions(release, track)` reads `releases[release]["tracks"][track]["fix_versions"]`.
   - `run(release, track)` and `run_all_statuses(release, track)` thread `track` through; keep JQL builder as-is (already exact `fixVersion IN`).
   - CLI: add `--track` option.

2. **`agent.py`** - restructure `run_release` into shared + per-track:
   - Shared once per release: Slack scan (union of both tracks' active ticket keys), meeting-notes fetch (union of all-status keys), `untracked_lookup` (union of mentioned keys).
   - New `run_track(release, track, track_cfg, slack_data, doc_data, untracked_lookup, ...)`: per-track Jira active + all-statuses query, chart, `compute_stats` (per-track previous state), `synthesize` (pass track fix_versions + track status/label -> per-track outlook, cross_ref, and per-track filtering of untracked/potential/meeting mentions).
   - Partition Slack relevant messages + meeting mentions to the track whose ticket set they reference.
   - Build `release_result = {release, label, tracks: [core_result, fusa_result]}`.
   - Render one doc per release from both track results.

3. **`tools/render_doc.py`** - biggest change.
   - New `build_release_doc_html(release_label, tracks=[...])` that renders a release header then, per track, a labelled sub-section (Core / FuSa) reusing existing section builders (status banner, stats, blocker table, chart, Slack digest, outlook).
   - Per-track **status banner** replaces the single `status == "released"` block (lines ~449-461) - fixes #2. Map `submission` -> "FuSa submission (not released)".
   - `build_combined_dashboard_html`: per release, emit two track rows/sub-blocks; summary table status color per track (line ~690-702).
   - Update `run(...)` signature to accept track results list.

4. **`tools/compute_stats.py`** - per-track change tracking: previous-state path becomes `kb/active/<release>/<track>/latest.json`. Logic otherwise unchanged.

5. **`tools/synthesize.py`** - `run(...)` and `generate_program_outlook(...)` take track-level config (status, fix_versions, label). `_ticket_matches_release` already keyed on fix_versions (exact) - no change. Program outlook iterates releases x tracks.

6. **State/history** - archive per track: `kb/history/<release>/<track>/<date>.json`, `kb/active/<release>/<track>/latest.json`.

7. **`tests/test_render_doc.py`** - update for new signatures; add a case asserting Core vs FuSa sections render separately and FuSa 2.0 is NOT labelled released.

## Watch-items / risks

- **Substring fix_versions** (`rhivos-2.0` in `rhivos-2.0-core` / `rhivos-2.0.z`): safe only with exact matching. JQL `fixVersion IN` is exact; keep synthesis matching on set membership, never substring.
- **Tickets in both tracks** (a ticket carrying both `rhivos-2.0` and `rhivos-2.0-core` fixVersions) will legitimately appear in both sections - acceptable/correct.
- **Doc size**: two full sections per doc roughly doubles length. Acceptable per chosen structure.
- **Slack/meeting double-count**: gather once per release, partition per track - avoids duplicate API calls.

## Rollout

1. Restructure config (also fixes #2 immediately).
2. Thread `track` through query_jira + synthesize + compute_stats.
3. Refactor agent.py orchestration (shared vs per-track).
4. Rework render_doc for track sub-sections + per-track status banner.
5. `--dry-run` locally, inspect HTML for all 3 releases.
6. Update tests; run ruff + pytest.
7. Republish 3 docs + combined; ping Whitney on the thread/ticket.

## Scope note

User asked to plan **fix #1** (the split). Fix #2 (released status) is folded in because it is fixed by the same config restructure + per-track status banner. No extra work.
