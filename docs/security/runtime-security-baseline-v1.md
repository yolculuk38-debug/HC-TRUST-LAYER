# HC:// Runtime Security Baseline v1

Metadata:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- Runtime behavior change: none.
- Schema mutation: none.
- Validator logic mutation: none.
- Signing logic mutation: none.
- Federation logic mutation: none.
- Workflow mutation: none.
- Canonical artifact mutation: none.
- Human final authority: required.

## Purpose

This document is the first consolidated security baseline for HC:// Runtime review in HC-TRUST-LAYER. It summarizes existing repository guidance for runtime hardening, abuse protection, response contracts, persistence audit controls, verification package integrity, rate limiting controls, secret boundary controls, federation security expectations, and production readiness requirements.

This baseline is documentation only. It does not implement runtime controls, mutate canonical records, change schemas, modify validators, alter signing logic, change federation behavior, or update workflows.

## Security Principles

1. Preserve advisory runtime semantics: HC:// Runtime output remains advisory-only, public-safe, traceable, and not a truth guarantee.
2. Keep human-supervised validation visible for unresolved, degraded, replay-risk, spoof-risk, disputed, or trust-kernel-impacting outcomes.
3. Protect canonical artifact boundaries, including schema definitions, deterministic serialization assumptions, hash-linked artifacts, record identity, and provenance continuity.
4. Preserve audit trail continuity across normal, degraded, replay-warning, malformed-input, abuse-warning, and recovery states.
5. Treat secrets, private signing material, credentials, deployment configuration, and infrastructure details as non-public operator-controlled material.
6. Keep federation peers advisory; remote validator or witness claims must not override local validation state or human final authority.
7. Avoid unsupported production readiness, forensic certainty, autonomous governance finality, or cryptographic guarantee language.

## HC:// Security Invariants

These invariants define the minimum security expectations for HC:// Runtime review:

| Invariant | Baseline expectation | Review implication |
| --- | --- | --- |
| Canonical records are immutable. | Runtime, persistence, federation, and incident response documentation must not describe canonical record mutation as remediation. | Escalate to canonical record boundary reviewers if any proposal could alter record identity or provenance continuity. |
| Signature validation cannot be bypassed. | Signing checks and allowed-key policy remain required where repository-defined verification or package integrity depends on them. | Escalate to signing and trust-kernel reviewers for any signature-validation exception, fallback, or shortcut. |
| Audit chains must remain preserved. | Accepted, rejected, stale, replayed, degraded, conflicting, and incident-related states must remain traceable in the audit trail. | Escalate to audit maintainers when a proposal could suppress, overwrite, or silently discard audit evidence. |
| Federation nodes are advisory only. | Federation peers may contribute evidence or warnings, but they do not override local validator state, canonical records, or human-supervised validation. | Escalate to federation reviewers for peer identity, freshness, replay, partition, or witness propagation uncertainty. |
| Human final authority is required. | Trust-kernel-impacting uncertainty, disputed evidence, degraded runtime behavior, incident recovery, and production readiness decisions require human-supervised validation. | Escalate to maintainers and governance reviewers before treating advisory output as final. |
| Verification packages must remain traceable. | Package manifests, signatures, witness material, revision chains, hashes, and metadata must remain linked to provenance and integrity checks. | Escalate to verification package and signing reviewers if package files, ordering, digest coverage, or witness references are unclear. |
| Public responses must stay public-safe. | Public runtime responses preserve advisory flags, stable warning behavior, redaction expectations, and no raw secret-bearing values. | Escalate to runtime and security reviewers if response shape changes or private values appear. |
| Operational controls do not expand the trust kernel by default. | Rate limiting, WAF rules, queue controls, secret managers, monitoring, deployment controls, and incident actions are operator/infrastructure controls unless separately reviewed. | Escalate before representing infrastructure enforcement as validator, signing, schema, policy, or canonical behavior. |

## Trust Boundaries

HC:// Runtime security review should distinguish the following boundaries:

