"""CI and local CLI must enforce the runtime's strict record contract."""
import json
from pathlib import Path

import pytest

from hc_trust.cli import main

ROOT = Path(__file__).resolve().parents[1]


def fixture_record():
    path = ROOT / "records/pending/HC-EXAMPLE-2026-0001.json"
    return json.loads(path.read_text(encoding="utf-8"))


def write_record(tmp_path, text):
    path = tmp_path / "records" / "pending" / "sample.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def test_valid_record_and_generated_artifact_exclusion(tmp_path, capsys):
    path = write_record(tmp_path, json.dumps(fixture_record()))
    (path.parent / "generated_index.json").write_text("not json", encoding="utf-8")
    assert main(["validate-records", str(tmp_path / "records")]) == 0
    assert "1 passed, 0 failed" in capsys.readouterr().out


@pytest.mark.parametrize("change", [
    {"created_at": "not-a-date"}, {"created_at": "2026-02-30T12:00:00Z"},
    {"schema_version": "unknown"},
])
def test_format_and_version_fail_the_ci_command(tmp_path, change):
    record = {**fixture_record(), **change}
    path = write_record(tmp_path, json.dumps(record))
    assert main(["validate-records", str(path)]) == 1


def test_duplicate_json_fields_fail_the_ci_command(tmp_path):
    text = json.dumps(fixture_record())
    text = '{"created_at":"2026-01-01T00:00:00Z",' + text[1:]
    path = write_record(tmp_path, text)
    assert main(["validate-records", str(path)]) == 1


def test_missing_content_fails_the_ci_command(tmp_path):
    record = fixture_record()
    del record["content"]
    assert main(["validate-records", str(write_record(tmp_path, json.dumps(record)))]) == 1


def test_empty_or_missing_record_set_fails(tmp_path):
    assert main(["validate-records", str(tmp_path)]) == 1
    assert main(["validate-records", str(tmp_path / "missing")]) == 1
