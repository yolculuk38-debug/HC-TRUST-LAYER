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


@pytest.mark.parametrize("legacy_text", [
    '{"created_at":"invalid"}',
    '{"record_id":"one","record_id":"two"}',
])
def test_bad_legacy_archive_record_fails_even_with_valid_pending_record(tmp_path, legacy_text):
    write_record(tmp_path, json.dumps(fixture_record()))
    legacy = tmp_path / "records/archive/legacy.json"
    legacy.parent.mkdir(parents=True)
    legacy.write_text(legacy_text, encoding="utf-8")
    assert main(["validate-records", str(tmp_path / "records")]) == 1


def test_valid_legacy_archive_record_is_selected(tmp_path, capsys):
    legacy = tmp_path / "records/archive/legacy.json"
    legacy.parent.mkdir(parents=True)
    legacy.write_text(json.dumps(fixture_record()), encoding="utf-8")
    assert main(["validate-records", str(tmp_path / "records")]) == 0
    assert "1 passed, 0 failed" in capsys.readouterr().out


@pytest.mark.parametrize("word", ["INDEX", "MANIFEST", "CACHE", "EXPORT", "GENERATED"])
def test_artifact_words_inside_record_names_cannot_bypass_validation(tmp_path, word):
    from validator import validate_record as legacy_validate_record

    write_record(tmp_path, json.dumps(fixture_record()))
    bad = tmp_path / "records/pending" / f"HC-{word}-2026-0001.json"
    record = {**fixture_record(), "created_at": "invalid"}
    bad.write_text(json.dumps(record), encoding="utf-8")
    assert main(["validate-records", str(tmp_path / "records")]) == 1
    assert legacy_validate_record(bad) is False


def test_generated_directory_is_excluded_precisely(tmp_path):
    write_record(tmp_path, json.dumps(fixture_record()))
    artifact = tmp_path / "records/pending/generated/data.json"
    artifact.parent.mkdir()
    artifact.write_text("not a record", encoding="utf-8")
    assert main(["validate-records", str(tmp_path / "records")]) == 0


@pytest.mark.parametrize("kind", ["index", "manifest", "cache", "export", "generated"])
@pytest.mark.parametrize("prefix", ["", "HC-EXAMPLE-2026-0001-", "HC-EXAMPLE-2026-0001_"])
def test_reserved_artifact_names_are_excluded_across_clis(tmp_path, capsys, kind, prefix):
    from hc_trust.verification import find_record_files
    from validator import validate_record as legacy_validate_record

    canonical = write_record(tmp_path, json.dumps(fixture_record()))
    artifact = canonical.parent / f"{prefix}{kind}.json"
    # Neither invalid JSON nor record-shaped content may turn an artifact into
    # canonical evidence. The hash CLI shares the same file-selection boundary.
    for content in ("not json", json.dumps(fixture_record())):
        artifact.write_text(content, encoding="utf-8")
        selected, skipped = find_record_files(tmp_path / "records")
        assert selected == [canonical]
        assert artifact in skipped
        assert main(["validate-records", str(tmp_path / "records")]) == 0
        assert "1 passed, 0 failed" in capsys.readouterr().out
        assert main(["verify", str(tmp_path / "records")]) == 0
        assert "1 passed, 0 failed" in capsys.readouterr().out
        assert legacy_validate_record(artifact) is True
        assert "SKIPPED ARTIFACT" in capsys.readouterr().out


def test_artifact_only_selection_is_not_schema_validation_success(tmp_path):
    artifact = tmp_path / "records/pending/HC-EXAMPLE-2026-0001-INDEX.json"
    artifact.parent.mkdir(parents=True)
    artifact.write_text(json.dumps(fixture_record()), encoding="utf-8")
    assert main(["validate-records", str(tmp_path / "records")]) == 1


@pytest.mark.parametrize("ancestor", ["records/cache/project", "cache/project", "export/project", "records/unrelated/project"])
@pytest.mark.parametrize("command", ["verify", "validate-records"])
def test_checkout_ancestor_names_do_not_hide_real_records(tmp_path, capsys, ancestor, command):
    root = tmp_path / ancestor
    valid = write_record(root, json.dumps(fixture_record()))
    assert main([command, str(root / "records")]) == 0
    assert "1 passed, 0 failed" in capsys.readouterr().out
    bad = valid.with_name("broken.json")
    bad.write_text('{"created_at":"invalid"}', encoding="utf-8")
    assert main([command, str(root / "records")]) == 1
    assert "1 passed, 1 failed" in capsys.readouterr().out
    from validator import validate_record as legacy_validate_record
    assert legacy_validate_record(bad) is False


@pytest.mark.parametrize("command", ["verify", "validate-records"])
def test_ambiguous_tree_requires_explicit_root(tmp_path, capsys, command):
    root = tmp_path / "records/pending/project"
    valid = write_record(root, json.dumps(fixture_record()))
    assert main([command, str(root / "records")]) == 1
    assert "specify --repo-root" in capsys.readouterr().out
    assert main([command, str(valid), "--repo-root", str(root)]) == 0
    # Relative paths and the default records path belong to the explicit root.
    assert main([command, "records", "--repo-root", str(root)]) == 0
    assert main([command, "--repo-root", str(root)]) == 0
    from validator import validate_record as legacy_validate_record
    assert legacy_validate_record(valid) is False
    assert legacy_validate_record("records/pending/sample.json", repo_root=root) is True


