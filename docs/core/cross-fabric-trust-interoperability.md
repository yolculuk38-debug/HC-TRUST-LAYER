# HC:// Cross-Fabric Trust Interoperability Model

This document defines the cross-fabric trust interoperability model for HC:// in HC-TRUST-LAYER.

The model describes how HC:// operational trust fabric coordinates with external verification systems, institutional trust layers, media verification services, and future public trust infrastructures while preserving inspectability, provenance continuity, and human-supervised validation.

Scope boundaries:

- Documentation-only interoperability model.
- No schema changes.
- No validator changes.
- No workflow changes.
- No signing, federation, policy, or canonical record semantics are changed by this document.
- No production-readiness, autonomous governance finality, or truth-guarantee claim is made.

## 1. Interoperability purpose

Cross-fabric interoperability provides a bounded coordination model so HC:// can exchange advisory trust signals across diverse trust fabrics without hidden trust inheritance.

The purpose is to:

- preserve advisory trust interpretation boundaries across participating fabrics;
- maintain inspectable provenance and audit trail continuity during cross-fabric exchange;
- keep consequential trust-kernel interpretation under human-supervised validation;
- ensure degraded or disputed interoperability conditions remain visible.

## 2. External trust fabric coordination

External trust fabric coordination defines how HC:// interoperates with non-HC:// verification infrastructures through explicit, traceable exchange surfaces.

Coordination expectations:

- interoperability exchange uses explicit trust-state mapping and warning mapping;
- cross-fabric route decisions remain inspectable and auditable;
- unresolved external ambiguity does not become implicit local trust certainty;
- degraded external visibility is surfaced as warning-grade interoperability context.

## 3. Institution interoperability concepts

Institution interoperability concepts enable institutions to exchange verification context with HC:// while preserving clear authority boundaries.

Concept expectations:

- institution trust gateways expose attributable source context and public-facing advisory boundaries;
- institution-facing interoperability maintains continuity references and challenge pathways;
- institutional trust indicators remain challengeable and do not bypass local review routing;
- high-impact institutional disagreement routes to explicit cross-fabric review escalation.

## 4. Media/public verification interoperability

Media/public verification interoperability enables broadcast, publishing, and public information channels to reference HC:// verification context through interoperable trust surfaces.

Interoperability expectations:

- media verification providers can attach interoperability-linked verification context;
- public-facing warning and continuity states remain visible in compact media formats;
- media interoperability cannot imply autonomous final authority;
- dispute visibility and review routing remain linked to inspectable evidence references.

## 5. Public API interoperability concepts

Public API interoperability concepts describe safe exchange boundaries for public-facing interoperability services.

API expectations:

- API responses expose advisory trust-state and interoperability state classes with provenance references;
- API outputs separate public-safe summaries from internal-sensitive details;
- interoperability response semantics remain stable, inspectable, and challengeable;
- warning and degraded conditions remain explicit in API-visible outputs.

## 6. Federation-to-federation coordination

Federation-to-federation coordination defines interoperability behavior when HC:// federation surfaces exchange advisory trust context with external federation-capable ecosystems.

Coordination expectations:

- federation interoperability preserves route attribution and exchange chronology;
- cross-fabric divergence remains explicitly visible;
- federation interoperability does not create hidden delegated trust authority;
- unresolved federation disagreement remains escalated through human-supervised validation pathways.

## 7. Continuity-aware interoperability

Continuity-aware interoperability ensures lineage and provenance continuity mismatches remain visible across fabrics.

Continuity expectations:

- continuity mismatch signals are preserved during trust-state exchange;
- unresolved continuity gaps cannot be presented as settled cross-fabric trust;
- continuity warning states persist until auditable supervised resolution;
- cross-fabric continuity references remain inspectable for reviewers and public audiences.

## 8. Advisory-safe interoperability behavior

Advisory-safe interoperability behavior ensures interoperability remains advisory and bounded even when external systems provide high-confidence trust signals.

Behavior expectations:

- external trust inputs remain advisory and challengeable;
- interoperability transformations remain documented and inspectable;
- consequential decisions remain subject to human-supervised validation;
- interoperability messaging avoids misleading authority or certainty claims.

