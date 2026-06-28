# Public API / CLI Boundary Review

## 1. Purpose

This document is an advisory, documentation-only review of observed HC-TRUST-LAYER public API, CLI, validator, QR, demo, and public-facing output boundaries.

It supports backlog item 4-3, “public API / CLI boundary review.” It maps visible public-facing surfaces by path and apparent role so maintainers can separate evidence outputs, advisory signals, demo-only flows, and surfaces that need stronger boundary language before future promotion.

This review does not change public API behavior, CLI behavior, validators, schemas, records, generated or canonical artifacts, workflows, tests, runtime behavior, or CI behavior.

## 2. HC boundary

- `advisory_only=true`.
- `public_safe=true`.
- `truth_guarantee=false`.
- `human_review_required=true`.
- Public outputs are evidence or advisory signals, not trust authority.
- API, CLI, QR, and demo outputs do not establish legal truth, identity finality, forensic certainty, certification, or production readiness.
- The human maintainer remains the final authority.

HC-TRUST-LAYER public-facing outputs must be interpreted as bounded evidence, local validation results, demo output, or advisory review material unless a separate human-reviewed PR explicitly promotes a surface with tests and documentation. No public surface should be read as autonomous governance authority or guaranteed correctness.

## 3. Review method

This review inspected observed public-facing surfaces by path and name, then classified them by apparent role. It does not invent files or directories and does not assert hidden maintainer intent. If a category was not observed, it is marked as `not observed`.

Observed categories reviewed:

- public validator surfaces;
- CLI entrypoints and command outputs;
- verification package CLI summaries;
- API response contracts;
- QR parser, QR public validator, QR record bridge, and QR spoofing outputs;
- static viewer, public explorer, browser, and mobile demo flows;
- demo runners and fixtures;
- public-safe telemetry or status outputs if present;
- relationship to `docs/project-control/core-package-boundary-review.md`;
- relationship to `docs/project-control/test-taxonomy-review.md`.

The review is conservative. Paths under `src/` and `scripts/` may produce public-facing output, but this PR only documents the boundary and does not inspect or alter runtime behavior beyond path/name-level review.

## 4. Public surface classification table

