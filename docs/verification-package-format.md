# HC-TRUST-LAYER Verification Package Format

## Status

- planned format / specification draft
- not yet a full production export system
- intended for future public verification API, federation, and external integrations

## Purpose

This document defines the **verification package** format for HC-TRUST-LAYER.

A verification package is a **portable, derived, non-canonical** structure used for external integrity verification and public verification workflows. It is intended to support export/import verification, federation exchange, and external trust integrations using HC:// reference contexts.

## Canonical Boundary

Verification packages are **derived artifacts**.

Verification packages are **not canonical records**.

Canonical records remain under:

- `records/pending/`
- `records/verified/`
- `records/archived/`

A verification package may reference canonical records, but it must never replace canonical record authority.

## Example Artifact Placement Note

The file `examples/verification-package-example.json` is an **illustrative** verification package.

- It is a **derived artifact** for documentation and integrity verification testing.
- It is **non-canonical** and must not be treated as a canonical record.
- It must **not** be placed under `records/`.
- Canonical record authority remains exclusively within canonical record paths.

## Definition

A **verification package** is a portable, derived artifact containing enough data to verify:

- record integrity
- provenance context
- witness context
- audit trail references
- source repository metadata

This package exists to move verification context across systems while preserving canonical record boundaries.

## Required Fields

A format-conforming package must include the following fields:

- `package_version`
- `package_id`
- `record_id`
- `record_hash`
- `content_hash`
- `verification_state`
- `canonical_record_path`
- `source_repository`
- `source_commit`
- `generated_at`
- `provenance`
- `audit`
- `witnesses`
- `signatures`
- `verification_policy`
- `warnings`

## Optional Fields

The following fields are optional and may be omitted when unavailable:

- `qr_reference`
- `explorer_url`
- `public_verify_url`
- `federation_source`
- `export_context`
- `dispute_status`
- `revocation_status`

## Illustrative JSON Example (Non-Canonical)

The example below is illustrative only.

- It is not a canonical record.
- It is not placed under `records/`.
- It does not supersede canonical record data.

```json
{
  "package_version": "0.1-draft",
  "package_id": "HCPKG-2026-05-24-0001",
  "record_id": "HC-EXAMPLE-2026-0001",
  "record_hash": "sha256:ab12...",
  "content_hash": "sha256:cd34...",
  "verification_state": "verified",
  "canonical_record_path": "records/verified/HC-EXAMPLE-2026-0001.json",
  "source_repository": "https://github.com/example/HC-TRUST-LAYER",
  "source_commit": "2f4c1e9",
  "generated_at": "2026-05-24T00:00:00Z",
  "provenance": {
    "origin": "HC://records/verified/HC-EXAMPLE-2026-0001.json",
    "created_by": "verification-export",
    "chain": [
      "HC://provenance/events/evt-001"
    ]
  },
  "audit": {
    "audit_refs": [
      "HC://audit/entries/a-1001"
    ],
    "audit_trail_hash": "sha256:ef56..."
  },
  "witnesses": [
    {
      "witness_id": "WIT-001",
      "witness_context": "human-review",
      "attested_at": "2026-05-24T00:00:00Z"
    }
  ],
  "signatures": [
    {
      "type": "ed25519",
      "key_id": "key-01",
      "signature": "base64:..."
    }
  ],
  "verification_policy": {
    "policy_id": "policy-baseline-v1",
    "integrity_rules": [
      "content_hash_match",
      "canonical_path_exists"
    ]
  },
  "warnings": [
    "source_commit_not_locally_present"
  ],
  "qr_reference": "HC://qr/HC-EXAMPLE-2026-0001",
  "explorer_url": "https://example.org/explorer/HC-EXAMPLE-2026-0001",
  "public_verify_url": "https://example.org/verify/HC-EXAMPLE-2026-0001",
  "federation_source": "node-east-1",
  "export_context": {
    "exported_by": "cli",
    "reason": "external_audit_request"
  },
  "dispute_status": "none",
  "revocation_status": "active"
}
```

## Schema Draft

Machine-readable schema draft:

- `schema/verification-package-v1.schema.json`

## Scope Note

This schema validates verification package structure only.

- It does not make verification packages canonical records.
- It does not verify truth.
- It does not replace canonical record validation.

## Verification Rules

A verifier should:

1. check package format version
2. locate canonical record path
3. verify `content_hash`
4. verify `record_hash` if available
5. compare `source_commit` if available
6. inspect audit references
7. inspect witness context
8. inspect warnings
9. never treat package data as more authoritative than the canonical record

## Security Notes

- verification packages may be copied or tampered with
- packages must be verified against canonical source or trusted mirror
- signatures are planned unless already implemented in active workflow
- source repository availability matters for reproducibility
- packages must not imply truth guarantees

## Future Direction

This specification is designed as a foundational format for:

- public verification exchange
- federation transport
- external integration interoperability

It does not introduce exporter code, schema enforcement, validator modifications, or new product features in this phase.