@pytest.mark.parametrize("command", ["verify", "validate-records"])
def test_nested_generated_records_tree_cannot_reset_artifact_context(tmp_path, command):
    root = tmp_path / "project"
    write_record(root, json.dumps(fixture_record()))
    nested = root / "records/pending/generated/records"
    nested_record = nested / "pending/sample.json"
    nested_record.parent.mkdir(parents=True)
    nested_record.write_text(json.dumps(fixture_record()), encoding="utf-8")
    assert main([command, str(nested)]) == 1
    assert main([command, str(nested), "--repo-root", str(root)]) == 1
    from hc_trust.verification import find_record_files
    selected, skipped = find_record_files(root / "records", repo_root=root)
    assert selected == [root / "records/pending/sample.json"]
    assert nested_record in skipped


@pytest.mark.parametrize("command", ["verify", "validate-records"])
@pytest.mark.parametrize("kind", ["empty", "missing", "artifact"])
def test_hash_and_schema_commands_require_a_checked_record(tmp_path, command, kind):
    root = tmp_path / "project"
    target = root / "records/pending"
    target.mkdir(parents=True)
    if kind == "missing":
        target = root / "absent"
    elif kind == "artifact":
        (target / "generated_index.json").write_text(json.dumps(fixture_record()), encoding="utf-8")
    assert main([command, str(target), "--repo-root", str(root)]) == 1


@pytest.mark.parametrize("kind", ["outside_file", "other_group", "artifact_target", "group_directory", "records_directory"])
def test_canonical_selection_rejects_symlink_escapes(tmp_path, kind):
    from hc_trust.verification import find_record_files
    from validator import validate_record as legacy_validate_record

    root = tmp_path / "project"
    record = write_record(root, json.dumps(fixture_record()))
    if kind in {"outside_file", "other_group", "artifact_target"}:
        target = {
            "outside_file": tmp_path / "outside.json",
            "other_group": root / "records/verified/target.json",
            "artifact_target": record.parent / "generated/target.json",
        }[kind]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(fixture_record()), encoding="utf-8")
        record.unlink()
        record.symlink_to(target)
    else:
        directory = record.parent if kind == "group_directory" else root / "records"
        destination = tmp_path / "moved"
        directory.rename(destination)
        directory.symlink_to(destination, target_is_directory=True)
    selected, skipped = find_record_files(record, repo_root=root)
    assert selected == []
    assert record in skipped
    for command in ("verify", "validate-records"):
        assert main([command, str(record), "--repo-root", str(root)]) == 1
    # Artifact targets may retain the legacy explicit skip diagnostic, but a
    # canonical directory/file escape must never return legacy validation success.
    if kind != "artifact_target":
        assert legacy_validate_record(record, repo_root=root) is False


def test_in_group_symlink_is_checked_but_artifact_alias_is_excluded(tmp_path):
    from hc_trust.verification import find_record_files
    root = tmp_path / "project"
    record = write_record(root, json.dumps(fixture_record()))
    alias = record.parent / "alias.json"
    alias.symlink_to(record)
    artifact_alias = record.parent / "cache.json"
    artifact_alias.symlink_to(record)
    selected, skipped = find_record_files(root / "records", repo_root=root)
    assert set(selected) == {record, alias}
    assert skipped == [artifact_alias]


def test_legacy_generic_file_does_not_skip_arbitrary_ancestors(tmp_path):
    from validator import validate_record as legacy_validate_record
    root = tmp_path / "records/cache/export/project"
    root.mkdir(parents=True)
    record = root / "standalone.json"
    record.write_text('{"created_at":"invalid"}', encoding="utf-8")
    assert legacy_validate_record(record) is False
    record.write_text(json.dumps(fixture_record()), encoding="utf-8")
    assert legacy_validate_record(record) is True
    assert legacy_validate_record(record, repo_root=root) is False


def test_explicit_root_does_not_admit_another_repository(tmp_path):
    from hc_trust.verification import should_validate_record_file
    intended = tmp_path / "intended"
    intended.mkdir()
    other = write_record(tmp_path / "other", json.dumps(fixture_record()))
    assert not should_validate_record_file(other, repo_root=intended)
    for command in ("verify", "validate-records"):
        assert main([command, str(other), "--repo-root", str(intended)]) == 1


def test_legacy_script_accepts_explicit_root_from_another_directory(tmp_path):
    import os
    import subprocess
    import sys
    root = tmp_path / "records/pending/project"
    write_record(root, json.dumps(fixture_record()))
    result = subprocess.run(
        [sys.executable, str(ROOT / "src/validator.py"), "records/pending/sample.json", "--repo-root", str(root)],
        cwd=tmp_path, env={**os.environ, "PYTHONPATH": str(ROOT / "src")},
        capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "VALID RECORD" in result.stdout
