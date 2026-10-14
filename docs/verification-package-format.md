# HC-TRUST-LAYER Verification Package Format Alignment Notes

## Status

These notes distinguish the implemented local directory manifest from the separate package formats under review. The local contract is an advisory integrity check and does not establish a canonical HC:// package standard.

The broader package formats remain experimental and under review. The local CLI manifest adds no HC:// trust guarantees.

## Current Package Shapes

### Flat v1 schema package

The current v1 schema draft describes a flat top-level verification package object. It requires fields such as `package_version`, `package_id`, `record_id`, `record_hash`, `content_hash`, `verification_state`, `canonical_record_path`, `source_repository`, `source_commit`, `generated_at`, `provenance`, `audit`, `witnesses`, `signatures`, `verification_policy`, and `warnings`.

This shape treats provenance, audit trail context, witnesses, signatures, policy, and warnings as top-level package sections rather than as a nested manifest/container.

### Local CLI directory manifest v1

The `verify-package` CLI consumes a directory with a root `manifest.json` using the `HC-LOCAL-VERIFICATION-MANIFEST-V1` schema. It requires non-empty `package_id` and `record_id`, a non-empty `files` list, and canonical lowercase SHA-256 entries. Optional parsed issuer, timestamp, and witness references are limited to their documented fields. Every regular file other than the root manifest must be covered by `files[]` or one of those proof references. Duplicate JSON keys, duplicate file paths, unknown fields, unlisted files, symlinks, and special filesystem objects are rejected. Empty directories are ignored.

File roles (`payload`, `proof`, `metadata`, `documentation`, or `opaque`) are descriptive. Unparsed payload bytes remain opaque even when their digest matches. Namespaced `extensions` values are also opaque and never participate in verification. Signature verification, signer identity, external time authority, witness authority, and legal truth remain outside this local contract.

This CLI manifest is a local filesystem inventory format. It is separate from the flat v1 package schema and the viewer-oriented fixtures below.

### Manifest/container package concept

Repository documentation also describes verification packages as portable derived artifacts that may bundle provenance, audit trail references, witness context, integrity references, warnings, and external review context. This points toward a possible manifest/container architecture, but no canonical container model is established here.

### MVP-1 example fixture shape

The MVP-1 verification package fixtures use a viewer-oriented shape. They include fields such as `package_id`, `content_hash`, `provenance_summary`, `provenance_timeline`, `validator_reviews`, `replay_indicators`, `dispute_indicators`, `trust_result`, `trust_confidence`, `audit_snapshot`, `generated_at`, and `human_review_required`.

These fixtures are useful for mobile-readable verification flow review, but they do not currently match the flat v1 schema package requirements.

### External/portable package variants

External and portable package references use compact bundle-style structures for review outside a live runtime. These variants emphasize provenance, revision references, witness references, integrity hash references, and federation source references. They remain experimental derived artifacts and do not replace canonical records.

## Current Known Mismatches

- **Hash format mismatch:** the flat v1 schema uses bare 64-character lowercase hex hashes, while MVP-1 fixtures use `sha256:<hex>` values.
- **Trust result vocabulary mismatch:** the flat v1 schema uses `verification_state` values such as `pending`, `verified`, `rejected`, `archived`, `disputed`, and `revoked`; MVP-1 fixtures use `trust_result` values such as `PASS`, `WARNING`, and `FAIL`.
- **Replay/dispute indicator shape mismatch:** MVP-1 fixtures use nested `replay_indicators` and `dispute_indicators`; the flat v1 package shape has optional flat status fields such as `dispute_status` and does not define equivalent nested indicator requirements.
- **`package_version` mismatch:** `package_version` is required in the flat v1 schema and external package schema, while MVP-1 fixtures currently omit it.
- **Architecture mismatch:** the flat v1 schema validates one flat top-level object, while the manifest/container concept suggests a package envelope with nested requirements for grouped evidence sections.

## Current Validation Boundaries

- The flat v1 schema validates a flat top-level package structure only; it is not the local CLI directory-manifest schema.
- The local CLI schema validates its versioned directory manifest and the implementation additionally enforces file inventory and filesystem-boundary rules.
- The MVP-1 validator checks required-field presence for the viewer fixture shape; it does not establish a canonical package schema.
- Viewer warnings are advisory review signals, not autonomous trust-kernel decisions.
- The exporter skeleton is not production signing. It creates derived verification package skeletons and marks signatures as not implemented.

## Standardization Decision Points

Before schema or validator changes, HC-TRUST-LAYER maintainers should decide:

1. whether the canonical package model is a flat v1 object, a manifest/container package, or a layered model that separates portable manifest data from viewer fixtures;
2. whether canonical hash fields use bare 64-character hex values, `sha256:<hex>` values, or explicitly typed hash objects;
3. whether MVP-1 fixtures are viewer fixtures only or canonical package examples;
4. which fields are required inside provenance, audit trail, witness, signature, warning, replay, and dispute sections;
5. whether trust result vocabulary should map to verification result states, viewer states, policy evaluator outcomes, or a separate package-level status vocabulary;
6. how to preserve canonical record boundaries while allowing portable HC:// verification context to move between systems.

## Safety Notes

- Do not claim production readiness for current verification package formats.
- Do not claim cryptographic guarantees from current package examples, viewer warnings, or exporter skeleton output.
- Do not treat verification packages as canonical records.
- Treat all current package formats as experimental and under human-supervised validation review.
- The local directory manifest does not replace canonical records, the flat package schema, or viewer fixtures.
