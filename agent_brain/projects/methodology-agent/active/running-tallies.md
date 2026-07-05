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

2026-07-01|autonomous|reporting|morning-briefing-parallel-scan|high
2026-07-01|autonomous|reporting|lp-status-cron-report|high
2026-07-01|assisted|communication|hubert-transition-slack-drafts|high
2026-07-01|enhanced|research|scrum-master-handoff-investigation|medium
2026-07-01|autonomous|project-tracking|deferred-queue-cleanup|high
2026-07-01|enhanced|research|autosd-cert-fix-rca-tracking|medium
2026-07-02|assisted|communication|sbi-feedback-kanitha-lp-priority|high
2026-07-02|assisted|tool-building|rhas-qe-expert-lead-agent-creation|high
2026-07-05|assisted|evaluation|qc-self-eval-career-aspirations-draft|high
2026-06-30|assisted|documentation|codebase-documentation-generation|high

