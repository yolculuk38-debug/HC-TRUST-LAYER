# HC:// QR Verification

> Status: **Documentation / Conceptual guidance**
>
> This page explains the current QR verification workflow and expected verification outputs for HC:// TRUST LAYER records.

## What the QR Points To

In HC:// TRUST LAYER, a QR code is used as a portable pointer to verification data.

A QR payload should resolve to a stable verification location that contains (directly or indirectly):

- the **record ID** (for example `HC-CHATGPT-2026-0001`)
- the **content hash** tied to that record
- the **repository source** used as the reference verification dataset
- the latest known **validation status**

Depending on deployment mode, the QR may point to:

1. A repository path containing the record and hash files.
2. A verification endpoint that returns record metadata.
3. A static verification artifact generated from repository state.

## What Is Verified After Scanning

After scanning, verification should confirm that the scanned reference matches canonical HC:// data.

The verification workflow checks the following fields:

1. **Record ID**
   - Format and identity consistency (ID in QR context should map to an existing HC:// record).
2. **Content Hash**
   - Hash value must match the canonical hash associated with the record.
3. **Repository Source**
   - Source location should be an expected HC:// repository or trusted mirror/source path.
4. **Validation Status**
   - Status should indicate whether schema/hash validation is currently passing, failing, or pending review.

## Minimum Verification Output

A scanner or verifier UI should display at least:

- `record_id`
- `content_hash`
- `repository_source`
- `validation_status`

Optional extended output may include provenance links, witness summary, and archive references.

## Example (Conceptual)

```text
record_id: HC-CHATGPT-2026-0001
content_hash: <sha256>
repository_source: github.com/<org>/<repo>
validation_status: PASS
```

## Notes

- QR is a discovery and access mechanism; trust comes from independent verification of data behind the QR.
- A readable QR alone is not proof of authenticity.
- Final trust decisions should include witness and provenance context, not hash checks alone.
