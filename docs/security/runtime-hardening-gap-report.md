# Runtime Security Hardening Gap Report

Metadata:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- Runtime behavior change: public-safe redaction of secret-like runtime output only.
- Schema mutation: none.
- Workflow mutation: none.
- Human final authority: required for prioritization, acceptance, and any security-sensitive follow-up.

## Purpose

This report converts broad runtime security concerns into repository-specific, evidence-based findings for HC-TRUST-LAYER and HC:// review planning.

It is advisory-only documentation. It does not implement Redis, JWT, Vault, ECC, RSA, rate limiting, signing changes, validator changes, workflow changes, schema changes, or autonomous blocking behavior.

## Scope

In scope:

- public-safe runtime contract posture
- secret handling review questions
- rate-limit and abuse-protection recommendations
- runtime contract risk notes
- future-option tracking for security hardening ideas

Out of scope:

- runtime verification behavior changes
- canonical record mutation
- schema contract mutation
- signing or trust anchor changes
- federation behavior changes
- policy evaluator behavior changes
- workflow or governance changes

## Verified repo findings

The following findings are based on repository evidence available in the HC-TRUST-LAYER tree:

| Finding | Repo evidence | Risk note | Advisory status |
|---|---|---|---|
| Runtime responses expose an advisory/public-safe contract. | `src/hc_runtime/contracts/responses.py` sets `advisory_only=True`, `public_safe=True`, and `truth_guarantee=False` in the shared response builder. | Good baseline, but every new runtime surface should preserve the same public-safe contract. | Verified in repo. |
| Runtime app copy avoids production-readiness and truth-authority claims. | `src/hc_runtime/app.py` describes the reference runtime as advisory-only, not production-ready, and not a truth guarantee. | Public operator copy should continue to avoid unsupported production-security guarantees. | Verified in repo. |
| Runtime verification routes keep human-supervised validation visible. | `src/hc_runtime/routes/verify.py` returns advisory payloads and warning text that routes unresolved interpretation to human-supervised validation. | This should remain visible when future hardening controls are added. | Verified in repo. |
| Runtime tests check public-safe advisory contract fields and redaction expectations. | `tests/runtime/` includes runtime contract, replay/continuity, and secret-like input redaction tests that assert `advisory_only`, `public_safe`, `truth_guarantee`, stable response keys, warning redaction, and no raw secret-like material in telemetry-like payload serialization. | Existing tests reduce accidental drift but do not replace human review. | Verified in repo. |
| Redis, Vault, JWT, ECC, and RSA are not implemented as runtime hardening controls in the current HC:// reference runtime. | Repository search found no runtime implementation references for these options. | Treat these as future options only unless a later PR adds implementation evidence and review coverage. | Future option only. |

## Advisory-only risk checklist

Use this checklist during review of runtime security hardening proposals. It is advisory_only=true and public_safe=true.

- [ ] Does the proposal preserve `advisory_only=true`, `public_safe=true`, and `truth_guarantee=false` in public runtime responses?
- [ ] Does the proposal avoid production-readiness, forensic certainty, or autonomous governance finality claims?
- [ ] Does the proposal keep human-supervised validation visible for unresolved, disputed, degraded, replay-risk, or spoof-risk outcomes?
- [ ] Does the proposal avoid changing schemas, validators, signing logic, federation behavior, policy evaluator behavior, protected governance files, or workflows unless explicitly approved?
- [ ] Does the proposal preserve audit trail continuity and provenance context for runtime warnings?
- [ ] Does the proposal distinguish verified repository evidence from future recommendations?
- [ ] Does the proposal remain reversible and small enough for safe review and rollback?
- [ ] Does the proposal avoid adding secrets, tokens, credentials, private keys, or environment-specific values?

## Secret handling review checklist

This checklist is for human reviewers and maintainers. It does not add automated secret scanning, secret storage, autonomous blocking behavior, or signing/security policy changes.

- [ ] No private keys, access tokens, API keys, session cookies, credentials, or secret-like literals are added to repository files.
- [ ] Runtime responses preserve `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and an always-present `warnings` field.
- [ ] Runtime response serialization preserves deterministic public keys while redacting or omitting raw secret-like input.
- [ ] Runtime warnings and history responses do not echo raw secret-bearing input.
- [ ] Logs, telemetry-like payloads, queues, and audit-visible events redact or omit secret-like input before public exposure.
- [ ] Public examples use placeholders such as `<redacted-token>`, `<redacted-api-key>`, or `<redacted-private-key>` instead of credential-shaped sample values.
- [ ] Configuration guidance separates public-safe documentation from deployment-only secret material.
- [ ] Any future secret-management implementation requires explicit human-supervised validation before merge.

### Public-safe example guidance

Use placeholder-only examples in runtime docs and tests intended for public review:

```text
hc://example-record hash:example <redacted-token>
api_key=<redacted-api-key>
private_key=<redacted-private-key>
```

Do not include credential-shaped sample values in documentation, warnings, telemetry-like payload examples, or public audit trail examples.

## Rate-limit and abuse-protection recommendations

No rate-limit or abuse-protection runtime behavior is implemented by this report.

Future PRs may consider the following options after reviewer approval:

1. Add public-safe request volume guidance for HC:// runtime operators.
2. Add advisory abuse-warning states for repeated spoof, replay, malformed-input, or degraded-runtime patterns.
3. Add bounded diagnostics for suspected abuse without exposing raw user input.
4. Add operator-facing recommendation text for ingress-layer rate limiting outside the trust kernel.
5. Evaluate Redis-backed counters only as a future option, not as an assumed dependency.
6. Preserve human final authority for any action that would block, quarantine, or alter trust interpretation.

## Future options, not current implementation

The following items are explicitly future options unless a later repository change implements them with tests and human-supervised validation:

| Future option | Current status | Boundary note |
|---|---|---|
| Redis-backed rate-limit counters | Future option only. | Must not become a hidden dependency or alter runtime responses without review. |
| Vault-backed secret storage | Future option only. | Must not introduce deployment secrets or trust-anchor changes without review. |
| JWT-based operator/session authentication | Future option only. | Must not imply validator authority, production identity, or governance finality by itself. |
| ECC signing hardening | Future option only. | Any signing change touches high-sensitivity trust-anchor semantics and requires explicit review. |
| RSA signing hardening | Future option only. | Any signing change touches high-sensitivity trust-anchor semantics and requires explicit review. |

## Human authority and review boundary

This report is not an enforcement mechanism. It is an advisory planning artifact for HC:// runtime security review.

Human reviewers retain final authority over risk acceptance, prioritization, implementation readiness, and whether any future hardening proposal is eligible to merge.
