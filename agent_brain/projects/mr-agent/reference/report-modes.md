---
last_accessed: 2026-06-21
access_count: 1
created: 2026-06-21
---

# Report Modes

Three operating modes controlling the time window and report label.

| Mode | Lookback | Default schedule | Subject format |
|------|----------|-----------------|----------------|
| `daily` | 1 day | Mon-Fri 07:30 | `[Daily] Team Activity – YYYY-MM-DD` |
| `weekly` | 7 days | Sunday 07:30 | `[Weekly] Team Summary – week of YYYY-MM-DD` |
| `weekend` | 4 days (Thu-Sun) | Sunday 07:00 | `[Weekend] Team Activity – YYYY-MM-DD` |

**Override:** `--days N` overrides the default lookback for any mode.

**Recipient:** `aefrat@redhat.com`

## Cron schedule

Weekend arrives 30 minutes before weekly on Sundays — focused Thu-Sun view first, then full 7-day context.

```
# Weekend — Sunday 07:00
0 7 * * 0   generate_report.py --mode weekend

# Weekly — Sunday 07:30
30 7 * * 0  generate_report.py --mode weekly

# Daily — Mon-Fri 07:30
30 7 * * 1-5  generate_report.py --mode daily
```

Logs: `/tmp/manager_report.log`

## Mode selection heuristic

When the user doesn't specify a mode:
- Sunday → weekend (most useful for weekend catch-up)
- Mon-Fri → daily
- Saturday → weekly (rare; full week in review)
