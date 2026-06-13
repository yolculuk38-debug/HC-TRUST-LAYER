import json

from scripts.hc_source_inventory import build_source_inventory, main


def test_build_source_inventory_classifies_repository_python_roots(tmp_path):
    (tmp_path / "src/hc_trust").mkdir(parents=True)
    (tmp_path / "src/hc_runtime/routes").mkdir(parents=True)
    (tmp_path / "src/security").mkdir(parents=True)
    (tmp_path / "scripts").mkdir()
    (tmp_path / "tests").mkdir()

    (tmp_path / "src/hc_trust/verification_package.py").write_text("", encoding="utf-8")
    (tmp_path / "src/hc_runtime/routes/health.py").write_text("", encoding="utf-8")
    (tmp_path / "src/security/audit.py").write_text("", encoding="utf-8")
    (tmp_path / "scripts/hc_control_bot.py").write_text("", encoding="utf-8")
    (tmp_path / "tests/test_example.py").write_text("", encoding="utf-8")

    report = build_source_inventory(tmp_path).to_dict()
    by_path = {entry["path"]: entry for entry in report["files"]}

    assert report["advisory_only"] is True
    assert report["public_safe"] is True
    assert report["truth_guarantee"] is False
    assert report["inventory_only"] is True
    assert report["modifies_repository"] is False
    assert report["python_file_count"] == 5
    assert by_path["src/hc_trust/verification_package.py"]["category"] == "trust_layer_implementation"
    assert by_path["src/hc_runtime/routes/health.py"]["category"] == "runtime_implementation"
    assert by_path["src/security/audit.py"]["category"] == "security_adjacent"
    assert by_path["scripts/hc_control_bot.py"]["category"] == "operator_support"
    assert by_path["tests/test_example.py"]["category"] == "test_support"
    assert "security_adjacent_review_recommended" in by_path["src/security/audit.py"]["notes"]


def test_main_prints_json_inventory_without_modifying_files(tmp_path, capsys):
    (tmp_path / "src").mkdir()
    source = tmp_path / "src/example.py"
    source.write_text("print('example')\n", encoding="utf-8")

    exit_code = main([str(tmp_path), "--root", "src"])
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 0
    assert payload["python_file_count"] == 1
    assert payload["files"] == [
        {
            "path": "src/example.py",
            "category": "source_implementation",
            "status": "inventory_only",
            "notes": [],
        }
    ]
    assert source.read_text(encoding="utf-8") == "print('example')\n"
