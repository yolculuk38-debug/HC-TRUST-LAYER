# Release Posture Definition

## Purpose

This document completes the architect-audit backlog item for release posture definition. It records the current HC-TRUST-LAYER release identity before any future change to package metadata, release channels, CLI behavior, workflow behavior, or product-facing claims.

This document is advisory-only. It is intended to help reviewers distinguish the repository's research protocol, installable package, advisory/demo runtime, public verifier direction, and governance operating-layer surfaces.

## HC boundary statement

HC-TRUST-LAYER is currently an early-stage, advisory, human-supervised verification infrastructure repository for HC:// records, review boundaries, and evidence-preserving workflows.

The current release posture is product-adjacent, governance-aware, research-heavy verification infrastructure. The repository includes an installable Python package and CLI surface, but that does not make the full repository a production product.

Preserved HC boundaries:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- `approval_authority=false`
- `merge_authority=false`
- `label_reviewer_mutation=false`
- `issue_comment_automation=false`
- no new automatic comments introduced by this document
- no new automatic labels introduced by this document
- no reviewer requests
- no approvals
- no merges
- no runtime behavior change
- no workflow behavior change
- no packaging behavior change
- no public API behavior change
- no schema, validator, record, generated, or canonical behavior change

CI/checks are evidence, not trust authority. Human maintainers make the final decision.

Existing governed/report-only workflow behavior is documented elsewhere and is not changed by this release posture document. Existing PR Risk Labeler and HC Control Bot advisory comment behavior, where present, remains bounded by existing workflow taxonomy and governance documentation. Those workflows do not create release authority, approval authority, rejection authority, merge authority, certification authority, truth authority, or human-review replacement authority.

## Scope and non-effects

This document records posture only. It does not implement, authorize, or imply any behavior change.

- This document is advisory-only.
- It does not change package metadata.
- It does not change release automation.
- It does not change CLI behavior.
- It does not change runtime behavior.
- It does not change workflow behavior.
- It does not change public API behavior.
- It does not change schema, validator, record, generated, canonical, policy, federation, signing, hash, or QR behavior.
- It does not create approval authority, merge authority, reviewer-request authority, labeling authority, or issue-comment automation.

## Current release posture

Current practical state:

- The repository has package, CLI, documentation, demo, workflow, governance, record, generated/canonical, and research surfaces.
- The installable package and `hc-trust` CLI are releasable as scoped technical surfaces only when reviewed within their documented limits.
- The wider HC:// ecosystem remains advisory and human-supervised.
- Public verifier, federation, external integration, and governance operating-layer material must remain bounded by repository evidence and human review.

The repository must not claim legal truth, identity finality, forensic certainty, certification authority, production readiness, autonomous governance authority, or guaranteed correctness.

## Surface classification table

| Surface | Current posture | User expectation | Risk if misrepresented | Safe next action |
|---|---|---|---|---|
| Core Python package / `hc_trust` | releasable core; protected/high-risk; needs more review | A scoped installable Python package for HC-TRUST-LAYER tooling, not a complete product promise. | Users may treat installation as production readiness or complete trust authority. | Review metadata and package boundary language before any packaging change. |
| CLI entrypoint / `hc-trust` | advisory runtime; releasable core; protected/high-risk | A local command surface for bounded verification workflows and reviewer support. | CLI output may be mistaken for legal, forensic, identity, or certification finality. | Document command scope and limitations before changing CLI behavior. |
| Verification package behavior | advisory runtime; protected/high-risk; needs more review | Reproducible technical evidence that supports human-supervised validation. | Verification packages may be treated as guaranteed correctness or final truth decisions. | Keep validation and package behavior changes separate from documentation posture work. |
| Public/API verification surfaces | advisory runtime; research/planned; protected/high-risk; needs more review | Public-safe verifier direction and API-adjacent surfaces that remain bounded by implementation evidence. | Users may assume hosted availability, stable API guarantees, or production trust decisions. | Produce API/public verifier boundary documentation before product-facing claims. |
| Demo/example materials | demo/example only | Training, walkthrough, fixture, and preview material for understanding HC:// flows. | Demo scenarios may be promoted to production evidence or generalized verification guarantees. | Keep demo labels explicit and avoid production wording. |
| Records and historical evidence surfaces | governance evidence; protected/high-risk | Evidence-preserving records and provenance material for audit-aware review. | Historical evidence can be silently rewritten, over-interpreted, or treated as certification. | Preserve audit continuity and require explicit human review for changes. |
| Generated/canonical artifacts | generated/canonical evidence; protected/high-risk | Derived or canonical-adjacent artifacts that support navigation, replay, or evidence review. | Hand edits or marketing claims may weaken canonical boundaries or provenance continuity. | Use documented generation/review paths; avoid manual mutation in posture work. |
| Governance/project-control documents | governance evidence; needs more review | Advisory operating-layer guidance for maintainers, contributors, and reviewers. | Governance docs may be mistaken for autonomous approval, merge, or enforcement authority. | Keep language advisory, scoped, and explicit about human final authority. |
| HC bot/report-only workflows | governance evidence; protected/high-risk | Report-only automation that can provide evidence for review. | Automation may be mistaken for approval authority, reviewer assignment authority, labels, comments, or merge control. | Do not expand workflow enforcement or bot authority in release posture PRs. |
| Federation/sync surfaces | research/planned; protected/high-risk; needs more review | Future or experimental interoperability direction, not a live guarantee. | Users may infer live federation, distributed trust guarantees, or production sync behavior. | Keep federation work documentation-first until explicitly reviewed. |
| External integration/research surfaces | research/planned; needs more review | Planning and integration research that may inform future channels. | Integrations may be marketed as supported product commitments before review. | Separate research notes from releasable package and public verifier channels. |

