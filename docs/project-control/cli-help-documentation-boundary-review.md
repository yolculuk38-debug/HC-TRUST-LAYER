# CLI Help Documentation Boundary Review

## Purpose

This document reviews the current `hc-trust` CLI-facing wording and adjacent documentation boundaries against the already merged release posture, release-channel classification, package metadata review, README wording review, and README boundary clarification.

The purpose is to document whether current CLI-facing surfaces preserve HC-TRUST-LAYER's posture as early-stage, advisory, human-supervised HC:// verification infrastructure. The CLI may support local technical verification and evidence inspection, but CLI output is advisory evidence only. It is not legal truth, identity finality, forensic certainty, certification authority, production readiness, autonomous governance authority, standards compliance, partnership, endorsement, or guaranteed correctness.

## HC boundary statement

Preserved HC boundaries for this review:

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

CLI output must not replace human review. PASS, FAIL, REVIEW, REVIEW_REQUIRED, VERIFIED, INVALID, UNKNOWN, or similar labels, where present, must be interpreted only within the evaluated technical scope and only as reviewer-support evidence.

## Scope and non-effects

This document is advisory-only.

- It does not change CLI behavior.
- It does not change CLI help text.
- It does not change README.
- It does not change ROADMAP.
- It does not change package metadata.
- It does not change `pyproject.toml`.
- It does not change release automation.
- It does not change runtime behavior.
- It does not change workflow behavior.
- It does not change public API behavior.
- It does not change schema, validator, record, generated, canonical, policy, federation, signing, hash, or QR behavior.
- Existing governed/report-only workflow behavior is documented elsewhere and is not changed by this document.
- Existing PR Risk Labeler and HC Control Bot advisory comment behavior, where present, remains bounded by existing workflow taxonomy and governance documentation.
- Those workflows do not create release authority, approval authority, rejection authority, merge authority, certification authority, truth authority, or human-review replacement authority.

The only effect of this document is to record a documentation-only review for future narrow PRs.

## Relationship to release posture definition

The release posture definition frames HC-TRUST-LAYER as early-stage, advisory, human-supervised verification infrastructure. It identifies the installable package and `hc-trust` CLI as narrow technical surfaces, not a production product or trust authority.

This review applies that posture to the CLI-facing wording. It treats the CLI as useful for local evidence inspection while preserving the boundary that human maintainers/reviewers make the final decision.

## Relationship to release channel surface classification

The release channel surface classification identifies the CLI/advisory runtime channel as a candidate future channel and marks the CLI as protected/high-risk because users may over-read command output.

This review does not create or publish a release channel. It records that CLI help text, README CLI examples, package metadata, release notes, public verifier wording, demo/example labels, and governance/report language should be aligned through separate narrow PRs.

## Relationship to package metadata review

The package metadata review treats package identity and console entry points as user-expectation surfaces. The current package metadata provides an installable package and exposes `hc-trust`, but installation alone must not be read as production readiness, certification, legal authority, or guaranteed correctness.

This review does not change the package name, version, classifiers, dependencies, scripts, or project URLs. Future package metadata changes should remain separate from CLI wording changes.

## Relationship to README boundary wording

The README now states that HC-TRUST-LAYER is early-stage, advisory, human-supervised verification infrastructure. README CLI examples and local/demo usage wording should remain aligned with that posture.

This review finds that README boundary language is generally aligned, while the concise CLI example could benefit from a future adjacent note that CLI output supports evidence inspection and reviewer handoff rather than final authority.

## CLI review method

Review method:

1. Inspect `pyproject.toml` for the console entry point and package-facing wording.
2. Inspect `src/hc_trust/cli.py`, `src/hc_trust/__main__.py`, and related `src/hc_trust` verification modules for CLI-visible command names, help text, result labels, JSON fields, warnings, and error messages.
3. Run local CLI help commands to observe top-level and subcommand help text.
4. Inspect README CLI examples and local/demo usage wording.
5. Compare observed wording with existing project-control and governance posture documents.

Reviewed commands included:

