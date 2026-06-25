import json
from pathlib import Path

import pytest

from scripts.check_hc_trust_engineer_output_contract import ContractError, validate_contract

FIXTURE = Path("tests/fixtures/project_control/hc_trust_engineer_operating_loop_output_sample.json")


@pytest.fixture
def sample_payload():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def section(payload, name):
    return next(item for item in payload["outputs"] if item["section"] == name)


def assert_invalid(payload, expected):
    with pytest.raises(ContractError, match=expected):
        validate_contract(payload)


def test_valid_sample_passes(sample_payload):
    validate_contract(sample_payload)


def test_missing_envelope_field_fails(sample_payload):
    del sample_payload["repository"]

    assert_invalid(sample_payload, "missing required envelope field: repository")


def test_wrong_hard_boundary_value_fails(sample_payload):
    sample_payload["advisory_only"] = False

    assert_invalid(sample_payload, "advisory_only must be exactly true")


def test_missing_exact_marker_string_fails(sample_payload):
    sample_payload["hard_boundary_markers"].remove("truth_guarantee=false")

    assert_invalid(sample_payload, "missing exact hard boundary marker: truth_guarantee=false")


def test_invalid_chain_status_fails(sample_payload):
    section(sample_payload, "CHAIN_STATUS")["status"] = "done"

    assert_invalid(sample_payload, "CHAIN_STATUS.status has invalid value")


def test_invalid_next_action_candidate_action_type_fails(sample_payload):
    section(sample_payload, "NEXT_ACTION_CANDIDATE")["action_type"] = "open_pr"

    assert_invalid(sample_payload, "NEXT_ACTION_CANDIDATE.action_type has invalid value")


def test_invalid_risk_level_fails(sample_payload):
    section(sample_payload, "RISK_BOUNDARY_CLASSIFICATION")["risk_level"] = "none"

    assert_invalid(sample_payload, "RISK_BOUNDARY_CLASSIFICATION.risk_level has invalid value")


def test_schemas_glob_fails_when_used_instead_of_schema_glob(sample_payload):
    section(sample_payload, "NEXT_ACTION_CANDIDATE")["forbidden_scope"] = ["schemas/**"]

    assert_invalid(sample_payload, "must not use schemas/\\*\\*")


def test_missing_required_field_inside_section_fails(sample_payload):
    del section(sample_payload, "HUMAN_HANDOFF_NOTE")["final_authority"]

    assert_invalid(sample_payload, "HUMAN_HANDOFF_NOTE missing required field: final_authority")
