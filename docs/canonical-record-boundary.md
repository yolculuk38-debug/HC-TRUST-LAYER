# HC-TRUST-LAYER Canonical Record Boundary

## Status and Purpose

This document defines canonical record boundaries for HC-TRUST-LAYER.

Goal: ensure generated/index/export/cache artifacts are never treated as canonical verification records.

Scope: documentation-only clarification aligned with current validator behavior. No verification logic is introduced or changed.

---

## 1) Canonical Record Locations

Canonical verification records are authoritative records that participate in record validation and verification lifecycle decisions.

Canonical locations:

- `records/pending/`
- `records/verified/`
- `records/archived/` (canonical target name)
- `records/archive/` (legacy/current repository path used by existing tooling)

Boundary rule:

- Files in canonical record locations are treated as verification records when they are record-shaped payloads (for example `record-v1` JSON records).
- Canonical validation decisions must be grounded in canonical records, not in derived artifacts.

---

## 2) Non-Canonical / Generated Locations and Artifacts

The following are non-canonical generated artifacts and must not be interpreted as immutable verification records:

- indexes
- explorer artifacts
- generated manifests
- exports
- cache files
- derived/search artifacts

Examples include:

- `records/explorer_index.json` (generated explorer index; non-canonical)
- `explorer/index/*.json` lookup outputs
- generated `manifest.json` files describing index/export batches
- `exports/` verification package outputs
- cache snapshots and temporary derived JSON artifacts

Boundary rule:

- Generated artifacts may support lookup, transport, caching, UX, or federation workflows.
- Generated artifacts do not define canonical verification truth.
- Generated artifacts must never be described as immutable canonical records.

---

## 3) Validator Expectations (Current Behavior)

Validator boundary expectations:

1. Canonical validation targets canonical records.
2. Generated artifacts must be skipped by canonical record validation.
3. Artifact/schema validation for generated outputs may exist separately, but it is not canonical record validation.

Current validator behavior alignment:

- `src/validator.py` skips files whose **filename** contains artifact hints:
  - `index`
  - `manifest`
  - `cache`
  - `export`
  - `generated`
- Skipped files return `SKIPPED ARTIFACT` and are not treated as canonical record failures.

Operational implication:

- Any file intentionally treated as non-canonical should keep naming and placement consistent with generated-artifact conventions to avoid accidental canonical handling in tooling.

---

## 4) Required Fields and Verification Context by File Class

### 4.1 Canonical record files

Canonical records (for example in `records/pending/`, `records/verified/`, `records/archived/` (or legacy `records/archive/`)) are expected to conform to active record schema requirements.

Canonical record fields required by current `record-v1` schema include:

- `content_hash` (required)
- `verification_status` (required)

Witness metadata expectations:

- witness-related metadata (for example `witnesses`) is optional extension context in current schema,
- but when present it should remain stable and traceable for audit workflows.

### 4.2 Non-canonical generated files

Generated files (indexes/manifests/exports/cache/derived search artifacts):

- are not required to satisfy canonical record schema,
- are not required to carry canonical verification state semantics,
- may include hash/state metadata for transport/indexing purposes,
- must not be interpreted as authoritative record verification decisions.

---

## 5) Canonical vs Non-Canonical Examples

### Canonical examples

- `records/pending/HC-CHATGPT-2026-0001.json`
- `records/verified/HC-CLAUDE-2026-0002.json`
- `records/archived/HC-EXAMPLE-2025-0420.json` (target naming)
- `records/archive/HC-EXAMPLE-2025-0420.json` (legacy/current path)

### Non-canonical examples

- `records/explorer_index.json`
- `explorer/index/records.json`
- `explorer/index/witnesses.json`
- `explorer/index/manifest.json`
- `exports/verification-package.json`
- `cache/search-snapshot.json`

---

## 6) Reference Audit Notes (post validation-hardening)

This boundary definition is consistent with existing HC-TRUST-LAYER docs that separate canonical records from generated artifacts.

Key aligned references:

- `docs/explorer-index-spec.md` defines explorer indexes as generated lookup artifacts and requires canonical validation to skip generated index/cache/export paths.
- `docs/record-format.md` defines canonical record required fields including `content_hash` and `verification_status`.
- `src/validator.py` implements skip behavior for artifact-like filenames and validates record-shaped canonical files against `record-v1` schema.

No new verification logic is introduced by this document.
