import hashlib
import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft7Validator

from scripts.hc_council_report import build_council_run, main, verify_output_hash


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "hc_council_run.schema.json"
EXAMPLE_PATH = ROOT / "examples" / "hc_council_run.example.json"


FIXTURE = {
    "repository": "yolculuk38-debug/HC-TRUST-LAYER",
    "command": "/hc council review repo",
    "repo_ref": "main",
    "pr_number": None,
    "evidence_refs": [
        "docs/project-control/hc-multi-ai-council-orchestrator.md",
        "https://meet.google.com/eba-vwjy-jti",
    ],
    "session": {
        "source": "calendar_or_command",
        "meeting_link": "https://meet.google.com/eba-vwjy-jti",
        "started_at": "2026-07-07T10:00:00Z",
    },
    "model_outputs": [
        {
            "role": "engineering_reviewer",
            "provider": "local_fixture",
            "model": "manual-entry",
            "prompt": "Review HC Council local report-only direction.",
            "output": (
                "The first implementation should remain local, deterministic, "
                "and report-only."
            ),
            "evidence_refs": [
                "docs/project-control/hc-multi-ai-council-orchestrator.md"
            ],
            "uncertainty": "low",
        },
        {
            "role": "risk_reviewer",
            "provider": "local_fixture",
            "model": "manual-entry",
            "prompt": "Identify authority risks for HC Council.",
            "output": (
                "Do not allow model output to approve, merge, close, label, "
                "or mutate protected paths automatically."
            ),
            "evidence_refs": [
                "docs/project-control/hc-multi-ai-council-orchestrator.md"
            ],
            "uncertainty": "low",
        },
    ],
    "synthesis": {
        "summary": (
            "Local report-only council output is safe to record before provider "
            "adapters are added."
        ),
        "risks": [
            "provider_credentials_must_not_be_committed",
            "model_output_is_not_canonical_truth",
        ],
        "next_safe_actions": [
            "validate schema",
            "run local report-only fixture",
            "keep human final authority",
        ],
        "blocked_items": [
            "autonomous provider execution",
            "auto-merge",
            "credential handling",
        ],
    },
}


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_against_schema(payload):
    schema = load_json(SCHEMA_PATH)
    errors = sorted(Draft7Validator(schema).iter_errors(payload), key=str)
    assert errors == []


def expected_output_hash(payload):
    unsigned = deepcopy(payload)
    unsigned["verification"]["output_sha256"] = None
    canonical = json.dumps(unsigned, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def test_example_output_matches_schema_and_hash_contract():
    example = load_json(EXAMPLE_PATH)

    validate_against_schema(example)
    assert example["mode"] == "report_only"
    assert example["advisory_only"] is True
    assert example["public_safe"] is True
    assert example["truth_guarantee"] is False
    assert example["verification"]["output_sha256"] == expected_output_hash(example)
    assert verify_output_hash(example) is True


def test_build_council_run_is_deterministic_and_public_safe():
    first = build_council_run(FIXTURE)
    second = build_council_run(dict(reversed(list(FIXTURE.items()))))

    validate_against_schema(first)
    assert first == second
    assert first["operator"] == "human_supervised"
    assert first["verification"]["advisory_only"] is True
    assert first["verification"]["truth_guarantee"] is False
    assert first["verification"]["hash_algorithm"] == "sha256"


def test_model_output_hashes_are_content_hashes():
    report = build_council_run(FIXTURE)

    for item in report["model_outputs"]:
        expected = hashlib.sha256(item["output"].encode("utf-8")).hexdigest()
        assert item["output_sha256"] == expected


def test_verification_hash_excludes_self_reference():
    report = build_council_run(FIXTURE)
    changed = deepcopy(report)
    changed["verification"]["output_sha256"] = "0" * 64

    assert verify_output_hash(report) is True
    assert verify_output_hash(changed) is False


def test_cli_outputs_schema_valid_json(tmp_path, capsys):
    fixture = tmp_path / "fixture.json"
    fixture.write_text(json.dumps(FIXTURE), encoding="utf-8")

    exit_code = main([str(fixture)])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)
    assert exit_code == 0
    validate_against_schema(payload)
    assert payload["repository"] == "yolculuk38-debug/HC-TRUST-LAYER"
    assert verify_output_hash(payload) is True
