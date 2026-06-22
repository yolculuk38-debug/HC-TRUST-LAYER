from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import hc_signal_watch_live_rss_fetch as live

RSS = """<?xml version=\"1.0\"?>
<rss><channel>
  <item>
    <title>GitHub Actions runner deprecation notice</title>
    <link>https://github.blog/changelog/example-actions</link>
    <pubDate>Mon, 01 Jun 2026 00:00:00 +0000</pubDate>
    <category>actions</category>
    <description>Actions runner image change for workflow operators.</description>
    <guid>actions-1</guid>
  </item>
  <item>
    <title>New profile decoration</title>
    <link>https://github.blog/changelog/example-profile</link>
    <guid>profile-1</guid>
  </item>
</channel></rss>
"""

RSS_WITH_TITLE_ONLY_ITEMS = """<?xml version=\"1.0\"?>
<rss><channel>
  <item>
    <title>First title-only operator signal</title>
  </item>
  <item>
    <title>Second title-only operator signal</title>
  </item>
</channel></rss>
"""


def test_parse_rss_classifies_actions_and_no_action():
    payload = {**live.SAFETY_MARKERS, **live.normalize_entries(live.parse_rss(RSS, live.DEFAULT_RSS_URL))}
    signals = payload["signals"]

    assert signals[0]["impact"] == "workflow"
    assert signals[0]["risk"] == "medium"
    assert signals[1]["impact"] == "none"
    assert signals[1]["recommended_action"] == "record as no action unless repository operations are affected"


def test_title_only_items_without_guid_or_link_remain_distinct():
    payload = {
        **live.SAFETY_MARKERS,
        **live.normalize_entries(live.parse_rss(RSS_WITH_TITLE_ONLY_ITEMS, live.DEFAULT_RSS_URL)),
    }

    assert [signal["title"] for signal in payload["signals"]] == [
        "First title-only operator signal",
        "Second title-only operator signal",
    ]
    assert payload["duplicates_suppressed"] == []


def test_timeout_error_is_safe_failure(monkeypatch):
    monkeypatch.setattr(live, "fetch_rss", lambda url, timeout: live.FetchResult(ok=False, error="timeout while fetching RSS"))

    payload = live.build_payload(live.DEFAULT_RSS_URL, 0.01)

    assert payload["fetch_status"] == "error"
    assert payload["safe_failure"] is True
    assert payload["signals"] == []
    assert payload["repository_mutation"] is False
    assert payload["issue_comment_automation"] is False


def test_safety_markers_and_no_repository_mutation(monkeypatch):
    monkeypatch.setattr(live, "fetch_rss", lambda url, timeout: live.FetchResult(ok=True, xml_text=RSS))

    payload = live.build_payload(live.DEFAULT_RSS_URL, 10)
    markdown = live.render_markdown(payload)

    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert payload["human_review_required"] is True
    assert payload["repository_mutation"] is False
    assert payload["issue_comment_automation"] is False
    assert payload["label_reviewer_mutation"] is False
    assert payload["approval_authority"] is False
    assert payload["merge_authority"] is False
    for marker in (
        "advisory_only=true",
        "public_safe=true",
        "truth_guarantee=false",
        "human_review_required=true",
        "repository_mutation=false",
        "issue_comment_automation=false",
        "label_reviewer_mutation=false",
        "approval_authority=false",
        "merge_authority=false",
    ):
        assert marker in markdown


def test_workflow_is_manual_only_and_read_only():
    workflow = (ROOT / ".github/workflows/hc-signal-watch-live-rss-dry-run.yml").read_text(encoding="utf-8")

    assert "workflow_dispatch:" in workflow
    assert "schedule:" not in workflow
    assert "pull_request:" not in workflow
    assert "issues: write" not in workflow
    assert "pull-requests: write" not in workflow
    assert "contents: write" not in workflow
    assert "permissions:\n  contents: read" in workflow
    assert "actions/upload-artifact@v7" in workflow
    assert "hc-signal-watch-live-rss-dry-run.json" in workflow
    assert "hc-signal-watch-live-rss-dry-run.md" in workflow
    assert "GITHUB_STEP_SUMMARY" in workflow
    assert "Full dry-run report" in workflow
    assert "Safe failure: Markdown report artifact is missing or empty" in workflow
    assert "recommended_action" in workflow
    forbidden = ("gh issue", "gh pr comment", "gh pr review", "gh pr merge", "actions/github-script", "add-labels", "request-reviewers")
    for token in forbidden:
        assert token not in workflow
