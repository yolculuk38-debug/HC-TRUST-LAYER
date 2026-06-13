import json

from scripts.hc_trust_engineer_report import build_report, main


def test_report_is_public_safe_and_advisory_for_clean_fixture():
    report = build_report(
        {
            "repository": "yolculuk38-debug/HC-TRUST-LAYER",
            "event_type": "pull_request",
            "target_number": 871,
            "base_sha": "base",
            "head_sha": "head",
            "open_prs": [871],
            "changed_files": ["docs/demo/example.md"],
            "checks": [{"name": "tests", "status": "completed", "conclusion": "success"}],
            "unresolved_threads": [],
            "missing_evidence": [],
        }
    ).to_dict()

    assert report["agent"] == "HC Trust Engineer"
    assert report["mode"] == "report_only"
    assert report["advisory_only"] is True
    assert report["public_safe"] is True
    assert report["truth_guarantee"] is False
    assert report["recommended_next_action"] == "continue"
    assert report["stop_reasons"] == []
    assert report["required_human_review"] is False
    assert report["evidence_source"] == "local fixture and changed file path metadata only"


def test_protected_path_stops_and_requires_human_review():
    report = build_report(
        {
            "open_prs": [1],
            "changed_files": ["schema/record-v1.schema.json"],
            "checks": [{"name": "tests", "status": "completed", "conclusion": "success"}],
        }
    ).to_dict()

    assert report["recommended_next_action"] == "stop"
    assert report["required_human_review"] is True
    assert "protected_paths_touched" in report["stop_reasons"]
    assert report["scan"]["protected_paths_touched"] == ["schema/record-v1.schema.json"]
    assert "schema-compatibility-review" in report["risk_flags"]


def test_pending_checks_unresolved_threads_and_missing_evidence_stop():
    report = build_report(
        {
            "open_prs": [2],
            "changed_files": ["docs/demo/example.md"],
            "checks": [{"name": "tests", "status": "in_progress", "conclusion": None}],
            "unresolved_threads": ["thread-1"],
            "missing_evidence": ["test output"],
        }
    ).to_dict()

    assert report["recommended_next_action"] == "stop"
    assert report["required_human_review"] is True
    assert report["stop_reasons"] == [
        "checks_pending",
        "missing_evidence",
        "unresolved_review_threads",
    ]


def test_failed_check_and_multiple_open_prs_stop():
    report = build_report(
        {
            "open_prs": [3, 4],
            "changed_files": ["docs/demo/example.md"],
            "checks": [{"name": "tests", "status": "completed", "conclusion": "failure"}],
        }
    ).to_dict()

    assert report["recommended_next_action"] == "stop"
    assert report["stop_reasons"] == ["checks_failed", "multiple_open_prs"]


def test_cli_outputs_deterministic_json(tmp_path, capsys):
    fixture = tmp_path / "fixture.json"
    fixture.write_text(
        json.dumps(
            {
                "repository": "yolculuk38-debug/HC-TRUST-LAYER",
                "event_type": "pull_request",
                "target_number": 10,
                "open_prs": [10],
                "changed_files": ["pyproject.toml"],
                "checks": [
                    {"name": "tests", "status": "completed", "conclusion": "success"}
                ],
            }
        ),
        encoding="utf-8",
    )

    exit_code = main([str(fixture)])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["agent"] == "HC Trust Engineer"
    assert payload["mode"] == "report_only"
    assert payload["advisory_only"] is True
    assert payload["truth_guarantee"] is False
    assert payload["recommended_next_action"] == "stop"
    assert payload["stop_reasons"] == ["version_alignment_review_required"]
    assert payload["scan"]["version_alignment_paths_touched"] == ["pyproject.toml"]
