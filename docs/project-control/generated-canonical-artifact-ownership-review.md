# Generated and Canonical Artifact Ownership Review

## 1. Purpose

This document is an advisory, documentation-only review of generated/canonical artifact ownership and source-of-truth boundaries in HC-TRUST-LAYER.

It supports backlog item 4-4, “generated/canonical artifact ownership review,” after the core package boundary review, test taxonomy review, and public API / CLI boundary review. It clarifies which observed paths appear to be source-of-truth records, generated outputs, canonical or reference artifacts, examples/demo fixtures, audit/evidence outputs, and paths that should not be manually edited without source, generator, and review context.

This review does not move files, rename files, regenerate artifacts, edit generated/canonical artifacts, modify schemas, modify records, change scripts, change tests, change workflows, change runtime behavior, add enforcement, or establish authority.

## 2. HC boundary

- `advisory_only=true`.
- `public_safe=true`.
- `truth_guarantee=false`.
- `human_review_required=true`.
- Generated/canonical artifacts are evidence or reproducible outputs, not autonomous truth authority.
- This review does not certify, approve, reject, enforce, regenerate, or establish truth.
- This review does not add approval, merge, comment, label, reviewer-request, assignment, close, or autonomous governance authority.
- Human maintainer review remains the final authority.

HC-TRUST-LAYER generated outputs, canonical/reference anchors, public summaries, fixtures, records, and checks must not be treated as legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, guaranteed correctness, or production readiness.

## 3. Review method

This review inspected observed repository paths by name and apparent role. It does not invent files, directories, generators, approvals, signatures, hashes, or maintainer intent. If a requested category was not observed, it is marked as `not observed`.

Observed paths and relationships reviewed:

- `generated/`.
- `canonical/`.
- `records/`.
- `schema/`.
- `docs/demo/fixtures/`.
- `docs/project-control/`.
- `scripts/check_canonical_artifacts.py`.
- scripts or tests that appear by name to produce, validate, normalize, or check generated/canonical artifacts.
- relationship to `docs/project-control/core-package-boundary-review.md`.
- relationship to `docs/project-control/test-taxonomy-review.md`.
- relationship to `docs/project-control/public-api-cli-boundary-review.md`.

The related boundary reviews already classify core package boundaries, test coverage boundaries, and public API / CLI boundaries. This document narrows the next review layer to ownership of source inputs, generated outputs, canonical/reference anchors, demo fixtures, and audit/evidence outputs.

## 4. Artifact classification table

