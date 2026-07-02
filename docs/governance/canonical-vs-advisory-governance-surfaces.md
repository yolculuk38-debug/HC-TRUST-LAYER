# Canonical vs Advisory Governance Surfaces

## Purpose

This document helps maintainers, contributors, and AI-assisted reviewers distinguish how to read existing HC-TRUST-LAYER governance and operating-layer surfaces. It classifies repository material into these conservative interpretation categories:

- canonical governance rules;
- advisory governance guidance;
- project-control evidence records;
- historical/reference records; and
- public/onboarding orientation.

This is a reading guide only. It does not rewrite existing governance rules, change authority, move files, archive files, or reclassify actual repository protection behavior.

## HC boundary statement

This document preserves the following HC:// and HC-TRUST-LAYER boundaries:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- `approval_authority=false`
- `merge_authority=false`
- `label_reviewer_mutation=false`
- `issue_comment_automation=false`
- no new workflow
- no new check
- no workflow permission change
- no runtime behavior change
- no packaging behavior change
- no public API behavior change
- no schema, validator, record, generated, or canonical behavior change
- no bot authority expansion

CI/checks are evidence, not trust authority. Human maintainers and reviewers make final repository decisions. A report-only runner, controlled assistant, HC Trust Engineer Agent, or other GitHub-native advisory layer can support review, but cannot approve, merge, label, request reviewers, close issues, mutate issue comments, or replace the governance boundary set by human maintainers.

## Classification vocabulary

### Canonical governance rule

A file that sets repository rules, protected-path expectations, contribution authority boundaries, security expectations, or final maintainer requirements.

### Advisory governance guidance

A file that explains recommended behavior, reviewer interpretation, examples, or process help but does not independently grant authority.

### Project-control evidence record

A project-control status, ledger, review, audit, checkpoint, or decision-support record that documents what was observed or completed. It is evidence for maintainers, not independent authority.

### Historical/reference record

A record kept for audit continuity or context that must not be treated as current active work unless a current project-control file or human maintainer direction says so.

### Public/onboarding orientation

A document that helps users or contributors enter the project safely but does not override canonical governance rules.

## Surface classification table

