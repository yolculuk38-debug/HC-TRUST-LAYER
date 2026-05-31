import json
from pathlib import Path

from public_verification_explorer import (
    ADVISORY_BOUNDARY,
    build_record_detail_response,
    list_records,
    lookup_record,
    render_record_detail_html,
    search_records,
)


def _index() -> dict:
    return json.loads(Path("generated/explorer_index.json").read_text(encoding="utf-8"))


def test_explorer_search_by_record_id() -> None:
    matches = search_records(_index(), "HC-EXAMPLE-2026-0001", search_by="record_id")

    assert len(matches) == 1
    assert matches[0]["record_id"] == "HC-EXAMPLE-2026-0001"
    assert matches[0]["read_only"] is True
    assert matches[0]["human_supervised"] is True


def test_explorer_search_by_hash() -> None:
    matches = search_records(_index(), "740f84dec83c", search_by="hash")

    assert len(matches) == 1
    assert matches[0]["content_hash"].startswith("740f84dec83c")
    assert matches[0]["witness_count"] == 2


def test_explorer_record_lookup_returns_detail_payload() -> None:
    response = lookup_record(_index(), "HC-2026-0000-0002")

    assert response["found"] is True
    record = response["record"]
    assert record["verification_status"] == "draft"
    assert record["timestamp"] == "2026-05-12T09:45:00Z"
    assert record["source_path"] == "records/pending/HC-2026-0002.json"
    assert record["witness_count"] == 4
    assert record["verification_history"]
    assert record["archive_status"] == "pending_archive"


def test_explorer_missing_record_handling_is_advisory_only() -> None:
    response = lookup_record(_index(), "HC-MISSING-2099-0001")

    assert response == {
        "found": False,
        "record_id": "HC-MISSING-2099-0001",
        "message": "Record ID was not found in generated/explorer_index.json.",
        **ADVISORY_BOUNDARY,
    }


def test_explorer_index_exposes_required_mvp_fields() -> None:
    for record in list_records(_index()):
        for field in (
            "record_id",
            "verification_status",
            "timestamp",
            "content_hash",
            "qr_reference",
            "witness_count",
            "source_path",
            "metadata",
            "verification_history",
            "witness_information",
            "archive_status",
        ):
            assert field in record


def test_record_detail_response_supports_explorer_record_route() -> None:
    response = build_record_detail_response(_index(), "HC-2026-0000-0002")

    assert response["found"] is True
    assert response["route"] == "/explorer/record/HC-2026-0000-0002"
    assert response["alternate_route"] == "/record/HC-2026-0000-0002"
    assert response["verification_summary"]["verification_status"] == "draft"
    assert response["record_metadata"]["source_path"] == "records/pending/HC-2026-0002.json"


def test_record_detail_response_returns_structured_missing_error() -> None:
    response = build_record_detail_response(_index(), "HC-MISSING-2099-0001")

    assert response["found"] is False
    assert response["route"] == "/explorer/record/HC-MISSING-2099-0001"
    assert response["error"] == {
        "code": "record_not_found",
        "human_message": "No generated explorer detail is available for this Record ID.",
    }
    assert "Record detail is unavailable" in response["message"]


def test_record_detail_html_renders_hash_field() -> None:
    html = render_record_detail_html(_index(), "HC-EXAMPLE-2026-0001")

    assert "Hash Information" in html
    assert "740f84dec83cce227ff4b6fb4280b088834dda8a632fa6c20250c829b80188dc" in html


def test_record_detail_html_renders_witness_metadata() -> None:
    html = render_record_detail_html(_index(), "HC-EXAMPLE-2026-0001")

    assert "Witness Information" in html
    assert "Witness count" in html
    assert "ChatGPT" in html
    assert "Claude" in html
