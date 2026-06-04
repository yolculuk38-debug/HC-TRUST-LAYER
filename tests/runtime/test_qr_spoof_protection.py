"""QR spoof-protection behavior tests for the HC:// advisory runtime."""

from __future__ import annotations

import hashlib
import json

import httpx
import pytest

from hc_runtime.app import create_app
from hc_runtime.state import ABUSE_SIGNAL_TRACKER, EVENT_STORE, QUEUE_STORE

EXPECTED_QR_RESPONSE_KEYS = [
    "status",
    "advisory_only",
    "runtime_stage",
    "verification_mode",
    "public_safe",
    "message",
    "warnings",
    "traceable",
    "truth_guarantee",
    "human_review_required",
    "record_id",
    "trust_state",
    "replay_warning",
    "continuity_warning",
    "degraded_runtime",
    "recovery_mode",
    "public_exposure",
    "qr_risk_level",
    "qr_risk_reasons",
    "human_review_recommended",
    "escalation_queued",
    "incident_summary",
    "canonical_lookup_status",
    "schema_valid",
    "hash_verified",
    "qr_scan_summary",
]


def _canonical_json(data: object) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _structured_qr_payload(record_id: str, **overrides: object) -> dict[str, object]:
    content = overrides.pop("content", {"record_id": record_id, "summary": "HC:// advisory QR test payload"})
    content_text = content if isinstance(content, str) else _canonical_json(content)
    payload: dict[str, object] = {
        "record_id": record_id,
        "verification_url": f"https://github.com/example/HC-TRUST-LAYER/verify/{record_id}",
        "content": content,
        "content_hash": _sha256_text(content_text),
        "created_at": "2026-05-28T00:00:00Z",
        "qr_version": "v1",
        "signed_payload_ref": f"signed-payloads/{record_id}.json",
    }
    payload.update(overrides)
    if "payload_hash" not in payload:
        payload["payload_hash"] = _sha256_text(_canonical_json(payload))
    return payload


def _encoded_qr(record_id: str, **overrides: object) -> str:
    return _canonical_json(_structured_qr_payload(record_id, **overrides))


def _payload_with_current_hash(payload: dict[str, object], *, uppercase_payload_hash: bool = False) -> dict[str, object]:
    payload = dict(payload)
    payload["payload_hash"] = _sha256_text(_canonical_json({key: value for key, value in payload.items() if key != "payload_hash"}))
    if uppercase_payload_hash:
        payload["payload_hash"] = str(payload["payload_hash"]).upper()
    return payload


def _encoded_payload(payload: dict[str, object], *, uppercase_payload_hash: bool = False) -> str:
    return _canonical_json(_payload_with_current_hash(payload, uppercase_payload_hash=uppercase_payload_hash))


@pytest.fixture(autouse=True)
def reset_runtime_state() -> None:
    EVENT_STORE._events.clear()
    QUEUE_STORE.verification_queue.clear()
    QUEUE_STORE.escalation_queue.clear()
    QUEUE_STORE.replay_warning_queue.clear()
    ABUSE_SIGNAL_TRACKER.reset()


@pytest.fixture()
async def client() -> httpx.AsyncClient:
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as async_client:
        yield async_client


def _assert_public_safe_advisory_contract(payload: dict[str, object], *, record_id: str) -> None:
    assert list(payload.keys()) == EXPECTED_QR_RESPONSE_KEYS
    assert payload["record_id"] == record_id
    assert payload["status"] == "ADVISORY"
    assert payload["advisory_only"] is True
    assert payload["runtime_stage"] == "prototype"
    assert payload["verification_mode"] == "advisory"
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert payload["human_review_required"] is bool(payload["warnings"])
    assert isinstance(payload["warnings"], list)
    assert all(isinstance(warning, str) for warning in payload["warnings"])
    assert payload["qr_risk_level"] in {"LOW", "MEDIUM", "HIGH", "INCIDENT"}
    assert isinstance(payload["qr_risk_reasons"], list)
    assert isinstance(payload["human_review_recommended"], bool)
    assert isinstance(payload["escalation_queued"], bool)
    assert isinstance(payload["incident_summary"], dict)
    assert isinstance(payload["canonical_lookup_status"], str)
    assert isinstance(payload["schema_valid"], bool)
    assert isinstance(payload["hash_verified"], bool)
    assert isinstance(payload["qr_scan_summary"], dict)
    assert payload["qr_scan_summary"]["advisory_only"] is True
    assert payload["qr_scan_summary"]["public_safe"] is True
    assert payload["qr_scan_summary"]["truth_guarantee"] is False
    assert payload["qr_scan_summary"]["request_denied"] is False
    assert payload["qr_scan_summary"]["human_final_authority"] is True
    assert isinstance(payload["qr_scan_summary"]["abuse_warnings"], list)


