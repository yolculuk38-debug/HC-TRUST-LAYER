# Onboarding Contributor Boundary Review

## 1. Purpose

This document is an advisory, documentation-only review of HC-TRUST-LAYER contributor and onboarding boundaries for backlog item 5-1, "onboarding / contributor guide boundary review."

It helps a new human contributor, AI-assisted contributor, maintainer, or reviewer understand observed project boundaries before opening issues or pull requests. It does not change code, tests, workflows, scripts, schemas, validators, records, generated/canonical artifacts, demo fixtures, runtime behavior, API behavior, CLI behavior, CI behavior, or governance enforcement.

## 2. HC boundary

- `advisory_only=true`.
- `public_safe=true`.
- `truth_guarantee=false`.
- `human_review_required=true`.
- AI-assisted contribution is advisory only.
- Contributors do not gain approval, merge, label, reviewer, comment, or governance authority from this document.
- CI produces evidence but does not replace human review.
- The human maintainer remains the final authority.

This review does not establish legal truth, identity finality, forensic certainty, certification, production readiness, guaranteed correctness, or autonomous governance authority.

## 3. Review method

This review inspected observed repository docs by path/name and apparent role. It does not invent files or policies. If a contributor guide or onboarding surface was not observed, it is marked as `not observed`.

Observed onboarding and boundary surfaces:

- `README.md` is observed as the top-level repository entrypoint.
- `CONTRIBUTING.md` and `docs/CONTRIBUTING.md` are observed as contributor-facing guidance.
- `docs/contributor-start-here.md` and `docs/developer-onboarding.md` are observed as onboarding surfaces.
- `docs/repo-map.md` is observed as a repository map.
- `docs/project-control/` is observed as the project-control report, status, and operating-layer area.
- `HC_BOOTSTRAP.md` is observed and referenced by onboarding docs; it was inspected but not edited.
- `AGENTS.md` is observed and referenced by onboarding docs; it was inspected but not edited.
- `.github/ISSUE_TEMPLATE/` is observed; issue templates were noted by path but not edited.
- `.github/pull_request_template.md` is observed as an onboarding / PR review surface; it was inspected but not edited.

Relationship to previous boundary reviews:

- `docs/project-control/core-package-boundary-review.md` classifies runtime, schema, records, generated/canonical, governance, and support boundaries.
- `docs/project-control/test-taxonomy-review.md` classifies tests as evidence, not trust authority.
- `docs/project-control/public-api-cli-boundary-review.md` classifies public API and CLI output boundaries.
- `docs/project-control/generated-canonical-artifact-ownership-review.md` classifies generated/canonical artifact ownership boundaries.
- `docs/project-control/demo-example-boundary-review.md` classifies demo and example boundaries.

## 4. Contributor surface classification table

