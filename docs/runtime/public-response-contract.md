# Runtime Public Response Contract

This document records the current public response contract boundaries for HC:// reference runtime review before any runtime or API changes. It is documentation only and does not change runtime code, schemas, validators, workflows, examples, tests, signing logic, federation logic, policy files, or canonical records.

## Current Runtime Contract

The implemented runtime response contract is the current source of truth for public runtime behavior. This note describes that implementation; it does not create a broader API promise.

Current public runtime responses are advisory-only and public-safe:

- `advisory_only=true`
- `runtime_stage=prototype`
- `verification_mode=advisory`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required` remains visible when warnings or escalation paths require review.
- `warnings` is present as a list, including when empty.

The human-supervised validation model remains the final interpretation boundary. Runtime output can support review, provenance inspection, and audit trail navigation, but it does not provide autonomous merge authority or a truth guarantee.

## Endpoint Differences

### `GET /verify/{record_id}`

`GET /verify/{record_id}` returns a lightweight advisory placeholder response for a route-scoped record lookup. It uses the public response builder and includes the base public-safe fields such as:

- `status`
- `advisory_only`
- `runtime_stage`
- `verification_mode`
- `public_safe`
- `message`
- `warnings`
- `traceable`
- `truth_guarantee`
- `human_review_required`
- `record_id`

This shape is intentionally narrow because the GET route does not run the QR validation flow.

### `POST /verify/{record_id}`

`POST /verify/{record_id}` runs the QR validation path and returns the ordered QR verification response shape. In addition to the base route-scoped keys, current runtime tests protect these response keys:

- `trust_state`
- `replay_warning`
- `continuity_warning`
- `degraded_runtime`
- `recovery_mode`
- `public_exposure`
- `qr_risk_level`
- `qr_risk_reasons`
- `human_review_recommended`
- `escalation_queued`
- `incident_summary`
- `canonical_lookup_status`
- `schema_valid`
- `hash_verified`
- `qr_scan_summary`

Malformed POST payload handling has a separate public-safe response shape that preserves the base route-scoped keys and adds:

- `detail`
- `malformed_input`
- `public_exposure`

### Why the Shapes Differ

The GET and POST routes intentionally return different response shapes because they represent different runtime paths:

- GET is a minimal advisory lookup placeholder.
- POST is an advisory QR verification flow with validation, trust-state classification, replay visibility, degraded-runtime visibility, QR risk visibility, and human review signals.

The difference is intentional and should not be treated as schema drift by itself.

## Compatibility Notes

The runtime response contract, API schema helper, and verification API documentation are related but not identical:

- The runtime response contract describes implemented public-safe runtime route output.
- The API schema helper describes an API-ready verification payload helper that includes an `api_version` field.
- Verification API documentation describes intended public API surfaces and may include route or model guidance that is broader than the current runtime implementation.

Compatibility review should compare these surfaces before changing response fields. A field appearing in one surface does not automatically mean it is guaranteed by the others.

## Rate-limit advisory warnings

Rate-limit warnings are advisory only. When emitted, the advisory warning code `rate_limit_recommended` indicates that operator or infrastructure rate-limit review may be appropriate, while preserving `warnings` always present as a list. It does not deny requests, quarantine records, or perform autonomous enforcement.

Enforcement belongs to the operator/infrastructure layer and requires separate review and human-supervised validation. This documentation does not add Redis, add database storage, add JWT authentication, add Vault secret access, add other security-control implementation, mutate schemas, weaken validators, change runtime behavior, or modify workflows, governance, policy routing, federation, signing, or canonical record handling.

## Not Yet Guaranteed

Current runtime responses do not guarantee:

- authentication
- authorization
- rate limiting
- durable persistence
- an API version field in runtime responses
- a generic exception response contract
- machine-readable warning codes

Warnings are public-safe advisory text. They should not be interpreted as stable machine-readable codes unless a future reviewed change explicitly adds that contract.

## Stability Notes

Current tests protect the base public response keys, the QR verification response keys, malformed input response keys, and the safety flags listed above. They also verify stable key order for QR verification responses and public-safe malformed-input behavior.

Compatibility should be reviewed before adding, removing, renaming, reordering, or changing the meaning of public response fields. Changes that affect trust-kernel boundaries, schema contracts, validator logic, policy interpretation, signing semantics, federation behavior, or canonical records require separate review and human-supervised validation.

## Safety Notes

Public runtime responses must continue to reinforce:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- merge authority remains human-controlled

These responses are review aids only. They do not provide production-readiness claims, autonomous blocking, autonomous governance finality, cryptographic guarantees, or policy guarantees beyond what is implemented and validated in this repository.
