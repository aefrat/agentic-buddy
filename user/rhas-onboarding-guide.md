# RHAS onboarding guide

Updated: 2026-09-09

This guide is a practical orientation to RHAS, the Red Hat Automotive Suite. It combines the current public Jumpstarter documentation, the current `automotive-dev-operator` repository, two internal onboarding documents, and the existing RHAS testing notes.

## 1. What RHAS is

RHAS is an OpenShift-based development and validation platform for automotive operating-system software. Its core workflow is:

```text
Source / configuration
        |
        v
CAIB and automotive-dev-operator
        |  build OCI, bootc, RPM, ISO or other OS artifacts
        v
Artifact registry / artifact service
        |
        v
Jumpstarter service
        |  lease a real or virtual target, flash/provision it, expose interfaces
        v
Developer or CI test client
        |  boot, interact, test, collect logs and results
        v
OpenShift pipelines, Git forge, test systems and release evidence
```

The two names most important to keep straight are:

- `automotive-dev-operator`: the OpenShift operator and API layer for automotive image builds, the Build API, CAIB, workspaces, container builds, catalog management, and Tekton integration.
- Jumpstarter: the hardware access and test execution layer. It manages exporters, clients, leases, drivers, routing, authentication, and access to physical or virtual devices.

RHAS was previously called RHAD, Red Hat Automotive Development. The current internal team name is PitCrew. RHIVOS, Red Hat In-Vehicle Operating System, is the operating-system product that RHAS helps develop, build, provision, and test.

## 2. Architecture in detail

### 2.1 OpenShift is the platform substrate

OpenShift supplies the Kubernetes control plane, namespaces, RBAC, Routes, operator lifecycle, persistent storage, image registries, scheduling, and Tekton/OpenShift Pipelines. RHAS components are installed as operators and configured with Kubernetes custom resources.

The public `automotive-dev-operator` repository currently documents OpenShift 4.18+ and the OpenShift Pipelines Operator as prerequisites. An internal installation draft says 4.17 or later. Treat 4.18+ as the safer current baseline and verify the exact supported version for the RHAS release being installed.

### 2.2 Build plane: CAIB and the builder operator

The builder operator watches declarative build resources and creates Tekton-based build executions. The repository describes two build modes:

- traditional automotive-image-builder manifests;
- modern bootc container builds.

The operator also provides:

- an `ImageBuild` custom resource;
- a Build API server;
- the `caib` CLI;
- artifact serving through OpenShift Routes or publishing to OCI registries;
- workspaces with cross-compilation toolchains and board deployment;
- Shipwright-backed container builds;
- image catalog management.

The main CLI groups are `caib image`, `caib workspace`, `caib container`, and `caib catalog`. Build artifacts are normally stored or exposed through a registry or artifact endpoint so that a later flashing step can consume a stable URI.

Important configuration areas in `OperatorConfig` include:

- `spec.osBuilds`: enablement, PVC or memory-backed workspaces, node selectors, and tolerations;
- `spec.buildAPI`: internal and JWT/OIDC authentication, client ID, issuer, audience, and claim mapping;
- `spec.jumpstarter`: Jumpstarter namespace, CLI image, target selectors, and flash command templates.

### 2.3 Hardware plane: Jumpstarter

Jumpstarter separates hardware access into four useful concepts:

- Exporter: a process running on a host connected to one or more devices. It exports the device interfaces to Jumpstarter clients.
- Driver: the implementation that talks to a device or virtual target, such as serial, power, SD card, network, CAN, U-Boot, QEMU, Renode, or a vendor-specific interface.
- Client: the developer or CI-side Python library/CLI that acquires a target and calls driver APIs.
- Lease: the allocation and isolation boundary that gives a client temporary access to an exporter and its drivers.

