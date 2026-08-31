---
last_accessed: 2026-08-31
access_count: 2
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

## RHIVOS 2.0 Developer-VM rebuild (ProdSec blocker) — status as of 2026-08-31

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

**Rejected dead-ends** (Charles Timko proposals; Petr Sabata rebutted):
- Swap RHEL release package via a "magic RPM" — done as a 1.0 workaround only; not
  user-friendly, can't be guaranteed, distributing it is problematic. Not feasible.
- Containers self-subscribing — RHSM design forbids (containers inherit host subs).
  Already explored.

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
