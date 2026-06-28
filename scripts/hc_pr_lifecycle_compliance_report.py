#!/usr/bin/env python3
"""Generate a report-only HC Control Bot PR lifecycle compliance artifact.

Stdlib-only, deterministic, public-safe, and non-mutating. The generator reads
local JSON/event evidence plus local changed-file lists and writes report.json
and summary.md for human review.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPORT_NAME = "HC Control Bot PR Lifecycle Compliance Report"
REPORT_VERSION = "0.1.0"
GENERATED_BY = "hc-pr-lifecycle-compliance-report"
SEVERITIES = {"info", "advisory", "warning", "hold_for_human_review"}

AUTHORITY_FLAGS = {
    "approval_authority": False,
    "merge_authority": False,
    "label_authority": False,
    "reviewer_request_authority": False,
    "assignment_authority": False,
    "issue_mutation_authority": False,
    "thread_resolution_authority": False,
    "governance_mutation_authority": False,
}
BOUNDARY_FLAGS = {
    "advisory_only": True,
    "report_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}

CANONICAL_ROOT_ARTIFACTS = {
    "protocol-graph.json",
    "verification-map.json",
    "trust-kernel-index.json",
}
PROTECTED_SURFACE_PREFIXES = (
    ".github/",
    "validators/",
    "src/hc_runtime/",
    "records/",
    "docs/project-control/",
    "schema/",
    "policy/",
    "federation/",
    "signing/",
    "signatures/",
    "canonical/",
    "generated/",
)
PROTECTED_SURFACE_FILES = {"CODEOWNERS", *CANONICAL_ROOT_ARTIFACTS}
PACKAGE_FILES = {
    "package.json", "package-lock.json", "npm-shrinkwrap.json", "yarn.lock",
    "pnpm-lock.yaml", "pyproject.toml", "poetry.lock", "requirements.txt",
    "requirements-dev.txt", "Pipfile", "Pipfile.lock", "Cargo.toml", "Cargo.lock",
    "go.mod", "go.sum", "Gemfile", "Gemfile.lock",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def load_json(path: str | None) -> dict[str, Any]:
    if not path:
        return {}
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    return data if isinstance(data, dict) else {}


def load_changed_files(path: str | None) -> list[str]:
    if not path:
        return []
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle) if path.endswith(".json") else handle.read().splitlines()
    if isinstance(data, dict):
        data = data.get("changed_files", [])
    if not isinstance(data, list):
        return []
    return sorted({str(item).replace("\\", "/").strip() for item in data if str(item).strip()})


def pr_from_event(event: dict[str, Any]) -> dict[str, Any]:
    pr = event.get("pull_request") if isinstance(event.get("pull_request"), dict) else event
    base = pr.get("base") if isinstance(pr.get("base"), dict) else {}
    head = pr.get("head") if isinstance(pr.get("head"), dict) else {}
    repo = pr.get("base", {}).get("repo", {}) if isinstance(pr.get("base"), dict) else {}
    return {
        "repository": event.get("repository", {}).get("full_name") or repo.get("full_name") or "unknown",
        "pr_number": pr.get("number") or event.get("number"),
        "pr_title": pr.get("title") or "",
        "pr_state": pr.get("state") or "unknown",
        "draft": bool(pr.get("draft", False)),
        "base_branch": base.get("ref") or "unknown",
        "head_branch": head.get("ref") or "unknown",
        "head_sha": head.get("sha") or "",
        "pr_updated_at": pr.get("updated_at") or "",
        "pr_body": pr.get("body") or "",
    }


def categorize(paths: list[str]) -> dict[str, bool]:
    cats = {name: False for name in [
        "docs_touched", "code_touched", "tests_touched", "workflows_touched",
        "scripts_touched", "templates_touched", "schema_touched", "validators_touched",
        "records_evidence_touched", "generated_artifacts_touched",
        "canonical_trust_kernel_artifacts_touched", "policy_touched", "federation_touched",
        "signing_signatures_touched", "demo_fixtures_touched", "package_dependency_files_touched",
    ]}
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        ext = Path(path).suffix
        cats["docs_touched"] |= path.startswith("docs/") or ext in {".md", ".rst", ".txt"}
        cats["code_touched"] |= path.startswith("src/") or ext in {".py", ".js", ".ts", ".rs", ".go", ".java"}
        cats["tests_touched"] |= path.startswith("tests/") or "/test" in path or name.startswith("test_")
        cats["workflows_touched"] |= path.startswith(".github/workflows/")
        cats["scripts_touched"] |= path.startswith("scripts/")
        cats["templates_touched"] |= "template" in path.lower() or path.startswith(".github/ISSUE_TEMPLATE")
        cats["schema_touched"] |= path.startswith("schema/")
        cats["validators_touched"] |= path.startswith("validators/") or "validator" in path.lower()
        cats["records_evidence_touched"] |= path.startswith("records/") or "evidence" in path.lower()
        cats["generated_artifacts_touched"] |= path.startswith("generated/")
        cats["canonical_trust_kernel_artifacts_touched"] |= path.startswith("canonical/") or name in CANONICAL_ROOT_ARTIFACTS
        cats["policy_touched"] |= path.startswith("policy/")
        cats["federation_touched"] |= path.startswith("federation/")
        cats["signing_signatures_touched"] |= path.startswith(("signing/", "signatures/")) or "signature" in path.lower()
        cats["demo_fixtures_touched"] |= path.startswith("docs/demo/fixtures/")
        cats["package_dependency_files_touched"] |= name in PACKAGE_FILES
    return cats


def finding(severity: str, title: str, detail: str) -> dict[str, str]:
    assert severity in SEVERITIES
    return {"severity": severity, "title": title, "detail": detail}


def generate_report(event: dict[str, Any], changed_files: list[str], observed_at: str | None = None, metadata_observed_at: str | None = None) -> dict[str, Any]:
    observed_at = observed_at or utc_now()
    metadata_observed_at = metadata_observed_at or observed_at
    pr = pr_from_event(event)
    cats = categorize(changed_files)
    findings = [finding("info", "Boundary", "Report is advisory-only, report-only, public-safe, and requires human review.")]
    warnings: list[str] = []
    blockers: list[str] = []
    not_evaluated: list[str] = []
    followups: list[str] = []

    if not pr["pr_number"] or not pr["head_sha"] or not changed_files:
        blockers.append("missing_evidence_requires_human_review")
        findings.append(finding("hold_for_human_review", "Missing evidence", "Required PR identity, head SHA, or changed-file evidence is missing."))
    if not pr["pr_title"]:
        blockers.append("pr_title_missing")
        findings.append(finding("hold_for_human_review", "PR title missing", "PR title evidence is missing."))
    if not pr["pr_body"]:
        blockers.append("pr_body_missing")
        findings.append(finding("hold_for_human_review", "PR body missing", "PR body evidence is missing."))

    body = pr["pr_body"].lower()
    sections = {key: (key in body) for key in ["summary", "testing", "scope", "out of scope", "human review"]}
    if pr["pr_updated_at"] and metadata_observed_at:
        updated = parse_time(pr["pr_updated_at"])
        observed = parse_time(metadata_observed_at)
        if updated and observed and updated > observed:
            warnings.append("pr_metadata_stale")
            findings.append(finding("warning", "PR metadata may be stale", "PR metadata updated after the supplied metadata observation time."))
    if event.get("expected_head_sha") and event.get("expected_head_sha") != pr["head_sha"]:
        warnings.append("head_sha_stale")
        findings.append(finding("warning", "Head SHA mismatch", "Expected head SHA does not match observed PR head SHA."))

    protected_touched = any(p.startswith(PROTECTED_SURFACE_PREFIXES) or p in PROTECTED_SURFACE_FILES for p in changed_files)
    workflow_bot_surface = cats["workflows_touched"] or any("bot" in p.lower() for p in changed_files)
    authority_adjacent = workflow_bot_surface or cats["templates_touched"]
    if protected_touched:
        blockers.append("protected_path_touched_requires_human_review")
        findings.append(finding("hold_for_human_review", "Protected path touched", "Protected or trust-kernel-adjacent path evidence requires human review."))
    if cats["canonical_trust_kernel_artifacts_touched"]:
        blockers.append("canonical_trust_kernel_artifact_touched_requires_human_review")
    if authority_adjacent and "report" not in body:
        warnings.append("authority_adjacent_surface_without_explicit_report_context")

    not_evaluated.extend(["review_window_evidence_unavailable", "current_head_checks_unavailable", "review_thread_state_unavailable"])

    return {
        "report_name": REPORT_NAME, "report_version": REPORT_VERSION, **BOUNDARY_FLAGS, **AUTHORITY_FLAGS,
        **{k: v for k, v in pr.items() if k != "pr_body"},
        "pr_metadata_observed_at": metadata_observed_at, "observed_at": observed_at,
        "evidence_sources": ["github_event_payload" if event else "private_context_required", "changed_files" if changed_files else "changed_files_missing"],
        "lifecycle_summary": {"pr_body_present": bool(pr["pr_body"]), "pr_title_present": bool(pr["pr_title"]), "body_sections_detected": sections},
        "changed_files": changed_files, "changed_file_categories": cats,
        "protected_path_signals": {"protected_path_touched": protected_touched, "canonical_trust_kernel_root_artifact_touched": cats["canonical_trust_kernel_artifacts_touched"], "workflow_ci_bot_surface_touched": workflow_bot_surface, "authority_adjacent_surface_touched": authority_adjacent},
        "findings": findings, "warnings": warnings, "blockers_for_human_review": blockers,
        "not_evaluated": not_evaluated, "followups": followups,
        "generated_by": GENERATED_BY, "generated_at": utc_now(),
    }


def render_markdown(report: dict[str, Any]) -> str:
    sig = report["protected_path_signals"]
    return "\n".join([
        f"# {REPORT_NAME}", "", "## Boundary",
        "- advisory_only=true", "- report_only=true", "- public_safe=true", "- truth_guarantee=false", "- human_review_required=true", "- Human maintainer makes the final decision.",
        "", "## PR identity", f"- PR: {report.get('pr_number')}", f"- Title present: {bool(report.get('pr_title'))}", f"- State: {report.get('pr_state')}", f"- Draft: {report.get('draft')}", f"- Base: {report.get('base_branch')}", f"- Head: {report.get('head_branch')} @ {report.get('head_sha')}",
        "", "## Scope signals", *[f"- {k}: {v}" for k, v in sorted(report["changed_file_categories"].items())],
        "", "## Protected path signals", *[f"- {k}: {v}" for k, v in sorted(sig.items())],
        "", "## Review-window signal", "- not_evaluated: review_window_evidence_unavailable",
        "", "## Current-head checks signal", "- not_evaluated: current_head_checks_unavailable",
        "", "## Review comments/thread signal", "- not_evaluated: review_thread_state_unavailable",
        "", "## Authority boundary signal", *[f"- {k}=false" for k in AUTHORITY_FLAGS],
        "", "## Human review note", "- This report is advisory evidence only. Human maintainer makes the final decision.",
        "", "## Follow-ups", *([f"- {item}" for item in report.get("followups", [])] or ["- None"]), "",
    ])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event-json")
    parser.add_argument("--changed-files")
    parser.add_argument("--output-dir", default="reports/hc-pr-lifecycle-compliance")
    parser.add_argument("--observed-at")
    parser.add_argument("--metadata-observed-at")
    args = parser.parse_args()
    report = generate_report(load_json(args.event_json), load_changed_files(args.changed_files), args.observed_at, args.metadata_observed_at)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (out / "summary.md").write_text(render_markdown(report), encoding="utf-8")
    print("HC PR lifecycle compliance report generated: advisory-only/report-only; human review remains required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