In distributed mode, the Jumpstarter service contains a controller and router. The controller authenticates clients and exporters, tracks resources and leases, applies selectors and access policy, and exposes the Kubernetes-native API. The router carries client-to-exporter traffic when the client and hardware host are not directly connected. The service is configured through a Jumpstarter custom resource and CRDs for clients, exporters, exporter access policies, exporter sets, leases, virtual target classes, and the service itself.

The driver model is intentionally layered:

```text
Test code -> DriverClient -> gRPC -> Driver on exporter -> physical or virtual interface
```

Unary RPCs handle commands such as power on/off. Server streaming handles continuous readings or logs. Bidirectional streams handle serial, video, SSH, or other tunnel-like interfaces. Adapters can transform a driver connection into a more convenient interface such as a forwarded port, terminal, or web connection.

Jumpstarter supports local mode for direct hardware access and distributed mode for shared labs and CI. Distributed mode uses client and exporter authentication, authorization, leases, and driver-package allowlists. Each session gets its own driver instances, which is important for test isolation.

### 2.4 Integration plane

The builder operator and Jumpstarter are joined by target mappings in `OperatorConfig`. A build target maps to:

- a Jumpstarter exporter label selector, for example `board-type=...`;
- a flash command template containing `{image_uri}`;
- the Jumpstarter namespace and CLI image used by the pipeline.

This makes a build-to-board flow declarative: the pipeline creates or obtains an image, selects a compatible board through labels, invokes the configured flash operation, and then runs tests through Jumpstarter drivers.

## 3. Installation path

### 3.1 Local prerequisites

For a developer workstation, install and authenticate:

- `oc` and optionally `kubectl`;
- Podman or Docker;
- Git;
- Python 3.11 or later for Jumpstarter exporter/client work;
- `tkn` if you will inspect Tekton directly;
- `caib` for builder workflows;
- an IDE such as VS Code if using the developer workspace flow.

For a production-like installation, also prepare an OpenShift cluster, wildcard application DNS, TLS/cert-manager strategy, registry access, identity provider configuration, storage, and the hardware hosts that will run exporters.

### 3.2 Install Jumpstarter

The supported operator paths are OperatorHub, OLM subscription, or a locally generated bundle. OperatorHub is the easiest OpenShift path. For source-based development:

```bash
git clone https://github.com/jumpstarter-dev/jumpstarter.git
cd jumpstarter/controller/deploy/operator
make build-installer
oc apply -f dist/install.yaml
```

Create a service namespace and a Jumpstarter custom resource. A minimal shape is:

```yaml
apiVersion: operator.jumpstarter.dev/v1alpha1
kind: Jumpstarter
metadata:
  name: jumpstarter
  namespace: jumpstarter-lab
spec:
  baseDomain: apps.example.com
  controller:
    grpc:
      endpoints:
        - address: grpc.apps.example.com:443
          route:
            enabled: true
  routers:
    grpc:
      endpoints:
        - address: router.apps.example.com:443
          route:
            enabled: true
```

The real values must match the cluster's wildcard Route domain and certificate setup. Verify:

```bash
oc get pods -n jumpstarter-lab
oc get jumpstarter -n jumpstarter-lab
oc get routes -n jumpstarter-lab
```

For high availability, the internal installation guide recommends at least three router replicas. Configure cert-manager or provide TLS secrets explicitly. Configure the authentication mechanism before onboarding exporters and clients.

Install the client packages from the public package index when using a released version:

```bash
pip install --extra-index-url https://pkg.jumpstarter.dev/ jumpstarter-cli
```

### 3.3 Configure an exporter

An exporter runs on a host physically connected to a board or device. It can run directly, in a privileged container, or as a systemd service. The configuration identifies the Jumpstarter endpoint, token, and drivers. A simplified example contains power, serial, and storage interfaces:

