# README Capability Alignment: Vision to Operational Core Runtime

## Scope and boundary

This document maps HC:// README vision statements to the currently documented HC-TRUST-LAYER operational core/runtime architecture.

This is a documentation-only alignment artifact for review routing, capability clarity, and human-supervised validation planning. It does not change validators, schemas, federation logic, policy behavior, or canonical record boundaries.

## Capability status model

Capability status values used in this map:

- **implemented**: runtime behavior is documented as active in core architecture flows.
- **partial**: core path exists, but coverage, automation depth, or ecosystem breadth is incomplete.
- **scaffolded**: architecture pattern and interfaces are documented, but operational depth is limited.
- **planned**: target capability is defined as a forward integration objective, not yet operational.

## 1) Vision -> Runtime mapping

| README vision capability | Runtime mapping in HC-TRUST-LAYER | Status |
| --- | --- | --- |
| public verification | Public verification runtime flow with controlled exposure and evidence-backed result presentation. | partial |
| QR verification | Public QR verification gateway routing QR payloads into validator runtime and response shaping. | partial |
| trust scoring | Trust evaluation and risk signaling path in trust layer with policy-aware advisory output. | scaffolded |
| witness coordination | Distributed validator coordination and witness-style consensus exchange for verification continuity. | scaffolded |
| federation review | Federation trust exchange and escalation routing for cross-domain or contested verification cases. | partial |
| immutable audit trail | Trust state persistence and audit runtime preserving provenance and continuity artifacts. | partial |
| advisory/risk signaling | Advisory policy outputs, risk-state communication, and non-authority result signaling. | partial |
| verification gateway | Gateway entry layer for public and QR-origin verification requests into runtime orchestration. | partial |
| continuity snapshots | Runtime state and verification continuity snapshot model for audit and replay context. | scaffolded |
| distributed validator ecosystem | Multi-validator coordination model for distributed verification participation under shared protocol boundaries. | scaffolded |
| public transparency layer | Public-safe transparency publication patterns that expose verification outcomes without over-claiming certainty. | partial |

## 2) Capability status classification detail

### Implemented

At this stage, this map does not classify any listed README capability as fully implemented across all operational dimensions.

### Partial

- public verification
- QR verification
- federation review
- immutable audit trail
- advisory/risk signaling
- verification gateway
- public transparency layer

### Scaffolded

- trust scoring
- witness coordination
- continuity snapshots
- distributed validator ecosystem

### Planned

Planned integration targets are listed in section 5 and represent interoperability expansion beyond the currently documented core runtime posture.

## 3) Runtime ownership map

| Capability | Primary runtime owner | Supporting runtime owners |
| --- | --- | --- |
| public verification | public exposure layer | gateway layer, validator layer, audit layer, trust layer |
| QR verification | gateway layer | orchestration layer, validator layer, trust layer, public exposure layer |
| trust scoring | trust layer | validator layer, audit layer |
| witness coordination | orchestration layer | validator layer, federation layer, audit layer |
| federation review | federation layer | orchestration layer, validator layer, audit layer, trust layer |
| immutable audit trail | audit layer | validator layer, trust layer, orchestration layer |
| advisory/risk signaling | trust layer | policy-aware routing in orchestration layer, public exposure layer |
| verification gateway | gateway layer | orchestration layer, validator layer |
| continuity snapshots | audit layer | orchestration layer, validator layer, trust layer |
| distributed validator ecosystem | validator layer | orchestration layer, federation layer, audit layer |
| public transparency layer | public exposure layer | gateway layer, trust layer, audit layer |

## 4) Operational dependency graph

The operational dependency path is layered and evidence-first. Representative runtime chains:

1. **QR verification path**  
   QR gateway -> validator runtime -> trust evaluation -> advisory policy shaping -> public response

2. **Public verification path**  
   Public verification request -> gateway routing -> validator checks -> audit persistence -> trust/advisory output -> public transparency response

3. **Federation escalation path**  
   Local validator outcome -> dispute/risk trigger -> federation review routing -> federation response capture -> audit continuity update -> supervised finalization

4. **Continuity and replay path**  
   Verification execution -> state persistence -> continuity snapshot publication -> later audit/review replay

Cross-cutting dependency rules:

- public exposure depends on prior validator and trust-layer completion states.
- trust-layer signaling depends on validator outputs and audit continuity.
- federation routing depends on local runtime outcomes and escalation policy gates.
- audit continuity depends on deterministic runtime event capture across layers.

## 5) Future integration targets

These are forward interoperability targets aligned to HC:// roadmap direction and human-supervised validation constraints:

- **public institutions**: standards-aligned verification exchange surfaces for institutional review workflows.
- **media verification**: structured verification packaging for newsroom and publisher provenance checks.
- **API integrations**: bounded API exposure for external systems consuming verification outcomes and provenance metadata.
- **external gateways**: controlled intake bridges from partner verification gateways into HC-TRUST-LAYER runtime boundaries.
- **mobile verification clients**: mobile-readable verification UX with constrained local-first verification flows when possible.
- **broadcast/public QR workflows**: large-audience QR verification entry patterns with dispute-aware routing and advisory-safe public output.

Status for these targets: **planned**.

## 6) Architectural principles reinforcement

Operational alignment remains anchored to these principles:

1. **protocol-first**: runtime behavior follows HC:// protocol boundaries before product-layer expansion.
2. **audit-first**: provenance and audit trail continuity are required for trust interpretation.
3. **verification-before-exposure**: public responses are downstream of verification execution, not a substitute for it.
4. **public-safe transparency**: expose verification-relevant outcomes without authority inflation or certainty over-claims.
5. **dispute-aware routing**: uncertain or contested outcomes route to supervised review paths.
6. **federation escalation only when required**: federation is an escalation mechanism, not a default execution path.

## Review and validation note

This map is advisory and should be reviewed alongside:

- `README.md`
- `docs/core/public-verification-runtime-flow.md`
- `docs/core/public-qr-verification-gateway.md`
- `docs/core/validator-orchestration-architecture.md`
- `docs/core/trust-state-persistence-and-audit-runtime.md`
- `docs/core/distributed-validator-consensus-coordination.md`
- `docs/core/federation-trust-exchange.md`

Any trust-kernel-impacting reinterpretation discovered during review should be routed to human-supervised validation before implementation changes.
