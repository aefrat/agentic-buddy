---
last_accessed: 2026-06-07
access_count: 1
created: 2026-06-07
---

# Skill: Engineering Manager Report

## When to use

Triggered by:
- "run the daily report" / "run the weekly report"
- "generate the manager report"
- "resend the daily/weekly"
- "rerun the report"

Full reference (script details, team members, Jira config, API notes):
`/home/aefrat/claude/manager-report/CLAUDE.md`

## Procedure

### 1. Generate the report

```bash
source ~/.bashrc
python3 /home/aefrat/claude/manager-report/generate_report.py --mode daily   --output /tmp/daily_report.html
python3 /home/aefrat/claude/manager-report/generate_report.py --mode weekly  --output /tmp/weekly_report.html
python3 /home/aefrat/claude/manager-report/generate_report.py --mode weekend --output /tmp/weekend_report.html
```

Use `--mode daily` (1-day lookback), `--mode weekly` (7-day), or `--mode weekend` (4-day, Thu–Sun). Optional `--days N` overrides the look-back window.

The script handles token cache clearing, fetches Jira + GitLab + GitHub + Google Docs + Slack, generates per-team AI summaries inline via `claude -p`, and writes the HTML report.

### 2. Send via email

```bash
gws gmail +send --to aefrat@redhat.com \
  --subject "[Daily] Team Activity – $(date +%Y-%m-%d)" \
  --body "$(cat /tmp/daily_report.html)" --html

gws gmail +send --to aefrat@redhat.com \
  --subject "[Weekly] Team Summary – week of $(date +%Y-%m-%d)" \
  --body "$(cat /tmp/weekly_report.html)" --html

gws gmail +send --to aefrat@redhat.com \
  --subject "[Weekend] Team Activity – $(date +%Y-%m-%d)" \
  --body "$(cat /tmp/weekend_report.html)" --html
```

## Scheduled runs

System crontab (`crontab -l`):
- **Daily**: Mon–Fri at 07:30 — `--mode daily`
- **Weekly**: Sundays at 07:30 — `--mode weekly`

Logs: `/tmp/manager_report.log`
