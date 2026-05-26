# Public Verification Boundaries

This document defines public HC:// verification boundaries for the first public flow in HC-TRUST-LAYER.

## What public verification verifies

Public verification in `docs/verify.html` verifies continuity signals for the first flow:

- input `record` and `hash` alignment with the expected first public flow values
- canonical record availability at `examples/demo_record.json`
- canonical record byte-integrity match against the expected SHA-256 hash
- explorer continuity reference presence in `generated/first_working_explorer_index.json`
- audit continuity reference presence in `generated/first_working_audit_snapshot.json`
- QR route consistency for the `docs/verify.html` verification route

These checks are lightweight continuity diagnostics for operator and reviewer visibility.

## What public verification does not verify

Public verification does not provide:

- objective truth guarantees
- intent, authorship, or motive certainty
- production-readiness guarantees
- autonomous governance finality
- forensic certainty claims

Public verification is an integrity and continuity surface, not a truth adjudication surface.

## Integrity vs truth

Integrity means that referenced bytes and continuity links match expected values under the documented workflow.

Truth is a broader human and institutional determination. Integrity evidence can support review, but it cannot independently prove truth.

## Generated artifact limitations

Generated artifacts are non-canonical and advisory in HC-TRUST-LAYER:

- `generated/first_working_explorer_index.json`
- `generated/first_working_audit_snapshot.json`
- other generated indexes, snapshots, exports, and cache outputs

Generated artifacts can fail, be missing, or drift from expected continuity references. They support diagnostics and audit visibility, but they do not replace canonical record surfaces.

## Advisory-only verification boundaries

The first public HC:// verification flow remains advisory-only.

Human-supervised validation remains required before consequential decisions. Public verification diagnostics should be treated as review inputs and continuity indicators, not final authority.

See `docs/qr-verification-security-model.md` for permission-aware HC:// QR entry constraints, spoofing risks, and advisory trust-boundary handling.


For future federation interoperability boundaries and advisory verification package semantics, see `docs/federation-readiness-model.md`.

For safe visible verification signals and advisory verification badge language, see `docs/verification-signal-model.md`.

For anti-spoof verification signal rendering boundaries and non-authoritative UX guidance, see `docs/anti-spoof-verification-signals.md`.
