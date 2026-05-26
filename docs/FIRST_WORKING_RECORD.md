# FIRST_WORKING_RECORD

This document defines the first fully linked, reproducible HC:// verification example in HC-TRUST-LAYER.

## End-to-end verification flow

- **Canonical demo record path:** `examples/demo_record.json`
- **Record ID:** `HC-DEMO2026-0001`
- **Full SHA-256 hash:** `ae83383b191d02970eb3df834c56b15e7a688fcd63f782d3408aaefd60b7b56a`
- **QR verification URL:** `https://<owner>.github.io/HC-TRUST-LAYER/docs/verify.html?record=HC-DEMO2026-0001&hash=ae83383b191d02970eb3df834c56b15e7a688fcd63f782d3408aaefd60b7b56a`
- **Explorer index reference (non-canonical):** `generated/first_working_explorer_index.json`
- **Audit snapshot reference (non-canonical):** `generated/first_working_audit_snapshot.json`

## Verification command

Run this command from repository root:

```bash
sha256sum examples/demo_record.json
```

Expected verification result:

```text
ae83383b191d02970eb3df834c56b15e7a688fcd63f782d3408aaefd60b7b56a  examples/demo_record.json
```

The hash output must match the hash in this document, in `docs/verify.html`, and in the non-canonical explorer/audit references listed above.

## Verification continuity

- The explorer index reference contains `HC-DEMO2026-0001` with the same `record_hash`.
- The audit snapshot reference contains `HC-DEMO2026-0001` with the same `record_hash`.
- The verification command reproduces the same SHA-256 result for `examples/demo_record.json`.

## Advisory verification boundary

Integrity verification proves that bytes match the expected hash under the selected workflow. Integrity verification does **not** prove objective truth.

HC:// verification in this flow remains advisory-only and requires human-supervised validation before consequential decisions.
