# Record Signatures

This directory stores witness and validator signature artifacts for HC:// records.

## Naming Guidance
- Recommended filename: `<record_id>--<signer_id>--<timestamp>.json`

## Requirements
Each signature object should validate against `schema/signature.schema.json` and include:
- `signer_id`
- `algorithm`
- `signed_hash`
- `signature`
- `timestamp`
- `witness_role`

## Storage Principles
- Append-only writes.
- Do not rewrite prior signature artifacts.
- Superseded signatures should be linked via revision/audit metadata rather than deleted.
