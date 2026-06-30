# README Release Posture Wording Review

## Purpose

This document reviews current `README.md` wording against the already documented HC-TRUST-LAYER release posture, release-channel surface classification, and package metadata posture review.

The purpose is to document whether the README accurately presents HC-TRUST-LAYER as early-stage, advisory, human-supervised, product-adjacent, governance-aware, and research-heavy HC:// verification infrastructure without overclaiming production readiness, legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, standards compliance, partnership, endorsement, or guaranteed correctness.

## HC boundary statement

This document is advisory-only.

Preserved HC boundaries:

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

Existing governed/report-only workflow behavior is documented elsewhere and is not changed by this document. Existing PR Risk Labeler and HC Control Bot advisory comment behavior, where present, remains bounded by existing workflow taxonomy and governance documentation. Those workflows do not create release authority, approval authority, rejection authority, merge authority, certification authority, truth authority, or human-review replacement authority.

## Scope and non-effects

This document reviews README wording only. It does not edit README text and does not implement any product, package, runtime, workflow, validator, record, generated artifact, canonical artifact, policy, federation, signing, hash, or QR behavior.

- It does not change README.
- It does not change ROADMAP.
- It does not change package metadata.
- It does not change `pyproject.toml`.
- It does not change release automation.
- It does not change CLI behavior.
- It does not change runtime behavior.
- It does not change workflow behavior.
- It does not change public API behavior.
- It does not change schema, validator, record, generated, canonical, policy, federation, signing, hash, or QR behavior.

README is a protected/high-risk public expectation surface because it is the main public-facing project explanation. This review is documentation-only evidence for future human-supervised wording work.

## Relationship to release posture definition

The release posture definition frames HC-TRUST-LAYER as early-stage, advisory, human-supervised verification infrastructure for HC:// records, review boundaries, and evidence-preserving workflows. It also states that an installable package and CLI do not make the whole repository a production product.

This README review applies that posture to the repository entrypoint. README can explain HC records, hash, QR, witness, audit, package, CLI, and demos, but it must not imply production readiness, legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, standards compliance, partnership, endorsement, or guaranteed correctness.

## Relationship to release channel surface classification

The release channel surface classification separates package, CLI, docs, demos, governance/report-only workflows, generated/canonical artifacts, records, public verifier direction, federation, and research surfaces. README should help users navigate those surfaces without collapsing them into one production or product promise.

The README currently uses conservative warnings in several public-facing areas. Future README edits should keep each surface labeled according to its actual channel posture: releasable core where applicable, advisory runtime where applicable, demo/example only where applicable, governance/report-only where applicable, and research/planned where applicable.

## Relationship to package metadata review

The package metadata review treats `pyproject.toml` as package-facing metadata that can shape public expectations. README is referenced as project readme metadata and therefore affects package-facing interpretation even when package metadata itself is unchanged.

This PR does not change `pyproject.toml`, package name, package version, classifiers, dependencies, scripts, project URLs, or package metadata. It only records whether README wording remains compatible with the current package metadata posture.

## README review method

Review method:

1. Inspect README surfaces that create public expectations.
2. Compare those surfaces to release posture, release-channel classification, package metadata review, boundary reviews, workflow taxonomy, release governance, and final readiness documentation.
3. Classify posture fit as one of: aligned, acceptable but needs clearer docs, overclaims current posture, protected/high-risk, or needs more review.
4. Identify risk if a reader misreads the surface.
5. Record a safe next action for a future narrow PR.

This review did not modify README, ROADMAP, `pyproject.toml`, source, tests, scripts, workflows, schemas, validators, records, generated artifacts, canonical artifacts, policy, federation, signatures, hash, QR, CODEOWNERS, AGENTS.md, or HC_BOOTSTRAP.md.

## README wording review table

