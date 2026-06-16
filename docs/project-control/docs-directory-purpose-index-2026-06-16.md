# Docs Directory Purpose Index — 2026-06-16

Status: advisory documentation-surface index.

This index classifies the `docs/` directory so the repository is easier to navigate from GitHub without changing any source, workflow, schema, record, test, or runtime behavior.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This file is navigation only.
- This file does not move, remove, rename, disable, or rewrite existing files.

## Docs operating rule

`docs/` should be read as a layered knowledge base:

```text
start here -> demo -> runtime/spec -> security/governance -> project-control -> vision/future -> historical evidence
```

A document can be important even when it is not active implementation.

## Main documentation classes

| Class | Purpose | Typical location |
|---|---|---|
| `PUBLIC_ENTRYPOINT` | First-reader navigation and high-level explanation. | `docs/START_HERE.md`, contributor guides |
| `PUBLIC_DEMO` | Demo and local quickstart material. | `docs/demo/` |
| `PUBLIC_VERIFICATION_REFERENCE` | Public validator, explorer, API, and response-shape references. | `docs/public/`, `docs/explorer/`, `docs/api/`, verification docs |
| `RUNTIME_PROTOCOL_REFERENCE` | Runtime contracts, package verification, schema/hash/QR behavior, and deterministic output notes. | `docs/runtime/`, `docs/spec/`, `docs/architecture/` |
| `GOVERNANCE_SECURITY` | Authority, security, protected paths, lifecycle, escalation, and threat-model notes. | `docs/governance/`, `docs/security/` |
| `OPERATING_LAYER` | Project state, task maps, workflow maps, cleanup maps, handoff, and operator guidance. | `docs/project-control/` |
| `VISION_REFERENCE` | Future direction, social/source verification, federation ideas, and ecosystem planning. | `docs/vision/`, `docs/future/` |
| `HISTORICAL_EVIDENCE` | Migration, origin, witness, release, provenance, or legacy-name context. | historical or migration docs |

## Reading path by role

### New contributor

1. `docs/START_HERE.md`
2. `README.md`
3. `CONTRIBUTING.md`
4. public demo quickstarts
5. safe first issues or docs-only improvements

### Maintainer or operator

1. `docs/project-control/project-state.md`
2. `docs/project-control/next-actions.md`
3. `docs/project-control/task-ledger.md`
4. `docs/project-control/operator-entry-map.md`
5. relevant governance or security docs

### Public validator reviewer

1. public validator specification and quickstarts
2. demo runner/static viewer docs
3. public verification flow/API docs
4. QR trust-boundary docs
5. runtime/package verification docs

### Security or governance reviewer

1. `SECURITY.md`
2. `GOVERNANCE.md`
3. `docs/security/`
4. `docs/governance/`
5. workflow and protected-path maps

## Cleanup discipline

Do not simplify documentation from visual clutter alone. First classify the document by purpose and risk.

A future documentation cleanup should preserve:

- public-safe language;
- advisory-only language;
- `truth_guarantee=false` boundaries;
- historical provenance where it matters;
- governance/security review boundaries;
- links from current navigation docs.

## Immediate next index work

1. `src/` module purpose index.
2. `scripts/` tool purpose index.
3. generated/reference artifact index.
4. historical/evidence index.
5. public/demo docs index.

## Final rule

Docs must make HC easier to understand without weakening HC boundaries.

```text
clearer navigation
preserved evidence
no silent deletion
no trust overclaim
```
