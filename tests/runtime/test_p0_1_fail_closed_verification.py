"""P0-1 regressions for fail-closed HC:// canonical evidence checks."""

from __future__ import annotations

import hashlib
import json

import httpx
import pytest

import hc_runtime.routes.verify as verify_route
from hc_runtime.app import create_app
from hc_runtime.runtime import ValidatorPipeline
from hc_runtime.state import ABUSE_SIGNAL_TRACKER, EVENT_STORE, QUEUE_STORE
from hc_trust.canonicalization import canonicalize_json
from hc_trust.hashing import (
    HC_CONTENT_HASH_PROFILE,
    calculate_content_hash,
    calculate_qr_payload_hash,
)


def _sha256(content: object) -> str:
    if isinstance(content, str):
        return calculate_content_hash(content)
    return calculate_content_hash(content, HC_CONTENT_HASH_PROFILE)


def _canonical_record(record_id: str, content: object) -> dict[str, object]:
    return {
        "schema_version": "hc-record-v1",
        "record_id": record_id,
        "created_at": "2026-08-08T12:00:00Z",
        "title": "P0-1 canonical evidence record",
        "record_type": "protocol_note",
        "witness_type": "human",
        "author": "HC-TRUST-LAYER tests",
        "content": content,
        "content_hash": _sha256(content),
        "content_hash_profile": HC_CONTENT_HASH_PROFILE,
        "archive_ref": "pending_archive",
        "verification_status": "draft",
    }


def _structured_qr(record_id: str, **overrides: object) -> str:
    content = {"safe": True}
    payload: dict[str, object] = {
        "record_id": record_id,
        "verification_url": f"https://github.com/example/HC-TRUST-LAYER/verify/{record_id}",
        "content": content,
        "content_hash": _sha256(content),
        "content_hash_profile": HC_CONTENT_HASH_PROFILE,
        "created_at": "2026-08-07T00:00:00Z",
        "qr_version": "v1",
        "signed_payload_ref": f"signed-payloads/{record_id}.json",
    }
    payload.update(overrides)
    payload["payload_hash"] = calculate_qr_payload_hash(payload)
    return canonicalize_json(payload).decode("utf-8")


def _structured_qr_with_explicit_null_profile(record_id: str) -> str:
    content = "legacy-compatible text"
    payload: dict[str, object] = {
        "record_id": record_id,
        "verification_url": f"https://github.com/example/HC-TRUST-LAYER/verify/{record_id}",
        "content": content,
        "content_hash": calculate_content_hash(content),
        "content_hash_profile": None,
        "created_at": "2026-08-07T00:00:00Z",
        "qr_version": "v1",
        "signed_payload_ref": f"signed-payloads/{record_id}.json",
    }
    payload["payload_hash"] = calculate_qr_payload_hash(payload)
    return canonicalize_json(payload).decode("utf-8")


