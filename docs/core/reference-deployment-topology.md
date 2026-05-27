# HC:// Reference Deployment Topology Model

## Scope and posture

This document defines a reference deployment topology model for HC:// operational trust infrastructure in HC-TRUST-LAYER.

It provides documentation-only topology guidance for deployment composition, topology visibility, continuity, and recovery routing.

This model is advisory and does not claim production readiness, autonomous authority, or forensic certainty.

Constraints preserved in this scope:

- no schema changes
- no validator changes
- no workflow changes

Human-supervised validation remains required for trust-kernel-impacting interpretation and escalation outcomes.

## 1) Deployment topology purpose

The deployment topology model defines how HC:// runtime roles can be arranged so verification handling, federation coordination, public-safe routing, and audit trail continuity remain inspectable.

The purpose is to:

- provide a minimal, reviewable deployment baseline;
- preserve provenance and audit trail continuity across topology states;
- keep degraded and recovery conditions explicit and auditable;
- preserve public-safe verification boundaries under operational stress;
- support local-first operation where possible.

## 2) Minimal single-node deployment

The minimal single-node deployment co-locates core runtime roles on one host for constrained operations.

Typical role placement:

- validator node
- public verification gateway
- continuity/audit node
- observability node
- escalation coordination node

Single-node expectations:

- verification remains advisory-only;
- local continuity and audit evidence remains accessible;
- degraded behavior is visible through explicit topology state markers;
- unresolved or disputed outcomes route to human-supervised validation.

## 3) Lightweight federation deployment

The lightweight federation deployment extends single-node operation with bounded federation connectivity for cross-domain review routing.

Additional role placement:

- federation relay node
- interoperability gateway node

Lightweight federation expectations:

- federation participation remains visible and attributable;
- cross-domain review paths preserve provenance linkage;
- federation routing does not imply hidden authority transfer;
- unresolved conditions remain auditable and reviewer-visible.

## 4) Regional federation topology

The regional federation topology organizes multiple validator and relay participants within region-scoped trust routing boundaries.

Regional topology expectations:

- regional participants expose explicit topology health and warning visibility;
- partition and divergence conditions remain visible across regional routes;
- continuity/audit nodes preserve cross-region event chronology;
- escalation coordination remains human-supervised for trust-kernel-impacting disagreements.

## 5) Public verification gateway topology

The public verification gateway topology defines public-facing deployment pathways for QR and link-based HC:// verification access.

Gateway topology expectations:

- public verification gateway surfaces remain advisory-only;
- public-safe response boundaries are preserved during normal and degraded states;
- gateway routing remains traceable and challengeable;
- public warnings remain visible when topology confidence is reduced.

## 6) Observability/telemetry topology

The observability/telemetry topology defines deployment visibility pathways for runtime health, anomaly signals, and coordination status.

Observability topology expectations:

- observability node remains inspectable and audit-linked;
- topology warning transitions are timestamped and attributable;
- telemetry does not create hidden policy override pathways;
- public-safe and operator-only visibility boundaries remain explicit.

## 7) Continuity/audit topology

The continuity/audit topology defines how continuity evidence and audit trail references remain available across distributed deployment surfaces.

Continuity topology expectations:

- continuity/audit node preserves event chronology and lineage references;
- trust-path continuity warnings remain visible rather than suppressed;
- federation and recovery events remain provenance-linked;
- canonical continuity review remains challengeable and reviewer-accessible.

## 8) Recovery/failover topology

The recovery/failover topology defines bounded deployment behavior when runtime, federation, or continuity dependencies degrade.

Recovery topology expectations:

- recovery coordination node activates explicit recovery topology state markers;
- degraded routing remains advisory-only and auditable;
- checkpoint restoration and handback progression remain review-visible;
- public warning boundaries remain active until recovery validation confirms stability.

## 9) Interoperability gateway topology

The interoperability gateway topology defines deployment surfaces that exchange verification context across external trust domains while preserving HC:// boundaries.

Interoperability topology expectations:

- interoperability gateway node preserves attribution and provenance references;
- external exchange remains bounded by advisory response semantics;
- interoperability routes remain auditable and inspectable;
- unresolved cross-domain outcomes remain escalation-eligible.

## Deployment roles

### validator node

- Executes bounded verification checks.
- Emits advisory result classes and warning markers.

### federation relay node

- Coordinates federation review routing.
- Preserves attributable cross-domain exchange records.

### public verification gateway

- Exposes public-safe verification responses.
- Preserves concise warning and provenance visibility.

### continuity/audit node

- Preserves continuity evidence and audit trail chronology.
- Surfaces continuity warnings and lineage mismatch indicators.

### observability node

- Publishes topology health, degradation, and recovery signals.
- Preserves inspectable telemetry references.

### recovery coordination node

- Coordinates failover routing and restoration checkpoints.
- Preserves auditable handback transitions.

### escalation coordination node

- Routes unresolved and disputed outcomes to human-supervised validation pathways.
- Preserves reviewer accountability and evidence continuity.

### interoperability gateway node

- Exchanges verification context with external trust domains.
- Preserves auditable boundary mapping and routing traceability.

## Topology states

Deployment topology should expose the following explicit states:

- `TOPOLOGY_OPERATIONAL`
- `TOPOLOGY_DEGRADED`
- `RECOVERY_TOPOLOGY_ACTIVE`
- `FEDERATION_PARTITION_ACTIVE`
- `PUBLIC_WARNING_ACTIVE`

State interpretation boundaries:

- topology states are visibility markers, not autonomous trust finality;
- state transitions should remain timestamped, attributable, and audit-linked;
- trust-kernel-impacting interpretation remains subject to human-supervised validation.

## Deployment safeguards

This topology model preserves the following safeguards:

- no hidden central authority;
- federation visibility preserved;
- degraded topology remains visible;
- recovery coordination remains auditable;
- public-safe routing boundaries preserved;
- observability remains inspectable.

## Deployment examples

### Single-server deployment

A single server hosts validator, gateway, continuity, observability, and escalation roles for local-first verification flow with explicit advisory boundaries.

### Small federation deployment

A small federation of organizations uses validator nodes plus federation relay nodes for cross-domain review routing while preserving visible, auditable exchange paths.

### Media verification deployment

Media surfaces route viewers to a public verification gateway topology that preserves advisory-state visibility, caution messaging, and provenance references during high-volume intake.

### Institution/public gateway deployment

An institution deployment combines public verification gateway and interoperability gateway nodes so institution/public verification remains consistent while external interoperability remains bounded and auditable.

### Degraded regional topology

A regional federation enters `TOPOLOGY_DEGRADED` during partial outage, activates `PUBLIC_WARNING_ACTIVE`, and preserves continuity/audit visibility until recovery checkpoints confirm stable routing.

### Emergency recovery topology

A severe partition activates `FEDERATION_PARTITION_ACTIVE` and `RECOVERY_TOPOLOGY_ACTIVE`, routes unresolved outcomes through escalation coordination, and preserves auditable handback progression before returning to `TOPOLOGY_OPERATIONAL`.

## Alignment with HC-TRUST-LAYER runtime models

This reference deployment topology model aligns with:

- `docs/core/minimal-reference-runtime-architecture.md`
- `docs/core/runtime-api-contract-architecture.md`
- `docs/core/federation-mesh-coordination.md`
- `docs/core/runtime-failover-and-recovery.md`
- `docs/core/global-verification-gateway-federation.md`
- `docs/core/runtime-observability-and-telemetry-model.md`
