from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "hc_pr_lifecycle_compliance_report.py"
SPEC = spec_from_file_location("hc_pr_lifecycle_compliance_report", MODULE_PATH)
MODULE = module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

build_report = MODULE.build_report
read_changed_files = MODULE.read_changed_files


def report_for(*paths: str):
    return build_report(list(paths))


def test_workflow_and_bot_surface_reports_protected_path_touched_true():
    report = report_for(".github/workflows/hc-pr-lifecycle-compliance-report.yml")

    assert report.protected_path_touched is True
    assert report.workflow_or_bot_surface_touched is True
    assert report.human_review_required is True
    assert report.blockers_for_human_review


def test_validators_reports_protected_path_touched_true():
    report = report_for("validators/hc_validator.py")

    assert report.protected_path_touched is True
    assert report.validator_surface_touched is True
    assert report.human_review_required is True


def test_src_hc_runtime_reports_protected_path_touched_true():
    report = report_for("src/hc_runtime/engine.py")

    assert report.protected_path_touched is True
    assert report.runtime_surface_touched is True
    assert report.human_review_required is True


def test_records_reports_protected_path_touched_true():
    report = report_for("records/example.json")

    assert report.protected_path_touched is True
    assert report.records_surface_touched is True
    assert report.human_review_required is True


def test_codeowners_reports_protected_path_touched_true():
    report = report_for("CODEOWNERS")

    assert report.protected_path_touched is True
    assert report.codeowners_touched is True
    assert report.human_review_required is True


def test_docs_project_control_reports_protected_path_touched_true():
    report = report_for("docs/project-control/hc-control-bot.md")

    assert report.protected_path_touched is True
    assert report.project_control_surface_touched is True
    assert report.human_review_required is True


def test_canonical_root_artifacts_report_protected_and_canonical_root_signals():
    for path in ("protocol-graph.json", "verification-map.json", "trust-kernel-index.json"):
        report = report_for(path)

        assert report.protected_path_touched is True
        assert report.canonical_root_artifact_touched is True
        assert report.generated_or_canonical_surface_touched is True
        assert report.human_review_required is True


def test_missing_evidence_fails_safe_into_human_review(tmp_path):
    changed_files, missing = read_changed_files(tmp_path / "missing-changed-files.txt")
    report = build_report(changed_files, evidence_missing=missing)

    assert missing is True
    assert report.evidence_missing is True
    assert report.protected_path_touched is True
    assert report.human_review_required is True
    assert "changed_files" in report.not_evaluated
    assert report.blockers_for_human_review


def test_authority_flags_remain_false():
    report = report_for("docs/index.md")

    assert report.approval_authority is False
    assert report.merge_authority is False
    assert report.label_authority is False
    assert report.reviewer_request_authority is False
    assert report.assignment_authority is False
    assert report.issue_mutation_authority is False
    assert report.thread_resolution_authority is False
    assert report.governance_mutation_authority is False


def test_boundary_flags_remain_correct():
    report = report_for("docs/index.md")

    assert report.advisory_only is True
    assert report.report_only is True
    assert report.public_safe is True
    assert report.truth_guarantee is False


def test_dependency_files_remain_protected_review_sensitive_surface():
    report = report_for("pyproject.toml")

    assert report.protected_path_touched is True
    assert report.dependency_surface_touched is True
    assert report.human_review_required is True


def test_workflow_runs_reporter_from_trusted_base_and_pr_content_as_data():
    workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/hc-pr-lifecycle-compliance-report.yml").read_text(
        encoding="utf-8"
    )

    assert "pull_request:" in workflow
    assert "pull_request_target" not in workflow
    assert "contents: read" in workflow
    assert "pull-requests: read" in workflow
    assert "path: trusted-base" in workflow
    assert "path: pr-data" in workflow
    assert "working-directory: trusted-base" in workflow
    assert "python scripts/hc_pr_lifecycle_compliance_report.py" in workflow
    assert "working-directory: pr-data" in workflow
    assert 'git fetch --no-tags --prune origin "${BASE_SHA}"' in workflow
    assert "${BASE_SHA}...${HEAD_SHA}" in workflow
    assert "--output report.json" in workflow
    assert "trusted_base_reporter_missing" in workflow
    assert "full lifecycle compliance report is not evaluated" in workflow
    assert "human maintainer must review manually" in workflow
    assert "does not claim checks passed" in workflow
    assert "does not claim merge-readiness" in workflow
    assert "does not run PR-head reporter code" in workflow
    assert "trusted-base/report.json" in workflow
    assert "trusted-base/summary.md" in workflow
    assert "actions/upload-artifact" in workflow
    assert "issues: write" not in workflow
    assert "pull-requests: write" not in workflow
    assert "secrets." not in workflow
    assert "GITHUB_TOKEN" not in workflow