| README surface | Current observed wording or summary | Posture fit | Risk if misread | Safe next action |
|---|---|---|---|---|
| Title / project identity | README identifies the project as `HC-TRUST-LAYER`. | aligned | Readers could still treat the repository name as a finished trust authority if not paired with boundary language. | Keep title stable; preserve early-stage and advisory context nearby. |
| Badges or metadata references | README shows license, MVP early-stage status, trust infrastructure category, verification workflow focus, and validation workflow badge. | acceptable but needs clearer docs | Badges can be read as maturity, endorsement, or guaranteed validation if detached from warnings. | Future README wording can clarify that badges and checks are status/navigation signals, not trust authority. |
| Motto or one-line claim | README describes HC:// trust infrastructure for verification workflow transparency, provenance visibility, and human-supervised validation. | aligned | The phrase could be overread as complete trust infrastructure unless scoped by early-stage text. | Keep human-supervised validation in the one-line framing and avoid stronger product promises. |
| Project description | README says HC-TRUST-LAYER is early-stage verification infrastructure supporting reproducible checks and structured review boundaries, without objective-truth finality, forensic certainty, or autonomous finality. | aligned | Low risk if kept with current disclaimers; risk rises if excerpts omit the limitations. | Preserve concise limitations in the opening section. |
| Installation / package-facing wording | README includes local dependency installation and package/CLI-oriented usage examples. | protected/high-risk | Readers may treat installability as production readiness or a complete supported product. | Future README wording can separate installable package scope from wider repository posture. |
| CLI usage wording | README shows `PYTHONPATH=src python -m hc_trust.cli verify records` and local lookup commands. | acceptable but needs clearer docs | CLI results may be mistaken for legal, forensic, identity, or certification finality. | Add future CLI boundary wording in a narrow PR without changing CLI behavior. |
| Verification / validator wording | README describes verification packages, validator review layers, result types, and human-supervised validation. | aligned | PASS/FAIL/REVIEW labels can be misread as final truth outcomes if copied without context. | Keep result definitions tied to evaluated scope and reviewer handoff. |
| QR / hash / evidence wording | README references browser-side SHA-256, QR-oriented demo limits, evidence, provenance, and audit continuity. | acceptable but needs clearer docs | Hash or QR language can be misread as authenticity proof, signed payload verification, or legal evidence finality. | Future wording can repeat that hash and QR outputs are signals or navigation aids unless separately validated. |
| Witness / audit wording | README uses audit trail continuity, provenance timeline, and reviewer handoff language. | aligned | Audit wording can be misread as regulated audit completion or external certification. | Preserve audit as repository evidence and reviewer support, not legal or certification authority. |
| Demo/example wording | README labels public validator and static viewer scenarios as demo-only, local-only, advisory-only, public-safe, and not production verification. | aligned | Demo links may be promoted externally as production verifier surfaces. | Keep demo labels explicit and consider consolidating repeated demo limitations in a future docs-only PR. |
| Governance / bot / automation wording | README points to contribution, supervised automation, issue workflow, and security/responsible use documentation. | acceptable but needs clearer docs | Readers may infer automation can approve, reject, merge, certify, label, or replace human review. | Future README wording can state CI/checks/bot reports are evidence or advisory support, not trust authority. |
| Release / roadmap wording | README states current phase and long-term direction; ROADMAP contains future stabilization, public verification, federation, integration, and ecosystem direction. | needs more review | Future-facing language can be read as committed release channels, production services, or guaranteed interoperability. | Keep roadmap links but preserve future/planned labels and avoid release-channel commitments. |
| External reference language, if present | README does not need specific external standards, organizations, products, protocols, companies, government systems, or certification bodies to explain current posture. | aligned | Naming external models could imply equivalence, compliance, partnership, endorsement, or certification. | Keep external naming generic unless a later human-reviewed PR explicitly approves specific references. |
| Security and responsible use | README says outputs are verification signals, not definitive truth claims, and asks contributors to preserve audit trail continuity. | aligned | Security wording can be overread as security certification if strengthened carelessly. | Preserve responsible-use wording and avoid certification language. |
| IP / brand / idea use notice | README says reuse should preserve origin references and avoid implying endorsement, production guarantees, or governance finality. | aligned | Brand wording could be misused as endorsement or authority if quoted out of context. | Keep non-endorsement and no-production-guarantee language explicit. |

## Claim-risk summary

Current README wording is broadly aligned with the documented release posture. It repeatedly frames HC-TRUST-LAYER as early-stage, advisory, public-safe where applicable, and human-supervised. It also includes direct limitations for production readiness, objective-truth finality, security certification, autonomous AI finality, live federation guarantee, and institutional/legal finality.

Highest-risk surfaces remain README itself, package-facing installation wording, CLI examples, PASS/FAIL result labels, QR/hash explanations, demo links, validation badges, governance automation references, and future roadmap language. These are not necessarily wrong today, but they are protected/high-risk public expectation surfaces because they can be excerpted or misunderstood.

No README wording change is made by this document.

## Current practical state

- README is the main public-facing project explanation.
- The repo has package, CLI, docs, demo, workflow, governance, record, generated/canonical, and research surfaces.
- These surfaces must not all be described under one production/product promise.
- The current repo remains early-stage, advisory, human-supervised, product-adjacent, governance-aware, and research-heavy.

## Ideal future state

README, package metadata, CLI docs, release notes, public verifier wording, demo/example labels, and governance/report language should be aligned through separate narrow PRs.

Any future README wording change should be based on this review and should preserve conservative safety wording. Future wording should maintain human final authority, avoid unsupported certainty language, and keep package, CLI, demo, governance, report, generated/canonical, and research surfaces separated.

## Safe next PR candidates

- README wording recommendation PR
- CLI help/documentation boundary review
- conservative v0.1.0 release notes wording review
- demo/example labeling review
- public verifier boundary review
- repo-wide external naming audit

## Do-not-do-yet list

- Do not change README in this PR.
- Do not change `pyproject.toml`.
- Do not change package name, version, classifiers, dependencies, scripts, or project URLs.
- Do not rename package or CLI.
- Do not publish or configure release channels.
- Do not change release automation.
- Do not change workflow enforcement.
- Do not move source modules.
- Do not promote demo/example surfaces to production.
- Do not claim certification, legal truth, identity finality, forensic certainty, production readiness, autonomous governance authority, standards compliance, partnership, endorsement, or guaranteed correctness.
- Do not expand bot or agent authority.

## Real-world analogy

A bank can have a public website, mobile app, developer tools, internal audit reports, training demos, and regulatory paperwork. The public homepage must not promise that every internal tool or demo has legal authority. HC README should explain the public project clearly while keeping package, CLI, demo, governance, report, and research surfaces separated.

## External reference-model naming posture

This PR does not name specific external standards, organizations, products, protocols, companies, government systems, or certification bodies.

When external reference-model language is needed in future work, use generic terms such as provenance metadata systems, verifiable-claim frameworks, independent timestamp evidence systems, certificate-chain based trust practice, regulated audit flows, or public-sector verification flows.

HC-TRUST-LAYER is not claiming equivalence, certification, legal authority, production readiness, standards compliance, partnership, endorsement, or guaranteed correctness with any external reference model.
