# Humanity Chain Verification Workflow v1

## Record Lifecycle

```
┌─────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  DRAFT  │ --> │ REVIEWED │ --> │ VERIFIED │ --> │ ARCHIVED │
└─────────┘     └──────────┘     └──────────┘     └──────────┘
```

---

## State Descriptions

### 1. DRAFT
- Record newly created
- Not yet validated
- Not reviewed by witnesses
- Can be modified

### 2. REVIEWED
- Checked by human or AI reviewer
- Issues marked and noted
- Under verification process
- Awaiting approval

### 3. VERIFIED
- All verification criteria met
- Multi-witness approval (optional)
- Ready for archive
- Content immutable
- Hash fingerprint locked

### 4. ARCHIVED
- Stored in official archive
- Long-term reference
- Fully immutable
- Permanent hash reference
- QR code linked

---

## Workflow Steps

### Create Record

```bash
# 1. Create record file (JSON format)
cat > records/draft/HC-MODEL-2026-0001.json << 'EOF'
{
  "record_id": "HC-MODEL-2026-0001",
  "created_at": "2026-05-14T10:00:00Z",
  "title": "Record Title",
  "record_type": "ai_witness",
  "witness_type": "ai",
  "author": "YourName",
  "content_hash": "abc123...",
  "archive_ref": "records/verified/HC-MODEL-2026-0001.md",
  "verification_status": "draft"
}
EOF

# 2. Validate with schema
python src/validator.py records/draft/HC-MODEL-2026-0001.json

# 3. Calculate content hash
python src/hash.py records/draft/HC-MODEL-2026-0001.json
```

### Review Process

```bash
# 1. Format and metadata check
python src/validator.py records/draft/HC-MODEL-2026-0001.json

# 2. Witness review (human/AI)
# - Examine content
# - Note issues if any
# - Approve or request changes

# 3. Update status to "reviewed"
# Edit JSON: "verification_status": "reviewed"

# 4. If issues: back to DRAFT
# If approved: proceed to verification
```

### Verification

```bash
# 1. Verify content hasn't changed
python src/hash.py records/draft/HC-MODEL-2026-0001.json

# 2. Check metadata completeness
python src/validator.py records/draft/HC-MODEL-2026-0001.json

# 3. Generate QR code
python src/qr.py HC-MODEL-2026-0001 <hash> records/verified/HC-MODEL-2026-0001.md

# 4. Update status to "verified"
# Edit JSON: "verification_status": "verified"
```

### Archive

```bash
# 1. Move to archive directory
mv records/draft/HC-MODEL-2026-0001.json records/verified/HC-MODEL-2026-0001.json

# 2. Store hash reference
echo "HC-MODEL-2026-0001: <hash>" >> hash/hashes.log

# 3. Link QR code
# QR already in: qr/HC-MODEL-2026-0001.png

# 4. Final status update
# Edit JSON: "verification_status": "archived"

# 5. Commit to repository
git add records/verified/ hash/ qr/
git commit -m "archive: Add HC-MODEL-2026-0001 to official archive"
```

---

## Available Tools

| Tool | Purpose | Command |
|------|---------|---------|
| **validator.py** | Validate record JSON | `python src/validator.py <file.json>` |
| **hash.py** | Calculate SHA256 | `python src/hash.py <file.json>` |
| **qr.py** | Generate QR code | `python src/qr.py <id> <hash> <ref>` |

---

## Example Workflows

### Quick Validation

```bash
# Test all example records
python src/validator.py examples/ai_witness_example.json
python src/validator.py examples/human_witness_example.json
python src/validator.py examples/multi_model_example.json
```

### Full Record Creation

```bash
# 1. Create record
cp examples/ai_witness_example.json records/draft/HC-NEW-2026-0001.json

# 2. Edit with your data
nano records/draft/HC-NEW-2026-0001.json

# 3. Validate
python src/validator.py records/draft/HC-NEW-2026-0001.json

# 4. Hash
python src/hash.py records/draft/HC-NEW-2026-0001.json

# 5. Generate QR
python src/qr.py HC-NEW-2026-0001 <hash> records/verified/HC-NEW-2026-0001.md

# 6. Update to "reviewed" status, then "verified", then "archived"
```

---

## Important Notes

- **Immutability**: Once `verified`, content hash cannot change
- **Archive**: `archived` status is permanent
- **Witness**: Can be human (manual) or AI (automated)
- **Multi-Witness**: Multiple reviewers increase confidence
- **Transparency**: All states visible in JSON metadata

---

## Status Reference

```json
{
  "draft": "Initial state, editable, no validation yet",
  "reviewed": "Reviewed by witness, issues may be noted",
  "verified": "Approved, hash locked, ready for archive",
  "archived": "In official archive, immutable, permanent"
}
```
