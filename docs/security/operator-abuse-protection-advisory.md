# Operator Abuse Protection Advisory

Metadata:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- Runtime behavior change: advisory abuse-signal visibility only.
- Schema mutation: none.
- Workflow mutation: none.
- Human final authority: required for rate-limit policy, review prioritization, and any enforcement decision.

## Purpose

This note gives HC:// runtime operators public-safe guidance for repeated malformed, spoof-risk, replay-risk, and degraded validation patterns.

The runtime may expose advisory warnings and deterministic summary fields so operators can notice repeated patterns. The helper does not deny requests, quarantine inputs, mutate canonical records, change signing logic, change validators, implement Redis, implement JWT, implement Vault, or create autonomous enforcement.

## Operator-side rate limiting guidance

Operators should treat operator-side rate limiting as an external control and apply any rate limiting outside the trust kernel at an ingress, proxy, or hosting-control layer they already supervise.

Recommended review posture:

1. Treat repeated malformed inputs as a capacity and hygiene signal, not as proof of attacker identity.
2. Treat repeated spoof-risk QR inputs as a review-prioritization signal that keeps human-supervised validation visible.
3. Treat repeated replay markers as an audit trail continuity signal that remains advisory unless a human operator applies external controls.
4. Treat degraded validator state as visible operational context; do not hide degraded states to preserve a cleaner result.
5. Keep public warnings concise and avoid raw secrets, tokens, credentials, private keys, or request bodies.
6. Preserve `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and an always-present `warnings` field.

## Boundary

This document is not an enforcement policy and does not change HC:// verification semantics.

Any future blocking, quarantine, account control, Redis-backed counter, JWT authentication, Vault secret-management, signing, validator, schema, federation, policy evaluator, workflow, or governance change requires separate review and human-supervised validation.
