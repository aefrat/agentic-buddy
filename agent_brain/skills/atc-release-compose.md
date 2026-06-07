---
last_accessed: 2026-06-07
access_count: 1
created: 2026-06-07
---

# Skill: ATC Release Compose

## When to use

Triggered by:
- "trigger a compose for RHIVOS-X.Y.Z"
- "create a release config for RCN"
- "kick off a compose build"
- "generate-compose is stuck / failed"
- "how do I trigger a release build?"
- "what's the status of the compose pipeline?"

## Repos

| Repo | URL |
|------|-----|
| downstream-pipelines-as-code (DPAC) | `https://gitlab.cee.redhat.com/automotive/pipe-x/downstream-pipelines-as-code` |
| rhivos (Pungi config) | `https://gitlab.cee.redhat.com/automotive/pipe-x/rhivos` |

GitLab CEE API base: `https://gitlab.cee.redhat.com/api/v4`
Auth header: `PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}` (exported in `~/.bashrc`)

URL-encoded project paths:
- DPAC: `automotive%2Fpipe-x%2Fdownstream-pipelines-as-code`
- rhivos: `automotive%2Fpipe-x%2Frhivos`

---

## Intent 1 — Create a new release config

Use when starting a new RC or release stream (e.g. `RHIVOS-2.0-RC1`).

### Step 1 — Find the closest existing config to copy from

```bash
source ~/.bashrc
# List existing release configs
curl -s "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Fdownstream-pipelines-as-code/repository/tree?path=.gitlab/release-configs&per_page=50" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}" | python3 -c "import sys,json; [print(f['name']) for f in json.load(sys.stdin)]"
```

Pick the closest existing config (e.g. previous RC). Read it:

```bash
CONFIG=RHIVOS-1.0.0-RC2.yml   # replace with chosen source
curl -s "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Fdownstream-pipelines-as-code/repository/files/.gitlab%2Frelease-configs%2F${CONFIG}/raw?ref=main" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}"
```

### Step 2 — Identify what to change

Key fields to update in the new config:

| Variable | What it means | Example |
|----------|---------------|---------|
| `RELEASE_NAME` | Human-readable name | `RHIVOS-1.0.0-RC3` |
| `ODCS_PUNGI_CONFIG_BRANCH` | Branch in rhivos.git with Pungi config | `rhivos-1.0.0` |
| `AIB_REF` | Automotive Image Builder version | `aib-0.3.x` or `main` |
| `GATOR_CONF` | Gating rules config path | `config/RHIVOS-1/RHIVOS-1.0.0-promote.yaml` |
| `CUSTOM_IMAGES_REF` | Pin for custom images | `0.1.4` |
| `SAMPLE_IMAGES_REF` | Pin for sample images | `0.9.3` |

For dev/nightly builds use `main` refs. For RCs, pin to tested versions.

Verify the `ODCS_PUNGI_CONFIG_BRANCH` exists in rhivos.git:
```bash
BRANCH=rhivos-1.0.0   # replace
curl -s "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Frhivos/repository/branches/${BRANCH}" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}" | python3 -c "import sys,json; d=json.load(sys.stdin); print('EXISTS:', d.get('name','NOT FOUND'))"
```

### Step 3 — Create a branch in DPAC and push the new config

```bash
NEW_RELEASE=RHIVOS-1.0.0-RC3       # the new release name
BRANCH_NAME="add-release-config-${NEW_RELEASE}"
NEW_CONFIG_CONTENT='variables:
  RELEASE_NAME: "RHIVOS-1.0.0-RC3"
  ODCS_RAW_CONFIG_NAME: "rhivos"
  ODCS_PUNGI_CONFIG_BRANCH: "rhivos-1.0.0"
  AIB_REF: "aib-0.3.x"
  PAC_JOBS_TAG: "latest"
  CUSTOM_IMAGES_REF: "0.1.4"
  SAMPLE_IMAGES_REF: "0.9.3"
  GATOR_CONF: "config/RHIVOS-1/RHIVOS-1.0.0-promote.yaml"
  DISABLE_PROMOTE_BUILDER: "false"
  TAG_MONTHLY_BUILDS: "false"'

# Create branch from main
curl -s -X POST "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Fdownstream-pipelines-as-code/repository/branches" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "{\"branch\": \"${BRANCH_NAME}\", \"ref\": \"main\"}" | python3 -c "import sys,json; d=json.load(sys.stdin); print('Branch:', d.get('name','ERROR'), d.get('message',''))"

# Commit the new config file
FILE_PATH=".gitlab%2Frelease-configs%2F${NEW_RELEASE}.yml"
ENCODED_CONTENT=$(echo "$NEW_CONFIG_CONTENT" | base64 -w 0)

curl -s -X POST "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Fdownstream-pipelines-as-code/repository/files/${FILE_PATH}" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "{\"branch\": \"${BRANCH_NAME}\", \"content\": \"${NEW_CONFIG_CONTENT}\", \"commit_message\": \"Add release config for ${NEW_RELEASE}\"}" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('File created:', d.get('file_path','ERROR'), d.get('message',''))"
```

### Step 4 — Open an MR

```bash
curl -s -X POST "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Fdownstream-pipelines-as-code/merge_requests" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "{\"source_branch\": \"${BRANCH_NAME}\", \"target_branch\": \"main\", \"title\": \"Add release config for ${NEW_RELEASE}\", \"description\": \"Adds .gitlab/release-configs/${NEW_RELEASE}.yml to enable compose pipeline for this release.\"}" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('MR URL:', d.get('web_url','ERROR'))"
```

Get MR reviewed and merged before proceeding to trigger.

---

## Intent 2 — Trigger a compose build

