# Rate Limiting and Abuse Control Architecture

Metadata:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- Runtime behavior change: none.
- Schema mutation: none.
- Workflow mutation: none.
- Storage dependency: none; no Redis implementation and no database dependency.
- Secret dependency: none; no JWT implementation, no Vault implementation, and no raw token exposure.
- Human final authority: required for interpretation and any operator-side enforcement.

## Purpose

This note defines how HC:// runtime surfaces should describe high-volume abuse indicators without adding autonomous blocking behavior. The HC-TRUST-LAYER runtime may expose public-safe advisory signals for repeated malformed validation attempts, repeated QR spoof patterns, replay-risk markers, brute-force style validation patterns, and degraded validator state.

These signals are visibility aids for operators and reviewers. They do not deny requests, quarantine records, mutate canonical records, change signing logic, weaken validators, modify federation behavior, modify policy evaluator behavior, or create production-readiness claims.

## Architectural boundary

Rate limiting is split into two clearly separated layers:

1. **Runtime advisory signal layer**: HC:// runtime responses keep deterministic response keys, include `warnings` as an always-present list, preserve `advisory_only=true`, preserve `public_safe=true`, preserve `truth_guarantee=false`, and expose suspicious patterns as advisory warnings only.
2. **Operator/infrastructure enforcement layer**: Any request throttling, IP-based controls, account controls, CAPTCHA, queue shaping, web application firewall rules, ingress proxy limits, or hosting-provider controls belong outside the trust kernel and require human-supervised validation before operational use.

The operator/infrastructure enforcement layer is separate from HC:// runtime response semantics.

The runtime advisory signal layer must never implement autonomous blocking, request denial behavior, quarantine behavior, Redis counters, database-backed counters, JWT authentication, Vault secret access, or hidden infrastructure enforcement.

## Abuse patterns to document and surface

| Pattern | Runtime advisory signal | Operator interpretation boundary |
| --- | --- | --- |
| Repeated malformed validation inputs | Public-safe warning for repeated malformed input families. | Capacity or hygiene signal; not proof of attacker identity. |
| Brute-force style validation attempts | Advisory `rate_limit_recommended` warning when repeated malformed, replay, spoof, or degraded patterns indicate high-volume probing. | Consider operator-side throttling outside HC:// runtime after human review. |
| Repeated QR spoof patterns | Public-safe warning for repeated spoof-risk QR inputs, with human-supervised validation visible. | Review routing and user-safety communication; no runtime blocking. |
| Replay-risk markers | Public-safe warning for repeated replay markers and visible replay continuity context. | Audit trail continuity review; no autonomous denial. |
| Repeated degraded validator state | Public-safe warning that degraded state remains visible. | Operational diagnosis; do not hide degraded states to preserve a cleaner response. |

## Advisory warning contract

When a rate-limit recommendation is documented or emitted by a runtime helper, it must remain advisory and public-safe:

```json
{
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "warnings": [
    "rate_limit_recommended: repeated HC:// abuse indicators observed; operator-side mitigation may be considered outside the trust kernel after human-supervised validation."
  ],
  "request_denied": false,
  "human_final_authority": true
}
```

The `rate_limit_recommended` warning is not an enforcement command. It is a public-safe prompt for operator review and does not alter validator outcomes, schema contracts, signing behavior, canonical record identity, audit trail continuity, federation state, or policy evaluator routing.

## Brute-force pattern documentation

Brute-force style validation attempts are documented as repeated, high-volume, or clustered attempts to force useful runtime behavior through malformed payloads, repeated QR spoof variants, repeated replay markers, or repeated hash/schema failures.

The HC:// runtime response may make these patterns visible through advisory warnings and summary counts, but must preserve:

- deterministic response keys
- an always-present `warnings` field
- visible degraded states
- public-safe warning text
- no raw secrets, tokens, private keys, credentials, or full request bodies
- no autonomous blocking or request denial
- human-supervised validation as final authority

## Operator-side mitigation checklist

Operators considering infrastructure-layer controls should verify:

- [ ] The runtime response remains `advisory_only=true`, `public_safe=true`, and `truth_guarantee=false`.
- [ ] `warnings` exists for empty and non-empty warning cases.
- [ ] Suspicious patterns produce advisory warnings only.
- [ ] Degraded states remain visible in public-safe responses.
- [ ] No raw secrets, tokens, keys, credentials, or private request bodies are exposed.
- [ ] Enforcement is implemented only at an operator-supervised infrastructure layer, not inside HC:// validation logic.
- [ ] Any throttling or request shaping is documented as external to the trust kernel.
- [ ] Human final authority remains visible in operator procedures and public-safe response summaries.
- [ ] No Redis, database, JWT, or Vault dependency is introduced by runtime advisory documentation.
- [ ] Audit trail and provenance continuity remain visible for review.

## Non-goals

This architecture note does not implement Redis, database storage, JWT, Vault, autonomous blocking, quarantine behavior, request denial, workflow changes, governance changes, schema changes, signing changes, validator weakening, federation behavior, policy evaluator behavior, or production enforcement guarantees.
