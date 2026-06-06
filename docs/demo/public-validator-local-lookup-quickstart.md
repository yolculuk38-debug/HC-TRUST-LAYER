# Local Public Validator Lookup Quickstart

> **Status:** PR #657 CLI quickstart for the local Public Validator lookup
> **Scope:** documentation/examples for local `record_id` lookup and advisory schema/hash signals
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed

## Purpose

The local Public Validator lookup lets a reviewer enter a `record_id` and inspect a deterministic, public-safe JSON result from the command line. It searches only the repository's allowed local record directories and, when exactly one matching record is found, reports advisory schema and `content_hash` / SHA-256 validation signals.

Use it to understand whether a local repository checkout contains a matching public-safe record entry and whether existing local schema/hash helpers could produce advisory signals for that matched record.

## What It Does

- Accepts a single `record_id` value from the command line.
- Rejects paths, URLs, queries, blank values, and malformed `record_id` input.
- Searches only:
  - `records/pending/*.json`
  - `records/verified/*.json`
  - `records/archived/*.json`
- Ignores demo fixtures, generated indexes, manifests, cache artifacts, and export artifacts.
- Returns a deterministic JSON result with stable top-level fields for found, unknown, invalid, duplicate, and lookup-error outcomes.
- Preserves `advisory_only: true`, `public_safe: true`, `truth_guarantee: false`, and `human_review_required: true` for every result.

## What It Does Not Do

This command is intentionally bounded. It is:

- local-only;
- advisory-only;
- public-safe;
- not a production API;
- not truth verification;
- not a QR authenticity proof;
- not signed payload verification;
- not legal, regulatory, food-safety, building-safety, security, issuer-authority, or compliance certification;
- not a backend, network service, federation service, database query, or live registry lookup;
- not a replacement for human-supervised review.

Human review remains required for every result, including `found` results and validation pass signals.

## Run the Command

From the repository root:

```bash
python scripts/run_public_validator_lookup.py HC-EXAMPLE-2026-0001
```

The command prints JSON to standard output.

## Example: Found Record

A found result has `status: "found"`, `found: true`, and a `source_path` within the allowed local record directories.

```json
{
  "record_id": "HC-EXAMPLE-2026-0001",
  "status": "found",
  "found": true,
  "source_path": "records/pending/HC-EXAMPLE-2026-0001.json",
  "schema_validation": {
    "status": "pass",
    "errors": []
  },
  "hash_validation": {
    "status": "pass",
    "errors": []
  },
  "validation_summary": {
    "schema_passed": true,
    "hash_passed": true,
    "canonical_record_checked": true
  },
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "human_review_required": true,
  "warnings": [
    "Local MVP lookup only; schema/hash validation signals are advisory and do not provide truth verification, QR authenticity, or signed payload verification."
  ],
  "errors": [],
  "checked_paths": [
    "records/pending/*.json",
    "records/verified/*.json",
    "records/archived/*.json"
  ]
}
```

Depending on the local Python environment, `schema_validation.status` may be `not_checked` instead of `pass` if the existing schema helper dependency is unavailable. That still preserves the same advisory-only contract.

## Example: Unknown `record_id`

```bash
python scripts/run_public_validator_lookup.py HC-NOT-FOUND-2026-0001
```

```json
{
  "record_id": "HC-NOT-FOUND-2026-0001",
  "status": "not_found",
  "found": false,
  "source_path": null,
  "schema_validation": {"status": "not_checked", "errors": []},
  "hash_validation": {"status": "not_checked", "errors": []},
  "validation_summary": {
    "schema_passed": false,
    "hash_passed": false,
    "canonical_record_checked": false
  },
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "human_review_required": true,
  "warnings": [
    "No matching record_id was found in allowed canonical record directories; demo fixtures and generated artifacts were not checked."
  ],
  "errors": [],
  "checked_paths": [
    "records/pending/*.json",
    "records/verified/*.json",
    "records/archived/*.json"
  ]
}
```

`not_found` means no matching local record was found in the allowed directories. It does not mean the record is false, fraudulent, revoked, legally invalid, or absent from any external system.

## Example: Invalid `record_id`

