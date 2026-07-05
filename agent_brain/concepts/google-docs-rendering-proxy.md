---
last_accessed: 2026-07-05
access_count: 0
created: 2026-07-05
---

# Google Docs as rendering proxy

Uploading HTML with `mimeType: application/vnd.google-apps.document` in the
request body metadata converts to native Google Docs format, rendering
inline in the browser. This bypasses Google Drive's download-only behavior
for HTML files and creates a "live dashboard" pattern: stable file_id URL,
content refreshed on each agent run.

## Key technical detail

For `gws drive files create`, the `mimeType` must go in `--json` (request
body metadata), NOT `--params` (URL parameters). Using `--params` uploads
the file as raw HTML; using `--json` triggers conversion.

```bash
# Correct - triggers HTML-to-Docs conversion
gws drive files create --json '{"name": "Report", "mimeType": "application/vnd.google-apps.document"}' --upload-file report.html

# Wrong - uploads as raw HTML, no conversion
gws drive files create --params '{"mimeType": "application/vnd.google-apps.document"}' --upload-file report.html
```

## Tradeoffs

- Gains: one-click viewing, permanent shareable URL, inline in Slack canvas
- Loses: CSS (grids, badges, gradients), anchor-based TOC links
- Google Docs auto-generates a Document Outline sidebar from `<h1>`-`<h6>`
  headings, which replaces anchor-based navigation

## Workarounds for formatting

- Use semantic heading elements (`<h2>`, not styled `<div>`) for sections
- Wrap all body content in a container `<table style="width: 100%">` to
  force uniform width (tables render narrower than body text otherwise)
- Place `<h2>` headings OUTSIDE table cells for Document Outline pickup

## Applications

Applied in PitCrew team report (Slack canvas link) and RHAS QE
deliverables (test strategy, release criteria). The pattern generalizes
to any agent-generated HTML report that needs browser-viewable permanent
links.

Source: [2026-06-24 log](../../logs/2026-06-24.md),
[2026-07-02 log](../../logs/2026-07-02.md)
