# HC:// Public Verification Gateway Runtime Flow Specification

This document defines the runtime flow specification for the HC:// Public Verification Gateway in HC-TRUST-LAYER so QR-based verification can operate as a complete operational lifecycle rather than a static documentation model.

Scope boundaries:

- Documentation-only runtime specification.
- Advisory verification posture is preserved.
- Human-supervised validation remains required for consequential decisions.
- No schema modifications.
- No validator modifications.
- No signing, federation, policy, or canonical record behavior changes.
- No production-readiness or truth-guarantee claims.

## 1. Gateway entry lifecycle

The Gateway entry lifecycle begins when a public user opens an HC:// verification URL directly or through a QR route.

Lifecycle checkpoints:

1. Entry source is identified (QR, copied link, shared deep-link).
2. Route parameters are normalized into an agent context for lookup.
3. Public-safe rendering mode is selected.
4. Runtime state initializes as `unresolved` until lookup and verification complete.

## 2. QR scan intake

QR scan intake standardizes decode and route parsing behavior:

1. QR payload is decoded.
2. Gateway validates route shape and required identifiers.
3. Gateway rejects malformed or spoof-like routes into safe failure rendering.
4. Gateway preserves an audit trail event for intake outcome.

QR intake remains routing-only. A QR scan is not standalone proof.

## 3. Record lookup routing

Record lookup routing resolves the requested record through HC-TRUST-LAYER public verification surfaces:

1. Gateway checks record identifier format.
2. Gateway routes to record lookup endpoints defined by repository documentation boundaries.
3. Gateway collects record metadata, provenance references, and visible continuity context.
4. Missing or inaccessible records transition to `unavailable` with public-safe messaging.

## 4. Hash verification sequence

Hash verification sequence compares caller-provided or record-presented hash context against available canonical references:

1. Capture candidate hash input from route or linked record context.
2. Resolve expected hash context from visible verification materials.
3. Compare candidate and expected hash values.
4. Emit comparison outcome to runtime state machine and audit trail.

Hash mismatch does not assert intent; it triggers advisory and escalation visibility.

## 5. Trust-state evaluation

Trust-state evaluation maps runtime evidence into public-facing advisory states:

- `verified` — record and hash signals align with available verification context.
- `advisory` — verification context is present but requires caution or reviewer interpretation.
- `disputed` — dispute indicators are present in visible trust-layer context.
- `unresolved` — insufficient evidence to complete a trust interpretation.
- `unavailable` — required verification surfaces cannot be reached or loaded.

State rendering must preserve human-supervised validation language.

## 6. Advisory/risk display routing

Advisory/risk display routing determines the response panel and warning emphasis:

1. Runtime state is mapped to a user-visible response template.
2. Risk copy includes spoofing and interpretation boundaries.
3. Gateway displays next-step guidance for human-supervised validation.
4. High-risk states emphasize dispute and continuity warnings before confidence cues.

## 7. Audit/history exposure

Audit/history exposure ensures public traceability without exposing restricted internals:

1. Gateway presents links to public audit trail and history surfaces.
2. Event timeline includes intake, lookup, and verification milestones.
3. Provenance references remain attributable and challengeable.
4. Sensitive internals remain outside public-safe response boundaries.

## 8. Federation escalation trigger

Federation escalation trigger is advisory routing, not automatic federation mutation:

1. Trigger conditions include `disputed`, repeated `unresolved`, continuity anomalies, or unresolved provenance conflicts.
2. Gateway surfaces escalation recommendation and reviewer handoff instructions.
3. Runtime records escalation event intent in audit trail continuity.
4. Human-supervised validation is required before consequential federation actions.

## 9. Runtime continuity behavior

Runtime continuity behavior preserves stable interpretation across refreshes and repeated scans:

1. Same input route should reproduce equivalent advisory state semantics when underlying data is unchanged.
2. Continuity warning signals must remain visible until evidence changes.
3. State transitions are logged as audit trail continuity events.
4. Gateway avoids silent state downgrades.

## 10. Failure-state handling

Failure-state handling defines bounded responses for operational errors:

- Parse failure -> `unresolved` or `unavailable` with corrective route guidance.
- Lookup timeout -> `unavailable` with retry guidance.
- Verification conflict -> `advisory` or `disputed` with escalation path.
- Missing artifacts -> `unresolved` with human review reminder.

Failure responses must preserve safe language and avoid certainty claims.

## 11. Public-safe response boundaries

Public-safe response boundaries constrain what the Gateway can assert:

- Do not assert legal finality, forensic certainty, or autonomous governance outcomes.
- Do not expose restricted internals, private reviewer context, or non-public trust-kernel detail.
- Keep responses concise, mobile-readable, and review-oriented.
- Preserve advisory-only posture and explicit human-supervised validation reminders.

## 12. Anti-spoof verification notes

Anti-spoof notes for public runtime behavior:

1. Verify domain and route integrity before trust interpretation.
2. Treat copied or re-hosted QR artifacts as potentially spoofed entry points.
3. Cross-check hash, record identity, and provenance before any consequential reliance.
4. Promote user-visible caution when route integrity or continuity is ambiguous.

## Operational flow examples

### Example A: nominal verified path

`QR -> Gateway -> Validator -> Trust Layer -> Public Response`

1. QR provides valid record and hash parameters.
2. Gateway routes request and receives matching verification context.
3. Validator confirms hash alignment with visible record context.
4. Trust Layer resolves advisory runtime state to `verified`.
5. Public Response shows verified advisory state, audit trail links, and human-supervised validation reminder.

### Example B: advisory mismatch path

`QR -> Gateway -> Validator -> Trust Layer -> Public Response`

1. QR route resolves to record identifier, but candidate hash differs from visible expected context.
2. Gateway records mismatch event and routes evidence to Validator.
3. Validator returns conflict outcome without certainty claims.
4. Trust Layer sets runtime state to `advisory` or `disputed` based on available dispute markers.
5. Public Response prioritizes warning copy, audit/history exposure, and federation escalation guidance.

### Example C: unavailable lookup path

`QR -> Gateway -> Validator -> Trust Layer -> Public Response`

1. QR decodes successfully, but lookup surface is unreachable.
2. Gateway emits availability failure event.
3. Validator cannot complete evidence comparison.
4. Trust Layer keeps state as `unavailable`.
5. Public Response shows retry and human-supervised validation guidance with no guarantee language.

## Implementation boundary reminder

This runtime flow specification is documentation guidance only. It does not modify schemas, validators, federation behavior, signing semantics, canonical records, or policy evaluator logic in HC-TRUST-LAYER.

## Related references

- `docs/core/public-qr-verification-gateway.md`
- `docs/core/runtime-state-model.md`
- `docs/core/trust-state-persistence-and-audit-runtime.md`
- `docs/protocol-graph-integrity.md`
- `docs/anti-spoofing-foundations.md`

- `docs/core/trust-state-scoring-and-confidence-model.md`
