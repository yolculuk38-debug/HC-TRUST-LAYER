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

## Explorer navigation flow

1. Open `docs/explorer/index.html` through a local or static file server.
2. The page attempts to load `generated/explorer_index.json` first, then documented fallback paths for static hosting.
3. Search by Record ID or Content Hash.
4. Select a result, or open a record detail route/query directly.
5. Review Verification Summary, Record Metadata, Hash Information, and Witness Information sections.
6. Use the source path and generated index metadata as navigation aids for human-supervised validation.

## List fields

The Explorer list displays these generated index fields when present:

- Record ID.
- Verification Status.
- Timestamp.
- Content Hash.
- QR reference.
- Witness Count.
- Source Path.

## Record detail endpoint

The MVP record detail route is:

- `/explorer/record/<record_id>`

The short route alias is:

- `/record/<record_id>`

For static hosting that does not rewrite route paths to `docs/explorer/index.html`, the same lookup can be represented as:

- `docs/explorer/index.html?record_id=<record_id>`
- `docs/explorer/index.html?record=<record_id>`

These routes are read-only navigation surfaces over the generated explorer index. They do not modify canonical records, schemas, validators, signing logic, federation behavior, or policy evaluator behavior.

## Detail page fields

The detail page displays:

### Verification Summary

- Record ID.
- Verification Status.
- Timestamp.
- Advisory/read-only/human-supervised flags when present.

### Record Metadata

- Source path.
- QR reference, when available.
- Generated index metadata such as author, record type, title, and created timestamp when present.

### Hash Information

- Content Hash.
- Content Hash Prefix, when present.

### Witness Information

- Witness count.
- Witness metadata from the generated explorer index.
- Witness type, when present.

The page may also show verification history, archive status, provenance/source fields, additional generated verification fields, and a raw generated index entry preview for audit trail review.

## Example successful detail response

```json
{
  "route": "/explorer/record/HC-EXAMPLE-2026-0001",
  "alternate_route": "/record/HC-EXAMPLE-2026-0001",
  "found": true,
  "record_id": "HC-EXAMPLE-2026-0001",
  "verification_summary": {
    "verification_status": "draft",
    "timestamp": "2026-05-12T10:00:00Z",
    "advisory_only": true,
    "human_supervised": true
  },
  "record_metadata": {
    "record_id": "HC-EXAMPLE-2026-0001",
    "source_path": "records/pending/HC-EXAMPLE-2026-0001.json",
    "qr_reference": "",
    "metadata": {
      "record_type": "ai_witness",
      "title": "Example AI Witness Record"
    }
  },
  "hash_information": {
    "content_hash": "740f84dec83cce227ff4b6fb4280b088834dda8a632fa6c20250c829b80188dc"
  },
  "witness_information": {
    "witness_count": 2,
    "witnesses": ["ChatGPT", "Claude"]
  },
  "advisory_only": true,
  "read_only": true,
  "human_supervised": true
}
```

## Example missing record response

```json
{
  "route": "/explorer/record/HC-MISSING-2099-0001",
  "alternate_route": "/record/HC-MISSING-2099-0001",
  "found": false,
  "record_id": "HC-MISSING-2099-0001",
  "message": "Record detail is unavailable because the Record ID was not found in generated/explorer_index.json.",
  "error": {
    "code": "record_not_found",
    "human_message": "No generated explorer detail is available for this Record ID."
  },
  "advisory_only": true,
  "read_only": true,
  "human_supervised": true
}
```

The human-readable page displays the same missing-record message and keeps the absence advisory. Absence from the generated explorer index is not a trust-kernel decision.

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

- Explorer helper tests for search, record lookup, record detail rendering, and missing record handling.
- Existing Explorer smoke tests for advisory-only and non-canonical UI boundaries.
- Terminology, docs drift, and canonical artifact guards when available in the repository environment.
