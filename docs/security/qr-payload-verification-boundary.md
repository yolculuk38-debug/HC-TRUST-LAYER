# QR Payload Verification Boundary

> **Status:** documentation/spec boundary only
> **Scope:** future HC:// Public Validator QR payload verification posture
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed

## Purpose

This document defines the trust boundary for a future HC:// QR payload verification step before any QR cryptography, signing, parser, backend, API, validator, schema, or runtime behavior is added.

The current Public Validator work can perform local Public Validator lookup and advisory schema/hash checks against local records. The existing QR/link demo can route a reviewer into the static demo experience. Those capabilities are useful for review, but they do not establish real QR authenticity.

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

The current local lookup flow is separate from QR payload trust. A successful `record_id` lookup only means a local repository checkout found exactly one matching record within the allowed local record directories. It does not prove that a scanned QR payload is trustworthy.

The current schema/hash checks are also separate from truth. A schema/hash pass can show that a matched local record conforms to current advisory checks, but it is not a truth guarantee, QR authenticity proof, issuer approval, legal finding, safety certification, or production trust decision.

## Separation of Concerns

Future QR verification must keep these boundaries separate:

1. **QR payload trust** — whether the scanned payload is well-formed, canonical, current, issuer-bound, and signed or signature-referenced.
2. **Record lookup** — whether a referenced `record_id` resolves to exactly one permitted canonical record in the selected lookup boundary.
3. **Record validity signals** — whether advisory schema/hash checks pass for the canonical record that was actually inspected.
4. **Human review** — whether a reviewer accepts the evidence, warnings, issuer context, and repository governance implications.

Passing one layer must not silently imply that another layer passed.

## Required Future QR Payload Fields

A future signed QR payload format must define and validate these fields before it is treated as QR payload verification:

| Field | Boundary requirement |
| --- | --- |
| `qr_version` | Version marker for the QR payload contract. |
| `record_id` | HC:// record identifier referenced by the payload. |
| `canonical_url` | Canonical public validation URL intended for the record. |
| `payload_hash` | Hash of the QR payload content under the future canonicalization rule. |
| `content_hash` | Hash expected to match the referenced canonical record content. |
| `issued_at` | Payload issuance timestamp. |
| `expires_at` or `validity_window` | Expiry or bounded validity period for staleness checks. |
| `issuer_id` | Issuer identity reference for review and key lookup. |
| `signature_reference` or `signature` | Detached signature reference or embedded signature material. |
| `algorithm` | Declared signing/hash algorithm for future verification. |
| `key_id` | Key identifier used to resolve the issuer verification key. |
| `warnings` | Public-safe warnings carried or produced by the QR payload layer. |

Missing or malformed required fields must produce advisory warnings or errors. They must not fall back to fixture data, hidden defaults, network discovery, or unverified assumptions.

## Required Checks for Future Implementation

A future QR payload parser/verifier must perform these checks before presenting a QR payload as verified:

- **Canonical domain check:** confirm `canonical_url` uses an approved HC:// canonical validation domain or route.
- **`record_id` format check:** reject paths, URLs, queries, blank values, and malformed identifiers.
- **`payload_hash` check:** recompute the payload hash using the defined canonicalization rule and compare it with `payload_hash`.
- **`content_hash` match against canonical record:** compare the payload `content_hash` with the inspected canonical record content hash.
- **Expiry/staleness check:** evaluate `issued_at` and `expires_at` or `validity_window` before presenting freshness.
- **Replay warning:** warn when a payload appears stale, reused outside its intended context, or otherwise replay-risky.
- **Signature/key reference check:** verify that `signature_reference` or `signature`, `algorithm`, `issuer_id`, and `key_id` can be resolved and validated under the future trust model.
- **Non-canonical URL warning:** warn when the scanned or displayed URL differs from the canonical route.
- **Missing field warning:** produce explicit warnings for absent required fields.
- **Malformed payload handling:** fail safely with public-safe errors for invalid JSON, unsupported versions, invalid timestamps, unexpected field types, oversize payloads, or ambiguous encodings.

These checks are future work. This document does not implement them.

## Security Boundaries

Future QR payload verification must preserve these boundaries:

- no blind URL trust;
- no external fetch by default;
- no hidden network calls;
- no fixture fallback;
- no truth guarantee;
- no production claim;
- no legal, regulatory, food-safety, building-safety, security, issuer-authority, or compliance certification;
- human review remains required.

A scanned URL must not be treated as trustworthy just because it came from a QR code. The verifier should parse and validate the payload boundary first, avoid automatic remote fetches by default, and make any network-dependent behavior explicit, reviewable, and opt-in in later work.

## Required Safety Markers for Future Results

Future QR payload verification results must preserve these public-safe safety markers unless a later reviewed specification explicitly changes them:

```json
{
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "human_review_required": true
}
```

These markers must be present even when QR payload checks pass. A pass means only that the future QR payload layer satisfied its implemented checks; it does not certify truth, safety, legality, regulatory compliance, or production readiness.

## Non-Goals for This PR

This PR does not:

- implement QR crypto;
- implement signing;
- modify runtime behavior;
- modify validators;
- modify schemas;
- modify workflows;
- add an API or backend;
- add network calls;
- alter existing QR demo behavior;
- claim production readiness;
- perform a large refactor.

## Recommended Next PR

Recommended next PR: **#661 QR payload parser MVP**.

That follow-up should remain local-only and parser-focused unless reviewers explicitly approve a broader scope. It should parse payload shape, produce public-safe warnings for missing or malformed fields, and continue to avoid QR crypto/signing implementation until a dedicated reviewed step.
