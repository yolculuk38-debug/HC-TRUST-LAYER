import json

from scripts.hc_task_handoff_issue import build_issue_handoff, issue_body_to_fixture, main


ISSUE_BODY = """### Task title

Add focused project-control note

### Goal

Create one small note for the project-control area.

### Allowed path scope

docs/project-control/example-note.md

### Blocked scope

schema/**
validators/**
records/**

### Evidence required

Changed files list
CI/check status
Advisory boundary confirmation

### Validation expected

PR checks should run normally.
No protected path changes expected.

### Handoff package

_No response_
"""


MARKDOWN_LIST_ISSUE_BODY = """### Task title

- Add protected-path review note

### Goal

- Confirm that markdown list markers do not hide protected paths.

### Allowed path scope

- schema/record-v1.schema.json
* validators/public_validator.py
+ docs/project-control/example-note.md
1. records/example.json
2) generated/example.json
- [ ] signatures/example.sig
- [x] federation/example.json

### Blocked scope

- schema/**
- validators/**
- records/**

### Evidence required

- Changed files list
- CI/check status
- Advisory boundary confirmation

### Validation expected

- PR checks should run normally.
- Protected path changes must remain visible to the handoff gate.

### Handoff package

_No response_
"""


EXPECTED_MARKDOWN_LIST_PATHS = {
    "schema/record-v1.schema.json",
    "validators/public_validator.py",
    "docs/project-control/example-note.md",
    "records/example.json",
    "generated/example.json",
    "signatures/example.sig",
    "federation/example.json",
}


def test_issue_body_to_fixture_extracts_core_fields():
    fixture = issue_body_to_fixture(ISSUE_BODY)

    assert fixture["task_title"] == "Add focused project-control note"
    assert fixture["goal"] == "Create one small note for the project-control area."
    assert fixture["changed_files"] == ["docs/project-control/example-note.md"]
    assert fixture["blocked_scope"] == ["schema/**", "validators/**", "records/**"]
    assert fixture["evidence_required"] == [
        "Changed files list",
        "CI/check status",
        "Advisory boundary confirmation",
    ]
    assert fixture["validation_expected"] == [
        "PR checks should run normally.",
        "No protected path changes expected.",
    ]
    assert fixture["open_prs"] == []
    assert fixture["unresolved_review_comments"] == []
    assert fixture["checks"] == []


def test_issue_body_to_fixture_strips_common_markdown_list_markers():
    fixture = issue_body_to_fixture(MARKDOWN_LIST_ISSUE_BODY)

    assert fixture["task_title"] == "Add protected-path review note"
    assert fixture["goal"] == "Confirm that markdown list markers do not hide protected paths."
    assert fixture["changed_files"] == [
        "schema/record-v1.schema.json",
        "validators/public_validator.py",
        "docs/project-control/example-note.md",
        "records/example.json",
        "generated/example.json",
        "signatures/example.sig",
        "federation/example.json",
    ]
    assert fixture["blocked_scope"] == ["schema/**", "validators/**", "records/**"]
    assert fixture["evidence_required"] == [
        "Changed files list",
        "CI/check status",
        "Advisory boundary confirmation",
    ]
    assert fixture["validation_expected"] == [
        "PR checks should run normally.",
        "Protected path changes must remain visible to the handoff gate.",
    ]


def test_markdown_list_paths_reach_protected_path_handoff_gate():
    payload = build_issue_handoff(MARKDOWN_LIST_ISSUE_BODY)

    plan = payload["handoff"]["plan"]
    assert set(plan["planned_prs"][0]["expected_files"]) == EXPECTED_MARKDOWN_LIST_PATHS
    assert plan["merge_gate"]["allowed"] is False
    assert plan["merge_gate"]["human_review_required"] is True
    assert any(
        "Protected path touched" in condition and "schema/record-v1.schema.json" in condition
        for condition in plan["stop_conditions"]
    )


def test_issue_body_handoff_is_advisory_and_does_not_invoke_external_agent():
    payload = build_issue_handoff(ISSUE_BODY)

    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert payload["fixture"]["task_title"] == "Add focused project-control note"
    assert payload["handoff"]["invokes_external_agent"] is False
    assert payload["handoff"]["creates_pull_request"] is False
    assert payload["handoff"]["requires_human_submit"] is True
    assert payload["handoff"]["merge_gate"]["allowed"] is False


def test_issue_body_to_fixture_uses_safe_default_title_for_missing_title():
    fixture = issue_body_to_fixture("### Goal\n\nOnly goal provided")

    assert fixture["task_title"] == "Untitled HC task handoff"
    assert fixture["goal"] == "Only goal provided"


def test_issue_parser_cli_outputs_handoff_json(tmp_path, capsys):
    issue_file = tmp_path / "issue.md"
    issue_file.write_text(ISSUE_BODY, encoding="utf-8")

    exit_code = main([str(issue_file)])
    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["advisory_only"] is True
    assert payload["fixture"]["task_title"] == "Add focused project-control note"
    assert payload["handoff"]["invokes_external_agent"] is False


def test_issue_parser_cli_outputs_fixture_only_json(tmp_path, capsys):
    issue_file = tmp_path / "issue.md"
    issue_file.write_text(ISSUE_BODY, encoding="utf-8")

    exit_code = main([str(issue_file), "--fixture-only"])
    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["task_title"] == "Add focused project-control note"
    assert payload["changed_files"] == ["docs/project-control/example-note.md"]
