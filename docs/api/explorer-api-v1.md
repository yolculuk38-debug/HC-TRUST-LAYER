# HC-TRUST-LAYER Explorer API (Experimental)

The **HC-TRUST-LAYER explorer runtime layer** provides public-safe, non-production lookup responses.

## Runtime Contract

All explorer responses are wrapped with:

- `runtime: "explorer"`
- `status: "experimental"`
- `non_production: true`
- `runtime_version: "HC-TRUST-LAYER-EXPLORER-RUNTIME-V1-EXPERIMENTAL"`

## Endpoints (Runtime Functions)

### 1) Record Lookup

Function: `get_explorer_record_lookup(record_id, record_store)`

Returns a public-safe payload containing:

- `record_id`
- `found`
- `status`
- `trust_score`
- optional `verification_level`
- optional `last_updated`

### 2) Verification Receipt Lookup

Function: `get_explorer_receipt_lookup(receipt_id, receipt_store)`

Returns a public-safe payload containing:

- `receipt_id`
- `found`
- `verification_state`
- `verification_timestamp`
- `federation_confirmations`
- `witness_summary`
- `integrity_summary`
- `revision_summary`

### 3) Federation Status Summary

Function: `get_federation_status_summary(nodes)`

Returns aggregated federation status:

- `network`
- `total_nodes`
- `online_nodes`
- `degraded_nodes`
- `offline_nodes`
- `sync_state`

## Non-Production Notice

This runtime is intentionally experimental and must not be treated as a production verification API.
