"""Compare the production Python boundary to shared byte/digest fixtures."""

import hashlib
import json
from pathlib import Path

import pytest

from hc_trust.canonicalization import CANONICALIZATION_PROFILE, canonicalize_json, strict_json_loads

CORPUS = json.loads((Path(__file__).parent / "fixtures/canonicalization/golden-v1.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("vector", CORPUS["vectors"], ids=lambda vector: vector["id"])
def test_production_canonicalization_matches_shared_bytes_and_digest(vector):
    assert CORPUS["profile"] == CANONICALIZATION_PROFILE
    expected = vector["canonical"].encode("utf-8")
    actual = canonicalize_json(strict_json_loads(vector["input_json"]))
    assert actual == expected
    assert actual.hex() == vector["utf8_hex"]
    assert hashlib.sha256(actual).hexdigest() == vector["sha256"]
