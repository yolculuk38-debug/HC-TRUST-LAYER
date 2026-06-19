import ast
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from hc_check_digest import SAFETY_MARKERS, build_digest, render_markdown


def test_required_safety_markers() -> None:
    digest = build_digest()

    for key, value in SAFETY_MARKERS.items():
        assert digest[key] is value


def test_all_success_allows_merge_after_human_review() -> None:
    digest = build_digest(checks=[{"name": "Validation", "status": "success"}])

    assert digest["merge_guidance"] == "merge_allowed_after_human_review"
    assert digest["blocking"] == []


def test_advisory_only_warning_requires_human_review_before_merge() -> None:
    digest = build_digest(checks=[{"name": "Signal Watch Report", "status": "warning"}])

    assert digest["merge_guidance"] == "human_review_before_merge"
    assert digest["advisory"][0]["name"] == "Signal Watch Report"


def test_failed_required_check_blocks_merge() -> None:
    digest = build_digest(checks=[{"name": "Policy Evaluation", "status": "failure"}])

    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["reason"] == "failed required check candidate"


def test_completed_required_check_with_failing_conclusion_blocks_merge() -> None:
    digest = build_digest(checks=[{"name": "Validation", "status": "completed", "conclusion": "failure"}])

    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["name"] == "Validation"


def test_unresolved_non_outdated_thread_blocks_merge() -> None:
    digest = build_digest(threads=[{"name": "Active thread", "resolved": False, "outdated": False}])

    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["reason"] == "unresolved non-outdated review thread"


def test_outdated_or_resolved_thread_does_not_block() -> None:
    digest = build_digest(
        threads=[
            {"name": "Resolved thread", "resolved": True, "outdated": False},
            {"name": "Outdated thread", "resolved": False, "outdated": True},
        ]
    )

    assert digest["merge_guidance"] == "merge_allowed_after_human_review"
    assert digest["blocking"] == []
    assert len(digest["external_review"]) == 2


def test_codex_p2_open_feedback_blocks_merge() -> None:
    digest = build_digest(reviews=[{"author": "codex", "severity": "P2", "status": "open", "title": "Codex P2"}])

    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["reason"] == "open Codex P2 feedback"


def test_bracketed_codex_p2_open_feedback_blocks_merge() -> None:
    digest = build_digest(reviews=[{"author": "codex", "title": "[P2] clarify digest parsing", "status": "open"}])

    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["reason"] == "open Codex P2 feedback"


def test_markdown_codex_p1_open_feedback_blocks_merge() -> None:
    digest = build_digest(reviews=[{"author": "codex", "body": "**P1** Badge: required failure hidden", "status": "open"}])

    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["reason"] == "open Codex P1 feedback"


def test_resolved_or_outdated_codex_p2_does_not_block() -> None:
    digest = build_digest(
        reviews=[
            {"author": "codex", "severity": "P2", "status": "resolved", "title": "Codex P2"},
            {"author": "codex", "severity": "P2", "status": "open", "outdated": True, "title": "Codex P2"},
        ]
    )

    assert digest["merge_guidance"] == "merge_allowed_after_human_review"
    assert digest["blocking"] == []


def test_markdown_contains_required_sections() -> None:
    markdown = render_markdown(build_digest())

    for section in (
        "# HC Check Digest",
        "## Safety markers",
        "## Blocking",
        "## Advisory",
        "## Automation helpers",
        "## External review",
        "## Artifacts",
        "## Merge guidance",
    ):
        assert section in markdown
    assert "none" in markdown


