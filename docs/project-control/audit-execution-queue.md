# Independent audit execution queue

Maintainer instruction (2026-09-18): complete the remaining supplied audit items
in order, with scoped implementation, tests, current-head review and CI.
This authorizes the necessary bounded code/workflow fixes, not new bot authority
or fabricated external acceptance. One PR at a time. Source baseline:
`479ea3cb8d4b74dcf70d7d44ef4aab2c0a7ed384` (#1242).

## Acceptance ledger

| Item | Evidence / outstanding work | Status |
| --- | --- | --- |
| A1 API/QR fail-closed | #1229 regressions; preserve no-evidence rejection | Core merged |
| A2 canonicalization | #1230/#1232; add Python/browser-compatible cross-language golden vectors | Partial |
| A3 single validation path | #1231 core; CI still bypasses shared strict/format validation | Active first slice |
| A4 unsupported trust claims | #1233 QR, #1242 certificates; remaining inventory and experimental isolation | Partial |
| A5 installed wheel/release | Add outside-checkout install smoke gate, exact tested-artifact handoff | Pending |
| B1 narrow product promise | Lead with local evidence-package integrity and limits | Pending |
| B2 evidence-package format | Inspect/version manifest, algorithms, file metadata, extension/proof boundaries | Pending |
| B3 result contract | Separate integrity, authentication, identity/trust, time, policy | Pending |
| B4 developer experience | Actual-file example, install, JSON/human output, exit codes and SDK | Partial |
| C1 standard signature | Standard library integration, key IDs, versioned envelope, explicit trust roots | Pending design/implementation |
| C2 key lifecycle | Expiry/revocation/rotation/unknown signer; no invented real identity authority | Pending |
| C3 external time evidence | Separate local time and authenticated time; replay policy | Pending |
| C4 external provenance | Standards-backed adapters and offline proof verification, not field-presence success | Pending |
| D1 persistent runtime | Duplicate IDs, bounded state, restart/multi-worker, durable audit, backup/restore | Pending |
| D2 operational security | Access/tenant boundaries, size/rate limits, safe telemetry/logs, operational runbook | Pending |
| D3 three real pilots | Prepare repeatable scenarios; real external participants and observed results required | External evidence required |
| D4 independent review | Threat model, abuse/parser/release review; two independent maintainers required | External reviewers required |

No readiness percentage or all-audit-complete claim follows from test counts.
Real pilot participation, reviewer independence, external identity/trust-root
ownership and production operations cannot be fabricated by repository edits.
Prepare reviewable artifacts and report any concrete access dependency.

## Slice 1: shared record validation in CI

Finding: `.github/workflows/validate.yml` uses `json.load` and bare
`jsonschema.validate`, unlike `hc_trust.verification.validate_record` which
rejects duplicate keys and applies the shared RFC 3339 format checker.

Scope: add `hc-trust validate-records` calling the existing shared validator,
replace only the inline CI schema step, run its negative contract tests in CI,
and document invocation/exit codes. Preserve separate content-hash validation,
workflow permissions and all existing checks. Empty input must fail instead of
reporting successful validation. Tests must cover bad timestamps, duplicate keys,
missing schema fields, valid records and excluded generated artifacts.

Invocation from a checkout: `PYTHONPATH=src python -m hc_trust.cli validate-records records`.
After installation: `hc-trust validate-records /path/to/records`.
Exit 0 means at least one selected canonical record passed schema/format checks
and none failed. Exit 1 means a failure or an empty selection. This command does
not check content hashes, signatures or truth; the separate hash step remains.

Slice 1 local validation: 40 focused schema/CLI tests and 1204 full-suite tests
passed on CPython 3.14.7; three checked-in canonical JSON records passed the new
command. Canonical, terminology and documentation guards passed (two existing
README warnings). No workflow permission or signing behavior changed.
