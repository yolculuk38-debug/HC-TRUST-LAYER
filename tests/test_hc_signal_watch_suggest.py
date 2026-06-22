import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "hc_signal_watch_suggest.py"


def _module():
    spec = importlib.util.spec_from_file_location("hc_signal_watch_suggest", SCRIPT)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["hc_signal_watch_suggest"] = module
    spec.loader.exec_module(module)
    return module


def _report(actions):
    return {"report_name": "HC GitHub Signal Watch", "recommended_human_actions": actions}


def test_p1_p2_become_issue_suggestions() -> None:
    module = _module()

    payload = module.build_suggestions(
        _report(
            [
                {
                    "priority": "P1",
                    "source": "GitHub Changelog fixture",
                    "reason": "security signal needs review",
                    "recommended_action": "inspect advisory security signal interpretation",
                    "human_review_required": True,
                    "automation_boundary": "advisory-only",
                },
                {
                    "priority": "P2",
                    "source": "GitHub Changelog fixture",
                    "reason": "workflow signal needs review",
                    "recommended_action": "inspect workflow action versions and warnings",
                    "human_review_required": True,
                    "automation_boundary": "advisory-only",
                },
            ]
        )
    )

    assert [suggestion["suggested_type"] for suggestion in payload["suggestions"]] == ["issue", "issue"]
    assert [suggestion["priority"] for suggestion in payload["suggestions"]] == ["P1", "P2"]


def test_p3_community_review_becomes_issue_when_action_is_real() -> None:
    module = _module()

    payload = module.build_suggestions(
        _report(
            [
                {
                    "priority": "P3",
                    "source": "GitHub Home",
                    "reason": "operator signal classified as low risk with community impact",
                    "recommended_action": "inspect onboarding and public safety language",
                    "human_review_required": True,
                    "automation_boundary": "advisory-only",
                }
            ]
        )
    )

    assert payload["suggestions"][0]["suggested_type"] == "issue"
    assert payload["suggestions"][0]["recommended_action"] == "inspect onboarding and public safety language"


def test_no_action_remains_no_action() -> None:
    module = _module()

    payload = module.build_suggestions(
        _report(
            [
                {
                    "priority": "P4",
                    "source": "GitHub Changelog",
                    "reason": "no HC-relevant keyword matched this signal",
                    "recommended_action": "no-action",
                    "human_review_required": True,
                    "automation_boundary": "advisory-only",
                }
            ]
        )
    )

    assert payload["suggestions"][0]["suggested_type"] == "no_action"


def test_report_generated_no_action_text_remains_no_action() -> None:
    module = _module()

    payload = module.build_suggestions(
        _report(
            [
                {
                    "priority": "P3",
                    "source": "GitHub Changelog",
                    "reason": "no HC-relevant keyword matched this signal",
                    "recommended_action": "record as no action unless repository operations are affected",
                    "human_review_required": True,
                    "automation_boundary": "advisory-only",
                }
            ]
        )
    )

    assert payload["suggestions"][0]["suggested_type"] == "no_action"
    assert "No action suggested" in payload["suggestions"][0]["title"]


def test_empty_report_produces_no_suggestions() -> None:
    module = _module()

    payload = module.build_suggestions(_report([]))
    markdown = module.render_markdown(payload)

    assert payload["suggestions"] == []
    assert "No dry-run suggestions were generated" in markdown


def test_malformed_json_fails_safely(tmp_path: Path) -> None:
    malformed = tmp_path / "malformed.json"
    malformed.write_text("not json", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(malformed), "--format", "json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode != 0
    assert "Signal Watch report file is not valid JSON" in result.stderr
    assert result.stdout == ""


def test_output_keeps_all_safety_markers() -> None:
    module = _module()

    payload = module.build_suggestions(
        _report(
            [
                {
                    "priority": "P1",
                    "source": "GitHub Changelog fixture",
                    "reason": "security signal needs review",
                    "recommended_action": "inspect advisory security signal interpretation",
                    "human_review_required": True,
                    "automation_boundary": "advisory-only",
                }
            ]
        )
    )
    markdown = module.render_markdown(payload)

    for key, value in module.SAFETY_MARKERS.items():
        assert payload[key] is value
        assert payload["suggestions"][0][key] is value
        assert f"{key}={module._markdown_bool(value)}" in markdown


def test_script_has_no_github_api_network_or_mutation_behavior() -> None:
    source = SCRIPT.read_text(encoding="utf-8")

    forbidden_fragments = [
        "import requests",
        "from requests",
        "import urllib.request",
        "from urllib",
        "import http.client",
        "api.github.com",
        "PyGithub",
        "Github(",
        "subprocess.run",
        "git push",
        "gh issue create",
        "gh pr create",
        "gh api",
        "create_issue",
        "create_pull",
        "request_reviewers",
        "add_to_labels",
        "create_comment",
        "merge(",
    ]
    for fragment in forbidden_fragments:
        assert fragment not in source

    payload = _module().build_suggestions(_report([]))
    assert payload["network_access"] is False
    assert payload["repository_mutation"] is False
    assert payload["issue_comment_automation"] is False
    assert payload["label_reviewer_mutation"] is False
    assert payload["approval_authority"] is False
    assert payload["merge_authority"] is False
