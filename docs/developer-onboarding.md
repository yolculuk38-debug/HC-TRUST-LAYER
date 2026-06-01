# Developer Onboarding

This guide describes a local contributor workflow for HC-TRUST-LAYER documentation, tests, and advisory tooling. It does not change HC:// protocol behavior, canonical record schemas, validators, signing logic, federation logic, or policy evaluator behavior.

## Supported Python Version

Use Python 3.11 or newer for local development and CI alignment. The repository may contain compatibility metadata for older Python versions, but new contributor environments should use Python 3.11+ unless maintainers document a different target.

## Create a Virtual Environment

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Install Dependencies

Install the pinned repository dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

For editable package installs used by runtime/API tests, contributors may also use:

```bash
pip install -e ".[test]"
```

## Run Tests

Run the pytest suite from the repository root:

```bash
pytest -q
```

For scoped changes, run the smallest relevant test subset first, then run the broader suite before opening a Pull Request when feasible.

## Run Lint Checks

Run Ruff before submitting changes:

```bash
ruff check .
```

If Ruff is not installed in the active environment, install it in the virtual environment:

```bash
pip install ruff
```

## Optional Type Checking

Type checking is advisory unless a workflow or maintainer marks it as required:

```bash
mypy src/
```

If mypy is not installed in the active environment, install it in the virtual environment:

```bash
pip install mypy
```

## Repository Guard Checks

Documentation-focused changes should run the repository guard checks when possible:

```bash
python scripts/check_terminology.py
python scripts/check_docs_drift.py
python scripts/check_canonical_artifacts.py
```

If a check cannot run in the local environment, document the command, observed error, and reason in the Pull Request. Do not imply a check passed unless it completed successfully.

## Contribution Workflow

Expected contributor flow:

1. Create a feature branch.
2. Implement a small, scoped change.
3. Run tests with `pytest -q` or the relevant subset.
4. Run lint checks with `ruff check .`.
5. Run applicable repository guard checks.
6. Open a Pull Request with a concise summary, test results, and any human-supervised validation notes.

## Review Boundaries

Escalate changes that may affect trust kernel boundaries, canonical record surfaces, schema contracts, validator behavior, signing semantics, federation behavior, or policy interpretation. HC-TRUST-LAYER treats agent output as advisory until reviewed through repository-defined checks and human-supervised validation.
