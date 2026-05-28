from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_pr_governance.py"
SPEC = spec_from_file_location("check_pr_governance", MODULE_PATH)
MODULE = module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

RiskLevel = MODULE.RiskLevel
render_summary = MODULE.render_summary
summarize_governance = MODULE.summarize_governance
apply_label_overrides = MODULE.apply_label_overrides


def test_docs_only_is_low_risk_and_auto_merge_eligible():
    summary = summarize_governance(["docs/verification-map.md", "README.md"])

    assert summary.risk == RiskLevel.LOW
    assert summary.auto_merge_eligible is True
    assert summary.human_review_required is False
    assert summary.protected_paths_touched is False


def test_dependency_only_is_low_risk_and_auto_merge_eligible():
    summary = summarize_governance(["pyproject.toml", "poetry.lock"])

    assert summary.risk == RiskLevel.LOW
    assert summary.auto_merge_eligible is True
    assert summary.human_review_required is False


def test_tests_only_is_low_risk_and_auto_merge_eligible():
    summary = summarize_governance(["tests/test_trust_engine.py", "tests/test_api_schema.py"])

    assert summary.risk == RiskLevel.LOW
    assert summary.auto_merge_eligible is True


def test_protected_paths_are_high_risk_never_auto_merge_and_require_human_review():
    high_risk_paths = [
        "schema/record-v1.schema.json",
        "validators/core_validator.py",
        "signatures/signer.py",
        "policy/routing.yaml",
        "federation/sync.py",
        ".github/workflows/ci.yml",
        "src/hc_runtime/pipeline.py",
    ]

    for changed_path in high_risk_paths:
        summary = summarize_governance([changed_path, "docs/index.md"])

        assert summary.risk == RiskLevel.HIGH
        assert summary.protected_paths_touched is True
        assert summary.auto_merge_eligible is False
        assert summary.human_review_required is True


def test_mixed_non_protected_changes_are_medium_risk():
    summary = summarize_governance(["src/trust_engine.py", "docs/index.md"])

    assert summary.risk == RiskLevel.MEDIUM
    assert summary.auto_merge_eligible is False
    assert summary.human_review_required is True


def test_rendered_output_includes_required_control_fields(capsys):
    changed_paths = ["docs/verification-map.md"]
    summary = summarize_governance(changed_paths)

    render_summary(summary, changed_paths)
    output = capsys.readouterr().out

    assert "RISK:" in output
    assert "AUTO_MERGE_ELIGIBLE:" in output
    assert "HUMAN_REVIEW_REQUIRED:" in output
    assert "PROTECTED_PATHS_TOUCHED:" in output


def test_manual_review_overrides_auto_merge_label_conflict():
    summary = summarize_governance(["docs/verification-map.md"])
    result = apply_label_overrides(summary, {"manual-review", "auto-merge"})

    assert result.auto_merge_eligible is False
    assert result.human_review_required is True
    assert result.override_reason is not None
    assert "manual-review overrides auto-merge" in result.override_reason


def test_risk_high_with_auto_merge_forces_human_review():
    summary = summarize_governance(["docs/verification-map.md"])
    result = apply_label_overrides(summary, {"risk-high", "auto-merge"})

    assert result.auto_merge_eligible is False
    assert result.human_review_required is True
    assert result.override_reason is not None
    assert "risk-high is not eligible for auto-merge" in result.override_reason


def test_blocked_human_review_with_auto_merge_forces_human_review():
    summary = summarize_governance(["docs/verification-map.md"])
    result = apply_label_overrides(summary, {"blocked-human-review", "auto-merge"})

    assert result.auto_merge_eligible is False
    assert result.human_review_required is True
    assert result.override_reason is not None
    assert "blocked-human-review disallows auto-merge" in result.override_reason