def test_no_network_or_github_api_behavior_exists() -> None:
    source = Path("scripts/hc_check_digest.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.append(node.module)

    forbidden_imports = {"requests", "urllib", "http.client", "socket", "aiohttp", "httpx"}
    assert forbidden_imports.isdisjoint(imports)
    assert "api.github.com" not in source
    assert "github.com" not in source.lower()


def _post_merge_smoke_path(name: str) -> Path:
    return Path("examples/hc-check-digest/post-merge-smoke") / name


def _load_json_fixture(name: str):
    import json

    return json.loads(_post_merge_smoke_path(name).read_text(encoding="utf-8"))


def test_post_merge_smoke_json_snapshot_is_stable() -> None:
    import json

    digest = build_digest(
        checks=_load_json_fixture("checks.json"),
        reviews=_load_json_fixture("reviews.json"),
        threads=_load_json_fixture("threads.json"),
        artifacts=_load_json_fixture("artifacts.json"),
    )
    actual = json.dumps(digest, indent=2, sort_keys=True) + "\n"

    assert actual == _post_merge_smoke_path("expected-hc-check-digest.json").read_text(encoding="utf-8")


def test_post_merge_smoke_markdown_snapshot_is_stable() -> None:
    digest = build_digest(
        checks=_load_json_fixture("checks.json"),
        reviews=_load_json_fixture("reviews.json"),
        threads=_load_json_fixture("threads.json"),
        artifacts=_load_json_fixture("artifacts.json"),
    )
    actual = render_markdown(digest)

    assert actual == _post_merge_smoke_path("expected-hc-check-digest.md").read_text(encoding="utf-8")


def test_post_merge_smoke_job_summary_snapshot_and_safety_text_are_stable() -> None:
    from hc_check_digest_render_summary import render_job_summary

    digest = build_digest(
        checks=_load_json_fixture("checks.json"),
        reviews=_load_json_fixture("reviews.json"),
        threads=_load_json_fixture("threads.json"),
        artifacts=_load_json_fixture("artifacts.json"),
    )
    actual = render_job_summary(digest)

    assert actual == _post_merge_smoke_path("expected-job-summary.md").read_text(encoding="utf-8")
    for safety_text in (
        "HC Check Digest is advisory-only.",
        "It does not approve, reject, label, assign, comment, or merge.",
        "Humans retain final authority.",
    ):
        assert safety_text in actual


def test_post_merge_smoke_blocking_and_nonblocking_boundaries() -> None:
    digest = build_digest(
        checks=_load_json_fixture("checks.json"),
        reviews=_load_json_fixture("reviews.json"),
        threads=_load_json_fixture("threads.json"),
        artifacts=_load_json_fixture("artifacts.json"),
    )

    assert digest["merge_guidance"] == "do_not_merge"
    assert {item["reason"] for item in digest["blocking"]} == {
        "failed required check candidate",
        "open Codex P2 feedback",
        "unresolved non-outdated review thread",
    }
    assert digest["advisory"] == [
        {"name": "Signal Watch Report", "status": "warning", "reason": "advisory check signal"}
    ]
    assert {item["name"] for item in digest["external_review"]} == {
        "[P2] Keep digest blockers visible",
        "Resolved reviewer thread",
        "Active reviewer thread",
    }
    assert digest["artifacts"] == [
        {"name": "hc-check-digest", "status": "available", "reason": "local artifact signal"}
    ]


def _repo_health_path(name: str) -> Path:
    return Path("examples/hc-check-digest/repo-health") / name


def _load_repo_health_fixture(name: str):
    import json

    return json.loads(_repo_health_path(name).read_text(encoding="utf-8"))


def test_repo_health_changelog_advisory_signal() -> None:
    digest = build_digest(repo_health=_load_repo_health_fixture("github-changelog-signals.json"))

    signal = digest["repo_health_signals"]["changelog"][0]
    assert signal["level"] == "advisory"
    assert digest["merge_guidance"] == "human_review_before_merge"
    assert digest["blocking"] == []


def test_repo_health_dependabot_update_note_is_advisory() -> None:
    digest = build_digest(repo_health=_load_repo_health_fixture("dependabot-update-notes.json"))

    signal = digest["repo_health_signals"]["dependabot"][0]
    assert signal["level"] == "advisory"
    assert digest["blocking"] == []


def test_repo_health_codeql_baseline_note_is_neutral() -> None:
    digest = build_digest(repo_health=_load_repo_health_fixture("codeql-baseline-notes.json"))

    signal = digest["repo_health_signals"]["codeql"][0]
    assert signal["level"] == "neutral/baseline"
    assert digest["merge_guidance"] == "merge_allowed_after_human_review"
    assert digest["blocking"] == []


def test_repo_health_weekly_summary_rendering_is_informational() -> None:
    digest = build_digest(repo_health=_load_repo_health_fixture("weekly-repo-health-summary.json"))
    markdown = render_markdown(digest)

    assert digest["repo_health_signals"]["weekly_summary"][0]["level"] == "informational"
    assert "### weekly_summary" in markdown
    assert "Weekly repo health summary" in markdown
    assert digest["blocking"] == []


def test_repo_health_explicit_blocker_propagates() -> None:
    digest = build_digest(
        repo_health={
            "changelog": [
                {
                    "name": "Explicit blocking changelog signal",
                    "status": "published",
                    "level": "blocking",
                    "reason": "Fixture explicitly marks this release note as blocking.",
                }
            ],
            "dependabot": [
                {
                    "name": "Explicit blocking security update",
                    "status": "open",
                    "security_blocking": True,
                    "reason": "Fixture explicitly marks this update as security blocking.",
                }
            ],
            "codeql": [
                {
                    "name": "Explicit blocking CodeQL note",
                    "status": "failed",
                    "blocking": True,
                    "reason": "Fixture explicitly marks this CodeQL note as blocking.",
                }
            ],
        }
    )

    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["summary"]["repo_health_counts"]["blocker"] == 3
    assert {item["reason"] for item in digest["blocking"]} == {
        "repo-health changelog blocker",
        "repo-health dependabot blocker",
        "repo-health codeql blocker",
    }


def test_repo_health_advisory_only_signals_do_not_block_merge_guidance() -> None:
    digest = build_digest(
        repo_health=[
            _load_repo_health_fixture("github-changelog-signals.json"),
            _load_repo_health_fixture("dependabot-update-notes.json"),
            _load_repo_health_fixture("codeql-baseline-notes.json"),
            _load_repo_health_fixture("weekly-repo-health-summary.json"),
        ]
    )

    assert digest["blocking"] == []
    assert digest["merge_guidance"] == "human_review_before_merge"
    assert digest["summary"]["repo_health_counts"] == {
        "blocker": 0,
        "advisory": 2,
        "neutral_baseline": 1,
        "informational": 1,
    }


def test_repo_health_json_snapshot_is_stable() -> None:
    import json

    digest = build_digest(
        repo_health=[
            _load_repo_health_fixture("github-changelog-signals.json"),
            _load_repo_health_fixture("dependabot-update-notes.json"),
            _load_repo_health_fixture("codeql-baseline-notes.json"),
            _load_repo_health_fixture("weekly-repo-health-summary.json"),
        ]
    )
    actual = json.dumps(digest, indent=2, sort_keys=True) + "\n"

    assert actual == _repo_health_path("expected-hc-check-digest-repo-health.json").read_text(encoding="utf-8")


def test_repo_health_markdown_snapshot_is_stable() -> None:
    digest = build_digest(
        repo_health=[
            _load_repo_health_fixture("github-changelog-signals.json"),
            _load_repo_health_fixture("dependabot-update-notes.json"),
            _load_repo_health_fixture("codeql-baseline-notes.json"),
            _load_repo_health_fixture("weekly-repo-health-summary.json"),
        ]
    )
    actual = render_markdown(digest)

    assert actual == _repo_health_path("expected-hc-check-digest-repo-health.md").read_text(encoding="utf-8")


def test_repo_health_parser_network_free_behavior_exists() -> None:
    source = Path("scripts/hc_check_digest.py").read_text(encoding="utf-8")
    assert "--repo-health" in source
    assert "requests" not in source
    assert "api.github.com" not in source


def test_repo_health_dependabot_security_true_becomes_blocker() -> None:
    digest = build_digest(
        repo_health={
            "dependabot": [
                {
                    "name": "Dependabot security update",
                    "status": "open",
                    "security": True,
                    "reason": "Fixture marks this Dependabot update as security-related.",
                }
            ]
        }
    )

    signal = digest["repo_health_signals"]["dependabot"][0]
    assert signal["level"] == "blocker"
    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"] == [
        {"name": "Dependabot security update", "status": "open", "reason": "repo-health dependabot blocker"}
    ]