```bash
python scripts/run_public_validator_lookup.py ../records/pending/example.json
```

```json
{
  "record_id": "../records/pending/example.json",
  "status": "invalid_record_id",
  "found": false,
  "source_path": null,
  "schema_validation": {"status": "not_checked", "errors": []},
  "hash_validation": {"status": "not_checked", "errors": []},
  "validation_summary": {
    "schema_passed": false,
    "hash_passed": false,
    "canonical_record_checked": false
  },
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "human_review_required": true,
  "warnings": [],
  "errors": [
    "Invalid record_id. Provide a non-empty record_id, not a path, URL, or query."
  ],
  "checked_paths": [
    "records/pending/*.json",
    "records/verified/*.json",
    "records/archived/*.json"
  ]
}
```

`invalid_record_id` means the input was rejected before lookup. Paths, URLs, query strings, blank values, and malformed values are not accepted as lookup IDs.

## Duplicate `record_id` Meaning

If the same `record_id` appears in more than one allowed local record file, the result status is `duplicate_record_id`.

That means the local checkout has an ambiguous public lookup boundary and the command refuses to choose one record. It does not prove fraud, issuer misconduct, malicious duplication, or a final governance decision. A human reviewer should inspect the listed paths, reconcile the record boundary, and use repository governance before relying on the result.

For duplicate results:

- `found` remains `false`;
- `source_path` remains `null`;
- `schema_validation` and `hash_validation` remain `not_checked`;
- `validation_summary.canonical_record_checked` remains `false`;
- `warnings` lists the matching local paths;
- `errors` explains that duplicate matches were found.

## Schema/Hash Fail Meaning

Schema and hash failures are advisory validation signals, not truth findings.

- `schema_validation.status: "fail"` means the matched local JSON record did not satisfy the currently reused local schema helper.
- `hash_validation.status: "fail"` means the matched local record's `content_hash` / SHA-256 check did not match the current reusable local hash helper.
- `status: "not_checked"` means the signal was not run or could not be safely produced in the current environment.

A schema/hash pass does not prove the underlying claim is true, legally valid, safe, authentic, signed, QR-bound, production-ready, or regulator-approved. A schema/hash fail does not by itself prove falsity, fraud, or legal noncompliance. Both outcomes require human-supervised review.

## Field Guide

| Field | Meaning |
|---|---|
| `record_id` | The exact requested lookup identifier returned for traceability. |
| `status` | Lookup outcome: `found`, `not_found`, `duplicate_record_id`, `invalid_record_id`, or `lookup_error`. |
| `found` | `true` only when exactly one matching allowed local record is found. |
| `source_path` | Relative path to the matched local record when `found` is `true`; otherwise `null`. |
| `schema_validation` | Advisory schema signal with `status` and `errors`; may be `pass`, `fail`, or `not_checked`. |
| `hash_validation` | Advisory `content_hash` / SHA-256 signal with `status` and `errors`; may be `pass`, `fail`, or `not_checked`. |
| `validation_summary` | Boolean summary of whether schema passed, hash passed, and a single local canonical record was checked. |
| `advisory_only` | Always `true`; output supports review but is not final authority. |
| `public_safe` | Always `true`; result shape avoids exposing private evidence beyond public-safe lookup metadata. |
| `truth_guarantee` | Always `false`; the lookup does not verify objective truth. |
| `human_review_required` | Always `true`; reviewer judgment remains required for every result. |
| `warnings` | Public-safe caution messages, duplicate paths, or advisory limitations. |
| `errors` | Public-safe error messages for invalid input, duplicate matches, lookup errors, or validation failures. |
| `checked_paths` | The deterministic local glob boundaries searched by the command. |

## Review Checklist

Before relying on output, confirm:

1. The command was run from the intended repository checkout.
2. The `checked_paths` list is limited to `records/pending/*.json`, `records/verified/*.json`, and `records/archived/*.json`.
3. `advisory_only` is `true`, `public_safe` is `true`, `truth_guarantee` is `false`, and `human_review_required` is `true`.
4. Any `warnings` or `errors` are reviewed by a human.
5. No result is treated as production API output, truth verification, QR authenticity proof, signed payload verification, or legal/regulatory/safety certification.
