"""Tests for the HC:// FastAPI reference runtime scaffold."""

from fastapi.testclient import TestClient

from hc_runtime.app import app

client = TestClient(app)


def test_health_endpoint_returns_advisory_runtime_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["runtime"] == "hc-reference-runtime"
    assert payload["advisory_only"] is True


def test_verify_endpoint_returns_public_safe_advisory_placeholder() -> None:
    response = client.get("/verify/test-record")

    assert response.status_code == 200
    payload = response.json()
    assert payload["record_id"] == "test-record"
    assert payload["status"] == "ADVISORY"


def test_verify_qr_flow_runs_pipeline_decision_and_response_contract() -> None:
    response = client.post("/verify/qr-record", json={"qr_input": "hc://demo hash:abc123"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ADVISORY"
    assert payload["trust_state"] == "ADVISORY"
    assert payload["replay_warning"] is False
    assert payload["continuity_warning"] is False
    assert payload["advisory_only"] is True


def test_qr_get_route_runs_advisory_runtime_integration() -> None:
    response = client.get("/qr/qr-get-record")

    assert response.status_code == 200
    payload = response.json()
    assert payload["record_id"] == "qr-get-record"
    assert payload["trust_state"] == "ADVISORY"
    assert payload["replay_warning"] is False


def test_verify_history_endpoint_returns_public_safe_event_history() -> None:
    client.post("/verify/history-record", json={"qr_input": "hc://history hash:ok"})
    response = client.get("/verify/history-record/history")

    assert response.status_code == 200
    payload = response.json()
    assert payload["record_id"] == "history-record"
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert isinstance(payload["events"], list)
    assert any(event["event_type"] == "trust_state_transition" for event in payload["events"])


def test_replay_warning_is_propagated_and_appended() -> None:
    response = client.post("/verify/replay-record", json={"qr_input": "hc://demo replay"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["replay_warning"] is True
    assert payload["trust_state"] == "REPLAY_WARNING"
    assert any("Replay warning" in warning for warning in payload["warnings"])

    history = client.get("/verify/replay-record/history").json()["events"]
    assert any(event["event_type"] == "replay_warning" for event in history)


def test_continuity_warning_is_propagated_in_response() -> None:
    response = client.post("/verify/continuity-warning-record", json={"qr_input": "hc://demo hash:ok continuity-warning"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["continuity_warning"] is True
    assert payload["trust_state"] == "DEGRADED"
    assert any("Continuity warning" in warning for warning in payload["warnings"])


def test_federation_review_route_is_advisory_local_only_placeholder() -> None:
    response = client.post("/federation/review", json={"record_id": "fed-review-1"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ADVISORY"
    assert payload["advisory_only"] is True
    assert "No external networking" in payload["message"]
