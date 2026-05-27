"""Tests for the HC:// FastAPI reference runtime scaffold."""

from fastapi.testclient import TestClient

from hc_runtime.app import app

client = TestClient(app)


def test_health_endpoint_returns_advisory_runtime_status() -> None:
    response = client.get("/health")
    assert response.status_code == 200


def test_verify_qr_flow_runs_pipeline_decision_and_response_contract() -> None:
    response = client.post("/verify/qr-record", json={"qr_input": "hc://demo hash:abc123"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ADVISORY"
    assert payload["trust_state"] == "ADVISORY"
    assert payload["replay_warning"] is False
    assert payload["continuity_warning"] is False
    assert payload["advisory_only"] is True


def test_verify_history_endpoint_returns_public_safe_event_history() -> None:
    client.post("/verify/history-record", json={"qr_input": "hc://history hash:ok"})
    response = client.get("/verify/history-record/history")

    assert response.status_code == 200
    payload = response.json()
    assert payload["record_id"] == "history-record"
    assert payload["public_safe"] is True
    assert isinstance(payload["events"], list)
    assert isinstance(payload["trust_state_transitions"], list)


def test_replay_warning_propagation_and_queueing() -> None:
    response = client.post("/verify/replay-record", json={"qr_input": "hc://demo hash:ok replay"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["replay_warning"] is True
    assert payload["public_exposure"] == "restricted"

    history = client.get("/verify/replay-record/history").json()
    assert history["replay_warning_visible"] is True


def test_federation_review_route_is_advisory_placeholder() -> None:
    response = client.post("/federation/review", json={"record_id": "fed-review-1", "replay_warning": True})

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ADVISORY"
    assert payload["relay"]["relay_mode"] == "local-placeholder"


def test_telemetry_routes_return_advisory_operational_signals() -> None:
    assert client.get("/telemetry/health").status_code == 200
    runtime_payload = client.get("/telemetry/runtime").json()
    queues_payload = client.get("/telemetry/queues").json()

    assert runtime_payload["advisory_only"] is True
    assert queues_payload["degraded_queue_handling"] is True


def test_degraded_runtime_recovery_behavior_is_public_safe() -> None:
    response = client.post("/verify/degraded-record", json={"qr_input": "hc://demo hash:ok degraded"})

    payload = response.json()
    assert response.status_code == 200
    assert payload["degraded_runtime"] is True
    assert payload["recovery_mode"] is True
