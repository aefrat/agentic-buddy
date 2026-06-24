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

Access: community slack-mcp MCP server (read-only, configured in `~/.mcp.json`). No tokens or credentials needed.

### Channels

| Channel | ID |
|---|---|
| team-toolchain-automotive | C04JDFLHJN6 |
| alerts-auto-toolchain | C04QLT849KN |
| team-auto-follow-on-activities | *(resolve via `get_channel_id_by_name`)* |

### Queries

**a. #team-toolchain-automotive (primary, last 7 days):**
```
mcp__slack-mcp__search_channel_messages(channel_id="C04JDFLHJN6", query="*", limit=30, sort="timestamp")
```

**b. #alerts-auto-toolchain (pipeline failures):**
```
mcp__slack-mcp__search_channel_messages(channel_id="C04QLT849KN", query="*", limit=20, sort="timestamp")
```

**c. #team-auto-follow-on-activities (FoA/validators):**
```
mcp__slack-mcp__search_channel_messages(channel_id=<RESOLVE_ID>, query="*", limit=20, sort="timestamp")
```

**d. Cross-channel keyword search:**
```
mcp__slack-mcp__search_messages(query="\"core-rpms\" OR execopen OR VROOM-31017", limit=20, sort="timestamp")
```

### Known issues
- MCP server is read-only. Never attempt write operations.
- If MCP tools return errors, flag in the report — don't silently skip.

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