| Path / onboarding surface | Observed role | Audience | Contributor risk level | Safe contribution type | Requires maintainer confirmation | Related boundary review | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `README.md` | Top-level onboarding and project summary. | New contributors, reviewers, public readers. | medium | docs-only | yes, for trust, status, or public-output wording | public API / CLI; core package | Public-facing wording should stay bounded and advisory-only. |
| `CONTRIBUTING.md` | Root contributor guidance. | Contributors and reviewers. | governance | docs-only | yes | onboarding contributor boundary | Changes can affect contribution expectations; do not add approval or merge authority. |
| `docs/CONTRIBUTING.md` | Documentation contributor guidance. | Contributors and maintainers. | governance | docs-only | yes | onboarding contributor boundary | Keep human final review language clear. |
| `docs/contributor-start-here.md` | Beginner onboarding surface. | First-time contributors. | low | docs-only | yes, for protected path or authority language | core package; test taxonomy | Safe place for small clarity improvements when scoped. |
| `docs/developer-onboarding.md` | Local setup, checks, and protected path warning flow. | Developers, AI-assisted contributors, reviewers. | medium | docs-only | yes, for check or protected-path changes | test taxonomy; generated/canonical | Check guidance is evidence routing, not trust authority. |
| `docs/repo-map.md` | Repository map and path orientation. | Contributors, maintainers, reviewers. | medium | docs-only | yes, for ownership or protected-path claims | core package; generated/canonical; demo/example | Useful first read before selecting change type. |
| `docs/project-control/` | Advisory status, boundary, operating-layer, and review evidence reports. | Maintainers, contributors, agents. | medium | report-only, advisory-only, docs-only | yes, for governance interpretation | all listed boundary reviews | Reports are evidence and navigation aids, not authority. |
| `docs/project-control/core-package-boundary-review.md` | Advisory core/runtime/package boundary review. | Maintainers and implementation contributors. | high | docs-only pointer or report-only | yes | core package | Runtime, schema, records, and protected paths require explicit scope. |
| `docs/project-control/test-taxonomy-review.md` | Advisory test taxonomy and coverage boundary review. | Test contributors and reviewers. | medium | docs-only pointer or test-only follow-up | yes, for coverage claims | test taxonomy | Tests provide evidence; they do not establish final trust. |
| `docs/project-control/public-api-cli-boundary-review.md` | Advisory public API / CLI output boundary review. | API, CLI, docs, and public-output contributors. | high | docs-only pointer | yes | public API / CLI | Public output wording must not imply final truth or production readiness. |
| `docs/project-control/generated-canonical-artifact-ownership-review.md` | Advisory generated/canonical ownership review. | Maintainers, release reviewers, artifact contributors. | critical | docs-only pointer or report-only | yes | generated/canonical | Generated/canonical artifacts must not be hand-edited casually. |
| `docs/project-control/demo-example-boundary-review.md` | Advisory demo/example boundary review. | Demo, example, docs, and reviewer audiences. | medium | docs-only pointer | yes | demo/example | Demo fixtures are not real records and should not be promoted casually. |
| `HC_BOOTSTRAP.md` | Operational bootstrap and handoff guide. | Humans, AI agents, maintainers. | governance | docs-only when explicitly scoped | yes | onboarding contributor boundary | Observed and referenced; not edited in this PR. |
| `AGENTS.md` | Repository-wide contributor and agent rules. | Agents and contributors. | governance | docs-only when explicitly scoped | yes | onboarding contributor boundary | Observed and referenced; not edited in this PR. |
| `.github/ISSUE_TEMPLATE/` | Issue intake templates. | Contributors and maintainers. | governance | not in this PR | yes | maintainer workflow follow-up | Observed but not edited; workflow/template changes need separate scope. |
| `.github/pull_request_template.md` | Contributor PR body guidance, validation prompts, self-audit checklist, and risk notes. | Contributors and reviewers. | governance, medium | not in this PR | yes | maintainer workflow follow-up | Observed but not edited; future checklist improvements should tighten or link from the existing PR template. |
| `.github/workflows/**` | CI and automation workflows. | Maintainers and CI operators. | protected path, high | not safe for docs-only PRs | yes | test taxonomy; public API / CLI | CI evidence does not replace human review. |
| `scripts/**` | Checks, validators, report generators, and local helpers. | Maintainers and developers. | high | not safe for docs-only PRs | yes | test taxonomy; generated/canonical | Script behavior changes can alter evidence production. |
| `src/**` | Runtime and library implementation. | Developers and reviewers. | code/runtime, critical | code/runtime only with explicit scope | yes | core package; public API / CLI | Runtime changes are not onboarding-doc work. |
| `tests/**` and root test files | Test evidence and coverage. | Developers and reviewers. | test-only, medium | test-only with explicit scope | yes, for trust-critical coverage | test taxonomy | Tests are evidence, not final authority. |
| `schema/**`, `validators/**`, `policy/**`, `federation/**`, `signing/**`, `signatures/**` | Protected trust-kernel or trust-adjacent surfaces. | Maintainers and specialist reviewers. | protected path, critical | not safe without explicit scope | yes | core package; generated/canonical | Do not modify casually. |
| `records/**` | Records/evidence and provenance-bearing material. | Maintainers, reviewers, evidence contributors. | records/evidence, critical | not safe without explicit scope | yes | core package; generated/canonical | Do not move, delete, normalize, regenerate, or rewrite without human review. |
| `generated/**` and `canonical/**` | Generated/canonical artifact areas. | Maintainers and release/artifact reviewers. | generated/canonical, critical | not safe without explicit scope | yes | generated/canonical | Generated/canonical artifacts differ from source records and need an audit path. |
| `docs/demo/fixtures/**` and demo/example docs | Demo fixtures and examples. | Demo contributors and public readers. | demo/example, medium | docs-only for narrative; fixture edits need scope | yes | demo/example | Demo/example material must not be treated as real records. |
| Public API, CLI, QR, and validator output docs | Public output wording and response expectations. | Public-output contributors and reviewers. | public output, high | docs-only wording with care | yes | public API / CLI | Avoid stronger claims than implemented and reviewed behavior. |

## 5. Contributor boundary findings

The safest surfaces for new contributors are small docs-only edits to explanatory documentation, navigation, typo fixes, broken-link repairs, and narrowly scoped project-control reports. Even safe docs should preserve HC:// and HC-TRUST-LAYER terminology, public-safe language, and human-final-review boundaries.

