# Core Package Boundary Review

## 1. Purpose

This document is an advisory, documentation-only review of the observed HC-TRUST-LAYER core package and trust-boundary structure.

It supports backlog item 4-1, “core package boundary review.” It classifies existing repository paths by observed role so future maintainers can discuss what appears to be trust-critical core logic, validation support, CLI/demo support, documentation, generated or canonical artifacts, tests, and experimental support.

This review does not move files, rename files, refactor code, change imports, change package metadata, change validators, change schemas, change records, change generated or canonical artifacts, change signing or federation behavior, change workflows, or add enforcement.

## 2. HC boundary

- `advisory_only=true`.
- `public_safe=true`.
- `truth_guarantee=false`.
- `human_review_required=true`.
- This documentation review does not approve, reject, certify, merge, or establish truth.
- CI/checks are evidence, not trust authority.
- The human maintainer remains the final authority.

HC-TRUST-LAYER documentation, checks, records, examples, validators, scripts, workflows, and generated artifacts must not be treated as legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, guaranteed correctness, or production readiness.

## 3. Review method

This review inspected the repository tree and classified existing paths by observed role. Classification is conservative and based on visible path names, repository documentation, and current organization. It does not assert hidden maintainer intent.

Observed categories reviewed:

- trust-critical core logic;
- schema/contracts;
- validators;
- records/evidence;
- generated/canonical artifacts;
- signing/signature material;
- federation or external trust interfaces;
- CLI/demo/local tools;
- scripts/report-only scanners;
- docs/governance;
- tests;
- workflows/automation;
- examples/fixtures if present;
- experimental or future-facing areas if present.

If a requested category was not observed as a top-level or clear nested repository area, it is marked as `not observed`. Some areas need maintainer confirmation before any future refactor because names alone cannot prove authority or ownership.

## 4. Boundary classification table