def _warning_text(payload: dict[str, object]) -> str:
    return " ".join(str(warning).lower() for warning in payload["warnings"])


async def _post_qr(client: httpx.AsyncClient, record_id: str, qr_input: str) -> dict[str, object]:
    response = await client.post(f"/verify/{record_id}", json={"qr_input": qr_input})
    assert response.status_code == 200
    payload = response.json()
    _assert_public_safe_advisory_contract(payload, record_id=record_id)
    return payload


def _assert_review_only_for_high_or_incident(payload: dict[str, object]) -> None:
    assert payload["human_review_recommended"] is (payload["qr_risk_level"] in {"HIGH", "INCIDENT"})


def _assert_contract_stability_with_visible_warnings(payload: dict[str, object]) -> None:
    assert list(payload.keys()) == EXPECTED_QR_RESPONSE_KEYS
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert payload["qr_scan_summary"]["advisory_only"] is True
    assert payload["qr_scan_summary"]["public_safe"] is True
    assert payload["qr_scan_summary"]["truth_guarantee"] is False
    assert payload["qr_scan_summary"]["human_final_authority"] is True
    assert payload["warnings"]
    assert payload["qr_scan_summary"]["warning_count"] == len(payload["warnings"])


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("record_id", "qr_input"),
    [
        ("malformed-json-payload", "{not-json"),
        ("partially-corrupted-payload", '{"record_id":"partially-corrupted-payload","verification_url":'),
        ("truncated-payload", _encoded_qr("truncated-payload")[:80]),
    ],
)
async def test_malformed_structured_payloads_preserve_public_safe_contract(
    client: httpx.AsyncClient,
    record_id: str,
    qr_input: str,
) -> None:
    payload = await _post_qr(client, record_id, qr_input)

    assert payload["qr_risk_level"] == "LOW"
    assert payload["qr_risk_reasons"] == []
    assert payload["human_review_recommended"] is False
    assert payload["escalation_queued"] is False
    assert "hash marker could not be confirmed" in _warning_text(payload)
    _assert_contract_stability_with_visible_warnings(payload)


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("record_id", "qr_input"),
    [
        ("array-payload-type", '[{"record_id":"array-payload-type"}]'),
        ("string-payload-type", '"record_id:string-payload-type"'),
        ("numeric-payload-type", "12345"),
    ],
)
async def test_invalid_payload_types_remain_advisory_without_qr_spoof_escalation(
    client: httpx.AsyncClient,
    record_id: str,
    qr_input: str,
) -> None:
    payload = await _post_qr(client, record_id, qr_input)

    assert payload["qr_risk_level"] == "LOW"
    assert payload["qr_risk_reasons"] == []
    assert payload["human_review_recommended"] is False
    assert payload["escalation_queued"] is False
    assert "hash marker could not be confirmed" in _warning_text(payload)
    _assert_contract_stability_with_visible_warnings(payload)


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("record_id", "verification_url", "expected_reason", "expected_warning"),
    [
        ("empty-verification-url", "", "verification_url_missing", "verification_url is missing"),
        ("whitespace-verification-url", "   ", "verification_url_missing", "verification_url is missing"),
        ("malformed-verification-url", "not a url", "non_canonical_scheme", "verification_url scheme"),
    ],
)
async def test_verification_url_edge_cases_are_visible_high_risk_advisory_findings(
    client: httpx.AsyncClient,
    record_id: str,
    verification_url: str,
    expected_reason: str,
    expected_warning: str,
) -> None:
    payload = await _post_qr(client, record_id, _encoded_qr(record_id, verification_url=verification_url))

    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert payload["qr_risk_level"] == "HIGH"
    assert expected_reason in payload["qr_risk_reasons"]
    assert expected_warning in _warning_text(payload)
    assert payload["human_review_recommended"] is True
    assert payload["escalation_queued"] is True
    assert QUEUE_STORE.escalation_queue[-1]["advisory_only"] is True
    assert QUEUE_STORE.escalation_queue[-1]["public_safe"] is True
    assert QUEUE_STORE.escalation_queue[-1]["truth_guarantee"] is False
    _assert_contract_stability_with_visible_warnings(payload)


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("record_id", "missing_field", "expected_reason", "expected_warning"),
    [
        ("missing-record-id-spoof-domain", "record_id", "record_id_missing", "missing record_id"),
        ("missing-payload-hash-spoof-domain", "payload_hash", "payload_hash_missing", "payload_hash is missing"),
        ("missing-content-hash-spoof-domain", "content_hash", "content_hash_missing", "content_hash is missing"),
    ],
)
async def test_combined_missing_payload_fields_with_spoof_domain_remain_visible(
    client: httpx.AsyncClient,
    record_id: str,
    missing_field: str,
    expected_reason: str,
    expected_warning: str,
) -> None:
    payload_data = _structured_qr_payload(record_id, verification_url=f"https://spoof.example/verify/{record_id}")
    payload_data.pop(missing_field)
    qr_input = _canonical_json(payload_data) if missing_field == "payload_hash" else _encoded_payload(payload_data)

    payload = await _post_qr(client, record_id, qr_input)

    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert payload["qr_risk_level"] == "HIGH"
    assert "non_canonical_domain" in payload["qr_risk_reasons"]
    assert expected_reason in payload["qr_risk_reasons"]
    assert "non-canonical qr verification_url domain" in _warning_text(payload)
    assert expected_warning in _warning_text(payload)
    assert payload["human_review_recommended"] is True
    assert payload["escalation_queued"] is True
    _assert_contract_stability_with_visible_warnings(payload)


