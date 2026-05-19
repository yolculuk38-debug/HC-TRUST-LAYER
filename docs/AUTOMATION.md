# Humanity Chain - Record Automation

This document explains how to use the automated record creation, normalization, validation, hash generation, and QR code generation tools.

## Overview

The automation layer handles:

- **Normalization**: Automatically fills missing required fields with safe defaults
- **Validation**: Ensures records conform to the JSON schema
- **Hashing**: Generates SHA256 fingerprints for content
- **QR Codes**: Creates QR codes for verification URLs

## Quick Start

### 1. Create a New Pending Record

Create a JSON file in `records/pending/` with minimal information:

```bash
# records/pending/HC-CHATGPT-2026-0001.json
{
  "title": "My AI Interaction Record",
  "content": "The full content or transcript here..."
}
```

### 2. Normalize Records

Automatically fill missing required fields:

```bash
python src/normalize_records.py --dry-run
```

Apply the proposed changes explicitly:

```bash
python src/normalize_records.py --write
```

Safety behavior:
- `--dry-run` prints unified diffs and never writes files
- without `--write`, changes are only reported and skipped
- records in `records/archive/` and `records/verified/` are never silently overwritten

This will:
- Derive `record_id` from filename if available
- Generate `record_id` if not present
- Add timestamps
- Set default values for missing fields
- Generate `content_hash` from content if missing
- Pretty-print JSON with stable key ordering

**Output:**
```
============================================================
Humanity Chain Record Normalizer
============================================================

Found 3 pending record(s)

✓ Normalized: records/pending/HC-CHATGPT-2026-0001.json
✓ Normalized: records/pending/HC-GEMINI-2026-0002.json
✓ Normalized: records/pending/HC-CLAUDE-2026-0003.json

============================================================
⚠️  3 record(s) were normalized

📋 Please review and commit changes:
   git add records/pending/
   git commit -m 'chore: normalize pending records'
============================================================
```

### 3. Validate Records

Validate all records against the schema:

```bash
python src/validator.py
```

This will check:
- JSON syntax validity
- Required fields presence
- Field type correctness
- Enum value validity
- SHA256 hash format

**Output:**
```
============================================================
Humanity Chain Record Validator
============================================================

✓ Schema loaded: schema/record-v1.schema.json

Found 6 record file(s)

✓ records/pending/HC-CHATGPT-2026-0001.json
✓ records/verified/HC-CLAUDE-2026-0002.json
✓ records/archive/HC-GEMINI-2026-0003.json

============================================================
Summary: 6 passed, 0 failed

✅ All records valid
============================================================
```

### 4. Generate Hash for Text

Generate SHA256 hash for a text string:

```bash
python src/hash.py --text "hello world"
```

**Output:**
```
7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069
```

### 5. Generate Hash for File

Generate SHA256 hash for a JSON file:

```bash
python src/hash.py --file records/pending/HC-CHATGPT-2026-0001.json
```

**Output:**
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a7b8c9d0e1f
```

### 6. Generate QR Code

Generate QR code for a record's verification URL:

```bash
python src/qr.py \
  --record-id HC-CHATGPT-2026-0001 \
  --url https://humanity-chain.example.com/verify/HC-CHATGPT-2026-0001
```

This creates `qr/HC-CHATGPT-2026-0001.png`

**Output:**
```
✓ QR code generated: qr/HC-CHATGPT-2026-0001.png
```

## Workflow

### Manual Workflow

```bash
# 1. Create pending record
echo '{ "title": "My Record", "content": "..." }' > records/pending/HC-2026-0001.json

# 2. Normalize
python src/normalize_records.py --dry-run

# 3. Validate
python src/validator.py

# 4. Generate hash
python src/hash.py --file records/pending/HC-2026-0001.json

# 5. Generate QR
python src/qr.py --record-id HC-2026-0001 --url https://example.com/verify/HC-2026-0001

