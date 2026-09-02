---
last_accessed: 2026-09-02
access_count: 3
created: 2026-08-26
---

# How Konflux builds qcow images

Research question: How does Konflux currently build qcow (disk/VM) images?
Sources: internal user docs (https://konflux.pages.redhat.com/docs/users/),
public docs (https://konflux-ci.dev/docs/), the konflux-ci/build-definitions
repo, and real-world consumers (osbuild/bootc-foundry, Fedora Copr).

## Short answer

Konflux does not build qcow images with a bespoke disk-imaging engine. It builds
a **bootc container image** with its standard buildah pipeline, then converts that
container into a disk image (qcow2, raw, iso, vhd, gce, ...) using the upstream
**bootc-image-builder** tool, wired in as a Tekton task named **`build-vm-image`**.
So it is a two-stage flow: build OCI bootc image -> convert to disk image.

## The mechanism

1. **Stage 1 - build the bootc container.** Use a normal Konflux pipeline
   (e.g. `docker-build` / `docker-build-oci-ta`) with buildah to build a derived
   bootc container image from a Containerfile, pushed to the registry
   (Quay via image-controller).

2. **Stage 2 - convert to disk image.** The `build-vm-image` Tekton task
   (`task/build-vm-image/0.1/` in konflux-ci/build-definitions) runs
   **bootc-image-builder** (BIB, e.g. `quay.io/centos-bootc/bootc-image-builder`)
   to turn the bootc container into a disk image.

### `build-vm-image` task details

- **Tool:** bootc-image-builder (BIB). Note: the bootc-image-builder repo has been
  merged into osbuild/image-builder and archived.
- **Supported IMAGE_TYPE formats:** qcow2 (native, already compressed), raw (.gz),
  iso (.gz), vhd (.gz), gce (tarball).
- **Key params:** `SOURCE_ARTIFACT` (input bootc image), `IMAGE_TYPE`,
  `BIB_CONFIG_FILE` (defines builder image + source image), `CONFIG_TOML_FILE`
  (optional osbuild config), `OUTPUT_IMAGE`, `PLATFORM`,
  `ENTITLEMENT_SECRET` / `ACTIVATION_KEY` (optional RHEL subscription).
- **How it runs:** provisions an SSH build host, `sudo podman pull` of the BIB
  image and source image, then
  `sudo podman run ... $BOOTC_BUILDER_IMAGE $IMAGE_TYPE_ARGUMENT --local $TAGGED_AS`,
  producing the disk image in `/output`.
- **Push:** packages the disk artifact with `buildah manifest` and pushes to a
  registry via `buildah manifest push` / `skopeo copy` (disk image stored as an
  OCI artifact).
- **Outputs:** `IMAGE_DIGEST`, `IMAGE_URL`, `IMAGE_REFERENCE`.

## What the internal user docs say (konflux.pages.redhat.com/docs/users)

Checked 2026-08-26. The **internal** user docs do **not** document the qcow/disk
build mechanism either — same gap as the public docs:

- The **Building** section lists only container-oriented pages and tasks. The
  "Task documentation" page enumerates tasks from `konflux-ci/container-build-catalog/task`
  (buildah, git-clone, prefetch-dependencies, ...) - no `build-vm-image`, bootc,
  or bootc-image-builder task appears.
- The only disk-image page is **"Releasing Disk Images to CDN"**
  (`releasing/releasing-disk-images-to-cdn.html`), which covers *releasing*, not
  building. It uses the **`push-disk-images-to-cdn`** release pipeline to publish
  ISOs, qcows, and tarballs to CDN.
  - Requires: an existing ReleasePlan + ReleasePlanAdmission; a Content Set +
    Pulp repository for the disk files; an empty RPM Pulp repo (for visibility in
    unified-downloads); Product + Product Versions in Content Gateway.
  - The ReleasePlanAdmission maps the **source file inside a container image**
    (e.g. `disk.qcow2`) -> destination Pulp repo + target version, with optional
    Content Gateway (Developer Portal) metadata.
- **Takeaway:** the internal docs confirm the disk image is produced/stored as
  (or inside) a container/OCI artifact and then *released* via a dedicated
  pipeline; the *build* step (bootc container -> `build-vm-image`/BIB) is assumed
  and lives in the build-definitions catalog + consumer projects, not the docs.

## Notable gaps / caveats

- Konflux's published docs (konflux-ci.dev/docs) focus almost entirely on
  container image builds and do **not** document qcow/disk/bootc builds. The
  disk-image capability lives in the build-definitions catalog (`build-vm-image`)
  and in consumer projects, not in the user-facing docs.
- Upstream Konflux runs BIB per-arch (VM per architecture). Fedora Konflux
  instance is limited to x86_64 + aarch64; other arches need an internal RH instance.
- Real-world reference implementations:
  - **osbuild/bootc-foundry** - base bootc Containerfiles per target
    (suffixes: qcow2, ec2, azure, gce, installer), built in Konflux via `.tekton`.
  - **Fedora Copr** - GitOps commit triggers multi-arch OCI build in Konflux,
    then BIB produces the disk images.
- Known instability: upstream BIB Konflux pipeline outages tracked (KONFLUX-9346).

## DIRECTION CHANGE (2026-09-01): Konflux ruled out — path is Brew

**Juanje's new plan (VROOM-52268 latest comment + Slack thread, Sep 1):** Konflux
is **eliminated for this image on a hard technical constraint**, not a timeline
preference. Reason: **Konflux can only build `bootc` images — even when converted
to VM/qcow2, internally it remains an immutable image. The Developer VM image must
be mutable.** So Konflux cannot build it. This settles the Brew-vs-Konflux debate
that had dominated the thread (it was previously leaning Konflux for long-term
automation).

**Verified (2026-09-02): Juanje's mutability claim is correct.** Checked against the
bootc filesystem docs, bootc-image-builder (BIB) docs, and RHEL image-mode docs:
- A bootc system is **immutable by default** — with composefs, `/usr` and `/` are
  read-only ("part of the same immutable image"); only `/etc` and `/var` are writable.
  `dnf install` does **not** persist across reboots; persistent change = rebuild the
  container image + `bootc upgrade`.
- **BIB only converts bootc containers → disk images (image mode/ostree).** It cannot
  emit a traditional package-mode (mutable, dnf-persistent) system. The bootc→qcow
  conversion packages the container; it does not change its immutable nature.
- There **is** a writability knob — `transient = true` (transient root) makes the whole
  rootfs writable at runtime, and state overlays give persistent overlays on specific
  dirs — **but transient-root writes are lost on reboot, and image updates override any
  local changes.** Neither gives a normal, persistently-mutable `dnf install` Developer VM.
- A persistently-mutable package-managed VM = **"package mode"**, produced by plain
  **osbuild/Image Builder blueprints** (the Brew path), not by BIB.
- **Extra nail:** Konflux's *only* disk-image path is `build-vm-image` (wraps BIB) and
  it **requires a bootc container input**. Konflux has no package-mode image path at all.
- The only way to keep Konflux would be to **redesign the Developer VM as a bootc/
  image-mode system** — which changes the developer UX (rebuild-image instead of
  `dnf install`); not viable for a developer VM. → Brew is the correct tool.

**New path: Brew/Koji + Image Builder (osbuild / osbuild-composer)** via the Koji
integration. Docs Juanje linked:
- Upstream: https://osbuild.org/docs/hosted/image-builder-koji/#building-images-via-koji-integration
- Internal RH: https://osbuild.pages.redhat.com/internal-guides/image-builder-service/koji-integration.html#internal-brew-integration

**Supporting Slack context (mpdm group DM, Sep 1):**
- **Joe Amato** confirmed "we are able to build qcow images today in Brew" and
  pulled in **Tomas Kopecek** for the build details/questions.
- Earlier in the thread Joe had flagged that there is **no existing path** he's
  aware of for building these images in Konflux and pushing to CDN — the risk is
  in the unknowns.
- **cfreitas (Christine)**: RHIVOS "will eventually need to convert to Konflux" —
  Konflux remains the org's long-term target, but the mutable-image constraint
  means it does not apply to *this* image as currently designed. Do what's right
  for the release now.
- **Pavol Brilla correction:** the artifact is the **RHIVOS tooling / developer-VM**
  ("developer-vm is RHIVOS, but not production one") — not "install RHIVOS using a
  non-RHIVOS VM."

**Open items on the Brew path (as of Sep 1):**
- Awaiting **Tomas Kopecek's** guidance on the Brew/Koji + Image Builder specifics.
- **CDN publish step is manual** under Brew (Brew builds; someone pushes to CDN).
  Who publishes: ideally RHIVOS Toolchain distribution owner, but expertise is
  still building — consult **Leon Kang (DST releng)**.
- **Cost center** confirmed: **669** (Avihai, Aug 31). Full label likely
  `EMEA.R&D RHIVOS.669`.
- **Engineering Product IDs** (Aman, Aug 31): RHIVOS 2.0 Core = **1030**, FuSa =
  **931**. Gathered for the Konflux RPA path; still relevant for errata/CDN.
- **Repo IDs** provided by Aman (see ticket): `rhivos-2.0-core-for-<arch>-*` and
  `rhivos-2.0-for-<arch>-*` (rpms/debug/source/files). Candidate CDN destinations:
  `/content/dist/rhivos2/2.0-core/<arch>/files`, `/content/dist/rhivos2/2.0/<arch>/files`
  (unconfirmed whether they map to QCOW).
- **Content Gateway product codes**: still unknown (Kanitha, Eitan checking).

**Note:** the Konflux implementation plan and option analysis below is now historical
for this image (retained for reference and for the eventual Konflux migration of
mutable-image-compatible artifacts). The active path is Brew.

## Brew build + CDN path — how it works (researched 2026-09-02)

Synthesized from the two docs Juanje linked (osbuild.org Koji integration; internal
osbuild.pages.redhat.com Brew integration), the koji-osbuild CLI source, and the ATC
Distribution FA wiki (cdn-publication, knowledge-transfer).

### Part 1 — Build the qcow in Brew

**Tool:** `brew osbuild-image` (Brew is Red Hat's Koji; the **koji-osbuild** plugin
adds this subcommand).

**Architecture:** three plugins — **hub** (new XMLRPC endpoint that creates
`osbuildImage` tasks), **builder** (handles the task, talks to osbuild-composer's Koji
API), **CLI** (submits the task) — plus **osbuild-composer** running as a separate Brew
tenant with dedicated workers. Composer builds the image and uploads the artifact back
into Brew. Pungi can also submit `osbuildImage` tasks (auto per-compose builds) later.

**Command signature** (positional order confirmed from CLI source):
```
brew osbuild-image [options] <name> <version> <distro> <target> <arch> [<arch> ...]
```
- `--image-type` is an **optional flag** (default `guest-image`) — set `--image-type qcow2`.
- `--repo <url>` (repeatable) — point at the RHIVOS 2.0 compose repos in rhsm-pulp.
- Other flags: `--release`, `--customizations <json>`, `--upload-options <json>`
  (cloud targets only — not needed for a plain qcow), ostree flags, `--wait/--nowait`.

**Internal RH reference example** (from the internal guide):
```
brew osbuild-image \
  --upload-options upload-options.json \
  --image-type azure-rhui \
  --repo '<repo-url>' \
  rhel-azure 8.8 rhel-88 guest-rhel-8.8.0-image x86_64 aarch64
```

**Sketch for RHIVOS Developer VM** (exact distro/target/name TBD from Image Builder team):
```
brew osbuild-image \
  --image-type qcow2 \
  --repo <rhivos-2.0-core compose repo url> \
  <name> 2.0 <rhivos-distro> <brew-target> x86_64 aarch64
```

**Prework required before that command can run** (this is where the real effort/unknowns
are — RHIVOS has never had images in Brew):
- **Image Builder team must define a RHIVOS "distro"** in osbuild-composer (the `<distro>`
  positional) + a **Brew build target** + a **whitelisted image/package name**. This is
  the main ask to **Tomas Kopecek** (Joe pulled him in for exactly this).
- Use `redhat-release-automotive(-core)` instead of RHEL's `redhat-release` for SWID
  (Pavol Brilla), sourcing RPMs from the RHIVOS compose (not automotive-image-builder —
  the Developer VM needs no automotive HW support).
- **Why Brew works where Konflux doesn't:** osbuild/Image Builder produces a normal
  **mutable** disk image; Konflux only produces bootc/immutable.

Output: a **qcow2 uploaded to Brew** as a build artifact.

### Part 2 — Publish to CDN → customer portal

The approved chain (Distribution FA wiki): **Brew build → RADAS sign → Errata advisory →
rhsm-pulp repo → Pub CLI `push-staged` → CDN live (Akamai) → teamnado mirrors to customer
portal / unified downloads.**

Concrete CDN steps (same mechanism RHIVOS uses for RPMs today):
1. **Prereqs:** rhsm-pulp repo exists for the version; Product IDs generated (x86_64 +
   aarch64); product listing created; advisory in **PUSH_READY**; Pub CLI access +
   `~/certs/$USER.crt|.key`.
2. **Stage:** `rd-stage-productids --productids-from <url> --release <url> --staging-dir <dir>`
   (run on `rcm-dev-01...redhat.com`).
3. **Push:** `pub push-staged --target cdn-stage --nowait <staging-dir>`, verify, then
   `--target cdn-live --nowait <staging-dir>`.
4. Advisory moves **PUSH_READY → IN_PUSH → SHIPPED_LIVE**; then tell **teamnado** to mirror
   to the customer portal (the portal is just a UI over CDN).
- Image files land in the `.../files` CDN sub-repos — Aman's candidates:
  `/content/dist/rhivos2/2.0-core/<arch>/files` and `/content/dist/rhivos2/2.0/<arch>/files`
  (unconfirmed they map to QCOW). Per the earlier investigation, disk files also need a
  Content Set + Pulp repo, plus an empty RPM Pulp repo for unified-downloads visibility.
- **Pub CLI access is restricted:** Kanitha Chim, Ozan Unsal, `auto-toolchain-service-distribution`.
  So the manual CDN push is done by Kanitha/Ozan.

**Important precedent — Paul's RHIVOS 1.0 developer-images process (VROOM-40519):** for 1.0,
images could **not** be released via CDN, so a workaround was used — request a **Pulp image
repo** (`private.console.redhat.com/api/pulp-content/rhivos[-stage]/`), **upload images to
Pulp** (contact @dkliban, `#wg-team-auto-toolchain-pulp`), then file a **CPCORE ticket** to
surface them at access.redhat.com/downloads (issues → `#forum-teamnado`). VROOM-52268 exists
precisely to move **off** this workaround onto the approved brew→cdn→portal path — but the
"request a Pulp image repo" and "teamnado/CPCORE to show in downloads" pieces likely still
apply in some form.

### Open questions to confirm with the experts

1. **Errata vs direct Pulp upload:** does a qcow go through the **Errata advisory** lifecycle
   (like RPMs, per cdn-publication.md) or a **direct Pulp image-repo upload** (like Paul's 1.0
   route)? "brew→cdn" phrasing implies errata/CDN, but images historically bypassed errata.
   → ask **Tomas Kopecek / Leon Kang (DST) / Kanitha**.
2. Who defines the RHIVOS **distro + Brew target + allowed image name** in osbuild-composer?
   → **Tomas Kopecek** (Image Builder team).
3. Exact `--repo` URLs and `<distro>`/`<target>` strings for RHIVOS 2.0 Core/FuSa.
4. Which CDN `files` repos exist already vs need creating (RHELDST ticket).

## RHIVOS 2.0 Developer-VM rebuild (ProdSec blocker) — Konflux investigation (historical, as of 2026-08-31)

**The problem.** RHIVOS 2.0 introduces two customer-facing *Developer VM* (installer)
qcow2 images — RHIVOS-2.0-Core and RHIVOS-2.0 (FuSa), each x86_64 + aarch64 — used
to install RHIVOS from a non-RHIVOS VM. Today they are built by RHIVOS's own pipeline
(automotive-image-builder / osbuild) and stored in **AWS S3**. **ProdSec blocks
distribution** of images built outside approved tools (Brew/Konflux). Approval chain
(per Kanitha Chim):
- `S3 -> CDN -> customer portal` = **NOT approved** (built outside brew/konflux)
- `Brew|Konflux -> CDN -> customer portal` = **approved** (prodsec-approved build tool)

Key insight: the customer-portal download page is just a UI over the CDN. Once an
image is on CDN, RHIVOS only needs to tell the **teamnado** team to mirror it — no
separate upload step. RHEL images on the download pages all ship via CDN.

**Why there is no exception path (compliance drivers, from Juanje's investigation
doc):**
- **As of May 26, 2026, Chris Wright eliminated exceptions to RH-SDLC company-wide.**
  Only images built via approved systems (Brew/Konflux) and delivered through
  authorized channels (CDN / Unified Downloader) can reach customers. A VP exception
  now requires VP sign-off and is reserved for rare cases — not a viable route here.
- The Developer VM environment falls under **EU Cyber Resilience Act (CRA)** scope —
  mandatory for the EU market. Konflux end-to-end is the cleanest fit for CRA + RH-SDLC.
- **Scope is only these images**, not the full RHIVOS image set. GA "potentially
  September 2026, not confirmed — no locked date, but must be resolved regardless."

**Tickets.**
- **VROOM-52268** (Build developer-vm image via Konflux/image-builder) — *In Progress,
  Blocker*, owner **Juanje Ojeda**. The active workstream. AC: rebuild the 2 images
  (both arches) via Brew or Konflux, tested/smoke-tested. Blocks VROOM-47600
  (access.stage.redhat.com publish image files).
- **RHELDST-44190** (make qcow images available on product pages) — *Resolved*.
  Distribution ticket; closed once it was clear S3-built images can't be distributed
  and the fix is to rebuild. Leon Kang: "you have everything to decide; open a new
  ticket if needed." GA target was beginning of September (tight).

**Two viable build options** (converged in the RHELDST-44190 thread; Tomas Mlcoch
framed them):

1. **Brew + Image Builder (osbuild).** Build the qcow in Brew, then a **manual** push
   to CDN (plus another team for the distribution hop). Lowest barrier / quickest to
   set up for the timeline. Ref: Image Builder onboarding in Brew doc from Project
   Stratosphere (AWS AMI). Recommended "for now" by **Joe Amato** and **Tomas Mlcoch**
   as lowest-risk for GA timing.
2. **Konflux (preferred long-term).** bootc container -> BIB converts to qcow2 ->
   `push-disk-images-to-cdn` ships to CDN — **all automated**, no manual hop. More
   onboarding/admin overhead but strategic direction. Precedent: **RHEL AI already
   does exactly this** (bootc -> qcow2 -> CDN via Konflux); RHEL-for-EKS partially.
   Juanje's investigation: admin part smaller than feared, ~1 sprint total.

Leaning: **Konflux** (Kanitha "tentatively choosing konflux"; Juanje prefers it).
Decision to be pitched with **Petr Sabata**. Difference that tips it: Brew doesn't
connect to CDN publication (extra manual step + team), Konflux does it end-to-end.

**Technical note.** RHIVOS images use automotive-image-builder (AIB, on osbuild) —
but the Developer VM image is *not* for automotive hardware, so it can be built by
Image Builder/Konflux pointing at the RHIVOS compose. The AIB manifest
(`developer-vm.aib.yml`) must be converted to a Konflux-usable form (Containerfile +
bootc builder config). Nothing AIB-special is needed.

**Rejected dead-ends** (investigation doc + thread):
- **Distribute from S3 directly** — violates RH-SDLC (not an authorized channel).
- **Swap redhat-release via a "magic RPM"** — certification collision (Petr); done as a
  1.0 workaround only; not user-friendly, can't be guaranteed, distribution problematic.
- **Container with RHSM subscription** — RHSM design limit: containers inherit the host
  subscription (Pavol Brilla). Already explored.
- **VP exception** — Chris Wright eliminated exceptions (May 26, 2026); VP sign-off only
  for rare cases. Not applicable.

**Deeper option detail (from the investigation doc):**
- *Konflux (Option A):* ~12 configuration artifacts in `konflux-release-data`
  (Application, Components, ReleasePlan, RPA, ECP), all **templated from RHEL AI
  examples**. Containerfile installs from RHIVOS compose repos + `redhat-release-
  automotive(-core)`; BIB config YAML references the bootc container. Uses
  `build-vm-image` task **v0.3** and the `push-disk-images-to-cdn` managed pipeline.
  Bottleneck: **tenant onboarding** (RelEng approval, unknown lead time).
- *Brew (Option B):* `brew osbuild-image <name> <ver> <distro> <target> <arch>
  --image-type qcow2 --repo <compose-url>`, then manual staging (`pub push-staged` ->
  cdn-stage/cdn-live). **SOA-certified** (ProdSec Security Operating Approval); Pungi
  integration possible (auto builds per compose). Bottleneck: **Image Builder team must
  define a RHIVOS "distro"**, plus a Brew target + whitelisted package name; RHIVOS has
  never had images in Brew.
- Both paths need the Content Delivery team to create the **Pulp CDN destination label +
  Content Gateway product codes** (shared external dependency). Neither needs new
  pipeline code. Both teams have **zero prior experience** with their respective path.

**Long-term caveat — BIB deprecation:** bootc-image-builder was **archived upstream
June 2026**. Still supported in the RHEL 10 lifecycle; the replacement is the
`image-builder` CLI. Not a blocker now, but shapes the long-term plan (affects the
Konflux `build-vm-image` path since it wraps BIB).

**Juanje's Konflux implementation plan** (10 steps, ~1 sprint technical): source repo
(Containerfile + .repo + rpms.in.yaml + lockfile + bootc-builder config + .tekton) ->
tenant namespace (MR, ~2 days approval) -> PaC config -> register app in KRD (2
components: bootc + disk-image) -> custom Enterprise Contract Policy (RHIVOS 2.0 repo
IDs not yet in the global approved list) -> Content Gateway product files -> request
Pulp CDN destination (RHELDST ticket) -> ReleasePlanAdmissions -> validate on stage
CDN -> flip to prod. External-dependency timelines (namespace, Pulp, stage CGW) are
the only out-of-control risks.

**Info Juanje still needs** (cc Kanitha Chim, Aman Vishwakarma): (1) Errata Engineering
Product IDs for RHIVOS 2.0 Core and FuSa; (2) exact RHIVOS 2.0 compose repo IDs in
rhsm-pulp; (3) whether RHIVOS-CORE/RHIVOS-FUSA products + a Pulp CDN destination
already exist in Content Gateway; (4) cost-center code for the tenant namespace.

**Options doc:** https://docs.google.com/document/d/10PXqrMHcfT6KvqPhybcEDrhG_IgL51pAKHGW3_CT8-A/edit
**RHEL AI reference:** gitlab.com/redhat/rhel-ai/containers/bootc (bootc->qcow2->CDN via Konflux)

## Key sources

- konflux-ci/build-definitions `task/build-vm-image/0.1/build-vm-image.yaml`
- osbuild/bootc-image-builder (archived -> osbuild/image-builder), osbuild.org/docs/bootc/
- osbuild/bootc-foundry
- Fedora Copr docs (docs.pagure.org/copr.copr), frostyx.cz "Copr builders powered by bootc"
- Red Hat "Using image mode for RHEL" (bootc-image-builder chapters)
