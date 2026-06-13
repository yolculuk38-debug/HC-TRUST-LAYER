import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from normalize_records import is_protected_record, normalize_record


def test_archive_path_is_protected() -> None:
    assert is_protected_record(Path("records/archive/example.json"))


def test_archived_path_is_protected() -> None:
    assert is_protected_record(Path("records/archived/example.json"))


def test_verified_path_is_protected() -> None:
    assert is_protected_record(Path("records/verified/example.json"))


def test_live_path_is_not_protected() -> None:
    assert not is_protected_record(Path("records/live/example.json"))


def test_archived_record_not_overwritten_when_write_enabled(tmp_path: Path) -> None:
    record_path = tmp_path / "records" / "archived" / "example.json"
    record_path.parent.mkdir(parents=True)
    original = '{"z":2,"a":1}\n'
    record_path.write_text(original, encoding="utf-8")

    changed = normalize_record(record_path, dry_run=False, write=True)

    assert changed is True
    assert record_path.read_text(encoding="utf-8") == original
