from scripts.hc_pr_lifecycle_compliance_report import generate_report, render_markdown


def _event(**overrides):
    pr = {
        "number": 123,
        "title": "feat(control-bot): add report-only artifact",
        "state": "open",
        "draft": False,
        "body": "## Summary\nAdds report only artifact.\n## Testing\npytest\n## Scope\nSmall.\nHuman review required.",
        "updated_at": "2026-06-28T10:00:00Z",
        "base": {"ref": "main", "repo": {"full_name": "hc/HC-TRUST-LAYER"}},
        "head": {"ref": "feature", "sha": "abc123"},
    }
    pr.update(overrides.pop("pr", {}))
    event = {"repository": {"full_name": "hc/HC-TRUST-LAYER"}, "pull_request": pr}
    event.update(overrides)
    return event


def test_basic_report_generation_from_public_safe_input():
    report = generate_report(_event(), ["docs/example.md"], observed_at="2026-06-28T10:01:00Z")

    assert report["report_name"] == "HC Control Bot PR Lifecycle Compliance Report"
    assert report["repository"] == "hc/HC-TRUST-LAYER"
    assert report["pr_number"] == 123
    assert report["head_sha"] == "abc123"
    assert report["changed_files"] == ["docs/example.md"]
    assert "github_event_payload" in report["evidence_sources"]
    assert "changed_files" in report["evidence_sources"]
    assert render_markdown(report).startswith("# HC Control Bot PR Lifecycle Compliance Report")


def test_docs_only_changed_file_classification():
    report = generate_report(_event(), ["docs/project-control/example.md"])

    assert report["changed_file_categories"]["docs_touched"] is True
    assert report["changed_file_categories"]["code_touched"] is False
    assert report["changed_file_categories"]["tests_touched"] is False


def test_protected_path_signal_detection():
    report = generate_report(_event(), ["schema/record.schema.json"])

    assert report["changed_file_categories"]["schema_touched"] is True
    assert report["protected_path_signals"]["protected_path_touched"] is True
    assert "protected_path_touched_requires_human_review" in report["blockers_for_human_review"]


def test_canonical_trust_kernel_root_artifact_detection():
    report = generate_report(_event(), ["protocol-graph.json", "verification-map.json", "trust-kernel-index.json"])

    assert report["changed_file_categories"]["canonical_trust_kernel_artifacts_touched"] is True
    assert report["protected_path_signals"]["canonical_trust_kernel_root_artifact_touched"] is True
    assert "canonical_trust_kernel_artifact_touched_requires_human_review" in report["blockers_for_human_review"]


def test_pr_body_title_metadata_staleness_signal():
    report = generate_report(
        _event(pr={"title": "", "body": "", "updated_at": "2026-06-28T10:05:00Z"}),
        ["docs/example.md"],
        metadata_observed_at="2026-06-28T10:00:00Z",
    )

    assert "pr_title_missing" in report["blockers_for_human_review"]
    assert "pr_body_missing" in report["blockers_for_human_review"]
    assert "pr_metadata_stale" in report["warnings"]


def test_head_sha_staleness_signal():
    report = generate_report(_event(expected_head_sha="oldsha"), ["docs/example.md"])

    assert "head_sha_stale" in report["warnings"]


def test_missing_evidence_fails_safe_into_human_review():
    report = generate_report({}, [])

    assert "missing_evidence_requires_human_review" in report["blockers_for_human_review"]
    assert "private_context_required" in report["evidence_sources"]
    assert "changed_files_missing" in report["evidence_sources"]
    assert "current_head_checks_unavailable" in report["not_evaluated"]
    assert "review_thread_state_unavailable" in report["not_evaluated"]


def test_no_authority_flags_remain_false():
    report = generate_report(_event(), ["docs/example.md"])

    for key in [
        "approval_authority",
        "merge_authority",
        "label_authority",
        "reviewer_request_authority",
        "assignment_authority",
        "issue_mutation_authority",
        "thread_resolution_authority",
        "governance_mutation_authority",
    ]:
        assert report[key] is False


def test_boundary_flags_remain_fixed():
    report = generate_report(_event(), ["docs/example.md"])

    assert report["advisory_only"] is True
    assert report["report_only"] is True
    assert report["public_safe"] is True
    assert report["truth_guarantee"] is False
    assert report["human_review_required"] is True
