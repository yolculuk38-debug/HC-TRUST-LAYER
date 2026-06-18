import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from hc_check_digest import build_digest
from hc_check_digest_github_adapter import normalize_check_runs, normalize_reviews


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
            "url": "https://github.example/checks/1",
        }
    ]
    digest = build_digest(checks=checks)
    assert digest["merge_guidance"] == "do_not_merge"
    assert digest["blocking"][0]["name"] == "Validation"


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
