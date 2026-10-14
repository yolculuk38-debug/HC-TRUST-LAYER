# Verification-package format contract — report before implementation

## Finding

B2 asks the repository to inspect and version its evidence-package manifest,
hash algorithms, file metadata, extension points and proof boundaries. The
repository currently contains several deliberately separate package shapes,
but the local hash-core manifest is not governed by an explicit schema.

`schema/verification-package-v1.schema.json` describes a flat derived-package
object with `package_version: "1.0"`, record hashes, lifecycle state, provenance,
audit, witness and signature arrays. The local directory CLI instead consumes
`manifest.json` with `schema_version`, `files[]`, and optional path/hash
references for issuer, timestamp and witness JSON. Viewer-oriented MVP fixtures
have another shape and result vocabulary. `docs/verification-package-format.md`
already records these as distinct experimental formats and lists unresolved
standardization choices; the v2 document is architectural concepts, not an
implemented schema.

## Repository evidence

- `src/hc_trust/verification_package.py` requires a parseable JSON object and a
  `files` list, but does not require or validate `package_id`, `record_id` or
  `schema_version`. The supplied version is copied into the result when present;
  missing IDs are returned as `null`.
- The manifest loader uses the standard JSON decoder, which silently keeps the
  last occurrence of a duplicate object key. Duplicate `files`, `path` or digest
  keys can therefore change the parsed package meaning without an error.
- `SUPPORTED_DIGEST_ALGORITHMS` contains only SHA-256. File entries may use
  `sha256`, or `digest`/`hash` with an optional `algorithm`. The direct `sha256`
  member returns before the algorithm label is checked. Other top-level and
  file-entry properties are ignored by the verifier.
- Repeated file paths are processed as separate entries; there is no duplicate
  path rejection or declared metadata interpretation.
- Optional issuer, timestamp and witness references are locally hash-checked;
  their referenced JSON receives limited structural checks. They do not
  authenticate an issuer, external time source or witness authority. The
  hash-core does not verify signatures; a signature-related field is not a
  supported verifier input.
- The sample manifest uses `verification-package-sample-v1`, the fixture
  manifest uses `verification-package-fixture-v1`, and a unit-test manifest
  uses `verification-package-v1`. These identifiers are not currently enforced
  by the parser.

Disposable temporary-package probes against the current source confirmed:

| Input variation | Observed result |
| --- | --- |
| Missing package/record IDs, unknown version, arbitrary top-level extension, `algorithm: "md5"` alongside a valid `sha256` member | `VERIFIED`; IDs are `null`; `sha256_only: true` |
| No `schema_version` | `VERIFIED`; result version is `null` |
| Same file path listed twice with the same digest | `VERIFIED`; two entries counted |
| Same `sha256` object key repeated with an invalid value first and a matching value last | `VERIFIED`; standard JSON parsing keeps the last value |

These probes show current parser behavior only; they do not establish an intended
compatibility contract.

## Proposed bounded contract

Keep the local hash-core manifest as its own format, separate from the flat v1
derived-package schema, the viewer fixtures and the future v2 concept. Give it a
unique, required v1 schema identifier and a repository-owned JSON Schema. Before
changing code, use this contract for the first implementation slice:

- Require non-empty `package_id` and `record_id`, plus the exact supported
  manifest version. Reject missing IDs and missing or unknown versions with a
  nonzero result.
- Parse the manifest and supported proof JSON with duplicate-object-key
  detection. Reject repeated keys at any object depth rather than accepting a
  last-value-wins interpretation.
- Define one canonical file digest representation. Preserve SHA-256 as the only
  supported algorithm; if an algorithm label is present, require it to agree
  with the digest representation. Reject conflicting aliases rather than
  silently choosing one.
- Define which file-entry metadata is meaningful to the verifier. Treat all
  other listed payload bytes as opaque; a matching digest does not validate
  their format or meaning.
- Reject duplicate normalized file paths. Define path normalization and
  package-boundary rules in the schema/validator contract.
- Reject unrecognized top-level and file-entry properties by default. If an
  extension point is retained, place it in one explicitly named, namespaced
  extension container and mark extension values as unverified input.
- Specify which proof kinds are parsed by the local verifier and their required
  JSON fields. Keep signature, authenticated timestamp and identity checks
  explicitly unsupported; unknown proof kinds must remain unverified and must
  not be mapped to a verified proof result. Keep the overall package status
  scoped to local integrity as B3 defines its result contract.
- Migrate only the local manifest fixtures and their tests. Keep viewer JSON and
  flat v1 package examples separate unless a later reviewed decision defines a
  mapping.

The preferred version identifier is `HC-LOCAL-VERIFICATION-MANIFEST-V1`; this
name distinguishes the directory manifest from the existing flat schema draft.
If maintainers prefer another identifier, record that decision before schema or
runtime changes.

## Out of scope

This report does not change schemas, examples, verifier behavior, generated
files or canonical records. It does not standardize the broader export package,
implement signing, prove external timestamps, establish identity or witness
authority, or change B3 result semantics. Resource limits and archive/container
handling belong to the separate operational-security and portability reviews.

## Acceptance

The implementation review should verify required identifiers, strict version
handling, duplicate-key rejection, digest-label consistency, duplicate-path
behavior, metadata and extension treatment, and each supported proof parser
with positive and negative fixtures. Documentation must state that listed
payload bytes are only integrity-checked and may remain syntactically or
semantically opaque. Compatibility impact for each existing local manifest
fixture must be explicit before merge.
