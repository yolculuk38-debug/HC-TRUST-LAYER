# Push-to-Main Duplication Review — 2026-06-16

## 1. Executive summary

This document is a report-only review of workflows that may create duplicated CI evidence by running on both pull request events and `push` to `main`.

No workflow files are changed by this report. No workflows are deleted, disabled, renamed, moved, or edited. No workflow runs are deleted. No source, tests, generated artifacts, records, schemas, validators, policy, federation, signatures, canonical files, trust-kernel files, issues, branches, or pull requests are changed.

This review follows the workflow run noise audit and the auto-merge policy overlap review. Its purpose is to separate useful post-merge audit evidence from avoidable duplicate workflow runs.

Boundary values preserved by this review:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- human final authority remains required
- CI/checks are evidence, not trust authority
- workflow checks do not grant merge authority

## 2. Review scope

This report reviews workflow run duplication patterns, not workflow correctness.

Primary duplication pattern:

- a workflow runs on `pull_request` before merge;
- the same or similar workflow runs again on `push` to `main` after merge;
- Actions UI run counts grow quickly even when all runs are legitimate.

This can be useful if the post-merge run creates independent main-branch audit evidence. It can be noisy if the main-branch run repeats the same evidence without adding a distinct post-merge assurance value.

## 3. Candidate workflow categories

The earlier workflow cleanup recommendation identified several workflows that run on both PR and main-push style contexts or otherwise add repeated evidence.

| Category | Example workflows | Why it may duplicate | Why it may be useful | Review recommendation |
| --- | --- | --- | --- | --- |
| Documentation consistency | `docs-drift.yml`, terminology-related checks | PR checks already validate docs changes before merge. | Post-merge run proves main still satisfies documentation rules. | KEEP for now; consider documenting main-push purpose before changing. |
| Canonical / artifact boundary | `canonical-artifacts.yml` | PR guard and main guard can both run. | Main-branch canonical boundary evidence is valuable after merge. | KEEP_SECURITY_OR_GOVERNANCE. |
| Validation / verification | `validate.yml`, `verification-package-schema.yml` | Runtime/schema checks can run on PR and again after merge. | Main branch validation evidence is important for release confidence. | KEEP unless a targeted review proves safe path filtering. |
| Repository inventory / release audit | `hc-repo-inventory.yml`, `release-audit.yml` | Can add visible run volume after many PRs. | Produces operator/audit evidence tied to main state. | KEEP until evidence retention policy exists. |
| Archive / provenance | `archive.yml`, `verify-archive.yml`, `auto-hash.yml` | Push-driven evidence may add runs outside PR checks. | Provenance and generated hash/archive checks are sensitive. | HUMAN_REVIEW_REQUIRED; do not reduce in noise cleanup. |
| Auto-merge policy reports | `enable-auto-merge.yml`, `safe-auto-merge.yml`, `docs-auto-merge.yml` | Multiple policy-report checks can run around each PR. | They preserve the no-autonomous-merge boundary. | Use the separate auto-merge overlap review first. |

## 4. Safe interpretation

A post-merge `push` to `main` run is not automatically waste.

It is useful when it answers a different question than the PR run:

- PR run: "Is this proposed change safe to merge?"
- main-push run: "Is the canonical main branch still safe after merge?"

It is likely noise when:

- it repeats the same report without adding main-branch-specific evidence;
- it does not upload, summarize, or validate anything that differs from the PR run;
- it is auto-merge-adjacent wording only and already covered by a clearer policy report;
- it runs for docs-only changes even though path filters could safely narrow it.

## 5. Reduction options for future implementation

No implementation change is recommended in this report.

Potential future options, each requiring separate human review:

1. Add clearer documentation to workflows that intentionally run on both PR and `main` push.
2. Add or refine `paths` filters only for low-risk docs/report workflows.
3. Keep post-merge runs for governance, security, canonical, release, provenance, validation, terminology, and generated-evidence workflows unless a replacement exists.
4. Prefer reducing duplicate policy-report checks before touching validation or provenance workflows.
5. Avoid disabling `push` to `main` checks that serve as canonical main-branch evidence.

## 6. Required gate before any workflow edit

Before editing `.github/workflows/**`, require all of the following:

- live open PR state is known;
- the workflow's PR and main-push purposes are documented;
- before/after trigger behavior is documented;
- before/after permissions are documented;
- no new write permissions are added;
- no human review requirement is removed;
- no canonical, provenance, release, policy, security, terminology, validation, schema, record, or trust-kernel protection is weakened;
- normal CI/checks pass;
- a human maintainer explicitly approves the behavior change.

## 7. Stop conditions

Stop and do not change workflows if any of the following are true:

- the workflow has write permissions;
- the workflow writes comments, labels, generated artifacts, records, hashes, or repository content;
- the workflow protects governance, policy, release, provenance, validation, terminology, canonical artifacts, schemas, validators, records, or trust-kernel boundaries;
- the difference between PR evidence and main-push evidence is not understood;
- the proposed reduction is based only on Actions UI run count;
- current PR/check state is unclear;
- human maintainer approval is missing.

## 8. Current safe action

The current safe action is no workflow behavior change now.

The next safe step is to create a workflow map/index that records each workflow's trigger, permissions, mutation behavior, and whether its `push` to `main` run is intended canonical evidence or possible duplication.

Only after that map exists should any future implementation PR attempt trigger/path reduction.