@pytest.mark.anyio
async def test_hash_case_differences_do_not_escalate_trust_or_change_deterministic_comparison(
    client: httpx.AsyncClient,
) -> None:
    lower_record_id = "hash-case-lower-record"
    upper_record_id = "hash-case-upper-record"
    lower_payload = _structured_qr_payload(lower_record_id)
    upper_payload = _structured_qr_payload(upper_record_id)
    upper_payload["content_hash"] = str(upper_payload["content_hash"]).upper()

    lower = await _post_qr(client, lower_record_id, _encoded_payload(lower_payload))
    upper = await _post_qr(client, upper_record_id, _encoded_payload(upper_payload, uppercase_payload_hash=True))

    assert lower["qr_risk_level"] == upper["qr_risk_level"] == "LOW"
    assert lower["qr_risk_reasons"] == upper["qr_risk_reasons"] == []
    assert lower["warnings"] == upper["warnings"] == []
    assert lower["trust_state"] == upper["trust_state"] == "ADVISORY"
    assert lower["hash_verified"] is True
    assert upper["hash_verified"] is True
    assert lower["human_review_recommended"] is False
    assert upper["human_review_recommended"] is False
    assert lower["escalation_queued"] is False
    assert upper["escalation_queued"] is False
    assert QUEUE_STORE.escalation_queue == []
    assert list(lower.keys()) == list(upper.keys()) == EXPECTED_QR_RESPONSE_KEYS
    assert lower["qr_scan_summary"]["human_final_authority"] is True
    assert upper["qr_scan_summary"]["human_final_authority"] is True


@pytest.mark.anyio
async def test_legacy_insanlik_zinciri_path_on_allowed_domain_is_high_risk(client: httpx.AsyncClient) -> None:
    record_id = "legacy-insanlik-zinciri-path"

    payload = await _post_qr(
        client,
        record_id,
        _encoded_qr(record_id, verification_url="https://github.com/yolculuk38-debug/Insanlik-Zinciri"),
    )

    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert payload["qr_risk_level"] == "HIGH"
    assert "non_canonical_path" in payload["qr_risk_reasons"]
    assert "non-canonical qr verification_url path" in _warning_text(payload)
    assert payload["human_review_recommended"] is True
    assert payload["escalation_queued"] is True
    assert QUEUE_STORE.escalation_queue[-1]["advisory_only"] is True
    assert QUEUE_STORE.escalation_queue[-1]["public_safe"] is True
    assert QUEUE_STORE.escalation_queue[-1]["truth_guarantee"] is False


@pytest.mark.anyio
async def test_canonical_qr_returns_low_risk_automatic_advisory_result(client: httpx.AsyncClient) -> None:
    record_id = "canonical-qr-spoof-record"

    payload = await _post_qr(client, record_id, _encoded_qr(record_id))

    assert payload["trust_state"] == "ADVISORY"
    assert payload["qr_risk_level"] == "LOW"
    assert payload["qr_risk_reasons"] == []
    assert payload["warnings"] == []
    assert payload["public_exposure"] == "standard"
    assert payload["human_review_recommended"] is False
    assert payload["escalation_queued"] is False
    assert QUEUE_STORE.escalation_queue == []
    _assert_review_only_for_high_or_incident(payload)


