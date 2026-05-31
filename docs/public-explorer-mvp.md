# HC:// Public Verification Explorer MVP

The HC:// Public Verification Explorer MVP is a read-only, user-facing view over `generated/explorer_index.json`.
It helps a reviewer search a generated verification index and inspect record metadata without opening repository files directly.

## Scope

The Explorer MVP is:

- Advisory Only.
- Read Only.
- Human Supervised.
- Local/static-data oriented, using `generated/explorer_index.json` as its data source.

The Explorer MVP does not provide production readiness, autonomous governance finality, forensic certainty, or truth guarantees.
Human-supervised validation remains the final authority for HC-TRUST-LAYER review boundaries.

## User flow

1. Open `docs/explorer/index.html` through a local or static file server.
2. The page attempts to load `generated/explorer_index.json` first, then documented fallback paths for static hosting.
3. Search by Record ID or Content Hash.
4. Select a result to view the read-only detail page.
5. Review metadata, verification history, witness information, and archive status.

## List fields

The Explorer list displays these generated index fields when present:

- Record ID.
- Verification Status.
- Timestamp.
- Content Hash.
- Witness Count.
- Source Path.

## Detail page fields

The detail page displays:

- Full record metadata from the generated index entry.
- Verification history from the generated index entry.
- Witness information and witness count.
- Archive status.
- Raw generated index entry preview for audit trail review.

## Explicit non-goals

The Explorer MVP does not implement:

- Trust scoring.
- Federation writes.
- Automatic decisions.
- Record modification.
- Schema, validator, signing, federation, canonical record, or policy evaluator changes.

## Data boundary

`generated/explorer_index.json` is an advisory navigation surface. It is not itself a canonical record.
Missing records in the Explorer mean only that the generated explorer index does not contain the queried Record ID or Content Hash.
Absence from the Explorer is not a trust-kernel decision.

## Validation notes

Relevant checks for this MVP include:

- Explorer helper tests for search, record lookup, and missing record handling.
- Existing Explorer smoke tests for advisory-only and non-canonical UI boundaries.
- Terminology, docs drift, and canonical artifact guards when available in the repository environment.