```yaml
apiVersion: jumpstarter.dev/v1alpha1
kind: ExporterConfig
metadata:
  namespace: default
  name: demo
endpoint: grpc.jumpstarter.example.com:443
token: <exporter-token>
export:
  power:
    type: jumpstarter_driver_yepkit.driver.Ykush
    config:
      serial: YK25838
      port: "1"
  serial:
    type: jumpstarter_driver_pyserial.driver.PySerial
    config:
      url: /dev/ttyUSB0
      baudrate: 115200
```

Use labels to describe the board type, enabled state, architecture, and any customer or lab grouping. The builder target mapping selects these labels later.

### 3.4 Install the automotive builder operator

The recommended OpenShift path is OperatorHub:

1. Open Operators > OperatorHub.
2. Search for CentOS Automotive Suite.
3. Install the operator.
4. Apply the `OperatorConfig` sample, then edit it for the cluster and board lab.

For local development or custom images:

```bash
git clone https://github.com/centos-automotive-suite/automotive-dev-operator.git
cd automotive-dev-operator
./hack/deploy-catalog.sh -y --keep-config
oc apply -f config/samples/automotive_v1_operatorconfig.yaml
```

For a direct development deployment:

```bash
make docker-build docker-push IMG=<registry>/automotive-dev-operator:<tag>
make install
make deploy IMG=<registry>/automotive-dev-operator:<tag>
oc apply -f config/samples/automotive_v1_operatorconfig.yaml
```

The repository currently says the default build platform is `arm64`; set `BUILD_PLATFORM` explicitly when building for another cluster architecture.

Verify:

```bash
oc get pods -n automotive-dev-operator-system
oc get deployments -n automotive-dev-operator-system
oc api-resources | grep -i automotive
```

Install CAIB from the repository's versioned release mechanism or its installer script, then set the Build API endpoint:

```bash
export CAIB_SERVER=https://build-api-automotive-dev-operator.apps.<cluster-domain>
```

The CLI can use the current `oc login` session or an explicit `CAIB_TOKEN`.

## 4. First useful workflow

A new engineer should learn the system in this order:

1. Build a small known-good image with CAIB.
2. Inspect the Tekton PipelineRun, Tasks, PVCs, logs, and final artifact URI.
3. List Jumpstarter exporters and acquire a lease for a non-production board.
4. Flash the image using the target mapping or a direct Jumpstarter command.
5. Open serial, power, network, or shell access through a driver.
6. Run one smoke test and save the test output and board identity.
7. Repeat the same flow from CI so the difference between interactive and automated access is clear.

The most important troubleshooting boundary is: first decide whether the failure is in image creation, artifact publication, exporter/lease acquisition, flashing, device boot, or test-result reporting. These layers produce different symptoms and are owned by different repositories.

## 5. Repositories and what to read

### Public upstream repositories

