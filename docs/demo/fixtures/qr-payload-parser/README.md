# QR Payload Parser Fixtures

> **Status:** PR #663 reviewer examples, test-backed by PR #664 and PR #667 golden output coverage
> **Scope:** documentation and demo fixtures only
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed

## Purpose

These fixtures make the local HC:// QR payload parser and local QR record bridge easier to review. They provide small payload examples and expected parser behavior for the CLI runner added in #662. PR #664 adds tests that run these fixtures through the parser CLI and compare stable public-safe output fields only. PR #667 adds explicit matching, mismatched, and uppercase `payload_hash` fixture coverage. PR #669 adds a local-only bridge CLI runner that accepts the same one-argument QR payload JSON shape:

```bash
python scripts/run_qr_payload_parser.py '<payload-json-string>'
python scripts/run_qr_record_bridge.py '<payload-json-string>'
```

The fixtures are not canonical records, schemas, validators, signed QR payloads, production QR manifests, backend/API responses, runtime lookup material, or evidence that a real-world claim is true. Their `payload_hash` values exercise the parser-local advisory hash check only. The local QR record bridge must not treat these demo fixtures as canonical records; bridge lookup remains limited to `records/pending/*.json`, `records/verified/*.json`, and `records/archived/*.json`.

PR #670 adds the first local combined advisory verification output through `run_qr_public_validator(payload, repo_root=None)`. The combined result reuses the QR parser, QR record bridge, and Local Public Validator lookup/schema/hash advisory result when exactly one allowed local canonical record is found. It remains local-only and public-safe: it does not fetch `canonical_url`, call a network, use a backend/API, verify signatures, prove QR authenticity, prove issuer authority, prove truth, or claim production readiness. Human review remains required.

The golden tests intentionally compare only stable parser output boundaries: `status`, the safety markers, and the list shape/content presence of `warnings` and `errors`. They do not test exact wording beyond current stable marker phrases needed to identify missing-field, unknown-field, malformed-payload, and mismatched `payload_hash` handling.


## Local QR Record Bridge Boundary

PR #668 adds a local advisory bridge helper that can compare a parser-valid QR payload `content_hash` with the `content_hash` on exactly one matched local canonical record. PR #669 exposes that helper through `scripts/run_qr_record_bridge.py` for local reviewer checks. The CLI prints deterministic JSON with sorted keys and no extra prose on stdout. It does not add network calls, backend/API behavior, signature verification, QR authenticity proof, issuer-authority proof, canonical URL fetching, schema changes, validator changes, or production claims.

A `content_hash` match means only that the QR payload hash string matches the local canonical record hash string in the inspected checkout after lowercase/whitespace normalization. It does not prove QR authenticity, record truth, issuer authority, legal status, regulatory status, safety certification, forensic certainty, or production readiness. Human review remains required. Demo fixtures in this directory are not canonical records and are not lookup targets for the bridge.

## Safety Markers

Every parser result must preserve these public-safe markers:

```json
{
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "human_review_required": true
}
```

These markers remain required even when `status` is `valid_payload`.

## Quickstart

Run each example from the repository root. The CLI accepts one JSON string argument, so these examples pass fixture contents with command substitution.

To run the fixture-backed parser golden output tests, bridge CLI tests, and combined local QR Public Validator tests:

```bash
python -m pytest tests/test_qr_payload_parser.py
python -m pytest tests/test_qr_record_bridge.py
python -m pytest tests/test_qr_public_validator.py
```

### Valid Payload Example

```bash
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/valid-payload.json)"
```

Expected behavior:

- `status` is `valid_payload`;
- `warnings` is empty;
- `errors` is empty;
- the parser-local advisory `payload_hash` check passes;
- safety markers remain `advisory_only: true`, `public_safe: true`, `truth_guarantee: false`, and `human_review_required: true`.

### Matching Payload Hash Example

```bash
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/matching-payload-hash.json)"
```

Expected behavior:

- `status` is `valid_payload`;
- `warnings` is empty;
- `errors` is empty;
- the parser-local advisory `payload_hash` check passes;
- safety markers remain `advisory_only: true`, `public_safe: true`, `truth_guarantee: false`, and `human_review_required: true`.

### Mismatched Payload Hash Example

```bash
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/mismatched-payload-hash.json)"
```

Expected behavior:

- `status` is `invalid_payload`;
- `warnings` is empty;
- `errors` reports the parser-local advisory `payload_hash` mismatch;
- the mismatch is a local integrity-failure signal only, not QR authenticity, signature verification, or truth verification;
- safety markers remain `advisory_only: true`, `public_safe: true`, `truth_guarantee: false`, and `human_review_required: true`.

### Uppercase Payload Hash Example

```bash
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/uppercase-payload-hash.json)"
```

Expected behavior:

- `status` is `valid_payload`;
- uppercase hexadecimal `payload_hash` input is normalized for comparison and does not fail only because of uppercase hex;
- `warnings` is empty;
- `errors` is empty;
- safety markers remain `advisory_only: true`, `public_safe: true`, `truth_guarantee: false`, and `human_review_required: true`.

### Missing Field Example

```bash
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/missing-field-payload.json)"
```

Expected behavior:

- `status` is `invalid_payload`;
- `warnings` identifies the missing required field;
- `errors` states that required field(s) are missing;
- safety markers remain present and human review remains required.