def _structured_qr_without_content_hash_or_profile(record_id: str) -> str:
    payload: dict[str, object] = {
        "record_id": record_id,
        "verification_url": f"https://github.com/example/HC-TRUST-LAYER/verify/{record_id}",
        "content": {"safe": True},
        "created_at": "2026-08-07T00:00:00Z",
        "qr_version": "v1",
        "signed_payload_ref": f"signed-payloads/{record_id}.json",
    }
    payload["payload_hash"] = calculate_qr_payload_hash(payload)
    return canonicalize_json(payload).decode("utf-8")


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
    record = _canonical_record("HC-DIFFERENT-2026-0001", content)
    result = ValidatorPipeline(canonical_records={"HC-REQUESTED-2026-0001": record}).run(
        record_id="HC-REQUESTED-2026-0001",
        qr_input="hc://HC-REQUESTED-2026-0001",
    )

    assert result["schema_result"]["checked"] is True
    assert result["schema_result"]["valid"] is True
    assert result["canonical_bridge"]["record_id_match"] is False
    assert result["canonical_bridge"]["lookup_status"] == "record_id_mismatch"
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
    record_id = "HC-EMPTYINPUT-2026-0001"
    content = {"evidence": "present"}
    record = _canonical_record(record_id, content)
    pipeline = ValidatorPipeline(canonical_records={record_id: record})
    internal = pipeline.run(record_id=record_id, qr_input="   ")
    monkeypatch.setattr(verify_route, "PIPELINE", pipeline)

    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as local_client:
        payload = (await local_client.post(f"/verify/{record_id}", json={"qr_input": "   "})).json()

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
    record_id = "structured-marker-record"
    payload = (
        await client.post(
            f"/verify/{record_id}",
            json={"qr_input": _structured_qr(record_id, replay_marker=True)},
        )
    ).json()

    assert payload["replay_warning"] is True
    assert payload["trust_state"] == "REPLAY_WARNING"
    assert payload["public_exposure"] == "restricted"
    assert payload["escalation_queued"] is True
    assert QUEUE_STORE.replay_warning_queue[-1]["record_id"] == record_id
    assert any(item.get("reason") == "replay_warning" for item in QUEUE_STORE.escalation_queue)
    assert not any(item.get("reason") == "advisory_downgrade" for item in QUEUE_STORE.escalation_queue)

    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as local_client:
        history = (await local_client.get(f"/verify/{record_id}/history")).json()
    assert history["replay_warning_visible"] is True


@pytest.mark.anyio
async def test_get_can_report_genuine_canonical_success_without_hash_marker(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    record_id = "HC-GET-2026-0001"
    content = "canonical GET content"
    record = _canonical_record(record_id, content)
    monkeypatch.setattr(
        verify_route,
        "PIPELINE",
        ValidatorPipeline(canonical_records={record_id: record}),
    )
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as local_client:
        payload = (await local_client.get(f"/qr/{record_id}")).json()

    assert payload["schema_valid"] is True
    assert payload["hash_verified"] is True
    assert QUEUE_STORE.verification_queue[-1]["qr_input"] == f"hc://{record_id}"


@pytest.mark.anyio
@pytest.mark.parametrize(
    "qr_input",
    [
        "hc://HC-OTHER-2026-0001",
        _structured_qr("HC-OTHER-2026-0001"),
        json.dumps({"content": {"evidence": "present"}}),
    ],
)
async def test_qr_identity_mismatch_does_not_promote_canonical_results(
    monkeypatch: pytest.MonkeyPatch,
    qr_input: str,
) -> None:
    record_id = "HC-RECORD-2026-0001"
    content = {"evidence": "present"}
    record = _canonical_record(record_id, content)
    pipeline = ValidatorPipeline(canonical_records={record_id: record})
    internal = pipeline.run(record_id=record_id, qr_input=qr_input)
    monkeypatch.setattr(verify_route, "PIPELINE", pipeline)
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as local_client:
        payload = (await local_client.post(f"/verify/{record_id}", json={"qr_input": qr_input})).json()

    assert internal["hash_result"]["checked"] is True
    assert internal["hash_result"]["hash_verified"] is True
    assert payload["schema_valid"] is False
    assert payload["hash_verified"] is False
    assert payload["trust_state"] != "ADVISORY"
    assert any("record" in warning.lower() and "input" in warning.lower() for warning in payload["warnings"])


@pytest.mark.anyio
@pytest.mark.parametrize(
    "qr_input",
    ["hc://HC-RECORD-2026-0002", _structured_qr("HC-RECORD-2026-0002")],
)
async def test_matching_qr_identity_promotes_genuine_canonical_results(
    monkeypatch: pytest.MonkeyPatch,
    qr_input: str,
) -> None:
    record_id = "HC-RECORD-2026-0002"
    content = {"evidence": "present"}
    record = _canonical_record(record_id, content)
    monkeypatch.setattr(
        verify_route,
        "PIPELINE",
        ValidatorPipeline(canonical_records={record_id: record}),
    )
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as local_client:
        payload = (await local_client.post(f"/verify/{record_id}", json={"qr_input": qr_input})).json()

    assert payload["schema_valid"] is True
    assert payload["hash_verified"] is True
    assert payload["trust_state"] == "ADVISORY"


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("qr_input", "expected_reason"),
    [
        (
            '{"record_id":"attacker","record_id":"HC-RISK-2026-0001"}',
            "structured_payload_invalid",
        ),
        ('{"record_id":"HC-RISK-2026-0001","unsafe":NaN}', "structured_payload_invalid"),
        (
            _structured_qr("HC-RISK-2026-0001", content_hash_profile="unknown-profile"),
            "content_hash_unverifiable",
        ),
        (
            _structured_qr_with_explicit_null_profile("HC-RISK-2026-0001"),
            "content_hash_unverifiable",
        ),
        (
            _structured_qr("HC-RISK-2026-0001", verification_url="https://["),
            "verification_url_invalid",
        ),
        (
            _structured_qr_without_content_hash_or_profile("HC-RISK-2026-0001"),
            "content_hash_unverifiable",
        ),
    ],
)
async def test_high_risk_structured_qr_never_promotes_valid_canonical_results(
    client: httpx.AsyncClient,
    monkeypatch: pytest.MonkeyPatch,
    qr_input: str,
    expected_reason: str,
) -> None:
    record_id = "HC-RISK-2026-0001"
    content = {"evidence": "present"}
    record = _canonical_record(record_id, content)
    monkeypatch.setattr(
        verify_route,
        "PIPELINE",
        ValidatorPipeline(canonical_records={record_id: record}),
    )

    response = await client.post(f"/verify/{record_id}", json={"qr_input": qr_input})

    assert response.status_code == 200
    payload = response.json()
    assert payload["qr_risk_level"] in {"HIGH", "INCIDENT"}
    assert expected_reason in payload["qr_risk_reasons"]
    assert payload["schema_valid"] is False
    assert payload["hash_verified"] is False
    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert payload["human_review_recommended"] is True
    assert [item["reason"] for item in QUEUE_STORE.escalation_queue] == ["qr_spoof_risk"]
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False


