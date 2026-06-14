# HC Release Audit Model

Status: advisory local audit model.

The HC release audit checker provides deterministic, local-only evidence for release review. It is report-only and bounded by `advisory_only=true`, `public_safe=true`, and `truth_guarantee=false`.

## What the checker reports

`python scripts/hc_release_audit.py --format md` reports:

- `release_files_changed` from local Git changes when available;
- `changelog_evidence`;
- `task_ledger_evidence`;
- `pr_reference_evidence`;
- `missing_evidence`;
- `human_review_required=true`;
- `merge_ready=false` unless evidence is complete and human review still remains required.

## Boundaries

The checker must not:

- publish releases;
- create tags;
- modify the changelog automatically;
- create release authority;
- claim production readiness, legal truth, identity finality, forensic certainty, certification authority, or guaranteed correctness.

Release evidence is an operator aid. Human final authority remains required before any release action.