| Surface / path | Observed role | Public audience | Output type | Trust sensitivity | Boundary statement required | Tests or evidence observed | Notes |
|---|---|---|---|---|---|---|---|
| `src/public_validator.py` | Public validator implementation surface. | Public users, reviewers, integrators. | Advisory validation result. | critical | Yes: validation output is evidence/advisory-only, not truth authority. | Public validator tests are referenced in the test taxonomy. | Needs maintainer confirmation before any stable public contract claim. |
| `src/hc_runtime/public_validator_lookup.py` | Local public validator lookup support. | Public demo users and maintainers. | Lookup status and record-matching signal. | high | Yes: lookup is supporting evidence only. | Demo lookup docs and tests are observed. | Must avoid implying record existence equals real-world truth. |
| `scripts/run_public_validator_lookup.py` | Script entrypoint for local lookup. | Maintainers, demo operators. | CLI-like local output. | high | Yes: local-only advisory lookup. | Referenced by public validator demo docs. | CLI behavior unchanged by this review. |
| `scripts/run_public_validator_demo.py` | Deterministic local public validator demo runner. | Public demo users, reviewers. | Demo JSON output. | demo-only | Yes: demo-only and advisory-only. | `tests/test_public_validator_demo_runner.py` observed. | Demo fixtures must stay separated from real records. |
| `docs/demo/fixtures/` | Public validator demo fixtures. | Public demo users, reviewers. | Fixture/demo evidence examples. | demo-only | Yes: fixtures are not real verification authority. | Demo runner tests reference fixture results. | Fixture records should not be promoted silently. |
| `docs/demo/public-validator-static-viewer.html` | Static viewer for public validator demo output. | Public users and reviewers. | Browser/static demo output. | medium | Yes: static viewer is advisory/demo output. | Static viewer tests are referenced in test taxonomy. | Visual language should avoid over-claiming. |
| `docs/explorer/` and `docs/public-explorer-mvp.md` | Public explorer documentation and static explorer surface. | Public users, maintainers. | Explorer/demo view. | medium | Yes: explorer output is navigation/evidence, not authority. | Explorer smoke and MVP tests are referenced in test taxonomy. | Public Explorer appears future-facing or MVP-bounded. |
| `src/public_verification_explorer.py`, `src/public_explorer_api.py`, `src/trust_explorer.py`, `src/verification_explorer.py` | Explorer/API-adjacent runtime surfaces. | Integrators and public viewers. | Explorer/API result or view data. | high | Yes: public output requires strict boundary language. | Explorer tests are referenced in test taxonomy. | Needs maintainer confirmation before public API stability claims. |
| `src/public_validator_api.py`, `src/verification_api.py`, `src/validator_api.py`, `src/api/routes/verification_routes.py` | API response and verification route surfaces. | Integrators, clients, maintainers. | API response contract. | critical | Yes: response fields must preserve advisory and human-review boundaries. | API/schema/public response tests are referenced in test taxonomy. | Stable contract status needs maintainer confirmation. |
| `src/hc_runtime/contracts/responses.py`, `src/hc_trust/api_schema.py`, `src/public_verification_response.py`, `src/sdk_response.py`, `src/validator_response.py` | Response contract and SDK-style output shapes. | Integrators and maintainers. | Structured response fields. | high | Yes: field meaning must be documented conservatively. | SDK/public response tests are referenced in test taxonomy. | Fields can be misunderstood as final verification. |
| `pyproject.toml` entrypoint `hc-trust = "hc_trust.cli:main"` | Installed CLI entrypoint. | Operators and maintainers. | CLI command output. | high | Yes: CLI output remains evidence/advisory-only. | CLI tests are referenced in test taxonomy. | Not modified in this docs-only PR. |
| `src/hc_trust/cli.py` and `src/hc_trust/__main__.py` | HC Trust CLI implementation surface. | Operators and maintainers. | CLI output/status. | high | Yes: command success must not imply real-world truth. | `tests/test_verification_cli.py` is referenced in test taxonomy. | CLI contract needs maintainer confirmation before promotion. |
| `src/verification_cli.py`, `src/verifier_entry.py`, `src/offline_verifier.py` | Verification CLI/offline verifier-adjacent surfaces. | Operators and maintainers. | CLI/offline verification summary. | high | Yes: local verification is supporting evidence. | Offline verifier and CLI tests are referenced in test taxonomy. | Offline output must not imply legal finality. |
| `scripts/view_verification_package.py` | Verification package CLI viewer. | Operators, reviewers, public demo users. | Human-readable package summary. | high | Yes: package summaries are advisory evidence summaries. | Package schema/summary tests are referenced in test taxonomy. | Summary output can be mistaken for certification. |
| `scripts/export_verification_package.py`, `scripts/validate_verification_package_examples.py` | Verification package export/validation helpers. | Maintainers and reviewers. | Package/export validation evidence. | high | Yes: export and validation are evidence only. | Package checks are referenced in test taxonomy. | Generated/canonical ownership remains separate follow-up. |
| `src/hc_runtime/qr_payload_parser.py`, `scripts/run_qr_payload_parser.py` | QR payload parsing surface. | Public/demo users and operators. | Parsed QR payload status. | high | Yes: QR payload is a pointer or payload, not proof by itself. | QR parser tests are referenced in test taxonomy. | Malformed or spoofed payloads need clear negative-path wording. |
| `src/hc_runtime/qr_public_validator.py` | Combined QR public validator surface. | Public/demo users and operators. | QR validation result plus local record signal. | critical | Yes: QR validation is advisory and not authenticity/truth proof. | `tests/test_qr_public_validator.py` observed. | Must avoid `verified=true` style over-claims without boundary. |
| `src/hc_runtime/qr_record_bridge.py`, `scripts/run_qr_record_bridge.py` | QR-to-record bridge surface. | Public/demo users and operators. | Bridge/match status. | high | Yes: bridge matching supports evidence only. | QR bridge tests are referenced in test taxonomy. | Hash match does not prove real-world claim truth. |
| `src/hc_runtime/qr_spoof_protection.py`, `src/qr_spoof_protection` equivalent not observed | QR spoofing output. | Maintainers and demo reviewers. | Spoof warning/negative-path signal. | high | Yes: warnings are advisory signals requiring human review. | QR spoof scenario in demo runner test observed. | Use conservative wording for spoofing results. |
| `src/qr.py`, `src/qr_guard.py`, `src/qr_hardening.py`, `src/qr_security.py`, `src/qr_orchestrator_integration.py` | QR/security-adjacent runtime surfaces. | Maintainers and integrators. | QR status/security signals. | high | Yes: QR/security labels must not overstate certainty. | QR tests are referenced in test taxonomy. | Needs maintainer confirmation for public contract meaning. |
| `src/browser_validator.py`, `src/browser_bridge.py`, `src/mobile_verification_flow.py`, `src/mobile_bridge.py` | Browser/mobile demo and bridge flows. | Public users, mobile/browser demo users. | Browser/mobile verification flow output. | medium | Yes: demo/public flow outputs are advisory-only. | Browser and mobile tests are referenced in test taxonomy. | Treat as not production-ready unless separately reviewed. |
| `src/verification_output_summary.py`, `src/hc_trust/result_formatter.py`, `src/hc_trust/verification_package.py` | Public-facing summary/formatter/package surfaces. | Operators, reviewers, integrators. | Summary and formatted response. | high | Yes: summaries need explicit field meaning. | Summary/result formatter tests are referenced in test taxonomy. | Summaries compress nuance and can be misunderstood. |
| `src/system_health.py`, `src/readiness_check.py`, `scripts/hc_bot_status.py` | Status/readiness or telemetry-like output. | Maintainers and operators. | Status/report signal. | medium | Yes: readiness/status does not imply production readiness. | Status checks exist by path/name; coverage needs confirmation. | Must avoid leaking secrets or internal-only context. |
| Live public API service deployment | not observed. | not observed | not observed | not observed | Needs maintainer confirmation if added. | not observed | API code exists, but a deployed service boundary was not observed in this docs-only review. |
| Top-level `validators/` directory | not observed. | not observed | not observed | not observed | Needs maintainer confirmation if added. | not observed | Validator code is observed under `src/`, not a top-level `validators/` path. |

