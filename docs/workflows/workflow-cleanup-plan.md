# Workflow Cleanup Plan

## Purpose

This document is a conservative planning layer for future workflow cleanup in HC-TRUST-LAYER. It identifies workflow surfaces that may be candidates for later review, surfaces that should remain separate, and workflow mutations that require explicit human-maintainer authorization before implementation.

This document does not change automation. It is docs-only planning for the project-control queue, the HC Trust Engineer Agent, report-only runner outputs, controlled assistant review, and the GitHub-native advisory layer.

## HC boundary statement

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- `approval_authority=false`
- `merge_authority=false`
- `label_reviewer_mutation=false`
- no new or unauthorized issue-comment automation
- no workflow change
- no workflow permission change
- no new workflow
- no new check
- no runtime behavior change
- no packaging behavior change
- no public API behavior change
- no schema/validator/record/generated/canonical behavior change
- no bot authority expansion
- CI/checks are evidence, not trust authority
- human maintainers/reviewers make final decisions

## Non-goals

This PR does not:

- rename workflows
- disable workflows
- delete workflows
- merge workflows
- split workflows
- add workflows
- add required checks
- remove required checks
- change permissions
- change trigger conditions
- change auto-merge behavior
- change advisory comment behavior
- change label/reviewer/comment/approval/merge/close authority
- change runtime/package/schema/validator/record/generated/canonical behavior

## Workflow cleanup vocabulary

- **Keep separate:** Workflow should remain independent because it protects a distinct boundary or produces separate evidence.
- **Candidate for future consolidation:** Workflow may later be reviewed for overlap, but only after evidence and human approval.
- **Report-only / advisory:** Workflow supports review but does not grant trust, approval, merge, or authority.
- **Enforcement / gate:** Workflow blocks or validates a protected boundary and must not be weakened without explicit authorization.
- **High-risk mutation:** Any workflow edit that affects permissions, triggers, required checks, protected paths, auto-merge, advisory comments, labels, reviewers, or generated/canonical artifacts.

## Conservative classification table

| Workflow family/name | Current role | Cleanup posture | Why it matters | Implementation risk | Required evidence before any future change |
|---|---|---|---|---|---|
| Automation Gate | Enforcement / gate for automation boundaries. | Keep separate. | Protects the governance boundary before automation-dependent work proceeds. | High: trigger, permission, or required-check changes could weaken review controls. | Current trigger and permission inventory, required-check mapping, recent run history, and explicit human-maintainer approval. |
| PR Scope Guard | Enforcement / gate for scoped changes and protected-path awareness. | Keep separate. | Helps preserve small, reviewable PRs and flags trust-kernel-adjacent changes. | High: weakening scope checks could obscure protected path changes. | Protected-path matrix, false-positive/false-negative review, required-check impact, and rollback path. |
| Governance Preflight | Enforcement / gate for governance-sensitive review preparation. | Keep separate. | Supports human-supervised validation before governance boundary changes. | High: changes may affect authority interpretation or pre-merge evidence. | Governance boundary review, old/new check behavior, required-check impact, and maintainer authorization. |
| Docs Review Policy | Enforcement / gate for documentation review expectations. | Keep separate unless a docs-only review proves equivalent evidence. | Keeps documentation changes aligned with review policy without changing runtime behavior. | Medium: consolidation could hide docs-specific policy signals. | Docs policy mapping, affected-path review, equivalent reporting proof, and human approval. |
| Docs Drift Check | Enforcement / gate for documentation drift signals. | Candidate for future consolidation with docs index reporting only if evidence is preserved. | Detects stale or inconsistent documentation references. | Medium: consolidation could reduce visibility into drift evidence. | Drift report comparison, old/new output comparison, required-check mapping, and rollback path. |
| Terminology Guard | Enforcement / gate for HC:// and HC-TRUST-LAYER terminology. | Keep separate. | Preserves repository terminology and avoids boundary-overstating language. | High: weakening terminology checks may introduce authority or readiness claims. | Terminology rule inventory, sample run comparison, advisory-only impact review, and maintainer approval. |
| Terminology Autofix Suggest (Advisory) | Report-only / advisory suggestion surface. | Keep separate from enforcement checks. | Provides controlled assistant suggestions without granting approval or mutation authority. | High: comment or mutation changes could expand bot authority. | Advisory-comment behavior inventory, permissions review, no-mutation proof, and explicit authorization. |
| Canonical Artifact Boundary Guard | Enforcement / gate for generated/canonical artifact boundaries. | Keep separate. | Protects generated/canonical evidence surfaces from unauthorized edits. | Very high: changes can affect evidence continuity and protected artifact handling. | Generated/canonical path inventory, old/new guard behavior, artifact evidence review, and maintainer approval. |
| verification-package-schema | Enforcement / gate for verification package schema expectations. | Keep separate. | Validates schema-adjacent package structure without granting truth authority. | High: changes can affect schema/validator interpretation. | Schema impact review, validator comparison, required-check mapping, and rollback path. |
| Advisory Policy Evaluation | Report-only / advisory policy evidence. | Candidate for future report grouping only. | Helps reviewers inspect policy signals without granting approval authority. | Medium: grouping could reduce signal clarity or alter advisory comments. | Old/new report output comparison, advisory-only impact statement, and maintainer approval. |
| HC Check Digest | Report-only / advisory summary surface. | Candidate for future report-only summary grouping. | Summarizes check state as evidence for human reviewers. | Medium: altered summaries could confuse evidence interpretation. | Summary field inventory, old/new digest examples, no authority expansion statement, and rollback path. |
| HC Control Bot Report | Report-only / advisory control-bot evidence. | Candidate for future report grouping only with no bot authority expansion. | Provides controlled assistant and report-only runner context for review. | High: changes to comments, labels, reviewers, or permissions could alter authority boundaries. | Permission inventory, comment behavior review, no label/reviewer mutation proof, and maintainer authorization. |
| HC PR Lifecycle Compliance Report | Report-only / advisory lifecycle evidence. | Candidate for future report grouping only. | Documents PR lifecycle signals for human review. | Medium: grouping could obscure lifecycle evidence. | Lifecycle field comparison, old/new report examples, and required-check impact statement. |
| HC Release Audit | Report-only / advisory release evidence. | Keep separate. | Release audit evidence should remain independently visible. | High: release workflows are trust-kernel-adjacent and evidence-bearing. | Release evidence inventory, old/new output comparison, rollback path, and explicit approval. |
| HC Repository Inventory | Report-only / advisory repository inventory. | Candidate for redundant scheduled inventory review only. | Supports repository visibility and drift review without granting authority. | Medium: schedule or output changes could reduce review evidence. | Schedule inventory, output comparison, stale-reference list, and maintainer approval. |
| Enable PR Auto-merge | Automation surface for auto-merge enablement. | Do not touch without explicit approval. | Auto-merge behavior affects merge flow even when human final authority is preserved. | Very high: permission, trigger, and merge-condition changes can alter authority boundaries. | Exact old/new behavior, required-check impact, auto-merge impact, rollback path, and explicit human-maintainer approval. |
| Safe Auto Merge | Automation surface for constrained auto-merge behavior. | Do not touch without explicit approval. | Must not be weakened or broadened without clear authorization. | Very high: may affect merge behavior and protected branch expectations. | Permission review, trigger review, required-check mapping, rollback path, and human-maintainer approval statement. |
| HC-TRUST-LAYER Validation | Enforcement / gate for repository validation. | Keep separate. | Provides broad validation evidence across repository expectations. | High: consolidation could reduce visibility into validation failures. | Validation command inventory, old/new check comparison, required-check impact, and rollback path. |
| Dependabot-related dependency update surface | Dependency update support surface where represented in docs or CI. | Keep separate unless maintainers approve scoped dependency workflow review. | Dependency update automation can affect package metadata and review workload. | High: schedule, permission, or update behavior changes can affect review boundaries. | Dependency update configuration inventory, package metadata impact statement, permission review, and maintainer approval. |

