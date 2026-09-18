# External audit follow-up — 2026-09-18

## Investigation and bounded implementation plan

The supplied audit reviewed `2b7d5cbaf70ef8b07c3c0a30da5a7a1ec0130974`.
This comparison starts from `477f9f15eea5a6a0c6fb8641d58e069a570f27a1`.
Merged PR history and executable source take precedence over stale shift notes.

| Audit item | Current evidence | Status / next acceptance gap |
| --- | --- | --- |
| P0-1 fabricated API schema/hash success | #1229; `tests/runtime/test_p0_1_fail_closed_verification.py` | Core containment merged. Preserve negative-path tests. |
| P0-2 inconsistent canonicalization | #1230, #1232; `hc_trust/canonicalization.py`, `tests/test_json_canonicalization.py` | Core versioned JCS / strict JSON merged. Audit-wide browser/second-language interoperability acceptance is not established by Python tests alone. |
| P0-3 schema/runtime mismatch | #1231; `hc_trust/verification.py`, installed schema data in `pyproject.toml` | Shared format-checked validator merged. `.github/workflows/validate.yml` still calls plain `jsonschema.validate`; align CI with the shared validator in a separate bounded follow-up. |
| P0-4 unsupported cryptographic claims | #1233 (`bb275a6b7163e2453d6c126efb075aaa50d0e14f`); QR inspector and checksum relabeling | QR containment merged; non-QR inventory remains open. This slice addresses only certificate-shaped claims. |
| P1 duplicate canonical IDs | `hc_runtime/canonical_record_loader.py` uses `setdefault` | Still open: reject ambiguous IDs instead of silently selecting the first record. |
| Packaging/release | Schema data files and wheel regression work in #1231 | Partial. Audit requirements for clean installed artifacts, release provenance, metadata and supported-platform evidence are not all closed by schema packaging. |
| Operations and product roadmap | Original audit sections B–D | Not certified complete by this comparison. Persistence, access controls, standard signatures/key lifecycle, external integrations and pilot acceptance require separate scoped evidence. |

## Reproduced certificate finding

At the comparison base, `verify_certificate` returns `trusted=true` for a
caller-created dictionary containing an arbitrary issuer, `verified=true`, and
`decision=VERIFIED`. `verify_certificate_chain({"chain_integrity": true})`
also returns `trusted=true`, even without a certificate or chain version.
Non-object chain input raises `AttributeError`. The certificate builder copies
upstream verification claims without authenticating their source.

Repository search found direct callers only in the three matching test files;
`portable_package_v2.py` transports a certificate-chain dictionary but does not
call these verifiers. Existing tests assert the unsupported success behavior.
External consumers are unknown, so this is an intentional fail-closed output
contract correction, retaining function names and version identifiers.

## Scope and expected impact

Change `certificate_verifier.py`, `certificate_chain.py`, and
`verification_certificate.py`, with direct regression tests. Separate shape
checks from trust: self-declared flags, signatures, or issuers cannot produce
verified/trusted results. Preserve SDK declarations only as explicitly
unverified source claims. An unchecked chain link is unknown, not proven intact
or broken. Keep advisory and false-truth-guarantee boundaries explicit. Public-safe output
must not retain arbitrary caller data.

No cryptographic implementation, key authority, schema, canonical record,
workflow permission or production-readiness claim is added. This protected
verification change is justified by the reproduced false-trust result and the
maintainer's request to continue the remaining audit work.

## Validation and review gate

Exercise forged declarations, builder-to-verifier composition, missing fields,
malformed JSON-shaped values and unchanged negative risk reporting. Run the
full repository suite and canonical, terminology and documentation guards.
Require current-head CI and matching Codex review before merge. Record actual
results below; implementation alone is not merge completion.

## Initial local validation results (before Codex P2 follow-up)

- CPython 3.14.7, pinned `requirements.txt` dependencies.
- Direct certificate regression tests: **50 passed**.
- Full repository suite: **1195 passed** in 61.73 seconds.
- Canonical artifact and terminology guards: passed.
- Documentation drift guard: passed with two pre-existing README warnings
  (lines 17 and 106); this slice does not change those claims.
- `git diff --check`: passed.
- GitHub checks, exact-head review and merge status are recorded on the PR;
  these local results do not assert that those later gates have completed.

## Codex P2 follow-up: disclosure markers

Review of `68adcacf62c3b2b0e423b3a7eb4518990e6148a3` identified that the
certificate and chain builders retained arbitrary caller data while marking it
public-safe. A synthetic-sensitive-data regression reproduced the problem.
Both builders now return `public_safe=false`. The certificate inspector also
returns false because it preserves caller-supplied risk-flag text. This does not
redact the data: callers must perform a separate disclosure review before
publication. The chain inspector alone keeps `public_safe=true` because its
output contains only fixed diagnostics and computed shape booleans; a regression
checks that caller text is not echoed. No disclosure permission is inferred from
advisory-only status or an input's own `public_safe` declaration.

Follow-up validation: 52 focused certificate tests and 1197 full-suite tests
passed on CPython 3.14.7 (full suite: 57.99 seconds). Canonical artifact,
terminology, documentation drift guards and whitespace checks passed; the same
two pre-existing README warnings remain. The synthetic disclosure regression
failed before the correction and passed afterward.
