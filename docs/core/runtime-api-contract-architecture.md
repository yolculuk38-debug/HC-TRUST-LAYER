# HC:// Runtime API Contract Architecture

## Scope and posture

This document defines an advisory runtime API contract architecture for HC-TRUST-LAYER and HC:// operational trust infrastructure.

It clarifies runtime API contract boundaries across validator orchestration, trust-state propagation, federation exchange, continuity handling, public verification exposure, observability, escalation routing, and recovery coordination.

This is documentation-only architecture guidance. It does not claim production readiness or autonomous authority.

Constraints preserved in this scope:

- no schema changes
- no validator changes
- no workflow changes

Human-supervised validation remains required for trust-kernel-impacting interpretation.

## 1) Runtime API contract purpose

Runtime API contracts define interoperable, auditable, and inspectable exchange boundaries between runtime components so trust decisions remain challengeable and provenance-preserving.

Primary purpose:

- preserve consistent interpretation of runtime states
- prevent hidden escalation pathways
- preserve audit trail continuity across component boundaries
- support public-safe verification exposure without leaking internal-sensitive details
- keep federation participation attributable and reviewable

## 2) Contract categories

Runtime API contracts are grouped into five categories:

1. **public-safe contracts**
   - externally exposable responses with bounded trust-state detail.
2. **federation contracts**
   - inter-participant review and exchange boundaries for cross-fabric coordination.
3. **internal runtime contracts**
   - validator, routing, and state-propagation interfaces used inside runtime boundaries.
4. **audit visibility contracts**
   - event and decision surfaces that preserve provenance and audit trail completeness.
5. **recovery/runtime contracts**
   - continuity restoration, degradation handling, and handback coordination surfaces.

## 3) Standard response states

Runtime contracts should use a stable response-state set:

- `VERIFIED`
- `ADVISORY`
- `DISPUTED`
- `UNRESOLVED`
- `CONTINUITY_WARNING`
- `RECOVERY_ACTIVE`
- `FEDERATION_REVIEW_ACTIVE`
- `PUBLIC_WARNING`

State transitions should remain explicit, timestamped, and attributable to preserve agent context and provenance continuity.

## 4) Contract safeguards

All contract categories should enforce these safeguards:

- no hidden trust escalation
- no silent trust inheritance
- contracts remain inspectable
- public-safe exposure boundaries are preserved
- interoperability remains auditable
- continuity events remain traceable

Additional guardrails:

- trust-state deltas remain advisory until human-supervised validation confirms trust-kernel-impacting outcomes
- disputed or unresolved states must not be silently converted to `VERIFIED`
- public-safe contracts must not expose internal-only diagnostics that can compromise operational boundaries

## 5) Runtime contract domains

### 5.1 Validator API contracts

Validator API contracts standardize request/response handling for verification operations, including:

- input reference identity and scope
- validator capability metadata
- response state and confidence class
- warning and escalation flags
- provenance reference links

Validator contracts should return bounded degradation context when runtime pressure, partial data, or dependency issues affect confidence.

### 5.2 Trust-state response contracts

Trust-state response contracts define how trust outcomes are packaged for internal consumers:

- state (`VERIFIED`, `ADVISORY`, `DISPUTED`, `UNRESOLVED`, and warning/recovery states)
- confidence tier
- policy decision hint (advisory, escalate, federation-route)
- continuity checkpoint status
- audit trail reference set

Trust-state contracts must preserve chronology so downstream components can reconstruct decision pathways.

### 5.3 Federation exchange contracts

Federation exchange contracts define cross-participant request/response patterns for review routing and divergence handling:

- federation review request identity
- participant attribution
- dispute class and review reason
- expected response window
- continuity evidence pointers

Federation contracts should preserve interoperability while avoiding authority inflation or implied unilateral finality.

### 5.4 Continuity event contracts

Continuity event contracts standardize how runtime continuity risks and restorations are emitted:

- continuity event class (`CONTINUITY_WARNING`, `RECOVERY_ACTIVE`)
- affected trust-path scope
- checkpoint and lineage references
- replay/tamper warning linkage
- remediation stage markers

Continuity contracts must keep warning history visible rather than replacing prior risk evidence.

### 5.5 Public verification response contracts

Public verification response contracts define externally consumable, public-safe payload boundaries:

- public-safe state class (`VERIFIED`, `ADVISORY`, `PUBLIC_WARNING`, `UNRESOLVED`)
- concise rationale summary
- timestamp and provenance summary
- escalation/review advisory indicator
- continuity caution notice when applicable

