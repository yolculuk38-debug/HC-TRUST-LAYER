import json
from pathlib import Path

from public_verification_explorer import (
    ADVISORY_BOUNDARY,
    list_records,
    lookup_record,
    normalize_record,
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
            "witness_count",
            "source_path",
            "metadata",
            "verification_history",
            "witness_information",
            "archive_status",
        ):
            assert field in record


def test_explorer_detail_preserves_explicit_zero_witness_count() -> None:
    record = normalize_record({
        "record_id": "HC-ZERO-WITNESS",
        "witness_count": 0,
        "witness_information": ["reviewer-a", "reviewer-b"],
    })

    assert record["witness_count"] == 0
