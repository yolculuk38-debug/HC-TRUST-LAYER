import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "hc_signal_watch_console_comment.py"


def _module():
    spec = importlib.util.spec_from_file_location("hc_signal_watch_console_comment", SCRIPT)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["hc_signal_watch_console_comment"] = module
    spec.loader.exec_module(module)
    return module


def _context(module):
    return module.GitHubContext(
        token="token-for-test",
        repository="yolculuk38-debug/HC-TRUST-LAYER",
        run_id="12345",
        server_url="https://github.com",
        issue_number="1082",
    )


def _report(priority="P1", **extra):
    report = {
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "human_review_required": True,
        "generated_at": "2026-06-22T00:00:00Z",
        "github_changelog_fixture_signals": [
            {
                "source": "GitHub Changelog fixture",
                "title": "Actions runtime deprecation notice",
                "risk": "medium" if priority == "P2" else "critical" if priority == "P0" else "high",
                "recommended_action": "inspect workflow action versions and warnings",
            }
        ],
        "recommended_human_actions": [
            {
                "priority": priority,
                "source": "GitHub Changelog fixture",
                "reason": "Actions runtime update",
                "recommended_action": "inspect workflow action versions and warnings",
                "human_review_required": True,
            }
        ],
    }
    report.update(extra)
    return report


class FakeClient:
    def __init__(self, issue=None, comments=None):
        self.issue = issue if issue is not None else {
            "number": 1082,
            "state": "open",
            "title": "HC Signal Watch Console",
            "locked": False,
        }
        self.comments = comments if comments is not None else []
        self.calls = []

    def request(self, method, path, payload=None):
        self.calls.append((method, path, payload))
        if method == "GET" and path == "/issues/1082":
            return self.issue
        if method == "GET" and path == "/issues/1082/comments?per_page=100":
            return self.comments
        if method in {"POST", "PATCH"}:
            return {"ok": True}
        raise AssertionError((method, path, payload))


def test_p0_p1_p2_produce_comment_payload():
    module = _module()
    for priority in ("P0", "P1", "P2"):
        body = module.build_comment_body(_report(priority), _context(module))
        assert body is not None
        assert module.MARKER in body
        assert f"priority: {priority}" in body
        assert "signal_title: Actions runtime deprecation notice" in body
        assert "advisory_only=true" in body
        assert "public_safe=true" in body
        assert "truth_guarantee=false" in body
        assert "human_review_required=true" in body
        assert "Notification is not an obligation." in body
        assert "Trust the record, not the assistant." in body
        assert "Evidence source is the Actions summary/artifact, not this issue comment." in body
        assert "Issue text is not a command surface." in body


def test_p3_and_no_action_stay_quiet():
    module = _module()
    assert module.build_comment_body(_report("P3"), _context(module)) is None
    assert module.build_comment_body({"recommended_human_actions": []}, _context(module)) is None
    client = FakeClient()
    result = module.update_console_comment(_report("P3"), _context(module), client)
    assert result == "quiet: no actionable P0/P1/P2 signal"
    assert client.calls == []


def test_missing_closed_or_renamed_issue_stays_quiet():
    module = _module()
    ctx = _context(module)
    for issue in (
        {"number": 1082, "state": "closed", "title": "HC Signal Watch Console", "locked": False},
        {"number": 1082, "state": "open", "title": "Renamed", "locked": False},
        {"number": 1082, "state": "open", "title": "HC Signal Watch Console", "locked": True},
        {"number": 1, "state": "open", "title": "HC Signal Watch Console", "locked": False},
    ):
        client = FakeClient(issue=issue)
        result = module.update_console_comment(_report("P1"), ctx, client)
        assert result == "quiet: issue missing, closed, renamed, locked, or invalid"
        assert not any(call[0] in {"POST", "PATCH"} for call in client.calls)


