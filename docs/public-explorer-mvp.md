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
3. Search by Record ID, Content Hash, Verification Status, or Source Path.
4. Select a result to view the read-only detail page.
5. Review metadata, verification history, witness information, and archive status.

## Search examples

The Explorer MVP search is deterministic over the loaded generated index and does not modify records.
Use the **Search by** selector to choose one of these advisory lookup modes:

- `record_id`: enter a full or partial Record ID, such as `HC-EXAMPLE-2026-0001`.
- `content hash`: enter a full or partial content hash, such as `740f84dec83c`.
- `verification_status`: enter a status value from the generated index, such as `draft`.
- `source_path`: enter a full or partial source path, such as `records/pending/HC-2026-0002.json`.
- `record_id, content hash, status, or source path`: use the combined mode when the exact field is unknown.

If no result appears, the Explorer only reports that the generated explorer index has no matching entry for the submitted value.
That empty result is not a trust-kernel decision and does not change the canonical record boundary.

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
Missing records in the Explorer mean only that the generated explorer index does not contain the queried Record ID, Content Hash, Verification Status, or Source Path.
Absence from the Explorer is not a trust-kernel decision.

## Validation notes

Relevant checks for this MVP include:

- Explorer helper tests for search, record lookup, and missing record handling.
- Existing Explorer smoke tests for advisory-only and non-canonical UI boundaries.
- Terminology, docs drift, and canonical artifact guards when available in the repository environment.