## 9. Degraded interoperability handling

Degraded interoperability handling defines safe behavior when external trust fabrics become unavailable, unstable, divergent, or partially observable.

Handling expectations:

- degraded external trust conditions remain visible to operators and public-safe surfaces;
- fallback paths preserve warning context and provenance linkage;
- interoperability degradation cannot silently elevate local trust interpretation;
- recovery transitions remain auditable, reversible, and continuity-aware.

## Interoperability participants

Cross-fabric interoperability includes these participants:

- **HC:// federation gateway**
  - primary HC:// exchange boundary for federation-aware interoperability routing.

- **institutional trust gateway**
  - institution-facing interoperability entry for public records and trust-state exchange.

- **external verification relay**
  - relay surface that maps external verification outputs into interoperable advisory context.

- **media verification provider**
  - media/broadcast integration participant that presents interoperability-linked verification visibility.

- **audit interoperability layer**
  - cross-fabric audit trail continuity surface for attributable event chronology and challenge paths.

- **continuity interoperability observer**
  - continuity-focused participant that monitors and exposes lineage mismatch and unresolved continuity risk.

## Interoperability states

The interoperability model uses the following states:

- `INTEROPERABILITY_ACTIVE`
- `INTEROPERABILITY_LIMITED`
- `TRUST_FABRIC_DIVERGENCE`
- `CONTINUITY_WARNING_ACTIVE`
- `EXTERNAL_REVIEW_REQUIRED`
- `PUBLIC_INTEROPERABILITY_WARNING`

State interpretation boundaries:

- interoperability states are advisory visibility and routing indicators;
- interoperability states are not autonomous final trust determinations;
- state transitions must preserve provenance references and audit trail continuity;
- escalated states require human-supervised validation before consequential closure.

## Safeguards

The cross-fabric interoperability model enforces the following safeguards:

- no hidden trust inheritance;
- interoperability remains inspectable;
- external trust signals remain challengeable;
- federation interoperability remains auditable;
- degraded external trust remains visible;
- public-safe warnings remain preserved.

## Operational scenarios

### Public institution verification exchange

A public institution publishes a record through an institutional trust gateway and exchanges interoperability context with an HC:// federation gateway. Interoperability remains advisory, challengeable, and provenance-linked while preserving clear reviewer escalation boundaries.

### Media verification interoperability

A media verification provider attaches cross-fabric trust context to a published artifact. Public-facing views preserve warning visibility, continuity indicators, and advisory interpretation boundaries in compact and mobile-readable presentation.

### Cross-fabric dispute escalation

An external verification relay and HC:// trust interpretation disagree on a material trust indicator. The model enters `EXTERNAL_REVIEW_REQUIRED`, preserves divergence evidence, and routes dispute handling through human-supervised validation.

### Degraded external trust provider

An external verification system reports unstable outputs and intermittent availability. Interoperability shifts to `INTEROPERABILITY_LIMITED` with explicit degraded warnings while preserving challengeability and audit trail continuity.

### Continuity mismatch between fabrics

Lineage references received from an external trust fabric conflict with local continuity expectations. `CONTINUITY_WARNING_ACTIVE` is preserved until supervised review resolves mismatch evidence and records closure rationale.

### Emergency public interoperability warning

A large-scale cross-fabric ambiguity event affects public-facing verification interpretation. `PUBLIC_INTEROPERABILITY_WARNING` is activated so public surfaces retain visible caution signals and avoid overstated trust certainty.

## Alignment with related models

This cross-fabric trust interoperability model aligns with:

- `docs/core/operational-trust-fabric-coordination.md`
- `docs/core/global-verification-gateway-federation.md`
- `docs/core/distributed-trust-propagation.md`
- `docs/core/runtime-policy-enforcement.md`
- `docs/core/runtime-observability-and-telemetry-model.md`
- `docs/core/public-trust-fabric-architecture.md`

## Scope constraints

This document defines an interoperability architecture model only.

- Documentation only
- No schema changes
- No validator changes
- No workflow changes