| Surface | Classification | Why it matters | Authority boundary | Reviewer note |
|---|---|---|---|---|
| `CODEOWNERS` | Canonical governance rule | Identifies ownership and protected review expectations. | High-authority repository control surface; this document does not change it. | Treat as a maintained authority surface and verify actual repository state. |
| `AGENTS.md` | Canonical governance rule | Defines agent operating expectations, claim boundaries, and protected-path care. | Binding for agents working within its scope. | Preserve HC:// terminology and human final authority. |
| `HC_BOOTSTRAP.md` | Canonical governance rule | Provides startup and handoff expectations for operating-layer work. | High-authority operating-layer file; this document does not change it. | Use for startup context without treating agents as final authority. |
| `SECURITY.md` | Canonical governance rule | Defines security reporting and vulnerability handling expectations. | Security-sensitive governance surface. | Follow security handling directions; do not route sensitive content through public project-control material. |
| `CONTRIBUTING.md` | Canonical governance rule | Defines contribution workflow, PR expectations, and contributor boundaries. | Contributor-facing rule surface unless a more specific maintained rule applies. | Use for PR readiness and contribution conduct. |
| `GOVERNANCE.md` | Canonical governance rule | Defines maintainer decision process and escalation expectations. | Maintainer authority surface; human review remains required. | Read before interpreting disputed authority or merge expectations. |
| `docs/governance/**` | Canonical or high-authority governance candidate | Contains governance procedures, migration notes, review expectations, and decision references. | High review sensitivity; individual files may be canonical, advisory, or reference depending on content and current maintainer interpretation. | Use conservative reading and escalate conflicts to maintainers. |
| `docs/security/**` | Canonical or high-authority governance candidate | Contains security boundaries, threat models, and review-sensitive guidance. | Security interpretation surface; does not replace `SECURITY.md` unless explicitly stated. | Treat as high sensitivity and preserve advisory-only limits where stated. |
| Branch protection / required checks, if represented in docs | Canonical or high-authority governance candidate | Documents repository merge gates and required validation evidence. | Actual repository settings and human maintainer decisions outrank summaries. | Confirm current settings before relying on documented summaries. |
| `docs/contributor-start-here.md` | Advisory governance guidance | Helps contributors enter the project safely. | Does not override `CONTRIBUTING.md`, `CODEOWNERS`, or maintainer direction. | Use as process help and onboarding context. |
| `docs/developer-onboarding.md` | Advisory governance guidance | Provides development setup and project orientation. | Does not grant authority to change protected paths. | Useful for setup; verify current commands and constraints. |
| `docs/maintainer-triage.md` | Advisory governance guidance | Supports issue and PR triage consistency. | Does not grant merge, label, reviewer, close, or issue-comment automation authority. | Treat as maintainer support guidance. |
| `docs/pr-workflow.md` | Advisory governance guidance | Explains PR flow and reviewer expectations. | Does not override branch protection, required checks, `CODEOWNERS`, or maintainer judgment. | Use to prepare reviewable PRs. |
| `docs/issue-workflow.md` | Advisory governance guidance | Explains issue handling and queue flow. | Does not authorize automated issue mutation. | Use as process guidance only. |
| `docs/label-taxonomy.md` | Advisory governance guidance | Explains label meanings and triage vocabulary. | Does not grant label mutation authority. | Label changes still require authorized maintainers or approved automation. |
| `docs/project-control/project-state.md` | Project-control evidence record | Summarizes current project state and handoff context. | Evidence for maintainers; not independent authority. | Use to avoid stale work assumptions. |
| `docs/project-control/task-ledger.md` | Project-control evidence record | Records completed, closed, or do-not-repeat work. | Evidence and continuity only. | Check before reopening completed backlog items. |
| `docs/project-control/next-actions.md` | Project-control evidence record | Lists candidate next actions and safe work. | Queue guidance, not automatic authorization. | Confirm protected-path permission before acting. |
| `docs/project-control/workflow-taxonomy.md` | Project-control evidence record | Documents observed workflow taxonomy and drift support. | Evidence about workflow surface; does not change workflows. | Do not treat as permission to edit workflow files. |
| `docs/project-control/core-package-boundary-review.md` | Project-control evidence record | Captures a core package boundary review. | Decision-support evidence only. | Use for continuity, not as a package metadata change. |
| `docs/project-control/src-top-level-module-boundary-audit.md` | Project-control evidence record | Captures module boundary audit observations. | Evidence only; does not change runtime boundaries. | Do not infer runtime behavior changes. |
| `docs/project-control/test-taxonomy-review.md` | Project-control evidence record | Captures test taxonomy review observations. | Evidence only; does not create required checks. | Treat as review context. |
| `docs/project-control/release-posture-definition.md` | Project-control evidence record | Documents release posture interpretation. | Evidence for maintainers; not a release approval. | Avoid production-readiness or guaranteed-correctness claims. |
| `docs/project-control/release-channel-surface-classification.md` | Project-control evidence record | Classifies release channel surfaces for review. | Evidence only; does not publish or approve a release. | Use to support conservative release review. |
| `docs/project-control/package-metadata-release-posture-review.md` | Project-control evidence record | Reviews package metadata release posture. | Evidence only; does not change package metadata. | Any metadata change remains separate. |
| `docs/project-control/readme-release-posture-wording-review.md` | Project-control evidence record | Reviews README release posture wording. | Evidence only; does not rewrite README here. | Use as continuity for wording decisions. |
| `docs/project-control/cli-help-documentation-boundary-review.md` | Project-control evidence record | Reviews CLI help and documentation boundary. | Evidence only; does not change CLI behavior. | Do not infer runtime or public API behavior changes. |
| `docs/project-control/public-surface-checklist.md` | Project-control evidence record | Tracks public surface review considerations. | Evidence and checklist support only. | Use for review coverage, not as automatic approval. |
| `README.md` | Public/onboarding orientation | Introduces the project to users and contributors. | Does not override canonical governance rules. | Keep public-safe and avoid overclaiming. |
| `docs/START_HERE.md` | Public/onboarding orientation | Provides role-based navigation and safe entry points. | Orientation only; does not replace governance authority. | Use as a starting point, then follow specific rule files. |
| `docs/repo-map.md` | Public/onboarding orientation | Maps repository areas and review sensitivity. | Advisory classification layer; not final authority by itself. | Use for risk triage and maintainer confirmation. |
| `docs/index.md` | Public/onboarding orientation | Provides documentation navigation. | Indexing surface; does not override specific governance rules. | Follow linked canonical files where applicable. |
| `docs/demo/**` | Public/onboarding orientation | Provides demo and public verification walkthroughs. | Demo-only and advisory unless separately implemented and reviewed. | Preserve public-safe and no-production-readiness language. |
| `docs/self-service-verify.html` | Public/onboarding orientation | Provides user-facing verification orientation. | Does not provide final truth, legal authority, or autonomous verification. | Keep boundary language visible. |
| `generated/**` | Generated/canonical/evidence surface | Contains generated or derived artifacts. | Protected or high-sensitivity; do not hand-edit unless explicitly authorized. | Regeneration and review must preserve provenance. |
| `canonical/**` | Generated/canonical/evidence surface | Contains canonical artifacts where present. | Protected; this document does not change canonical behavior. | Treat as high review sensitivity. |
| `records/**` | Generated/canonical/evidence surface | Contains evidence-bearing records and provenance material. | Protected evidence surface. | Preserve audit continuity and avoid silent mutation. |
| `schema/**` | Generated/canonical/evidence surface | Contains record schemas and verification contracts. | Protected schema surface. | Changes can affect validation semantics. |
| `validators/**` | Generated/canonical/evidence surface | Contains validation and verification surfaces. | Protected validation surface. | Changes can affect verification interpretation. |
| `signatures/**` | Generated/canonical/evidence surface | Contains signature-related evidence or references where present. | Protected signing/evidence surface. | Do not infer signing guarantees beyond implemented checks. |
| `hash/**` | Generated/canonical/evidence surface | Contains hash references and integrity artifacts. | Protected integrity surface. | Preserve canonical linkage. |
| `qr/**` | Generated/canonical/evidence surface | Contains QR-related verification artifacts and references. | Protected verification-adjacent surface. | Do not imply QR authenticity proof unless implemented and reviewed. |

