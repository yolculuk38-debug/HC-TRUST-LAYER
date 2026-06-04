# Validation Architecture

Documentation-only validation architecture reference for HC-TRUST-LAYER and HC:// review routing.

## 1. Purpose

This document consolidates existing repository evidence about HC:// validation surfaces, validation outputs, canonical record handling, public verification, verification packages, runtime advisory validation, policy evaluation, trust scoring, provenance, and audit trail continuity.

Repository evidence is authoritative. This document is advisory and documentation-only.

This document does not:

- change runtime behavior;
- change schemas;
- change validators;
- change records;
- change policy;
- change federation;
- change signing;
- create automation;
- create governance enforcement;
- claim production readiness, security certification, forensic certainty, truth finality, or autonomous governance.

Human-supervised validation remains required for sensitive trust-kernel-impacting work.

## 2. Authority Boundary

This document is an orientation and review aid. It summarizes validation architecture concepts already present across repository documentation, schemas, scripts, runtime notes, and package specifications.

It is not an executable validator, schema contract, policy engine, signing profile, federation protocol, canonical record, or governance approval. If this document conflicts with repository evidence in protected or source-of-truth surfaces, the repository evidence controls.

Validation authority is distributed by surface:

- canonical records and their accepted paths define record evidence boundaries;
- schemas define structural conformance for specific payloads;
- validator scripts and runtime paths define their implemented checks;
- policy rules and policy evaluator output provide advisory merge-risk routing;
- verification packages are derived, non-canonical artifacts;
- public verification outputs are advisory and read-only;
- human-supervised validation remains the interpretation boundary for sensitive trust-kernel work.

## 3. Validation Architecture Overview

HC-TRUST-LAYER validation is layered rather than singular. Repository evidence currently describes several related but non-identical validation surfaces:

1. canonical record presence and path review;
2. JSON Schema conformance;
3. hash and integrity checks;
4. verification package generation and validation;
5. public verification response shaping;
6. runtime advisory validation;
7. policy evaluation for change-risk routing;
8. trust scoring as a heuristic signal;
9. provenance and audit trail continuity review;
10. human-supervised validation for sensitive outcomes.

These layers may share vocabulary, but identical words do not always carry identical authority. For example, `VERIFIED` in one component does not automatically mean the same thing as `VERIFIED` in another component.

## 4. Conceptual Canonical Validation Path

The conceptual canonical validation path is the evidence-first route a reviewer should use when interpreting HC:// validation state:

1. identify the claimed canonical record or record candidate;
2. confirm whether the record path is inside an accepted canonical record boundary;
3. inspect the applicable record schema and status vocabulary;
4. validate record structure against the applicable schema when an executable path exists;
5. verify declared hashes, previous-hash links, content hashes, or package hashes where implemented;
6. compare provenance references, witness context, revision links, dispute markers, and audit trail entries;
7. inspect any verification package only as a derived artifact;
8. review public verification or runtime output as advisory evidence, not canonical mutation;
9. evaluate policy routing separately when the question concerns repository change risk;
10. escalate sensitive ambiguity to human-supervised validation.

This is a conceptual review path. No single executable validation source of truth is currently declared.

## 5. Executable Validation Paths

Executable validation paths exist for specific scopes, but they are not a single universal authority:

- terminology checks protect canonical HC:// and HC-TRUST-LAYER language;
- docs drift checks protect documentation/index consistency;
- canonical artifact checks protect canonical record boundary expectations;
- verification package checks validate package examples or schema conformance for package artifacts;
- runtime tests protect implemented runtime response behavior where present;
- policy evaluator scripts classify changed paths for advisory merge-risk routing.

Each executable path should be interpreted only within its implemented scope. A passing schema check does not imply trust approval, policy approval, production readiness, or governance enforcement.

## 6. Canonical Record Path

Canonical record path handling is high sensitivity because it affects canonical record identity, provenance continuity, and audit trail interpretation.

Current repository evidence uses `records/pending`, `records/verified`, and `records/archived` in canonical artifact checks, verification package export logic, policy rules, and verification package schema patterns. However, `records/archive` vs `records/archived` ambiguity exists in repository language and must not be silently normalized by documentation.

Contributor interpretation rules:

- treat canonical record path language as repository-evidence-bound;
- do not move, rename, or rewrite records as part of documentation-only validation clarification;
- do not infer that a derived package path can replace a canonical record path;
- escalate any direct or indirect canonical record path change for human-supervised validation.

