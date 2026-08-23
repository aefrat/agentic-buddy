---
last_accessed: 2026-08-23
access_count: 3
created: 2026-06-29
---

# RHAS Features Requiring Testing

Based on the PitCrew Full Status Report (Jun 1, 2026), RHAS Strategic Guide,
and 2026 Roadmap. Organized by testing domain.

## 1. Core Platform Components

### Automotive Image Builder (AIB) / Builder Operator
- OCI image builds, bootc images, RPMs, ISOs
- Safe Rust / C / C++ binary compilation
- Satellite OS update delivery
- Konflux-based productization pipeline (PITCREW-335, PITCREW-119)
- SSO integration (Q3 target)
- Telemetry integration (in progress)

### Jumpstarter - Hardware-in-the-Loop Testing
- Board management and lease policies (QC 8650/8775/8979/8255, NXP S32N79/iMX8, Renesas R-Car X5H)
- DUT networking and firmware updates (fastboot, A/B boot)
- Exporter connectivity (e.g., Nissan cluster)
- Cert renewal and Keycloak staging endpoints
- pytest integration with bootc tests
- Documentation accuracy

### Konflux / CI-CD Pipelines
- Pipeline execution on OCP (Tekton)
- Artifact signing and supply chain provenance
- RH-SDLC compliance gates (PITCREW-334, target RHAS-0726)
- x86 and arm64 cross-architecture scheduling

### GitOps / Git Forge Integration
- GitLab CI/IDE integration
- GitHub CI/IDE integration
- Source forge connectivity without rip-and-replace

### Keycloak / SSO
- Authentication flows
- Certificate management (annual renewal)
- Multi-tenant access control

## 2. Feature Epics by Release Target

**Note:** RHAS releases use RHAS-MMYY format (MM=month, YY=year). See `agent_brain/projects/rhas-qe-agent/reference/release-naming-convention.md`.

### RHAS-0626 (June 2026) - Past Due
| Epic | Feature | Testing Focus |
|------|---------|---------------|
| PITCREW-335 | Konflux Onboarding | Pipeline creation, artifact builds, SDLC gates |
| PITCREW-298 | Android Virtual Target Deployment | Virtual target provisioning, Android image deployment |

### RHAS-0726 (July 2026)
| Epic | Feature | Testing Focus |
|------|---------|---------------|
| PITCREW-334 | RH-SDLC Compliance | Compliance validation, audit trail, evidence collection |
| PITCREW-331 | CTC (Continuous Testing Cycle) | Test infrastructure itself, gating criteria, automated regression |
| PITCREW-330 | Lab Infrastructure | Lab provisioning, C2 recovery, board management at scale |
| PITCREW-294 | Autonomous Platform Reactions | Self-healing triggers, reaction correctness, false-positive rate |

### RHAS-0826 (August 2026)
| Epic | Feature | Testing Focus |
|------|---------|---------------|
| PITCREW-299 | Virtual Target Orchestration | QEMU targets, multi-target scheduling, resource management |
| PITCREW-295 | Seconds-per-Iteration | Build/deploy/test cycle time, performance benchmarks |

### RHAS-0926 (September 2026) - Tech Preview
| Epic | Feature | Testing Focus |
|------|---------|---------------|
| PITCREW-329 | External Dependency Resilience | Failure injection, dependency isolation, recovery paths |
| PITCREW-336 | Distribution | Product distribution channels, content delivery validation |

### RHAS-1026 (October 2026)
| Epic | Feature | Testing Focus |
|------|---------|---------------|
| PITCREW-337 | QE Readiness | Test plan completeness, coverage metrics, escape rate |
| PITCREW-292 | Unified Developer Session | End-to-end developer workflow, UX validation |
| PITCREW-338 | Product Documentation | Doc accuracy, procedure validation, tutorial completeness |

### RHAS-1126 (November 2026)
| Epic | Feature | Testing Focus |
|------|---------|---------------|
| PITCREW-300 | Virtual Interface Simulation | Simulated hardware interfaces, fidelity validation |
| PITCREW-332 | ATC | ATC integration testing |

### RHAS-1226 (December 2026) - GA
| Epic | Feature | Testing Focus |
|------|---------|---------------|
| PITCREW-290 | Agentic Platform | AI agent reliability, prompt/response validation |
| PITCREW-293 | Ask the Platform | Query accuracy, response relevance, hallucination rate |

### Unversioned
| Epic | Feature | Testing Focus |
|------|---------|---------------|
| PITCREW-396 | PitCrew AI | AI feature validation |
| PITCREW-398 | Platform Web Console | UI testing, accessibility, browser compatibility |
| PITCREW-343 | Ship with Evidence | Evidence generation, audit readiness |

## 3. Testing Domains Summary

1. **Kubernetes/OpenShift** - Operators, pods, RBAC, multi-arch scheduling, ROSA
2. **Hardware-in-the-loop** - Physical boards (6+ SoC families), firmware, fastboot, DUT networking
3. **CI/CD pipelines** - Konflux, Tekton, artifact signing, cross-arch builds
4. **Image builds** - bootc, OCI, RPMs, ISOs, Safe Rust/C/C++ binaries
5. **Security** - Supply chain, cert management, ISO 21434, ProdSec, CVE process
6. **Performance** - Boot time, build time, iteration speed, scalability
7. **Integration** - Multi-component (Builder+Jumpstarter+GitOps+Keycloak), end-to-end flows
8. **Virtual targets** - QEMU, Android virtual targets, interface simulation
9. **Customer environments** - Ford, Nissan, HATCI, Applied (varied HW + configs)
10. **Observability** - OpenTelemetry, monitoring, alerting, metrics
11. **Distribution** - Content delivery, Satellite updates, CDN
12. **Compliance** - RH-SDLC, FuSa/ASIL, evidence collection
