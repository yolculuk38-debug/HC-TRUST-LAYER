# HC:// TRUST LAYER — Verify a Record

This page is a minimal, visible verification guide for first-time visitors.

## What a QR Code Points To

In HC:// TRUST LAYER, a QR code should point to verification data that includes:

- **record id**
- **content hash**
- **record URL**
- **verification status**

## Minimal Text-Only Verification Example

```text
input_record_id: HC-DEMO-2026-0001
input_hash: 9c169042065246d3b963163cfe8ffe876ffce57fa8759e402281d036f0f9cffc
expected_verification_result: PASS (record id + hash + URL consistency)
```

## Demo Links

- Demo record: [`examples/demo_record.json`](../examples/demo_record.json)
- Demo flow: [`docs/demo-flow.md`](demo-flow.md)

## Note

HC:// verification confirms record integrity and provenance signals, not objective truth.
