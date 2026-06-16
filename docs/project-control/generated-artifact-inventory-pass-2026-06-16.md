# Generated Artifact Inventory Pass — 2026-06-16

Status: advisory inventory pass.

This document records a directly verified generated/reference artifact inventory pass after the repository index chain and first safe repo plan.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This inventory is documentation only.
- This inventory does not change runtime behavior, workflows, tests, schemas, records, QR data, hash data, generated artifacts, policy, federation, signatures, or repository settings.

## Inventory method

This pass uses direct file reads for known generated/reference artifacts and their source/check helpers.

It does not claim to be a complete repository file listing. A complete inventory requires a dedicated full tree listing or generated inventory artifact.

## Directly verified generated/reference artifacts

| Path | Status | Role | Source / consumer note |
|---|---|---|---|
| `generated/explorer_index.json` | generated reference | Read-only advisory explorer index. | Declares `generated_by: src/generate_explorer_index.py`; contains record summaries derived from record paths. |
| `generated/example_federation_package.json` | example package | Advisory federation reference package. | Declares advisory-only metadata and warns it is generated and non-canonical. |

## Directly verified generator/check helpers

| Path | Status | Role | Boundary note |
|---|---|---|---|
| `src/generate_explorer_index.py` | generator | Builds `generated/explorer_index.json` from allowed record directories. | Read-only input scan plus generated JSON output. |
| `scripts/check_canonical_artifacts.py` | deterministic guard | Detects non-canonical artifact patterns and canonical-boundary violations. | Treats generated/index/cache/export artifacts as non-canonical unless proper boundaries are preserved. |

## Evidence notes

`generated/explorer_index.json` currently declares:

```text
generated_by: src/generate_explorer_index.py
advisory_only: true
read_only: true
human_supervised: true
```

`generated/example_federation_package.json` currently declares:

```text
verification_mode: advisory-only
human_supervised_validation_required: true
external_verification_authority: none
generated_artifact_warning: generated and non-canonical
```

`src/generate_explorer_index.py` currently writes the explorer index to:

```text
generated/explorer_index.json
```

and reads record directories including:

```text
records/pending
records/verified
records/archived
records/archive
```

`scripts/check_canonical_artifacts.py` currently marks generated/index/export/cache artifact patterns as non-canonical and checks canonical record boundaries.

## Review posture

Generated/reference artifacts should be reviewed by:

1. source input path;
2. generator path;
3. consumer path;
4. advisory/reference/canonical status;
5. reproducibility;
6. public-safety impact;
7. canonical-boundary impact.

## Safe next work

A future complete inventory PR may add a repository tree-derived artifact list if the tooling can produce one deterministically.

Until then, use this pass as a verified anchor list, not a complete generated-artifact inventory.

## Final rule

Generated artifacts must be traceable before they are reorganized.

```text
known path
known generator
known consumer or review use
known boundary
no canonical overclaim
```
