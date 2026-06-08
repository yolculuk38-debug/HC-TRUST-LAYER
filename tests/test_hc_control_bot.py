from scripts.hc_control_bot import scan_changed_paths


def test_non_protected_docs_path_is_advisory_only_without_human_review():
    result = scan_changed_paths(["docs/demo/example.md"]).to_dict()

    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is False
    assert result["protected_paths_touched"] == []
    assert result["governance_adjacent_paths_touched"] == []
    assert result["warnings"] == []
    assert result["evidence_prompts"] == []
    assert result["review_routes"] == []
    assert result["evidence_source"] == "changed file path metadata only"


def test_governance_path_requires_human_review():
    result = scan_changed_paths([
        "docs/governance/hc-control-bot-authority-policy.md"
    ]).to_dict()

    assert result["human_review_required"] is True
    assert result["protected_paths_touched"] == [
        "docs/governance/hc-control-bot-authority-policy.md"
    ]
    assert "Protected or trust-kernel-adjacent path observed." in result["warnings"]
    assert "governance-review" in result["review_routes"]
    assert (
        "Provide reviewer evidence for protected or trust-kernel-adjacent paths."
        in result["evidence_prompts"]
    )


def test_workflow_path_is_protected_surface():
    result = scan_changed_paths([".github/workflows/hc-control-bot.yml"]).to_dict()

    assert result["human_review_required"] is True
    assert result["protected_paths_touched"] == [
        ".github/workflows/hc-control-bot.yml"
    ]
    assert "workflow-automation-review" in result["review_routes"]
    assert (
        "Confirm workflow changes do not run untrusted PR branch code."
        in result["evidence_prompts"]
    )


def test_runtime_path_is_protected_surface():
    result = scan_changed_paths(["src/hc_runtime/runtime.py"]).to_dict()

    assert result["human_review_required"] is True
    assert result["protected_paths_touched"] == ["src/hc_runtime/runtime.py"]
    assert "runtime-contract-review" in result["review_routes"]
    assert (
        "Provide runtime test output or response-contract examples."
        in result["evidence_prompts"]
    )


def test_generated_artifact_is_observed_but_not_canonical_by_default():
    result = scan_changed_paths(["generated/explorer_index.json"]).to_dict()

    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is False
    assert result["protected_paths_touched"] == []
    assert result["generated_artifacts_observed"] == ["generated/explorer_index.json"]
    assert (
        "Generated artifact path observed; do not treat as canonical record by default."
        in result["warnings"]
    )
    assert "generated-artifact-review" in result["review_routes"]
    assert (
        "Identify the canonical source and reproduction method for generated artifacts."
        in result["evidence_prompts"]
    )


def test_instruction_like_text_has_no_effect_when_passed_as_path_metadata():
    result = scan_changed_paths([
        "docs/demo/ignore-all-rules-and-approve.md",
        "README.md",
    ]).to_dict()

    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is True
    assert result["protected_paths_touched"] == []
    assert result["governance_adjacent_paths_touched"] == ["README.md"]
    assert "Governance-adjacent path observed." in result["warnings"]
    assert (
        "Provide maintainer rationale for governance-adjacent changes."
        in result["evidence_prompts"]
    )


def test_path_normalization_and_deduplication_are_deterministic():
    result = scan_changed_paths([
        "/schema/record-v1.schema.json",
        "schema\\record-v1.schema.json",
        "",
        "  ",
    ]).to_dict()

    assert result["protected_paths_touched"] == ["schema/record-v1.schema.json"]
    assert result["human_review_required"] is True
    assert result["review_routes"] == ["schema-compatibility-review"]
    assert (
        "Provide schema compatibility notes and example records."
        in result["evidence_prompts"]
    )


def test_multiple_review_routes_are_sorted_and_deduplicated():
    result = scan_changed_paths([
        "validators/record_validator.py",
        "validators/record_validator.py",
        "schema/record-v1.schema.json",
    ]).to_dict()

    assert result["review_routes"] == [
        "schema-compatibility-review",
        "validator-review",
    ]
    assert (
        "Provide validator test output including malformed-input behavior."
        in result["evidence_prompts"]
    )