- [jumpstarter-dev/jumpstarter](https://github.com/jumpstarter-dev/jumpstarter): monorepo for the Python client, CLI, drivers, controller/operator, protobuf protocol, and E2E infrastructure. Start with `python/`, `controller/`, `protocol/`, and `e2e/`.
- [centos-automotive-suite/automotive-dev-operator](https://github.com/centos-automotive-suite/automotive-dev-operator): operator, APIs, Tekton definitions, CAIB CLI, samples, unit tests, E2E tests, and deployment/catalog tooling. Start with `README.md`, `api/v1alpha1`, `cmd/caib`, `.tekton`, `config`, `internal`, and `test`.
- [automotive-image-builder](https://gitlab.com/CentOS/automotive/src/automotive-image-builder): AIB implementation and upstream RPM/Packit flow.
- [automotive tests/all](https://gitlab.cee.redhat.com/automotive/tests/all): internal bootc and automotive test plans, including tests that create images and use Jumpstarter against physical boards.

### Internal RHAS and lab repositories

The onboarding document identifies these as the main internal paths. Access and branch names may require Red Hat VPN and group membership:

- `gitlab.cee.redhat.com/automotive/jumpstarter`: Red Hat internal Jumpstarter work.
- `gitlab.cee.redhat.com/automotive/jumpstarter/toolchain-pipelines`: CI/toolchain integration effort.
- `gitlab.cee.redhat.com/automotive/jumpstarter/rhas-ci`: downstream RHAS CI infrastructure for ephemeral OpenShift and integration tests.
- `gitlab.cee.redhat.com/automotive/ai/agents/hardware-enablement/board-bringup`: board bring-up automation using CAIB and Jumpstarter.
- `github.com/centos-automotive-suite`: public automotive suite organization and related projects.
- `github.com/jumpstarter-dev`: public Jumpstarter organization.

## 6. Infrastructure map

The internal onboarding document describes two useful cluster contexts:

- public automotive development cluster: `console-openshift-console.apps.automotive1.ocp.automotive.sig.centos.org`;
- internal dev cluster: `console-openshift-console.apps.rosa.auto-devcluster.bzdx.p3.openshiftapps.com`.

The internal dev cluster is described as ROSA on AWS, IT-managed, associated with cost center 669, connected to Red Hat on-premise data centers, spread across three availability zones, and using a hosted control plane. The documented machine pool was two `m6g.xlarge` arm64, non-virtualization nodes in `us-east-1`. Treat these values as onboarding context, not immutable infrastructure facts, and verify them against the current cluster configuration before relying on them.

The downstream CI design is separate from the shared development cluster: an ephemeral arm64 IPI SNO OpenShift cluster on ATC AWS infrastructure, created for a pipeline run and destroyed afterward. The intended flow is install OpenShift, install the builder and Jumpstarter operators, run black-box integration tests, and destroy the cluster. DNS, IAM, pull secrets, temporary credentials, and wildcard application routes are critical dependencies.

## 7. Existing product capabilities

The current product and roadmap materials point to these capability groups:

- reproducible automotive OS image builds, including bootc, OCI, RPM, and ISO workflows;
- cross-compilation and developer workspaces;
- image artifact serving, OCI publication, and catalogs;
- declarative flashing and board provisioning;
- shared physical-board access with leases and access policy;
- virtual targets such as QEMU and Android virtual targets;
- serial, power, storage, network, CAN, diagnostics, U-Boot, fastboot, video, and tunnel interfaces through drivers;
- CI/CD integration with GitHub, GitLab, Tekton, Shipwright, and existing OpenShift workflows;
- multi-architecture scheduling and hardware enablement;
- GitOps, SSO/Keycloak, certificates, telemetry, monitoring, and alerting;
- evidence-oriented testing and CTC integration;
- agentic and human-facing platform workflows, including platform queries and automation.

Some of these are mature upstream capabilities, while others are RHAS productization or roadmap areas. Do not assume that a feature listed in a roadmap has a release-qualified implementation.

## 8. Test architecture and current testing picture

The internal testing architecture has three layers:

1. Jumpstarter upstream E2E tests, generally run on kind for the Jumpstarter service.
2. Builder/operator upstream E2E tests, also commonly run on kind, although kind is less representative for an OpenShift-oriented builder.
3. RHAS black-box integration tests on OpenShift, covering installation, image build, flashing, workspaces, and real-board testing.

The desired downstream pipeline installs both operators on an OpenShift cluster and then tests the integrated user journey. It should run the upstream suites on OpenShift as well as RHAS-specific tests, because a test passing on kind does not prove compatibility with Routes, OpenShift Pipelines, RBAC, registries, storage, or cluster lifecycle behavior.

### Test types to expect

- Unit and API tests for Go controllers, APIs, CAIB, and Python components.
- Operator reconciliation tests and CRD validation tests.
- Tekton task and pipeline tests.
- Jumpstarter client/driver tests.
- Upstream E2E tests on kind.
- OpenShift installation and upgrade tests.
- Build-to-artifact contract tests.
- Artifact-to-flash contract tests.
- Physical hardware-in-the-loop tests across Qualcomm, NXP, and Renesas families.
- Virtual-target tests using QEMU, Android virtual targets, or emulators.
- Reliability tests for exporters, leases, board recovery, firmware updates, and certificate renewal.
- Performance tests for build time, flashing time, and seconds-per-iteration.
- Security and compliance tests for authentication, authorization, supply-chain evidence, and release gating.
- Result-integrity tests that verify failed, skipped, errored, and sub-test outcomes roll up correctly.

The existing RHAS testing notes identify upstream per-PR testing as operational, while downstream integrated CI and formal QE readiness have been the larger gaps. Hardware-in-the-loop infrastructure is already used for RHIVOS CTC, but RHAS-specific ownership, regression suites, and formal release gates must be checked against the latest team status before treating them as complete.

## 9. Suggested learning plan

### Day 1: vocabulary and one local flow

Read the Jumpstarter introduction pages for drivers, exporters, clients, and service. Install the CLI, understand local versus distributed mode, and draw the exporter-client-controller-router path.

### Days 2-3: cluster installation

Deploy Jumpstarter to a disposable OpenShift namespace. Inspect its CRDs, pods, Routes, TLS, authentication, and logs. Deploy the automotive builder operator and inspect the generated Tekton resources.

### Days 4-5: build and flash

Run one CAIB build, follow the PipelineRun to its artifact, configure one exporter, acquire a lease, flash a development board, and access serial or power control.

### Week 2: code and tests

Read the Jumpstarter controller and protocol code, then the builder operator API and Tekton definitions. Run `make test`, `make lint`, and the relevant E2E targets in each repository. Trace one test from the test code through the client, gRPC protocol, exporter driver, and board.

### Week 3: product integration

Read the internal RHAS CI design, understand ephemeral IPI SNO creation and teardown, review the current test coverage map, and reproduce one CI failure or recovery scenario. Then select a feature area such as leases, image builds, board bring-up, virtual targets, or test evidence for deeper ownership.

## 10. Open questions to verify with the team

- Which RHAS release and OpenShift version are currently the supported qualification target?
- Which CAIB and Jumpstarter versions are pinned together for the release?
- Is the production installation OperatorHub-based, a Red Hat catalog, or an internal bundle?
- What is the supported authentication path: internal tokens, Kubernetes service accounts, Keycloak/OIDC, or a combination?
- Which board types are release-qualified versus engineering-only?
- What is the authoritative artifact contract between the builder and Jumpstarter?
- Which tests are release gates, and where are their results stored?
- Is downstream CI now operational, and what is its current DNS/IAM design?
- Which internal repository is authoritative when public and internal Jumpstarter implementations differ?
- What is the upgrade and rollback policy for operators, exporters, driver packages, and board firmware?

## Source index

- [Jumpstarter documentation](https://jumpstarter.dev/)
- [Jumpstarter drivers](https://jumpstarter.dev/main/introduction/drivers.html)
- [Jumpstarter exporters](https://jumpstarter.dev/main/introduction/exporters.html)
- [Jumpstarter clients](https://jumpstarter.dev/main/introduction/clients.html)
- [Jumpstarter service](https://jumpstarter.dev/main/introduction/service.html)
- [Jumpstarter installation](https://jumpstarter.dev/main/getting-started/installation/index.html)
- [Jumpstarter source repository](https://github.com/jumpstarter-dev/jumpstarter)
- [Automotive Dev Operator source repository](https://github.com/centos-automotive-suite/automotive-dev-operator)
- [Internal RHAS onboarding document](https://docs.google.com/document/d/1bBB44X4369l1-8Bb3OkEwBkWZKWZvKuIM9mTmp3UzN8/edit?tab=t.0)
- [Internal RHAS installation guide](https://docs.google.com/document/d/1DVYhOqfo0KZ-Yc4JTsH2oXnPSC5uM5AANZgM6XvfdRk/edit?tab=t.0#heading=h.9brafox4dsiw)

