"""Versioned HC content and QR digest profile tests."""

from __future__ import annotations

import hashlib

import pytest

from hc_trust.canonicalization import canonicalize_json
from hc_trust.hashing import (
    CONTENT_HASH_PROFILE_FIELD,
    DIGEST_ALGORITHM,
    HC_CONTENT_HASH_PROFILE,
    HC_QR_PAYLOAD_HASH_PROFILE,
    LEGACY_TEXT_HASH_PROFILE,
    ContentHashError,
    calculate_content_hash,
    calculate_qr_payload_hash,
)
from hc_trust.verification import find_record_files, verify_record_hash


def test_required_digest_profile_identifiers_are_stable() -> None:
    assert DIGEST_ALGORITHM == "sha-256"
    assert HC_CONTENT_HASH_PROFILE == "hc-content-sha256-v2"
    assert LEGACY_TEXT_HASH_PROFILE == "hc-content-raw-utf8-sha256-v1"
    assert HC_QR_PAYLOAD_HASH_PROFILE == "hc-qr-payload-jcs-sha256-v1"
    assert CONTENT_HASH_PROFILE_FIELD == "content_hash_profile"


def test_legacy_text_and_explicit_v2_text_preserve_raw_utf8() -> None:
    content = "Beyan de\u011fil, kay\u0131t esast\u0131r."
    expected = hashlib.sha256(content.encode("utf-8")).hexdigest()

    assert calculate_content_hash(content) == expected
    assert calculate_content_hash(content, HC_CONTENT_HASH_PROFILE) == expected


def test_explicit_v2_structured_content_uses_jcs() -> None:
    first = {"z": [3, {"b": 2, "a": "\u00e9"}], "a": 1.0}
    second = {"a": 1, "z": [3, {"a": "\u00e9", "b": 2}]}
    expected = hashlib.sha256(canonicalize_json(first)).hexdigest()

    assert calculate_content_hash(first, HC_CONTENT_HASH_PROFILE) == expected
    assert calculate_content_hash(second, HC_CONTENT_HASH_PROFILE) == expected


def test_algorithm_absent_structured_content_fails_closed() -> None:
    with pytest.raises(ContentHashError, match="legacy_structured_content_algorithm_ambiguous") as exc_info:
        calculate_content_hash({"evidence": "present"})

    assert exc_info.value.reason == "legacy_structured_content_algorithm_ambiguous"


@pytest.mark.parametrize(
    "profile",
    [None, LEGACY_TEXT_HASH_PROFILE, "sha256", "unknown-profile"],
)
def test_unknown_explicit_content_profile_fails_closed(profile: object) -> None:
    with pytest.raises(ContentHashError, match="unknown_content_hash_profile") as exc_info:
        calculate_content_hash("text", profile)

    assert exc_info.value.reason == "unknown_content_hash_profile"


def test_qr_payload_hash_uses_jcs_without_mutating_input() -> None:
    payload = {
        "record_id": "HC-JCS-2026-0001",
        "payload_hash": "declared-value",
        "nested": {"z": "\u0131", "a": [1.0, False, None]},
    }
    snapshot = {
        "record_id": payload["record_id"],
        "payload_hash": payload["payload_hash"],
        "nested": {"z": "\u0131", "a": [1.0, False, None]},
    }
    unhashed = {key: value for key, value in payload.items() if key != "payload_hash"}

    assert calculate_qr_payload_hash(payload) == hashlib.sha256(canonicalize_json(unhashed)).hexdigest()
    assert payload == snapshot


def test_all_checked_in_canonical_records_retain_existing_hashes() -> None:
    record_files, skipped = find_record_files("records")

    assert len(record_files) == 3
    assert skipped
    for record_path in record_files:
        passed, message = verify_record_hash(record_path)
        assert passed, message
