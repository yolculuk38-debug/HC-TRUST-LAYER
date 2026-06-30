# Release Channel Surface Classification

## Purpose

This document classifies HC-TRUST-LAYER surfaces that may later need separate release-channel treatment. It supports the architect-audit backlog item for release channel / advisory-demo-runtime surface classification before any package metadata, release automation, CLI behavior, workflow behavior, public verifier behavior, or product-facing claims are changed.

This document is advisory-only. It does not create release channels. It does not publish release channels. It records a planning boundary so future work can keep HC:// verification infrastructure public-safe, reviewable, and human-supervised.

## HC Boundary Statement

The following HC boundaries apply to this document:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- `approval_authority=false`
- `merge_authority=false`
- no new label/reviewer mutation authority
- no new issue comment automation authority
- no new automatic comments introduced by this document
- no new automatic labels introduced by this document
- no reviewer requests
- no approvals
- no merges
- no runtime behavior change
- no workflow behavior change
- no packaging behavior change
- no public API behavior change
- no schema/validator/record/generated/canonical behavior change

CI/checks are evidence, not trust authority. Human maintainers make the final decision.

This classification must not be read as legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, production readiness, or guaranteed correctness.

## Scope and Non-Effects

This document covers documentation-only classification of candidate future release channels. It does not change repository behavior.

Specifically:

- It does not change package metadata.
- It does not change release automation.
- It does not change CLI behavior.
- It does not change runtime behavior.
- It does not change workflow behavior.
- It does not change public API behavior.
- It does not change schema, validator, record, generated, canonical, policy, federation, signing, hash, or QR behavior.
- Existing governed/report-only workflow behavior is documented elsewhere and is not changed by this document.
- Existing PR Risk Labeler and HC Control Bot advisory comment behavior, where present, remains bounded by existing workflow taxonomy and governance documentation.
- Those workflows do not create release authority, approval authority, rejection authority, merge authority, certification authority, truth authority, or human-review replacement authority.

## Relationship to Release Posture Definition

The release posture definition frames HC-TRUST-LAYER as early-stage advisory HC:// verification infrastructure with human-supervised validation and conservative release claims. This document does not replace that posture. It narrows one planning question: which repository surfaces would belong to different future release channels if maintainers later decide to create those channels.

Release posture remains the governing context for public claims. Channel classification is only a map for future review boundaries.

## Future Release-Channel Vocabulary

The following terms describe possible future channels. They are planning vocabulary only.

- **core package channel**: future packaging and library surface for `hc_trust` primitives and stable package-facing behavior.
- **CLI/advisory runtime channel**: future command-line and local runtime surface for advisory checks and reviewer-support workflows.
- **public verifier channel**: future public-facing verification API, viewer, or hosted verifier surface, if separately approved and validated.
- **demo/example channel**: public-safe examples, fixtures, static demos, and training materials that do not represent production verification.
- **governance/report channel**: project-control, governance reports, workflow evidence, and advisory automation outputs used for human review.
- **generated/canonical evidence channel**: generated artifacts, canonical artifacts, records, digests, hashes, and evidence-bearing outputs whose handling must preserve auditability.
- **federation/research channel**: future federation, sync, external integration, and research surfaces that are not release promises today.

## Surface-to-Channel Classification Table

