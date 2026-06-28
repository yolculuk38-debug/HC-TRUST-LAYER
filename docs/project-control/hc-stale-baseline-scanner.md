# HC Stale Baseline Scanner

The HC stale baseline scanner is a deterministic, local, ecosystem-aware, report-only helper for HC-TRUST-LAYER baseline review.
It scans documentation for stale-looking Python, Java, Node/JavaScript/TypeScript, Go, Rust, and future ecosystem baseline references that may otherwise be mistaken for current repository-declared baseline guidance.

## What it checks

The scanner observes baseline signals declared inside this repository.
It does not compare against the latest versions available upstream.
Current/latest baseline means the latest baseline declared in repository files, not the newest release published by an external project.

Initial baseline sources include:

- Python: `pyproject.toml`, `requirements.txt`, workflow `python-version` values
- Java: `pom.xml`, `build.gradle`, `build.gradle.kts`, `gradle.properties`, `.java-version`, workflow `java-version` values
- Node / JavaScript / TypeScript: `package.json`, lockfiles, `.nvmrc`, `.node-version`, workflow `node-version` values
- Go: `go.mod`, workflow `go-version` values
- Rust: `Cargo.toml`, `rust-toolchain`, `rust-toolchain.toml`

It then scans `docs/**/*.md` for configured stale-looking references such as older runtime versions, dependency pins, or workflow/runtime declarations.
Matches are annotated by ecosystem and reported as either historical-safe or missing-boundary findings.
A documentation file is treated as historical-safe when it contains an explicit boundary note such as `Historical/report-only boundary`, `historical/report-only`, or wording that says the evidence should not be read as the current baseline.

## What it does not do

The scanner does not fetch latest upstream versions and does not replace Dependabot, Renovate, or similar dependency update tooling.
It does not rewrite old audit records, edit files, create pull requests, comment on issues, apply labels, request reviewers, approve changes, merge changes, call an LLM, use the GitHub API, or make network calls.
It is advisory-only and does not provide truth, security, legal, identity, approval, or merge authority.

## Why old audit records are not rewritten

Historical HC:// and HC-TRUST-LAYER evidence may contain older runtime versions, dependency pins, workflow runtimes, or CI/test observations.
Those values can be valid audit records for their review moment even when they are no longer the active repository-declared baseline.
Rewriting old evidence would weaken provenance continuity and make the review trail harder to audit.
The scanner therefore reports stale-looking references and boundary status without changing historical documents.

## Review boundary

The current repository-declared baseline must still be confirmed from package metadata, dependency files, workflow files, and live GitHub Actions when live CI status is relevant.
Local CI/check output is evidence, not trust authority.
Human review remains final for HC-TRUST-LAYER governance and release decisions.
