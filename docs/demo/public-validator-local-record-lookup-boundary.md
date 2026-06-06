# Public Validator Local Record Lookup Boundary

> **Status:** boundary specification for the next Public Validator phase
> **Scope:** local-only HC:// Public Validator record lookup planning
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed
> **Recommended next PR:** #654 Local Public Validator record lookup MVP

## Purpose

This document defines the trust boundary between the current fixture-backed Public Validator Record ID demo and a future local Public Validator MVP that may read canonical JSON records from `records/`.

The boundary exists to prevent the demo Record ID input from being mistaken for real canonical record lookup, a production API, a backend service, truth verification, QR authenticity proof, signature verification, or autonomous governance output.

## Current State: Fixture-Backed Demo

The current Public Validator demo is static and fixture-backed.

It currently provides:

- bundled static demo data;
- bundled result examples and scenario fixtures;
- demo `record_id` mapping from supported fixture IDs to static scenarios;
- static viewer interaction for scenario selection, QR/link entry examples, query-string selection, and Record ID fixture matching;
- a local runner that prints deterministic fixture output.

It does not provide:

- canonical lookup from `records/`;
- backend processing;
- API access;
- database queries;
- live scanning of `records/`;
- schema validation against a loaded canonical record;
- content hash or SHA-256 validation against a loaded canonical record;
- QR authenticity proof;
- signature verification;
- production verification;
- truth verification.

Fixture matching is a demo convenience only. A matching demo `record_id` means only that the static viewer can select a bundled demo scenario.

## Future Local MVP Boundary

A future local Public Validator MVP may introduce real local lookup while remaining local-only and advisory.

The expected flow is:

1. A user enters a `record_id`.
2. The system searches only the allowed canonical record directories.
3. The system loads the matching JSON record from an allowed path.
4. The system performs schema validation for the loaded record.
5. The system performs `content_hash` / SHA-256 validation for the loaded record where the record shape supports that check.
6. The system returns a deterministic, public-safe, advisory-only result.

This future MVP must not be described as a production API, live federation service, legal authority, fraud finding, safety certification, forensic determination, QR authenticity proof, signing authority, or truth guarantee.

## Allowed Canonical Record Paths

Local lookup must be restricted to these canonical record directories:

- `records/pending/*.json`
- `records/verified/*.json`
- `records/archived/*.json`

The lookup boundary must reject arbitrary paths and must not traverse outside these directories.

## Explicitly Excluded Sources

The future local MVP must not use these sources for canonical lookup:

- generated indexes;
- explorer indexes;
- manifests;
- cache artifacts;
- export artifacts;
- demo fixtures;
- static viewer bundled data.

These materials may support navigation, demos, review, or derived packaging, but they must not be treated as the canonical lookup source for a user-entered `record_id`.

## Required Future Safety Markers

A future local lookup result must preserve explicit safety markers in its public-safe result shape:

```json
{
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "human_review_required": true,
  "warnings": []
}
```

Additional fields may describe lookup status, schema validation status, hash validation status, public-safe evidence summaries, and errors. Those fields must not weaken the safety markers above.

## Boundary Statements

- Fixture matching is not real record lookup.
- Local record lookup is not a production API.
- Local record lookup is not a backend service.
- Schema validation is not a truth guarantee.
- `content_hash` / SHA-256 validation is not a truth guarantee.
- A matching `record_id` is not issuer authority proof.
- QR/link entry is not QR authenticity proof.
- Public-safe output is not a legal, regulatory, safety, forensic, or certification determination.
- Human-supervised review remains required.

## Security Notes for the Future MVP

The local lookup implementation should preserve these constraints:

- use safe path handling;
- disallow arbitrary file reads;
- search only allowed canonical record paths;
- perform no network calls;
- perform no external URL fetching;
- avoid hidden fallback to fixtures when local lookup fails;
- return a clear error for an unknown `record_id`;
- return a clear error for duplicate matching records if duplicates are found;
- return a deterministic result shape for success and failure;
- preserve public-safe output boundaries;
- avoid exposing private, sensitive, or non-public evidence beyond the public-safe result shape.

Unknown `record_id` values should produce an explicit public-safe error such as `record_not_found` rather than silently selecting a demo scenario.

## Non-Goals for This PR

This PR does not implement local lookup.

It does not modify:

- schemas;
- validators;
- workflows;
- runtime code;
- static viewer behavior;
- demo fixture behavior;
- canonical records;
- signing logic;
- federation logic;
- API behavior;
- backend behavior;
- QR cryptography.

## Recommended Next PR

The recommended next PR is **#654 Local Public Validator record lookup MVP**.

That PR should remain local-only, use the allowed canonical record paths above, preserve deterministic public-safe output, and report schema/hash validation as advisory signals requiring human review.