## Candidate cleanup types, no implementation

The following cleanup types are candidates only. Docs-only planning is safe, workflow mutation requires a separate PR, human maintainer approval is required, and current checks must remain intact until replaced with equal or better evidence.

- **Duplicate naming clarification:** Clarify names in documentation without renaming workflow files or checks.
- **Documentation index consolidation:** Group workflow documentation references without changing workflow behavior.
- **Artifact naming consistency:** Document artifact naming patterns before any workflow output changes.
- **Report-only summary grouping:** Consider whether advisory reports can be summarized together while preserving each evidence source.
- **Redundant scheduled inventory review:** Review scheduled inventory overlap without changing schedules in this PR.
- **Stale workflow reference cleanup:** Remove or update stale documentation references only after confirming current workflow names.
- **Old cancelled run interpretation cleanup:** Document how to interpret old cancelled runs without changing active workflow logic.

## Do-not-touch without explicit approval

Do not touch these surfaces without explicit human-maintainer approval in a separate workflow mutation PR:

- auto-merge workflows
- workflow permissions
- required checks
- branch protection-linked workflows
- advisory comment workflows
- label/reviewer mutation workflows
- generated/canonical artifact guards
- schema/validator checks
- governance/preflight gates
- release audit workflows

## Safe future PR sequence

1. Docs-only workflow index refresh.
2. Docs-only stale reference cleanup.
3. One workflow family at a time permission review.
4. One workflow family at a time trigger review.
5. Only then consider consolidation, and only when equivalent evidence is preserved.

## Real-world analogy

Treat workflow cleanup like bank branch control procedures or public-sector audit process cleanup: first map controls, then classify authority, then remove duplication only after proving no audit evidence or approval boundary is lost.

## PR body guidance for any future workflow mutation

Future workflow mutation PRs must state:

- exact workflows changed
- old trigger/permission/check behavior
- new trigger/permission/check behavior
- required-check impact
- protected-path impact
- advisory-only impact
- auto-merge impact
- rollback path
- validation evidence
- human-maintainer approval statement