# 6. Commit
git add records/pending/ qr/
git commit -m 'feat: add new record HC-2026-0001'
```

### CI/CD Workflow

When you push changes:

1. **`.github/workflows/validate.yml`** runs automatically
   - Normalizes records
   - If changes needed, fails with clear message
   - Validates all records
   - Ensures consistency before merge

2. **`.github/workflows/test.yml`** runs tests
   - Tests all Python modules
   - Ensures code quality

## Field Reference

### Required Fields

| Field | Type | Example | Auto-filled |
|-------|------|---------|-------------|
| `record_id` | string | `HC-CHATGPT-2026-0001` | Yes, from filename or generated |
| `created_at` | ISO datetime | `2026-05-14T12:34:56Z` | Yes, current UTC |
| `title` | string | `"My AI Interaction"` | Yes, from record_id if missing |
| `record_type` | enum | `ai_witness` | Yes, defaults to `ai_witness` |
| `witness_type` | enum | `multi` | Yes, defaults to `multi` |
| `author` | string | `Fatih` | Yes, defaults to `Fatih` |
| `content_hash` | SHA256 | `a1b2c3...` | Yes, from content field |
| `archive_ref` | string | `pending_archive` | Yes |
| `verification_status` | enum | `draft` | Yes, defaults to `draft` |

### Optional Fields

| Field | Type | Purpose |
|-------|------|---------|
| `content` | string | The main record content |
| `description` | string | Additional description |
| `tags` | array | Classification tags |
| `id` | string | Same as record_id |
| `status` | string | Current status (`pending`, `approved`, etc.) |
| `prev_hash` | string | Hash of previous version |
| `hash` | string | Current version hash |

## Validation Rules

### record_id Pattern
```
^HC-[A-Z0-9]+-[0-9]{4}-[0-9]{4}$
```

Examples:
- ✓ `HC-CHATGPT-2026-0001`
- ✓ `HC-GPT4-2026-0100`
- ✗ `HC-chatgpt-2026-0001` (lowercase)
- ✗ `HC-2026-0001` (missing model)

### content_hash Format
```
^[a-f0-9]{64}$
```

Must be valid SHA256 (64 hex characters)

### Enum Values

**record_type:**
- `ai_witness`
- `human_witness`
- `multi_model_record`
- `protocol_note`

**witness_type:**
- `ai`
- `human`
- `multi`

**verification_status:**
- `draft`
- `reviewed`
- `verified`
- `archived`

## Error Handling

### Normalization Errors

**Problem:** Invalid JSON
```
✗ records/pending/bad.json: Invalid JSON - ...
```

**Solution:** Fix JSON syntax

### Validation Errors

**Problem:** Missing required field
```
✗ records/pending/HC-2026-0001.json
    └─ 'author' is a required property
```

**Solution:** Run `python src/normalize_records.py --dry-run` to auto-fill

**Problem:** Invalid enum value
```
✗ records/pending/HC-2026-0001.json
    └─ 'invalid_type' is not one of ['ai_witness', ...]
```

**Solution:** Use valid enum value from schema

**Problem:** Invalid SHA256 hash
```
✗ records/pending/HC-2026-0001.json
    └─ 'not-a-hash' does not match '^[a-f0-9]{64}$'
```

**Solution:** Run `python src/hash.py --file <filepath>` to generate valid hash

## Examples

### Example 1: AI Witness Record

```json
{
  "record_id": "HC-CHATGPT-2026-0001",
  "created_at": "2026-05-14T10:30:00Z",
  "title": "ChatGPT Interaction on Verification Systems",
  "content": "User: What are verification systems?\n\nChatGPT: Verification systems are...",
  "record_type": "ai_witness",
  "witness_type": "ai",
  "author": "Fatih",
  "content_hash": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a7b8c9d0e1f",
  "archive_ref": "pending_archive",
  "verification_status": "draft"
}
```

### Example 2: Human Witness Record

```json
{
  "record_id": "HC-HUMAN-2026-0001",
  "created_at": "2026-05-14T11:00:00Z",
  "title": "Human Witness: Discussion on Content Verification",
  "content": "Witnessed discussion between...",
  "record_type": "human_witness",
  "witness_type": "human",
  "author": "Fatih",
  "content_hash": "b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a7b8c9d0e1f2",
  "archive_ref": "pending_archive",
  "verification_status": "draft"
}
```

## Command Reference

```bash
# Normalize all pending records
python src/normalize_records.py --dry-run

# Validate all records
python src/validator.py

# Hash text
python src/hash.py --text "<text>"

# Hash file
python src/hash.py --file <filepath>

# Generate QR code
python src/qr.py --record-id <id> --url <url> [--output <path>]

# Run tests
pytest tests/ -v

# Run validation workflow (CI)
python src/normalize_records.py --dry-run --dry-run
python src/normalize_records.py --dry-run --write
python src/validator.py
```

## Troubleshooting

### Issue: "Records were auto-normalized. Please run locally."

**Cause:** CI detected records that needed normalization

**Solution:**
```bash
python src/normalize_records.py --dry-run
git add records/pending/
git commit -m 'chore: normalize pending records'
git push
```

### Issue: "content_hash does not match pattern"

**Cause:** Invalid SHA256 hash in record

**Solution:**
```bash
# Get content hash
python src/hash.py --text "<content>"

# Update record_id field with the output
```

### Issue: Tests failing

**Solution:**
```bash
# Install test dependencies
pip install pytest

# Run tests with verbose output
pytest tests/ -v --tb=long
```

## Advanced Usage

### Batch Processing

```bash
# Process multiple records
for file in records/pending/*.json; do
  python src/hash.py --file "$file"
done
```

### Integration with Git Hooks

```bash
# .git/hooks/pre-commit
#!/bin/bash
python src/normalize_records.py --dry-run
if [ $? -ne 0 ]; then
  exit 1
fi
python src/validator.py
exit $?
```

### Automated QR Generation

```bash
#!/bin/bash
# Generate QR codes for all verified records
for file in records/verified/*.json; do
  record_id=$(jq -r '.record_id' "$file")
  url="https://example.com/verify/$record_id"
  python src/qr.py --record-id "$record_id" --url "$url"
done
```