## 5. Output meaning table

| Output / status / field | Intended meaning | Must not be interpreted as | Human review requirement | Notes |
|---|---|---|---|---|
| `valid` | The checked input met the local validator or parser rule being applied. | Legal truth, identity finality, certification, or guaranteed correctness. | Required for consequential use. | Scope depends on the specific validator. |
| `invalid` | The checked input failed a local validator or parser rule. | Final fraud finding, legal judgment, or complete forensic conclusion. | Required before escalation or external claim. | May reflect malformed input, missing evidence, or unsupported shape. |
| `verified` | A bounded local check or response may have matched expected evidence. | Real-world truth, identity finality, certification, or production assurance. | Required. | Prefer field-specific explanation over broad use. |
| `unverified` | A bounded local check did not establish the expected match or support. | Proof that a real-world claim is false. | Required. | Absence of local verification is not full-world disproof. |
| `advisory_only` | Output is guidance/evidence for review. | Enforcement, approval, merge authority, or certification. | Always required. | Expected value is `true` for public-safe advisory outputs. |
| `public_safe` | Output is intended to avoid private or sensitive internal context. | A guarantee that no sensitive material exists in every caller context. | Required for publication decisions. | Public-safe outputs must avoid secrets, private paths, tokens, and internal-only context. |
| `truth_guarantee` | Whether the output claims truth authority. | A hidden legal or factual guarantee when `false`. | Always required. | Expected value is `false`. |
| `human_review_required` | Human maintainer or authorized reviewer must make the final decision. | Optional review for consequential interpretation. | Always required. | Expected value is `true`. |
| `warnings` | Advisory concerns, ambiguity, or negative-path signals. | Definitive legal or forensic findings. | Required before public claims. | Warnings should be explicit and understandable. |
| `missing_evidence` | Required or expected evidence was not observed locally. | Proof that evidence does not exist anywhere. | Required. | Indicates a local evidence gap. |
| `conflicting_evidence` | Observed evidence appears inconsistent under local rules. | Final dispute resolution or fraud determination. | Required. | Needs reviewer evaluation and context. |
| `record_id` | Identifier or reference for an HC:// record or fixture. | Proof of identity, authorship, or real-world truth. | Required for consequential use. | Demo IDs must remain visibly separate from real records. |
| `hash` / `digest` | Content matching or integrity check against bytes or canonicalized data. | Proof that the underlying real-world claim is true. | Required. | Hash match proves content matching only. |
| `QR payload` | Encoded pointer or payload for lookup/bridge/validation. | Proof of authenticity, signature validity, identity, or truth by itself. | Required. | QR validation must treat QR as a pointer or payload. |
| `witness` | Supporting evidence about an observed review, actor, or event. | Final authority or certification. | Required. | Witness meaning depends on source and validation context. |
| `timestamp` | Time-related evidence or recorded time field. | Complete chronology proof or legal time attestation. | Required. | Timestamp source and signing context matter. |
| `provenance` | Evidence chain or origin/context summary. | Complete real-world truth guarantee. | Required. | Provenance supports review; it does not replace it. |
| `audit summary` | Compressed view of checks, records, or review trail. | Full audit, certification, or dispute resolution. | Required. | Summaries may omit details and should link to evidence where possible. |
| `status` / `readiness` | Operational or local check state. | Production readiness or security guarantee. | Required. | Readiness wording must stay conservative. |

