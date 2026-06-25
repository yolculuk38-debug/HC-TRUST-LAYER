import json
import subprocess
import sys
from pathlib import Path

import pytest

from scripts.check_hc_trust_engineer_output_contract import REQUIRED_MARKERS, validate_contract
from scripts.hc_trust_engineer_local_emitter import EmitterInputError, emit_from_file

FIXTURE = Path(
    "tests/fixtures/project_control/hc_trust_engineer_local_emitter_input_sample.json"
)
SCRIPT = Path("scripts/hc_trust_engineer_local_emitter.py")


def write_input(tmp_path, **updates):
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    for key, value in updates.items():
        if value is None:
            data.pop(key, None)
        else:
            data[key] = value
    path = tmp_path / "input.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def section(payload, name):
    return next(item for item in payload["outputs"] if item["section"] == name)


def test_valid_input_emits_json_that_passes_validate_contract():
    payload = emit_from_file(FIXTURE)

    validate_contract(payload)
    assert payload["repository"] == "HC-TRUST-LAYER"


def test_cli_success_prints_valid_json_to_stdout():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(FIXTURE)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert result.stderr == ""
    payload = json.loads(result.stdout)
    validate_contract(payload)


def test_invalid_chain_status_fails(tmp_path):
    path = write_input(tmp_path, chain_status="done")

    with pytest.raises(EmitterInputError, match="chain_status has invalid value"):
        emit_from_file(path)


def test_invalid_next_action_type_fails(tmp_path):
    path = write_input(tmp_path, next_action_type="open_pr")

    with pytest.raises(EmitterInputError, match="next_action_type has invalid value"):
        emit_from_file(path)


def test_invalid_risk_level_fails(tmp_path):
    path = write_input(tmp_path, risk_level="none")

    with pytest.raises(EmitterInputError, match="risk_level has invalid value"):
        emit_from_file(path)


def test_missing_required_input_field_fails(tmp_path):
    path = write_input(tmp_path, repository=None)

    with pytest.raises(EmitterInputError, match="missing required input field: repository"):
        emit_from_file(path)


def test_emitted_hard_boundary_markers_are_exact():
    payload = emit_from_file(FIXTURE)

    assert payload["hard_boundary_markers"] == REQUIRED_MARKERS


def test_emitted_forbidden_scope_includes_schema_glob():
    payload = emit_from_file(FIXTURE)

    forbidden_scope = section(payload, "NEXT_ACTION_CANDIDATE")["forbidden_scope"]
    assert "schema/**" in forbidden_scope


def test_emitted_forbidden_scope_does_not_include_schemas_glob(tmp_path):
    path = write_input(tmp_path, forbidden_scope=["records/**", "schemas/**"])
    payload = emit_from_file(path)

    forbidden_scope = section(payload, "NEXT_ACTION_CANDIDATE")["forbidden_scope"]
    assert "schemas/**" not in forbidden_scope
    assert "schema/**" in forbidden_scope


def test_failure_path_does_not_print_partial_json_to_stdout(tmp_path):
    path = write_input(tmp_path, risk_level="none")

    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(path)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert result.stdout == ""
    assert "risk_level has invalid value" in result.stderr
