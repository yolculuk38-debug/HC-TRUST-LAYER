# Demo Flow (Visible Verification)

This demo shows the shortest **text-first** verification path for HC:// TRUST LAYER:

`record → hash → QR → verify → trust explanation`

## 1) Record

Use the sample record:

- `examples/demo_record.json`

## 2) Hash

Generate a SHA-256 hash for the record:

```bash
PYTHONPATH=src python src/hash.py examples/demo_record.json
```

Example output:

```text
SHA256: 9c169042065246d3b963163cfe8ffe876ffce57fa8759e402281d036f0f9cffc
```

## 3) QR (text-only demo)

Generate a QR artifact from record id + hash + archive reference:

```bash
PYTHONPATH=src python src/qr.py HC-DEMO-2026-0001 9c169042065246d3b963163cfe8ffe876ffce57fa8759e402281d036f0f9cffc https://github.com/owner/repo/blob/main/examples/demo_record.json
```

Example output:

```text
✅ Secure QR oluşturuldu: qr/HC-DEMO-2026-0001.png
🔗 URL: https://yolculuk38-debug.github.io/HC-TRUST-LAYER/?record=HC-DEMO-2026-0001&hash=9c169042065246d3b963163cfe8ffe876ffce57fa8759e402281d036f0f9cffc&ref=https://github.com/owner/repo/blob/main/examples/demo_record.json&sig=<signature>
```

> Do not commit generated QR image files (`*.png`, `*.jpg`, etc.). Keep demo evidence text-only.

## 4) Verify

Run repository verification:

```bash
PYTHONPATH=src python -m hc_trust.cli verify records
```

Example output:

```text
Verifying SHA-256 hashes for 2 record(s)...
✅ PASS: records/pending/HC-2026-0002.json (hash: 7fdd78c9832ea154...)
✅ PASS: records/pending/HC-EXAMPLE-2026-0001.json (hash: 740f84dec83cce22...)

Results: 2 passed, 0 failed
```

## 5) Trust explanation

HC:// verifies integrity and provenance signals, not objective truth.
