# HC-TRUST-LAYER Verification Package Generation Architecture

## Status

- documentation/specification only
- no exporter implementation in this phase
- no validator, schema, or canonical record changes in this phase

## Purpose

This document defines the HC-TRUST-LAYER **verification package generation** architecture.

It specifies how a **verification package** should be produced as a **derived artifact** from a **canonical record** source, without introducing production exporter logic yet.

## Canonical Authority and Generation Boundary

Package generation output is **non-canonical**.

Package generation must never mutate canonical records.

Package generation must never overwrite `records/`.

Generated verification packages are derived export artifacts intended for portability and integrity verification workflows; they never become canonical records.

## Allowed and Disallowed Generation Sources

### Allowed canonical source scopes

- `records/pending/`
- `records/verified/`
- `records/archived/`

### Disallowed source scopes

Generation must not use the following as canonical generation sources:

- generated caches
- explorer indexes
- manifests
- temporary artifacts
- `docs/generated/`
- `exports/cache/`

## Generation Pipeline Stages

A package generation flow should follow these stages.

1. **canonical record selection**
   - Resolve a canonical record path only from allowed `records/` scopes.
   - Reject sources outside canonical record boundaries.

2. **integrity verification**
   - Validate record-level integrity inputs required for package export context.
   - Stop generation on malformed hash shapes or invalid canonical paths.

3. **provenance extraction**
   - Extract provenance context required by verification package fields.
   - Preserve provenance references without rewriting canonical provenance meaning.

4. **audit reference collection**
   - Collect audit trail references relevant to the selected canonical record.
   - Keep audit references as transport context, not authority replacement.

5. **witness extraction**
   - Extract witness entries and witness context required by package semantics.
   - Reject malformed or unresolved witness references.

6. **verification state capture**
   - Capture verification state aligned with canonical state at read time.
   - Reject internally inconsistent state combinations.

7. **metadata normalization**
   - Normalize metadata fields for stable serialization and interoperability.
   - Apply deterministic key and list ordering where possible.

8. **package assembly**
   - Assemble the verification package envelope from collected derived data.
   - Mark output semantics as derived/non-canonical export.

9. **schema validation**
   - Validate assembled output against the declared verification package schema.
   - Reject unsupported package versions.

10. **derived artifact classification**
    - Classify output explicitly as a derived artifact.
    - Ensure generated output cannot be interpreted as canonical authority.

## Generation Safety Rules

Generation implementations should enforce the following safety rules:

- immutable-style source handling
- read-only canonical processing
- reproducible package generation
- deterministic metadata ordering where possible
- no truth guarantees
- no authority escalation

### Additional safety clarifications

- Package generation is a read/derive/export operation, never a canonical mutation operation.
- Generated package metadata does not elevate AI, tool, or exporter authority over canonical records.
- Integrity verification in generation is consistency checking, not objective truth proof.

## Generation Failure Categories

Generation and pre-export validation outcomes should classify blocking failures into explicit categories:

- invalid canonical path
- schema mismatch
- malformed hashes
- missing provenance fields
- unsupported package version
- inconsistent verification state
- invalid witness references

## Future Generation Targets

This architecture is intended to support multiple future export and transport targets without changing canonical authority boundaries:

- local export
- public verification API response
- federation exchange package
- offline verification bundle
- archive transport package

## Future Compatibility

Planned compatibility directions:

- Ed25519 signing
- federation transport
- external mirrors
- verification API
- explorer download integration

These are compatibility goals for future package generation and transport pathways; they do not imply current production readiness.

## Deterministic Generation Notes

**Deterministic generation** means that, given the same canonical inputs and versioned generation rules, package output should be reproducible aside from explicitly time-scoped metadata fields (for example `generated_at` when policy allows runtime timestamps).

Deterministic generation improves audit trail consistency for HC:// verification contexts while preserving canonical record authority.

## Non-Goals for This Phase

- implementing production exporter logic
- modifying validators
- changing schemas
- creating generated packages
- redefining canonical record authority

## Related Specifications

- verification package format: `docs/verification-package-format.md`
- verification package validation semantics: `docs/verification-package-validation.md`
- implementation maturity map: `docs/implementation-map.md`
- capability status matrix: `docs/capability-status.md`

## Exporter Skeleton Usage (Non-Production)

A safe **exporter skeleton** is available at `scripts/export_verification_package.py` for HC-TRUST-LAYER.

### Safety scope

- accepts only canonical record JSON paths under:
  - `records/pending/*.json`
  - `records/verified/*.json`
  - `records/archived/*.json`
- rejects generated/index/export/cache artifact paths
- reads canonical record as input only (no mutation)
- emits a **verification package** as a **derived artifact** (**non-canonical**)
- schema-validates against `schema/verification-package-v1.schema.json` when optional validation dependency is available
- prints package JSON to stdout by default
- writes to disk only when `--output` is provided and the output is under `examples/generated/`

### Explicit warnings in output

The exporter skeleton includes explicit warnings that:

- this is an exporter skeleton
- package output is derived and non-canonical
- signatures are not yet implemented

### Example commands

```bash
python3 scripts/export_verification_package.py records/pending/HC-EXAMPLE-2026-0001.json
```

```bash
python3 scripts/export_verification_package.py \
  records/pending/HC-EXAMPLE-2026-0001.json \
  --output examples/generated/HC-EXAMPLE-2026-0001.package.json
```

This workflow supports integrity verification and portability for HC:// contexts while preserving canonical record authority boundaries.
