# Historical Evidence Index — 2026-06-16

Status: advisory historical/provenance index.

This document classifies historical, witness, provenance, record, hash, and origin surfaces so HC-TRUST-LAYER can become easier to navigate without losing evidence-bearing context.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This index is documentation only.
- This index does not modify records, hashes, witnesses, QR data, generated artifacts, source code, tests, workflows, schemas, policy, federation, signatures, or repository settings.
- No file is moved, renamed, deleted, archived, regenerated, or consolidated by this document.

## Historical evidence operating rule

Historical material should be reviewed by evidence role before any cleanup:

```text
origin record -> witness/provenance note -> hash/reference artifact -> current reader index -> later cleanup proposal
```

Visual clutter is not deletion evidence. Historical material can be messy and still be valuable.

## Main historical/evidence classes

| Class | Purpose | Review posture |
|---|---|---|
| `ORIGIN_RECORD` | Preserves project origin or first recorded experiment context. | Preserve; no silent rewrite. |
| `HISTORICAL_EVIDENCE` | Evidence-bearing records, timeline notes, hashes, or witness records. | Index before any move/archive. |
| `HASH_REFERENCE` | Hash prefixes, SHA-256 candidates, or integrity references. | Do not overstate as canonical unless source text and hash verification exist. |
| `WITNESS_REFERENCE` | Multi-model, human, or system witness context. | Preserve provenance language. |
| `MIGRATION_CONTEXT` | Explains old names, early repo structure, or transition from earlier concepts. | Keep discoverable to prevent confusion. |
| `LEGACY_NAME_CONTEXT` | Historical naming such as Humanity Chain or Insanlik-Zinciri when used as provenance. | Preserve when it documents origin. |
| `ARCHIVE_CANDIDATE_REPORT_ONLY` | May be moved later only after full classification and review. | No automatic archive from name alone. |

## Verified anchors

These anchors were checked during this indexing pass:

| Path | Class | Purpose |
|---|---|---|
| `GENESIS_BLOCK.md` | `ORIGIN_RECORD` | Preserves the early multi-model response archive and hash-reference origin of HC:// TRUST LAYER. |
| `records/` | `HISTORICAL_EVIDENCE` | Evidence-bearing records and archived records. |
| `hash/` | `HASH_REFERENCE` | Hash references and integrity artifacts. |
| `halkalar/` | `WITNESS_REFERENCE` | Early witness/origin/provenance trail from Humanity Chain / HC evolution. |
| `witness/` | `WITNESS_REFERENCE` | Witness-related records or references if present. |
| `timeline/` | `HISTORICAL_EVIDENCE` | Timeline/provenance chronology if present. |
| `council/` | `WITNESS_REFERENCE` | Council or multi-reviewer context if present. |
| `media/` | `HISTORICAL_EVIDENCE` | Media/provenance examples or historical references if present. |

## Genesis Block boundary

`GENESIS_BLOCK.md` is historical/provenance context. It documents origin, witness experimentation, and hash-reference preservation.

Its own text states that historical prefixes and screenshot-derived full-hash candidates are not canonical verification anchors unless original canonical source text and verification evidence are available.

Cleanup rule:

- preserve it at root unless a future root reorganization has explicit redirect and evidence handling;
- do not rewrite historical model/provider labels to make them look current;
- do not convert hash candidates into canonical claims;
- do not remove caveats that distinguish provenance from verification.

## Records and hash boundary

`records/` and `hash/` are not normal clutter folders.

They can contain evidence, demonstrations, historical continuity, or integrity references. A future cleanup PR must classify:

1. record purpose;
2. hash source;
3. whether source content is available;
4. whether the hash is verified, candidate, fixture, or historical display prefix;
5. whether a public/demo or canonical boundary is involved;
6. what tests or docs reference it.

## Witness and legacy boundary

Witness and legacy naming may look inconsistent from a modern repo view, but these names can preserve project origin.

Do not silently remove or rename:

- Humanity Chain references when used as origin context;
- Insanlik-Zinciri references when used as historical context;
- witness chain notes;
- council or multi-reviewer provenance notes;
- early timeline context.

Prefer index notes and redirects before any move.

## Future cleanup requirements

A future move/archive/delete/consolidation PR for historical material must state:

1. exact paths;
2. current classification;
3. why it is not protected evidence;
4. new location or redirect;
5. link impact;
6. tests or docs affected;
7. audit note;
8. post-merge verification plan.

## Do not combine

Do not combine historical/evidence cleanup with unrelated:

- workflow permission changes;
- source refactors;
- dependency upgrades;
- schema changes;
- generated artifact rewrites;
- public validator behavior changes;
- governance authority changes.

## Immediate next index work

1. public/demo docs index.
2. optional complete generated artifact inventory.
3. optional complete historical path inventory.
4. root/docs navigation update linking completed indexes.

## Final rule

Historical evidence must become easier to find, not easier to erase.

```text
preserve origin
label evidence status
separate candidate from canonical
index before moving
no silent rewrite
```
