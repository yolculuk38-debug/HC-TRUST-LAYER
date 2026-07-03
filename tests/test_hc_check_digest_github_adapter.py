import json
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from hc_check_digest import build_digest
from hc_check_digest_github_adapter import (
    fetch_github_inputs,
    fetch_pr_number_for_sha,
    normalize_check_runs,
    normalize_review_threads,
    normalize_reviews,
)


class FakeHeaders:
    def __init__(self, link: str | None = None) -> None:
        self.link = link

    def get(self, key: str) -> str | None:
        if key.lower() == "link":
            return self.link
        return None


class FakeResponse:
    def __init__(self, payload: object, link: str | None = None) -> None:
        self.payload = payload
        self.headers = FakeHeaders(link)

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        return None

    def read(self) -> bytes:
        return json.dumps(self.payload).encode("utf-8")


def test_adapter_normalizes_completed_failure_check_run_for_digest_blocker() -> None:
    checks = normalize_check_runs(
        {
            "check_runs": [
                {
                    "name": "Validation",
                    "status": "completed",
                    "conclusion": "failure",
                    "html_url": "https://github.example/checks/1",
                }
            ]
        }
    )

    assert checks == [
        {
            "name": "Validation",
            "status": "completed",
            "conclusion": "failure",
            "workflow": "",
            "summary": "",
            "text": "",
            "url": "https://github.example/checks/1",
        }
    ]
    digest = build_digest(checks=checks)
    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["name"] == "Validation"



def test_adapter_preserves_check_run_output_summary_for_stale_action_proposal() -> None:
    checks = normalize_check_runs(
        {
            "check_runs": [
                {
                    "name": "Action runtime report",
                    "status": "completed",
                    "conclusion": "success",
                    "output": {
                        "summary": "Node.js 20 deprecation notice for repository-controlled actions.",
                        "text": "Audit action versions before a scoped maintenance PR.",
                    },
                    "html_url": "https://github.example/checks/2",
                }
            ]
        }
    )

    assert checks[0]["summary"] == "Node.js 20 deprecation notice for repository-controlled actions."
    assert checks[0]["text"] == "Audit action versions before a scoped maintenance PR."
    digest = build_digest(checks=checks)
    assert digest["project_control_proposals"]
    assert digest["project_control_proposals"][0]["repository_mutation"] is False
    assert digest["repository_mutation"] is False
    assert digest["approval_authority"] is False
    assert digest["merge_authority"] is False
    assert digest["merge_guidance"] == "merge_allowed_after_human_review"

def test_adapter_preserves_codex_p2_review_text_for_digest_blocker() -> None:
    reviews = normalize_reviews(
        [
            {
                "user": {"login": "codex"},
                "state": "COMMENTED",
                "body": "[P2] Keep HC Check Digest workflow advisory-only.",
                "html_url": "https://github.example/review/1",
            }
        ]
    )

    assert reviews[0]["author"] == "codex"
    assert reviews[0]["title"] == "[P2] Keep HC Check Digest workflow advisory-only."
    digest = build_digest(reviews=reviews)
    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["reason"] == "open Codex P2 feedback"


def test_rest_review_comment_without_thread_state_is_non_blocking_external_review() -> None:
    reviews = normalize_reviews(
        {
            "comments": [
                {
                    "user": {"login": "reviewer"},
                    "body": "Please consider clarifying this wording.",
                    "html_url": "https://github.example/comment/1",
                }
            ]
        }
    )
    threads = normalize_review_threads(
        {
            "comments": [
                {
                    "user": {"login": "reviewer"},
                    "body": "This REST comment has no resolved thread state.",
                }
            ]
        }
    )

    digest = build_digest(reviews=reviews, threads=threads)
    assert threads == []
    assert digest["merge_guidance"] == "merge_allowed_after_human_review"
    assert digest["external_review"][0]["name"].startswith("PR review by reviewer")


def test_true_unresolved_non_outdated_thread_still_blocks() -> None:
    threads = normalize_review_threads(
        {
            "threads": [
                {
                    "user": {"login": "reviewer"},
                    "body": "Real unresolved thread",
                    "isResolved": False,
                    "isOutdated": False,
                }
            ]
        }
    )

    digest = build_digest(threads=threads)
    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["reason"] == "unresolved non-outdated review thread"


def test_resolved_or_outdated_true_thread_does_not_block() -> None:
    threads = normalize_review_threads(
        {
            "threads": [
                {"body": "Resolved thread", "isResolved": True, "isOutdated": False},
                {"body": "Outdated thread", "isResolved": False, "isOutdated": True},
            ]
        }
    )

    digest = build_digest(threads=threads)
    assert digest["merge_guidance"] == "merge_allowed_after_human_review"
    assert digest["blocking"] == []


def test_fetch_github_inputs_follows_pagination_for_failed_required_check() -> None:
    responses = [
        FakeResponse(
            {"check_runs": [{"name": "Validation", "status": "completed", "conclusion": "success"}]},
            '<https://api.github.com/page2>; rel="next"',
        ),
        FakeResponse({"check_runs": [{"name": "Policy Evaluation", "status": "completed", "conclusion": "failure"}]}),
        FakeResponse({"workflow_runs": []}),
        FakeResponse({"reviews": []}),
        FakeResponse({"comments": []}),
        FakeResponse({"data": {"repository": {"pullRequest": {"reviewThreads": {"nodes": [], "pageInfo": {"hasNextPage": False}}}}}}),
        FakeResponse({"artifacts": []}),
    ]

    def fake_urlopen(request: object, timeout: int = 30) -> FakeResponse:
        return responses.pop(0)

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        checks, reviews, threads, artifacts = fetch_github_inputs("owner/repo", "1066", "abc123", "token")

    digest = build_digest(checks=checks, reviews=reviews, threads=threads, artifacts=artifacts)
    assert responses == []
    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["name"] == "Policy Evaluation"


def test_fetch_github_inputs_follows_pagination_for_codex_p2_review() -> None:
    responses = [
        FakeResponse({"check_runs": []}),
        FakeResponse({"workflow_runs": []}),
        FakeResponse({"reviews": [{"user": {"login": "human"}, "state": "COMMENTED", "body": "Looks scoped."}]}, '<https://api.github.com/page2>; rel="next"'),
        FakeResponse({"reviews": [{"user": {"login": "codex"}, "state": "COMMENTED", "body": "[P2] Address refresh behavior."}]}),
        FakeResponse({"comments": []}),
        FakeResponse({"data": {"repository": {"pullRequest": {"reviewThreads": {"nodes": [], "pageInfo": {"hasNextPage": False}}}}}}),
        FakeResponse({"artifacts": []}),
    ]

    def fake_urlopen(request: object, timeout: int = 30) -> FakeResponse:
        return responses.pop(0)

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        checks, reviews, threads, artifacts = fetch_github_inputs("owner/repo", "1066", "abc123", "token")

    digest = build_digest(checks=checks, reviews=reviews, threads=threads, artifacts=artifacts)
    assert responses == []
    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["reason"] == "open Codex P2 feedback"


def test_fetch_pr_number_for_sha_uses_paginated_commit_pull_lookup() -> None:
    responses = [
        FakeResponse({"pulls": []}, '<https://api.github.com/page2>; rel="next"'),
        FakeResponse({"pulls": [{"number": 1066}]}),
    ]

    def fake_urlopen(request: object, timeout: int = 30) -> FakeResponse:
        return responses.pop(0)

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        pr_number = fetch_pr_number_for_sha("owner/repo", "abc123", "token")

    assert responses == []
    assert pr_number == "1066"
