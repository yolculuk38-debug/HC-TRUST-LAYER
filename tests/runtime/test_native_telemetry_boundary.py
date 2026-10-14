"""An upgrade must not activate FastAPI's native telemetry in the HC app."""

import pytest
from fastapi import FastAPI
from fastapi.telemetry import _runtime
from fastapi.testclient import TestClient
from opentelemetry import _logs, metrics, trace

from hc_runtime.app import create_app


@pytest.mark.parametrize("factory,probes_expected", [(create_app, False), (FastAPI, True)])
def test_native_telemetry_stays_disabled_with_environment_and_global_providers(
    monkeypatch, factory, probes_expected
):
    calls = {"endpoint": [], "trace": [], "metrics": [], "logs": []}
    monkeypatch.delenv("OTEL_SDK_DISABLED", raising=False)
    monkeypatch.setenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://127.0.0.1:9")

    # Observe discovery without configuring exporters or making network calls.
    def endpoint_probe(signal):
        calls["endpoint"].append(signal)
        return None

    monkeypatch.setattr(_runtime, "_export_endpoint", endpoint_probe)
    for module, name, label, provider in (
        (trace, "get_tracer_provider", "trace", trace.NoOpTracerProvider()),
        (metrics, "get_meter_provider", "metrics", metrics.NoOpMeterProvider()),
        (_logs, "get_logger_provider", "logs", _logs.NoOpLoggerProvider()),
    ):
        def provider_probe(label=label, provider=provider):
            calls[label].append(True)
            return provider
        monkeypatch.setattr(module, name, provider_probe)

    app = factory()

    @app.get("/probe/{number}")
    def valid_request(number: int):
        return {"number": number}

    @app.get("/probe-failure")
    def failed_request():
        raise RuntimeError("synthetic-private-exception")

    with TestClient(app, raise_server_exceptions=False) as client:
        assert client.get("/probe/1").status_code == 200
        assert client.get("/probe/invalid").status_code == 422
        assert client.get("/probe-failure").status_code == 500

    if probes_expected:
        # Discriminating control: unchanged FastAPI defaults reach all probes.
        assert calls["endpoint"] == ["TRACES", "METRICS", "LOGS"]
        assert all(calls[key] for key in ("trace", "metrics", "logs"))
    else:
        assert calls == {"endpoint": [], "trace": [], "metrics": [], "logs": []}
