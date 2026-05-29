# Advisory Rate Limit Warning Contract

Metadata:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- Runtime behavior change: none.
- Schema mutation: none.
- Enforcement behavior: none.
- Human final authority: required for interpretation and any mitigation decision.

## Contract summary

HC:// runtime rate-limit signals are advisory warnings, not autonomous enforcement. They exist to help operators notice repeated malformed validation attempts, repeated QR spoof inputs, replay-risk patterns, brute-force style probing, and degraded validator states while preserving deterministic public response keys.

A runtime response that carries an advisory rate-limit recommendation must preserve:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `warnings` as an always-present list
- `request_denied=false` in QR scan or abuse-signal summaries
- visible `human_final_authority` or equivalent human-supervised validation language
- no raw secrets, tokens, keys, credentials, or private request bodies
- no Redis, database, JWT, or Vault dependency

## Deterministic response keys

This section preserves deterministic response keys for advisory rate-limit review.

The top-level response keys documented in `docs/runtime/public-response-contract.md` remain stable. Abuse-control warnings may add values inside `warnings` or advisory summary subfields, but they must not remove existing top-level keys, hide degraded runtime state, or convert advisory warnings into request denial behavior.

## Advisory warning code

The public-safe warning code for operator review is:

```text
rate_limit_recommended
```

Recommended public-safe warning text:

```text
rate_limit_recommended: repeated HC:// abuse indicators observed; operator-side mitigation may be considered outside the trust kernel after human-supervised validation.
```

This warning means only that operator-side mitigation may be considered outside the HC:// runtime advisory layer. It does not block a request, deny a request, quarantine an input, change signing logic, change validator logic, mutate schemas, or produce a truth guarantee.

## Pattern examples

| Example pattern | Expected advisory result | Forbidden runtime result |
| --- | --- | --- |
| Repeated malformed validation input | Warning remains public-safe; `warnings` exists; human-supervised validation remains visible. | Request denial, quarantine, hidden fallback, or raw input echo. |
| Repeated QR spoof pattern | Spoof-risk warning remains advisory and may recommend operator-side rate limiting. | Autonomous QR blocking or changed signing/trust-anchor behavior. |
| Replay-risk pattern | Replay warning remains visible in audit trail context. | Autonomous account lockout or suppression of replay/degraded state. |
| Brute-force style probing | `rate_limit_recommended` may be documented for operator review. | Redis/database/JWT/Vault implementation or runtime enforcement. |

## Infrastructure enforcement boundary

Any real throttling, request shaping, queue control, account control, CAPTCHA, web application firewall rule, reverse-proxy rate limit, hosting-provider limit, or incident response action belongs to the operator/infrastructure layer.

The HC:// runtime advisory layer only preserves public-safe visibility. Enforcement decisions require human-supervised validation and must be documented separately from runtime response semantics.