## What is currently releasable

The current practical releasable surface is narrow:

- the scoped Python package as package metadata currently defines it;
- the `hc-trust` CLI entrypoint as an advisory local tool;
- documentation that accurately describes current repository evidence;
- bounded release evidence and governance notes that preserve human final authority.

Releasable does not mean production-ready. Releasable does not mean legally authoritative, forensically certain, identity-final, certification-grade, autonomously governed, or guaranteed correct.

## What is advisory/demo only

The following surfaces should be treated as advisory, demo, example, or preview unless future human-reviewed evidence changes that posture:

- public validator demos and static viewer examples;
- bundled demo scenarios, fixture IDs, and walkthroughs;
- local-only preview flows;
- report-only scans and generated reports;
- runtime/API examples that are not documented as stable production services.

These surfaces can help reviewers understand HC:// workflows, but they do not replace human-supervised validation.

## What is research/planned

The following remain research, planned, or future-facing unless separately implemented, validated, and accepted by maintainers:

- separate release channels for public verifier, demo examples, governance reports, and federation surfaces;
- federation and sync behavior;
- external platform integrations;
- public verifier productization;
- stable API commitments beyond current repository evidence;
- final trust scoring semantics;
- autonomous dispute or governance handling.

## What must not be claimed yet

HC-TRUST-LAYER must not claim:

- legal truth;
- identity finality;
- forensic certainty;
- certification authority;
- production readiness;
- autonomous governance authority;
- guaranteed correctness;
- live federation guarantees;
- final public verifier availability for arbitrary records;
- automatic approval, merge, label, comment, reviewer-request, or enforcement authority.

## Safe next PR candidates

Safe next PRs should be documentation-first and reviewable:

- documentation and metadata review that compares package metadata against this posture;
- CLI documentation review that clarifies advisory output boundaries;
- public verifier boundary review before product-facing claims;
- demo/example labeling review;
- release notes wording review for conservative v0.1.0 positioning;
- governance report wording review to preserve human final authority.

Packaging, workflow, runtime, schema, validator, record, generated, canonical, policy, federation, signing, hash, QR, source, test, or script changes should occur only after the release posture is agreed and a narrow follow-up scope is approved.

## Do-not-do-yet list

- Do not change `pyproject.toml` in this PR.
- Do not rename package or CLI.
- Do not publish release channels.
- Do not change workflow enforcement.
- Do not move source modules.
- Do not promote demo/example surfaces to production.
- Do not claim certification, legal truth, identity finality, forensic certainty, production readiness, or guaranteed correctness.
- Do not expand bot or agent authority.

## Ideal vs current practical state

Current practical state:

The repo has package, CLI, and release surfaces, but the wider ecosystem remains advisory and human-supervised. The package and CLI can support bounded workflows, while demos, records, governance docs, generated/canonical artifacts, public verifier planning, and federation research require conservative labeling and human review.

Ideal future state:

Separate release channels can exist later for the core package, public verifier, demo examples, governance reports, and research/federation surfaces. Those channels should be defined only after maintainers agree on scope, evidence requirements, human-supervised validation expectations, and release automation boundaries.

Safe sequencing:

Documentation and metadata review should come first. Packaging or workflow changes should happen only after this posture is agreed.

## Real-world analogy

A bank can have internal audit tools, customer-facing apps, training demos, and compliance reports. They should not all be released or marketed under the same promise. HC should label each release surface before changing package or release behavior.
