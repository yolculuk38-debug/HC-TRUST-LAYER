# Generated Reference Artifact Index — 2026-06-16

Status: advisory generated/reference artifact index.

This document classifies generated and machine-readable reference artifacts so HC-TRUST-LAYER can preserve evidence, navigation, and automation outputs without confusing derived files with canonical records.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This index is documentation only.
- This index does not modify generated files, root JSON indexes, workflows, source behavior, tests, schemas, records, QR data, hash data, or repository settings.
- No artifact is moved, renamed, deleted, disabled, regenerated, or consolidated by this document.

## Artifact operating rule

Generated and machine-readable artifacts should be reviewed by origin, generator, consumer, and risk boundary:

```text
source input -> generator/tool -> generated artifact -> consumer/check -> audit note
```

A derived artifact can be useful, but it is not automatically a canonical record.

## Main artifact classes

| Class | Purpose | Review posture |
|---|---|---|
| `ROOT_REFERENCE_INDEX` | Machine-readable project navigation or trust-kernel reference at repository root. | Keep stable and review drift carefully. |
| `GENERATED_REFERENCE` | Derived JSON, index, manifest, or static artifact produced from repository inputs. | Generator/source path should remain clear. |
| `PUBLIC_VIEWER_ARTIFACT` | Static public viewer or explorer output used for demos or navigation. | Must keep public-safe and advisory boundaries. |
| `EXAMPLE_PACKAGE` | Example verification or federation package used by docs/tests/demos. | Do not treat as live production evidence. |
| `REPORT_ARTIFACT` | Output created by a report-only workflow, bot, or inventory script. | Evidence for review, not final decision authority. |
| `CACHE_OR_EXPORT` | Derived cache/export/manifest content. | Must not silently replace canonical records. |

## Verified root reference indexes

These root reference indexes were checked from current repository content during this indexing pass:

| Path | Class | Purpose |
|---|---|---|
| `protocol-graph.json` | `ROOT_REFERENCE_INDEX` | Machine-readable HC:// protocol and component navigation reference. |
| `verification-map.json` | `ROOT_REFERENCE_INDEX` | Machine-readable verification-context map for repository-level HC:// surfaces. |
| `trust-kernel-index.json` | `ROOT_REFERENCE_INDEX` | Machine-readable trust-kernel navigation layer linking protocol graph and verification map foundations. |

## Verified generated/reference anchors

Search evidence found these generated/reference anchors:

| Path | Class | Purpose |
|---|---|---|
| `generated/explorer_index.json` | `GENERATED_REFERENCE` | Explorer/navigation index generated from repository records or docs. |
| `generated/example_federation_package.json` | `EXAMPLE_PACKAGE` | Example federation package for generated/demo/reference use. |
| `src/generate_explorer_index.py` | `GENERATOR` | Source-side generator for explorer index output. |
| `scripts/check_canonical_artifacts.py` | `DETERMINISTIC_GUARD` | Canonical/generated artifact boundary check helper. |
| `docs/governance/post-migration-generated-artifact-review.md` | `GOVERNANCE_SECURITY` | Governance review note for generated artifact handling. |

This is not a complete artifact inventory. It is the first generated/reference map. A later PR may add a complete file-list inventory if needed.

## Review rules for generated artifacts

A generated/reference artifact change should identify:

1. exact artifact paths changed;
2. source inputs;
3. generator/tool path;
4. consumer path or workflow;
5. whether the output is public-facing;
6. whether it touches records, QR, hash, schema, policy, federation, signing, or canonical boundaries;
7. whether regeneration is deterministic;
8. whether the artifact is advisory/reference or canonical.

## Do not combine

Do not combine generated artifact changes with unrelated:

- workflow permission changes;
- runtime behavior changes;
- dependency upgrades;
- schema changes;
- record/hash/QR edits;
- governance authority changes;
- broad source refactors.

## Cleanup discipline

Do not delete or overwrite generated/reference artifacts from visual clutter alone.

A future cleanup PR should first answer:

- is this derived or canonical;
- what generated it;
- what reads it;
- what test or workflow protects it;
- what audit note explains the change;
- how a reviewer can reproduce or validate it.

## Immediate next index work

1. historical/evidence index.
2. public/demo docs index.
3. optional complete generated artifact inventory.
4. optional root/docs navigation update linking completed indexes.

## Final rule

Generated artifacts must be traceable before they are trusted as evidence.

```text
clear source
clear generator
clear consumer
clear status
no silent overwrite
```
