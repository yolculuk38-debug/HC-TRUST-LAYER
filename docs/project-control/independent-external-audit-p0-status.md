# Independent External Audit P0 Status

Status: advisory implementation checkpoint as of 2026-09-18.

This note tracks the current independent external audit separately from the
historical #905-#923 outside-review sequence. Repository files, merged GitHub
history, checks, and human review decisions remain the source of truth.

## P0 closeout table

| Finding | Repository status | Evidence | Remaining gate |
| --- | --- | --- | --- |
| P0-1: API surfaces could report fabricated schema/hash success | Completed by #1229 | Merge commit `cfbc8ebdd3542ab6076d8d2e4fe1ac3737d12ddd`; fail-closed runtime regressions | Do not reintroduce success from marker presence, parse success, or unchecked evidence. |
| P0-2: JSON canonicalization was inconsistent | Completed by #1230; compatibility follow-up completed by #1232 | Merge commits `a58bbe09a47aada72e649c970943a598a91d772f` and `3d2331d3e1ce756b7742b2c211a79b6ca1adef35`; versioned RFC 8785 JCS and strict JSON boundaries reused by import and QR compatibility paths | Future compatibility paths must use the versioned primitive or remain explicitly non-canonical. |
| P0-3: record schema and runtime validation disagreed | Completed by #1231 | Merge commit `e5f04028135f4c4d9e32c64bd5c86967bc6bcd5a`; one Draft 2020-12 schema, declared schema/hash-profile versions, required `content`, strict RFC 3339 checking, a shared validator, installed-wheel schema packaging, and separate schema/hash/record-binding results | Do not reintroduce a second executable record schema or bypass the shared validator. |
| P0-4: cryptographic-strength names exceed implemented guarantees | QR containment merged by #1233; certificate containment is the current bounded follow-up | Merge `bb275a6b7163e2453d6c126efb075aaa50d0e14f`; `audit-followup-2026-09-18.md` records the reproduced certificate gap and audit comparison | Current-head validation and review for the certificate slice; other non-QR inventory remains open. |

## P0-4 bounded scope

The merged #1233 change was limited to the QR claim boundary and its direct
public wording. The current certificate slice is scoped and validated in
`audit-followup-2026-09-18.md`. It does not modify schemas, canonical records, workflows, policy,
generated artifacts, federation, key management, or signing implementations.

The QR inspector no longer treats a non-empty signature-shaped value as
cryptographic evidence. The QR link generator now labels its public-field
SHA-256 value as an unkeyed advisory checksum instead of a signature. The
broader symbol inventory is recorded separately and is not silently treated as
implemented cryptography.

## QR slice acceptance evidence (merged #1233)

The QR slice required the following acceptance evidence; these checks do not
close the remaining certificate and non-QR work:

- the full repository test suite passes;
- canonical artifact, terminology, and documentation-drift guards pass;
- signature presence alone cannot produce `VERIFIED` or `trusted: true` on the
  changed QR path;
- the orchestrator bridge cannot promote the current QR inspector output to a
  trusted input;
- generated QR links use the named unkeyed checksum profile and do not emit a
  `sig` claim;
- CLI, capability, example, and QR-boundary documentation use advisory wording;
- no cryptographic primitive, authority, or truth guarantee was added;
- GitHub checks and review comments are current-head clean, or an explicit
  exact-head human exception is recorded.

## Boundaries and next slice

QR structure, URL, digest, checksum, or signature-presence checks do not prove
content truth, signer identity, key ownership, issuer authority, signature
validity, QR authenticity, provenance authenticity, or governance approval.
Outputs remain `advisory_only=true`, `public_safe=true`, and
`truth_guarantee=false`; human final authority is unchanged.

The remaining named non-QR surfaces are listed in
`p0-4-cryptographic-claim-inventory.md`. Address them only through separate,
bounded, repository-backed follow-ups after each current PR closes; avoid adding
cryptography as part of a naming correction.

The full external audit has broader acceptance criteria than these core slices.
The September comparison records remaining CI/shared-validator alignment and
cross-language evidence gaps; the core closeout table is not a claim that the
entire external audit is complete.