| Surface | Candidate future channel | Current status | User-facing expectation | Risk if released or marketed under the wrong channel | Safe next action |
| --- | --- | --- | --- | --- | --- |
| Core Python package / `hc_trust` | core package channel | active narrow release surface; protected/high-risk; needs more review | Users may expect installable utilities, but not production-final verification guarantees. | Package metadata could imply stable product scope, production readiness, or guarantees beyond repository evidence. | Run a docs/metadata review comparing `pyproject.toml` metadata to current release posture without changing metadata. |
| CLI entrypoint / `hc-trust` | CLI/advisory runtime channel | advisory runtime; needs more review | Users may run local advisory commands to support review. Human interpretation remains required. | CLI naming or docs could imply final verification, certification, or automated trust decisions. | Perform a CLI documentation boundary review and label advisory behavior clearly. |
| Verification package behavior | core package channel; CLI/advisory runtime channel | advisory runtime; protected/high-risk; needs more review | Users may inspect packages and validation outputs as evidence for review. | Treating package behavior as conclusive could imply truth finality or guaranteed correctness. | Review verification-package docs for conservative status language and current limitations. |
| Public/API verification surfaces | public verifier channel | research/planned; protected/high-risk; needs more review | Users should expect planning or bounded local surfaces unless separately deployed and validated. | Marketing as a public verifier could imply hosted availability, production readiness, or public API guarantees. | Create a public verifier channel boundary review before changing API behavior or claims. |
| Public validator demos / static viewer examples | demo/example channel | demo/example only | Users can explore public-safe scenarios and static examples. | Demo surfaces could be mistaken for production verification, signed-payload validation, or arbitrary record lookup. | Review demo labels and entry-point wording for clear demo-only boundaries. |
| Demo scenarios and fixtures | demo/example channel | demo/example only | Users can learn expected flows using bundled scenarios and fixtures. | Fixtures could be mistaken for canonical records, live evidence, or production test coverage. | Keep fixture docs public-safe and distinguish training material from evidence-bearing records. |
| Records and historical evidence | generated/canonical evidence channel | generated/canonical evidence; protected/high-risk | Users should treat records as evidence-bearing artifacts requiring audit continuity. | Releasing records as a product channel could damage provenance boundaries or imply broader truth claims. | Preserve evidence and require separate protected-surface review for any record change. |
| Generated/canonical artifacts | generated/canonical evidence channel | generated/canonical evidence; protected/high-risk | Users should treat artifacts as audit-sensitive outputs, not casual product assets. | Wrong-channel release could break audit trails, imply canonical finality, or weaken provenance continuity. | Keep generated/canonical ownership review separate from release channel implementation. |
| Governance/project-control documents | governance/report channel | governance/report-only | Users should read these as advisory planning, governance, and review-boundary material. | Governance docs could be misread as automated approval or release authority. | Continue small docs-only project-control reviews with explicit human authority language. |
| HC Control Bot Report | governance/report channel | governance/report-only; advisory runtime | Users may treat reports as review evidence only. | Bot output could be mistaken for maintainer approval, rejection, or certification. | Keep report wording bounded by workflow taxonomy and human final authority. |
| HC PR Lifecycle Compliance Report | governance/report channel | governance/report-only | Users may treat lifecycle reporting as evidence for reviewers. | Compliance wording could be mistaken for automatic merge eligibility or approval. | Review report-channel wording for advisory-only interpretation. |
| HC Check Digest | governance/report channel | governance/report-only | Users may use check summaries as CI evidence. | Digest output could be mistaken for trust authority or release approval. | Preserve the distinction that CI/checks are evidence, not trust authority. |
| PR Risk Labeler | governance/report channel | governance/report-only; protected/high-risk | Users may see existing bounded advisory risk-routing behavior where configured. | Risk labels could be mistaken for rejection, approval, or human-review replacement. | Document existing behavior only; do not expand bot or label authority. |
| Workflow taxonomy and workflow evidence | governance/report channel | governance/report-only; protected/high-risk | Users should use taxonomy and evidence to understand bounded workflow behavior. | Workflow classification could be mistaken for enforcement changes or release automation. | Keep workflow changes out of this PR and route any future workflow work separately. |
| Federation/sync surfaces | federation/research channel | research/planned; protected/high-risk | Users should expect future-facing planning, not live federation guarantees. | Wrong-channel release could imply distributed consensus, availability, or interoperability guarantees. | Keep federation work research/planning until maintainers approve explicit criteria. |
| External integration/research surfaces | federation/research channel | research/planned | Users should treat integrations and research as exploratory unless separately reviewed. | Integration claims could imply supported SDK/API commitments or third-party reliability. | Maintain research labels and require separate integration boundary review before implementation. |

## What Can Be Documented Now

The repository can document:

- candidate future channel vocabulary;
- which surfaces should not share a single customer promise;
- advisory/demo/runtime/governance/evidence/research distinctions;
- safe next PR candidates;
- non-effects for docs-only classification;
- human final authority and current limitations.

## What Must Remain Advisory/Demo/Research

The following must remain advisory, demo-only, or research/planned unless separate maintainer-approved work changes their status:

- public verifier claims beyond validated repository evidence;
- static demos and fixture-based examples;
- workflow reports and bot comments;
- federation and sync concepts;
- external integration concepts;
- generated/canonical evidence handling that has not received protected-surface review.

## Safe Next PR Candidates

- docs/metadata review comparing `pyproject.toml` metadata to current release posture;
- CLI documentation boundary review;
- public verifier channel boundary review;
- demo/example labeling review;
- governance/report channel wording review;
- release notes wording review for conservative v0.1.0 positioning.

## Do-Not-Do-Yet List

- Do not change `pyproject.toml`.
- Do not rename package or CLI.
- Do not publish or configure release channels.
- Do not change workflow enforcement.
- Do not change release automation.
- Do not move source modules.
- Do not promote demo/example surfaces to production.
- Do not claim certification, legal truth, identity finality, forensic certainty, production readiness, autonomous governance authority, or guaranteed correctness.
- Do not expand bot or agent authority.

## Ideal vs Current Practical State

### Current Practical State

HC-TRUST-LAYER has package, CLI, docs, demo, workflow, governance, record, generated/canonical, and research surfaces.

These surfaces should not all be released or marketed under the same promise.

The current repo remains early-stage, advisory, human-supervised, product-adjacent, governance-aware, and research-heavy.

### Ideal Future State

Separate release channels may exist later for core package, CLI/advisory runtime, public verifier, demo/example materials, governance/report outputs, generated/canonical evidence, and federation/research surfaces.

Each future channel needs explicit maintainer approval, release criteria, safety language, versioning expectations, and human-review boundaries.

## Real-World Analogy

A bank may have a mobile app, internal audit tools, compliance reports, test training materials, and research prototypes. They can all belong to the same organization, but they must not be released under the same customer promise. HC should label release channels before changing release behavior.
