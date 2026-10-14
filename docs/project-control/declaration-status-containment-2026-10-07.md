# Legacy declaration-to-status containment

## Finding and scope before implementation

Audit A4 remains open after proof and certificate containment. The top-level
legacy `evidence_engine` scores caller booleans as verified evidence and its
`trust_orchestrator` passes that score to policy. `consensus_rules` labels a
majority of unauthenticated witness IDs trusted, and `consensus_status_integration`
invents a successful hash check from that majority. `verification_status_engine`
promotes raw flags/counts to verified provenance/federation levels.
`trust_passport` and its status integration expose the same unsupported claims.
The revision-status adapter can also promote a local hash chain to locked
provenance. None of these entry points authenticates the declarations it receives.

Contain these connected legacy entry points in one slice. Preserve input claims
under an explicitly unverified `source_claims` container, keep agreement counts
as diagnostics, and emit no verified/trusted/hash-checked/signature/identity
authority from declarations. Shape-valid declarations require review; malformed
inputs and explicit invalid/conflict results remain invalid. Effective evidence
and trust scores stay zero so the orchestrator cannot authorize through them.
Retain enum constants for import compatibility, not as achievable proof states.

Files in scope: the nine named top-level modules, their existing tests, one
cross-entry-point negative regression module, this report, the active audit
ledger, and the existing validation workflow's focused test list. Do not alter
packaged `hc_trust` content/file integrity checks, HMAC verification, revision
hash calculation, canonical records, stored digests, schema or signature design.

Validate forged complete declarations, caller overrides, malformed scalar/list
fields, duplicate witness identities, hash conflicts, all output branches and
the full suite. Review all direct callers and preserve raw inputs without
mutating them. Current-head CI and matching review remain required before merge.

## Limits

This closes only the connected declaration/status/passport slice. Media evidence
review, cryptographic identity naming, legacy pseudo-signature/snapshot surfaces,
the generic SDK formatter and other A4 inventory entries remain separate. The
result is an advisory review boundary, not implementation of real signatures,
identity ownership, independent witnesses, locked provenance or federation.

## October 12 validation checkpoint

The connected slice passed 76 focused tests and 1383 full-suite tests on CPython
3.14.7; one upstream Starlette TestClient warning remains. Negative cases include
100 self-declared witnesses, complete success flags, caller-supplied verified
passport overrides, malformed flags/counts, input preservation and nested claim
copy independence. Existing QR and graph passport tests now expect review;
their real local hash checks and invalid-input behavior remain intact.
Canonical, terminology, docs and whitespace guards passed (two existing README
wording warnings). The existing runtime CI job runs all 13 affected test modules.

The code deliberately changes legacy output semantics: effective evidence/trust
scores are zero, verification levels remain unverified, passport summary booleans
are false, and raw summaries/consensus inputs are under `source_claims`. Consumers
must treat those retained claims as unverified input. A consensus count describes
agreement among declared IDs, not independent or authenticated witnesses.
This is intentional containment, not a backwards-compatible trust promotion.

## October 14 final local validation

Rebased onto the actual #1249 merge
`fa17a118f5647712a5beee3e36a8e08d2706edd7` with FastAPI 0.142.2.
All 1388 full-suite tests and 79 focused declaration/status/integration tests
passed on CPython 3.14.7, with the same upstream warning. The additional witness
enum regressions reject malformed containers before the legacy shape validator;
raw consensus results are retained only inside `source_claims`. All repository
guards and whitespace checks passed with the two existing README warnings.
This 24-file slice awaits matching current-head CI and Codex review.
