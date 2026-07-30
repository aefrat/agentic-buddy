---
last_accessed: 2026-07-30
access_count: 1
created: 2026-07-30
---

# Gemini transcription verification

AI-generated meeting notes (Google Gemini) reliably garble domain-specific
technical terms, product names, and proper nouns. The AI summary layer adds
further distortion beyond the raw transcript.

## Pattern

Gemini's speech-to-text substitutes phonetically similar common words for
specialized terms:

- "RHIVOS" -> "Rivos", "Rivals", "Ryos" (Jul 30)
- "Polarion" -> "Pulp" (Jun 23)
- "Kanitha" -> "Kita" (Jun 23)
- "RHAS" -> "ROS" (Jun 23)

The raw transcript tab is more accurate than the AI-generated Notes/Summary
tab, but still contains name variations. The summary compounds errors by
rephrasing garbled terms into plausible-but-wrong descriptions ("Rivals
migration" for RHIVOS-on-GitLab).

## Mitigation

1. Never act on Gemini meeting notes without cross-referencing claims against
   primary sources (Jira, Slack, code).
2. Use the raw transcript tab over the summary for factual extraction.
3. When quoting from Gemini notes in documents, verify technical terms and
   proper nouns against known correct spellings.
4. Treat the AI summary as a structural outline (who spoke when, topic flow)
   rather than a factual record.

## Scope

Observed with Google Gemini in Google Meet. Likely applies to any AI
transcription service processing domain-specific vocabulary without custom
vocabulary lists.

Source: [2026-06-23 log](../../logs/archive/2026-06/2026-06-23.md),
[2026-07-30 log](../../logs/2026-07-30.md)

> Related: [Source authority hierarchy](source-authority-hierarchy.md) -
> AI meeting notes rank below primary sources (Jira, Slack, code) in the
> authority hierarchy. This concept details the specific failure mode.