## 7. Schema Validation

Schema validation answers a structural question: does a JSON payload conform to a specific declared schema?

It does not answer all trust questions. JSON Schema conformance is not the same as trust approval.

Known schema complexity includes:

- multiple record schemas may exist with different required fields or status models;
- `schema/record-v1.schema.json` and `schema/record-v1.json` use different required identifiers and status vocabularies;
- `schema/verification-result-v1.schema.json` defines a verification result vocabulary that differs from runtime, package, viewer, and trust-result terminology;
- `schema/verification-package-v1.schema.json` validates derived package shape, not canonical record authority.

Schema changes are trust-kernel-sensitive and are outside this document's scope.

## 8. Hash and Integrity Validation

Hash and integrity validation checks whether declared digest material is internally consistent with available payloads, records, package manifests, or revision references.

Hash validation can support integrity review, replay detection, package validation, provenance continuity, and public verification, but it does not independently establish truth finality or governance approval.

Integrity checks should remain scoped to the artifact being validated:

- record hash checks concern canonical record payload or linkage fields;
- content hash checks concern declared content material;
- package hash checks concern derived package files or manifests;
- revision hash checks concern revision continuity;
- audit-linked hash checks support audit trail continuity.

Hash and integrity validation should expose mismatch, missing data, ambiguous linkage, and stale-context warnings instead of inflating certainty.

## 9. Verification Package Validation

Verification packages package verification references for transport, review, interoperability, and offline or public verification workflows.

Verification packages are derived, non-canonical artifacts. A package can help reviewers inspect provenance, integrity hashes, witness references, audit references, signatures, revision context, and verification snapshots, but it must not be elevated above the canonical record.

Package validation may include:

- schema conformance for package shape;
- manifest or inventory checks;
- hash and digest checks;
- canonical record path reference checks;
- source repository and source commit visibility;
- provenance, audit, witness, signature, and policy field presence;
- warning visibility.

A valid package shape does not prove that the underlying canonical record is approved, current, undisputed, or policy-accepted.

## 10. Public Verification

Public verification provides read-only evidence visibility for external or user-facing inspection.

Public verification is advisory and does not mutate canonical records. It may expose integrity status, canonical path visibility, provenance context, witness context, audit consistency, revision visibility, public response categories, package links, replay indicators, dispute indicators, and human-supervised validation guidance.

Public verification must not be described as:

- a truth oracle;
- production readiness;
- security certification;
- autonomous governance;
- canonical record mutation;
- final approval.

## 11. Runtime Advisory Validation

Runtime advisory validation refers to implemented runtime or API response behavior that helps users and reviewers inspect HC:// verification signals.

Repository evidence describes runtime public responses as advisory-only, public-safe, prototype-stage, and bounded by human-supervised validation. Runtime responses may include fields such as schema validity, hash verification, warnings, trust state, replay warning, continuity warning, canonical lookup status, human review recommendations, and QR risk indicators.

Runtime output is a review aid. It does not provide autonomous merge authority, governance finality, truth guarantee, production readiness, or broader API promises beyond implemented and tested behavior.

## 12. Policy Evaluation

Policy evaluation answers a change-routing question: how should repository changes be classified for merge-risk review?

The current policy evaluator is advisory-only. It classifies changed paths using policy rules and recommends merge-risk outcomes such as `auto_merge_allowed`, `conditional_merge`, `human_review_required`, or `blocked`.

Policy evaluation is not the same as record validation, schema validation, public verification, trust scoring, or signing validation. A policy evaluator outcome should preserve audit trail continuity and human-supervised validation expectations, especially for trust kernel and protected surfaces.

## 13. Trust Scoring

Trust scoring converts multiple verification signals into a structured trust indicator.

Trust scoring is heuristic and advisory. It is not record validation, schema conformance, proof of truth, policy approval, production readiness, or governance enforcement.

Trust scoring may consider signals such as hashes, QR verification, signed verification records, audit snapshots, export/import verification, multi-witness consensus, provenance continuity, source reliability, and dispute state. The score remains an interpretation aid and must not override canonical records or human-supervised validation.

## 14. Provenance and Audit Continuity

Provenance validation examines lineage and context: where evidence came from, how it changed, which witnesses or validators are linked, and whether transformations, revisions, disputes, or supersessions are visible.

Audit continuity examines whether review, validation, recovery, dispute, replay, revision, and change events remain traceable across repository-defined evidence surfaces.

