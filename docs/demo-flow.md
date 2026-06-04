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
SHA256: ae83383b191d02970eb3df834c56b15e7a688fcd63f782d3408aaefd60b7b56a
```

## 3) QR (text-only demo)

Generate a QR artifact from record id + hash + archive reference. `docs/verify.html` is a first-flow/demo static QR verification page only; it does not verify arbitrary records.

```bash
PYTHONPATH=src python src/qr.py HC-DEMO2026-0001 ae83383b191d02970eb3df834c56b15e7a688fcd63f782d3408aaefd60b7b56a https://github.com/owner/repo/blob/main/examples/demo_record.json
```

Example output:

```text
✅ Secure QR oluşturuldu: qr/HC-DEMO2026-0001.png
🔗 URL: https://<owner>.github.io/HC-TRUST-LAYER/docs/verify.html?record=HC-DEMO2026-0001&hash=ae83383b191d02970eb3df834c56b15e7a688fcd63f782d3408aaefd60b7b56a&ref=https%3A%2F%2Fgithub.com%2Fowner%2Frepo%2Fblob%2Fmain%2Fexamples%2Fdemo_record.json&sig=...
```

> Do not commit generated QR image files (`*.png`, `*.jpg`, etc.). Keep demo evidence text-only. Existing QR artifacts should not be treated as active v0.1.0 evidence unless decoded or regenerated after PR #592.

## 4) Verify

Run repository verification. v0.1.0 does not provide a hosted general public verifier for arbitrary records; non-demo `/verify/{record_id}` QR routes are advisory/navigation placeholders unless separately deployed and validated.

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

HC:// verifies integrity and provenance signals, not objective truth. Public QR verification remains advisory-only and human-supervised; do not claim production readiness, security certification, truth finality, forensic certainty, or live public verifier guarantees.
