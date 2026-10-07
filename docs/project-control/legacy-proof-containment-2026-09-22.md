# Legacy exported-proof claim containment

## Scope and evidence

Maintainer authorization: complete the remaining independent audit in bounded
slices. This is A4 claim containment, not new signature implementation.

`exported_proof.py` marks a caller-supplied digest valid without hashing bytes.
`public_validator.py` counts non-empty signature/provenance strings and emits
`VERIFIED` with two witnesses. `offline_verifier.py` demonstrates this with fake
hash/signature strings; `verifier_entry.py` and `sdk_response.py` carry the result.
The relevant tests currently assert this unsupported success.

Change the builder and inspector to identify declarations explicitly and keep
hash, signature, witness, identity and trust verification false/not-performed.
Preserve legacy imports and decision constants for compatibility; the inspector
may return only `INVALID` or `REVIEW_REQUIRED` until actual verification exists.
Keep input conflict/failure signals conservative. Reject malformed nested shapes
without exceptions. Raw retained declarations require `public_safe=false`.
Offline/browser wrappers must preserve these boundaries. The SDK formatter is
not itself an evidence verifier; its arbitrary-input behavior is outside this
slice, but the actual inspector-to-SDK path must not promote declarations.

Scope: the builder, legacy inspector, offline/browser metadata and demonstration,
their tests, and `docs/public-validator.md`. The existing runtime/API CI job
also runs the legacy proof regressions so this boundary stays covered. No
schema, canonical record, crypto, workflow permission, signing authority or
production deployment changes.

Validation: regress forged signatures, caller-controlled success flags, malformed
revision/witness/passport shapes, unverified builder declarations and propagation
through offline/browser/SDK paths; run the full suite and repository guards.
Require current-head review and CI after the prior PR closes.

## Historical local validation

23 focused tests and 1243 full-suite tests passed on CPython 3.14.7 before the
unrelated CI runtime-selector update. After rebasing that update, all 23 focused
tests passed again. Terminology and documentation guards passed with two existing
README warnings. These counts describe the September candidate, not the new head.

## October 7 continuation

The patch is based on the actual #1244 merge. The inspector now uses
`content_hash_valid=null` because it never computes a digest, including when
the input declares failure. Five non-object input regressions complement the
malformed nested-input and forged-success cases. Runtime/API CI runs all five
legacy proof/SDK test modules. No new permissions or production guarantees are
introduced.

Current validation on CPython 3.14.7: 29 focused tests and 1266 full-suite tests
passed. The full suite reports one upstream Starlette TestClient deprecation
warning. Canonical, terminology and documentation guards passed; the docs guard
retains two pre-existing README warnings. Current-head GitHub CI and review are
still required before merge.

Codex review of `09f63674bf76` found two P2 issues: nested source claims were
dropped in the builder-to-inspector path, and malformed source-claims containers
were ignored. Preserve the nested unverified object, validate its known fields,
and reject non-object containers. Regressions cover offline/browser propagation,
extension declaration preservation, legacy claims and malformed containers.

After both review fixes: 38 focused tests and 1275 full-suite tests passed on
CPython 3.14.7, with the same one upstream warning. Repository guards and
`git diff --check` passed. Matching review and CI must run on the new commit.