Public responses should remain understandable, mobile-readable, and explicit that outcomes are advisory and subject to human-supervised validation.

The advisory QR verification response also exposes canonical record lookup diagnostics when the runtime bridge is active:

- `canonical_lookup_status`: one of `found`, `missing`, `malformed`, `schema_invalid`, `hash_missing`, `hash_mismatch`, or `verified`.
- `schema_valid`: public-safe boolean indicating whether the advisory runtime bridge accepted the loaded record shape for the requested record id.
- `hash_verified`: public-safe boolean indicating whether the loaded record `content_hash` matched deterministic SHA-256 evaluation.

These fields are diagnostics only. They do not approve trust, do not mutate canonical records, do not change trust-state policy, and do not replace human-supervised validation.

### 5.6 Observability and telemetry contracts

Observability/telemetry contracts standardize runtime signal exchange for health, anomaly, and coordination visibility:

- signal category
- severity class
- affected scope
- correlation identifier
- escalation recommendation
- audit visibility reference

Telemetry contracts should prioritize inspectability and should not provide a hidden channel for policy override.

### 5.7 Escalation and review routing contracts

Escalation/review routing contracts define how cases move into operator, trust-kernel reviewer, or federation review lanes:

- escalation level
- routing reason
- required reviewer role
- response due window
- linked evidence package
- current route state (`FEDERATION_REVIEW_ACTIVE`, `DISPUTED`, `UNRESOLVED`)

Routing contracts should preserve handoff continuity and explicit accountability.

### 5.8 Recovery coordination contracts

Recovery coordination contracts define bounded restoration and handback flow:

- recovery activation marker (`RECOVERY_ACTIVE`)
- degraded capability summary
- mitigation actions in progress
- validation checkpoints required for handback
- post-recovery monitoring window

Recovery contracts must preserve traceability from warning through restoration so audit trail continuity remains complete.

## 6) Operational examples

### Example A: QR verification API response

A QR verification request returns `ADVISORY` when validator consensus is partial:

- includes verification request identifier and timestamp
- includes confidence class and concise caution note
- includes provenance summary and continuity checkpoint reference
- includes escalation advisory when unresolved anomalies exist

### Example B: Federation review request

A cross-fabric provenance conflict triggers federation routing:

- review request state is `FEDERATION_REVIEW_ACTIVE`
- includes participant attribution and divergence summary
- includes response window and evidence reference bundle
- includes public exposure caution while review is pending

### Example C: Continuity warning event

A continuity checkpoint mismatch emits `CONTINUITY_WARNING`:

- event includes affected trust-path scope
- includes checkpoint identifier and lineage linkage context
- includes traceable remediation routing state
- preserves prior warning chronology for audit review

### Example D: Replay-warning propagation event

Replay anomaly signals propagate across runtime surfaces:

- internal runtime event marks `PUBLIC_WARNING` eligibility for public-safe responses
- observability signal links replay-warning correlation identifier
- escalation routing contract references unresolved replay risk window
- trust-state remains `UNRESOLVED` until review completes

### Example E: Public verification response payload

Public response example (public-safe):

```json
{
  "request_id": "qrv_01HCT...",
  "state": "PUBLIC_WARNING",
  "summary": "Verification signal requires review before higher-confidence interpretation.",
  "verified_at": "2026-05-27T00:00:00Z",
  "provenance": {
    "record_ref": "hc://record/...",
    "trace_ref": "audit://trail/..."
  },
  "review": {
    "human_supervised_validation_required": true,
    "route_state": "FEDERATION_REVIEW_ACTIVE"
  }
}
```

### Example F: Degraded validator response

A validator dependency outage returns a degraded response:

- state returns `ADVISORY` or `UNRESOLVED` based on evidence completeness
- includes degraded capability indicator
- includes retry guidance and escalation hint
- includes continuity warning linkage if checkpoint freshness is affected

## 7) Alignment with related architecture references

This runtime API contract architecture aligns with:

- `docs/core/cross-fabric-trust-interoperability.md`
- `docs/core/global-verification-gateway-federation.md`
- `docs/core/operational-trust-fabric-coordination.md`
- `docs/core/distributed-trust-propagation.md`
- `docs/core/runtime-policy-enforcement.md`
- `docs/core/runtime-observability-and-telemetry-model.md`

## 8) Boundary reminder

This document is architectural guidance for documentation and review planning only.

It does not modify schema contracts, validator logic, federation logic, policy evaluator behavior, canonical records, signing semantics, or workflow controls.

HC:// remains an advisory verification and provenance surface with human-supervised validation as a required control boundary.
