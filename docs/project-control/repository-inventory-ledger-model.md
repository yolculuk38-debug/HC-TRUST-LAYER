# Repository Inventory Ledger Model

Status: advisory operating model.

This model defines how HC-TRUST-LAYER classifies repository files, tests, docs, examples, workflows, records, schemas, and operator scripts without giving automation final authority.

## Goal

Keep a generated, reviewable inventory of repository surfaces so the operator can see:

- newest changed items first;
- source files and matching test anchors;
- protected surfaces;
- reviewer-role suggestions;
- files that are active, test support, docs/example support, or review-needed.

The inventory is evidence. It is not permission for structural repository changes.

## Generator

The repository uses a report-only generator:

```bash
python scripts/hc_repo_inventory.py . --format json
python scripts/hc_repo_inventory.py . --format md
```

The generator scans repository roots and emits an advisory ledger ordered by last Git commit metadata when available. Each file receives:

- `review_order`;
- `path`;
- `category`;
- `lifecycle`;
- `owner_role`;
- `protected_surface`;
- `direct_test_anchor`;
- last commit timestamp, SHA, and subject when Git history is available.

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
| `active_with_test_anchor` | Source file has an obvious matching test file. |
| `test_support` | Test file or integration script. |
| `docs_or_example_support` | Documentation or example surface. |
| `protected_review_required` | Protected or trust-kernel-adjacent surface. |
| `review_needed_without_direct_test_anchor` | Source or script needs evidence review before any structural proposal. |
| `inventory_only_review_needed` | File is only classified for review; no action is authorized. |

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
- A source file without a direct test anchor should be classified as review-needed, not as an action target.
- A record/schema/policy/signature/federation file should never be changed based on inventory output alone.

## Next improvement path

1. Generate the inventory artifact on PRs and manual workflow dispatch.
2. Review the newest entries first.
3. Convert repeated findings into small scoped PRs.
4. Add CODEOWNERS or ruleset review requirements only after the inventory model is stable and human-approved.