## 6. Public API / CLI findings

Public-facing surfaces that appear trust-critical include public validator outputs, API response contracts, verification route outputs, SDK/public response shapes, CLI verification summaries, QR public validator results, QR record bridge status, and verification package summaries. These surfaces can directly influence how users understand HC:// evidence and therefore need strict boundary language.

Demo-only surfaces include the public validator demo runner, demo fixtures, static viewer, public demo documentation, QR spoof fixture scenario, and browser/mobile demo flows when they are presented as examples. These outputs should remain visually and textually separated from real records and must not imply production readiness.

Advisory/report-only surfaces include local scripts, package viewers, output formatters, status reports, readiness reports, public-safe telemetry-like status outputs, and project-control documentation. They may produce useful evidence for maintainers, but they do not approve, certify, merge, or establish truth.

Outputs most likely to be misunderstood include `valid`, `verified`, hash/digest matches, QR payload matches, `record_id`, provenance summaries, audit summaries, witness fields, timestamps, and readiness/status labels. Each should be paired with boundary language when exposed publicly.

Areas needing maintainer confirmation before promotion include stable public API contract status, CLI output contract status, public explorer maturity, QR validation contract status, browser/mobile demo status, public-safe telemetry scope, and any transition from demo/advisory output to enforcement or production use.

The test taxonomy shows observed coverage for public response contracts, CLI behavior, QR parsing/validation/bridge behavior, demo runner behavior, static viewer/explorer behavior, browser/mobile flows, result formatting, SDK response, verification output summary, and package validation. It does not by itself prove complete public contract coverage, and maintainers should confirm coverage before treating any surface as stable.

## 7. Recommended HC public-surface rules

- Public outputs must include or preserve boundary language when they may be interpreted as verification.
- CLI, API, QR, and demo outputs must not claim truth, identity finality, certification, or production readiness.
- Demo fixtures must be clearly separated from real records.
- QR validation must treat QR as a pointer or payload, not as proof by itself.
- Hash/digest output proves content matching only, not real-world truth.
- Witness, timestamp, and provenance output is supporting evidence, not final authority.
- Public validator responses should be deterministic and test-covered.
- Public-safe outputs must avoid leaking secrets, private paths, tokens, or internal-only context.
- Any promotion from demo/advisory to enforcement or production use requires a separate PR, tests, and human review.

## 8. Ideal vs current practical state

### Ideal

- Stable public API contract.
- Explicit CLI output contract.
- Deterministic public validator behavior.
- QR validation boundary clearly documented.
- Demo outputs visually and textually separated from real verification.
- Public response fields mapped to trust meaning.
- Negative-path tests for spoofing, missing evidence, conflicting evidence, invalid hashes, and invalid signatures.

### Current practical next step

- Document observed public surfaces first.
- Do not change code or CLI/API behavior in this PR.
- Propose small follow-up PRs for missing boundary labels, docs, or tests.

## 9. Real-world analogy

An SSL/TLS browser lock indicates certificate and channel validation, not that the website’s claims are true. Banks and e-devlet-style public services show transaction receipts and audit logs, but final disputes still require authorized review.

C2PA metadata, W3C Verifiable Credentials, and OpenTimestamps provide evidence layers, not automatic truth about every real-world claim. HC-TRUST-LAYER public outputs should follow the same boundary: evidence first, human final review.

## 10. Follow-up items

- 4-3b optional: add or tighten public API response boundary documentation in a separate PR.
- 4-3c optional: add CLI output contract tests if missing.
- 4-3d optional: add QR/demo boundary labels if missing.
- 4-4: generated/canonical artifact ownership review.
- 4-5: demo/example boundary review.

These follow-ups should remain small, scoped, evidence-preserving, and human-reviewed. They should not modify protected paths unless explicitly authorized, and they should not add approval, merge, comment, label, reviewer-request, close, or autonomous governance authority.
