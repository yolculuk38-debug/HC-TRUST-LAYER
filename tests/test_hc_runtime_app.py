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

    message = payload["message"].lower()
    assert "placeholder" in message
    assert "advisory" in message
    assert "no truth guarantee" in message
    assert "no canonical record mutation" in message
    assert "no private data exposure" in message
