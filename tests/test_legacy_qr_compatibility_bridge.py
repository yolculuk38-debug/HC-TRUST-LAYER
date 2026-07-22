import importlib.util
from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
_CANONICAL_ARTIFACTS_SPEC = importlib.util.spec_from_file_location(
    "check_canonical_artifacts", ROOT / "scripts" / "check_canonical_artifacts.py"
)
assert _CANONICAL_ARTIFACTS_SPEC is not None
assert _CANONICAL_ARTIFACTS_SPEC.loader is not None
canonical_artifacts = importlib.util.module_from_spec(_CANONICAL_ARTIFACTS_SPEC)
_CANONICAL_ARTIFACTS_SPEC.loader.exec_module(canonical_artifacts)
RECORD_ID = "HC-TEST-2026-0001"
BRIDGE_PATH = ROOT / "records" / "verified" / f"{RECORD_ID}.md"
ARCHIVED_PATH = ROOT / "records" / "archived" / f"{RECORD_ID}.md"
MANIFEST_PATH = ROOT / "hash" / f"{RECORD_ID}.sha256"
AUTO_HASH_WORKFLOW_PATH = ROOT / ".github" / "workflows" / "auto-hash.yml"


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

    assert digest == "10a252de2f70d8890bc71007c21194a0023f1e3322ef1c127f599966ad3499c5"
    assert relative_path == "records/archived/HC-TEST-2026-0001.md"
    assert sha256(ARCHIVED_PATH.read_bytes()).hexdigest() == digest


def test_bridge_is_not_the_canonical_hash_target() -> None:
    digest, relative_path = _manifest_entry()

    assert relative_path != "records/verified/HC-TEST-2026-0001.md"
    assert sha256(BRIDGE_PATH.read_bytes()).hexdigest() != digest


def test_auto_hash_workflow_skips_legacy_bridge_before_writing_manifest() -> None:
    workflow = AUTO_HASH_WORKFLOW_PATH.read_text(encoding="utf-8")
    skip_check = 'if [ "$file" = "records/verified/HC-TEST-2026-0001.md" ]; then'
    hash_write = 'sha256sum "$file" > "hash/${filename}.sha256"'

    assert skip_check in workflow
    assert "Skipping legacy QR compatibility bridge: $file" in workflow
    assert workflow.index(skip_check) < workflow.index(hash_write)
    assert "records/archived/HC-TEST-2026-0001.md" in MANIFEST_PATH.read_text(encoding="utf-8")


def test_canonical_guard_skips_only_exact_legacy_bridge_exception(capsys) -> None:
    exact_bridge = Path("records/verified/HC-TEST-2026-0001.md")
    adjacent_verified_record = Path("records/verified/HC-TEST-2026-0002.md")
    archived_record = Path("records/archived/HC-TEST-2026-0001.md")

    assert canonical_artifacts.is_legacy_qr_bridge_exception(exact_bridge) is True
    assert canonical_artifacts.is_legacy_qr_bridge_exception(adjacent_verified_record) is False
    assert canonical_artifacts.is_legacy_qr_bridge_exception(archived_record) is False

    assert canonical_artifacts.main() == 0
    output = capsys.readouterr().out
    assert "SKIP: records/verified/HC-TEST-2026-0001.md (explicitly non-canonical legacy QR compatibility bridge)" in output
    assert "CANONICAL: records/verified/HC-TEST-2026-0001.md" not in output
