# Public Demo Inventory Pass — 2026-06-16

Status: advisory inventory pass.

This document records a directly verified public/demo inventory pass after the public demo docs index and historical/generated inventory passes.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This inventory is documentation only.
- This inventory does not change demos, scripts, source code, tests, workflows, schemas, records, QR data, hash data, generated artifacts, policy, federation, signatures, or repository settings.

## Inventory method

This pass uses direct evidence from:

1. `public-demo-docs-index-2026-06-16.md`;
2. `README.md` public demo links;
3. current project-control public/demo classification notes.

This pass does not claim to be a complete repository file listing. A complete public/demo inventory requires a deterministic tree-derived report.

## Directly verified public/demo anchors

| Path | Class | Role | Boundary note |
|---|---|---|---|
| `README.md` | `PUBLIC_ENTRYPOINT` | Public first page and demo navigation entry. | Must keep no-production and no-truth-finality limits visible. |
| `docs/START_HERE.md` | `PUBLIC_ENTRYPOINT` | Start-here navigation for new readers and operators. | Must preserve advisory boundaries. |
| `docs/demo/public-validator-static-viewer.html` | `STATIC_DEMO_VIEWER` | Static public validator scenario viewer. | Demo-only; does not prove QR authenticity or signed payload verification. |
| `docs/demo/public-validator-demo-quickstart.md` | `PUBLIC_VERIFICATION_DOC` | Public validator demo quickstart. | Must preserve public-safe and human-review language. |
| `docs/demo/public-validator-local-lookup-quickstart.md` | `LOCAL_RECORD_LOOKUP` | Local record lookup quickstart. | Local-only; not backend/API availability. |
| `docs/demo/public-validator-local-record-lookup-boundary.md` | `BOUNDARY_DOC` | Explains fixture demo versus local allowed-path lookup. | Must preserve fixture/canonical distinction. |
| `docs/self-service-verify.html` | `STATIC_DEMO_VIEWER` | Browser-side self-service verification preview. | No upload; preview only; not registration. |
| `scripts/run_public_validator_demo.py` | `LOCAL_DEMO_RUNNER` | Local deterministic demo runner. | Demo output is advisory only. |
| `scripts/run_public_validator_lookup.py` | `LOCAL_RECORD_LOOKUP` | Local lookup CLI. | Must preserve allowed lookup path boundary. |

## README evidence status

`README.md` currently presents the demo path as public-safe and advisory-only. It links the static viewer, demo scenarios, local demo runner, demo quickstart, local lookup quickstart, and local verification preview.

The README also states that:

- fixture IDs do not perform canonical record lookup;
- local lookup is local-only and advisory-only;
- local lookup is not a production API;
- local lookup is not truth verification;
- local lookup is not QR authenticity proof;
- local lookup is not signed payload verification;
- human review remains required.

## Local lookup boundary

The public/demo docs index records the allowed local lookup paths as:

```text
records/pending/*.json
records/verified/*.json
records/archived/*.json
```

Demo fixtures, generated indexes, explorer indexes, manifests, cache artifacts, export artifacts, and static viewer bundled data must not be treated as canonical lookup sources for user-entered record IDs.

## Review posture

Public/demo paths should be reviewed by:

1. public entrypoint role;
2. static viewer role;
3. local runner role;
4. local lookup role;
5. fixture versus canonical distinction;
6. public-safe wording;
7. QR/hash/schema/generated boundary impact;
8. human-review language.

## Not approved by this pass

This pass does not approve:

- changing public demo behavior;
- changing local lookup allowed paths;
- changing response shape;
- adding network/backend/API behavior;
- changing QR/hash/schema validation behavior;
- treating demo fixtures as canonical records;
- weakening public-safe or human-review limits.

## Safe next work

A future complete public/demo inventory PR may add a tree-derived path list if the tooling can produce one deterministically.

Until then, this pass is a verified anchor list, not a complete public/demo inventory.

## Final rule

Public demos should make HC:// easy to try without making trust claims stronger than the evidence.

```text
try locally
see the evidence
see the limits
no production overclaim
human review remains required
```