Provenance validation and audit continuity are distinct from policy evaluation. Provenance concerns evidence lineage. Policy evaluation concerns change-risk routing and merge guidance.

Both should surface uncertainty and unresolved gaps instead of claiming forensic certainty.

## 15. Authoritative Components

Within their declared scope, authoritative components include:

| Component | Authority scope | Boundary |
| --- | --- | --- |
| Repository evidence | Source-of-truth architecture, policy baselines, implementation status, verification documentation, and protected path boundaries. | Controls over this advisory document when conflicts exist. |
| Canonical records | Canonical record evidence where accepted by repository-defined paths and review process. | Must not be mutated by public verification or package inspection. |
| Schemas | Structural conformance for the specific artifact type and schema version. | Do not imply trust approval. |
| Implemented validators and checks | Executable validation within their implemented scope. | Do not imply universal validation success. |
| Policy rules | Declared advisory merge-risk classification inputs. | Do not validate record truth or package integrity. |
| Human-supervised validation | Required interpretation and approval boundary for sensitive trust-kernel-impacting work. | Cannot be replaced by agent output or advisory automation. |

## 16. Advisory Components

Advisory components include:

| Component | Advisory role | Limitation |
| --- | --- | --- |
| This document | Consolidates validation architecture evidence for orientation. | Documentation-only; no behavior change. |
| Public verification output | Surfaces read-only evidence and warnings. | Does not mutate canonical records or finalize trust. |
| Runtime advisory output | Helps inspect implemented runtime signals. | Does not create truth guarantee or governance finality. |
| Verification packages | Transport and review derived evidence. | Non-canonical; derived from canonical records and other references. |
| Trust scoring | Summarizes signals as heuristic confidence guidance. | Not record validation or policy approval. |
| Policy evaluator output | Advises merge-risk routing. | Does not enforce governance unless separately activated and validated. |
| Viewer summaries | Improve human-readable interpretation. | Must remain scoped, advisory, and uncertainty-aware. |

## 17. Output Vocabulary Map

Multiple validation vocabularies exist across schemas, runtime, viewer, public validator, package outputs, and trust engines. Similar words can have different scopes.

| Surface | Example vocabulary | Meaning boundary |
| --- | --- | --- |
| Public verification API draft | `PASS`, `WARNING`, `FAIL`, `UNKNOWN` | External-facing response categories for future public verification semantics. |
| Public validator core | `VERIFIED`, `PARTIAL`, `REVIEW_REQUIRED`, `INVALID`, `UNTRUSTED` | Public proof-validation decision vocabulary. |
| Verification result schema | `VERIFIED`, `REVIEW_REQUIRED`, `DISPUTED`, `REVOKED`, `EXPERIMENTAL` | Schema-level high-level verification result values. |
| Record schemas | `draft`, `reviewed`, `verified`, `archived`; `pending`, `verified`, `archived` | Record schema status values that differ by schema file. |
| Verification package schema | `pending`, `verified`, `rejected`, `archived`, `disputed`, `revoked` | Derived package `verification_state` values. |
| Runtime public response | `status`, `trust_state`, `schema_valid`, `hash_verified`, warnings, review flags | Implemented advisory runtime response fields. |
| Policy evaluator | `auto_merge_allowed`, `conditional_merge`, `human_review_required`, `blocked` | Advisory merge-risk guidance. |
| Trust result standard/viewer | `VERIFIED TRACE`, `PARTIAL TRACE`, `REPLAY WARNING`, `DISPUTED`, `UNVERIFIED`, `HUMAN REVIEW REQUIRED` | Human-readable advisory trust summary labels. |
| Trust score engine | Numeric or categorized trust indicators | Heuristic signal summary, not truth finality. |

`VERIFIED` in one component does not automatically mean the same thing as `VERIFIED` in another component.

## 18. PASS / REVIEW / FAIL / INCONCLUSIVE Relationship

For cross-surface documentation and contributor discussion, use this relationship as an advisory normalization aid only:

