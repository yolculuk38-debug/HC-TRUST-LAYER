# HC:// Demo Verification Flow

This document defines the first real end-to-end HC:// demo verification flow in HC-TRUST-LAYER.

## 1) Record file path

- `records/verified/demo-record-001.json`

## 2) Content used for hash

The `content_hash` is computed from the exact `content` field value in the demo record:

```text
HC:// demo verification payload v1
package_id: HC-DEMO-PKG-2026-0001
record_id: HC-DEMO-RECORD-2026-0001
subject: first end-to-end verification flow demonstration
provenance: generated in-repo with human-supervised validation required
audit_ref: AUDIT-HC-DEMO-2026-0001
timestamp: 2026-05-26T00:00:00Z
```

## 3) SHA-256 hash

- `4e0639d833024b68a5961362ef959d480f9ad79e1df29ee228c6f5b64bcc82f4`

## 4) How to verify the hash locally

```bash
python - <<'PY'
import hashlib
content = """HC:// demo verification payload v1
package_id: HC-DEMO-PKG-2026-0001
record_id: HC-DEMO-RECORD-2026-0001
subject: first end-to-end verification flow demonstration
provenance: generated in-repo with human-supervised validation required
audit_ref: AUDIT-HC-DEMO-2026-0001
timestamp: 2026-05-26T00:00:00Z
"""
print(hashlib.sha256(content.encode()).hexdigest())
PY
```

## 5) Expected verification result

The command should print:

```text
4e0639d833024b68a5961362ef959d480f9ad79e1df29ee228c6f5b64bcc82f4
```

This matches `records/verified/demo-record-001.json` and demonstrates a real advisory integrity/provenance check path in-repo.

## 6) QR/landing page status

QR and landing-page integration for this demo record is planned and not yet implemented as part of this scoped change.
