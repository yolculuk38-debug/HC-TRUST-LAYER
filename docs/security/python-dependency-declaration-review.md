# Python Dependency Declaration Review

Status: report only.

Historical note: This document is a historical/report-only review. It records dependency declarations observed at the time of that review and should not be read as the current dependency baseline. Current package metadata must be confirmed from `pyproject.toml`. Current pinned install/test dependencies must be confirmed from `requirements.txt`. Current Python support baseline must be confirmed from `pyproject.toml` and the latest Python migration/support checkpoint.

This document reviews duplicate Python dependency declarations across `requirements.txt` and `pyproject.toml` before any Dependabot Python monitoring is enabled.

No dependency versions are changed by this document.

No Dependabot configuration is changed by this document.

## Source files reviewed

```text
requirements.txt
pyproject.toml
```

## Observed dependency declarations

### `requirements.txt`

```text
jsonschema==4.17.3
qrcode[pil]==7.4.2
anyio==4.9.0
fastapi==0.115.14
pydantic==2.11.7
httpx==0.28.1
pytest==9.0.3
```

### `pyproject.toml` runtime dependencies

```text
fastapi==0.115.14
jsonschema==4.17.3
pydantic==2.11.7
qrcode[pil]==7.4.2
```

### `pyproject.toml` optional test dependencies

```text
anyio==4.9.0
httpx==0.28.1
pytest<9; python_version < '3.10'
pytest==9.0.3; python_version >= '3.10'
```

## Duplicate dependency map

| Dependency | `requirements.txt` | `pyproject.toml` | Status |
| --- | --- | --- | --- |
| `fastapi` | `0.115.14` | `0.115.14` | aligned |
| `jsonschema` | `4.17.3` | `4.17.3` | aligned |
| `pydantic` | `2.11.7` | `2.11.7` | aligned |
| `qrcode[pil]` | `7.4.2` | `7.4.2` | aligned |
| `anyio` | `4.9.0` | `4.9.0` in optional `test` | aligned |
| `httpx` | `0.28.1` | `0.28.1` in optional `test` | aligned |
| `pytest` | `9.0.3` | conditional marker in optional `test` | partially aligned |

## Key finding

The current declarations are mostly aligned, but there is duplicate dependency ownership across `requirements.txt` and `pyproject.toml`.

This creates a future drift risk if Dependabot updates one file without updating the other.

## Pytest marker note

`requirements.txt` pins:

```text
pytest==9.0.3
```

`pyproject.toml` uses conditional markers:

```text
pytest<9; python_version < '3.10'
pytest==9.0.3; python_version >= '3.10'
```

This was intentional-looking at the time of this historical review because the project then supported `requires-python = ">=3.9"`. This note is historical and superseded by later Python baseline work.

Before automated Python dependency monitoring is enabled, maintainers should decide whether Python 3.9 compatibility remains required for test dependencies.

## Risk areas by dependency

### Runtime/API adjacent

```text
fastapi
pydantic
anyio
httpx
```

Potential impact:

- response serialization;
- runtime app behavior;
- async behavior;
- test client behavior;
- advisory response contract stability.

### Schema / validation adjacent

```text
jsonschema
```

Potential impact:

- schema validation behavior;
- validation error shape;
- validator compatibility.

### QR adjacent

```text
qrcode[pil]
```

Potential impact:

- QR artifact generation;
- image-generation dependency behavior;
- demo or public validator QR outputs.

### Test tooling

```text
pytest
httpx
anyio
```

Potential impact:

- test collection;
- async test execution;
- runtime endpoint test behavior.

## Recommended decision before Dependabot Python monitoring

Do not enable Python monitoring until the repository picks one of these ownership models:

### Option A — `requirements.txt` remains CI install source

Use `requirements.txt` as the main CI pin file and manually mirror required package metadata into `pyproject.toml`.

Benefit:

- simple CI behavior;
- current pattern remains stable.

Risk:

- duplicated dependency versions can drift.

### Option B — `pyproject.toml` becomes package dependency source

Use `pyproject.toml` as the canonical package dependency source and reduce `requirements.txt` to CI/test install guidance.

Benefit:

- package metadata becomes cleaner.

Risk:

- requires careful CI/install review;
- may affect existing scripts or documentation.

### Option C — keep both, but require paired updates

Keep both files but require every dependency PR to update both declarations when relevant.

Benefit:

- smallest policy shift.

Risk:

- still depends on human review discipline.

## Recommended immediate path

For the next step, prefer Option C.

Reason:

- it avoids install behavior changes;
- it preserves current CI expectations;
- it allows safe manual review before enabling automation;
- it matches the current human-supervised HC governance model.

## Proposed rule for future Python dependency PRs

Every Python dependency update PR should include a short declaration consistency section:

```text
Dependency declaration consistency:
- requirements.txt checked: yes/no
- pyproject.toml checked: yes/no
- duplicated dependency versions aligned: yes/no/not applicable
- Python version marker impact reviewed: yes/no/not applicable
```

## Final recommendation

Do not update `.github/dependabot.yml` yet.

Next safe action after this report:

```text
Add a dependency consistency checklist reference to the dependency update policy.
```

Only after that should maintainers consider a scoped `.github/dependabot.yml` change for Python monitoring.

Trust the record, not the narrative.

Historical dependency reviews must be read in sequence with later dependency-wave checkpoints, Python migration checkpoints, `pyproject.toml`, and `requirements.txt`.
