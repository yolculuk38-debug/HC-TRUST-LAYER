from __future__ import annotations

import importlib.util
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
EVALUATE_POLICY_PATH = REPO_ROOT / "scripts" / "evaluate_policy.py"

spec = importlib.util.spec_from_file_location("evaluate_policy_script", EVALUATE_POLICY_PATH)
evaluate_policy_script = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(evaluate_policy_script)


def test_signal_watch_paths_are_classified() -> None:
    rules = evaluate_policy_script.load_path_risk_rules(REPO_ROOT / "policy" / "hc-policy-v1.yml")

    paths = [
        "scripts/hc_signal_watch_report.py",
        "scripts/hc_signal_watch_rss_ingest.py",
        "tests/test_hc_signal_watch_report.py",
        "tests/test_hc_signal_watch_rss_ingest.py",
    ]

    for path in paths:
        assert evaluate_policy_script.match_risk(path, rules) != "unknown"
