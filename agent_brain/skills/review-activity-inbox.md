---
last_accessed: 2026-09-02
access_count: 0
created: 2026-09-02
---

# Skill: Review activity inbox (personal status update)

## When to use

Triggered by: "status update", "what needs my attention", "go over my
Slack mentions and emails", "what happened while I was out", "catch me up",
"review my inbox", or any request to synthesize what needs the *user's*
attention across their own Slack mentions/DMs and email over a recent window.

Distinct from sibling skills:
- `scan-slack-channels` — team/channel activity (what the team is doing).
- `person-slack-lookup` — a specific *other* person's activity.
- This skill — what needs *the user's own* attention (mentions + DMs + mail),
  synthesized into a prioritized status update.

## Procedure

### 1. Set the time window

Default to the last 24h (or "since last review"). If the user names a
window ("last day", "this week", "while I was out"), use it.

**Purpose:** Bounds the search so the output is a focused status update,
not an archive dump.

### 2. Pull the user's Slack mentions and DMs

- Resolve the user's own Slack user ID via `mcp__slack-mcp__whoami`.
- `mcp__slack-mcp__search_messages` with query `<@USER_ID>` for the window
  to find where others mentioned the user.
- Include DMs and mpdm threads where the user is active.
- For each significant hit, `mcp__slack-mcp__get_thread` to read the full
  thread — the parent message alone usually hides the decision or the ask.

**Purpose:** Mentions and DMs are the highest-signal "someone needs you"
channel. Threads reveal what actually changed or what is being asked.

**Constraint:** Slack access is read-only via the community `slack-mcp`
server only (Rule 20). Never post.

### 3. Pull recent email

Use the `google:gws-gmail` skills to read messages from the window.
Focus on: direct asks, deadlines, approvals awaited, service/system
notices (token expiry, migrations, CMDB/ServiceNow tasks), and calendar
invites tied to decisions.

**Purpose:** Many action items and deadlines arrive only by email
(compliance, HR/Workday, infra migrations) and never appear in Slack.

### 4. Cross-reference against known context

Before presenting, check items against `agent_brain/deferred.md`,
active project files, and CLAUDE.md Active context. Mark what is genuinely
new vs. already tracked.

**Purpose:** Avoids re-surfacing items the user already knows about;
highlights the net-new signal. (See `agent_brain/concepts/` on filtered
vs. raw capture — filtered capture creates value.)

### 5. Synthesize a prioritized status update

Group by urgency, not by source:
- **Needs action** — direct asks, decisions pending, deadlines within the
  window. Include the ask, who is waiting, and the source link.
- **Awareness** — context shifts, FYIs, things to watch (no action yet).

For each item: one line of what it is + why it matters + the source.

### 6. Capture, don't just report

Write actionable items to `user/` (inbox or the relevant file) and any
near-term deadlines to `agent_brain/deferred.md`. Reported ≠ captured —
a status update that isn't written is lost next session (Rule 9).

## Success criteria

- User's own Slack user ID confirmed via `whoami` (not assumed).
- Both @mentions and DMs searched; significant threads read in full.
- Email window scanned for asks/deadlines/notices.
- Items cross-referenced against deferred queue + projects (new vs. known).
- Output grouped by needs-action vs. awareness, each with a source.
- Actionable items written to `user/`; deadlines to `deferred.md`.

## Disconfirmation gate

Before finalizing, ask: "Am I flagging something as needs-action that is
actually already handled or already tracked?" Demote anything already in
the deferred queue or resolved in a project file to awareness (or drop it).
The value of this skill is separating the true signal from the noise the
user has already seen.

## Notes

- Source authority: read the thread/email, don't infer the ask from
  subject lines or channel proximity (temporal proximity is not content
  attribution).
- This is a read-and-synthesize skill: no writes to Slack, no email sends
  unless the user explicitly asks.
