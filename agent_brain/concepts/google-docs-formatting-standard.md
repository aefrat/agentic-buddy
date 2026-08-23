---
last_accessed: 2026-08-23
access_count: 1
created: 2026-08-23
---

# Google Docs Formatting Standard

User preference (established Aug 23, 2026): **Always create Google Docs with professional formatting** - proper headings, tables, colors, and structure.

## Implementation Method

Create HTML files with professional styling, then upload to Google Docs using the Drive API:

```bash
gws drive files update \
  --params '{"fileId": "DOC_ID", "uploadType": "media"}' \
  --upload filename.html \
  --upload-content-type "text/html"
```

For new docs:
```bash
# Create blank doc first
gws docs documents create --json '{"title": "Document Title"}'
# Then upload HTML content via Drive API
```

## Professional Styling Standards

### Color Palette (Google Material Design)
- Primary blue: `#1a73e8` (headings, links, accent borders)
- Dark gray: `#202124` (body text)
- Medium gray: `#5f6368` (subtitles, secondary text)
- Light gray: `#e8eaed` (borders, dividers)
- Background gray: `#f8f9fa` (cards, hover states)
- Success green: `#1e8e3e`
- Warning orange: `#f29900`
- Error red: `#d93025` / `#ea4335`
- Info blue: `#e8f0fe` (background)
- Alert red: `#fce8e6` (background)

### Typography
- Font family: `'Google Sans', Arial, sans-serif`
- H1: 32px, color `#1a73e8`, bottom border 3px
- H2: 24px, color `#1a73e8`, left border 4px
- H3: 18px, color `#5f6368`, font-weight 500
- Body: 11pt (16px), line-height 1.6
- Subtitle: 14px, italic, color `#5f6368`

### Tables
- Header background: `#1a73e8` (blue)
- Header text: white
- Row hover: `#f8f9fa`
- Cell padding: 12px
- Border: 1px solid `#e8eaed`
- Box shadow: `0 2px 4px rgba(0,0,0,0.1)`

### Status Indicators
- ✓ Operational: green (`#1e8e3e`)
- ⚠ Partial: orange (`#f29900`)
- ✗ Missing: red (`#d93025`)

### Cards and Boxes
- **Epic cards**: Gray background (`#f8f9fa`), red left border (4px `#ea4335`)
- **Summary boxes**: Blue background (`#e8f0fe`), blue left border (4px `#1a73e8`)
- **Alert boxes**: Red background (`#fce8e6`), red left border (4px `#ea4335`)
- **Stat cards**: White background, border (`#dadce0`), centered text
- Border radius: 4-8px

### Gradients (for headers)
- Primary: `linear-gradient(90deg, #1a73e8 0%, #4285f4 100%)`
- Alert: `linear-gradient(90deg, #ea4335 0%, #f28b82 100%)`
- Success: `linear-gradient(90deg, #1e8e3e 0%, #5bb974 100%)`

### Icons and Symbols
Use unicode symbols in headings and references:
- 📊 for spreadsheets/data
- 📁 for directories/folders
- 🤝 for meetings/collaborations
- ✓ for success/operational
- ⚠ for warnings/partial
- ✗ for errors/missing

## Document Structure Template

1. **Title** (H1) - centered, large, blue underline
2. **Subtitle** - metadata (date, source), italic, gray
3. **Executive Summary** (summary box) - key findings, blue background
4. **Tables** - professional styling with blue headers
5. **Sections** (H2) - blue left border
6. **Subsections** (H3) - gray, medium weight
7. **Cards** - for repeated items (EPICs, issues, etc.)
8. **Alert boxes** - for critical information
9. **Stats grid** - visual metrics display
10. **References** - links and resources

## Why This Approach

1. **HTML → Google Docs** preserves rich formatting better than plain text
2. Consistent with Google Material Design principles
3. Professional appearance suitable for stakeholder presentations
4. Easy to scan with color coding and visual hierarchy
5. User preference: "top notch G-doc design"

## Example Use Cases

- Status reports (manager reports, QE reports)
- Analysis documents (EPIC coverage, gap analysis)
- Meeting notes (with action items in colored boxes)
- Technical documentation (with code blocks and tables)
- Executive summaries (with stat cards and highlights)

## Template Location

Reference HTML template: See `/tmp/rhas-coverage.html` from Aug 23, 2026 RHAS EPIC coverage analysis.
