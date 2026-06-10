# Developer Onboarding

This guide describes an advisory local contributor workflow for HC-TRUST-LAYER documentation, tests, and review preparation. It helps human contributors and AI agents understand setup, checks, contribution flow, protected paths, and agent check-in / checkout without changing HC:// protocol behavior, canonical record schemas, validators, signing logic, federation logic, policy evaluator behavior, or workflow automation.

## Start-Here Read Order

Before changing files, read these repository sources in order so local work stays aligned with current project state and review boundaries:

1. `AGENTS.md`
2. `HC_BOOTSTRAP.md`
3. `docs/project-control/project-state.md`
4. `docs/project-control/agent-operating-model.md`
5. `docs/project-control/task-ledger.md`
6. `docs/project-control/next-actions.md`
7. `README.md`
8. `docs/CONTRIBUTING.md`

Use these documents as the first source of truth for repository status, contributor expectations, and agent context. If they appear to conflict, stop and ask maintainers which current direction to follow instead of inferring a production guarantee.

## Python Version Guidance

Use Python 3.14 or newer for local development when possible.

- Preferred contributor version: Python 3.14+
- Package metadata floor: Python >=3.14
- CI alignment target: Python 3.14

If your local Python version differs from CI alignment, report that in check notes when failures may be environment-related.

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

Install the repository dependencies from the repository root:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For editable package installs used by runtime/API tests, contributors may also use:

```bash
python -m pip install -e ".[test]"
```

## Local Test Environment

Use `PYTHONPATH=src` for local pytest commands so tests resolve the in-repository package consistently without implying any production deployment behavior.

Common commands:

```bash
PYTHONPATH=src pytest -q
PYTHONPATH=src pytest -q tests/test_hc_runtime_app.py tests/test_hc_runtime_pipeline.py tests/test_hc_runtime_response_contracts.py tests/runtime
PYTHONPATH=src pytest -q tests/runtime tests/test_hc_runtime_response_contracts.py
```

For scoped changes, run the smallest relevant test subset first, then run the broader suite before opening a Pull Request when feasible.

## Optional Developer Checks

Run Ruff before submitting code or formatting-sensitive documentation changes when applicable:

```bash
ruff check .
```

If Ruff is not installed in the active environment, install it in the virtual environment:

```bash
python -m pip install ruff
```

Type checking is advisory unless a workflow or maintainer marks it as required:

```bash
mypy src/
```

If mypy is not installed in the active environment, install it in the virtual environment:

```bash
python -m pip install mypy
```

## Governance and Guard Checks

Documentation-focused changes should run the repository guard checks when possible:

```bash
python scripts/check_terminology.py
python scripts/check_docs_drift.py
python scripts/check_canonical_artifacts.py
```

When the touched scope is relevant to verification package structure or documentation, also run:

```bash
python scripts/check_verification_package_schema.py
```

If a check cannot run in the local environment, document the command, observed error, and reason in the Pull Request. Do not imply a check passed unless it completed successfully.

## Protected Path Warning Flow

Treat these paths as protected unless a task explicitly requests changes there:

- `schema/**`
- `validators/**`
- `federation/**`
- `signatures/**`
- `canonical/**`
- `policy/**`
- `.github/workflows/**`
- `records/**`

If a requested change appears to require a protected path:

1. Stop before editing the protected path.
2. Explain why the protected path appears necessary.
3. Identify the trust-kernel, canonical record, schema, validator, signing, federation, policy, or workflow boundary that may be affected.
4. Ask for explicit maintainer direction and human-supervised validation expectations.
5. Prefer a documentation clarification or test-only proposal when it can safely describe the gap without changing protected behavior.

## Contribution Workflow

Expected contributor flow:

1. Read the start-here documents.
2. Create a feature branch for one small, reviewable change.
3. Confirm the change scope avoids protected paths unless explicitly approved.
4. Implement the smallest advisory change that satisfies the task.
5. Run relevant tests and guard checks from the repository root.
6. Review `git diff --check` and `git status --short` before committing.
7. Commit with a concise message that reflects the scope.
8. Open a Pull Request with changed files, checks run, known limitations, and any human-supervised validation notes.

Do not weaken governance guardrails, bypass validation controls, or claim production readiness, security guarantees, forensic certainty, autonomous governance finality, or complete dispute automation.

## Agent Check-In Template

AI agents should begin work with a concise check-in note such as:

```text
Task: <requested task>
Mode: <docs only / tests only / implementation / investigation>
Planned scope: <files or directories expected to change>
Protected paths: <none expected / list and escalation need>
Start-here status: <documents reviewed or reason not reviewed>
Validation plan: <checks or tests planned>
Uncertainties: <open questions or repository evidence needed>
```

Keep the check-in advisory and update it if the task scope changes.

## Agent Checkout Template

AI agents should finish work with a checkout note such as:

```text
Changed files: <exact files changed>
Protected paths modified: <no / yes with explicit approval reference>
Checks run: <commands and pass/fail/environment notes>
Human-supervised validation needed: <none identified / describe boundary>
Commit: <hash if committed>
PR: <link or number if opened>
Limitations: <anything not run or not verified>
```

The checkout should make review provenance clear and should not imply success for checks that were not run.

## Troubleshooting

- If imports fail in local tests, retry from the repository root with `PYTHONPATH=src`.
- If dependency installation fails, confirm the active virtual environment and Python version before changing files.
- If guard checks fail, inspect the reported paths and prefer targeted documentation fixes over broad rewrites.
- If docs drift or canonical artifact checks identify generated or canonical surfaces, do not edit protected artifacts unless the task explicitly authorizes that scope.
- If a task request conflicts with repository guidance, document the conflict and escalate instead of guessing.

## Guardrails and Escalation

Escalate before changing runtime verification behavior, schema contracts, validator logic, signing and trust anchor semantics, federation behavior, policy evaluator behavior, canonical record identity, deterministic serialization assumptions, hash-linked artifacts, or provenance continuity.

All non-trivial trust-kernel-impacting changes require explicit human-supervised validation. For onboarding work, prefer concise documentation clarification that preserves existing HC:// terminology and keeps review boundaries visible.