| Path | Observed role | Trust sensitivity | Runtime impact | Mutation risk | Review expectation | Notes |
|---|---|---|---|---|---|---|
| `src/` | Runtime and library implementation surfaces; observed HC runtime, trust, API, and security modules. | critical | Direct runtime impact. | High: can change verification semantics or operator output. | Implementation review, tests, and maintainer confirmation for boundary changes. | Appears to be the current core package boundary, especially `src/hc_trust/` and `src/hc_runtime/`. |
| `src/hc_trust/` | HC trust tooling implementation surface. | critical | Direct runtime impact. | High. | Treat as core logic; refactor only in small tested PRs. | Needs maintainer confirmation before namespace split or public API claims. |
| `src/hc_runtime/` | HC runtime implementation surface. | critical | Direct runtime impact. | High. | Treat as core logic; refactor only in small tested PRs. | Runtime behavior should not be casually modified. |
| `src/api/` | API-adjacent runtime surface. | high | Possible runtime or integration impact. | Medium to high. | Maintain API boundary review before changes. | Needs maintainer confirmation before declaring public API stability. |
| `src/security/` | Security-adjacent runtime support. | high | Possible runtime/security interpretation impact. | High. | Security-aware implementation review and tests. | Do not overstate security guarantees from this path. |
| `schema/` | Schema definitions and verification contracts. | critical | Indirect to direct validation impact. | High: can change record shape expectations. | Protected-path review and explicit justification. | Canonical contract material; not changed by this review. |
| `validators/` | Protected validation and verification surfaces. | not observed | Not observed. | Not observed. | If added later, treat as high or critical. | No top-level `validators/` directory was observed in this repository tree during this review. |
| `records/` | Evidence-bearing records, archives, pending and verified examples, and provenance material. | critical | Usually indirect, but evidence interpretation impact is high. | High: can damage audit continuity. | Protected-path review; preserve evidence and history. | Includes `records/signatures/`, which is signature/evidence-adjacent. |
| `generated/` | Generated or derived artifacts. | generated/artifact | Indirect; may influence review evidence. | High if hand-edited. | Do not edit without generation and audit path. | Generated artifacts are evidence, not trust authority. |
| `canonical/` | Canonical artifact area. | not observed | Not observed. | Not observed. | If added later, treat as generated/artifact or critical. | No top-level `canonical/` directory was observed during this review. |
| `trust-kernel-index.json` | Root trust-kernel reference artifact. | critical | Indirect trust-boundary interpretation impact. | High. | Explicit maintainer review before mutation. | Root canonical/protected interpretation surface. |
| `verification-map.json` | Root verification map reference. | high | Indirect trust-boundary interpretation impact. | High. | Explicit maintainer review before mutation. | Evidence and verification navigation surface. |
| `policy/` | Policy and governance-control material. | critical | Indirect governance and trust interpretation impact. | High. | Protected-path review and explicit justification. | Do not modify casually. |
| `signing/` | Signing implementation or signing reference path. | not observed | Not observed. | Not observed. | If added later, treat as critical. | No top-level `signing/` directory was observed during this review. |
| `signatures/` | Signature material path. | not observed | Not observed. | Not observed. | If added later, treat as critical. | No top-level `signatures/` directory was observed; `records/signatures/` is observed. |
| `records/signatures/` | Signature-related evidence or record material. | critical | Indirect evidence/signature interpretation impact. | High. | Protected evidence review. | Preserve auditability; do not treat as implemented signing authority. |
| `federation/` | Federation schemas or example external trust-interface material. | high | Possible future external trust impact. | High. | Protected-path review and maintainer confirmation. | Federation surfaces should remain conservative until explicitly implemented and reviewed. |
| `.github/` | Workflow, issue, PR, and automation configuration. | high | CI and review-flow impact. | High. | Workflow/governance review; do not change in docs-only boundary PRs. | Automation provides evidence or mutation according to workflow design, not final trust authority. |
| `.github/workflows/` | GitHub Actions automation. | high | CI/review behavior impact. | High. | Workflow review and branch-protection awareness. | Not changed by this review. |
| `scripts/` | Checks, validators, report generators, scanners, and local operator helpers. | medium | Can affect reports, local checks, or validation evidence. | Medium to high. | Keep report-only scanners report-only unless explicitly promoted. | Scripts may support evidence but do not approve, certify, or establish truth. |
| `tools/` | Developer tooling and helper documentation. | medium | Local helper impact. | Medium. | Scoped review for behavior changes. | Tool output should remain advisory unless separately reviewed. |
| `docs/` | Documentation, architecture, governance, demos, planning, and explanatory material. | docs-only | No runtime impact unless docs are consumed by automation. | Low to high depending on governance meaning. | Docs review; governance docs need extra care. | Docs can explain boundaries but must not claim legal truth or certification. |
| `docs/project-control/` | Project-control planning, status, and operating-layer coordination. | medium | No direct runtime impact. | Medium: can affect operator interpretation. | Keep concise, advisory, and human-reviewed. | This document lives here. |
| `docs/governance/` | Governance documentation. | high | Governance interpretation impact. | High. | Maintainer/governance review. | Do not use docs to grant approval or merge authority. |
| `docs/core/`, `docs/runtime/`, `docs/spec/`, `docs/architecture/`, `docs/verification/` | Core, runtime, specification, architecture, and verification explanation. | high | Indirect behavior and trust interpretation impact. | Medium to high. | Maintainer confirmation when used as normative boundary material. | Explanatory docs may be read as contracts; wording should remain careful. |
| `docs/demo/`, `docs/public/`, `docs/explorer/` | Demo, public verification, and explorer documentation. | low | No direct runtime impact. | Medium: public claims can be over-read. | Public-safe docs review. | Demos must not be mistaken for trust guarantees. |
| `docs/future/`, `docs/vision/`, `docs/drafts/` | Future-facing, vision, and draft material. | low | No direct runtime impact. | Medium if treated as implemented behavior. | Mark advisory or draft when needed. | Experimental or future-facing areas are present. |
| `tests/` | Test suites and fixtures. | medium | Indirect runtime confidence impact. | Medium. | Keep mapped to boundary areas and update with code changes. | Tests are evidence, not trust authority. |
| `test_integration.py` | Root integration test. | medium | Indirect runtime confidence impact. | Medium. | Review with runtime and validation changes. | Root test file exists outside `tests/`. |
| `examples/` | Examples, fixtures, demo packages, and report inputs. | low | Usually none; possible local demo impact. | Medium if confused with canonical evidence. | Keep advisory and non-canonical unless explicitly promoted. | Examples and fixtures are present. |
| `exports/` | Exported schemas or sample packages. | generated/artifact | Indirect evidence or packaging impact. | Medium to high. | Maintainer confirmation before mutation. | May be generated or release-support material. |
| `hash/` | Hash references or integrity artifacts. | generated/artifact | Indirect integrity interpretation impact. | High. | Do not hand-edit without audit path. | Treat as evidence-adjacent. |
| `qr/` | QR-related verification artifacts or references. | generated/artifact | Indirect verification interpretation impact. | High. | Do not hand-edit without audit path. | Treat as evidence-adjacent. |
| `reviewers/` | Reviewer registry material. | high | Governance interpretation impact. | High. | Maintainer review. | Can affect perceived reviewer boundaries. |
| `council/`, `witness/`, `timeline/`, `witness-archive/` | Governance, witness, timeline, or historical/evidence-adjacent material. | high | Indirect provenance or governance interpretation impact. | High. | Preserve evidence and historical context. | Do not silently rewrite history. |
| `agents/`, `hc_context/` | Agent and context material. | medium | Operator guidance impact. | Medium. | Advisory wording and human-final-authority review. | Helpful context, not final trust authority. |
| `media/` | Media assets and public-facing support material. | low | No direct runtime impact. | Low to medium. | Docs/public review when changed. | Sensitivity rises if media becomes evidence-bearing. |
| Root governance files such as `AGENTS.md`, `CODEOWNERS`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `HC_CONSTITUTION.md`, `SUPPORT.md`, and `LICENSE` | Contributor rules, governance, ownership, support, and licensing. | high | Governance and contribution interpretation impact. | High. | Maintainer review; ownership files require special care. | `CODEOWNERS` and `AGENTS.md` are not changed by this review. |
| Package metadata such as `requirements.txt`, `requirements-test.txt`, and `VERSION` | Dependency and version metadata. | high | Runtime, test, or release impact. | High. | Separate implementation/release review. | Not changed by this docs-only review. |