| Path / artifact group | Observed role | Source-of-truth status | Generated or hand-authored | Trust sensitivity | Allowed mutation path | Guard/check observed | Notes |
|---|---|---|---|---|---|---|---|
| `records/pending/` | Pending record material inside the canonical record boundary used by the canonical artifact guard. | source-of-truth / audit/evidence / protected | hand-authored or source-provided; needs maintainer confirmation per record | critical | Human-reviewed record change with schema/check evidence; do not normalize, rewrite, move, delete, or regenerate silently. | `scripts/check_canonical_artifacts.py`; record and public-validator tests by name. | Guard treats this as a canonical record boundary and rejects non-canonical artifacts inside it. |
| `records/verified/` | Verified record boundary named by the canonical artifact guard. | source-of-truth / audit/evidence / protected | hand-authored or source-provided; needs maintainer confirmation | critical | Human-reviewed record/evidence change only. | `scripts/check_canonical_artifacts.py`; record validation tests by name. | Directory is observed; contents may be absent or minimal in the current tree. |
| `records/archived/` | Archived record boundary named by the canonical artifact guard. | source-of-truth / audit/evidence / protected | hand-authored or migrated historical record material; needs maintainer confirmation | critical | Human-reviewed archive/evidence change only; preserve provenance. | `scripts/check_canonical_artifacts.py`; normalizer safety tests by name. | Archived records should not be rewritten as cleanup. |
| `records/archive/` | Archive area observed under `records/`. | audit/evidence / protected | hand-authored or historical; needs maintainer confirmation | high | Human-reviewed archive/evidence change only. | Record normalization safety references in project-control docs; tests by name. | Not listed as a canonical guard directory in the observed script, but still evidence-sensitive. |
| `records/explorer_index.json` | Explorer/navigation index inside `records/`. | derived-output / non-canonical | generated or derived; needs maintainer confirmation | high | Regenerate only through documented source/generator path, or document why a manual edit is necessary. | `scripts/check_canonical_artifacts.py` skips `explorer_index.json` as non-canonical. | Should not be treated as a record source of truth. |
| `records/signatures/` | Signature-related evidence/reference material. | audit/evidence / protected | hand-authored or evidence-provided; needs maintainer confirmation | critical | Human-reviewed evidence/signature boundary change only. | Signature/witness tests and docs by name; no signing authority inferred. | Evidence-adjacent; does not establish certification authority. |
| `schema/` | Schema definitions and record-shape contracts. | source-of-truth / protected | hand-authored | critical | Separate protected-path PR with explicit justification and validation. | Schema validation tests by name. | Schema changes can alter what future generated/canonical artifacts mean. |
| `generated/audit_snapshot.json` | Generated audit snapshot. | derived-output / audit/evidence | generated; needs generator confirmation | high | Regenerate only through documented process; avoid manual edit. | Generated artifact inventory docs; canonical artifact guard skips `generated/**`. | Evidence summary, not full source record. |
| `generated/first_working_audit_snapshot.json` | Historical or generated audit snapshot. | derived-output / audit/evidence | generated; needs generator confirmation | high | Regenerate or update only with source/generator/audit note. | Canonical artifact guard skips `generated/**`. | Historical naming suggests audit evidence; maintainer confirmation needed. |
| `generated/explorer_index.json` | Generated explorer/navigation index. | derived-output / reference | generated | high | Regenerate through the documented explorer-index generator and verify output. | Generated artifact inventory names `src/generate_explorer_index.py`; canonical artifact guard skips `generated/**`. | Advisory index, not a canonical verification record. |
| `generated/first_working_explorer_index.json` | Historical generated explorer/navigation index. | derived-output / reference | generated; needs maintainer confirmation | medium to high | Regenerate or update only with documented source/generator/audit note. | Canonical artifact guard skips `generated/**`. | Historical generated reference; not source of truth by itself. |
| `generated/example_federation_package.json` | Example generated federation package. | fixture/demo / derived-output | generated example | medium to high | Update only as explicit example/demo artifact with public-safe boundary language. | Generated artifact inventory docs; canonical artifact guard skips `generated/**`. | Example package, not live federation authority. |
| `canonical/` | Top-level canonical artifact directory. | not observed | not observed | needs maintainer confirmation | If added later, require source input, generator/owner, reproducibility, and human review. | not observed as a directory; canonical artifact guard uses record subdirectories as canonical boundaries. | Do not invent canonical contents. |
| Root reference indexes such as `trust-kernel-index.json`, `verification-map.json`, `protocol-graph.json` | Machine-readable reference/navigation anchors. | canonical/reference / docs/governance / protected | hand-authored or generated/reference; needs maintainer confirmation | critical | Separate human-reviewed PR with explicit justification and checks. | Generated reference artifact index docs. | Reference anchors need reproducible provenance and careful wording. |
| `docs/demo/fixtures/` | Demo/public-validator/QR fixture material. | fixture/demo | hand-authored or generated fixture; needs maintainer confirmation per fixture | low to medium | Demo-only PRs with clear fixture labels; do not promote to records without review. | Public validator, QR parser, and fixture tests by name. | Examples are not real verification authority. |
| `docs/project-control/` | Project-control plans, inventories, ledgers, reviews, and advisory evidence docs. | docs/governance / audit/evidence | hand-authored | medium | Documentation-only PRs; preserve advisory boundaries and human final authority. | `scripts/check_docs_drift.py`; `scripts/check_terminology.py`. | Coordinates review; does not approve or establish truth. |
| `docs/project-control/generated-artifact-inventory-pass-2026-06-16.md` | Earlier generated/reference artifact inventory. | docs/governance / audit/evidence | hand-authored | medium | Update only through scoped docs review if stale. | Docs checks. | Useful prior anchor, not complete inventory. |
| `docs/project-control/generated-reference-artifact-index-2026-06-16.md` | Earlier generated/reference artifact index. | docs/governance / audit/evidence | hand-authored | medium | Update only through scoped docs review if stale. | Docs checks. | Defines traceability posture for generated/reference artifacts. |
| `exports/` | Exported or derived examples and release-support material. | derived-output / fixture/demo / needs maintainer confirmation | generated or hand-authored; unclear | high | Do not hand-edit silently; identify source/generator/consumer first. | Canonical artifact guard skips `exports/**`; export/import tests by name. | Ownership needs maintainer confirmation. |
| `hash/` | Hash references and integrity artifacts. | audit/evidence / canonical/reference | generated or hand-authored; unclear | critical | Human-reviewed evidence change with source and digest-generation evidence. | Hash and digest tests/scripts by name. | Hashes prove content matching only, not real-world truth. |
| `qr/` | QR-related verification artifacts and references. | audit/evidence / fixture/demo / canonical/reference | generated or hand-authored; unclear | high | Human-reviewed evidence/demo change with source and parsing/check evidence. | QR parser, QR guard, and QR record bridge tests by name. | QR outputs are validation aids, not final authority. |
| `scripts/check_canonical_artifacts.py` | Deterministic canonical/generated artifact boundary guard. | guard/check | hand-authored script | high | Script changes require separate implementation PR and tests; not changed here. | It is the observed guard. | Marks generated/index/export/cache artifacts as non-canonical and protects record boundaries. |
| `src/generate_explorer_index.py` | Explorer-index generator named by existing generated artifact inventory. | generator | hand-authored source code | high | Code change or regeneration must be separate from this docs-only review. | Existing inventory docs; tests/checks by name. | Generator ownership is referenced by prior docs, not revalidated by code changes here. |
| `tests/test_deterministic_export.py`, `tests/test_export_import.py`, and verification-package tests by name | Tests for deterministic export, packages, proofs, hashes, and generated/canonical-adjacent behavior. | guard/check | hand-authored tests | medium to high | Test changes require separate test/code PR. | Test taxonomy review. | Evidence of coverage, not authority. |
| `tests/test_normalize_records.py`, `tests/test_normalize_records_safety.py` | Record normalization and safety tests by name. | guard/check | hand-authored tests | high | Separate test/code PR only. | Test taxonomy review and source-inventory checkpoint docs. | Important for preventing unsafe record rewrites. |

