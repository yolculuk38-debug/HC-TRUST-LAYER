# Record Format (record-v1)

This document describes the **human-readable record format** used by the HC:// TRUST LAYER.

## Purpose of `record-v1`

`record-v1` defines a consistent JSON shape for trust records so they can be:

- validated automatically,
- compared across systems,
- archived in a stable format,
- reviewed by humans without ambiguity.

In this repository, the single executable record schema is
`schema/record-v1.schema.json`. It uses JSON Schema Draft 2020-12. The shared
Python validator applies a strict RFC 3339 format checker in addition to schema
rules.

---

## Required vs Optional Fields

### Required by `record-v1`

The following fields are required by the active `record-v1` schema:

- `schema_version` (`hc-record-v1`)
- `record_id`
- `created_at`
- `title`
- `record_type`
- `witness_type`
- `author`
- `content`
- `content_hash`
- `content_hash_profile` (`hc-content-sha256-v2`)
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
SHA-256 hash of record `content` under the declared profile.

- Type: `string`
- Pattern: `^[a-f0-9]{64}$`
- Purpose: integrity verification

### `content_hash_profile` (required)
Versioned rule used to turn `content` into bytes before SHA-256 hashing.

- Required value: `hc-content-sha256-v2`
- Text: raw UTF-8 bytes
- Structured JSON: RFC 8785 JCS bytes

The profile makes structured-content hashing deterministic. A matching digest
shows internal integrity consistency only; it does not establish that the
content was originally true.

### `created_at` (required)
Record creation time in the strict RFC 3339 profile enforced by the shared
validator.

- Example: `2026-05-19T00:00:00Z`
- A timezone (`Z` or numeric offset) is required.

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
  "schema_version": "hc-record-v1",
  "record_id": "HC-EXAMPLE-2026-0001",
  "created_at": "2026-05-19T00:00:00Z",
  "title": "Minimal valid record",
  "record_type": "ai_witness",
  "witness_type": "ai",
  "author": "hc-system",
  "content": "Minimal valid record content.",
  "content_hash": "3bc32e81106ad6849e0772f721c2f925cb69a1d42f5712137c8c82aa5655ce41",
  "content_hash_profile": "hc-content-sha256-v2",
  "archive_ref": "pending_archive",
  "verification_status": "draft"
}
```

Schema validation, content-digest verification, requested-record binding, and
trust interpretation are separate checks. Passing one must not be promoted as
evidence that the others passed.

---

## Integrity Rule: No Silent Post-Verification Mutation

Once a record reaches `verified` status, it **must not be silently modified**.

Any correction or update must be explicitly recorded through a traceable process (for example: a new record, explicit revision metadata, or an archive/provenance-linked amendment), so auditors can detect and review the change history.
