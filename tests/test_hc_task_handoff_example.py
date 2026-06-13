import json
from pathlib import Path

from scripts.hc_task_handoff import build_handoff


def test_example_handoff_fixture_builds_safe_package():
    fixture_path = Path("examples/hc-task-handoff/docs-note-task.json")
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))

    package = build_handoff(fixture).to_dict()

    assert package["advisory_only"] is True
    assert package["public_safe"] is True
    assert package["truth_guarantee"] is False
    assert package["invokes_external_agent"] is False
    assert package["creates_pull_request"] is False
    assert package["requires_human_submit"] is True
    assert package["task_title"] == "Add focused project-control note"
    assert package["merge_gate"]["allowed"] is True
    assert package["stop_conditions"] == []
    assert "HC Trust Engineer task handoff package." in package["handoff_prompt_lines"]
    assert any("Expected files: docs/project-control/example-note.md" == line for line in package["handoff_prompt_lines"])
