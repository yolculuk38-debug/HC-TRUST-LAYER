# HC:// Security Baseline Checklist v1

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

This checklist supports review of the HC:// Runtime Security Baseline v1. It is documentation only and does not modify runtime code, schemas, validators, signing logic, federation logic, workflows, policy files, GitHub Actions, or canonical records.

Use this checklist with `docs/security/runtime-security-baseline-v1.md` when reviewing security posture, documentation changes, runtime-facing guidance, and production readiness discussions.

## Checklist

| Control | Purpose | Validation method | Review frequency | Escalation path |
| --- | --- | --- | --- | --- |
| Advisory response contract | Preserve `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, stable response fields, and an always-present `warnings` list. | Review runtime docs, response contract references, and applicable runtime contract tests when response behavior is touched. | Every runtime-facing documentation or response-shape change. | Runtime owners and security reviewers. |
| Human final authority | Ensure advisory output does not become autonomous final authority. | Confirm human-supervised validation remains visible for disputed, degraded, replay-risk, spoof-risk, abuse, and incident outcomes. | Every trust-kernel-impacting review and every production readiness review. | Governance reviewers, trust-kernel reviewers, and maintainers. |
| Canonical record immutability | Prevent incident response, persistence, or runtime guidance from mutating canonical records. | Check that docs do not describe canonical record edits as remediation and that protected canonical paths are not modified. | Every security baseline update and every incident recovery proposal. | Canonical record boundary reviewers and maintainers. |
| Signature validation continuity | Prevent bypass of repository-defined signature validation or allowed-key policy expectations. | Review signing references, verification package integrity language, and federation identity expectations for bypass or fallback claims. | Every package, federation, validator, or signing-related proposal. | Signing reviewers, security reviewers, and trust-kernel reviewers. |
| Validator integrity | Preserve validator checks and avoid undocumented validator behavior changes. | Confirm no validator files or logic are modified and that validator uncertainty routes to human-supervised validation. | Every runtime, verification, or trust-state change. | Validator maintainers, security reviewers, and trust-kernel reviewers. |
| Audit trail preservation | Keep accepted, rejected, replayed, stale, degraded, conflicting, and incident states traceable. | Review audit language for warning preservation, provenance continuity, and no silent fallback or evidence deletion. | Every persistence, incident, federation, or verification package review. | Audit maintainers, security reviewers, and runtime owners. |
| Secret boundary control | Keep secrets, credentials, private signing material, `.env` contents, and private infrastructure data out of public surfaces. | Search changed docs/examples for raw secret-like material and confirm placeholder-only examples. | Every documentation, example, fixture, log, screenshot, and runtime-output review. | Security reviewers and responsible operators. |
| Abuse protection posture | Keep abuse signals advisory unless operator/infrastructure enforcement is separately reviewed. | Confirm rate-limit and abuse-control language does not imply request denial, quarantine, trust-kernel enforcement, or production guarantees. | Every abuse, QR spoof, replay-risk, and rate-limit guidance update. | Security reviewers, runtime owners, and operations maintainers. |
| Rate limiting boundary | Separate public-safe `rate_limit_recommended` style warnings from infrastructure throttling controls. | Verify that Redis, database, JWT, Vault, WAF, queue, CAPTCHA, or hosting-provider controls are not described as implemented unless repository evidence exists. | Every rate-limit or operational security update. | Security reviewers and operations maintainers. |
| Persistence audit control | Preserve advisory persistence wording, warning visibility, redaction, and write/read/re-verify traceability without unsupported durability claims. | Review persistence docs for public-safe serialization, no hidden fallback, and no unapproved database or Redis dependency. | Every persistence or storage proposal. | Runtime owners, audit maintainers, and security reviewers. |
| Verification package integrity | Preserve manifest-first integrity checks, digest coverage, signature checks, revision chain consistency, witness traceability, and metadata completeness. | Review package docs and examples for traceability, canonical ordering, witness references, replay controls, and non-verified failure states. | Every verification package format, export, import, or validation update. | Verification package reviewers, signing reviewers, and trust-kernel reviewers. |
| Federation advisory model | Ensure federation peers remain advisory and do not override local validation state, canonical records, or human final authority. | Review peer identity, signature, replay, freshness, stale propagation, witness spoofing, and partition language. | Every federation-related documentation or implementation proposal. | Federation reviewers, signing reviewers, security reviewers, and trust-kernel reviewers. |
| Production readiness boundary | Avoid unsupported production readiness, forensic certainty, complete automation, or truth guarantee claims. | Confirm readiness language requires evidence, operational review, incident handling, rollback or recovery planning, and human-supervised validation. | Every release, deployment, hardening, and readiness review. | Governance reviewers, security reviewers, runtime owners, and maintainers. |
| Incident evidence preservation | Preserve incident evidence while redacting secrets and avoiding emergency mutation of protected surfaces. | Confirm incident guidance identifies affected boundaries, retains audit context, documents uncertainty, and avoids shortcut changes. | Every incident, recovery, rollback, or emergency-freeze review. | Security reviewers, governance reviewers, runtime owners, and affected domain maintainers. |
| Operational environment separation | Separate local review, test or staging, and operator-managed deployment configuration. | Confirm examples use placeholders and do not include real credentials, secret scopes, infrastructure paths, or environment dumps. | Every operations, deployment, configuration, or runbook update. | Operations maintainers and security reviewers. |
| Documentation-only scope control | Ensure baseline changes remain non-behavioral unless explicit approval expands scope. | Check changed files for docs-only paths and confirm no protected paths, workflows, policy files, schemas, validators, signing logic, federation logic, or runtime code are modified. | Every security baseline PR. | Maintainers, governance reviewers, and affected domain reviewers. |

## Review Notes

- This checklist is an advisory review aid and does not create autonomous enforcement.
- Any trust-kernel-impacting change requires explicit human-supervised validation before merge.
- Any future implementation of runtime hardening, secret management, rate limiting, persistence, federation controls, validators, signing behavior, schemas, policy evaluation, workflows, or canonical record behavior must be proposed separately.
