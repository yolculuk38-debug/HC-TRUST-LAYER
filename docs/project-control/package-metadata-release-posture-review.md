# Package Metadata Release Posture Review

## Purpose

This document reviews the current Python package metadata and CLI/package-facing claims against the already merged HC-TRUST-LAYER release posture and release-channel classification documents.

It exists before any future change to `pyproject.toml`, package metadata, README wording, ROADMAP wording, release notes, CLI behavior, release automation, or package-facing public claims.

## HC boundary statement

HC-TRUST-LAYER remains early-stage, advisory, human-supervised, product-adjacent, governance-aware, and research-heavy HC:// verification infrastructure.

This document preserves these HC boundaries:

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

## Scope and non-effects

This document is advisory-only.

It does not change package metadata. It does not change `pyproject.toml`. It does not change README or ROADMAP. It does not change release automation. It does not change CLI behavior. It does not change runtime behavior. It does not change workflow behavior. It does not change public API behavior. It does not change schema, validator, record, generated, canonical, policy, federation, signing, hash, or QR behavior.

Existing governed/report-only workflow behavior is documented elsewhere and is not changed by this document. Existing PR Risk Labeler and HC Control Bot advisory comment behavior, where present, remains bounded by existing workflow taxonomy and governance documentation. Those workflows do not create release authority, approval authority, rejection authority, merge authority, certification authority, truth authority, or human-review replacement authority.

This review treats `hc_trust` and package metadata as a narrow package-facing release surface only. It treats the `hc-trust` CLI as advisory runtime unless a later PR proves otherwise. It does not imply that the full repository is a finished product because a package and CLI exist.

## Relationship to release posture definition

The release posture definition frames HC-TRUST-LAYER as advisory HC:// verification infrastructure with human-supervised validation and conservative release claims. The current package metadata is therefore reviewed as a scoped technical surface, not as a full product identity or production-readiness statement.

This document follows the release posture definition by avoiding claims of production readiness, legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, or guaranteed correctness.

## Relationship to release channel surface classification

The release channel surface classification separates the core package, CLI/advisory runtime, public verifier, demo/example, governance/report, generated/canonical evidence, and federation/research surfaces. This review applies that channel distinction to current package metadata.

The package and CLI can be package-facing surfaces without carrying the promises of public verifier, governance authority, generated/canonical evidence, records, federation, or future research channels.

## Package metadata review method

Review method:

1. Inspect `pyproject.toml` for current package metadata and package discovery configuration.
2. Compare package-facing wording with README, ROADMAP, repository map, release posture, release channel classification, package boundary, CLI/API boundary, demo/example boundary, generated/canonical ownership, workflow taxonomy, source module boundary, release governance, v0.1.0 release checklist, and final readiness review documents.
3. Classify each observed metadata surface using the following posture fit values: `aligned`, `acceptable but needs clearer docs`, `overclaims current posture`, `protected/high-risk`, or `needs more review`.
4. Identify risks if readers misread package metadata as broader than the narrow package-facing release surface.
5. Record safe next actions without changing package metadata.

## Package metadata review table

