# Contributing to HC-TRUST-LAYER

Thank you for contributing to HC-TRUST-LAYER.

First-time contributors should start with the [Contributor Start Here guide](docs/contributor-start-here.md). For public-facing governance expectations, review the [Community Governance Summary](docs/community-governance.md). Before opening a public issue, review the [Issue Workflow Guide](docs/issue-workflow.md). Before opening a pull request, review the [PR Workflow Guide](docs/pr-workflow.md). Maintainers should use the [Maintainer Triage Guide](docs/maintainer-triage.md) when classifying issues and PRs.

This project focuses on transparent archival systems, verification workflows, and documented human-AI interaction research.

---

## Contribution Principles

All contributions should aim to support:

- Transparency
- Traceability
- Verification
- Open documentation
- Constructive collaboration

---

## Record Standards

When submitting a new interaction record:

- Use clear and consistent formatting.
- Include date references when possible.
- Avoid manipulated or unverifiable content.
- Preserve the original context of responses.
- Do not modify archived responses after verification.

---

## File Naming

Recommended naming format:

HC-[MODEL]-[YEAR]-[NUMBER].md

Example:

HC-CHATGPT-2026-0002.md

---

## Verification Process

Records may include:

- SHA-256 hash references
- QR verification links
- Timeline references
- Witness references
- Archive metadata

---

## Conduct

Contributors are expected to follow the HC-TRUST-LAYER Code of Conduct.

Respectful, evidence-based, and transparent collaboration is required.

---

## Experimental Status

HC:// is an experimental research protocol surface.

Structures, workflows, and standards may evolve over time.

---

## Pull Request Merge Policy (Security-First)

HC-TRUST-LAYER uses a **security-first default** for pull requests:

- All PRs require passing checks and human-supervised merge.
- Documentation-only PRs may be classified as lower risk, but they are not automatically merged.
- PRs that touch code, schemas, automation/workflows, source, or tooling paths are labeled `manual-review` and must be reviewed by a maintainer before merge.

### Docs-Only Review and Merge

Documentation-only pull requests remain human-merge required:

- The Docs Review Policy workflow is report-only and read-only.
- Docs-only classification is advisory; it does not approve or merge the PR.
- Required checks must pass before merge.
- A maintainer must perform the final merge.

### Manual Review Triggers

Any PR that changes sensitive or executable surfaces is labeled `manual-review`, including but not limited to:

- `src/`
- `schema/`
- `.github/workflows/`
- `SECURITY.md`
- `CODEOWNERS`
- dependency/runtime files (`requirements.txt`, `package.json`, `pnpm-lock.yaml`)

If a PR includes both documentation changes and protected-path changes, `manual-review` takes precedence and the PR must remain human-reviewed and human-merged.

If there is uncertainty, the policy defaults to `manual-review`.


## Setup

- Python 3.14+ recommended.
- Install dependencies: `pip install -r requirements.txt`

## Validation

- Run schema and protocol validations before opening PRs.
- Keep backward compatibility for existing record paths and links.

## Testing

- Run unit tests: `pytest -q`
- Run integration checks touching `records/`, `witness/`, `verified/`, and `archived/` paths when protocol changes are made.

## PR Workflow

1. Create a feature branch.
2. Commit focused changes with clear messages.
3. Open a PR and request review.
4. Ensure required checks pass before merge.

## Branch Naming

Use one of:
- `chore/<topic>`
- `docs/<topic>`
- `feat/<topic>`
- `fix/<topic>`