@pytest.mark.anyio
async def test_advisory_downgrade_queue_action_is_reported(client: httpx.AsyncClient) -> None:
    payload = (await client.post("/verify/missing", json={"qr_input": "hc://missing"})).json()

    assert payload["escalation_queued"] is True
    assert payload["qr_scan_summary"]["escalation_queued"] is True
    assert any(item.get("reason") == "advisory_downgrade" for item in QUEUE_STORE.escalation_queue)


@pytest.mark.anyio
async def test_low_risk_structured_missing_record_queues_advisory_downgrade(client: httpx.AsyncClient) -> None:
    record_id = "structured-missing-record"
    payload = (await client.post(f"/verify/{record_id}", json={"qr_input": _structured_qr(record_id)})).json()

    assert payload["qr_risk_level"] == "LOW"
    assert payload["trust_state"] == "UNRESOLVED"
    assert payload["schema_valid"] is False
    assert payload["hash_verified"] is False
    assert payload["escalation_queued"] is True
    assert payload["qr_scan_summary"]["escalation_queued"] is True
    assert [item.get("reason") for item in QUEUE_STORE.escalation_queue] == ["advisory_downgrade"]


@pytest.mark.anyio
async def test_structured_canonical_success_remains_unqueued(
    client: httpx.AsyncClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    record_id = "HC-STRUCTURED-2026-0001"
    content = {"evidence": "present"}
    record = _canonical_record(record_id, content)
    monkeypatch.setattr(verify_route, "PIPELINE", ValidatorPipeline(canonical_records={record_id: record}))

    payload = (await client.post(f"/verify/{record_id}", json={"qr_input": _structured_qr(record_id)})).json()

    assert payload["trust_state"] == "ADVISORY"
    assert payload["schema_valid"] is True
    assert payload["hash_verified"] is True
    assert payload["escalation_queued"] is False
    assert payload["qr_scan_summary"]["escalation_queued"] is False
    assert QUEUE_STORE.escalation_queue == []
