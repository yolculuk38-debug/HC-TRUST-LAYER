"""HC:// signed witness layer.

This module provides deterministic witness signing and verification helpers.
Signatures are verification signals, not automatic authority.
"""

from __future__ import annotations

import hashlib
import hmac
import json
from typing import Any


SIGNATURE_VERSION = "HC-SIG-V1"


def canonical_json(data: dict[str, Any]) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def build_witness_payload(record_id: str, witness_id: str, verdict: str, content_hash: str) -> dict[str, str]:
    return {
        "record_id": record_id,
        "witness_id": witness_id,
        "verdict": verdict.upper(),
        "content_hash": content_hash,
    }


def sign_witness(payload: dict[str, Any], secret_key: str) -> dict[str, Any]:
    canonical = canonical_json(payload)
    signature = hmac.new(secret_key.encode("utf-8"), canonical.encode("utf-8"), hashlib.sha256).hexdigest()

    return {
        "signature_version": SIGNATURE_VERSION,
        "payload": payload,
        "signature": signature,
    }


def verify_witness_signature(signed_payload: dict[str, Any], secret_key: str) -> dict[str, Any]:
    if not isinstance(signed_payload, dict):
        return {"verified": False, "reason": "invalid signed payload"}

    payload = signed_payload.get("payload")
    signature = signed_payload.get("signature")
    version = signed_payload.get("signature_version")

    if not payload or not signature:
        return {"verified": False, "reason": "missing payload or signature"}

    if version != SIGNATURE_VERSION:
        return {"verified": False, "reason": "unsupported signature version"}

    canonical = canonical_json(payload)
    expected_signature = hmac.new(
        secret_key.encode("utf-8"),
        canonical.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    verified = hmac.compare_digest(signature, expected_signature)

    return {
        "verified": verified,
        "reason": "signature valid" if verified else "signature mismatch",
    }


__all__ = [
    "SIGNATURE_VERSION",
    "build_witness_payload",
    "sign_witness",
    "verify_witness_signature",
]