```bash
PYTHONPATH=src python -m hc_trust.cli --help
PYTHONPATH=src python -m hc_trust.cli verify --help
PYTHONPATH=src python -m hc_trust.cli verify-package --help
```

## CLI surface review table

| CLI surface | Current observed wording or behavior summary | Posture fit | Risk if misread | Safe next action |
| --- | --- | --- | --- | --- |
| `pyproject.toml` console entry point | Exposes `hc-trust = "hc_trust.cli:main"`. Package description is short: `HC Trust Layer utilities`. | Acceptable but needs clearer docs | Users may treat package installation and command availability as production readiness or a complete trust product. | Keep metadata unchanged here; consider a future package metadata wording PR only if maintainers want more conservative package-facing language. |
| CLI module entrypoint | `src/hc_trust/__main__.py` delegates to `cli.main`; `src/hc_trust/cli.py` builds the parser and routes commands. | Aligned | Entrypoint itself is neutral, but command output can still be over-read. | No behavior change; document advisory CLI interpretation. |
| Top-level CLI help text | Help output says `HC Trust Layer CLI` and lists `verify`, `hash`, `qr`, and `verify-package`. | Acceptable but needs clearer docs | The bare phrase may look product-like without advisory boundary context. | Future CLI help wording recommendation PR can add conservative boundary wording. |
| Command names | Commands are `verify`, `hash`, `qr`, and `verify-package`. | Protected/high-risk | `verify` and `verify-package` may be mistaken for final truth, certification, or identity validation. | Keep names unchanged here; future docs/help should clarify evaluated technical scope. |
| `verify` command description | Help says `Verify record content hashes`; runtime prints hash verification progress and pass/fail count. | Acceptable but needs clearer docs | Users may treat hash agreement as full record truth, identity finality, or authority. | Future CLI help could say local content-hash check and point to human review. |
| `hash` command description | Help says `Calculate file SHA256`; output prints a digest for a local file. | Aligned | Low risk; digest calculation could still be misused as provenance proof if isolated from context. | No immediate change; docs can remind users that a digest is evidence, not authority. |
| `qr` command description | Help says `Generate verification QR`; output includes secure QR wording and URL text. | Needs more review | QR wording may imply authenticity or secure verification beyond generated link material. | Future QR/demo wording review should distinguish navigation support from authenticity or final trust proof. |
| `verify-package` command description | Help says it verifies a local HC verification package manifest and SHA-256 file integrity. | Aligned | Some users may shorten this to full package truth or authority despite the scoped wording. | Preserve scoped wording; future help can add advisory-only boundary text. |
| `verify` result wording | `PASS` and `FAIL` are emitted by record hash checks, with final `Results: n passed, n failed`. | Protected/high-risk | PASS may be mistaken for full record validity, legal truth, or reviewer approval; FAIL may be mistaken for final rejection beyond technical hash scope. | Future documentation should state PASS/FAIL are local content-hash outcomes only. |
| `verify-package` status labels | JSON and summary may include `VERIFIED`, `INVALID`, or `REVIEW_REQUIRED`. | Protected/high-risk | VERIFIED may be mistaken for final trust, identity, timestamp, witness, legal, or certification authority. | Preserve current advisory fields; future docs should keep status labels scoped to local package integrity checks. |
| JSON output fields | Package verification JSON includes `status`, `verified`, `advisory_only`, `public_safe`, `truth_guarantee`, `human_review_required`, paths, IDs, checks, missing evidence, conflicting evidence, and warnings. | Aligned | `verified: true` can be over-read if separated from `advisory_only` and `truth_guarantee`. | Keep advisory fields visible; future formatter docs should explain each field. |
| Warnings and advisory fields | Summary output includes `human_review_required`, `advisory_only: true`, `public_safe: true`, `truth_guarantee: false`, and optional warning/evidence lists. | Aligned | Human review can be missed if users only read status. | Future docs can recommend reading boundary fields before acting on status. |
| Verification package module wording | Module docstring states local-only and advisory-only, and excludes legal truth, QR authenticity, signature validity, witness authority, timestamp authority, and production readiness. | Aligned | Low risk if users read it; CLI help does not expose all of this context. | Reuse this wording as source material for future CLI help/docs PRs. |
| README CLI examples | README shows local command usage for `PYTHONPATH=src python -m hc_trust.cli verify records` near preview-only and human-supervised validation wording. | Aligned | The code block alone may be copied without surrounding boundary text. | Future README CLI example boundary note PR can attach an explicit advisory-output note. |
| README local/demo usage wording | README describes public-safe advisory demo and local-only lookup boundaries, including no production API and human review requirements. | Aligned | Low to moderate risk if users skip surrounding paragraphs. | Keep README unchanged here; future narrow PR may improve CLI-specific callouts. |
| Error messages and user-facing messages | Some messages report missing files, invalid JSON, skipped files, and QR argument errors. Some current strings are not English. | Needs more review | Non-English messages can reduce reviewer clarity; terse errors may not state advisory boundaries. | Future CLI wording PR may standardize English user-facing text without changing behavior. |
| Lookup wording | The main `hc-trust` CLI does not expose a `lookup` command; README references local lookup through a script outside the CLI. | Aligned | Users may conflate script lookup with general CLI or hosted lookup behavior. | Keep boundaries in README and demo docs; review lookup script wording separately if changed. |

