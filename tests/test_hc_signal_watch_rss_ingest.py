import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "hc_signal_watch_rss_ingest.py"


def _module():
    spec = importlib.util.spec_from_file_location("hc_signal_watch_rss_ingest", SCRIPT)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["hc_signal_watch_rss_ingest"] = module
    spec.loader.exec_module(module)
    return module


def test_xml_fixture_normalizes_and_classifies_without_live_network() -> None:
    module = _module()
    fixture = ROOT / "examples" / "hc-signal-watch" / "github-changelog-rss-fixture.xml"

    payload = module.normalize_entries(module.load_fixture(fixture))

    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert payload["network_access"] is False
    assert payload["issue_comment_automation"] is False
    assert payload["label_reviewer_mutation"] is False
    assert payload["approval_authority"] is False
    assert payload["merge_authority"] is False
    assert [signal["impact"] for signal in payload["signals"]] == ["workflow", "none"]
    assert (
        payload["signals"][0]["recommended_action"]
        == "inspect workflow action versions and warnings"
    )
    assert (
        payload["signals"][1]["evidence_gap"]
        == "fixture entry did not include an HC-relevant category or keyword"
    )


def test_json_fixture_deduplicates_by_url() -> None:
    module = _module()
    fixture = ROOT / "examples" / "hc-signal-watch" / "github-changelog-signals-fixture.json"

    payload = module.normalize_entries(module.load_fixture(fixture))

    assert len(payload["signals"]) == 2
    assert [signal["impact"] for signal in payload["signals"]] == ["security", "dependency"]
    assert payload["signals"][0]["impact"] == "security"
    assert payload["signals"][0]["risk"] == "high"
    assert payload["duplicates_suppressed"] == [
        {
            "title": "Secret scanning update duplicate",
            "dedupe_key": "url:https://example.invalid/github-changelog/secret-scanning",
            "url": "https://example.invalid/github-changelog/secret-scanning",
        }
    ]


def test_cli_outputs_fixture_only_json(tmp_path: Path, capsys) -> None:
    module = _module()
    fixture = tmp_path / "github-changelog.json"
    fixture.write_text(
        json.dumps(
            [
                {
                    "title": "Dependabot pip update",
                    "url": "https://example.invalid/dependabot",
                }
            ]
        ),
        encoding="utf-8",
    )

    exit_code = module.main([str(fixture)])
    output = json.loads(capsys.readouterr().out)

    assert exit_code == 0
    assert output["mode"] == "local_fixture_only"
    assert output["repository_mutation"] is False
    assert output["signals"][0]["impact"] == "dependency"


def test_keyword_matching_uses_token_and_phrase_boundaries() -> None:
    module = _module()

    payload = module.normalize_entries(
        [
            module.FeedEntry(
                source="GitHub Changelog fixture",
                title="Repository preview availability improvements",
                url="https://example.invalid/preview-availability",
                summary="Public preview availability update for repository insights",
            )
        ]
    )

    assert payload["signals"][0]["impact"] == "none"
    assert payload["signals"][0]["matched_keywords"] == []


def test_classification_prefers_highest_risk_keyword_group() -> None:
    module = _module()

    payload = module.normalize_entries(
        [
            module.FeedEntry(
                source="GitHub Changelog fixture",
                title="Secret scanning for GitHub Actions",
                url="https://example.invalid/secret-scanning-actions",
            ),
            module.FeedEntry(
                source="GitHub Changelog fixture",
                title="GitHub Actions security advisory",
                url="https://example.invalid/actions-security-advisory",
            ),
        ]
    )

    assert [signal["impact"] for signal in payload["signals"]] == ["security", "security"]
    assert [signal["risk"] for signal in payload["signals"]] == ["high", "high"]
    assert payload["signals"][0]["matched_keywords"] == ["secret scanning"]
    assert payload["signals"][1]["matched_keywords"] == ["security advisory"]
