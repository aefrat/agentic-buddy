# Local AI Agents

Agents available on this workstation. Open a terminal in the repo and start a session.

## Active

| Agent | Repo | How to run | What it does |
|-------|------|------------|--------------|
| **Pipelines Debugger** | `~/git/pipelines-debugger` | `cd ~/git/pipelines-debugger && claude` | Diagnoses CI/CD pipeline failures for AutoSD/RHIVOS. Structured diagnosis: root cause, evidence, recommendations. Skills for GitLab query, artifact fetch, health checks, Slack search. |
| **Agentic Buddy** | `~/agentic-buddy` | `cd ~/agentic-buddy && claude` | Persistent context processor with file-based memory. Captures tasks, decisions, ideas. Runs manager report, QC reports, Slack scans, 1:1 processing. |

## Setup notes

### Pipelines Debugger
- **Repo:** `~/git/pipelines-debugger` (cloned from `gitlab.cee.redhat.com/automotive/ai/agents/toolchain/pipelines-debugger`)
- **Harness:** Claude Code (CLAUDE.md identity, skills in `skills/`, tools in `tools/`)
- **Env:** `.env` configured with `GITLAB_PRIVATE_TOKEN_UP`, `GITLAB_PRIVATE_TOKEN_DOWN`, `SLACK_XOXC_TOKEN`, `SLACK_XOXD_COOKIE`
- **Python deps:** Synced via `uv sync --extra dev`
- **CLI tools:** `bin/check-health`, `bin/compare-pipelines`, `bin/compute-stats`, `bin/fetch-artifacts`, `bin/fetch-test-log`, `bin/gitlab-query`, `bin/slack-search`
- **Policy:** Covered under Red Hat Open Source AI Technologies blanket approval (MIT license, Gemini/Claude approved). CI/CD log data classification needs Velocity AI confirmation (see project file).