## 5. Ownership boundary findings

Observed source-of-truth paths appear to include `records/pending/`, `records/verified/`, `records/archived/`, evidence-preserving parts of `records/archive/`, and schema contracts under `schema/`. These are protected or trust-critical and should not be rewritten, normalized, moved, deleted, or regenerated without human review and validation evidence.

Observed generated or derived paths include `generated/**`, `records/explorer_index.json`, likely some `exports/**` material, generated audit snapshots, and explorer indexes. These files should not be manually edited unless the PR explicitly documents the source input, generator or manual reason, reproducibility evidence, and review boundary.

Observed canonical/reference anchors include the record-boundary directories named by `scripts/check_canonical_artifacts.py`, root reference indexes such as `trust-kernel-index.json`, `verification-map.json`, and `protocol-graph.json`, and generated/reference indexes documented by prior project-control inventory notes. They need reproducible provenance and conservative human review before mutation.

Observed demo/fixture-only areas include `docs/demo/fixtures/**` and some generated/example package material. These examples should remain visibly separated from real records and must not be promoted into verification authority without a separate reviewed change.

Observed audit/evidence outputs include generated audit snapshots, project-control inventory/review documents, record archives, hash/QR-related evidence surfaces, and report artifacts described by existing project-control documentation. Audit summaries help review but are not substitutes for the underlying source records.

Areas needing maintainer confirmation include exact ownership for every generated file under `generated/`, whether any `exports/**`, `hash/**`, or `qr/**` file is hand-authored versus generated, whether root machine-readable reference indexes are generated or hand-authored in current practice, and the complete generator/consumer map for generated/canonical-adjacent artifacts.