| Field / surface | Current observed wording or behavior | Release posture fit | Risk if misread | Safe next action |
| --- | --- | --- | --- | --- |
| project name | `hc-trust-layer` | acceptable but needs clearer docs | The package name could be read as representing the whole HC-TRUST-LAYER trust ecosystem, not only a scoped Python package surface. | In a later PR, consider documentation that distinguishes the package label from repository-wide governance, records, public verifier, and federation surfaces. |
| version | `0.1.0` | aligned | Users may treat a v0.1.0 package version as production readiness if surrounding docs are not conservative. | Keep v0.1.0 release wording advisory and evidence-bound. |
| description | `HC Trust Layer utilities` | acceptable but needs clearer docs | The phrase is concise but may be too broad if read as complete trust infrastructure or verification authority. | In a later metadata PR, consider a narrower advisory description only after maintainer review. |
| readme | `README.md` | protected/high-risk | README wording can shape public package expectations and may be mistaken for complete product scope. | Review README wording separately before any package metadata or README change. |
| requires-python | `>=3.14` | needs more review | A strict Python requirement may affect installability expectations but does not itself create trust authority. | Review packaging compatibility separately; do not mix with posture-only docs. |
| license | No `[project]` license field observed in `pyproject.toml`; repository badge references Apache-2.0 in README. | needs more review | Package index readers may not see license posture directly from package metadata. | Review package license metadata in a future narrow packaging PR if maintainers approve. |
| authors/maintainers | No authors or maintainers field observed. | needs more review | Missing contact metadata could obscure package stewardship, but adding names can imply authority or support expectations if not bounded. | Review maintainer metadata separately with governance-aware wording. |
| keywords | No keywords observed. | aligned | No keyword over-marketing risk exists in current metadata. | If keywords are later added, keep them conservative and avoid certification, truth, identity-final, or production wording. |
| classifiers | No classifiers observed. | aligned | No classifier overclaim exists today; future classifiers could imply maturity, audience, or production stability. | Review classifiers in a separate metadata PR before publication changes. |
| dependencies | `fastapi==0.138.1`, `jsonschema==4.26.0`, `pydantic==2.13.4`, `qrcode[pil]==8.2` | protected/high-risk | Dependencies suggest API, validation, and QR capability; readers may infer production API, schema finality, or QR authenticity guarantees. | Keep dependency review separate from docs posture; document advisory boundaries for API, validation, and QR claims. |
| optional dependencies | `test` extra with `anyio`, `httpx`, and `pytest` pins/markers | aligned | Test extras are likely read as development support, not public trust authority. | Keep test dependency changes out of posture docs; review separately if packaging policy changes. |
| scripts / console entry points | `hc-trust = "hc_trust.cli:main"` | protected/high-risk | A CLI named `hc-trust` may be mistaken for final verification, certification, legal truth, identity finality, or autonomous trust decisions. | Conduct a CLI help/documentation boundary review before changing CLI behavior or package metadata. |
| package discovery settings | `package-dir = {"" = "src"}` and package discovery where `src` | protected/high-risk | Discovery settings expose package modules and may shape public API assumptions if users infer all modules are stable. | Keep package discovery unchanged; review public API/package boundary separately. |
| project URLs | No project URLs observed. | needs more review | Missing URLs may limit package-index navigation; future URLs could route users to docs that overstate status if not conservative. | Review project URLs only in a future metadata PR with advisory target pages. |
| build system metadata | `setuptools>=68`, `wheel`, `setuptools.build_meta` | aligned | Build backend metadata is technical and does not imply trust authority. | No posture action needed unless packaging process changes. |

## CLI/package-facing claim review

Current package-facing surfaces indicate an installable package and the `hc-trust` console entry point. That is enough to create user expectations, but it is not enough to claim a finished product, production verifier, legal or regulatory decision system, certification authority, identity authority, forensic authority, autonomous governance authority, or guaranteed correctness.

The CLI should be treated as advisory runtime. CLI output can support human-supervised validation, but it must not replace reviewer judgment or repository-defined governance. Any future CLI help text, README quickstart, package description, release notes, or public verifier wording should make the bounded advisory status visible.

## Current practical state

HC-TRUST-LAYER has an installable package and CLI-facing metadata.

The wider repository remains early-stage, advisory, human-supervised, product-adjacent, governance-aware, and research-heavy.

Package metadata should be conservative and should not over-market the full repository.

## Ideal future state

Package metadata, README, CLI docs, release notes, public verifier claims, demo/example labels, and governance/report language can be aligned through separate narrow PRs.

Any future package metadata change should be based on this review and should preserve conservative safety wording.

## Safe next PR candidates

- docs-only package metadata wording recommendation
- README wording review against release posture
- CLI help/documentation boundary review
- conservative v0.1.0 release notes wording review
- demo/example labeling review
- public verifier boundary review

## Do-not-do-yet list

- Do not change `pyproject.toml`.
- Do not change package name, version, classifiers, dependencies, scripts, or project URLs.
- Do not rename package or CLI.
- Do not publish or configure release channels.
- Do not change release automation.
- Do not change workflow enforcement.
- Do not move source modules.
- Do not promote demo/example surfaces to production.
- Do not claim certification, legal truth, identity finality, forensic certainty, production readiness, autonomous governance authority, or guaranteed correctness.
- Do not expand bot or agent authority.

## Real-world analogy

A bank can publish a mobile app, internal audit tools, compliance reports, developer SDKs, and training demos. The package label must not promise the authority of the whole bank. HC package metadata should describe the narrow package surface, not overclaim the full trust ecosystem.

## External standards reference posture

External standards and institutional practices are useful reference models for cautious wording, not equivalence claims.

- C2PA-style provenance does not mean truth finality.
- W3C Verifiable Credentials-style claims still require issuer, verifier, and trust-context boundaries.
- OpenTimestamps-style timestamp evidence does not certify semantic truth.
- SSL/TLS certificates prove bounded cryptographic assertions, not that all content is true.
- Bank and e-government systems separate customer-facing services, internal audit logs, compliance reports, and legal authority.

This PR does not claim HC-TRUST-LAYER equivalence with those systems. It does not claim certification, legal authority, production readiness, standards compliance, or guaranteed correctness.
