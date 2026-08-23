---
last_accessed: 2026-08-23
access_count: 2
created: 2026-08-23
---

# Google Docs Formatting Standard

User preference (established Aug 23, 2026): **Always create Google Docs with clean, professional formatting suitable for sharing with engineering teams.**

## Implementation Method

**Use Google Docs native API (batchUpdate) - NOT HTML upload.**

HTML upload causes boundary markers and formatting issues. Instead:

1. Create document: `gws docs documents create --json '{"title": "Document Title"}'`
2. Add content as plain text: `gws docs +write --document "DOC_ID" --text "$(cat content.txt)"`
3. Apply styles with batchUpdate: `gws docs documents batchUpdate --params '{"documentId": "DOC_ID"}' --json '{"requests": [...]}'`

### Example: Apply HEADING_1 to title
```json
{
  "requests": [
    {
      "updateParagraphStyle": {
        "range": {"startIndex": 1, "endIndex": 50},
        "paragraphStyle": {"namedStyleType": "HEADING_1"},
        "fields": "namedStyleType"
      }
    }
  ]
}
```

## Professional Styling Standards

**Design Philosophy:** Clean, simple, minimal. Use Google Docs' default styles. Easy to read and navigate.

### Typography (Google Docs Default Styles)
Use namedStyleType for all headings - don't override colors or fonts:

- **HEADING_1**: Document title (24pt, bold)
- **HEADING_2**: Major sections (18pt, bold)
- **HEADING_3**: Subsections (14pt, bold)
- **SUBTITLE**: Metadata under title (15pt, gray)
- **NORMAL_TEXT**: Body text (11pt, normal)

### Status Indicators
Use simple unicode symbols inline with text:
- ✓ Success/Operational (green context)
- ⚠ Warning/Partial (orange context)
- ✗ Error/Missing (red context)

### Tables
- Use insertTable request: `{"insertTable": {"location": {"index": N}, "rows": R, "columns": C}}`
- Populate cells with insertText requests
- Apply header styling to first row if needed
- Keep it simple - Google Docs will apply default table styling

## Document Structure Pattern

```
TITLE (HEADING_1)

Generated: [Date] | Source: [Source] (SUBTITLE)

Executive Summary (HEADING_2)

[Summary paragraph]

Key Finding: [Critical finding paragraph]

Current Testing State (HEADING_2)

[Status items with unicode symbols]
✓ Item 1: Details
⚠ Item 2: Details
✗ Item 3: Details

Section Name (HEADING_2)

Subsection (HEADING_3)

[Content organized by subsections]

References (HEADING_2)

[Links and sources]
```

## Content Organization Principles

1. **Clear hierarchy** - H1 → H2 → H3, no skipping levels
2. **Scannable sections** - Each H2 is a major topic
3. **Consistent formatting** - Same pattern for similar items
4. **Minimal decoration** - Let content and structure speak
5. **Professional tone** - Suitable for technical stakeholders

## Building Documents Step-by-Step

1. **Write plain text version** - All content in a .txt file with clear section markers
2. **Upload as plain text** - `gws docs +write`
3. **Apply heading styles** - batchUpdate with updateParagraphStyle for each heading
4. **Add tables if needed** - insertTable + populate cells
5. **No colors, no fancy styling** - Keep it clean and professional

## Why This Approach

- **No HTML boundary markers** - Native API avoids upload artifacts
- **Clean, simple design** - Uses Google Docs' default styles
- **Easy to maintain** - No custom CSS or complex formatting
- **Professional appearance** - Suitable for engineering teams
- **Accessible** - Works well in all viewing modes
- **User preference** - "professional looking G-doc that I can share with an engineering team"

## Example Use Cases

- Status reports (manager reports, QE reports)
- Analysis documents (EPIC coverage, gap analysis)
- Meeting notes (with action items)
- Technical documentation
- Executive summaries

## Reference Implementation

RHAS EPICs Per Release vs Test Coverage Analysis (Aug 23, 2026):
- Document ID: `1M2ON8WedyWO-UztdZYeXTl7nobLJ9SJWY86Ar5F_GJE`
- Method: Plain text → batchUpdate for headings
- Style: Clean, simple, professional - uses default Google Docs styles
