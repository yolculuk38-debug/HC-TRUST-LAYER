# Public Validator Local Record Lookup Boundary

> **Status:** local lookup MVP boundary and #656 result-contract notes
> **Scope:** local-only HC:// Public Validator record lookup
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed
> **Current validation step:** #656 Local Public Validator result contract hardening

## Purpose

This document defines the trust boundary between the fixture-backed Public Validator Record ID demo and the local Public Validator MVP that reads canonical JSON records from allowed `records/` directories and reports advisory schema/hash validation signals.

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
- advisory schema validation against a loaded canonical record;
- advisory content hash or SHA-256 validation against a loaded canonical record;
- QR authenticity proof;
- signature verification;
- production verification;
- truth verification.

Fixture matching is a demo convenience only. A matching demo `record_id` means only that the static viewer can select a bundled demo scenario.

## Local MVP Boundary

PR #654 introduced real local lookup while remaining local-only and advisory. PR #655 added advisory schema/hash validation signals for a matched canonical record without changing the lookup allowlist or claiming truth verification. PR #656 locks the local Public Validator result contract so public-safe response semantics cannot silently drift.

The current MVP flow is:

1. A user enters a `record_id`.
2. The system searches only the allowed canonical record directories.
3. The system loads matching JSON records from allowed paths.
4. The system rejects duplicate matching `record_id` values.
5. When exactly one matching canonical record is found, the system reports advisory `schema_validation`, `hash_validation`, and `validation_summary` signals when existing local helpers can be safely reused.
6. The system returns a deterministic, public-safe, advisory-only result.

Schema validation and `content_hash` / SHA-256 validation signals do not establish a truth guarantee. The local MVP must not be described as a production API, live federation service, legal authority, fraud finding, safety certification, forensic determination, QR authenticity proof, signed payload verification, signing authority, or truth guarantee.

## Allowed Canonical Record Paths

Local lookup must be restricted to these canonical record directories:

- `records/pending/*.json`
- `records/verified/*.json`
- `records/archived/*.json`

The lookup boundary must reject arbitrary paths and must not traverse outside these directories.

## Explicitly Excluded Sources

The local MVP must not use these sources for canonical lookup:

- generated indexes;
- explorer indexes;
- manifests;
- cache artifacts;
- export artifacts;
- demo fixtures;
- static viewer bundled data.

These materials may support navigation, demos, review, or derived packaging, but they must not be treated as the canonical lookup source for a user-entered `record_id`.

## Required Safety Markers

A local lookup result must preserve explicit safety markers in its public-safe result shape:

```json
{
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "human_review_required": true,
  "warnings": []
}
```

The stable result contract includes the following top-level fields for every lookup result: `record_id`, `status`, `found`, `source_path`, `advisory_only`, `public_safe`, `truth_guarantee`, `human_review_required`, `warnings`, `errors`, `checked_paths`, `schema_validation`, `hash_validation`, and `validation_summary`. Schema/hash validation fields must not weaken the safety markers above.

`warnings` and `errors` are always lists. `checked_paths` is deterministic and limited to `records/pending/*.json`, `records/verified/*.json`, and `records/archived/*.json`. `source_path` remains `null` unless exactly one allowed canonical record is found.

`schema_validation` and `hash_validation` each expose only `status` and `errors`; validation status values are limited to `pass`, `fail`, and `not_checked`. `validation_summary` exposes `schema_passed`, `hash_passed`, and `canonical_record_checked`. `canonical_record_checked` is true only when exactly one canonical record was found and validation signals were attempted.

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

## Security Notes for the Local MVP

The local lookup implementation preserves these constraints:

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

Unknown `record_id` values produce an explicit public-safe `not_found` result rather than silently selecting a demo scenario.

## Non-Goals for This MVP

This MVP does not implement backend/API serving, QR authenticity proof, signed payload verification, or truth verification. Schema/hash checks are advisory validation signals only and remain subject to human-supervised review.

It does not modify:

- schemas;
- validators;
- workflows;
- static viewer behavior;
- demo fixture behavior;
- canonical records;
- signing logic;
- federation logic;
- API behavior;
- backend behavior;
- QR cryptography.

## #655 Validation Signal Boundary

PR **#655 Local Public Validator schema/hash validation integration** remains local-only, preserves deterministic public-safe output, and reports schema/hash validation as advisory signals requiring human review. A schema pass or hash pass means only that the local canonical record shape or `content_hash` check passed through existing reusable local helpers; it is not truth verification, production readiness, QR authenticity proof, issuer authority proof, signature verification, or autonomous governance approval.

## #656 Result Contract Boundary

PR **#656 Local Public Validator result contract hardening** locks the local Public Validator output shape for every lookup status: `found`, `not_found`, `duplicate_record_id`, `invalid_record_id`, and `lookup_error`. Unknown, invalid, duplicate, and lookup-error results still include advisory schema/hash validation fields with public-safe defaults.

The result contract is public-safe and advisory-only. Validation pass values do not establish a truth guarantee, production readiness, QR authenticity proof, signed payload verification, legal authority, or autonomous governance approval. Human review remains required for all result types.

Recommended next PR: **#657 Local Public Validator CLI quickstart and examples**.
