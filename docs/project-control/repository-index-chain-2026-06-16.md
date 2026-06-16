# Repository Index Chain — 2026-06-16

Status: advisory navigation index.

This document links the repository purpose indexes completed during the 2026-06-16 cleanup mapping pass.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This document is navigation only.
- This document does not modify runtime behavior, workflows, tests, schemas, records, QR data, hash data, generated artifacts, policy, federation, signatures, or repository settings.

## Why this exists

The repository now has separate purpose indexes for the main surfaces that were previously hard to scan as one large tree.

Use this chain before proposing a repository reorganization PR.

```text
map first -> link the map -> propose one small safe change -> run CI -> human review
```

## Index chain

1. Root file purpose index: [`root-file-purpose-index-2026-06-16.md`](root-file-purpose-index-2026-06-16.md)
2. Docs directory purpose index: [`docs-directory-purpose-index-2026-06-16.md`](docs-directory-purpose-index-2026-06-16.md)
3. Source module purpose index: [`src-module-purpose-index-2026-06-16.md`](src-module-purpose-index-2026-06-16.md)
4. Scripts tool purpose index: [`scripts-tool-purpose-index-2026-06-16.md`](scripts-tool-purpose-index-2026-06-16.md)
5. Generated/reference artifact index: [`generated-reference-artifact-index-2026-06-16.md`](generated-reference-artifact-index-2026-06-16.md)
6. Historical evidence index: [`historical-evidence-index-2026-06-16.md`](historical-evidence-index-2026-06-16.md)
7. Public demo docs index: [`public-demo-docs-index-2026-06-16.md`](public-demo-docs-index-2026-06-16.md)

## Inventory pass chain

Use these inventory passes after the purpose indexes when a later PR needs path-level evidence:

1. Generated artifact inventory pass: [`generated-artifact-inventory-pass-2026-06-16.md`](generated-artifact-inventory-pass-2026-06-16.md)
2. Historical path inventory pass: [`historical-path-inventory-pass-2026-06-16.md`](historical-path-inventory-pass-2026-06-16.md)
3. Public demo inventory pass: [`public-demo-inventory-pass-2026-06-16.md`](public-demo-inventory-pass-2026-06-16.md)

These passes are verified anchor lists, not complete tree listings.

## Surface summary

| Surface | Current index | Review posture |
|---|---|---|
| Root files and top-level directories | Root file purpose index | Keep public, governance, tooling, and evidence roles separate. |
| Documentation tree | Docs directory purpose index | Keep public docs, governance docs, project-control docs, and historical references distinct. |
| Source modules | Source module purpose index | Review by runtime, telemetry, validator, QR, redaction, and state boundaries. |
| Scripts and tools | Scripts tool purpose index | Review by capability: read-only, report-only, generator, local verifier, or write-capable. |
| Generated/reference artifacts | Generated/reference artifact index | Track source, generator, consumer, and reference status. |
| Historical/evidence material | Historical evidence index | Preserve origin and evidence status before any reorganization. |
| Public/demo documentation | Public demo docs index | Keep demos easy to try and hard to overclaim. |

## Reorganization gate

A future repository reorganization PR should state:

1. exact paths;
2. relevant index entry;
3. current role;
4. proposed target role;
5. link impact;
6. test or check impact;
7. reviewer risk boundary.

## Safe next work

The next safe work after this chain is one of:

- complete generated artifact inventory;
- complete historical path inventory;
- complete public/demo inventory;
- root/docs navigation link refresh;
- first small reorganization proposal if the index chain supports it.

## Final rule

Repository cleanup must improve traceability before it changes structure.

```text
classification first
small PRs only
no hidden authority
human review remains required
```
