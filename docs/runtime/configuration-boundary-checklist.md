# Runtime Configuration Boundary Checklist

Metadata:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- Runtime behavior change: none.
- Schema mutation: none.
- Workflow mutation: none.
- Storage dependency: none; no secret storage implementation, no Redis implementation, no database dependency, and no Vault implementation.
- Authentication dependency: none; no JWT implementation.
- Signing mutation: none.
- Human final authority: required for operator configuration review.

## Purpose

This checklist helps HC:// operators and reviewers keep runtime configuration separate from public verification data, signing material, and operational secrets. It supports the secret boundary architecture in `docs/security/secret-boundary-architecture.md` and remains documentation only.

## Public-safe configuration checklist

Before sharing runtime output, examples, logs, or operator notes, verify:

- [ ] Public verification data is limited to documented public response fields, public-safe warnings, provenance summaries, audit trail references, and verification map references.
- [ ] Runtime configuration data is summarized without exposing raw environment variables, tenant secrets, private hostnames, internal paths, credentials, or signing custody details.
- [ ] Signing material is absent from public output, examples, fixtures, docs, screenshots, and telemetry-like payloads.
- [ ] Operational secrets such as API tokens, bearer tokens, session cookies, webhook secrets, database passwords, cloud credentials, Vault tokens, and JWT secrets are absent.
- [ ] Examples use placeholders such as `<redacted-token>`, `<redacted-private-key>`, `<operator-config-name>`, and `<public-record-id>`.
- [ ] Public output remains `advisory_only=true`, `public_safe=true`, and `truth_guarantee=false`.
- [ ] Human-supervised validation remains visible for interpretation, exposure response, and operator-side remediation.

## Configuration trust zone review

| Trust zone | Public example allowed? | Review requirement |
| --- | --- | --- |
| Public verification zone | Yes, when deterministic and public-safe. | Confirm examples match `docs/runtime/public-response-contract.md`. |
| Runtime configuration zone | Limited summaries only. | Confirm no raw environment dumps, secrets, or private routing details are exposed. |
| Signing custody zone | No private material. | Confirm only public-safe key identifiers or signature status references are used when already documented. |
| Operational secret zone | No. | Confirm no credential-like strings, tokens, cookies, or secret-manager handles appear. |
| Human review zone | Limited summaries only. | Confirm reviewer notes do not expose private operator context. |

## Public-safe examples

Allowed example:

```json
{
  "record_id": "<public-record-id>",
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "warnings": [
    "configuration_boundary_review: runtime configuration summarized without exposing secrets."
  ],
  "operator_config": "<operator-config-name>",
  "secret_reference": "<redacted-token>"
}
```

Disallowed example shape:

```text
Do not include raw environment variables, bearer tokens, private keys, API keys, session cookies, webhook secrets, database passwords, Vault tokens, JWT secrets, or signing custody material.
```

The allowed example is a documentation fixture only. It does not define a new runtime response schema and does not require a new `operator_config` field.

## No secret leakage examples

Use these deterministic placeholder patterns in documentation tests and examples:

- `<redacted-token>` for operational secret values;
- `<redacted-private-key>` for signing material;
- `<operator-config-name>` for public-safe configuration labels;
- `<public-record-id>` for public verification references.

Do not use realistic token prefixes, live hostnames, copied `.env` lines, private key block markers, session cookie values, or cloud credential formats.

## Operator configuration checklist

- [ ] Keep local, staging, and operator-managed deployment configuration separated.
- [ ] Keep signing material in a separate custody path from runtime configuration.
- [ ] Keep operational secrets outside the repository and outside public examples.
- [ ] Confirm diagnostic bundles redact secret-like input before sharing.
- [ ] Confirm public verification outputs do not reveal hidden infrastructure assumptions.
- [ ] Confirm operator-side controls are documented outside HC:// runtime behavior.
- [ ] Confirm any exposure response is reviewed through human-supervised validation.
- [ ] Confirm no Vault implementation, no Redis implementation, no JWT implementation, no database dependency, and no secret storage implementation is introduced.

## Deterministic documentation references

- `docs/security/secret-boundary-architecture.md`
- `docs/runtime/public-response-contract.md`
- `docs/runtime/runtime-contract-risk-notes.md`
- `docs/security/runtime-hardening-gap-report.md`
- `docs/security/persistence-risk-checklist.md`
- `docs/security/rate-limiting-abuse-control.md`
- `docs/signing-architecture.md`

These references are stable documentation anchors for review. They do not modify schemas, validators, signing logic, federation behavior, policy evaluator behavior, workflows, or runtime behavior.

## Non-goals

This checklist does not implement secret managers, credentials, `.env` files (.env files), Vault, Redis, JWT, databases, infrastructure dependencies, secret storage, runtime behavior, validators, signing logic, workflows, or schema changes.