### Malformed JSON Example

```bash
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/malformed-payload.txt)"
```

Expected behavior:

- `status` is `malformed_payload`;
- `errors` explains that the QR payload is malformed JSON;
- no network, backend, API, URL fetch, signature verification, record lookup, or truth verification is attempted;
- safety markers remain present and human review remains required.

### Unknown Field Example

```bash
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/unknown-field-payload.json)"
```

Expected behavior:

- `status` is `valid_payload` when all required fields are otherwise well-shaped;
- `warnings` reports that the unknown field was ignored;
- `errors` is empty because the fixture `payload_hash` was computed over the full payload object after removing `payload_hash`;
- ignored fields do not create hidden defaults, network discovery, backend/API lookup, record truth verification, or signature verification.

## Combined Local QR Public Validator

`run_qr_public_validator(payload, repo_root=None)` combines the parser, the QR record bridge, and the Local Public Validator lookup/schema/hash advisory result into one public-safe local result. The `local_validator` field is included only when lookup finds exactly one allowed local canonical record; otherwise it is `null`.

Combined statuses are `qr_record_validated`, `qr_record_mismatch`, `record_not_found`, `duplicate_record_id`, `invalid_payload`, `malformed_payload`, and `validation_not_checked`. The combined result is advisory-only and local-only. QR payload validity does not prove QR authenticity, `content_hash` match does not prove truth, and local schema/hash validation does not prove issuer authority. The helper does not fetch `canonical_url`, call a network, use a backend/API, verify signatures, or claim production readiness. Human review remains required.

## Bridge CLI Quickstart

The bridge runner accepts one QR payload JSON string argument and returns public-safe JSON from `check_qr_payload_record_bridge`:

```bash
python scripts/run_qr_record_bridge.py "$(cat docs/demo/fixtures/qr-payload-parser/matching-payload-hash.json)"
```

Expected behavior for these demo fixtures is usually `record_not_found`, because this fixture directory is intentionally not a canonical record lookup path. A `bridge_match` can occur only when the payload `record_id` resolves to exactly one allowed local canonical record under `records/pending/`, `records/verified/`, or `records/archived/` and the payload `content_hash` matches that record's `content_hash`. `bridge_match` remains advisory-only and does not prove QR authenticity, signature verification, `canonical_url` control, record truth, safety, legality, regulatory status, or production readiness.

## Status Meanings

| Status | Meaning |
| --- | --- |
| `valid_payload` | The JSON object has the required MVP parser fields, locally checked field shapes, and any present advisory `payload_hash` consistency check passes. This is not a QR authenticity proof, signature verification, canonical URL fetch, record lookup, record truth verification, or production trust decision. |
| `invalid_payload` | The JSON object was parsed, but required fields, field types, blank values, `record_id` shape, `canonical_url` shape, `issued_at` shape, or advisory `payload_hash` consistency failed local checks. Human review remains required. |
| `malformed_payload` | The input could not be parsed as a JSON object. The parser fails safely with public-safe errors and does not call a network, backend, API, or runtime lookup. |

## Advisory Payload Hash Rule

For this MVP parser only, `payload_hash` is checked with this parser-local advisory canonicalization rule:

1. parse the payload as a JSON object;
2. remove the `payload_hash` field before hashing;
3. dump JSON with sorted keys;
4. use compact separators;
5. encode the canonical JSON as UTF-8;
6. compute the SHA-256 hexadecimal digest;
7. compare the digest to `payload_hash` after normalizing hexadecimal case and surrounding whitespace.

This is an advisory consistency check, not signature verification, QR authenticity proof, final signing canonicalization standard, canonical URL fetch, or record truth verification. A mismatch returns `invalid_payload` as the safer local integrity-failure signal while preserving the stable public-safe result contract. Human review remains required.

## Fixture Guide

| Fixture | Expected status | Review purpose |
| --- | --- | --- |
| [`valid-payload.json`](valid-payload.json) | `valid_payload` | Shows the smallest complete public-safe JSON shape accepted by the parser. |
| [`matching-payload-hash.json`](matching-payload-hash.json) | `valid_payload` | Shows explicit matching parser-local advisory `payload_hash` behavior. |
| [`mismatched-payload-hash.json`](mismatched-payload-hash.json) | `invalid_payload` | Shows that a mismatched parser-local advisory `payload_hash` returns a public-safe local integrity-failure signal. |
| [`uppercase-payload-hash.json`](uppercase-payload-hash.json) | `valid_payload` | Shows that uppercase hexadecimal `payload_hash` input is normalized for comparison. |
| [`missing-field-payload.json`](missing-field-payload.json) | `invalid_payload` | Shows missing required field handling without falling back to hidden defaults. |
| [`malformed-payload.txt`](malformed-payload.txt) | `malformed_payload` | Shows safe handling of invalid JSON input. |
| [`unknown-field-payload.json`](unknown-field-payload.json) | `valid_payload` with a warning | Shows that unknown fields are ignored with a warning when required fields are valid. |

## Required Warnings

The parser checks payload shape and a parser-local advisory `payload_hash` consistency signal only. It does not:

- prove QR authenticity;
- verify signatures;
- fetch `canonical_url`;
- call a network, backend, or API;
- verify record truth;
- replace human-supervised review.

Use these fixtures for reviewer orientation only. They are intentionally small, public-safe examples for understanding parser output boundaries.
