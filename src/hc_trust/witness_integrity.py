from hashlib import sha256
from typing import Dict


WITNESS_ENGINE_VERSION = "hc-witness-integrity-v1-experimental"


REQUIRED_FIELDS = {
    "witness_id",
    "record_id",
    "decision",
    "timestamp",
}


def canonicalize_witness_payload(payload: Dict) -> str:
    if not isinstance(payload, dict):
        raise ValueError("payload must be a dictionary")

    normalized = []

    for key in sorted(payload.keys()):
        normalized.append(f"{key}={payload[key]}")

    return "|".join(normalized)


def build_witness_digest(payload: Dict) -> str:
    canonical = canonicalize_witness_payload(payload)
    return sha256(canonical.encode("utf-8")).hexdigest()


def build_witness_package(payload: Dict) -> Dict:
    missing = REQUIRED_FIELDS.difference(payload.keys())

    if missing:
        raise ValueError(f"missing required fields: {sorted(missing)}")

    canonical = canonicalize_witness_payload(payload)
    digest = build_witness_digest(payload)

    return {
        "engine": WITNESS_ENGINE_VERSION,
        "canonical_payload": canonical,
        "witness_digest": digest,
        "payload": payload,
        "experimental": True,
    }


def verify_witness_package(package: Dict) -> bool:
    if not isinstance(package, dict):
        return False

    payload = package.get("payload")
    digest = package.get("witness_digest")

    if not isinstance(payload, dict):
        return False

    if not isinstance(digest, str):
        return False

    calculated = build_witness_digest(payload)
    return calculated == digest