@pytest.mark.anyio
async def test_stale_qr_returns_medium_risk_with_visible_warning_without_forced_review(client: httpx.AsyncClient) -> None:
    record_id = "stale-qr-version-record"

    payload = await _post_qr(client, record_id, _encoded_qr(record_id, qr_version="v0", stale=True))

    assert payload["trust_state"] == "ADVISORY"
    assert payload["qr_risk_level"] == "MEDIUM"
    assert "stale_qr_version" in payload["qr_risk_reasons"]
    assert "stale_qr_payload" in payload["qr_risk_reasons"]
    assert "stale qr version marker" in _warning_text(payload)
    assert "stale qr payload flag" in _warning_text(payload)
    assert payload["human_review_recommended"] is False
    assert payload["escalation_queued"] is False
    assert QUEUE_STORE.escalation_queue == []
    _assert_review_only_for_high_or_incident(payload)


@pytest.mark.anyio
async def test_missing_signed_payload_reference_returns_medium_risk(client: httpx.AsyncClient) -> None:
    record_id = "missing-signed-ref-record"

    payload = await _post_qr(client, record_id, _encoded_qr(record_id, signed_payload_ref=""))

    assert payload["trust_state"] == "ADVISORY"
    assert payload["qr_risk_level"] == "MEDIUM"
    assert payload["qr_risk_reasons"] == ["signed_payload_ref_missing"]
    assert "signed payload reference is missing" in _warning_text(payload)
    assert payload["human_review_recommended"] is False
    assert payload["escalation_queued"] is False
    _assert_review_only_for_high_or_incident(payload)


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("record_id", "qr_input", "expected_reason", "expected_warning"),
    [
        (
            "non-canonical-domain-record",
            _encoded_qr("non-canonical-domain-record", verification_url="https://spoof.example/verify/non-canonical-domain-record"),
            "non_canonical_domain",
            "non-canonical qr verification_url domain",
        ),
        ("expected-record-id", _encoded_qr("spoofed-record-id"), "record_id_mismatch", "record_id mismatch"),
        ("payload-hash-mismatch-record", _encoded_qr("payload-hash-mismatch-record", payload_hash="0" * 64), "payload_hash_mismatch", "payload_hash mismatch"),
        ("content-hash-mismatch-record", _encoded_qr("content-hash-mismatch-record", content_hash="f" * 64), "content_hash_mismatch", "content_hash mismatch"),
    ],
)
async def test_high_risk_qr_indicators_enter_escalation_queue(
    client: httpx.AsyncClient,
    record_id: str,
    qr_input: str,
    expected_reason: str,
    expected_warning: str,
) -> None:
    payload = await _post_qr(client, record_id, qr_input)

    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert payload["qr_risk_level"] == "HIGH"
    assert expected_reason in payload["qr_risk_reasons"]
    assert expected_warning in _warning_text(payload)
    assert payload["human_review_recommended"] is True
    assert payload["escalation_queued"] is True
    assert QUEUE_STORE.escalation_queue[-1]["record_id"] == record_id
    assert QUEUE_STORE.escalation_queue[-1]["risk_level"] == "HIGH"
    assert QUEUE_STORE.escalation_queue[-1]["advisory_only"] is True
    assert QUEUE_STORE.escalation_queue[-1]["public_safe"] is True
    assert QUEUE_STORE.escalation_queue[-1]["truth_guarantee"] is False
    _assert_review_only_for_high_or_incident(payload)


@pytest.mark.anyio
async def test_low_risk_qr_does_not_enter_escalation_queue(client: httpx.AsyncClient) -> None:
    payload = await _post_qr(client, "low-risk-no-escalation", _encoded_qr("low-risk-no-escalation"))

    assert payload["qr_risk_level"] == "LOW"
    assert payload["escalation_queued"] is False
    assert QUEUE_STORE.escalation_queue == []


@pytest.mark.anyio
async def test_medium_risk_qr_does_not_force_human_review_by_default(client: httpx.AsyncClient) -> None:
    payload = await _post_qr(client, "medium-no-review", _encoded_qr("medium-no-review", signed_payload_ref=""))

    assert payload["qr_risk_level"] == "MEDIUM"
    assert payload["human_review_recommended"] is False
    assert payload["escalation_queued"] is False
    assert "human-supervised validation" not in _warning_text(payload)
    assert QUEUE_STORE.escalation_queue == []