## 5. Core package boundary findings

The current practical core package boundary appears to be the implementation under `src/`, especially `src/hc_trust/` and `src/hc_runtime/`. Additional adjacent runtime or integration surfaces include `src/api/` and `src/security/`. These paths should be treated as trust-critical or high-sensitivity because they can affect local verification behavior, runtime output, operator interpretation, or future public API expectations.

Trust-critical or high-sensitivity paths include `src/`, `schema/`, `records/`, `records/signatures/`, `policy/`, `federation/`, `.github/`, root trust references such as `trust-kernel-index.json` and `verification-map.json`, root governance files, reviewer/witness/governance records, and package metadata. These paths should not be casually modified, and future refactors should be split into small PRs with tests and explicit maintainer review.

Documentation and support-only paths include most explanatory material under `docs/`, demo guidance under `docs/demo/`, public/explorer guidance under `docs/public/` and `docs/explorer/`, local examples under `examples/`, and helper documentation under `tools/`. These areas still need careful language because public-safe advisory docs can be over-read as guarantees.

Generated or canonical-adjacent paths include `generated/`, `exports/`, `hash/`, `qr/`, root trust references, and any future `canonical/` path. These should not be hand-edited without a clear generation, review, and audit path. Where generated status is unclear, maintainer confirmation is required before mutation.

Paths needing maintainer confirmation before refactor include `src/api/`, `src/security/`, `exports/`, `reviewers/`, `council/`, `witness/`, `timeline/`, `witness-archive/`, `agents/`, `hc_context/`, and specification-like documentation under `docs/core/`, `docs/runtime/`, `docs/spec/`, `docs/architecture/`, and `docs/verification/`.

## 6. Protected surface recommendations

- Schema, validators, records, generated/canonical artifacts, signing, federation, policy, and workflow governance paths require careful review.
- Generated/canonical artifacts should not be edited without a generation and audit path.
- Validators should stay deterministic and test-covered.
- Scripts that produce advisory reports must remain report-only unless explicitly promoted through a separate reviewed change.
- Demos and examples must not be mistaken for trust guarantees.
- Docs may explain trust boundaries but must not claim legal truth, certification, identity finality, forensic certainty, autonomous governance authority, guaranteed correctness, or production readiness.
- Refactors should be split into small PRs with tests.
- Workflow, label, comment, reviewer-request, approval, rejection, merge, or close authority should not be added through boundary documentation.
- Package metadata, dependency files, validators, schemas, records, generated artifacts, and canonical artifacts should remain outside documentation-only boundary review PRs unless explicitly authorized.

## 7. Ideal vs current practical state

### Ideal

- Clear public API.
- Clear core package namespace.
- Explicit trust-kernel boundary.
- Deterministic validators.
- Generated artifacts separated from source.
- Test taxonomy mapped to boundary areas.

### Current practical next step

- Document observed boundaries first.
- Do not move code yet.
- Do not rename packages yet.
- Do not change imports yet.
- Do not promote examples or demos into trust guarantees.
- Only propose later refactor or cleanup PRs after maintainer review.

## 8. Real-world analogy

SSL/TLS certificate ecosystems separate key material, validation logic, certificate transparency logs, operator tooling, and browser UI. Banks and e-devlet-style services similarly separate transaction records, audit logs, operator panels, and public views.

HC-TRUST-LAYER should follow the same conservative separation pattern: core trust logic, evidence records, generated artifacts, validators, governance docs, report-only scanners, demos, and public-facing views should remain distinguishable so reviewers can understand what is authoritative, what is advisory evidence, and what is only explanatory support.

## 9. Follow-up items

- 4-1b optional: add CODEOWNERS/protected-path review for core boundary if needed.
- 4-2: test taxonomy / coverage boundary review.
- 4-3: public API / CLI boundary review.
- 4-4: generated/canonical artifact ownership review.
- 4-5: demo/example boundary review.

These follow-ups should remain small, scoped, evidence-preserving, and human-reviewed. They should not add approval, merge, comment, label, reviewer-request, close, or autonomous governance authority.
