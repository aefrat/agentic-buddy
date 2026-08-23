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

**Design Philosophy:** Clean, minimal, professional. Optimized for readability and scan-ability by engineering teams.

### Color Palette (Refined for Professional Docs)
- Primary blue: `#4285f4` (accent borders, links)
- Black: `#1a1a1a` (headings)
- Dark gray: `#333` (body text)
- Medium gray: `#666` (labels, metadata)
- Light gray: `#e0e0e0` (borders, dividers)
- Background gray: `#f8f9fa` / `#f5f5f5` (cards, tables)
- Success green: `#1e8e3e` (backgrounds: `#e6f4ea`)
- Warning orange: `#f29900` (backgrounds: `#fef7e0`)
- Error red: `#d93025` / `#ea4335` (backgrounds: `#fce8e6`)

### Typography
- Font family: `Arial, sans-serif` (clean, universally readable)
- H1: 28px, color `#1a1a1a`, weight 600, letter-spacing -0.5px
- H2: 20px, color `#1a1a1a`, weight 600, bottom border 2px `#e0e0e0`
- H3: 16px, color `#1a1a1a`, weight 600
- Body: 13-14px, line-height 1.6-1.7, color `#333`
- Metadata: 13px, color `#666`

### Tables
- Header background: `#f5f5f5` (subtle gray, not bright colors)
- Header text: `#1a1a1a`, weight 600, uppercase, 13px, letter-spacing 0.5px
- Header border: 2px solid `#e0e0e0`
- Row hover: `#fafafa` (very subtle)
- Cell padding: 12-16px
- Border: 1px solid `#e0e0e0` (outer), 1px solid `#f0f0f0` (row dividers)
- Clean, minimal design - no heavy shadows

### Status Badges (Pill-Style Indicators)
Use inline badge elements instead of plain symbols:
- Success: background `#e6f4ea`, color `#1e8e3e`, text "Operational"
- Warning: background `#fef7e0`, color `#f29900`, text "Partial" or "Infrastructure Ready"
- Error: background `#fce8e6`, color `#d93025`, text "None" or "Do Not Exist"
- Badge style: 4px/10px padding, 3px border-radius, 11px font-size, uppercase, weight 600

### Cards and Boxes
- **EPIC cards**: White background, 1px border `#e0e0e0`, 16px padding, 4px border-radius
  - Hover: subtle shadow `0 2px 8px rgba(0,0,0,0.08)`
  - EPIC key in blue (`#4285f4`)
  - Details in gray (`#666`)
  - Status badges inline
- **Summary boxes**: `#f8f9fa` background, 4px left border `#4285f4`, 24px padding
- **Alert boxes**: `#fce8e6` background (critical) or `#fef7e0` (warning), 4px left border
- **Stat cards**: White background, 1px border `#e0e0e0`, centered text, large number (36px bold)
- **Release headers**: `#f5f5f5` background, 4px left border `#4285f4`, 12px/16px padding
  - Tech Preview: border `#ea4335`, background `#fef7e0`
  - GA: border `#1e8e3e`, background `#e6f4ea`

### Spacing and Layout
- Document padding: 40px all sides
- Section margins: 40px top for H2, 28px for H3
- Paragraph margins: 12px between paragraphs
- Table margins: 20px top/bottom
- Card margins: 12-16px between cards
- Max width: 900px (readable line length)

## Document Structure Template

1. **Header Section** (top border, not centered)
   - H1 title: 28px, black, weight 600
   - Metadata below: 13px gray, author + date
   - Bottom border: 3px `#4285f4`

2. **Executive Summary** (gray box with left border)
   - Background `#f8f9fa`, 4px blue left border
   - H2 inside with margin-top 0
   - Key finding in white sub-box with red left border

3. **Content Sections**
   - H2: bottom border 2px `#e0e0e0`
   - Tables: subtle gray headers (not bright colors)
   - Badge-style status indicators (pill design)

4. **EPIC Cards** (for repeated structured items)
   - Clean white cards with 1px border
   - EPIC key in blue, details in gray
   - Inline coverage badges
   - Hover effect for interaction

5. **Release Sections**
   - Header bar with left border (color-coded by milestone)
   - EPIC cards nested inside
   - Clean separation between releases

6. **Stats Grid** (4-column for key metrics)
   - Large numbers (36px bold)
   - Small labels (12px uppercase)
   - Color-coded for severity (red=critical, orange=warning)

7. **Alert Boxes** (for critical info)
   - Colored background + left border
   - Urgent items stand out visually

8. **Footer** (references, metadata)
   - Top border separator
   - Small gray text
   - Links to source documents

## Why This Approach

1. **HTML → Google Docs** preserves rich formatting better than plain text or batchUpdate API
2. **Clean, minimal design** - professional without being overwhelming
3. **Engineering-team optimized** - easy to scan, clear hierarchy, actionable insights
4. **Subtle colors** - gray headers instead of bright blues, status badges instead of symbols
5. **Print-friendly** - works well on screen and paper
6. **User preference** - "professional looking G-doc that I can share with an engineering team"

## Design Principles

- **Clarity over decoration** - no unnecessary gradients or heavy shadows
- **Hierarchy through spacing** - generous whitespace, clear sections
- **Scannable content** - badges, cards, tables optimized for quick reading
- **Professional polish** - suitable for stakeholder presentations and technical reviews
- **Consistent patterns** - EPIC cards, release sections, stat grids reusable across docs

## Example Use Cases

- Status reports (manager reports, QE reports, weekly updates)
- Analysis documents (EPIC coverage, gap analysis, technical assessments)
- Meeting notes (with action items in colored alert boxes)
- Technical documentation (with tables and structured data)
- Executive summaries (with stat cards and key findings)

## Reference Implementation

RHAS EPICs Per Release vs Test Coverage Analysis (Aug 23, 2026):
- Document ID: `1M2ON8WedyWO-UztdZYeXTl7nobLJ9SJWY86Ar5F_GJE`
- Demonstrates: Clean header, executive summary, professional tables, EPIC cards, stats grid, alert boxes, recommendations sections, footer
