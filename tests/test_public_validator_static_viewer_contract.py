from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIEWER = ROOT / "docs" / "demo" / "public-validator-static-viewer.html"


def _html() -> str:
    return VIEWER.read_text(encoding="utf-8")


def test_static_viewer_lists_demo_scenarios() -> None:
    html = _html()

    for scenario in ("banana", "building", "news", "qr-spoof"):
        assert f'data-scenario="{scenario}"' in html



def test_static_viewer_maps_demo_record_ids() -> None:
    html = _html()

    expected = {
        "HC-DEMO-PV-FIXTURE-FOOD-0001": "banana",
        "HC-DEMO-PV-FIXTURE-CONCRETE-0001": "building",
        "HC-DEMO-PV-FIXTURE+NEWS-0001": "news",
        "HC-DEMO-PV-FIXTURE+QR-0001": "qr-spoof",
    }

    for record_id, scenario in expected.items():
        assert f'"{record_id}": "{scenario}"' in html


def test_static_viewer_keeps_core_result_fields_visible() -> None:
    html = _html()

    for field in (
        "record_id",
        "scenario",
        "status",
        "source_chain",
        "responsibility_chain",
        "evidence",
        "missing_evidence",
        "conflicting_evidence",
        "warnings",
    ):
        assert field in html



def test_static_viewer_keeps_safety_markers_visible() -> None:
    html = _html()

    for marker in (
        "advisory_only",
        "public_safe",
        "truth_guarantee",
        "human_review_required",
    ):
        assert marker in html
