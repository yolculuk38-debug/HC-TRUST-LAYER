# Operational Verification Response Lifecycle

## Scope and Intent

This document defines the complete HC:// operational verification response lifecycle used by HC-TRUST-LAYER runtime components to process public verification requests from intake through public-safe response exposure.

This lifecycle is advisory-only and remains subject to human-supervised validation for disputed, high-risk, or unresolved outcomes.

## 1) Verification Request Intake

Runtime intake accepts four request entry points and normalizes them into a shared verification request envelope with provenance, request timestamp, and correlation identifiers.

1. **QR entry**
   - Intake source: QR scan request from public client flow.
   - Runtime action: decode target reference, validate format, attach client context metadata.
2. **Direct lookup**
   - Intake source: user-provided identifier or canonical reference lookup.
   - Runtime action: normalize identifier, resolve lookup target, attach lookup provenance.
3. **API request**
   - Intake source: authenticated or scoped runtime API call.
   - Runtime action: validate request contract, route request to orchestration runtime.
4. **Public verification gateway request**
   - Intake source: HC:// public verification gateway edge request.
   - Runtime action: apply gateway boundary checks, request shaping, and rate-aware intake controls.

All intake paths must preserve audit trail continuity and must not bypass verification prerequisites.

## 2) Runtime Evaluation Stages

After intake normalization, runtime processing follows ordered evaluation stages:

1. **Schema validation**
   - Confirm request and referenced payload structure validity before evaluation.
2. **Integrity/hash verification**
   - Compare provided and computed hash-linked values for integrity continuity.
3. **Trust-state evaluation**
   - Resolve current trust-state from trust-state runtime and relevant policy context.
4. **Continuity verification**
   - Evaluate record lineage, provenance continuity, and revision linkage expectations.
5. **Advisory analysis**
   - Produce human-readable advisory interpretation with explicit uncertainty markers.
6. **Escalation checks**
   - Detect conditions requiring reviewer escalation or dispute routing.
7. **Federation activation checks**
   - Determine whether federation-assisted review should be activated for conflict or ambiguity handling.

A stage failure can short-circuit later stages when continuation would create misleading public exposure.

## 3) Response Lifecycle States

Each request transitions through the following operational response states:

- **accepted**: request is normalized and admitted for runtime processing.
- **processing**: evaluation stages are currently executing.
- **verified**: runtime checks support a low-risk advisory verification outcome.
- **advisory**: response is available with cautionary interpretation or incomplete confidence.
- **disputed**: conflicting evidence or challenge path is active.
- **escalation-active**: human-supervised validation escalation is in progress.
- **unavailable**: runtime dependencies are temporarily unavailable.
- **continuity-warning**: continuity signals indicate gaps, breaks, or uncertain lineage.
- **unresolved**: runtime cannot produce a stable advisory conclusion without further review.

State transitions must be traceable, timestamped, and linked to runtime decision reasons.

## 4) Public-Safe Response Rules

Public-safe response exposure must preserve transparent verification visibility while protecting sensitive internals.

### Safe to Expose Publicly

- high-level trust-state summary
- hash-match or mismatch result category
- continuity state category
- advisory warning indicators
- dispute visibility status
- federation review status class
- non-sensitive audit/history references

### Must Remain Internal

- sensitive internal identifiers or private routing metadata
- raw policy-evaluator internals not intended for public exposure
- internal escalation notes and reviewer identity details
- protected infrastructure topology and security-sensitive runtime traces

### Audit-Safe Transparency Boundaries

- expose reason codes and state transitions in summarized form
- preserve challengeability by showing why response class was assigned
- avoid exposing restricted evidence payloads in public channels

### Privacy-Aware Verification Exposure

- disclose only minimum necessary fields for verification understanding
- redact or omit personal or sensitive metadata from public responses
- preserve provenance continuity without leaking protected context

## 5) Conditional Runtime Routing

Runtime routing is condition-driven and must remain deterministic and auditable.

### Normal Low-Risk Flow

Accepted -> Processing -> Verified -> Public-safe advisory response exposure.

### Disputed Flow

Accepted -> Processing -> Disputed -> Escalation-active -> Advisory or Unresolved response.

### Federation-Assisted Flow

Accepted -> Processing -> Federation activation checks passed -> federation review coordination -> Advisory or Disputed response.

### Continuity-Recovery Flow

Accepted -> Processing -> Continuity-warning -> recovery lookup and continuity reassessment -> Advisory or Unresolved response.

### Emergency Integrity Flow

Accepted -> Processing -> integrity/hash verification failure or replay suspicion -> escalation-active or unavailable gate -> public caution response.

## 6) Verification Response Outputs

Response outputs should be concise, mobile-readable, and challengeable.

- **trust-state summary**: high-level current trust-state with advisory framing.
- **hash-match result**: match, mismatch, or unavailable classification.
- **continuity state**: continuous, warning, or unresolved continuity signal.
- **advisory warning**: cautionary explanation for uncertainty or elevated risk.
- **dispute visibility**: whether active dispute or challenge pathway exists.
- **federation review status**: inactive, requested, active, or completed advisory status.
- **audit/history references**: non-sensitive references for traceable review continuity.

## 7) Failure-State Handling

Runtime failure states must return explicit, non-silent outcomes:

- **record missing**
  - return unavailable or unresolved state with lookup failure reason.
- **hash mismatch**
  - return advisory or disputed state with integrity warning.
- **continuity failure**
  - return continuity-warning or unresolved state and trigger escalation checks.
- **unavailable validator**
  - return unavailable state and preserve retry guidance.
- **unresolved disagreement**
  - return unresolved state with challenge path visibility.
- **replay suspicion**
  - return escalation-active or disputed state with integrity caution marker.

## 8) Operational Principles

The lifecycle follows these operational principles:

- **verification before exposure**: no public-safe response is emitted before required checks run.
- **no silent override**: conflicting or failed checks must remain visible in response state.
- **challengeable responses**: outputs must preserve dispute and review routing visibility.
- **traceable runtime decisions**: state transitions require reason-linked audit trail continuity.
- **public-safe transparency**: expose understandable outcomes while protecting restricted internals.
- **advisory-only verification**: runtime outputs are advisory and do not assert autonomous finality.

## 9) Runtime Dependency References

This lifecycle depends on coordinated behavior across these runtime surfaces:

- **validator runtime**: executes verification checks and integrity evaluation primitives.
- **persistence runtime**: stores request, state transition, and audit trail continuity records.
- **federation sync**: supports cross-boundary advisory review when federation activation is required.
- **public verification gateway**: enforces boundary-safe intake and response exposure shaping.
- **orchestration runtime**: coordinates stage ordering, routing, retries, and escalation paths.
- **trust-state runtime**: resolves current trust-state signals used by advisory response generation.

## Verification and Governance Boundary Note

This document defines operational guidance only. It does not modify schemas, validators, federation logic, signing logic, policy files, or workflow behavior. All trust-kernel-impacting changes remain subject to explicit human-supervised validation.
