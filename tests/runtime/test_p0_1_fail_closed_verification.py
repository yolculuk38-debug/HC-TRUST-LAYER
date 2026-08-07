"""P0-1 regressions for fail-closed HC:// canonical evidence checks."""

from __future__ import annotations

import hashlib
import json

import httpx
import pytest

from hc_runtime.app import create_app
from hc_runtime.runtime import ValidatorPipeline
from hc_runtime.state import ABUSE_SIGNAL_TRACKER, EVENT_STORE, QUEUE_STORE
import hc_runtime.routes.verify as verify_route


def _sha256(content: object) -> str:
    text = content if isinstance(content, str) else json.dumps(content, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _structured_qr(record_id: str, **overrides: object) -> str:
    content = {"safe": True}
    payload: dict[str, object] = {
        "record_id": record_id,
        "verification_url": f"https://github.com/example/HC-TRUST-LAYER/verify/{record_id}",
        "content": content,
        "content_hash": _sha256(content),
        "created_at": "2026-08-07T00:00:00Z",
        "qr_version": "v1",
        "signed_payload_ref": f"signed-payloads/{record_id}.json",
    }
    payload.update(overrides)
    payload["payload_hash"] = _sha256(payload)
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


@pytest.mark.parametrize("qr_input", ["hc://unconfigured", "hash:attacker-controlled"])
def test_unconfigured_pipeline_does_not_fabricate_schema_or_hash_evidence(qr_input: str) -> None:
    result = ValidatorPipeline().run(record_id="absent", qr_input=qr_input)

    assert result["schema_result"]["checked"] is False
    assert result["schema_result"]["valid"] is False
    assert result["hash_result"]["checked"] is False
    assert result["hash_result"]["hash_verified"] is False
    assert any("not configured" in warning.lower() for warning in result["trust_assignment"]["warnings"])


@pytest.mark.parametrize(
    "qr_input",
    [
        "hc://missing",
        "hc://missing hash:attacker-controlled",
        _structured_qr("missing"),
        '{"record_id":',
    ],
)
def test_missing_record_does_not_fabricate_canonical_evidence(qr_input: str) -> None:
    result = ValidatorPipeline(canonical_records={}).run(record_id="missing", qr_input=qr_input)

    assert result["schema_result"]["checked"] is False
    assert result["schema_result"]["valid"] is False
    assert result["hash_result"]["checked"] is False
    assert result["hash_result"]["hash_verified"] is False
    assert any("no record" in warning.lower() for warning in result["trust_assignment"]["warnings"])


@pytest.mark.parametrize(
    ("record", "expected_status"),
    [
        ({"record_id": "missing-field", "content": "value"}, "hash_missing"),
        (
            {
                "record_id": "missing-field",
                "content_hash": hashlib.sha256(b"null").hexdigest(),
            },
            "schema_invalid",
        ),
    ],
)
def test_incomplete_record_never_runs_digest_comparison(record: dict[str, object], expected_status: str) -> None:
    result = ValidatorPipeline(canonical_records={"missing-field": record}).run(
        record_id="missing-field", qr_input="hc://missing-field"
    )

    assert result["canonical_bridge"]["lookup_status"] == expected_status
    assert result["hash_result"]["checked"] is False
    assert result["hash_result"]["hash_verified"] is False


def test_schema_and_hash_checks_remain_independent_positive_control() -> None:
    content = {"evidence": "present"}
    record = {"record_id": "different-id", "content": content, "content_hash": _sha256(content)}
    result = ValidatorPipeline(canonical_records={"requested-id": record}).run(
        record_id="requested-id", qr_input="hc://requested-id"
    )

    assert result["schema_result"]["checked"] is True
    assert result["schema_result"]["valid"] is False
    assert result["hash_result"]["checked"] is True
    assert result["hash_result"]["hash_verified"] is True


@pytest.fixture()
async def client(monkeypatch: pytest.MonkeyPatch) -> httpx.AsyncClient:
    EVENT_STORE._events.clear()
    QUEUE_STORE.verification_queue.clear()
    QUEUE_STORE.escalation_queue.clear()
    QUEUE_STORE.replay_warning_queue.clear()
    ABUSE_SIGNAL_TRACKER.reset()
    monkeypatch.setattr(verify_route, "PIPELINE", ValidatorPipeline(canonical_records={}))
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as async_client:
        yield async_client


@pytest.mark.anyio
@pytest.mark.parametrize(
    "qr_input",
    [
        "hc://missing",
        "hc://missing hash:attacker-controlled",
        _structured_qr("missing"),
        '{"record_id":',
    ],
)
async def test_public_missing_record_response_is_fail_closed(client: httpx.AsyncClient, qr_input: str) -> None:
    payload = (await client.post("/verify/missing", json={"qr_input": qr_input})).json()

    assert payload["status"] == "ADVISORY"
    assert payload["trust_state"] == "UNRESOLVED"
    assert payload["schema_valid"] is False
    assert payload["hash_verified"] is False
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert payload["qr_scan_summary"]["human_final_authority"] is True
    assert any("no record" in warning.lower() for warning in payload["warnings"])


@pytest.mark.anyio
async def test_get_missing_record_uses_no_fabricated_hash_marker(client: httpx.AsyncClient) -> None:
    payload = (await client.get("/qr/missing")).json()

    assert payload["trust_state"] == "UNRESOLVED"
    assert payload["schema_valid"] is False
    assert payload["hash_verified"] is False
    assert QUEUE_STORE.verification_queue[-1]["qr_input"] == "hc://missing"


@pytest.mark.anyio
async def test_empty_input_does_not_promote_real_canonical_results(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    content = {"evidence": "present"}
    record = {"record_id": "canonical-empty", "content": content, "content_hash": _sha256(content)}
    pipeline = ValidatorPipeline(canonical_records={"canonical-empty": record})
    internal = pipeline.run(record_id="canonical-empty", qr_input="   ")
    monkeypatch.setattr(verify_route, "PIPELINE", pipeline)

    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as local_client:
        payload = (await local_client.post("/verify/canonical-empty", json={"qr_input": "   "})).json()

    assert internal["hash_result"]["checked"] is True
    assert internal["hash_result"]["hash_verified"] is True
    assert payload["schema_valid"] is False
    assert payload["hash_verified"] is False
    assert payload["trust_state"] == "UNRESOLVED"
    assert any("qr input" in warning.lower() for warning in payload["warnings"])


@pytest.mark.anyio
async def test_malformed_non_empty_json_is_tracked_as_malformed(client: httpx.AsyncClient) -> None:
    first = (await client.post("/verify/malformed-family-001", json={"qr_input": '{"record_id":'})).json()
    second = (await client.post("/verify/malformed-family-002", json={"qr_input": '{"record_id":'})).json()

    assert first["qr_scan_summary"]["abuse_pattern_counts"]["malformed_input"] == 1
    assert second["qr_scan_summary"]["abuse_pattern_counts"]["malformed_input"] == 2
    assert "repeated_malformed_input" in second["qr_scan_summary"]["abuse_signal_reasons"]


@pytest.mark.anyio
async def test_structured_replay_marker_remains_visible_and_queued(client: httpx.AsyncClient) -> None:
    payload = (
        await client.post(
            "/verify/structured-replay",
            json={"qr_input": _structured_qr("structured-replay", replay_marker=True)},
        )
    ).json()

    assert payload["replay_warning"] is True
    assert payload["trust_state"] == "REPLAY_WARNING"
    assert payload["public_exposure"] == "restricted"
    assert payload["escalation_queued"] is True
    assert QUEUE_STORE.replay_warning_queue[-1]["record_id"] == "structured-replay"
    assert any(item.get("reason") == "replay_warning" for item in QUEUE_STORE.escalation_queue)

    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as local_client:
        history = (await local_client.get("/verify/structured-replay/history")).json()
    assert history["replay_warning_visible"] is True


@pytest.mark.anyio
async def test_get_can_report_genuine_canonical_success_without_hash_marker(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    content = "canonical GET content"
    record = {"record_id": "canonical-get", "content": content, "content_hash": _sha256(content)}
    monkeypatch.setattr(
        verify_route,
        "PIPELINE",
        ValidatorPipeline(canonical_records={"canonical-get": record}),
    )
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as local_client:
        payload = (await local_client.get("/qr/canonical-get")).json()

    assert payload["schema_valid"] is True
    assert payload["hash_verified"] is True
    assert QUEUE_STORE.verification_queue[-1]["qr_input"] == "hc://canonical-get"
