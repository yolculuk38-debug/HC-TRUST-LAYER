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
| A3 single validation path | #1231 core; #1243 merged strict CI validation and runtime artifact selection | Core and CI merged; public lookup selection follow-up remains |
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
| D1 persistent runtime | Duplicate IDs/resolved-path containment active; bounded state, restart/multi-worker, durable audit, backup/restore remain | Active collision slice; persistence pending |
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

Codex P2 follow-up: the shared record-file selector now includes documented
legacy `records/archive/` alongside `records/archived/`; existing evidence is not
moved. Regressions cover a bad legacy record mixed with a valid pending record,
duplicate keys and a valid legacy-only selection. This also aligns the existing
hash CLI selection with the documented legacy canonical path.

A second Codex P2 identified an inherited substring selector that could skip a
canonical ID containing INDEX/MANIFEST/CACHE/EXPORT/GENERATED. Replaced it with
precise reserved artifact basenames/directories shared with `src/validator.py`.
Regression cases ensure those words cannot hide invalid canonical records.

September 22 review follow-up scope: restore established delimiter-suffix
artifacts such as `HC-EXAMPLE-2026-0001-index.json` and `..._export.json` in the
shared selector. Reserve complete `-`/`_` suffixes for index, manifest, cache,
export and generated artifacts, plus their standalone basenames. Do not restore
substring skipping: `HC-INDEX-2026-0001.json` remains a validation target.
Validate schema CLI, hash CLI and legacy single-file behavior against invalid
and record-shaped artifacts, and retain the earlier bypass regressions.

September 22 validation: 38 focused CLI/loader tests and 1229 full-suite tests
passed on CPython 3.14.7. Canonical, terminology and documentation guards passed
with the same two existing README warnings. This addresses review comment
4070043375; current-head CI and a matching fresh review remain the merge gate.

The next review (4070109210) identifies the still-broad runtime file selector.
Move the prepared shared-predicate alignment into this PR so the CI and runtime
agree on artifact words, reserved suffixes and legacy archive records. Keep the
duplicate-ID and resolved-path containment changes in the separate second slice.
Add runtime lookup regressions for ordinary IDs containing artifact words and
legacy archive records; preserve original suffix-exclusion tests.

Runtime alignment validation: 44 focused tests and 1235 full-suite tests passed
on CPython 3.14.7. The suffix exclusions and interior-word bypass regressions
remain passing. Duplicate rejection is still a separate pending change.

## Slice 2: ambiguous canonical record IDs

The runtime loader uses `setdefault`, so two records declaring the same ID select
one silently. The separate Public Validator lookup already reports duplicates.
Contain the runtime loader gap with an explicit duplicate marker and public
`duplicate_record_id` status; schema/hash checks must remain not-performed.
Clear collision state on explicit refresh. Cover identical and different content,
three collisions, different directories, ignored artifacts, refresh and the API.
The loader's path containment must use resolved paths so a symlink cannot import
records outside the approved root. This is a local lookup boundary correction;
no identity, schema, record contents or federation authority changes.

The runtime loader also checks the documented legacy `records/archive/` spelling,
so a duplicate across legacy/current directories cannot escape collision checks.
Both the lexical path and resolved target must pass artifact exclusions.

Slice 2 pre-rebase validation: 48 focused loader/fail-closed tests and 1214 full
suite tests passed on the first CI-slice head. Two dependency deprecation warnings
come from the API test client. Re-run after incorporating the CI legacy-path fix.

Slice 2 final validation on CI head `bf87138791686691193bf511c9aad5630cfc3cfa`:
65 focused tests and 1224 full-suite tests passed (61.89 seconds), with two
upstream TestClient deprecation warnings. Canonical, terminology and docs guards
passed with the two existing README warnings. Runtime selection now shares the
precise artifact predicate introduced by the CI fix.

September 22 continuation: the dependent slice now includes the restored
artifact-suffix compatibility from #1243. Preserve the original runtime
`-index.json` / `-export.json` regression while adding precise-name coverage.
Rebase onto the actual #1243 merge before opening its separate PR.

The shared artifact predicate and legacy archive selection moved into #1243
following review 4070109210. This slice retains collision detection and resolved
path containment; the original runtime suffix tests remain unchanged.

September 22 validation: 1240 full-suite tests passed after the artifact-suffix
repair, and 87 focused CLI/runtime/fail-closed tests passed after including the
six new runtime-selector regressions from #1243. Two upstream TestClient
deprecation warnings remain. The final PR will be based on the actual main merge
and requires current-head CI/review; no merge or all-audit closure is claimed.

## September 22 sequencing checkpoint

#1243 merged as `d4406efdb66a9271795df796b75d2e8e79402292` after a clean
review of head `11e6f87c41e67ba312180a5a84cceb78f12cd42b`, all 26 checks and
four resolved findings. Slice 2 is rebased onto that actual merge.
The legacy exported-proof containment candidate is saved separately on
`fix/legacy-proof-claims-20260922`; it must follow this PR, based on its eventual
main merge. Its scope is `legacy-proof-containment-2026-09-22.md` on that branch.

Additional bounded A3 follow-up: `public_validator_lookup.py` still uses flat
directory globs and broad filename exclusions. Align it with the precise shared
selector, documented legacy archive and recursive canonical paths, updating
checked-path fixtures deliberately. Test duplicate IDs hidden in nested/legacy
paths. This is separate from the runtime collision slice; do not mark A3 fully
closed until that lookup path is aligned.

Post-rebase validation on `d4406efdb66a9271795df796b75d2e8e79402292`:
1246 full-suite tests passed on CPython 3.14.7, with two upstream TestClient
deprecation warnings. Canonical/terminology/docs guards passed with the two
existing README warnings. Four files differ from the merged base.
