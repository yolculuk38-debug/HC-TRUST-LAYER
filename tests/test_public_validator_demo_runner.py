import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "run_public_validator_demo.py"
SAFETY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}
REQUIRED_LISTS = ["warnings", "missing_evidence", "conflicting_evidence"]


def run_scenario(scenario: str) -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, str(RUNNER), scenario],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def assert_deterministic_json(scenario: str) -> dict[str, object]:
    first = run_scenario(scenario)
    second = run_scenario(scenario)
    assert first == second
    return first


def assert_safety_markers(result: dict[str, object]) -> None:
    for key, value in SAFETY_MARKERS.items():
        assert result[key] is value
    for key in REQUIRED_LISTS:
        assert key in result
        assert isinstance(result[key], list)


def test_banana_scenario_returns_deterministic_json() -> None:
    result = assert_deterministic_json("banana")
    assert result["record_id"] == "HC-DEMO-PV-FIXTURE-FOOD-0001"
    assert result["scenario"] == "imported_banana_food_provenance"
    assert result["status"] == "needs_human_review"


def test_building_scenario_returns_deterministic_json() -> None:
    result = assert_deterministic_json("building")
    assert result["record_id"] == "HC-DEMO-PV-FIXTURE-CONCRETE-0001"
    assert result["scenario"] == "building_concrete_provenance"
    assert result["status"] == "needs_human_review"


def test_news_scenario_returns_deterministic_json() -> None:
    result = assert_deterministic_json("news")
    assert result["record_id"] == "HC-DEMO-PV-FIXTURE-NEWS-0001"
    assert result["scenario"] == "news_source_provenance"
    assert result["status"] == "needs_human_review"


def test_qr_spoof_scenario_returns_warning() -> None:
    result = assert_deterministic_json("qr-spoof")
    assert result["record_id"] == "HC-DEMO-PV-FIXTURE-QR-0001"
    assert any("Non-canonical link" in warning for warning in result["warnings"])


def test_invalid_scenario_exits_non_zero() -> None:
    completed = subprocess.run(
        [sys.executable, str(RUNNER), "invalid"],
        capture_output=True,
        text=True,
    )
    assert completed.returncode != 0


def test_safety_markers_are_always_present() -> None:
    for scenario in ["banana", "building", "news", "qr-spoof"]:
        assert_safety_markers(run_scenario(scenario))
