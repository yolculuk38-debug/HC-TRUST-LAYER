# HC-DEC-0001 — Copilot Implementation Feedback Summary

Status: advisory evidence only.

This record summarizes external Copilot implementation, repository structure, testing, and maintainability feedback for HC-DEC-0001.

Main advisory points:

- Prioritize authority policy, deterministic scanning, protected-path detection, advisory-only bot behavior, and minimal tests.
- Keep implementation small, reviewable, and dependency-light.
- Prefer Python standard library for deterministic validators where possible.
- Treat governance docs, workflows, scripts, and protected-path configuration as trust-kernel critical surfaces.
- Keep HC Control Bot advisory-only in code and avoid merge, approve, close, or reject behavior.
- Use structured JSON output for deterministic report artifacts before expanding comments or automation.
- Keep fixtures small, human-readable, and version-controlled.

Recommended next small code PR:

- Add a deterministic changed-file scanner that reads protected-path configuration and emits structured JSON.
- Do not add autonomous approval, merge, close, or rejection behavior.
- Do not add AI scoring or non-deterministic behavior.

Recommended next small docs PR:

- Add or maintain a concise HC Control Bot authority policy describing advisory-only behavior, human final authority, and disable-on-violation expectations.

Tests recommended before public demo expansion:

- Unit tests for changed-file scanning logic.
- Integration tests with mock PR metadata.
- Policy-boundary tests for advisory-only behavior.
- Backward compatibility regression tests.

Implementation work to postpone:

- External standards integrations.
- Complex provenance or witness chains.
- Multi-language semantic analysis.
- AI-driven scoring or ranking.

Minimal release-readiness checklist:

- Authority policy in main.
- Deterministic validator script.
- Minimal workflow permissions.
- Advisory-only report template.
- Unit and integration tests passing.
- Disable-on-policy-violation logic documented.
- Maintainer-facing documentation clear.

Integrity boundary:

This document does not change runtime behavior, workflows, schemas, validators, bot permissions, final decision state, release status, or truth guarantees.
