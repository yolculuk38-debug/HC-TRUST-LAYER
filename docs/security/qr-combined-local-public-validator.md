# Combined Local QR Public Validator

> **Status:** local advisory MVP
> **Scope:** QR payload parser + local record bridge + local Public Validator lookup/schema/hash signals
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed

## Purpose

This document describes the first combined local QR/Public Validator advisory result.

The combined flow exists to help reviewers inspect one local result that brings together:

1. QR payload parsing;
2. parser-local `payload_hash` advisory consistency;
3. QR payload `content_hash` to local canonical record `content_hash` bridge;
4. local Public Validator lookup/schema/hash advisory signals when exactly one local canonical record is found.

## Local-Only Flow

```text
QR payload JSON
↓
parse_qr_payload
↓
check_qr_payload_record_bridge
↓
lookup_public_validator_record
↓
combined public-safe advisory result
```

The lookup boundary remains unchanged and limited to:

```text
records/pending/*.json
records/verified/*.json
records/archived/*.json
```

Demo fixtures, generated artifacts, manifests, cache/export outputs, arbitrary paths, and remote URLs are not treated as canonical records.

## Result Contract

The combined result uses this stable top-level shape:

```text
status
qr_payload_status
bridge_status
record_lookup_status
content_hash_match
local_validator
warnings
errors
advisory_only
public_safe
truth_guarantee
human_review_required
```

Allowed combined statuses:

```text
qr_record_validated
qr_record_mismatch
record_not_found
duplicate_record_id
invalid_payload
malformed_payload
validation_not_checked
```

Required safety markers:

```json
{
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "human_review_required": true
}
```

## CLI Entry Point

The existing `hc-trust` console entry point exposes the combined engine without changing its parser, lookup allowlist, result contract, or network boundary:

```bash
hc-trust qr-public-validator "$(cat docs/demo/fixtures/qr-payload-parser/record-match-payload.json)"
```

For a repository checkout without an installed console script:

```bash
PYTHONPATH=src python -m hc_trust.cli qr-public-validator \
  "$(cat docs/demo/fixtures/qr-payload-parser/record-match-payload.json)"
```

The command:

- accepts exactly one QR payload JSON string;
- resolves `records/` and `schema/` from the current working directory, so run it from the repository checkout root;
- writes one deterministic, sorted JSON result to stdout with no explanatory prose;
- returns exit code `0` only for `qr_record_validated`;
- returns exit code `1` for mismatch, malformed, invalid, not-found, duplicate, or not-checked outcomes;
- preserves `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and `human_review_required=true`;
- does not read a payload file implicitly, fetch `canonical_url`, call a network/backend/API, or widen the allowed local record paths.

The bundled `record-match-payload.json` is a public-safe, non-canonical CLI input fixture that references the checked-in `HC-RELEASE-2026-0001` record. Its successful local hash comparison is test evidence for the CLI path, not proof that the QR is authentic or that the record content is true.

## Non-Claims

A combined `qr_record_validated` result does **not** prove:

- QR authenticity;
- signature verification;
- issuer authority;
- `canonical_url` ownership;
- record truth;
- legal, regulatory, forensic, food-safety, building-safety, or security certification;
- production readiness.

A `content_hash` match only means the inspected QR payload and exactly one matched local canonical record are locally advisory-consistent under the current checkout and current helper behavior.

Human review remains required for every outcome.

## Non-Goals

This combined local MVP does not:

- add signature verification;
- add QR authenticity proof;
- fetch `canonical_url`;
- call a network;
- add backend/API behavior;
- modify schemas;
- modify validators;
- modify workflows;
- widen lookup paths;
- treat demo fixtures as canonical records;
- claim truth verification.