Areas requiring maintainer confirmation include contributor policy, governance wording, project-control status, public API/CLI output wording, generated/canonical ownership claims, demo/example interpretation, test coverage claims, and any path that could affect records, schemas, validators, runtime behavior, workflows, package metadata, or protected trust-kernel interpretation.

Protected paths must not be changed casually. This includes schemas, validators, records, policy, federation, signing, signatures, generated/canonical artifacts, workflow automation, trust-kernel indexes, and runtime or public validator behavior. If a requested task touches these areas, contributors should confirm explicit scope before editing.

Docs-only work changes explanatory text and should not alter behavior. Test-only work changes evidence checks and coverage but still does not establish trust authority. Code/runtime work can change behavior and needs implementation review, tests, and maintainer confirmation. Protected-path work needs explicit scope and human-supervised validation.

Generated/canonical artifacts differ from source records. Source records are evidence-bearing material whose provenance should be preserved. Generated/canonical artifacts are derived or boundary-defining outputs that should not be hand-edited without a clear generation, review, and audit path.

Demo/examples differ from real records. Demo fixtures and examples may help explain workflows, but they must remain clearly separated from records/evidence and must not be promoted into real records without a separate PR and maintainer review.

Public API/CLI output wording must stay bounded. Public validator, QR, API, CLI, and package-facing docs should avoid claims of legal truth, identity finality, forensic certainty, certification, production readiness, guaranteed correctness, or autonomous governance authority.

Project-control reports are advisory evidence, not authority. They may help route work, identify boundaries, and preserve review context, but they do not approve, merge, label, request reviewers, close issues, or establish governance outcomes.

## 6. Recommended contributor rules

- Start with small docs-only or test-only PRs.
- Do not modify protected paths without explicit scope.
- Do not modify records, schemas, validators, signing, federation, policy, generated/canonical artifacts, or workflows casually.
- Do not move, delete, normalize, regenerate, or rewrite records without human review.
- Do not promote demo/example fixtures into real records without a separate PR and maintainer review.
- Do not claim legal truth, identity finality, forensic certainty, certification, production readiness, guaranteed correctness, or autonomous governance authority.
- Do not add approval, merge, label, reviewer-request, issue-close, or autonomous governance authority.
- AI-generated suggestions must be treated as advisory.
- CI success is evidence, not trust authority.
- The human maintainer remains the final authority.

## 7. Contributor workflow recommendation

A safe practical workflow is:

1. Read `docs/repo-map.md` and the relevant onboarding surface.
2. Identify whether the proposed change is docs-only, test-only, code/runtime, protected-path, generated/canonical, records/evidence, demo/example, governance, or public-output work.
3. Check the related boundary review before editing.
4. Keep the PR small and scoped to one task.
5. State docs-only, test-only, code/runtime, protected-path, or other relevant scope in the PR body.
6. List forbidden paths not changed when the task has sensitive boundaries.
7. Run local checks when applicable and report exact results.
8. Wait for the review window and maintainer comments.
9. Resolve review feedback before merge.
10. Treat human final review as required.

## 8. Ideal vs current practical state

### Ideal

- Clear contributor guide.
- Clear maintainer checklist.
- Protected path map.
- Demo/generated/canonical/public-output rules linked from onboarding.
- AI-assisted contribution rules visible.
- Existing PR body template includes or links boundary confirmation.
- Every contributor knows CI is evidence, not final trust.

### Current practical next step

- Document observed onboarding/contributor boundaries first.
- Do not edit templates or protected files in this PR.
- Propose small follow-up PRs for missing onboarding links, checklist wording, or changes that tighten or link from the existing PR template.

## 9. Real-world analogy

In banking/e-devlet systems, a new operator may fill forms or prepare evidence, but cannot rewrite the ledger or approve their own transaction. In SSL/TLS systems, a developer can update docs or tests, but certificate authority/root trust changes require strict review. In C2PA, W3C Verifiable Credentials, and OpenTimestamps workflows, examples and proofs are useful only when source, context, and authority boundaries are clear.

HC-TRUST-LAYER contributors should follow the same principle: small changes, clear evidence, protected boundaries, and human final review.

## 10. Follow-up items

- 5-1b optional: add contributor-facing boundary links to onboarding docs where missing.
- 5-1c optional: tighten or link from the existing PR template for docs-only/test-only/protected-path claims.
- 5-1d optional: add AI-assisted contribution note if missing.
- 5-2: maintainer workflow / PR review checklist boundary review.
- 5-3: protected path contributor guide review.