Files that should not be manually edited unless the generator/source path is also reviewed include `generated/**`, `records/explorer_index.json`, `exports/**`, hash/digest outputs, QR evidence outputs, and any future `canonical/**` artifacts. Schema or validator changes should not silently alter canonical outputs or generated evidence.

Existing protection observed includes `scripts/check_canonical_artifacts.py`, which treats `records/pending`, `records/verified`, and `records/archived` as canonical record boundaries and skips generated/index/export/cache artifacts as non-canonical. The test taxonomy review also names deterministic export, verification package, hash, canonical record loading, canonical schema/hash bridge, QR, record normalization, and public-validator tests as generated/canonical-adjacent evidence.

## 6. Source vs generated distinction

- Source files define intended record, schema, policy, or validation behavior.
- Generated artifacts are outputs of a documented process and need source/generator traceability.
- Canonical artifacts are reference anchors and need reproducible provenance.
- Demo fixtures are examples, not real verification authority.
- Audit summaries are evidence summaries, not full source records.
- Hash or digest artifacts prove content matching only, not real-world truth.
- Generated/canonical artifacts need generation/audit trace, not manual narrative.
- Public summaries or explorer indexes can help humans inspect evidence, but they do not replace records, schemas, or human review.

## 7. Recommended HC artifact rules

- Do not manually edit generated artifacts unless the PR explicitly documents why.
- Changes to canonical artifacts require source input, generation method, and check evidence.
- Demo fixtures must be visibly separated from real records.
- Records must not be normalized, rewritten, deleted, moved, or regenerated without human review.
- Schema or validator changes must not silently alter canonical outputs.
- Generated/canonical artifact checks should remain deterministic.
- Any future enforcement promotion requires a separate PR, tests, and human review.
- Artifact ownership must distinguish “who authored the source” from “which script produced the output.”
- Hash, QR, explorer, export, and audit-summary files should remain traceable to source records or documented fixture inputs.
- Project-control documentation may describe ownership boundaries, but it must not create autonomous approval or truth authority.

## 8. Ideal vs current practical state

### Ideal

- Every generated/canonical artifact maps to a source input.
- Every artifact has a documented generator or hand-authored owner.
- Canonical artifacts have reproducible hashes.
- Generated outputs are never manually edited silently.
- Demo fixtures are separate from real records.
- Artifact checks are deterministic and CI-visible.
- Audit/evidence outputs point back to source records.

### Current practical next step

- Document observed artifact ownership first.
- Do not move, regenerate, or edit artifacts in this PR.
- Propose small follow-up PRs for missing ownership labels, reproducibility docs, or guard checks.
- Keep generated/canonical ownership work separate from schema, validator, record, runtime, workflow, package metadata, and CI behavior changes.
- Ask maintainers to confirm unclear source/generator/consumer relationships before artifact mutation.

## 9. Real-world analogy

In banking and e-devlet systems, a receipt view is not the ledger itself; the ledger and audit trail are the canonical records.

In SSL/TLS, a browser lock is an output of certificate and path validation, not the certificate authority database itself.

In C2PA, W3C Verifiable Credentials, and OpenTimestamps, metadata and proofs are evidence artifacts that must remain tied to their source and generation process.

HC-TRUST-LAYER should separate source records, generated outputs, canonical anchors, and public summaries the same way, so reviewers can see what is source evidence, what is derived evidence, what is a reference anchor, and what is only a public or demo view.

## 10. Follow-up items

- 4-4b optional: map each generated/canonical artifact to source input and generator.
- 4-4c optional: add artifact ownership labels or docs where missing.
- 4-4d optional: add deterministic reproducibility checks where missing.
- 4-5: demo/example boundary review.
- 5-1: onboarding / contributor guide boundary review.

These follow-ups should remain small, scoped, evidence-preserving, and human-reviewed. They should not add enforcement, regenerate artifacts, change schemas, change records, change workflows, change scripts, change tests, change runtime behavior, or add approval, merge, comment, label, reviewer-request, assignment, close, or autonomous governance authority.
