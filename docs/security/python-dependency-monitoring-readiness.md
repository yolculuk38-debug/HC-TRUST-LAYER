# Python Dependency Monitoring Readiness

Status: report only.

This document assesses whether HC-TRUST-LAYER is ready to expand Dependabot beyond GitHub Actions into Python dependency monitoring.

No Dependabot configuration is changed by this document.

## Current state

The repository currently has Python dependency declarations in two places:

```text
requirements.txt
pyproject.toml
```

`requirements.txt` contains pinned dependencies for CI stability and runtime API tests.

`pyproject.toml` contains package metadata, runtime dependencies, and optional test dependencies.

Current `.github/dependabot.yml` only watches GitHub Actions dependencies.

## Relevant dependency files

### `requirements.txt`

Current observed dependencies:

```text
jsonschema==4.17.3
qrcode[pil]==7.4.2
anyio==4.9.0
fastapi==0.115.14
pydantic==2.11.7
httpx==0.28.1
pytest==9.0.3
```

### `pyproject.toml`

Current observed runtime dependencies:

```text
fastapi==0.115.14
jsonschema==4.17.3
pydantic==2.11.7
qrcode[pil]==7.4.2
```

Current observed optional test dependencies:

```text
anyio==4.9.0
httpx==0.28.1
pytest<9; python_version < '3.10'
pytest==9.0.3; python_version >= '3.10'
```

## Readiness assessment

Python dependency monitoring is useful, but it should not be enabled blindly.

Python updates may affect:

- runtime/API behavior;
- validator behavior;
- schema validation behavior;
- QR generation or parsing behavior;
- test collection and CI stability;
- advisory-only response contracts;
- public-safe runtime semantics.

## Risks

### Duplicate declaration risk

Some dependencies appear in both `requirements.txt` and `pyproject.toml`.

A Dependabot update may touch one file but not the other, creating version drift.

### Runtime/API risk

Dependencies such as `fastapi`, `pydantic`, `httpx`, and `anyio` are runtime/API-adjacent.

Updates may change request handling, response serialization, test client behavior, or validation behavior.

### Schema and validator risk

`jsonschema` is schema-adjacent.

Updates may affect validation behavior or error formatting.

### QR dependency risk

`qrcode[pil]` is QR-adjacent.

Updates may affect generated QR artifacts or dependencies used by image generation.

### Test stability risk

`pytest` and `httpx` updates may affect test collection, async behavior, or runtime app testing.

## Recommended policy before enabling

Before adding Python to `.github/dependabot.yml`, the repository should decide:

- whether `requirements.txt`, `pyproject.toml`, or both are authoritative for dependency updates;
- whether updates should be security-only or routine;
- whether the cadence should be weekly or monthly;
- whether the open pull request limit should be lower than GitHub Actions updates;
- whether grouped updates are allowed;
- which tests must pass before merging;
- how to avoid drift between duplicate dependency declarations.

## Recommended initial Dependabot scope

If Python monitoring is enabled later, the safest first configuration would be:

```text
package ecosystem: pip
directory: /
schedule: monthly
open pull request limit: 2
allow auto-merge: no
```

Recommended initial mode:

```text
security and patch-level updates only where possible
```

If Dependabot cannot express the exact intended filtering safely, keep Python monitoring disabled until the review process is ready.

## Required review checklist for Python dependency PRs

Every Python dependency PR should answer:

- Which dependency changed?
- Is it runtime, schema, validator, QR, test, or tooling related?
- Does the change affect both `requirements.txt` and `pyproject.toml`?
- Are dependency declarations still consistent?
- Did runtime/API tests run?
- Did schema/validator tests run where relevant?
- Did QR-related tests or docs require review?
- Did the PR touch protected paths?
- Does the PR preserve advisory-only and public-safe behavior?
- Does `truth_guarantee` remain false where applicable?

## Recommended decision

Do not expand Dependabot to Python dependencies yet.

Next safe action:

```text
Review dependency duplication between requirements.txt and pyproject.toml.
```

After that, open a separate PR if maintainers decide to add Python monitoring.

## Final boundary

Dependency monitoring is helpful.

Dependency monitoring is not a substitute for runtime tests, schema review, validator review, governance review, or human maintainer judgment.

Trust the record, not the narrative.
