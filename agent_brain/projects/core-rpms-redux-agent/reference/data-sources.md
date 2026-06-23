---
last_accessed: 2026-06-23
access_count: 0
created: 2026-06-23
---

# Core RPMs Redux — Data Sources

## Jira

CLI: `jira` (per CLAUDE.md Rule 18 — never raw API calls).

### Queries

**a. Epic details:**
```bash
jira issue view VROOM-31017 --plain
```

**b. All children/linked issues of VROOM-31017:**
```bash
jira issue list -q "parent = VROOM-31017 OR 'Epic Link' = VROOM-31017 ORDER BY status ASC, key ASC" --plain --columns key,summary,status,assignee,type
```

**c. Known open work tickets (remaining work):**
```bash
jira issue list -q "key in (VROOM-40719, VROOM-40584, VROOM-37096, VROOM-37575, VROOM-30619) ORDER BY key ASC" --plain --columns key,summary,status,assignee,type
```

**d. Toolchain umbrella (VROOM-31421) subtasks:**
```bash
jira issue list -q "parent = VROOM-31421 ORDER BY status ASC, key ASC" --plain --columns key,summary,status,assignee,type
```

**e. Related epics:**
```bash
jira issue list -q "key in (VROOM-37039, VROOM-29696, VROOM-38899)" --plain --columns key,summary,status,assignee,type
```

### Known issues
- Atlassian API token "Avi2" expires Jun 27, 2026 — needs rotation.
- Not sprint-based — no sprint queries needed.

## Slack

Auth: `$SLACK_XOXC_TOKEN` + `$SLACK_XOXD_COOKIE` from `~/.bashrc` (per CLAUDE.md Rule 20 — never Slack MCP plugin).

### Searches

**a. #team-toolchain-automotive (primary, last 7 days):**
```bash
source ~/.bashrc
curl -s "https://redhat.enterprise.slack.com/api/search.messages" \
  -H "Authorization: Bearer $SLACK_XOXC_TOKEN" \
  -H "Cookie: d=$SLACK_XOXD_COOKIE" \
  --data-urlencode "query=in:#team-toolchain-automotive" \
  -d "sort=timestamp&sort_dir=desc&count=30"
```

**b. #alerts-auto-toolchain (pipeline failures):**
```bash
source ~/.bashrc
curl -s "https://redhat.enterprise.slack.com/api/search.messages" \
  -H "Authorization: Bearer $SLACK_XOXC_TOKEN" \
  -H "Cookie: d=$SLACK_XOXD_COOKIE" \
  --data-urlencode "query=in:#alerts-auto-toolchain" \
  -d "sort=timestamp&sort_dir=desc&count=20"
```

**c. #team-auto-follow-on-activities (FoA/validators):**
```bash
source ~/.bashrc
curl -s "https://redhat.enterprise.slack.com/api/search.messages" \
  -H "Authorization: Bearer $SLACK_XOXC_TOKEN" \
  -H "Cookie: d=$SLACK_XOXD_COOKIE" \
  --data-urlencode "query=in:#team-auto-follow-on-activities" \
  -d "sort=timestamp&sort_dir=desc&count=20"
```

**d. Cross-channel keyword search:**
```bash
source ~/.bashrc
curl -s "https://redhat.enterprise.slack.com/api/search.messages" \
  -H "Authorization: Bearer $SLACK_XOXC_TOKEN" \
  -H "Cookie: d=$SLACK_XOXD_COOKIE" \
  --data-urlencode "query=\"core-rpms\" OR execopen OR VROOM-31017" \
  -d "sort=timestamp&sort_dir=desc&count=20"
```

### Known issues
- Tokens expire without warning. `invalid_auth` response means `~/.bashrc` tokens need refresh.
- Use `redhat.enterprise.slack.com` (not `slack.com`) for API endpoint.

## Google Docs

CLI: `gws docs` (per CLAUDE.md Rule 18).

### Documents

| Name | Document ID | Usage |
|------|-------------|-------|
| ToolChain Open Sync | `1TegJmbETVM627zvw5hj8F5NtiQvvJ40OSbgkGlz-pWw` | Weekly sync notes, latest decisions |
| Workstreams doc | `1uakPWEkSvMksJ9XAfPHlU_h9mMVpcIr9F2uufJw4-Ek` | Workstream status, cross-team context |

### Fetch pattern
```bash
gws docs documents get --params '{"documentId": "<DOC_ID>"}' 2>/dev/null | python3 -c "
import json, sys
raw = sys.stdin.read()
decoder = json.JSONDecoder()
data, _ = decoder.raw_decode(raw)
def extract_text(content):
    result = []
    if isinstance(content, dict):
        if 'paragraph' in content:
            for elem in content['paragraph'].get('elements', []):
                if 'textRun' in elem:
                    result.append(elem['textRun'].get('content', ''))
        if 'table' in content:
            for row in content['table'].get('tableRows', []):
                row_texts = []
                for cell in row.get('tableCells', []):
                    cell_text = []
                    for c in cell.get('content', []):
                        cell_text.extend(extract_text(c))
                    row_texts.append(''.join(cell_text).strip())
                result.append(' | '.join(row_texts) + '\n')
    return result
body = data.get('body', {})
for item in body.get('content', []):
    text = extract_text(item)
    if text:
        print(''.join(text), end='')
"
```

### Known issues
- `gws docs` returns empty on 403. Run `gws auth status` first to verify.
- Can expire silently.
