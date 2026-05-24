from public_explorer_api import (
    EXPLORER_RUNTIME_VERSION,
    get_explorer_receipt_lookup,
    get_explorer_record_lookup,
    get_federation_status_summary,
)


def test_record_lookup_found_response_is_public_safe_and_experimental():
    response = get_explorer_record_lookup(
        record_id="HC-REC-1",
        record_store={"HC-REC-1": {"status": "verified", "trust_score": 94}},
    )

    assert response["status"] == "experimental"
    assert response["non_production"] is True
    assert response["runtime_version"] == EXPLORER_RUNTIME_VERSION
    assert response["payload"]["found"] is True
    assert response["payload"]["status"] == "VERIFIED"


def test_receipt_lookup_supports_verification_receipts():
    response = get_explorer_receipt_lookup(
        receipt_id="VREC-1",
        receipt_store={
            "VREC-1": {
                "verification_state": "verified",
                "federation_confirmations": 3,
                "witness_summary": {"count": "2"},
            }
        },
    )

    assert response["payload"]["found"] is True
    assert response["payload"]["verification_state"] == "VERIFIED"
    assert response["payload"]["federation_confirmations"] == 3


def test_federation_status_summary_counts_node_states():
    response = get_federation_status_summary(
        nodes=[
            {"node_id": "n1", "state": "online"},
            {"node_id": "n2", "state": "OFFLINE"},
            {"node_id": "n3", "state": "degraded"},
        ]
    )

    payload = response["payload"]
    assert payload["total_nodes"] == 3
    assert payload["online_nodes"] == 1
    assert payload["degraded_nodes"] == 1
    assert payload["offline_nodes"] == 1