- **Public verification boundary**: public-safe response fields, warnings, verification map references, provenance summaries, and audit trail pointers.
- **Trust kernel boundary**: validators, signing semantics, schema contracts, policy interpretation, canonical records, and deterministic serialization assumptions.
- **Canonical artifact boundary**: hash-linked artifacts, record identity, package manifests, revision chains, and canonical provenance continuity.
- **Operator infrastructure boundary**: reverse proxies, rate limiting, deployment configuration, monitoring, secret custody, storage services, and recovery procedures.
- **Human authority boundary**: reviewer decisions, escalation records, incident acceptance, production readiness assessment, and final interpretation of disputed trust state.

Cross-boundary movement should be explicit, documented, and reviewable. Documentation-only guidance must not imply a runtime behavior change across these boundaries.

## Canonical Artifact Protection

Canonical artifact protection requires:

- no mutation of canonical records to hide errors, recover from incidents, or simplify deployment;
- stable references between verification packages, manifests, digests, witness evidence, revision chains, and metadata;
- clear separation between public verification data and private operator configuration;
- preservation of provenance continuity when records, packages, or audit events are referenced;
- explicit reviewer escalation for any proposed change touching canonical record identity, deterministic serialization, or hash-linked artifact assumptions.

## Validator Integrity

Validator integrity requires:

- no bypass of repository-defined validation checks or signing expectations;
- no validator logic mutation as part of this baseline;
- preservation of advisory warnings for malformed input, replay risk, continuity risk, spoof risk, abuse indicators, and degraded runtime state;
- human-supervised validation for validator compromise concerns, unexpected identity transitions, unexplained trust-state changes, and disputed validation outcomes;
- clear distinction between validator evidence and federation, witness, or operator-provided advisory context.

## Audit Integrity

Audit integrity requires:

- an always-visible audit trail for security-relevant events and limitations;
- retention of warnings for replay, degraded runtime, continuity, spoof, abuse, malformed input, stale federation data, and incident recovery;
- no silent fallback, overwriting, or deletion of evidence that could affect trust interpretation;
- public-safe redaction of secret-like values in logs, warnings, examples, telemetry-like payloads, and shared diagnostics;
- incident recovery notes that document impact, reviewer decisions, limitations, and provenance continuity.

## Federation Trust Model

Federation is advisory in this baseline. Federation peers may provide evidence, witness propagation, freshness signals, or conflict context, but they must not override local validation state, canonical records, signature validation, or human final authority.

Federation security review should confirm:

- peer identity evidence is explicit and verifiable;
- signatures cover complete federation messages, including replay-protection metadata;
- stale, late, conflicting, replayed, rejected, or partitioned messages remain preserved as audit trail context;
- witness claims remain separately traceable and are not merged into untraceable aggregate claims;
- trust score or reputation changes do not bypass validator checks, signing expectations, or reviewer oversight.

## Human Authority Model

Human final authority is required for:

- trust-kernel-impacting uncertainty;
- production readiness decisions;
- incident classification, recovery acceptance, and public impact language;
- disputed validation outcomes, witness conflicts, stale federation evidence, or replay-risk interpretation;
- any proposed change to schemas, validators, signing logic, federation behavior, policy evaluator behavior, workflows, canonical records, or protected governance controls.

Agent output and runtime output are advisory unless validated through repository-defined checks and reviewer oversight.

## Incident Handling

Incident handling should preserve evidence, avoid canonical mutation, and route decisions to human-supervised validation.

Minimum incident handling expectations:

1. Identify the affected boundary: runtime response, persistence, audit trail, verification package, secret exposure, federation, validator integrity, signing, policy, or canonical record surface.
2. Preserve public-safe audit trail context, including warnings, timestamps where available, affected record or package references, and reviewer notes.
3. Redact raw secrets, tokens, private keys, credentials, and private infrastructure details from public-facing material.
4. Avoid emergency shortcuts that modify schemas, validators, signing logic, federation logic, security workflows, policy files, GitHub Actions, or canonical records without explicit approval.
5. Document recovery limits, unresolved uncertainty, rollback evidence where applicable, and human-supervised validation before returning to normal operation.

