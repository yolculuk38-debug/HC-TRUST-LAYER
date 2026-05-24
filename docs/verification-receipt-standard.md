# Verification Receipt Standard (Draft Foundation)

Status:
- implemented: receipt model foundation in runtime code.
- experimental: receipt data is scaffold-level and not externally signed.
- planned: signature envelope and federation confirmation linking.
- research: interoperable receipt exchange profiles.

## Receipt fields

- `receipt_id`
- `verification_timestamp`
- `verification_state`
- `federation_confirmations`
- `witness_summary`
- `integrity_summary`
- `revision_summary`

## Design intent

Receipts provide an auditable summary view that can be preserved alongside records. They are intentionally modular and should remain compatible with future validator-network expansion.

## Non-production warning

This document and implementation describe a foundation only.

> Trust the record, not the narrative.