@pytest.mark.anyio
async def test_repeated_high_risk_qr_pattern_creates_incident_style_escalation_summary(client: httpx.AsyncClient) -> None:
    first_record = "incident-domain-family-001"
    second_record = "incident-domain-family-002"

    first = await _post_qr(
        client,
        first_record,
        _encoded_qr(first_record, verification_url=f"https://spoof.example/verify/{first_record}"),
    )
    second = await _post_qr(
        client,
        second_record,
        _encoded_qr(second_record, verification_url=f"https://spoof.example/verify/{second_record}"),
    )

    assert first["qr_risk_level"] == "HIGH"
    assert second["qr_risk_level"] == "INCIDENT"
    assert second["human_review_recommended"] is True
    assert second["escalation_queued"] is True
    assert second["incident_summary"]["active"] is True
    assert "domain:spoof.example" in second["incident_summary"]["group_keys"]
    assert second["incident_summary"]["related_high_findings"] == 2
    assert QUEUE_STORE.escalation_queue[-1]["risk_level"] == "INCIDENT"
    assert QUEUE_STORE.escalation_queue[-1]["incident_summary"]["active"] is True


@pytest.mark.anyio
async def test_human_review_recommended_only_for_high_or_incident_states(client: httpx.AsyncClient) -> None:
    low = await _post_qr(client, "review-low", _encoded_qr("review-low"))
    medium = await _post_qr(client, "review-medium", _encoded_qr("review-medium", signed_payload_ref=""))
    high = await _post_qr(
        client,
        "review-high",
        _encoded_qr("review-high", verification_url="https://spoof-review.example/verify/review-high"),
    )
    incident = await _post_qr(
        client,
        "review-high-repeat",
        _encoded_qr("review-high-repeat", verification_url="https://spoof-review.example/verify/review-high-repeat"),
    )

    assert [(payload["qr_risk_level"], payload["human_review_recommended"]) for payload in [low, medium, high, incident]] == [
        ("LOW", False),
        ("MEDIUM", False),
        ("HIGH", True),
        ("INCIDENT", True),
    ]


@pytest.mark.anyio
async def test_stable_qr_response_keys_across_low_medium_high_and_incident_states(client: httpx.AsyncClient) -> None:
    low = await _post_qr(client, "stable-low", _encoded_qr("stable-low"))
    medium = await _post_qr(client, "stable-medium", _encoded_qr("stable-medium", signed_payload_ref=""))
    high = await _post_qr(
        client,
        "stable-high-001",
        _encoded_qr("stable-high-001", verification_url="https://stable-spoof.example/verify/stable-high-001"),
    )
    incident = await _post_qr(
        client,
        "stable-high-002",
        _encoded_qr("stable-high-002", verification_url="https://stable-spoof.example/verify/stable-high-002"),
    )

    responses = [low, medium, high, incident]

    assert [payload["qr_risk_level"] for payload in responses] == ["LOW", "MEDIUM", "HIGH", "INCIDENT"]
    assert all(list(payload.keys()) == EXPECTED_QR_RESPONSE_KEYS for payload in responses)
    assert all(payload["advisory_only"] is True for payload in responses)
    assert all(payload["public_safe"] is True for payload in responses)
    assert all(payload["truth_guarantee"] is False for payload in responses)
    assert all(isinstance(payload["warnings"], list) for payload in responses)


@pytest.mark.anyio
async def test_summary_count_behavior_for_qr_scan_outcomes(client: httpx.AsyncClient) -> None:
    record_id = "summary-count-record"

    payload = await _post_qr(client, record_id, _encoded_qr(record_id, signed_payload_ref="", stale=True))

    assert payload["qr_risk_level"] == "MEDIUM"
    assert payload["qr_scan_summary"] == {
        "warning_count": len(payload["warnings"]),
        "risk_reason_count": len(payload["qr_risk_reasons"]),
        "escalation_queued": False,
        "human_review_recommended": False,
        "risk_level": "MEDIUM",
        "abuse_signal_level": "MEDIUM",
        "abuse_signal_reasons": ["medium_qr_risk_visible"],
        "abuse_pattern_counts": {},
        "abuse_warnings": [],
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "request_denied": False,
        "human_final_authority": True,
    }
    assert payload["qr_scan_summary"]["warning_count"] >= 2
    assert payload["qr_scan_summary"]["risk_reason_count"] >= 2