| Normalized discussion term | Related repository terms | Interpretation guidance |
| --- | --- | --- |
| `PASS` | `PASS`, `VERIFIED`, `verified`, `VERIFIED TRACE`, positive `hash_verified` or `schema_valid` within scope | Indicates checks passed within a declared component scope. Does not imply universal approval. |
| `REVIEW` | `WARNING`, `REVIEW_REQUIRED`, `HUMAN REVIEW REQUIRED`, `conditional_merge`, `human_review_required`, replay or continuity warnings | Indicates material uncertainty, caution, or required human-supervised validation. |
| `FAIL` | `FAIL`, `INVALID`, `UNTRUSTED`, `REVOKED`, `rejected`, `blocked`, hash mismatch, schema failure | Indicates a failed check or blocked state within a declared component scope. |
| `INCONCLUSIVE` | `UNKNOWN`, `EXPERIMENTAL`, `PARTIAL`, `pending`, `PARTIAL TRACE`, `UNVERIFIED`, missing data, unavailable evidence | Indicates insufficient, partial, ambiguous, unavailable, or out-of-scope evidence. |

This map does not create a new schema, validator, runtime result, policy rule, governance state, or canonical record status.

## 19. Known Validation Gaps

Known validation gaps include:

- No single executable validation source of truth is currently declared.
- `records/archive` vs `records/archived` ambiguity exists.
- Multiple record schemas may exist with different required fields or status models.
- Multiple validation vocabularies exist across schemas, runtime, viewer, public validator, package outputs, and trust engines.
- `VERIFIED` in one component does not automatically mean the same thing as `VERIFIED` in another component.
- JSON Schema conformance is not the same as trust approval.
- Public verification is advisory and does not mutate canonical records.
- Verification packages are derived, non-canonical artifacts.
- Runtime response contracts, API architecture drafts, schema helpers, and viewer summaries are related but not identical.
- Trust scoring remains heuristic and advisory.
- Policy evaluation currently addresses change-risk routing, not canonical record truth.
- Hash validation can show integrity consistency or inconsistency but cannot independently establish truth finality.
- Provenance and audit trail continuity depend on available repository evidence and should surface missing or ambiguous links.

## 20. Contributor Guidance

Contributors should:

- preserve HC-TRUST-LAYER and HC:// terminology;
- treat repository evidence as authoritative;
- keep validation language scoped to the component being discussed;
- distinguish canonical records from derived verification packages;
- distinguish schema validation from trust evaluation;
- distinguish public verification from canonical verification;
- distinguish provenance validation from policy evaluation;
- distinguish trust scoring from record validation;
- preserve advisory-only and human-supervised validation language;
- avoid production readiness, security certification, forensic certainty, truth finality, or autonomous governance claims;
- avoid editing protected runtime, schema, validator, record, policy, federation, signing, workflow, source-code, test, trust-kernel index, `hc_context`, or agent surfaces unless explicitly requested and validated.

## 21. Risks and Guardrails

Primary risks:

- authority inflation from advisory output;
- vocabulary collision across components;
- accidental elevation of verification packages above canonical records;
- conflation of JSON Schema conformance with trust approval;
- conflation of public verification with canonical verification;
- conflation of trust scoring with record validation;
- silent normalization of `records/archive` vs `records/archived` ambiguity;
- unsupported production, security, forensic, truth, or governance claims.

Guardrails:

- preserve source-of-truth order and repository evidence;
- keep validation claims component-scoped;
- surface ambiguity rather than inferring guarantees;
- keep public verification read-only;
- keep verification packages derived and non-canonical;
- route sensitive trust-kernel-impacting work to human-supervised validation;
- run terminology, docs drift, canonical artifact, and diff checks for documentation changes.

## 22. Related Documents

- `AGENTS.md`
- `docs/project-control/trust-kernel-boundary.md`
- `docs/canonical-record-boundary.md`
- `docs/verification-map.md`
- `docs/protocol-graph-integrity.md`
- `docs/public-verification-api.md`
- `docs/public-verification-flow.md`
- `docs/public-validator.md`
- `docs/runtime/public-response-contract.md`
- `docs/verification-package-spec.md`
- `docs/verification-package-v2.md`
- `docs/external-verification-packages.md`
- `docs/policy-evaluator.md`
- `docs/policy-rules.md`
- `docs/policy-workflow-integration.md`
- `docs/trust-score-engine.md`
- `docs/trust-result-standard.md`
- `docs/verification-status-ux.md`
- `schema/record-v1.schema.json`
- `schema/record-v1.json`
- `schema/verification-result-v1.schema.json`
- `schema/verification-package-v1.schema.json`
- `scripts/check_canonical_artifacts.py`
- `scripts/export_verification_package.py`
- `scripts/view_verification_package.py`
- `scripts/evaluate_policy.py`
