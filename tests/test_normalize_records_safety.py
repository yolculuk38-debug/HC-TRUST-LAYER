import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "src" / "normalize_records.py"
SPEC = importlib.util.spec_from_file_location("normalize_records", MODULE_PATH)
normalize_records = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(normalize_records)


def test_normalize_record_dry_run_reports_without_writing(tmp_path, capsys):
    record = tmp_path / "records" / "pending" / "HC-TEST.json"
    record.parent.mkdir(parents=True)
    original = '{"b": 2, "a": 1}\n'
    record.write_text(original, encoding="utf-8")

    changed = normalize_records.normalize_record(record, dry_run=True, write=False)

    assert changed is True
    assert record.read_text(encoding="utf-8") == original
    output = capsys.readouterr().out
    assert "[DRY-RUN]" in output
    assert "Proposed changes" in output


def test_normalize_record_requires_explicit_write(tmp_path, capsys):
    record = tmp_path / "records" / "pending" / "HC-TEST.json"
    record.parent.mkdir(parents=True)
    original = '{"b": 2, "a": 1}\n'
    record.write_text(original, encoding="utf-8")

    changed = normalize_records.normalize_record(record, dry_run=False, write=False)

    assert changed is True
    assert record.read_text(encoding="utf-8") == original
    assert "Use --write" in capsys.readouterr().out


def test_normalize_record_does_not_overwrite_protected_records_even_with_write(tmp_path, capsys):
    record = tmp_path / "records" / "archive" / "HC-ARCHIVE.json"
    record.parent.mkdir(parents=True)
    original = '{"b": 2, "a": 1}\n'
    record.write_text(original, encoding="utf-8")

    changed = normalize_records.normalize_record(record, dry_run=False, write=True)

    assert changed is True
    assert record.read_text(encoding="utf-8") == original
    assert "Protected record not overwritten" in capsys.readouterr().out


def test_normalize_record_writes_only_when_explicitly_allowed_for_writable_record(tmp_path):
    record = tmp_path / "records" / "pending" / "HC-WRITE.json"
    record.parent.mkdir(parents=True)
    record.write_text('{"b": 2, "a": 1}\n', encoding="utf-8")

    changed = normalize_records.normalize_record(record, dry_run=False, write=True)

    assert changed is True
    assert record.read_text(encoding="utf-8") == '{\n  "a": 1,\n  "b": 2\n}\n'
