# QR Payload Parser Fixtures

> **Status:** PR #663 reviewer examples, test-backed by PR #664 golden output coverage
> **Scope:** documentation and demo fixtures only
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed

## Purpose

These fixtures make the local HC:// QR payload parser easier to review. They provide small payload examples and expected parser behavior for the CLI runner added in #662. PR #664 adds tests that run these fixtures through the CLI and compare stable public-safe output fields only:

```bash
python scripts/run_qr_payload_parser.py '<payload-json-string>'
```

The fixtures are not canonical records, schemas, validators, signed QR payloads, production QR manifests, backend/API responses, runtime lookup material, or evidence that a real-world claim is true.

The golden tests intentionally compare only stable parser output boundaries: `status`, the safety markers, and the list shape/content presence of `warnings` and `errors`. They do not test exact wording beyond current stable marker phrases needed to identify missing-field, unknown-field, and malformed-payload handling.

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

To run the fixture-backed golden output tests:

```bash
python -m pytest tests/test_qr_payload_parser.py
```

### Valid Payload Example

```bash
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/valid-payload.json)"
```

Expected behavior:

- `status` is `valid_payload`;
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
- `errors` is empty;
- ignored fields do not create hidden defaults, network discovery, backend/API lookup, record truth verification, or signature verification.

## Status Meanings

| Status | Meaning |
| --- | --- |
| `valid_payload` | The JSON object has the required MVP parser fields and locally checked field shapes. This is not a QR authenticity proof, signature verification, canonical URL fetch, record lookup, record truth verification, or production trust decision. |
| `invalid_payload` | The JSON object was parsed, but required fields, field types, blank values, `record_id` shape, `canonical_url` shape, or `issued_at` shape failed local shape checks. Human review remains required. |
| `malformed_payload` | The input could not be parsed as a JSON object. The parser fails safely with public-safe errors and does not call a network, backend, API, or runtime lookup. |

## Fixture Guide

| Fixture | Expected status | Review purpose |
| --- | --- | --- |
| [`valid-payload.json`](valid-payload.json) | `valid_payload` | Shows the smallest complete public-safe JSON shape accepted by the parser. |
| [`missing-field-payload.json`](missing-field-payload.json) | `invalid_payload` | Shows missing required field handling without falling back to hidden defaults. |
| [`malformed-payload.txt`](malformed-payload.txt) | `malformed_payload` | Shows safe handling of invalid JSON input. |
| [`unknown-field-payload.json`](unknown-field-payload.json) | `valid_payload` with a warning | Shows that unknown fields are ignored with a warning when required fields are valid. |

## Required Warnings

The parser checks payload shape only. It does not:

- prove QR authenticity;
- verify signatures;
- fetch `canonical_url`;
- call a network, backend, or API;
- verify record truth;
- replace human-supervised review.

Use these fixtures for reviewer orientation only. They are intentionally small, public-safe examples for understanding parser output boundaries.
