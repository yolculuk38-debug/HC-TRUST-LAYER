#!/usr/bin/env python3
"""Report-only workflow taxonomy drift checker for HC Control Bot.

The checker treats changed file paths as data. It does not call the network,
GitHub APIs, secrets, labels, comments, approvals, reviewer requests, or merge
operations. All normal outcomes exit 0 and remain advisory for human review.
"""

from __future__ import annotations

import argparse
from pathlib import PurePosixPath
from typing import Iterable, Sequence

TAXONOMY_PATH = "docs/project-control/workflow-taxonomy.md"
WARNING_MESSAGE = "Workflow files changed without workflow taxonomy update. Human review required."
SECTION_TITLE = "## HC Workflow Taxonomy Drift"


def normalize_path(path: str) -> str:
    """Normalize a changed path for deterministic POSIX-style matching."""
    normalized = path.strip().replace("\\", "/")
    while "//" in normalized:
        normalized = normalized.replace("//", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    if normalized in {"", "."}:
        return ""
    return str(PurePosixPath(normalized))


def unique_normalized_paths(paths: Iterable[str]) -> list[str]:
    """Return sorted, de-duplicated, normalized paths."""
    return sorted({normalized for path in paths if (normalized := normalize_path(path))})


def is_workflow_path(path: str) -> bool:
    """Return True when a path is under .github/workflows/."""
    return path.startswith(".github/workflows/") and path != ".github/workflows"


def analyze_changed_paths(paths: Iterable[str]) -> dict[str, object]:
    """Classify changed paths for workflow taxonomy drift reporting."""
    changed_paths = unique_normalized_paths(paths)
    workflow_paths = [path for path in changed_paths if is_workflow_path(path)]
    taxonomy_changed = TAXONOMY_PATH in changed_paths

    if not workflow_paths:
        status = "ok"
        message = "No workflow file changes detected."
        human_review_required = False
    elif taxonomy_changed:
        status = "ok"
        message = "Workflow taxonomy update was detected for changed workflow files."
        human_review_required = True
    else:
        status = "warning"
        message = WARNING_MESSAGE
        human_review_required = True

    return {
        "status": status,
        "message": message,
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "human_review_required": human_review_required,
        "workflow_paths": workflow_paths,
        "taxonomy_changed": taxonomy_changed,
        "expected_taxonomy_path": TAXONOMY_PATH,
        "blocks_merge": False,
    }


def _bool_text(value: object) -> str:
    return "true" if value else "false"


def render_markdown(result: dict[str, object]) -> str:
    """Render a GitHub step-summary friendly Markdown report."""
    workflow_paths = result["workflow_paths"]
    assert isinstance(workflow_paths, list)

    lines = [
        SECTION_TITLE,
        "",
        f"- status: {result['status']}",
        f"- message: {result['message']}",
        f"- advisory_only={_bool_text(result['advisory_only'])}",
        f"- public_safe={_bool_text(result['public_safe'])}",
        f"- truth_guarantee={_bool_text(result['truth_guarantee'])}",
        f"- human_review_required={_bool_text(result['human_review_required'])}",
        f"- expected_taxonomy_path: `{result['expected_taxonomy_path']}`",
        "- merge_blocking: false",
        "- note: This report is advisory only and does not block merge.",
        "",
        "Changed workflow files:",
    ]
    if workflow_paths:
        lines.extend(f"- `{path}`" for path in workflow_paths)
    else:
        lines.append("- None")
    lines.append("")
    return "\n".join(lines)


def read_paths_file(path: str | None) -> list[str]:
    if not path:
        return []
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read().splitlines()
    except OSError as exc:
        return [f"__hc_input_read_warning__/{type(exc).__name__}"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Report workflow taxonomy drift for HC Control Bot.")
    parser.add_argument("paths", nargs="*", help="Changed file paths treated as data.")
    parser.add_argument("--paths-file", help="Text file containing one changed path per line.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = [*read_paths_file(args.paths_file), *args.paths]
    print(render_markdown(analyze_changed_paths(paths)))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
