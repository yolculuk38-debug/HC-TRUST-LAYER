# HC Protocol v1 Specification Foundation

## 1. Scope
HC Protocol v1 defines a protocol-first verification infrastructure for HC:// records. This document establishes baseline semantics for lifecycle, trust, auditability, federation, and portability.

## 2. Record Lifecycle
1. **ingested**: Record accepted by a node with syntactic validation.
2. **normalized**: Canonicalized representation and deterministic hash established.
3. **pending_verification**: Awaiting validator and witness workflows.
4. **verified**: Verification threshold met per policy.
5. **quarantined**: Temporarily isolated due to risk conditions.
6. **superseded**: Replaced by a newer revision while retained for history.
7. **challenged**: Marked for targeted re-check after a formal challenge.
8. **disputed**: Conflicting evidence under adjudication.
9. **revoked**: Explicitly invalidated with signed cause.
10. **superseded**: Replaced by newer revision while retained for history.
11. **archived**: Frozen for long-term retention.

Lifecycle rules:
- States are append-only in history; current state is a projection.
- `quarantined` does not delete prior evidence.
- `superseded` records remain addressable.

## 3. Verification States
- `unverified`: no validator decision yet.
- `in_review`: active validator/witness processing.
- `verified`: policy threshold satisfied.
- `disputed`: conflicting evidence or governance challenge.
- `revoked`: explicit invalidation with signed cause.
- `quarantined`: elevated risk pending adjudication.

## 4. Validator Flow
1. Pull canonical record and referenced artifacts.
2. Recompute content hash and compare to declared hash.
3. Validate schema and required protocol metadata.
4. Evaluate policy checks and risk flags.
5. Emit signed validator decision with timestamp.
6. Publish decision to federation peers.

## 5. Witness Flow
1. Witness receives canonical record hash.
2. Witness verifies context and provenance references.
3. Witness signs decision (`attest`, `reject`, or `abstain`).
4. Witness signature is bound to record hash and timestamp.
5. Witness package is persisted in append-only storage.

## 6. Replay Protection
- Every decision binds to immutable `record_id + content_hash + revision context`.
- Timestamp and monotonic sequence constraints prevent stale replays.
- Duplicate signatures are ignored unless cryptographically distinct and valid.
- Cross-node replay anomalies move record to `quarantined` until resolved.

## 7. Federation Basics
- Nodes exchange verification events, not mutable record bodies.
- Trust propagation is weighted by validator reputation policy.
- Conflicting decisions remain visible as parallel evidence entries.
- Federation can operate in partial sync; eventual consistency is required.

## 8. Trust Terminology
- **trust score**: derived confidence value for a record.
- **trust vector**: component-level signals (validator quality, witness quality, risk penalties).
- **trust domain**: bounded policy context (node, consortium, public federation).

## 9. Audit Terminology
- **audit chain**: append-only sequence of verification and governance events.
- **audit event**: immutable, timestamped record of protocol action.
- **audit proof**: portable export of event subset with integrity metadata.

## 10. Export/Import Terminology
- **export package**: deterministic bundle of record, signatures, and audit references.
- **import verification**: process to validate package integrity and chain linkage.
- **portable proof**: minimal evidence set sufficient for third-party verification.

## 11. Compatibility Notes
- This specification is forward-compatible with federation expansion.
- Optional provenance adapters can map to external standards (including C2PA) without altering core lifecycle semantics.
