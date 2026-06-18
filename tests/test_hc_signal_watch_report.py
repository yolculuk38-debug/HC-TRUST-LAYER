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
    assert "issue_comment_automation=false" in markdown
    assert "label_reviewer_mutation=false" in markdown
    assert "merge_authority=false" in markdown


def test_signal_watch_imports_changelog_fixture_signals_json(tmp_path: Path) -> None:
    module = _module()
    fixture = ROOT / "examples" / "hc-signal-watch" / "github-changelog-signals-fixture.json"
    ingest_script = ROOT / "scripts" / "hc_signal_watch_rss_ingest.py"
    spec = importlib.util.spec_from_file_location("hc_signal_watch_rss_ingest_for_report", ingest_script)
    assert spec is not None
    assert spec.loader is not None
    ingest = importlib.util.module_from_spec(spec)
    sys.modules["hc_signal_watch_rss_ingest_for_report"] = ingest
    spec.loader.exec_module(ingest)

    payload_path = tmp_path / "github-changelog-normalized.json"
    payload_path.write_text(
        json.dumps(ingest.normalize_entries(ingest.load_fixture(fixture))),
        encoding="utf-8",
    )

    report = module.build_report(ROOT, changelog_signals_file=payload_path)

    signals = report["github_changelog_fixture_signals"]
    assert len(signals) == 2
    assert signals[0]["source"] == "GitHub Changelog fixture"
    assert signals[0]["title"] == "Secret scanning update"
    assert signals[0]["url"] == "https://example.invalid/github-changelog/secret-scanning"
    assert signals[0]["published"] == "2026-06-16T12:00:00Z"
    assert signals[0]["category"] == "security"
    assert signals[0]["impact"] == "security"
    assert signals[0]["risk"] == "high"
    assert signals[0]["recommended_action"] == "inspect advisory security signal interpretation"
    assert signals[0]["classification_reason"] == "code scanning, secret scanning, or supply-chain signal"
    assert signals[0]["matched_keywords"] == ["secret scanning"]
    assert signals[0]["evidence_gap"] is None
    assert signals[0]["automation_boundary"] == "advisory-only; no issue/comment automation, labels, reviewers, approval, or merge"
    assert signals[0]["dedupe_key"] == "url:https://example.invalid/github-changelog/secret-scanning"


def test_signal_watch_markdown_includes_changelog_fixture_section(tmp_path: Path) -> None:
    module = _module()
    payload = {
        "mode": "local_fixture_only",
        "network_access": False,
        "signals": [
            {
                "source": "GitHub Changelog fixture",
                "title": "GitHub Actions runner update",
                "impact": "workflow",
                "risk": "medium",
                "recommended_action": "inspect workflow action versions and warnings",
                "matched_keywords": ["actions", "runner"],
                "automation_boundary": "advisory-only; no issue/comment automation, labels, reviewers, approval, or merge",
                "dedupe_key": "url:https://example.invalid/actions-runner",
            }
        ],
    }
    payload_path = tmp_path / "changelog-signals.json"
    payload_path.write_text(json.dumps(payload), encoding="utf-8")

    markdown = module.render_markdown(module.build_report(ROOT, changelog_signals_file=payload_path))

    assert "## GitHub Changelog fixture signals" in markdown
    assert "### GitHub Actions runner update" in markdown
    assert "- matched_keywords: actions, runner" in markdown
    assert "- dedupe_key: url:https://example.invalid/actions-runner" in markdown


def test_signal_watch_missing_changelog_input_keeps_current_behavior() -> None:
    module = _module()

    report = module.build_report(ROOT)

    assert report["github_changelog_fixture_signals"] == []
    assert report["signals"] == []
    assert "No signal JSON was supplied" in report["evidence_gaps"][0]


def test_signal_watch_changelog_signal_file_fails_safely(tmp_path: Path) -> None:
    module = _module()
    malformed = tmp_path / "malformed.json"
    malformed.write_text("not json", encoding="utf-8")

    try:
        module.build_report(ROOT, changelog_signals_file=malformed)
    except ValueError as exc:
        assert "changelog signal file is not valid JSON" in str(exc)
    else:
        raise AssertionError("malformed changelog signal file should fail safely")

    missing = tmp_path / "missing.json"
    try:
        module.build_report(ROOT, changelog_signals_file=missing)
    except ValueError as exc:
        assert "changelog signal file not found" in str(exc)
    else:
        raise AssertionError("missing changelog signal file should fail safely")
