# Historical Path Inventory Pass — 2026-06-16

Status: advisory inventory pass.

This document records a directly verified historical/evidence path inventory pass after the repository index chain and first safe repo plan.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This inventory is documentation only.
- This inventory does not change runtime behavior, workflows, tests, schemas, records, QR data, hash data, generated artifacts, policy, federation, signatures, witness material, historical records, or repository settings.

## Inventory method

This pass uses existing repository indexes and directly verified historical anchors.

It does not claim to be a complete repository file listing. A complete historical inventory requires a dedicated tree-derived report.

## Directly verified historical/evidence anchors

| Path | Status | Role | Boundary note |
|---|---|---|---|
| `GENESIS_BLOCK.md` | origin record | Historical HC:// TRUST LAYER origin and multi-model witness archive. | Historical/provenance context, not a canonical verification anchor. |
| `records/` | evidence surface | Evidence-bearing record directories and archived records. | Must not be silently rewritten. |
| `hash/` | hash reference surface | Hash references and integrity artifacts. | Candidate/display/hash status must remain explicit. |
| `halkalar/` | witness/origin surface | Early Humanity Chain / HC evolution witness trail. | Preserve historical naming when it documents origin. |
| `witness/` | witness surface | Witness-related records or references if present. | Preserve witness semantics. |
| `timeline/` | chronology surface | Timeline/provenance chronology if present. | Preserve sequence context. |
| `council/` | multi-reviewer context | Council or multi-reviewer reference if present. | Classify before moving. |
| `media/` | provenance/example context | Media/provenance examples if present. | Classify before moving. |

## Direct evidence notes

`GENESIS_BLOCK.md` records:

```text
Initial AI Response Record Date: May 7, 2026
Chain Initialization Date: May 8, 2026
```

It also states that the Genesis Block preserves historical origin as traceable archival context and that some hash values are screenshot-derived candidates rather than canonical anchors.

The root purpose index classifies:

```text
records/ -> HISTORICAL_EVIDENCE
hash/ -> HISTORICAL_EVIDENCE
halkalar/ -> HISTORICAL_EVIDENCE
witness/ -> HISTORICAL_EVIDENCE
timeline/ -> HISTORICAL_EVIDENCE
```

## Review posture

Historical/evidence paths should be reviewed by:

1. origin purpose;
2. evidence status;
3. hash status;
4. witness/provenance role;
5. link impact;
6. public-safety wording;
7. whether the material is historical, candidate, fixture, demo, or canonical.

## Not approved by this pass

This pass does not approve:

- moving evidence paths;
- renaming historical paths;
- rewriting witness records;
- changing hash status;
- converting candidates into canonical anchors;
- removing historical names from provenance context;
- changing public verification behavior.

## Safe next work

A future complete historical inventory PR may add a tree-derived path list if the tooling can produce one deterministically.

Until then, use this pass as a verified anchor list, not a complete historical path inventory.

## Final rule

Historical material must become easier to inspect, not easier to erase.

```text
preserve origin
label evidence status
separate candidate from canonical
index before moving
human review remains required
```