Use after the release config is merged to DPAC main.

The compose pipeline is triggered by **creating a tag in rhivos.git** that matches the release config filename (e.g. tag `RHIVOS-1.0.0-RC3` loads `RHIVOS-1.0.0-RC3.yml`).

### Step 1 — Verify prerequisites

```bash
NEW_RELEASE=RHIVOS-1.0.0-RC3

# 1. Config file exists in DPAC main
curl -s -o /dev/null -w "%{http_code}" \
  "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Fdownstream-pipelines-as-code/repository/files/.gitlab%2Frelease-configs%2F${NEW_RELEASE}.yml/raw?ref=main" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}"
# Expect: 200

# 2. Tag does NOT already exist in rhivos
curl -s -o /dev/null -w "%{http_code}" \
  "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Frhivos/repository/tags/${NEW_RELEASE}" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}"
# Expect: 404 (tag doesn't exist yet)
```

### Step 2 — Create the tag in rhivos.git

```bash
NEW_RELEASE=RHIVOS-1.0.0-RC3
REF=main   # or specific commit SHA / branch to tag

curl -s -X POST "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Frhivos/repository/tags" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "{\"tag_name\": \"${NEW_RELEASE}\", \"ref\": \"${REF}\", \"message\": \"Release ${NEW_RELEASE}\"}" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('Tag:', d.get('name','ERROR'), '|', d.get('message',''))"
```

This immediately triggers the DPAC pipeline.

### Step 3 — Get the pipeline URL

```bash
sleep 10   # give GitLab a moment to create the pipeline
curl -s "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Fdownstream-pipelines-as-code/pipelines?ref=${NEW_RELEASE}&per_page=3" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}" \
  | python3 -c "import sys,json; pipes=json.load(sys.stdin); [print(f\"Pipeline {p['id']}: {p['status']} — {p['web_url']}\") for p in pipes]"
```

### Step 4 — Monitor generate-compose job

```bash
PIPELINE_ID=12345   # from step above

# Get the generate-compose job
curl -s "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Fdownstream-pipelines-as-code/pipelines/${PIPELINE_ID}/jobs?per_page=50" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}" \
  | python3 -c "import sys,json; jobs=json.load(sys.stdin); [print(f\"{j['name']}: {j['status']}\") for j in jobs if 'compose' in j['name'].lower() or j['status'] in ('failed','running')]"
```

Expected pipeline stages in order:
1. `initiate-workspace` → `generate-compose` ← *ODCS step, takes 10–30 min*
2. `check-repoclosure` — validates compose
3. `build-*-image` jobs — parallel image builds
4. `smoke-tests-*` — hardware testing
5. `promote-packages-in-brew` — gating via Gator
6. `generate-cat-manifest`, `delta-analysis` — compliance

---

## Intent 3 — Troubleshoot a stuck or failed compose

### Failure mode lookup

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `generate-compose` fails immediately | Kerberos auth failure (KEYTAB_ODCS secret) | Check `krb5_trace.log` artifact; verify secret is valid in DPAC CI/CD settings |
| `generate-compose` stuck >30 min | ODCS service overloaded or config name wrong | Check `https://odcs.engineering.redhat.com/`; verify `ODCS_RAW_CONFIG_NAME=rhivos` |
| ODCS error: config not found | Wrong `ODCS_RAW_CONFIG_NAME` | Should be `rhivos` for all RHIVOS releases |
| ODCS error: branch not found | `ODCS_PUNGI_CONFIG_BRANCH` doesn't exist in rhivos.git | Verify branch exists (see Intent 1 Step 2) |
| Downstream jobs use wrong compose | COMPOSE_ID artifact not passed correctly | Check `generate-compose` artifacts; ensure `needs: ["generate-compose"]` in job |
| `check-repoclosure` fails | Missing package dependencies in compose | Pungi config issue — escalate to rhivos.git maintainers |

### Get job logs via API

```bash
PIPELINE_ID=12345
JOB_NAME="generate-compose"

JOB_ID=$(curl -s "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Fdownstream-pipelines-as-code/pipelines/${PIPELINE_ID}/jobs?per_page=50" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}" \
  | python3 -c "import sys,json; jobs=json.load(sys.stdin); print(next(j['id'] for j in jobs if j['name']=='${JOB_NAME}'), end='')")

curl -s "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Fdownstream-pipelines-as-code/jobs/${JOB_ID}/trace" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}" | tail -50
```

### Retry a failed job

```bash
curl -s -X POST "https://gitlab.cee.redhat.com/api/v4/projects/automotive%2Fpipe-x%2Fdownstream-pipelines-as-code/jobs/${JOB_ID}/retry" \
  -H "PRIVATE-TOKEN: ${GITLAB_CEE_TOKEN}" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('Retried job:', d.get('id'), d.get('status'))"
```

---

## Key concepts

- **ODCS** (On-Demand Compose Service) — Red Hat internal service at `https://odcs.engineering.redhat.com/`. Takes a Pungi config and generates an RPM repository (compose). ATC's compose is named `rhivos`.
- **Pungi config** — Lives in `rhivos.git`. Defines which RPM packages (from Koji/Brew) go into the OS. One branch per release stream (e.g. `rhivos-1.0.0`, `rhivos-2.0-core`).
- **COMPOSE_ID** — Identifier output by `generate-compose`. Downstream build jobs use it to find the RPM repo. Format: `rhivos-YYYYMMDD.N`.
- **BUILD_BRANCH** — GitLab CI variable that selects which release config to load for non-tag (dev/nightly) pipelines.
- **Gator** — Release gating system. Triggered by `promote-packages-in-brew` job after successful build. May require manual approval.
