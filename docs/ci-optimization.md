# HC-TRUST-LAYER CI Speed and Safety Model

## Purpose

This document describes how CI is optimized for faster feedback while preserving trust-critical safety checks.

## Design Principles

- keep trust-sensitive checks mandatory for schema, validator, records, policy, and workflow changes
- avoid redundant CI runs on superseded commits by using workflow concurrency cancellation
- apply least-privilege GitHub token permissions for read-only checks
- reduce setup time with Python dependency caching
- prevent docs-only changes from triggering unrelated heavy validation jobs

## Safety-Critical Coverage

The following areas remain protected by validation and guard workflows:

- `schema/**`
- `src/**` (validator/runtime scripts)
- `records/**`
- `policy/**`
- `.github/workflows/**`

Changes in these paths must continue to run the relevant schema validation, record validation, canonical artifact checks, and workflow-linked protections.

## Speed Optimizations

### 1) Concurrency with cancel-in-progress

Documentation and validation workflows use concurrency groups with `cancel-in-progress: true` so stale runs are cancelled when newer commits arrive on the same ref.

### 2) Least-privilege permissions

Read-only CI jobs use:

```yaml
permissions:
  contents: read
```

This narrows token scope and reduces accidental write capability in guard workflows.

### 3) Python dependency caching

Workflows using `actions/setup-python` enable pip caching to reduce repeated dependency download/install overhead.

### 4) Path-scoped triggering

Heavy validation workflows are scoped with path filters so docs-only edits avoid unnecessary compute, while trust-critical path changes still trigger the expected checks.

## Guardrails That Must Not Be Weakened

Optimization does not relax:

- terminology guard
- docs drift guard
- canonical artifact guard
- CodeQL (when configured/applicable)
- schema and validation checks for trust-critical paths

## Relationship to Governance

This CI model supports trusted automation by combining:

- fast feedback for low-risk changes
- full checks for trust-sensitive modifications
- explicit permission boundaries
- auditable workflow behavior

See also:

- `docs/trusted-auto-merge.md`
- `docs/policy-rules.md`
