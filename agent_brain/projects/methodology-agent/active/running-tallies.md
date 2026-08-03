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
2026-07-12|autonomous|reporting|atc-slack-channel-scan-10ch|high
2026-07-12|autonomous|reporting|stakeholder-slack-activity-lookup-4ppl|high
2026-07-12|autonomous|project-tracking|vhcl-009-closure-tracking|high
2026-07-13|assisted|evaluation|roderick-spse-l5-gap-analysis|high
2026-07-13|autonomous|evaluation|qc-self-input-roderick-career|high
2026-07-13|assisted|people-management|kanitha-retention-conversation-prep|high
2026-07-13|assisted|people-management|kanitha-1on1-transcript-analysis-summary|high
2026-07-13|assisted|communication|kanitha-slack-draft-jamie|high
2026-07-19|assisted|reporting|atc-completed-ticket-synthesis-6-vroom|high
2026-07-19|autonomous|reporting|atc-slack-channel-scan-13ch|high
2026-07-19|autonomous|reporting|stakeholder-slack-activity-lookup-4ppl|high
2026-07-23|autonomous|reporting|atc-completed-ticket-synthesis-6-tickets|high
2026-07-23|autonomous|reporting|pitcrew-slack-monitoring-1day|high
2026-07-30|assisted|reporting|osci-meeting-briefing-html-gdoc|high
2026-07-30|enhanced|research|gemini-transcript-cross-referencing|medium
2026-07-30|autonomous|project-tracking|rog-project-file-update|high
2026-07-30|assisted|research|slack-dm-confluence-cross-reference|high
2026-07-30|assisted|documentation|confluence-5page-gap-updates|high
2026-07-30|assisted|tool-building|distribution-fa-llm-wiki-creation|high
2026-08-02|assisted|research|autosd-jumpstarter-gap-research-response-draft|high
2026-08-03|enhanced|tool-building|gitlab-cicd-podman-executor-pipeline-debug|high
2026-08-03|assisted|tool-building|ruff-lint-56-errors-autofix-manual|high

