# QR Payload Verification Boundary

> **Status:** documentation/spec boundary with local parser and CLI runner
> **Scope:** HC:// Public Validator QR payload parsing posture
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed

## Purpose

This document defines the trust boundary for HC:// QR payload parsing, the local QR record bridge, and future QR payload verification. The current implementation includes a local-only parser, a local-only parser CLI runner, and a local-only QR record bridge CLI runner, but it does not add QR cryptography, signing, backend/API behavior, validator changes, schema changes, network calls, or URL fetches.

The current Public Validator work can perform local Public Validator lookup and advisory schema/hash checks against local records. The existing QR/link demo can route a reviewer into the static demo experience. The QR payload parser can check JSON payload shape locally. The QR record bridge can compare a parser-valid payload `content_hash` with exactly one matched local canonical record `content_hash`. Those capabilities are useful for review, but they do not establish real QR authenticity or record truth.

## Current Boundary

The current demo QR/link flow is not real QR verification.

A demo QR code or ordinary link is only a navigation entry point into a public-safe demo surface. It does not prove that:

- the QR label is authentic;
- the QR payload came from an authorized issuer;
- the URL is canonical;
- the payload is signed;
- the referenced record is valid;
- the real-world claim is true;
- the result is production-ready, legally authoritative, regulatory-approved, safety-certified, or forensically certain.

The current local QR payload parser is separate from QR authenticity and record trust. It checks payload shape and one local advisory `payload_hash` consistency signal, returns advisory public-safe markers, does not verify signatures, does not fetch `canonical_url`, and does not prove that a QR code came from an authorized issuer.

The current local lookup flow is separate from QR payload trust. A successful `record_id` lookup only means a local repository checkout found exactly one matching record within the allowed local record directories. It does not prove that a scanned QR payload is trustworthy.

The local QR record bridge adds one advisory connection between these layers: after the QR payload parser accepts a local payload, the bridge can reuse the local Public Validator lookup path for the parsed `record_id` and compare the QR payload `content_hash` with the matched local canonical record `content_hash`. This bridge checks only the existing allowed canonical record paths: `records/pending/*.json`, `records/verified/*.json`, and `records/archived/*.json`. It does not fetch `canonical_url`, call a network, use a backend/API, verify signatures, prove QR authenticity, prove issuer authority, or prove truth. Demo fixtures remain documentation examples only and are not treated as canonical records.

The current schema/hash checks are also separate from truth. A schema/hash pass or bridge `content_hash` match can show local advisory consistency with the inspected checkout, but it is not a truth guarantee, QR authenticity proof, issuer approval, legal finding, safety certification, or production trust decision.


## Local Parser CLI Runner

Reviewers can run the local parser from the command line with one JSON string argument:

```bash
python scripts/run_qr_payload_parser.py '{"qr_version":"1","record_id":"HC-EXAMPLE-2026-0001","canonical_url":"https://example.invalid/record/HC-EXAMPLE-2026-0001","payload_hash":"771d6e804359164526070f3806d2f82cd53bf71f49e6fa843f067e7f848d3271","content_hash":"def","issued_at":"2026-01-01T00:00:00Z","issuer_id":"demo","algorithm":"none","key_id":"demo-key"}'
```

The CLI output is deterministic JSON from `parse_qr_payload`. It is local-only and emits no extra prose on stdout.

The CLI parser:

- checks QR payload JSON shape;
- computes a local advisory `payload_hash` consistency check when `payload_hash` is present;
- does not prove QR authenticity;
- does not verify signatures;
- does not fetch `canonical_url`;
- does not call a network, backend, or API;
- does not verify truth, issuer authority, safety, legality, or production readiness;
- keeps human review required.

## Local QR Record Bridge

`check_qr_payload_record_bridge` is a local advisory helper for reviewer and test workflows. It accepts a raw QR payload JSON string or parsed payload object, runs the local QR payload parser, and only proceeds to local record lookup when the payload is parser-valid. Malformed payloads, invalid payloads, missing `record_id`, and invalid `record_id` values return public-safe advisory results without record lookup.

Reviewers can run the bridge from the command line with one JSON string argument:

```bash
python scripts/run_qr_record_bridge.py '{"qr_version":"1","record_id":"HC-EXAMPLE-2026-0001","canonical_url":"https://example.invalid/record/HC-EXAMPLE-2026-0001","payload_hash":"771d6e804359164526070f3806d2f82cd53bf71f49e6fa843f067e7f848d3271","content_hash":"def","issued_at":"2026-01-01T00:00:00Z","issuer_id":"demo","algorithm":"none","key_id":"demo-key"}'
```