## Reading order for conflicts

Use this conservative reading order when surfaces appear to conflict:

1. Repository state and actual files are the source of truth.
2. Human maintainers and reviewers make final decisions.
3. `CODEOWNERS`, branch protection, required checks, and explicit governance rules outrank advisory docs.
4. Project-control records are evidence and continuity, not automatic authority.
5. Historical docs must not be treated as active TODO unless current `project-state`, `next-actions`, or human maintainer direction confirms it.
6. AI, bot, Codex, controlled assistant, report-only runner, and HC Trust Engineer Agent output is advisory evidence only.

## What this document does not do

This document does not:

- change `CODEOWNERS`;
- change branch protection;
- change workflows;
- change permissions;
- create new required checks;
- grant bot or controlled-assistant authority;
- approve auto-merge;
- change issue, comment, label, reviewer, close, or other mutation behavior;
- change runtime behavior;
- change CLI behavior;
- change package metadata;
- change public API behavior;
- change schema behavior;
- change validator behavior;
- change record behavior;
- change generated or canonical artifact behavior;
- change policy behavior;
- change federation behavior;
- change signing behavior;
- change hash behavior; or
- change QR behavior.

## Safe follow-up candidates

Conservative future follow-ups may include:

- Add a short pointer from contributor or onboarding docs to this classification.
- Review any missing governance files against this classification.
- Consider a future docs-only index if governance docs grow further.
- Do not propose workflow or authority changes here.
