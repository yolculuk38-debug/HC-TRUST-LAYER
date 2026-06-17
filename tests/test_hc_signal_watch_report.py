import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "hc_signal_watch_report.py"


def _module():
    spec = importlib.util.spec_from_file_location("hc_signal_watch_report", SCRIPT)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["hc_signal_watch_report"] = module
    spec.loader.exec_module(module)
    return module


def test_signal_watch_report_is_report_only() -> None:
    module = _module()

    report = module.build_report(ROOT)

    assert report["advisory_only"] is True
    assert report["public_safe"] is True
    assert report["truth_guarantee"] is False
    assert report["human_review_required"] is True
    assert report["network_access"] is False
    assert report["repository_mutation"] is False
    assert report["approval_authority"] is False
    assert report["merge_authority"] is False


def test_signal_watch_report_confirms_local_policy_links() -> None:
    module = _module()

    report = module.build_report(ROOT)

    assert report["policy"]["present"] is True
    assert report["policy"]["requires_repo_wide_pr_search"] is True
    assert report["policy"]["requires_annotation_review"] is True
    assert report["policy"]["requires_community_signal_review"] is True
    assert report["active_work_registry"]["links_policy"] is True


def test_signal_watch_report_confirms_dependabot_config() -> None:
    module = _module()

    report = module.build_report(ROOT)

    assert report["dependabot"]["present"] is True
    assert report["dependabot"]["github_actions_weekly"] is True
    assert report["dependabot"]["pip_weekly"] is True
    assert report["dependabot"]["github_actions_grouped"] is True


def test_signal_watch_classifies_operator_supplied_signals(tmp_path: Path) -> None:
    module = _module()
    signal_file = tmp_path / "signals.json"
    signal_file.write_text(
        json.dumps(
            [
                {
                    "source": "GitHub Changelog",
                    "title": "Actions runtime deprecation notice for Node",
                    "url": "https://example.invalid/actions-node",
                },
                {
                    "source": "GitHub Home",
                    "title": "First external star on the repository",
                },
                {
                    "source": "GitHub Changelog",
                    "title": "Unrelated UI theme update",
                },
            ]
        ),
        encoding="utf-8",
    )

    report = module.build_report(ROOT, signal_file)

    assert [finding["impact"] for finding in report["signals"]] == ["workflow", "community", "none"]
    assert report["signals"][0]["recommended_action"] == "inspect workflow action versions and warnings"
    assert report["signals"][1]["recommended_action"] == "inspect onboarding and public safety language"
    assert report["signals"][2]["evidence_gap"] == "no HC-relevant keyword matched this signal"


def test_signal_watch_markdown_keeps_safety_markers() -> None:
    module = _module()

    markdown = module.render_markdown(module.build_report(ROOT))

    assert "advisory_only=true" in markdown
    assert "public_safe=true" in markdown
    assert "truth_guarantee=false" in markdown
    assert "human_review_required=true" in markdown
    assert "repository_mutation=false" in markdown
    assert "merge_authority=false" in markdown
