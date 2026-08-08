"""Versioned RFC 8785 canonicalization and strict JSON boundaries for HC://."""

from __future__ import annotations

import json
import math
from collections.abc import Callable
from typing import Any, TextIO

import rfc8785

CANONICALIZATION_PROFILE = "rfc8785-jcs-v1"
MAX_SAFE_INTEGER = 2**53 - 1
MIN_SAFE_INTEGER = -MAX_SAFE_INTEGER


class CanonicalizationError(ValueError):
    """Public-safe failure raised by the HC canonicalization boundary."""

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)


def _validate_string(value: str) -> None:
    try:
        value.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise CanonicalizationError("invalid_unicode_scalar") from exc


def _validate_json_value(value: Any, active_containers: set[int] | None = None) -> None:
    value_type = type(value)

    if value is None or value_type is bool:
        return
    if value_type is str:
        _validate_string(value)
        return
    if value_type is int:
        if not MIN_SAFE_INTEGER <= value <= MAX_SAFE_INTEGER:
            raise CanonicalizationError("unsafe_integer")
        return
    if value_type is float:
        if not math.isfinite(value):
            raise CanonicalizationError("non_finite_json_number")
        return

    if value_type not in (dict, list):
        raise CanonicalizationError("unsupported_json_type")

    active = active_containers if active_containers is not None else set()
    container_id = id(value)
    if container_id in active:
        raise CanonicalizationError("cyclic_json_value")
    active.add(container_id)
    try:
        if value_type is list:
            for item in value:
                _validate_json_value(item, active)
            return

        for key, item in value.items():
            if type(key) is not str:
                raise CanonicalizationError("non_string_object_key")
            _validate_string(key)
            _validate_json_value(item, active)
    finally:
        active.remove(container_id)


def canonicalize_json(value: Any) -> bytes:
    """Return exact RFC 8785 UTF-8 bytes for an actual JSON value."""

    try:
        _validate_json_value(value)
    except CanonicalizationError:
        raise
    except RecursionError as exc:
        raise CanonicalizationError("json_nesting_too_deep") from exc
    try:
        encoded = rfc8785.dumps(value)
    except rfc8785.CanonicalizationError as exc:
        raise CanonicalizationError("rfc8785_canonicalization_failed") from exc
    except (RecursionError, OverflowError, TypeError, ValueError) as exc:
        raise CanonicalizationError("rfc8785_canonicalization_failed") from exc
    if type(encoded) is not bytes:  # pragma: no cover - upstream contract guard
        raise CanonicalizationError("rfc8785_output_invalid")
    return encoded


def _reject_duplicate_properties(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CanonicalizationError("duplicate_json_property")
        result[key] = value
    return result


def _reject_non_finite_constant(_value: str) -> Any:
    raise CanonicalizationError("non_finite_json_number")


def strict_json_loads(text: str) -> Any:
    """Parse JSON without duplicate properties or non-I-JSON values."""

    if type(text) is not str:
        raise CanonicalizationError("json_text_required")
    try:
        value = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_properties,
            parse_constant=_reject_non_finite_constant,
        )
    except CanonicalizationError:
        raise
    except RecursionError as exc:
        raise CanonicalizationError("json_nesting_too_deep") from exc
    except (json.JSONDecodeError, ValueError, TypeError) as exc:
        raise CanonicalizationError("invalid_json") from exc
    try:
        _validate_json_value(value)
    except CanonicalizationError:
        raise
    except RecursionError as exc:
        raise CanonicalizationError("json_nesting_too_deep") from exc
    return value


def strict_json_load(file_object: TextIO) -> Any:
    """Read and strictly parse JSON from a text file-like object."""

    reader: Callable[[], Any] | None = getattr(file_object, "read", None)
    if reader is None or not callable(reader):
        raise CanonicalizationError("json_text_reader_required")
    try:
        text = reader()
    except (OSError, UnicodeError) as exc:
        raise CanonicalizationError("json_read_failed") from exc
    return strict_json_loads(text)


__all__ = [
    "CANONICALIZATION_PROFILE",
    "MAX_SAFE_INTEGER",
    "MIN_SAFE_INTEGER",
    "CanonicalizationError",
    "canonicalize_json",
    "strict_json_load",
    "strict_json_loads",
]
