from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIEWER = ROOT / "docs" / "demo" / "public-validator-static-viewer.html"

SCENARIO_LINKS = {
    "banana": "HC-DEMO-PV-FIXTURE-FOOD-0001",
    "building": "HC-DEMO-PV-FIXTURE-CONCRETE-0001",
    "news": "HC-DEMO-PV-FIXTURE-NEWS-0001",
    "qr-spoof": "HC-DEMO-PV-FIXTURE-QR-0001",
}


def _viewer_html() -> str:
    return VIEWER.read_text(encoding="utf-8")


def test_static_viewer_keeps_query_scenario_and_button_entry_points() -> None:
    html = _viewer_html()

    for scenario in SCENARIO_LINKS:
        assert f"?scenario={scenario}" in html
        assert f'data-scenario="{scenario}"' in html

    assert "function scenarioFromQueryString()" in html
    assert 'url.searchParams.set("scenario", key);' in html


def test_static_viewer_record_id_input_maps_supported_fixture_ids() -> None:
    html = _viewer_html()

    assert 'id="record-id-form"' in html
    assert 'id="record-id-input"' in html
    assert "fixture matching only, not canonical record lookup" in html

    for scenario, record_id in SCENARIO_LINKS.items():
        assert f'"{record_id}": "{scenario}"' in html
        assert f'record_id: "{record_id}"' in html


def test_static_viewer_unsupported_record_id_is_public_safe_and_static_only() -> None:
    html = _viewer_html()

    assert "Public-safe demo warning: unsupported demo record_id" in html
    assert "does not call a backend" in html
    assert "perform canonical lookup" in html
    assert "verify truth" in html
    assert "prove QR authenticity" in html
    assert "validate signed payloads" in html

    forbidden_network_calls = ["fetch(", "XMLHttpRequest", "sendBeacon", "WebSocket", "EventSource"]
    for forbidden in forbidden_network_calls:
        assert forbidden not in html
