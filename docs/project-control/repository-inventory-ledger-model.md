# Repository Inventory Ledger Model

Status: advisory operating model.

This model defines how HC-TRUST-LAYER classifies repository files, tests, docs, examples, workflows, records, schemas, and operator scripts without giving automation final authority.

## Goal

Keep a generated, reviewable inventory of repository surfaces so the operator can see:

- newest changed items first;
- source files and matching test anchors, including name-based or reference-based anchors;
- protected surfaces;
- reviewer-role suggestions;
- files that are active, test support, docs/example support, or review-needed;
- actor and PR trace evidence from local Git metadata when available.

The inventory is evidence. It is not permission for structural repository changes.

## Generator

The repository uses a report-only generator:

```bash
python scripts/hc_repo_inventory.py . --format json
python scripts/hc_repo_inventory.py . --format md
```

The generator scans repository roots and emits an advisory ledger ordered by last Git commit metadata when available. JSON output remains the compatibility surface for automation consumers. Markdown output adds operator-facing category views so humans can review current changes by surface without changing the underlying inventory data. Each file receives:

- `review_order`;
- `path`;
- `category`;
- `lifecycle`;
- `owner_role`;
- `protected_surface`;
- `direct_test_anchor`;
- last commit timestamp, SHA, and subject when Git history is available;
- last commit author and committer names from local Git metadata;
- best-effort PR number inferred only from squash-merge style subjects such as `Some subject (#123)`;
- best-effort commit URL when `remote.origin.url` points to GitHub.

## Markdown views

Markdown output includes these advisory sections:

1. Latest changes — all files
2. Tests — newest first
3. Source — newest first
4. Workflows — newest first
5. Docs — newest first
6. Records / schema / protected — newest first
7. Review-needed — priority first

The first six views keep the newest-first ordering from `review_order`. The review-needed view prioritizes protected review before other files that need human review. Entry tables include operator-friendly `Actor`, `PR`, and `Last commit` columns. These views are for review triage only and do not authorize changes.

## Categories

| Category | Meaning |
| --- | --- |
| `trust_layer_source` | Trust-layer implementation under `src/hc_trust/`. |
| `runtime_source` | Runtime implementation under `src/hc_runtime/`. |
| `source` | Other source implementation under `src/`. |
| `test` | Test files under `tests/` or root `test_integration.py`. |
| `operator_script` | Local operator/report/planner scripts under `scripts/`. |
| `project_control_doc` | Project-control docs under `docs/project-control/`. |
| `documentation` | Other documentation under `docs/`. |
| `example` | Example fixtures and demo material under `examples/`. |
| `github_workflow` | GitHub Actions workflows under `.github/workflows/`. |
| `record`, `schema`, `validator`, `policy`, `signature_material`, `federation` | Protected or trust-kernel-adjacent surfaces. |

## Lifecycle values

| Lifecycle | Meaning |
| --- | --- |
| `active_with_test_anchor` | Source or script file has an obvious matching test file by name or test-file reference. |
| `test_support` | Test file or integration script. |
| `docs_or_example_support` | Documentation or example surface. |
| `protected_review_required` | Protected or trust-kernel-adjacent surface. |
| `review_needed_without_direct_test_anchor` | Source or script needs evidence review before any structural proposal. |
| `inventory_only_review_needed` | File is only classified for review; no action is authorized. |

## Actor and PR trace fields

The inventory separates responsibility from authorship. `owner_role` is a CODEOWNERS-like review responsibility hint. It is not the author of a file and does not grant merge authority.

Trace fields are local Git evidence for operator review:

| Field | Meaning | Boundary |
| --- | --- | --- |
| `last_commit_author_name` | Name recorded as the author of the last Git change for the file. | Git metadata only; not identity finality. |
| `last_commit_committer_name` | Name recorded as the committer of the last Git change for the file. | Git metadata only; may differ from author. |
| `last_commit_pr_number` | Best-effort PR number parsed from a subject ending like `(#123)`. | `null` when the subject does not expose a number. |
| `last_commit_url` | Best-effort GitHub commit URL built from `remote.origin.url` and the commit SHA. | `null` when the remote is missing or not a GitHub URL. |

The generator uses local Git history only and does not call the GitHub API. These fields provide audit evidence for HC:// review workflows. They are not legal truth, identity finality, certification, production readiness, or guaranteed correctness. Human final authority remains required.

## Automation boundary

The generated inventory remains:

- advisory-only;
- public-safe;
- `truth_guarantee=false`;
- inventory-only;
- non-mutating.

The generator must not approve, reject, merge, close, label, assign, request reviewers, rewrite records, change protected configuration, or create authority-changing behavior.

## GitHub automation model

The workflow runs as report-only and uploads generated JSON/Markdown as artifacts. It uses read-only repository permissions and does not commit generated output back to `main` automatically.

This follows the HC governance boundary:

```text
AI assists.
CI reports.
Governance constrains.
Audit records.
Human final authority remains.
```

## Practical examples

- A new test file should appear near the top after merge and be categorized as `test` with lifecycle `test_support`.
- A workflow change should be categorized as `github_workflow`, marked `protected_surface=true`, and routed to `protected-surface-reviewer`.
- A source or script file without a direct test anchor should be classified as review-needed, not as an action target. Test anchors may be name-based, such as `tests/test_<source>_*.py`, or reference-based when a test imports or references the source module or script name.
- A record/schema/policy/signature/federation file should never be changed based on inventory output alone.

## Next improvement path

1. Generate the inventory artifact on PRs and manual workflow dispatch.
2. Review the newest entries first.
3. Convert repeated findings into small scoped PRs.
4. Add CODEOWNERS or ruleset review requirements only after the inventory model is stable and human-approved.
