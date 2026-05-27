# HC:// Distributed Trust Propagation Architecture Model

## Scope and Intent

This document defines an advisory distributed trust propagation architecture model for HC:// operational runtime in HC-TRUST-LAYER.

This is documentation-only guidance and does not change schemas, validators, workflow behavior, federation logic, signing logic, policy files, or canonical record boundaries.

Human-supervised validation remains required for non-trivial trust-kernel-impacting decisions.

## Propagation Purpose

Distributed trust propagation coordinates how trust-state, warning-state, escalation, continuity risk, and recovery signals move across runtime components while preserving provenance, audit trail continuity, and review-visible routing boundaries.

Propagation behavior should remain deterministic, challengeable, and bounded by public-safe disclosure constraints.

## Propagation State Set

The runtime propagation model uses these architecture states:

- **TRUST_PROPAGATED**
- **WARNING_PROPAGATED**
- **ESCALATION_PROPAGATED**
- **FEDERATION_DIVERGENCE_VISIBLE**
- **RECOVERY_PROPAGATION_ACTIVE**
- **PROPAGATION_RESTRICTED**

State transitions must include timestamps, reason codes, actor/system origin, and linkage to upstream evidence references.

## 1) Trust-State Propagation Lifecycle

Trust-state propagation lifecycle defines the baseline path for low-ambiguity advisory movement:

1. Trust-state output is produced from trust-state scoring and current validator health context.
2. Runtime communication lanes attach provenance and correlation metadata.
3. Propagation enters **TRUST_PROPAGATED** with traceable source references.
4. Downstream surfaces consume propagated trust-state under policy-aware visibility controls.
5. Public-safe summaries are emitted only after required lifecycle checks are complete.

Lifecycle progression must not bypass escalation checks or suppress uncertainty markers.

## 2) Warning-State Propagation

Warning-state propagation covers continuity risk, reduced confidence, partial evidence, and degraded runtime advisories:

1. Warning trigger is detected by trust scoring, validator health, or runtime communication integrity checks.
2. Warning enters **WARNING_PROPAGATED** with warning class and impact scope.
3. Warning visibility is preserved across orchestration lanes and operator surfaces.
4. Warning remains active until an auditable supervised resolution is recorded.
5. Public-safe warning summaries remain visible where response exposure could otherwise mislead.

Warning propagation must preserve challengeability and avoid normalization of unresolved risk.

## 3) Escalation Propagation

Escalation propagation governs high-risk or disputed routing:

1. Escalation condition is raised from disagreement, tamper suspicion, continuity break severity, or policy-triggered review requirement.
2. State transitions to **ESCALATION_PROPAGATED**.
3. Escalation evidence bundle references are attached for reviewer continuity.
4. Runtime routing prioritizes supervised review paths and controlled handling.
5. Escalation closure is permitted only after explicit human-supervised validation checkpoints.

Escalation propagation is advisory and does not imply autonomous governance finality.

## 4) Federation Visibility Propagation

Federation visibility propagation covers cross-boundary divergence signaling without claiming live federation guarantees:

1. Local runtime observes divergence, mismatch class, or unresolved cross-boundary interpretation.
2. State transitions to **FEDERATION_DIVERGENCE_VISIBLE**.
3. Divergence summaries propagate to federation-aware operator surfaces.
4. Local provenance and local decision chronology remain intact during federation exchange.
5. Public-safe response channels expose divergence visibility class when relevant.

Federation propagation must remain inspectable and bounded by repository-defined federation trust exchange boundaries.

## 5) Continuity-Warning Propagation

Continuity-warning propagation defines how lineage uncertainty remains visible:

1. Continuity check detects gap, break, stale linkage, or unresolved sequence anomaly.
2. Warning class is propagated through **WARNING_PROPAGATED** and, when recovery is active, **RECOVERY_PROPAGATION_ACTIVE**.
3. Continuity-warning markers are carried through review, escalation, and recovery routing.
4. Continuity warning is not cleared silently; closure requires auditable resolution evidence.
5. Public-safe continuity indicators remain present until supervised closure.

Continuity propagation should preserve canonical record identity context without modifying canonical artifacts.

## 6) Replay/Tamper Alert Propagation

Replay/tamper alert propagation ensures high-sensitivity integrity signals remain explicit:

1. Replay or tamper suspicion enters warning or escalation detection layers.
2. Alert propagates as **ESCALATION_PROPAGATED** and may concurrently activate **RECOVERY_PROPAGATION_ACTIVE**.
3. Alert propagation includes detection source, confidence class, and affected runtime surface.
4. Routing prioritizes containment, supervised review, and recovery trace preservation.
5. Alert deactivation requires auditable reason codes and reviewer-visible rationale.

No replay/tamper alert may be suppressed without an attributable record.

## 7) Public-Safe Propagation Boundaries

Propagation outputs should separate public-safe summaries from internal-sensitive details.

### Public-safe propagation surface

- trust-state class summary
- warning or escalation visibility class
- federation divergence visibility marker
- continuity-warning category
- recovery activity indicator
- non-sensitive audit trail references

### Internal-only propagation surface

- sensitive internal routing metadata
- protected reviewer notes and identities
- infrastructure topology-sensitive traces
- restricted security or policy evaluator internals

When uncertainty is unresolved, propagation should favor transparent caution indicators over hidden simplification.

## 8) Propagation Rollback and Recovery Behavior

Rollback and recovery behavior defines reversible correction paths for propagation anomalies:

1. Detect propagation error, stale signal, or inconsistent state fan-out.
2. Enter **PROPAGATION_RESTRICTED** to prevent uncontrolled downstream amplification.
3. Activate **RECOVERY_PROPAGATION_ACTIVE** for bounded rollback/replay handling.
4. Reconcile affected propagation paths using checkpointed provenance and audit trail continuity.
5. Resume normal propagation only after supervised validation of corrected state visibility.

Rollback and recovery paths must remain reversible, inspectable, and explicitly attributable.

## Safeguards

Distributed trust propagation follows these safeguards:

- **no hidden trust amplification**
  - trust-state influence cannot be increased through undocumented fan-out or suppressed warning weighting.
- **no silent propagation suppression**
  - warning, escalation, and continuity signals cannot be dropped without auditable reason records.
- **propagation remains auditable**
  - all propagation transitions are logged with state, reason, timestamp, and provenance linkage.
- **federation propagation remains inspectable**
  - federation-visible divergence pathways preserve local and cross-boundary review visibility.
- **recovery propagation remains traceable**
  - rollback/recovery events must preserve before/after state lineage and supervised closure checkpoints.

## Model Alignment

This distributed trust propagation architecture model aligns with:

- **trust scoring model alignment**
  - propagated trust-state and warning-state classes should reflect trust scoring confidence and uncertainty boundaries.
- **validator health model alignment**
  - propagation routing should incorporate degraded, isolated, or unavailable validator health states.
- **runtime communication model alignment**
  - propagation transport should preserve ordering, attribution, and synchronization guarantees defined for runtime communication.
- **failover/recovery model alignment**
  - propagation restriction and recovery activation should map to failover and recovery orchestration controls.
- **operational response lifecycle alignment**
  - propagated states should remain consistent with intake-to-response lifecycle state exposure rules.

## Verification and Governance Boundary Note

This model is documentation guidance only for HC:// runtime architecture in HC-TRUST-LAYER.

It does not introduce production-readiness claims, truth-guarantee claims, or forensic-certainty claims, and it does not modify trust-kernel implementation surfaces.
