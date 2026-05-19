# Record Format (record-v1)

This document describes the **human-readable record format** used by the HC:// TRUST LAYER.

## Purpose of `record-v1`

`record-v1` defines a consistent JSON shape for trust records so they can be:

- validated automatically,
- compared across systems,
- archived in a stable format,
- reviewed by humans without ambiguity.

In this repository, schema validation is enforced against `schema/record-v1.schema.json`.

---

## Required vs Optional Fields

### Required by `record-v1`

The following fields are required by the active `record-v1` schema:

- `record_id`
- `created_at`
- `title`
- `record_type`
- `witness_type`
- `author`
- `content_hash`
- `archive_ref`
- `verification_status`

### Optional in current schema

The following fields are currently optional in `record-v1`:

- `description`
- `tags`

### Trust-context fields (optional, extension/interop)

Some trust workflows may include additional contextual fields such as:

- `timestamp` (often treated as alias/interoperability field for `created_at`)
- `metadata`
- `witnesses`
- `provenance`
- `signature`

These fields are useful for richer verification context, but they are not required by the current `record-v1.schema.json` unless your environment applies additional constraints.

---

## Main Field Definitions

### `record_id` (required)
Unique record identifier.

- Type: `string`
- Pattern: `^HC-[A-Z0-9]+-[0-9]{4}-[0-9]{4}$`
- Example: `HC-CHATGPT-2026-0001`

### `author` (required)
Human or system identifier that authored the record.

- Type: `string`
- Min length: `1`

### `content_hash` (required)
SHA-256 hash of canonical record content.

- Type: `string`
- Pattern: `^[a-f0-9]{64}$`
- Purpose: integrity verification

### `timestamp` (optional / interop)
Record creation time in ISO 8601 datetime format.

- In the active schema, the required creation field is `created_at`.
- Use `timestamp` only for compatibility with systems that expect it.

### `verification_status` (required)
Current verification lifecycle state.

- Type: `string`
- Allowed values:
  - `draft`
  - `reviewed`
  - `verified`
  - `archived`

### `metadata` (optional extension)
Structured extra context (tooling, labels, environment details, etc.).

- Suggested type: `object`
- Recommendation: keep metadata deterministic and audit-friendly.

### `witnesses` (optional extension)
List of witness references or witness records connected to this record.

- Suggested type: `array`
- Recommendation: each witness entry should be stable and traceable.

### `provenance` (optional extension)
Origin and transformation chain information.

- Suggested type: `object`
- Typical content: source, processing steps, upstream identifiers, references.

### `signature` (optional, if present)
Cryptographic signature over canonical record payload.

- Suggested type: `string` or `object` (depending on signature scheme)
- If present, signature material should include enough information to verify key identity and algorithm.

---

## Minimal Valid JSON Example (`record-v1`)

```json
{
  "record_id": "HC-EXAMPLE-2026-0001",
  "created_at": "2026-05-19T00:00:00Z",
  "title": "Minimal valid record",
  "record_type": "ai_witness",
  "witness_type": "ai",
  "author": "hc-system",
  "content_hash": "9f3a3fb4f7c21ab3a89d4f7db0bf75db6ea9cc57f398a7db53f4a62f5a4d8d57",
  "archive_ref": "pending_archive",
  "verification_status": "draft"
}
```

---

## Integrity Rule: No Silent Post-Verification Mutation

Once a record reaches `verified` status, it **must not be silently modified**.

Any correction or update must be explicitly recorded through a traceable process (for example: a new record, explicit revision metadata, or an archive/provenance-linked amendment), so auditors can detect and review the change history.
