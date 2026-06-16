# Auto-Merge Policy Overlap Review — 2026-06-16

## 1. Executive summary

This document is a report-only review of auto-merge-related workflow overlap in HC-TRUST-LAYER.

No workflow files are changed by this report. No workflows are deleted, disabled, renamed, moved, or edited. No workflow runs are deleted. No source, tests, generated artifacts, records, schemas, validators, policy, federation, signatures, canonical files, trust-kernel files, issues, branches, or pull requests are changed.

This review follows the workflow run noise audit and the earlier workflow cleanup recommendation. Its purpose is to identify whether auto-merge-adjacent workflows create operator confusion or unnecessary run volume, while preserving the current project rule that AI and automation do not have independent merge authority.

Boundary values preserved by this review:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- human final authority remains required
- CI/checks are evidence, not trust authority
- workflow checks do not grant merge authority

## 2. Reviewed workflow family

This review focuses only on the auto-merge-adjacent workflow family identified in the cleanup recommendation:

| Workflow | Current role in operator model | Risk signal | Review status |
| --- | --- | --- | --- |
| `.github/workflows/enable-auto-merge.yml` | Reports or evaluates auto-merge enablement boundaries. | Auto-merge-adjacent name and PR lifecycle/label context. | REVIEW_OVERLAP |
| `.github/workflows/safe-auto-merge.yml` | Reports the safe auto-merge boundary and human merge requirement. | Auto-merge-adjacent name and workflow_run/PR context. | REVIEW_OVERLAP |
| `.github/workflows/docs-auto-merge.yml` | Classifies docs-only/manual-review scope and reports docs review policy. | Auto-merge-adjacent name and docs-only policy context. | REVIEW_OVERLAP |

This report does not inspect or change unrelated security, validation, provenance, release, policy, terminology, canonical-artifact, assistant, labeler, or generated-evidence workflows.

## 3. Observed overlap

The overlap is primarily operator-facing and semantic, not necessarily behavioral:

- all three workflow names contain or imply auto-merge policy;
- all three can appear in Actions/checks around PR review;
- the current governance model requires human merge authority regardless of docs-only scope;
- repeated successful or cancelled auto-merge-adjacent runs can make the Actions UI look noisy;
- a maintainer may confuse report-only policy checks with actual merge automation if the naming is not explicit.

This overlap should be documented before any behavior change.

## 4. Safety interpretation

Auto-merge-adjacent workflows are sensitive even when report-only because they describe or enforce the merge boundary. In this project, the safe interpretation is:

- automation may evaluate scope;
- automation may report whether a PR appears docs-only;
- automation may report whether human review is required;
- automation may report that auto-merge is disabled or not authorized;
- automation must not approve, reject, close, merge, or bypass human final authority.

Any future change that enables actual auto-merge, changes merge permissions, changes review requirements, or reduces human visibility is authority-changing and must stop for explicit human governance review.

## 5. Recommended consolidation path

No immediate workflow implementation change is recommended in this report.

Recommended future path:

1. Keep all three workflows active until maintainers approve a targeted implementation change.
2. Add or improve operator-facing documentation first, so report-only versus merge-capable behavior is unmistakable.
3. If maintainers want less UI noise later, prepare a separate implementation PR that changes only one workflow family.
4. In any implementation PR, preserve equivalent evidence for docs-only scope, manual-review requirements, and disabled/non-authoritative auto-merge behavior.
5. Prefer naming clarity over behavior changes as the first low-risk step.

Possible future documentation-only naming model:

| Current label | Safer operator wording |
| --- | --- |
| Enable PR Auto-merge | Auto-merge boundary report |
| Safe Auto Merge | Human merge gate report |
| Docs auto-merge | Docs review policy report |

These are documentation/naming concepts only. This report does not rename workflow files or workflow names.

## 6. Required gate before any implementation PR

Before changing `.github/workflows/**`, require all of the following:

- live open PR state is known;
- the proposed workflow change is scoped to this auto-merge-adjacent family only;
- before/after trigger behavior is documented;
- before/after permissions are documented;
- no new write permissions are added;
- no auto-merge enablement is added;
- no human review requirement is removed;
- no governance, policy, terminology, canonical artifact, validation, release, provenance, assistant, or labeler workflow is changed in the same PR;
- normal CI/checks pass;
- a human maintainer explicitly approves the behavior change.

## 7. Stop conditions

Stop and do not change workflows if any of the following are true:

- the workflow's current behavior is not fully understood;
- a workflow uses write permissions or changes PR labels/comments;
- a workflow relies on `pull_request_target`, `issue_comment`, or other sensitive event contexts;
- the change would reduce auditability;
- the change would remove evidence that a PR was checked;
- the change would blur the rule that human final authority remains required;
- the proposal is based only on UI clutter and not on a documented duplicate behavior;
- there is an open unresolved review thread or failed check.

## 8. Current safe action

The current safe action is no workflow behavior change now.

The next safe step is either:

- keep this report as the audit record and stop; or
- open a future targeted documentation/naming clarification PR for the auto-merge-adjacent workflow family.

Any actual workflow behavior change should be separate, small, human-reviewed, and limited to reducing confusion without reducing evidence or changing authority.
