# Public Demo Docs Index — 2026-06-16

Status: advisory public/demo documentation index.

This document classifies public-facing demo and validator documentation so HC-TRUST-LAYER can present a clear first-user path without weakening safety boundaries.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This index is documentation only.
- This index does not modify demos, scripts, source code, tests, workflows, schemas, records, QR data, hash data, generated artifacts, or repository settings.
- No public/demo file is moved, renamed, deleted, disabled, regenerated, or consolidated by this document.

## Public/demo operating rule

Public/demo material must be easy to try and hard to overclaim.

```text
public overview -> static demo -> local runner -> local record lookup -> boundary docs -> future production proposal
```

A demo can be useful without being a production service.

## Main public/demo classes

| Class | Purpose | Review posture |
|---|---|---|
| `PUBLIC_ENTRYPOINT` | First-reader public navigation. | Keep short, clear, and linked from README/START_HERE. |
| `STATIC_DEMO_VIEWER` | Browser/static viewer demo. | Must remain public-safe and demo-only. |
| `LOCAL_DEMO_RUNNER` | Local deterministic command runner for fixture/demo output. | Must avoid production/API claims. |
| `LOCAL_RECORD_LOOKUP` | Local-only allowed-path record lookup. | Must preserve allowed paths and no-network posture. |
| `DEMO_FIXTURE` | Bundled static scenarios and sample IDs. | Must not be confused with canonical lookup. |
| `PUBLIC_VERIFICATION_DOC` | Explains public validation response shape and limitations. | Must preserve advisory-only and human-review markers. |
| `BOUNDARY_DOC` | Explicitly states what demo/local MVP does and does not do. | Do not weaken caveats. |

## Verified public/demo anchors

These anchors were checked from current repository content during this indexing pass:

| Path | Class | Purpose |
|---|---|---|
| `README.md` | `PUBLIC_ENTRYPOINT` | Public first page linking public validator demo, local lookup quickstart, static viewer, and local demo runner. |
| `docs/START_HERE.md` | `PUBLIC_ENTRYPOINT` | Start-here navigation for new readers and operators. |
| `docs/demo/public-validator-local-record-lookup-boundary.md` | `BOUNDARY_DOC` | Defines fixture demo vs local allowed-path record lookup boundary. |
| `docs/demo/public-validator-static-viewer.html` | `STATIC_DEMO_VIEWER` | Static browser viewer referenced from README. |
| `docs/demo/public-validator-demo-quickstart.md` | `PUBLIC_VERIFICATION_DOC` | Demo quickstart referenced from README. |
| `docs/demo/public-validator-local-lookup-quickstart.md` | `LOCAL_RECORD_LOOKUP` | Local record lookup quickstart referenced from README. |
| `scripts/run_public_validator_demo.py` | `LOCAL_DEMO_RUNNER` | Local deterministic demo runner referenced from README. |
| `scripts/run_public_validator_lookup.py` | `LOCAL_RECORD_LOOKUP` | Local lookup CLI referenced from README. |
| `docs/self-service-verify.html` | `STATIC_DEMO_VIEWER` | Local verification preview entry point referenced from README. |

This is not a complete public/demo inventory. It is the first public demo map. A later PR may add a complete file-list inventory if needed.

## Safety statements that must remain visible

Public/demo docs should preserve these distinctions:

- static fixture matching is not canonical record lookup;
- local lookup is not a production API;
- local lookup is not backend service availability;
- QR/link entry is not QR authenticity proof;
- schema/hash signals are advisory validation signals;
- public-safe output is not legal, regulatory, safety, forensic, or certification determination;
- `truth_guarantee=false` remains visible;
- human-supervised review remains required.

## Local lookup boundary

Local lookup must stay restricted to allowed canonical record directories unless a later focused PR changes that boundary with tests and review.

Current allowed paths are documented as:

- `records/pending/*.json`
- `records/verified/*.json`
- `records/archived/*.json`

Demo fixtures, generated indexes, explorer indexes, manifests, cache artifacts, export artifacts, and static viewer bundled data must not be treated as canonical lookup sources for user-entered `record_id` values.

## Review rules for public/demo changes

A public/demo PR should identify:

1. exact files changed;
2. whether the change is static viewer, CLI runner, local lookup, fixture, docs, or generated output;
3. whether it changes allowed lookup paths;
4. whether it changes response shape;
5. whether it introduces network/backend/API behavior;
6. whether it touches QR, record, hash, schema, generated, or public-facing output boundaries;
7. targeted tests or smoke checks.

## Do not combine

Do not combine public/demo changes with unrelated:

- workflow permission changes;
- dependency upgrades;
- schema changes;
- record/hash/QR edits;
- generated artifact rewrites;
- governance authority changes;
- broad source refactors.

## Immediate next index work

1. optional complete generated artifact inventory.
2. optional complete historical path inventory.
3. optional complete public/demo inventory.
4. root/docs navigation update linking completed indexes.
5. then consider first safe move/archive proposal if evidence supports it.

## Final rule

Public demos should invite use while preventing overclaim.

```text
try it locally
see the evidence
see the limits
human review remains required
```
