from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORD_ID = "HC-TEST-2026-0001"
BRIDGE_PATH = ROOT / "records" / "verified" / f"{RECORD_ID}.md"
ARCHIVED_PATH = ROOT / "records" / "archived" / f"{RECORD_ID}.md"
MANIFEST_PATH = ROOT / "hash" / f"{RECORD_ID}.sha256"


def _manifest_entry() -> tuple[str, str]:
    digest, relative_path = MANIFEST_PATH.read_text(encoding="utf-8").strip().split(maxsplit=1)
    return digest, relative_path


def test_legacy_verified_path_is_advisory_bridge_to_archived_record() -> None:
    bridge = BRIDGE_PATH.read_text(encoding="utf-8")

    assert "Legacy QR Compatibility Bridge" in bridge
    assert "records/archived/HC-TEST-2026-0001.md" in bridge
    assert "Authority: advisory-only" in bridge
    assert "Public-safe: true" in bridge
    assert "Truth guarantee: false" in bridge
    assert "Human review: required" in bridge
    assert "Status: VERIFIED" not in bridge
    assert "Initial Humanity Chain verification test record" not in bridge


def test_hash_manifest_keeps_the_archived_record_as_its_target() -> None:
    digest, relative_path = _manifest_entry()

    assert relative_path == "records/archived/HC-TEST-2026-0001.md"
    assert sha256(ARCHIVED_PATH.read_bytes()).hexdigest() == digest


def test_bridge_is_not_the_canonical_hash_target() -> None:
    digest, relative_path = _manifest_entry()

    assert relative_path != "records/verified/HC-TEST-2026-0001.md"
    assert sha256(BRIDGE_PATH.read_bytes()).hexdigest() != digest
