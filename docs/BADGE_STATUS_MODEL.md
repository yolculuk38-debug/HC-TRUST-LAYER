# Public Verification Badge Status Model

## Purpose

This document defines the HC-TRUST-LAYER public badge/status model for verified content records.

The model is designed for **integrity-first verification** across public interfaces, APIs, and embedded verification views.

## Scope

HC-TRUST-LAYER public badges communicate whether a content record can be technically validated against trusted verification signals.

They do **not** represent social influence, popularity, or reputation alone.

## Not a Social "Blue Check"

HC-TRUST-LAYER verification badges are different from social-media “blue check” patterns.

- HC-TRUST-LAYER verifies **content and record integrity**.
- It checks cryptographic consistency, record continuity, and witness-backed verification signals.
- It does not grant authority because of follower counts, visibility, or brand status.
- Identity context can be one input, but identity alone is not sufficient for a VERIFIED status.

## Status Definitions

### VERIFIED

Use when the original record exists, the content hash matches, and signature/witness checks pass.

### SUSPICIOUS

Use when the record exists, but risk signals are present or a partial mismatch exists.

Examples include unresolved risk flags, inconsistent provenance metadata, or non-blocking witness disagreement requiring review.

### UNVERIFIED

Use when no trusted record is found for the submitted content or reference.

### REVOKED

Use when a previously verifiable record was withdrawn or superseded through the revision chain.

Consumers should follow the revision chain to the active replacement record.

### EXPIRED

Use when the verification package is stale and requires refresh under current policy windows.

The underlying content may be unchanged, but its verification package must be renewed.

## Public Badge Fields

The following fields define the public badge payload:

- `record_id`
- `content_hash`
- `verification_status`
- `trust_score`
- `witness_count`
- `verified_at`
- `verification_url`
- `revision_id`

## JSON Example

```json
{
  "record_id": "HC-NEWS-2026-0184",
  "content_hash": "b4c37b3e0d2f3c5dfd7d7b20510f4a31c5839f4f6a8a89f7b741de8293d5e6ac",
  "verification_status": "VERIFIED",
  "trust_score": 92,
  "witness_count": 5,
  "verified_at": "2026-05-23T12:40:00Z",
  "verification_url": "https://example.org/verify/HC-NEWS-2026-0184",
  "revision_id": "rev-03"
}
```

## Implementation Notes

- Status values are intended for public-facing UX labels, API responses, and badge rendering layers.
- `verification_status` should be treated as the canonical state machine output for badge color/icon mapping.
- `trust_score` is complementary context and must not override a non-VERIFIED status.
- Revision-aware clients should prioritize `REVOKED` handling by resolving the latest active revision target.

## Brand Consistency

HC-TRUST-LAYER presents a transparent, auditable verification layer.

Public badge status should consistently communicate:

- integrity over popularity
- traceability over assumptions
- reproducible verification over unsupported claims