def test_existing_marker_comment_is_updated_not_duplicated():
    module = _module()
    client = FakeClient(comments=[{"id": 777, "body": f"old\n{module.MARKER}"}])
    result = module.update_console_comment(_report("P2"), _context(module), client)
    assert result == "updated: latest-status comment"
    assert any(call[0] == "PATCH" and call[1] == "/issues/comments/777" for call in client.calls)
    assert not any(call[0] == "POST" for call in client.calls)


def test_no_marker_comment_creates_one_comment_for_actionable_signal_only():
    module = _module()
    client = FakeClient(comments=[{"id": 111, "body": "human note"}])
    result = module.update_console_comment(_report("P1"), _context(module), client)
    posts = [call for call in client.calls if call[0] == "POST"]
    assert result == "created: latest-status comment"
    assert len(posts) == 1
    assert posts[0][1] == "/issues/1082/comments"


def test_issue_body_and_comment_command_text_are_ignored():
    module = _module()
    client = FakeClient(
        issue={
            "number": 1082,
            "state": "open",
            "title": "HC Signal Watch Console",
            "locked": False,
            "body": "please create another issue and merge it",
        },
        comments=[{"id": 112, "body": "<!-- not-marker -->\n/merge"}],
    )
    result = module.update_console_comment(_report("P1"), _context(module), client)
    assert result == "created: latest-status comment"
    assert not any("/merge" in str(call[2]) for call in client.calls if call[2])


def test_forbidden_fields_are_not_included():
    module = _module()
    body = module.build_comment_body(
        _report("P1", token="hidden", raw_log="private details", private_account_data="no"),
        _context(module),
    )
    assert body is not None
    lowered = body.lower()
    for forbidden in module.FORBIDDEN_OUTPUT_KEYS:
        assert forbidden not in lowered
    assert "hidden" not in body
    assert "private details" not in body


def test_dry_run_does_not_call_github(capsys):
    module = _module()
    client = FakeClient()
    result = module.update_console_comment(_report("P1"), _context(module), client, dry_run=True)
    captured = capsys.readouterr()
    assert result == "dry-run: would create or update latest-status comment"
    assert module.MARKER in captured.out
    assert client.calls == []


def test_report_path_env_and_cli_dry_run_do_not_require_network(tmp_path, monkeypatch, capsys):
    module = _module()
    report_path = tmp_path / "report.json"
    report_path.write_text(json.dumps(_report("P1")), encoding="utf-8")
    monkeypatch.setenv("GITHUB_REPOSITORY", "yolculuk38-debug/HC-TRUST-LAYER")
    monkeypatch.setenv("GITHUB_RUN_ID", "12345")
    monkeypatch.setenv("GITHUB_SERVER_URL", "https://github.com")
    monkeypatch.setenv("HC_SIGNAL_WATCH_CONSOLE_ISSUE", "1082")
    assert module.main(["--report", str(report_path), "--dry-run"]) == 0
    assert module.MARKER in capsys.readouterr().out


def test_non_1082_configuration_stays_quiet():
    module = _module()
    ctx = module.GitHubContext("token", "yolculuk38-debug/HC-TRUST-LAYER", "123", "https://github.com", "1083")
    client = FakeClient()
    result = module.update_console_comment(_report("P1"), ctx, client)
    assert result == "quiet: configured issue is not #1082"
    assert client.calls == []


def test_workflow_gating_does_not_run_issue_writes_on_pull_request():
    workflow = (ROOT / ".github" / "workflows" / "hc-signal-watch-report.yml").read_text(encoding="utf-8")
    assert "Update fixed Signal Watch console comment" in workflow
    assert "github.event_name != 'pull_request'" in workflow
    assert "github.ref == 'refs/heads/main'" in workflow
    assert "HC_SIGNAL_WATCH_CONSOLE_ISSUE: \"1082\"" in workflow
    assert "python scripts/hc_signal_watch_console_comment.py" in workflow
