# HC-TRUST-LAYER Verification Package Validation Semantics

## Status

- documentation/specification only
- no exporter implementation changes
- no federation implementation changes
- no validator code changes
- no canonical record schema changes

## Purpose

This document defines **validation semantics** for a HC-TRUST-LAYER **verification package**.

The goal is to improve consistency checks for package consumers before future public verification APIs and federation exchange layers are expanded.

## Canonical Authority Boundary

A **verification package** is a **derived artifact**.

A verification package is a transport/export object.

A verification package is non-canonical.

A **canonical record** remains authoritative.

Package validation must never override canonical record authority and must never treat package-level metadata as canonical truth.

## Validation Flow

A package validator should execute the following flow in order.

1. **Package structure validation**
   - confirm top-level object structure
   - confirm required field presence
   - confirm expected object/array nesting for `provenance`, `audit`, and `witnesses`
2. **Schema validation**
   - validate against the declared verification package schema
   - reject unsupported or unknown schema versions
3. **Canonical path validation**
   - validate `canonical_record_path` scope is within canonical record boundaries
   - ensure path format aligns to canonical directories (`records/pending/`, `records/verified/`, `records/archived/`)
4. **`content_hash` format validation**
   - require SHA-256 shape using `sha256:<64-lowercase-hex>` formatting
5. **`verification_state` validation**
   - ensure value is known/allowed by current package semantics
   - detect contradictions between declared state and included provenance/audit context
6. **Witness structure validation**
   - validate witness entry structure and required witness context fields
   - ensure each witness element is structurally complete
7. **Audit structure validation**
   - validate `audit` object structure
   - validate audit trail references are present and well-formed
8. **Warnings inspection**
   - inspect `warnings` for risk signals and non-fatal caveats
   - preserve warnings in output rather than discarding them

## Validator Semantics Requirements

A verification package validator should:

- validate schema version
- validate required fields
- validate canonical path scope
- validate SHA-256 formatting
- inspect provenance context
- inspect witness context
- inspect warnings
- never assume truth guarantees
- never override canonical records

## Failure Categories

Validation outcomes should classify failures into explicit categories:

- invalid schema
- malformed hashes
- invalid canonical path
- unsupported package version
- missing provenance fields
- inconsistent verification state
- malformed witness structure

## Validation Result Model

Validation result levels:

- **PASS**
  - package structure and semantics checks pass
  - no blocking validation errors
- **WARNING**
  - structure is valid but cautionary conditions exist
  - warnings or partial context reduce confidence for transport use
- **FAIL**
  - one or more blocking semantic/structural checks fail
  - package cannot be accepted for integrity verification workflows

## Example Outcomes

### 1) Valid package case (PASS)

- package schema version is supported
- required fields are present
- `canonical_record_path` is in allowed canonical scope
- `content_hash` uses valid SHA-256 format
- provenance, audit trail, and witness context are structurally valid
- warnings list is empty or informational only

### 2) Warning case (WARNING)

- schema is valid and required fields are present
- canonical path and hash formatting are valid
- warnings include non-blocking transport caveats (for example missing optional mirror metadata)
- validator returns WARNING and preserves warning details for downstream review

### 3) Fail case (FAIL)

- any blocking condition exists, such as:
  - unsupported `package_version`
  - malformed `content_hash`
  - canonical path outside `records/` canonical boundaries
  - missing required provenance fields
  - malformed witness structure
- validator returns FAIL with explicit failure categories

## Integrity Verification Notes

Validation semantics support integrity verification workflows for derived artifacts.

Validation success means structural/semantic consistency checks passed for the package format; it does not change canonical record authority.

Canonical record verification remains the authoritative source of state for HC-TRUST-LAYER.

## Future Compatibility Notes

This validation semantics baseline is designed to remain compatible with planned extensions:

- Ed25519 signing planned
- federation transport planned
- public verify API planned
- external mirrors planned

These future capabilities should extend package transport confidence without changing canonical authority boundaries.

See generation architecture: `docs/verification-package-generation.md`.
See public verification API architecture draft: `docs/public-verification-api.md`.
