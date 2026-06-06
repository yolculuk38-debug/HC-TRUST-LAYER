# Local Public Validator Golden Output Fixtures

These JSON files are illustrative, test-backed golden output fixtures for the local Public Validator CLI result contract added during the #654-#658 sequence.

They are intended for reviewer comparison, documentation examples, onboarding, and stable contract-shape checks. They are not canonical HC:// records, schemas, validator logic, generated indexes, signed payloads, QR artifacts, production API responses, or evidence of truth verification.

## Fixtures

- [`found.json`](found.json): example `found` result for `HC-EXAMPLE-2026-0001`.
- [`not-found.json`](not-found.json): example `not_found` result for an unknown local `record_id`.
- [`invalid-record-id.json`](invalid-record-id.json): example `invalid_record_id` result for path-like input rejected before lookup.

## Contract Boundary

Each fixture keeps the stable top-level result fields:

- `record_id`
- `status`
- `found`
- `source_path`
- `advisory_only`
- `public_safe`
- `truth_guarantee`
- `human_review_required`
- `warnings`
- `errors`
- `checked_paths`
- `schema_validation`
- `hash_validation`
- `validation_summary`

Each fixture also preserves the safety markers:

- `advisory_only: true`
- `public_safe: true`
- `truth_guarantee: false`
- `human_review_required: true`

The deterministic local lookup boundary remains:

```json
[
  "records/pending/*.json",
  "records/verified/*.json",
  "records/archived/*.json"
]
```

## Review Notes

The found fixture shows an example environment where advisory schema and hash validation both pass. Tests compare the CLI against stable fixture contract fields and intentionally avoid comparing environment-dependent schema status values directly. A local checkout without the existing schema helper dependency may return `schema_validation.status: "not_checked"` while preserving the same top-level contract and safety markers.

These fixtures do not imply production readiness, QR authenticity, signed payload verification, legal/regulatory/safety certification, issuer authority, forensic certainty, or truth verification. Human-supervised review remains required for every result.
