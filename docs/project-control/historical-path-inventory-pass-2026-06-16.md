# Historical Path Inventory Pass — 2026-06-16

Status: advisory inventory pass.

This document records a directly verified historical/evidence path inventory pass after the historical evidence index and generated artifact inventory pass.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This inventory is documentation only.
- This inventory does not change records, hashes, witnesses, QR data, generated artifacts, source code, tests, workflows, schemas, policy, federation, signatures, or repository settings.
- No path is moved, renamed, deleted, archived, regenerated, or consolidated by this document.

## Inventory method

This pass uses direct evidence from:

1. `historical-evidence-index-2026-06-16.md`;
2. `GENESIS_BLOCK.md`;
3. current project-control root classification notes.

This pass does not claim to be a complete repository tree listing. A complete historical inventory requires a dedicated full tree listing or deterministic inventory artifact.

## Directly verified historical/evidence anchors

| Path | Class | Role | Review posture |
|---|---|---|---|
| `GENESIS_BLOCK.md` | `ORIGIN_RECORD` | Historical origin and early multi-model witness/hash-reference record. | Preserve caveats; do not convert candidates into canonical claims. |
| `records/` | `HISTORICAL_EVIDENCE` | Evidence-bearing records and archived records. | Protected evidence; no casual cleanup. |
| `hash/` | `HASH_REFERENCE` | Hash references and integrity artifacts. | Do not overstate as verified/canonical without source content. |
| `witness-archive/` | `WITNESS_REFERENCE` | Early witness/origin/provenance trail from Humanity Chain / HC evolution. | Preserve historical naming when it documents origin. |
| `witness/` | `WITNESS_REFERENCE` | Witness-related records or references if present. | Index before any move/archive proposal. |
| `timeline/` | `HISTORICAL_EVIDENCE` | Timeline/provenance chronology if present. | Preserve sequence context. |
| `council/` | `WITNESS_REFERENCE` | Council or multi-reviewer context if present. | Classify before movement. |
| `media/` | `HISTORICAL_EVIDENCE` | Media/provenance examples or historical references if present. | Preserve source/status notes. |

## Genesis Block evidence status

`GENESIS_BLOCK.md` states that:

- it preserves the historical origin of the HC:// TRUST LAYER experiment;
- historical hash prefixes are display-level references;
- recovered full-hash values are screenshot-derived candidates;
- it is historical/provenance context, not a canonical verification anchor.

Therefore, any future change touching `GENESIS_BLOCK.md` must preserve:

1. original chronology;
2. historical prefix/candidate distinction;
3. no-endorsement language;
4. no truth/canonical overclaim;
5. archive meaning.

## Records and hash review posture

`records/` and `hash/` require explicit review before any future structure change.

A future PR must state:

1. exact path;
2. evidence role;
3. source availability;
4. hash status;
5. canonical vs advisory status;
6. link impact;
7. tests or docs affected;
8. post-merge verification plan.

## Witness and legacy-name posture

Historical names such as Humanity Chain, Insanlik-Zinciri, and witness-chain phrasing may be part of the provenance trail.

Do not silently normalize those names when they document origin.

Prefer:

```text
historical label preserved
current HC:// term explained
redirect or index note added
```

## Safe next work

A future complete historical inventory PR may add a tree-derived path list if the tooling can produce one deterministically.

Until then, this pass is a verified anchor list, not a complete historical path inventory.

## Final rule

Historical paths must become easier to understand before they are reorganized.

```text
preserve origin
label evidence status
keep candidate separate from canonical
no silent rewrite
human review remains required
```
