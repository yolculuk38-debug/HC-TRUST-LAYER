import hashlib
import json
import sys
from pathlib import Path
from urllib.parse import quote, urlencode
import qrcode

HC_TRUST_LAYER_BASE_URL = "https://yolculuk38-debug.github.io/HC-TRUST-LAYER"
DEMO_RECORD_ID = "HC-DEMO2026-0001"
DEMO_VERIFICATION_URL = f"{HC_TRUST_LAYER_BASE_URL}/docs/verify.html"

# Advisory v0.1.0 route placeholder for non-demo QR generation.
# This intentionally avoids the demo-only docs/verify.html page, which only
# checks the first demo record and would report arbitrary records as mismatches.
# The route shape is a review/navigation target, not a claim that a live
# arbitrary-record verifier is implemented.
ADVISORY_RECORD_VERIFICATION_BASE_URL = f"{HC_TRUST_LAYER_BASE_URL}/verify"


def generate_signature(record_id, content_hash, archive_ref):
    raw = f"{record_id}:{content_hash}:{archive_ref}"
    return hashlib.sha256(raw.encode()).hexdigest()


def generate_qr(record_id, content_hash, archive_ref, output_dir="qr"):
    Path(output_dir).mkdir(exist_ok=True)
    signature = generate_signature(record_id, content_hash, archive_ref)
    query = urlencode(
        {
            "record": record_id,
            "hash": content_hash,
            "ref": archive_ref,
            "sig": signature,
        }
    )
    if record_id == DEMO_RECORD_ID:
        verification_url = f"{DEMO_VERIFICATION_URL}?{query}"
    else:
        quoted_record_id = quote(record_id, safe="")
        verification_url = (
            f"{ADVISORY_RECORD_VERIFICATION_BASE_URL}/{quoted_record_id}?{query}"
        )
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(verification_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    output_path = Path(output_dir) / f"{record_id}.png"
    img.save(output_path)
    return str(output_path), verification_url


def find_verified_records(records_dir="records"):
    records = []
    for path in sorted(Path(records_dir).rglob("*.json")):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"❌ Hata: {path} okunamadı ({exc})", file=sys.stderr)
            return None

        if str(data.get("verification_status", "")).lower() != "verified":
            continue

        record_id = data.get("record_id") or data.get("id")
        content_hash = data.get("content_hash")
        archive_ref = data.get("archive_ref")
        if not (record_id and content_hash and archive_ref):
            print(f"❌ Hata: {path} gerekli alanları içermiyor", file=sys.stderr)
            return None

        records.append((record_id, content_hash, archive_ref, path))
    return records
