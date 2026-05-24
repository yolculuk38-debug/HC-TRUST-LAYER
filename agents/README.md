# HC-TRUST-LAYER Agent Workspace

## Purpose

The HC-TRUST-LAYER **agent workspace** is a repo-native documentation surface for AI-assisted development across HC:// trust-kernel domains.

It provides stable **agent context**, explicit task routing, verification discipline, and auditable collaboration patterns that preserve **provenance**, **audit trail** continuity, and **human-supervised validation**.

## Supported Agents

This workspace is designed for:

- ChatGPT
- Codex
- Claude
- Cursor
- future agents

## Core Rules

- The repository is the source of truth for architecture, implementation status, the **verification map**, the machine-readable verification map index (`verification-map.json`, `docs/verification-map-index.md`), and the **protocol graph**.
- All non-trivial trust-kernel-impacting work requires explicit **human-supervised validation**.
- Agent output is advisory and must not be treated as autonomous approval.

## Governance and Claim Boundaries

- No autonomous governance.
- No production claims.
- No production-readiness guarantees unless implemented and validated in-repo.

## Related Workspace Docs

- `agents/chatgpt.md`
- `agents/codex.md`
- `agents/workflow.md`
- `agents/task-template.md`