## Claim-risk summary

The current CLI-facing surfaces are mostly aligned with the repository posture because the strongest package verification output includes explicit `advisory_only`, `public_safe`, `truth_guarantee`, and `human_review_required` fields. The main risk is user expectation: concise terms such as `verify`, `verified`, `PASS`, `FAIL`, `Secure QR`, and `HC Trust Layer CLI` can be over-read outside their technical scope.

The CLI is therefore a protected/high-risk user expectation surface. It may support local technical verification and evidence inspection, but it must not be presented as trust authority. CLI output must not imply legal truth, identity finality, forensic certainty, certification authority, production readiness, autonomous governance authority, standards compliance, partnership, endorsement, or guaranteed correctness.

## Current practical state

- The repository has an installable package and a CLI-facing entry point.
- README now states that HC-TRUST-LAYER is early-stage, advisory, human-supervised verification infrastructure.
- CLI-facing wording must remain aligned with that README posture.
- CLI output should support evidence inspection and reviewer handoff, not final authority.
- Existing package verification output already includes boundary fields that preserve advisory-only, public-safe, truth-guarantee-false, and human-review-required interpretation.
- Some concise help strings and result labels would benefit from clearer documentation or future wording changes.

## Ideal future state

CLI help text, README CLI examples, package metadata, release notes, public verifier wording, demo/example labels, and governance/report language should be aligned through separate narrow PRs.

Any future CLI wording change should be based on this review and should preserve conservative safety wording. Future output documentation should make clear that PASS/FAIL/REVIEW-style labels are scoped to evaluated technical checks only and that human maintainers/reviewers make the final decision.

## Safe next PR candidates

- CLI help wording recommendation PR
- README CLI example boundary note PR
- conservative v0.1.0 release notes wording review
- public verifier boundary review
- demo/example labeling review
- repo-wide external naming audit

## Do-not-do-yet list

- Do not change CLI behavior in this PR.
- Do not change CLI help text in this PR.
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

A bank can provide an internal audit command-line tool, a customer app, a public website, and regulated legal processes. A command-line tool can help staff inspect evidence, but it does not become the bank's legal authority by printing a status. HC CLI output should be treated as scoped evidence and reviewer support, not final trust authority.

## External reference-model naming posture

This review intentionally avoids naming specific external standards, organizations, products, protocols, companies, government systems, or certification bodies.

Generic reference models may be useful for future comparison, including provenance metadata systems, verifiable-claim frameworks, independent timestamp evidence systems, certificate-chain based trust practice, regulated audit flows, and public-sector verification flows. HC-TRUST-LAYER is not claiming equivalence, certification, legal authority, production readiness, standards compliance, partnership, endorsement, or guaranteed correctness against any of those reference models.
