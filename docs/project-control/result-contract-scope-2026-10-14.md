# Local verification result contract — report before implementation

Status: proposed bounded B3 result contract; report-only checkpoint  
Baseline: main after B2 implementation PR #1255, merge `77696dbd1c375f18d5f56d3c2592e559c8ccbc88`

## Finding

B3 asks the local verification-package result to separate package integrity,
authentication, identity/trust, time, and policy outcomes. The current result
has one `status` and one `verified` boolean. In
`src/hc_trust/verification_package.py`, `status` is derived from local evidence:
missing or conflicting evidence yields `INVALID`; warnings yield
`REVIEW_REQUIRED`; otherwise the package is `VERIFIED`. An empty file list
would reach the review-required fallback, but the v1 manifest schema rejects
empty lists as invalid first. The CLI in `src/hc_trust/cli.py` returns exit
code 0 only for that `VERIFIED` result.

The sample package demonstrates why the machine-readable dimensions should be
explicit. It returns `status: VERIFIED`, `verified: true`, and
`human_review_required: false`. Its issuer and timestamp files each have
`status: PRESENT`, while `identity_verified` and `external_verified` remain
false. The verifier checks the issuer document's shape and digest, checks the
timestamp claim's syntax and subject digest, and checks witness-document shape
and subject binding. It does not verify a signature, establish issuer or
witness authority, authenticate an external clock, or evaluate policy. The
result includes false booleans for some of these operations, but it has no
separate status for authentication, identity/trust, time, or policy.

Current documentation already limits `VERIFIED`, proof `PRESENT`/`MATCH`, and
`human_review_required: false` to local package-integrity work. This report
records a result-contract clarity gap; the observed implementation does not
turn those proof files into authenticated identity, time, or policy decisions.

## Proposed bounded contract

Add an explicitly versioned, additive result section, for example
`result_contract_version: HC-LOCAL-VERIFICATION-RESULT-V1` and a
`result_dimensions` object with independent statuses:

| Dimension | Proposed status | Meaning in this verifier |
| --- | --- | --- |
| `integrity` | Existing `VERIFIED`, `INVALID`, or `REVIEW_REQUIRED` | Local manifest, inventory, proof-file and SHA-256 checks only. |
| `authentication` | `NOT_PERFORMED` | No signature or other cryptographic authentication is performed. |
| `identity_trust` | `NOT_ESTABLISHED` | Issuer and witness identifiers are parsed declarations, not trusted identities. |
| `time` | `NOT_AUTHENTICATED` | A timestamp claim may be parsed and locally bound to a digest, but no external time authority is checked. |
| `policy` | `NOT_EVALUATED` | This package verifier accepts no policy input and makes no policy decision. |

The existing top-level `status` and `verified` fields should remain compatible
aliases for the integrity dimension, with no aggregate trust status. Keep the
CLI's current exit-code rule scoped to local package integrity. Keep proof
`PRESENT`, file `MATCH`, and existing checked/present booleans as local evidence
descriptions; none may promote another result dimension. Preserve
`advisory_only: true`, `public_safe: true`, and `truth_guarantee: false`.

Clarify `human_review_required` as applying to the local integrity result, and
include `human_final_authority: true` in the versioned result so a successful
integrity check cannot be read as removing human authority for consequential
interpretation. The human-authority field is a boundary statement, not a
policy or trust decision.

The JSON output and `--summary` output should both show the version and the
five dimensions. The summary should describe `VERIFIED` as local package
integrity and display unsupported dimensions as their explicit non-success
statuses. No dimension should be inferred from proof-file presence.

## Scope and compatibility

This slice changes only the local verification-package result construction,
its CLI summary, focused tests, and package documentation. Keep the v1 manifest
schema and its proof shapes unchanged. Preserve the current top-level keys and
exit codes; the new result dimensions are additive. Inventory showed the
production call path is the package verifier and its CLI, with the remaining
direct references in tests.

Do not implement signatures, key or identity registries, authenticated time,
policy evaluation, federation, a general trust score, or mappings from the
flat derived-package schema and viewer fixtures. Those remain separate C1-C4
and broader audit work. Do not describe local proof parsing or digest matching
as authentication.

## Acceptance

- A versioned result contract exposes independent integrity,
  authentication, identity/trust, time, and policy statuses.
- Valid issuer, timestamp, and witness proof files can report local `PRESENT`
  or `MATCH` evidence without changing authentication, identity/trust, or time
  to a success state.
- Integrity mismatch and review-required cases map only to the integrity
  dimension; unsupported dimensions remain explicit and non-successful.
- Existing `status`, `verified`, `human_review_required`, JSON output keys,
  and CLI exit behavior retain documented compatibility.
- The human-authority boundary is visible in JSON and human-readable output.
- Focused tests cover proof absent/present/malformed/mismatching cases and both
  CLI formats; the full suite, schema/example guard, installed-wheel gate, and
  current-head review pass before merge.

This document does not implement the result contract or claim that external
authentication, identity, time, or policy checks exist.
