# FIRST_WORKING_RECORD

This document defines the first fully linked, reproducible HC:// verification example in HC-TRUST-LAYER.

## End-to-end verification flow

- **Canonical demo record path:** `examples/demo_record.json`
- **Record ID:** `HC-DEMO2026-0001`
- **Full SHA-256 hash:** `ae83383b191d02970eb3df834c56b15e7a688fcd63f782d3408aaefd60b7b56a`
- **QR verification URL:** `https://<owner>.github.io/HC-TRUST-LAYER/docs/verify.html?record=HC-DEMO2026-0001&hash=ae83383b191d02970eb3df834c56b15e7a688fcd63f782d3408aaefd60b7b56a`
- **Explorer index reference (non-canonical):** `generated/first_working_explorer_index.json`
- **Audit snapshot reference (non-canonical):** `generated/first_working_audit_snapshot.json`

## Reproducible verification commands

Run these commands from repository root:

```bash
sha256sum examples/demo_record.json
python3 -m json.tool generated/first_working_explorer_index.json >/dev/null
python3 -m json.tool generated/first_working_audit_snapshot.json >/dev/null
```

Expected command outputs:

```text
ae83383b191d02970eb3df834c56b15e7a688fcd63f782d3408aaefd60b7b56a  examples/demo_record.json
```

- The `sha256sum` output must match the full SHA-256 hash in this document, in `docs/verify.html`, and in the non-canonical explorer/audit references listed above.
- The `python3 -m json.tool` commands return no text output and exit successfully when generated artifacts are valid JSON.

## Verification continuity

1. Canonical record continuity:
   - `examples/demo_record.json` is the canonical source path for this first working flow.
2. QR route continuity:
   - `docs/verify.html?record=HC-DEMO2026-0001&hash=ae83383b191d02970eb3df834c56b15e7a688fcd63f782d3408aaefd60b7b56a`
3. Verification page continuity:
   - `docs/verify.html` compares input parameters against expected canonical `record` and full SHA-256 `hash`.
4. Explorer continuity:
   - `generated/first_working_explorer_index.json` contains `HC-DEMO2026-0001` with the same `record_hash`.
5. Audit continuity:
   - `generated/first_working_audit_snapshot.json` contains `HC-DEMO2026-0001` with the same `record_hash`.

If continuity warnings appear on `docs/verify.html`, treat them as advisory continuity diagnostics (missing generated artifact, missing canonical record, hash mismatch, or broken continuity reference) and continue with human-supervised validation.

## Integrity boundary explanation

- Canonical boundary:
  - `examples/demo_record.json` is treated as canonical reference content for this first public verification example.
- Generated boundary:
  - `generated/first_working_explorer_index.json` and `generated/first_working_audit_snapshot.json` are generated non-canonical artifacts used for lookup and audit visibility only.
- Verification boundary:
  - `docs/verify.html` provides a static, local-only advisory continuity view and does not replace repository validators or reviewer decisions.

## Advisory verification boundary

Integrity verification proves that bytes match the expected hash under the selected workflow. Integrity verification does **not** prove objective truth.

HC:// verification in this flow remains advisory-only and requires human-supervised validation before consequential decisions.

See `docs/public-verification-boundaries.md` for public verification boundary definitions and integrity-versus-truth framing.