## Operational Security

Operational security controls belong primarily to operator/infrastructure layers unless a separate approved implementation changes that boundary.

Baseline controls include:

- maintaining advisory response contracts with `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and an always-present `warnings` list;
- treating rate limiting and abuse controls as operator-side mitigation recommendations unless separately implemented and reviewed;
- keeping secrets, signing material, `.env` contents, deployment credentials, and private infrastructure details out of repository-facing docs, tests, logs, examples, screenshots, and public runtime output;
- separating local review, test or staging, and operator-managed deployment environments;
- reviewing persistence or storage proposals for traceability, redaction, warning preservation, and absence of unsupported durability claims;
- preserving public-safe degraded-state, replay-risk, QR spoof-risk, malformed-input, and abuse-signal visibility.

## Consolidated Control Summary

| Area | Baseline summary | Required review posture |
| --- | --- | --- |
| Runtime Hardening | Maintain advisory/public-safe response semantics and visible warnings without adding unreviewed enforcement dependencies. | Runtime and security review for response-shape or control changes. |
| Abuse Protection | Surface abuse indicators as advisory warnings and preserve human-supervised validation for mitigation decisions. | Runtime, security, and operations review for repeated abuse patterns. |
| Response Contracts | Preserve stable public response fields, redaction expectations, and no truth guarantee language. | Runtime contract review before changing public response shape. |
| Persistence Audit Controls | Preserve write/read/re-verify traceability, explicit warnings, and no unsupported production durability claims. | Audit and runtime review for persistence proposals. |
| Verification Package Integrity | Preserve manifest-first checks, digest coverage, signatures, revision chain consistency, witness traceability, and metadata completeness. | Verification package, signing, and trust-kernel review for package changes. |
| Rate Limiting Controls | Treat rate limiting as advisory warning or operator/infrastructure enforcement outside the trust kernel unless separately approved. | Security and operations review before enforcement claims. |
| Secret Boundary Controls | Keep secret material out of public docs, examples, responses, logs, telemetry-like payloads, and canonical surfaces. | Security review for exposure or custody changes. |
| Federation Security Expectations | Treat federation nodes as advisory, signed, freshness-checked evidence sources that do not override local state. | Federation, signing, and trust-kernel review for federation changes. |
| Production Readiness Requirements | Require explicit human-supervised validation, operational evidence, incident planning, recovery evidence, and no unsupported readiness claims. | Governance, security, runtime, and operations review. |

## Future Security Roadmap

Future security work should remain small, scoped, and separately reviewed. Candidate follow-up areas include:

- expanded public-safe incident response templates;
- additional documentation for operator-managed rate limiting and abuse triage;
- verification package integrity review examples for mobile-readable flows;
- stronger documentation links between audit trail preservation and trust-kernel review routing;
- clearer federation freshness and replay review examples;
- secret exposure tabletop guidance using placeholder-only examples;
- production readiness evidence templates that preserve advisory language and human-supervised validation.

Any future implementation work must be proposed separately and must not be inferred from this baseline.

## Related Repository References

- `docs/security/runtime-hardening-gap-report.md`
- `docs/security/operator-abuse-protection-advisory.md`
- `docs/runtime/public-response-contract.md`
- `docs/runtime/advisory-rate-limit-warning-contract.md`
- `docs/runtime/persistence-roundtrip-audit.md`
- `docs/security/persistence-risk-checklist.md`
- `docs/security/rate-limiting-abuse-control.md`
- `docs/security/secret-boundary-architecture.md`
- `docs/security/federation-risk-checklist.md`
- `docs/security/production-risk-checklist.md`
- `docs/verification-package-spec.md`
- `docs/verification-package-validation.md`
- `docs/execution-audit-trail.md`
- `docs/canonical-record-boundary.md`
- `docs/verification-map.md`
- `docs/protocol-graph-index.md`
