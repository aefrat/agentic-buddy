# Running Tallies

Structured ledger for compute_stats.py input. Each line is one classified
task. Append-only, never edit existing lines.

Format: `DATE|CATEGORY|DOMAIN|TASK_LABEL|CONFIDENCE`

Example:
```
2026-06-29|autonomous|reporting|manager-report-daily|high
2026-06-29|assisted|evaluation|qc-juanje-draft|high
2026-06-29|enhanced|research|slack-channel-scan|medium
```

---

2026-06-30|assisted|documentation|codebase-documentation-generation|high