def test_repo_health_dependabot_level_security_becomes_blocker() -> None:
    digest = build_digest(
        repo_health={
            "dependabot": [
                {
                    "name": "Dependabot security level update",
                    "status": "open",
                    "level": "security",
                    "reason": "Fixture marks this Dependabot update level as security.",
                }
            ]
        }
    )

    assert digest["repo_health_signals"]["dependabot"][0]["level"] == "blocker"
    assert digest["merge_guidance"] == "do_not_merge"


def test_repo_health_dependabot_severity_security_becomes_blocker() -> None:
    digest = build_digest(
        repo_health={
            "dependabot": [
                {
                    "name": "Dependabot security severity update",
                    "status": "open",
                    "severity": "SECURITY",
                    "reason": "Fixture marks this Dependabot update severity as security.",
                }
            ]
        }
    )

    assert digest["repo_health_signals"]["dependabot"][0]["level"] == "blocker"
    assert digest["merge_guidance"] == "do_not_merge"


def test_repo_health_dependabot_category_and_type_security_become_blockers() -> None:
    digest = build_digest(
        repo_health={
            "dependabot": [
                {
                    "name": "Dependabot security category update",
                    "status": "open",
                    "category": "security",
                },
                {
                    "name": "Dependabot security type update",
                    "status": "open",
                    "type": "security",
                },
                {
                    "name": "Dependabot blocking severity update",
                    "status": "open",
                    "severity": "blocking",
                },
            ]
        }
    )

    assert [signal["level"] for signal in digest["repo_health_signals"]["dependabot"]] == [
        "blocker",
        "blocker",
        "blocker",
    ]
    assert digest["summary"]["repo_health_counts"]["blocker"] == 3
    assert digest["merge_guidance"] == "do_not_merge"


def test_repo_health_dependabot_normal_advisory_update_remains_non_blocking() -> None:
    digest = build_digest(repo_health=_load_repo_health_fixture("dependabot-update-notes.json"))

    assert digest["repo_health_signals"]["dependabot"][0]["level"] == "advisory"
    assert digest["blocking"] == []
    assert digest["merge_guidance"] == "human_review_before_merge"
