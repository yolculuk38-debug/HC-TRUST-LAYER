# Runtime Public Response Contract

This document defines the public response contract for HC:// reference runtime integration surfaces. It is a documentation and test-locking aid only; it does not mutate schema contracts, workflows, governance, signing logic, security policy, federation behavior, or validator semantics.

## Scope

Applies to public-safe runtime responses under:

- `GET /health`
- `GET /verify/{record_id}`
- `POST /verify/{record_id}`
- `GET /qr/{record_id}`
- `GET /verify/{record_id}/history`
- runtime telemetry endpoints
- advisory federation review placeholders

The `POST /verify/{record_id}` QR validation flow is the primary integration-facing response shape covered here. Health, telemetry, history, and federation placeholder responses share the public-safe safety flags and warning-list behavior but may expose endpoint-specific fields.

## Stable public keys

Verification response builders preserve these base keys in this order:

| Key | Type | Contract |
| --- | --- | --- |
| `status` | string | Runtime status label for the advisory response. |
| `advisory_only` | boolean | Always `true`; runtime output is not autonomous final authority. |
| `public_safe` | boolean | Always `true`; response fields are intended for public-safe integration use. |
| `message` | string | Public-safe explanatory text with no secret-bearing values. |
| `warnings` | list of strings | Always present, even when empty. |
| `traceable` | boolean | Always `true` for public response builder output. |
| `truth_guarantee` | boolean | Always `false`; no truth guarantee is asserted. |
| `record_id` | string, when route scoped | Public-safe record identifier for route-scoped responses. |

QR validation responses additionally preserve these keys:

| Key | Type | Contract |
| --- | --- | --- |
| `trust_state` | string | Advisory trust-state label from the runtime decision path. |
| `replay_warning` | boolean | Replay marker visibility; warning only, not blocking. |
| `continuity_warning` | boolean | Continuity warning visibility for human-supervised validation. |
| `degraded_runtime` | boolean | Degraded state visibility; never hidden by fallback behavior. |
| `recovery_mode` | boolean | Visible recovery-mode indicator when degraded runtime behavior is detected. |
| `public_exposure` | string | Public exposure classification such as `standard` or `restricted`. |
| `qr_risk_level` | string | Advisory QR risk label: `LOW`, `MEDIUM`, `HIGH`, or `INCIDENT`. |
| `qr_risk_reasons` | list of strings | Public-safe QR spoof risk reasons. |
| `human_review_recommended` | boolean | Human-supervised validation recommendation signal. |
| `escalation_queued` | boolean | Visibility that advisory escalation routing was queued locally. |
| `incident_summary` | object | Public-safe incident grouping summary for repeated high-risk QR indicators. |
| `qr_scan_summary` | object | Public-safe QR and abuse-signal summary metadata. |

Malformed request responses preserve the base route-scoped keys and add:

| Key | Type | Contract |
| --- | --- | --- |
| `malformed_input` | boolean | Always `true` for malformed validator request payloads. |
| `public_exposure` | string | Always `restricted` for malformed validator request payloads. |

## Advisory semantics

Runtime public responses must preserve:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `warnings` always present as a list
- human-supervised validation as final interpretation authority

Warnings for abuse, spoof, replay, malformed input, degraded runtime state, and continuity concerns are advisory visibility signals. They do not create autonomous blocking, quarantine, signing changes, security-policy changes, workflow changes, governance changes, or schema mutation.

## Warning behavior

- Empty warning sets are represented as `warnings: []`.
- Warning strings must remain public-safe and must not echo secrets, tokens, private keys, or raw credential-like material.
- Degraded states remain visible through `degraded_runtime`, `recovery_mode`, telemetry degraded fields, and warning text where applicable.
- Replay, QR spoof, and abuse-signal warnings remain advisory-only and route to human-supervised validation instead of autonomous enforcement.

## Rate-limit advisory warnings

Rate-limit and abuse-control warnings are advisory runtime signals only. The public-safe warning code `rate_limit_recommended` may be documented or surfaced when repeated malformed validation attempts, repeated QR spoof inputs, replay-risk markers, or brute-force style probing indicate that operator-side mitigation should be considered.

The warning does not deny requests, quarantine inputs, mutate schemas, change signing logic, weaken validators, add Redis, add database storage, add JWT authentication, add Vault secret access, or move enforcement into the trust kernel. Enforcement belongs to the operator/infrastructure layer and requires human-supervised validation.

See `docs/runtime/advisory-rate-limit-warning-contract.md` and `docs/security/rate-limiting-abuse-control.md` for the advisory boundary.

## Integration-facing examples

### Normal validation response

```json
{
  "status": "ADVISORY",
  "advisory_only": true,
  "public_safe": true,
  "message": "Advisory HC:// runtime flow executed: request → validator pipeline → trust-state engine → event append → response contract → continuity history.",
  "warnings": [],
  "traceable": true,
  "truth_guarantee": false,
  "record_id": "normal-runtime-contract",
  "trust_state": "ADVISORY",
  "replay_warning": false,
  "continuity_warning": false,
  "degraded_runtime": false,
  "recovery_mode": false,
  "public_exposure": "standard",
  "qr_risk_level": "LOW",
  "qr_risk_reasons": [],
  "human_review_recommended": false,
  "escalation_queued": false,
  "incident_summary": {
    "active": false,
    "group_keys": [],
    "related_high_findings": 0
  },
  "qr_scan_summary": {
    "advisory_only": true,
    "public_safe": true,
    "truth_guarantee": false,
    "request_denied": false,
    "human_final_authority": true
  }
}
```

The `qr_scan_summary` example is abbreviated. Integrators should preserve unknown public-safe subkeys and rely on the stable top-level keys above.

### Malformed input response

```json
{
  "status": "MALFORMED_INPUT",
  "advisory_only": true,
  "public_safe": true,
  "message": "Malformed HC:// validator input was rejected within advisory runtime boundaries. Human-supervised validation is required before trust interpretation.",
  "warnings": [
    "Validator input was malformed, incomplete, or not processable as a public-safe QR verification request.",
    "No hidden fallback behavior was applied; warning routing remains explicit."
  ],
  "traceable": true,
  "truth_guarantee": false,
  "record_id": "malformed-runtime-contract",
  "malformed_input": true,
  "public_exposure": "restricted"
}
```

## Persistence roundtrip audit

For advisory write → read → re-verify review boundaries, see `docs/runtime/persistence-roundtrip-audit.md` and `docs/security/persistence-risk-checklist.md`. Runtime roundtrip audit documentation preserves `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, an always-present `warnings` list, visible degraded states, visible replay warnings, no hidden fallback behavior, and human-supervised validation as final authority. It does not add Redis, database storage, schema mutation, workflow mutation, governance mutation, or canonical artifact mutation.

## Configuration and secret boundary

Public HC:// runtime responses must keep public verification data separate from runtime configuration, signing material, and operational secrets. Secret boundary architecture guidance lives in `docs/security/secret-boundary-architecture.md`; the operator configuration checklist lives in `docs/runtime/configuration-boundary-checklist.md`. These references are advisory documentation only and do not add secret storage, Vault, Redis, JWT, schema changes, workflow changes, signing changes, or runtime behavior changes.

## Non-goals

This contract documentation does not implement Redis, JWT, Vault, signing changes, autonomous blocking, quarantine behavior, schema mutation, governance mutation, workflow mutation, or federation behavior changes.
