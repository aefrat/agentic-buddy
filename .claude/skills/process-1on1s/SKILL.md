---
name: process-1on1s
description: Process all 1:1 Google Docs to extract the latest meeting from each, log a digest, capture action items, and add reflections. Use when asked to process 1:1s, digest 1:1 meetings, sync 1:1 notes, or review latest 1:1s.
compatibility: Requires gws CLI with Google Drive and Docs API access.
---

## Doc registry

| Person | Doc name | Doc ID |
|--------|----------|--------|
| Kanitha | Notes - 1:1 Kanitha / Avi | 1YW7pLd8pJGZasJqIiMm6q_IfrkvwU-bx_on403d-YEM |
| Muhamad | Notes - Muhamad/Avi 1:1 | 1rxsNN3GdkDT12XqscA9RndcMOzjxMCuNFNd5jW1DbE8 |
| Jaime | Avi/Jaime | 15Mct3u5q9xrPYUpEy6XFUMRNwe7B2dtWTewjr2Y4440 |
| Bella | Notes - Bella/Avi 1:1s | 1N-FhlCTpqbZaeNuUp63BpOEQv8IpVc79CsjvKSevhHk |
| Benny | Notes - Avi/Benny 1:1s | 1A10om-eAD7lf8mUNMD13imKFzArrrTOOY9BBcv0devs |
| Roddie | Roddie/Avi 1:1 | 1b-tbZ_r33xxupsraY9fmrGpKeXuEvLg8McirP9yUgMs |
| Hubert | Notes - 1:1 - Hubert / Avi | 14xYO1kAy3Vv5wWukM5JfyJkWlbHSTZ3WwifYZSicBIk |
| Roni | Notes - 1:1 Roni/Avihai | 1sjWfMmFwKGqFkI4K0Vq8gDQjFlHr-cfmMMC16Sum63I |
| Matt | Notes - Matt/Avi 1:1s | 1i97AYB2DnHQyjSqDR2A0y2XlY6lXhyI2Nu-lDho8I-0 |
| Paul | Notes - Paul/Avi Sync | 1DKLez4cVB14ddsw0RmeMxRxKK-L_zZWgQ3yIb-OYMok |

To update the registry, search Drive:
```bash
gws drive files list --params '{"q": "mimeType=\"application/vnd.google-apps.document\" and (name contains \"/Avi\" or name contains \"/ Avi\" or name contains \"Avi/\" or name contains \"Avi /\" or name contains \"1:1\")", "fields": "files(id,name,modifiedTime)", "pageSize": 30}'
```

## Procedure

### 1. Export all docs

For each doc in the registry, export to plain text:

```bash
gws drive files export --params '{"fileId": "<DOC_ID>", "mimeType": "text/plain"}' -o 1on1-export-<person>.txt
```

Export all docs before processing. Add 0.3s delay between exports to respect rate limits.

### 2. Extract the latest meeting from each doc

Docs are structured with meetings in reverse chronological order. Each meeting starts with a date header — common formats:

- `Jun 18, 2026`
- `June 18, 2026`
- `May 20, 2026`
- `2026-06-18`
- Date on its own line, sometimes followed by a blank line

For each exported doc:
1. Find the **first date header** — this is the start of the latest meeting.
2. Find the **second date header** — this is the boundary (end of latest meeting).
3. Extract everything between these two dates as the latest meeting content.

If no date header is found, treat the entire doc content (first 200 lines) as the latest entry.

### 3. Process each meeting

For each person's latest meeting, extract:

**Action items** — lines matching any of:
- `[ ]` checkbox syntax
- Explicit asks: "please", "can you", "will you", "need to", "should", "let's", "reach out", "follow up", "schedule", "set up"
- Items with a person's name + verb (e.g., "Roderick: schedule intro meetings")
- Lines under headers like "Next steps", "Action items", "TODOs", "Follow-ups"

For each action item, determine the **owner**:
- If the item references someone by name → that person owns it
- If it's in second person ("you should…") → the other person in the 1:1
- If unclear → mark as `[owner?]`

**Decisions** — conclusions reached, directions set, agreements made.

**Key topics** — main subjects discussed (2-4 bullet points).

**Open questions / blockers** — unresolved items, things waiting on someone else.

### 4. Write action items

Create or update `user/1on1-action-items.md`:

```markdown
# 1:1 Action Items

Last processed: YYYY-MM-DD

## Kanitha (meeting: Jun 18, 2026)
- [ ] **Avi:** [action item description]
- [ ] **Kanitha:** [action item description]

## Muhamad (meeting: Jun 17, 2026)
- [ ] **Muhamad:** [action item description]

...
```

If the file already exists, **replace** the section for each person with updated content from the latest meeting. Preserve any manually added items that don't appear in the doc (marked with `[manual]` or under a `### Manual` subsection).

### 5. Log the digest

Append to `logs/YYYY-MM-DD.md` under a new section:

```markdown
## 1:1 meeting digest

Processed 1:1 docs for N people. Latest meetings span [date range].

### Per-person summary

**Kanitha** (Jun 18, 2026)
- Topics: [2-4 bullet points]
- Decisions: [if any]
- Open: [unresolved items]

**Muhamad** (Jun 17, 2026)
- Topics: ...

...

### Cross-cutting themes
- [Theme 1: which 1:1s it appeared in]
- [Theme 2: ...]

### Action items captured
- Total: N items across M people
- Avi's items: N
- Written to user/1on1-action-items.md
```

### 6. Add reflections

After processing all meetings, look for patterns:

- **Recurring blockers** across multiple 1:1s (same issue mentioned by 2+ people)
- **Team sentiment signals** (morale, workload, frustration patterns)
- **Knowledge gaps** (multiple people unsure about the same topic)
- **Organizational patterns** (process issues, communication gaps)

If any pattern qualifies as an observation candidate (per process-conversation.md rules), append to `agent_brain/observations.md` under the appropriate category.

Add a brief note in the log's Context section linking the 1:1 digest to any relevant project or concept files.

### 7. Clean up and commit

```bash
rm -f 1on1-export-*.txt
git add logs/ user/1on1-action-items.md agent_brain/observations.md
git commit -m "1on1: process latest meetings — YYYY-MM-DD"
```

## Scope options

The user can narrow the scope:
- **Single person:** "process 1:1 with Kanitha" → only that doc
- **Time filter:** "process 1:1s from this week" → skip docs whose latest meeting is older
- **All (default):** process all docs in the registry

## Maintaining the registry

When the user mentions a new 1:1 doc or a new direct report:
1. Search Drive for the doc
2. Add the entry to the registry table above
3. Note the addition in the daily log
