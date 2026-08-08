# Independent External Audit P0 Status

Status: advisory implementation checkpoint as of 2026-08-08.

This note tracks the current independent external audit separately from the
historical #905-#923 outside-review sequence. Repository files, merged GitHub
history, checks, and human review decisions remain the source of truth.

## P0 closeout table

| Finding | Repository status | Evidence | Remaining gate |
| --- | --- | --- | --- |
| P0-1: API surfaces could report fabricated schema/hash success | Completed by #1229 | Merge commit `cfbc8ebdd3542ab6076d8d2e4fe1ac3737d12ddd`; fail-closed runtime regressions | Do not reintroduce success from marker presence, parse success, or unchecked evidence. |
| P0-2: JSON canonicalization was inconsistent | Completed by #1230 | Merge commit `a58bbe09a47aada72e649c970943a598a91d772f`; versioned RFC 8785 JCS and strict JSON boundaries | Follow-up compatibility paths must use the versioned primitive or remain explicitly non-canonical. |
| P0-3: record schema and runtime validation disagreed | Implemented in the current change; not merged | One Draft 2020-12 schema, declared schema/hash-profile versions, required `content`, strict RFC 3339 checking, a shared validator, installed-wheel schema packaging, and separate schema/hash/record-binding results | Current-head checks, Codex/reviewer evidence, and human merge decision. |
| P0-4: cryptographic-strength names exceed implemented guarantees | Not started | Audit finding only; no repository mutation is claimed by this note | After P0-3 closes, inventory the named surfaces and contain, rename, or relabel them in one bounded slice unless real cryptographic evidence exists. |

## P0-3 protected-path scope

The current change intentionally touches `schema/`, `records/pending/`, the
shared validator, and advisory runtime verification. The scope is limited to
one executable record contract and the minimum metadata required to bind
checked-in canonical records to that contract and the existing
`hc-content-sha256-v2` hash profile.

The three changed pending records retain their exact `content` and
`content_hash` values. Only `schema_version=hc-record-v1` and
`content_hash_profile=hc-content-sha256-v2` are added. Generated artifacts,
workflows, policy, signing, federation, and canonical content are not changed.

## Required P0-3 merge evidence

Before merge, reviewers must confirm all of the following on the current head:

- the full repository test suite passes;
- canonical artifact, terminology, and documentation-drift guards pass;
- the built wheel contains and can load the single canonical record schema;
- all checked-in canonical JSON records pass the shared schema and content-hash
  checks;
- changed-record review confirms no `content` or `content_hash` mutation;
- GitHub checks and review comments are current-head clean, or an explicit
  exact-head human exception is recorded.

## Boundaries and next slice

Schema conformance and digest equality are integrity evidence only. They do not
prove content truth, author identity, witness authority, signature validity,
timestamp authority, consensus, provenance authenticity, or governance
approval. Outputs remain `advisory_only=true`, `public_safe=true`, and
`truth_guarantee=false`; human final authority is unchanged.

Do not open P0-4 implementation work while the P0-3 PR is open. After human
review and merge, begin P0-4 with a repository-backed symbol and public-surface
inventory; avoid adding cryptography as part of a naming correction.