The CLI output is deterministic JSON from `check_qr_payload_record_bridge` with sorted keys and no extra prose on stdout. It is local-only: it does not call a network, fetch `canonical_url`, use a backend/API, verify signatures, or widen the existing local lookup boundary.

When lookup proceeds, the bridge reuses the existing local Public Validator lookup boundary and reports one of these advisory bridge outcomes: `bridge_match`, `bridge_mismatch`, `record_not_found`, `duplicate_record_id`, `invalid_payload`, `malformed_payload`, or `bridge_not_checked`. If exactly one allowed local canonical record is found, the bridge compares the QR payload `content_hash` with the local record `content_hash` after normalizing surrounding whitespace and hexadecimal case.

A bridge `content_hash` match does not prove QR authenticity, does not prove truth, does not prove issuer authority, does not verify signatures, does not validate `canonical_url` ownership, and does not replace human review. A bridge mismatch is a local advisory integrity warning for reviewers, not a final legal, regulatory, safety, forensic, or production decision. The bridge result preserves `advisory_only: true`, `public_safe: true`, `truth_guarantee: false`, and `human_review_required: true` for every outcome.

## Parser Result Contract

Every parser result must remain public-safe and use the same stable top-level field set:

- `status`;
- `warnings`;
- `errors`;
- `advisory_only`;
- `public_safe`;
- `truth_guarantee`;
- `human_review_required`.

Allowed `status` values are `valid_payload`, `invalid_payload`, and `malformed_payload`. `warnings` and `errors` must always be lists. Unknown payload fields should produce public-safe warnings instead of crashing or triggering network lookup. Missing required fields should produce `invalid_payload`, a mismatched `payload_hash` should produce `invalid_payload` as a safer local integrity-failure signal, and malformed JSON should produce `malformed_payload`.

The current parser includes an advisory MVP `payload_hash` canonicalization rule for local parser consistency only. It parses the payload as a JSON object, removes the `payload_hash` field before hashing, serializes the remaining object with sorted keys and compact separators, UTF-8 encodes that JSON, computes the SHA-256 hex digest, and compares it with `payload_hash` after normalizing hexadecimal case and surrounding whitespace. This rule is not a final signing canonicalization standard, does not verify signatures, does not fetch `canonical_url`, and does not prove QR authenticity or record truth.

The safety markers are fixed for this parser contract: `advisory_only` is `true`, `public_safe` is `true`, `truth_guarantee` is `false`, and `human_review_required` is `true`. A `valid_payload` result means only that local parser shape checks and any present advisory `payload_hash` consistency check passed. It must not imply QR authenticity, signature verification, truth verification, URL fetching, issuer approval, legal authority, safety certification, or production readiness.

## Reviewer Fixture Quickstart

Example payload fixtures are available under [`docs/demo/fixtures/qr-payload-parser/`](../demo/fixtures/qr-payload-parser/). They are documentation/demo fixtures only, not canonical records, schemas, validators, signed QR payloads, production QR manifests, runtime lookup material, backend/API responses, or truth-verification evidence.

Run these examples from the repository root:

```bash
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/valid-payload.json)"
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/matching-payload-hash.json)"
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/mismatched-payload-hash.json)"
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/uppercase-payload-hash.json)"
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/missing-field-payload.json)"
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/malformed-payload.txt)"
python scripts/run_qr_payload_parser.py "$(cat docs/demo/fixtures/qr-payload-parser/unknown-field-payload.json)"
```

Status meanings:

| Status | Meaning |
| --- | --- |
| `valid_payload` | Required MVP fields, local field-shape checks, and any present advisory `payload_hash` consistency check passed. This is local advisory parser validation only, not QR authenticity, signature verification, URL fetching, record lookup, record truth verification, or production readiness. |
| `invalid_payload` | The input was valid JSON, but one or more local checks failed, such as missing fields, invalid field types, blank values, malformed `record_id`, malformed `canonical_url`, malformed `issued_at`, or mismatched advisory `payload_hash`. |
| `malformed_payload` | The input could not be parsed as a JSON object. The parser returns public-safe errors and does not attempt fallback lookup, network access, backend/API calls, URL fetching, signature verification, or record truth verification. |

For detailed fixture descriptions and expected behavior, read the fixture quickstart: [`docs/demo/fixtures/qr-payload-parser/README.md`](../demo/fixtures/qr-payload-parser/README.md).

## Separation of Concerns

Future QR verification must keep these boundaries separate:

1. **QR payload trust** — whether the scanned payload is well-formed, canonical, current, issuer-bound, and signed or signature-referenced.
2. **Record lookup** — whether a referenced `record_id` resolves to exactly one permitted canonical record in the selected lookup boundary.
3. **Record validity signals** — whether advisory schema/hash checks pass for the canonical record that was actually inspected.
4. **Human review** — whether a reviewer accepts the evidence, warnings, issuer context, and repository governance implications.

Passing one layer must not silently imply that another layer passed.

## QR Payload Fields

The local parser checks a minimal MVP field shape for reviewer testing. A future signed QR payload format must define and validate these fields before it is treated as QR payload verification:

| Field | Boundary requirement |
| --- | --- |
| `qr_version` | Version marker for the QR payload contract. |
| `record_id` | HC:// record identifier referenced by the payload. |
| `canonical_url` | Canonical public validation URL intended for the record. |
| `payload_hash` | Advisory parser-local SHA-256 hash of the QR payload content after removing `payload_hash` and applying the MVP JSON canonicalization rule. This is not a signing canonicalization standard. |
| `content_hash` | Hash expected to match the referenced canonical record content. |
| `issued_at` | Payload issuance timestamp. |
| `expires_at` or `validity_window` | Expiry or bounded validity period for staleness checks. |
| `issuer_id` | Issuer identity reference for review and key lookup. |
| `signature_reference` or `signature` | Detached signature reference or embedded signature material. |
| `algorithm` | Declared signing/hash algorithm for future verification. |
| `key_id` | Key identifier used to resolve the issuer verification key. |
| `warnings` | Public-safe warnings carried or produced by the QR payload layer. |

Missing or malformed required fields must produce advisory warnings or errors. They must not fall back to fixture data, hidden defaults, network discovery, or unverified assumptions.

## Required Checks for Future Verification Implementation

The current parser does not present payloads as verified. A future QR payload verifier must perform these checks before presenting a QR payload as verified:

- **Canonical domain check:** confirm `canonical_url` uses an approved HC:// canonical validation domain or route.
- **`record_id` format check:** reject paths, URLs, queries, blank values, and malformed identifiers.
- **`payload_hash` check:** recompute the payload hash using a reviewed final canonicalization rule and compare it with `payload_hash`. The current parser has only an advisory MVP JSON canonicalization rule.
- **`content_hash` match against canonical record:** compare the payload `content_hash` with the inspected canonical record content hash.
- **Expiry/staleness check:** evaluate `issued_at` and `expires_at` or `validity_window` before presenting freshness.
- **Replay warning:** warn when a payload appears stale, reused outside its intended context, or otherwise replay-risky.
- **Signature/key reference check:** verify that `signature_reference` or `signature`, `algorithm`, `issuer_id`, and `key_id` can be resolved and validated under the future trust model.
- **Non-canonical URL warning:** warn when the scanned or displayed URL differs from the canonical route.
- **Missing field warning:** produce explicit warnings for absent required fields.
- **Malformed payload handling:** fail safely with public-safe errors for invalid JSON, unsupported versions, invalid timestamps, unexpected field types, oversize payloads, or ambiguous encodings.

These checks are future work. This document does not implement them.

## Security Boundaries

Current QR payload parser and future QR payload verification work must preserve these boundaries:

- no blind URL trust;
- no external fetch by default;
- no hidden network calls;
- no fixture fallback;
- no truth guarantee;
- no production claim;
- no legal, regulatory, food-safety, building-safety, security, issuer-authority, or compliance certification;
- human review remains required.

A scanned URL must not be treated as trustworthy just because it came from a QR code. The verifier should parse and validate the payload boundary first, avoid automatic remote fetches by default, and make any network-dependent behavior explicit, reviewable, and opt-in in later work.

## Required Safety Markers

Current parser results and future QR payload verification results must preserve these public-safe safety markers unless a later reviewed specification explicitly changes them:

```json
{
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "human_review_required": true
}
```

These markers must be present even when QR payload checks pass. A pass means only that the future QR payload layer satisfied its implemented checks; it does not certify truth, safety, legality, regulatory compliance, or production readiness.

## Non-Goals for This Parser/CLI Scope

This parser/CLI scope does not:

- implement QR crypto;
- implement signing;
- modify validators;
- modify schemas;
- modify workflows;
- add an API or backend;
- add network calls;
- alter existing QR demo behavior;
- prove QR authenticity;
- verify signatures;
- fetch `canonical_url`;
- claim production readiness;
- perform a large refactor.

## Recommended Next PR

Recommended next PR: a dedicated, reviewed follow-up only if reviewers approve broader QR verification work. Any follow-up must remain evidence-preserving, human-reviewable, and explicit about whether it changes parsing, signing, lookup, validator, schema, backend/API, or network behavior.
