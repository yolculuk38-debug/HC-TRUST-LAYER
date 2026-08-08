"""RFC 8785 and strict-JSON contract tests for the shared HC primitive."""

from __future__ import annotations

import io
import math
from decimal import Decimal

import pytest

from hc_trust.canonicalization import (
    CANONICALIZATION_PROFILE,
    CanonicalizationError,
    canonicalize_json,
    strict_json_load,
    strict_json_loads,
)


def test_profile_identifier_and_rfc_number_vector() -> None:
    assert CANONICALIZATION_PROFILE == "rfc8785-jcs-v1"
    assert canonicalize_json(
        [333333333.33333329, 1e30, 4.50, 2e-3, 1e-27]
    ) == b"[333333333.3333333,1e+30,4.5,0.002,1e-27]"
    assert canonicalize_json(1) == b"1"
    assert canonicalize_json(1.0) == b"1"
    assert canonicalize_json(-0.0) == b"0"


def test_utf16_property_order_and_literal_utf8() -> None:
    value = {
        "\u20ac": "Euro Sign",
        "\r": "Carriage Return",
        "\ufb33": "Hebrew Letter Dalet With Dagesh",
        "1": "One",
        "\U0001f600": "Emoji: Grinning Face",
        "\u0080": "Control",
        "\u00f6": "Latin Small Letter O With Diaeresis",
    }

    assert canonicalize_json(value) == (
        '{"\\r":"Carriage Return","1":"One","\u0080":"Control",'
        '"\u00f6":"Latin Small Letter O With Diaeresis",'
        '"\u20ac":"Euro Sign","\U0001f600":"Emoji: Grinning Face",'
        '"\ufb33":"Hebrew Letter Dalet With Dagesh"}'
    ).encode("utf-8")
    assert canonicalize_json({"text": "T\u00fcrkiye"}) == '{"text":"T\u00fcrkiye"}'.encode("utf-8")


def test_nested_values_are_order_independent_and_escape_controls() -> None:
    first = {"z": [{"b": 2, "a": 1}], "a": "\b\t\n\f\r\"\\"}
    second = {"a": "\b\t\n\f\r\"\\", "z": [{"a": 1, "b": 2}]}

    assert canonicalize_json(first) == canonicalize_json(second)
    assert canonicalize_json(first) == b'{"a":"\\b\\t\\n\\f\\r\\\"\\\\","z":[{"a":1,"b":2}]}'


def test_unicode_is_not_normalized() -> None:
    composed = canonicalize_json({"value": "\u00e9"})
    decomposed = canonicalize_json({"value": "e\u0301"})

    assert composed != decomposed
    assert b"\xc3\xa9" in composed
    assert b"e\xcc\x81" in decomposed


@pytest.mark.parametrize(
    "value",
    [
        (1, 2),
        {1, 2},
        b"bytes",
        Decimal("1.0"),
        object(),
        {"tuple": (1, 2)},
        {"subclass": type("ListSubclass", (list,), {})([1, 2])},
        {1: "non-string-key"},
        2**53,
        -(2**53),
        math.nan,
        math.inf,
        -math.inf,
        "\ud800",
    ],
)
def test_non_json_or_unsafe_values_are_rejected(value: object) -> None:
    with pytest.raises(CanonicalizationError):
        canonicalize_json(value)


def test_safe_integer_boundaries_are_accepted() -> None:
    assert canonicalize_json(2**53 - 1) == b"9007199254740991"
    assert canonicalize_json(-(2**53) + 1) == b"-9007199254740991"


def test_cyclic_container_is_rejected() -> None:
    value: list[object] = []
    value.append(value)

    with pytest.raises(CanonicalizationError, match="cyclic_json_value"):
        canonicalize_json(value)


def test_excessive_nesting_is_wrapped_in_public_safe_error() -> None:
    value: object = None
    for _ in range(2_000):
        value = [value]

    with pytest.raises(CanonicalizationError, match="json_nesting_too_deep"):
        canonicalize_json(value)

    document = "[" * 2_000 + "null" + "]" * 2_000
    with pytest.raises(CanonicalizationError, match="json_nesting_too_deep"):
        strict_json_loads(document)


@pytest.mark.parametrize(
    "document",
    [
        '{"record_id":"first","record_id":"second"}',
        '{"outer":{"payload_hash":"first","payload_hash":"second"}}',
    ],
)
def test_duplicate_properties_are_rejected_at_every_depth(document: str) -> None:
    with pytest.raises(CanonicalizationError, match="duplicate_json_property"):
        strict_json_loads(document)


@pytest.mark.parametrize("document", ["NaN", "Infinity", "-Infinity", "1e400"])
def test_non_finite_json_numbers_are_rejected(document: str) -> None:
    with pytest.raises(CanonicalizationError):
        strict_json_loads(document)


def test_strict_file_loader_reuses_the_same_contract() -> None:
    loaded = strict_json_load(io.StringIO('{"b":2,"a":1}'))

    assert loaded == {"b": 2, "a": 1}
    assert canonicalize_json(loaded) == b'{"a":1,"b":2}'
