---
last_accessed: 2026-07-19
access_count: 2
created: 2026-06-29
---

# Team & Program Priorities

Reference file for team-level and program-level priorities. Used by the talent-development skill (to map growth areas to real team needs) and the manager report (to check work alignment). Update quarterly or when priorities shift.

**Sources:**
- [CY26Q3 Priorities](https://docs.google.com/document/d/1uX_NBIRiDA46d_xzxCgWYkE7AaMUKoW9L1rDh-tp7kg) - Q3 team priorities from Kanitha Chim (ATC) and Paul Wallrabe (PitCrew)
- [RHIVOS April 2026 All-Hands, slides 17-24](https://docs.google.com/presentation/d/18b4bZ75C1c_K8KUELQRtiWibm9-Wmi1zB5Ct0HiHe0Y) - program priorities and planning preview

---

## Program Priorities (RHIVOS, April 2026 All-Hands)

**Core directive:** Focus on activities that secure 3 or more wins with automotive customers.

### Customer Engagements (CATS)

- **Nissan:** Boot time improvements (<5s to network), S32N platform, finish kernel enablement, platform integration
- **42dot:** Waiting on confirmation. May change hardware from QC 8650 to Renesas (R-Car S4 or V4H). ADAS on 8650 for now
- **Traton:** PoCs and multiple production projects. S32G - kernel enablement, platform integration
- **NVidia:** Support engagement
- **Applied Intuition:** PoC for Honda on S32G (now Renesas R-Car S4)
- **Tier IV:** Demo on QC 8775 - CES 2027 demo potential
- **Harman:** Build PoC showing RHIVOS integration with their OTA stack
- **Porsche:** QC 8775 - support upcoming questions, define next goals
- **Qorix:** Define next goals
- **JLR:** Re-engage end of Q2
- **BMW:** Define next goals
- **Ford:** RHAS alignment

### Platform & Hardware Roadmap

- **Q2:** QC 8775 kernel, Gen 4.5 platform, QC 8650 kernel, QC 8255 kernel, S32G kernel, S32N kernel
- **Q3:** S32G platform, FuSa, R-Car S4/V4H kernel + platform, S32N platform, Gen 5 kernel, imx8
- **Q4:** QNX Guest, S32G (continued)

### FuSa (Functional Safety)

- September submission target
- Need to allow for P1/P2 from exida
- Capacity for customer-driven new scope (likely 42dot or Traton)
- Internal assessment pass, Validas for glibc, C++ through Validas
- Community activities: ELISA, ISO standard v3, AI safety standard

### Post-2.0 Planning

- **2.0.z:** New hardware support lands here first. December target
- **2.1:** Hardware also comprehended here
- **Feature on Demand:** SELinux Policy generator (internally identified)
- **Toolchain improvements:** CAIB in RHAS (within 6 months), Konflux (within 12 months)
- **PDR:** Hardware Platform Roadmap, Partner infrastructure (Build/Test), Platform Integration Team

### Agentic SDLC (AAA Team)

- Agentic SDLC transformation - move up "levels of agentic" while balancing RHIVOS demands
- Agent workflows: CTC failure analysis automation, full CTC task automation, kernel debug analysis
- FuSa collateral: AIIL requirements from code, testing coverage, triage/change impact, validator creation
- Partner integration: Qualcomm Yocto-to-RHIVOS, expand to alternate platforms (imx8, imx9, Orin, QC RB5)
- Disseminate findings to RHIVOS teams (target Q3)
- Future: AgenticOS new market development, PSIRT

---

## ATC Priorities (Q3 2026)

Source: Kanitha Chim, June 2 ATC meeting.

**Top priority: RHIVOS 2.0.z (December release)**

1. **Prepare CDN repo and Errata config for 2.0.z** - distribution infrastructure for the z-stream release
2. **Layered Product setup** - LP configuration for 2.0.z
3. **Pulp integration in pipeline** - integrate Pulp into the release pipeline
4. **CAIB integration** - onboard CAIB (Container and Application Image Builder) into ATC toolchain
5. **Konflux integration** - begin Konflux adoption (12-month program-level target)
6. **Infra and monitoring** - infrastructure improvements and monitoring maturity
7. **Test Console** - address security issues, performance issues, and LLM integration

---

## PitCrew/RHAS Priorities (Q3 2026)

Source: Paul Wallrabe.

1. **Q2 cleanup - C2 recovery goals** - close out remaining Q2 commitments
2. **Hatchi** - Virtual Env, Android, virtual interfaces as Bluetooth
3. **Productization** - onboarding to Konflux, creating internal builds, Agentic Platform (including telemetry)
4. **Internal requirements** - address internal feature requests
5. **Driving internal adoption of the builder parts** - increase RHAS/Builder adoption within Red Hat

---

## How to use this file

**In talent-development:** When generating growth opportunities and recommended next steps, match framework gaps to priorities above. Example: if a member needs "cross-component design leadership" (Level 4 Scope), recommend leading the CAIB integration design rather than a generic "lead a cross-component initiative."

**In manager report (weekly):** Scan closed tickets and in-progress work against priorities. Flag work that advances a stated priority. Note priorities with no visible activity.
