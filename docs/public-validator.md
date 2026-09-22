# HC:// legacy public proof inspector

`src/public_validator.py` inspects the basic shape of exported declarations and
reports declared conflicts or failures. It does not verify file bytes, content
hashes, witness signatures, provenance, revision integrity, signer identity or
trust passports. Non-empty signature strings are not signature evidence.

The current result is `INVALID` for malformed inputs or declared failures and
`REVIEW_REQUIRED` otherwise. `verified`, `trusted`, `signature_verified`,
`witnesses_verified` and `content_hash_checked` remain false. Historical decision
constants remain importable, but this inspector does not emit `VERIFIED` or
`PARTIAL`. The supported verification level is null; any input level is retained
only under unverified `source_claims`.

`build_exported_proof` preserves declared levels/passports under `source_claims`
and leaves `content_hash_valid` null because it has not hashed any content.
The offline and browser wrappers preserve the inspector's unverified result;
offline capability describes local execution, not proof authenticity.

All these results are advisory, require human review, and carry
`truth_guarantee=false`. Retained caller declarations are not redacted:
`public_safe=false` requires a separate disclosure review before publication.

This legacy top-level module is separate from the canonical-record runtime and
the `hc-trust verify-package` file-integrity command. Future stronger results
require implemented, separately reviewed evidence verification; a caller flag
cannot enable them.
