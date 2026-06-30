# HC Operating Layer

HC-TRUST-LAYER onboarding guide for human contributors, ChatGPT, Codex, Copilot, Claude, Gemini, future autonomous agents, and other review participants working on HC:// verification infrastructure.

## Project Mission

HC-TRUST-LAYER is an open verification protocol and provenance infrastructure for HC:// records, review boundaries, and evidence-preserving workflows.

The repository defines a trust layer for record-based verification work. It organizes schemas, records, documentation, scripts, runtime code, and governance references so contributors can inspect provenance, preserve audit trails, and support human-supervised validation.

HC-TRUST-LAYER is not a substitute for reviewer judgment. Governance remains human-supervised, and agent output is advisory until validated through repository-defined checks and reviewer oversight.

## Repository Map

- `schema/`: Schema definitions and record-shape references. Treat these as canonical record boundary material.
- `records/`: Record examples and provenance-bearing artifacts. Preserve existing evidence and auditability.
- `docs/`: Architecture, governance, verification map, protocol graph, trust kernel, and operating-layer documentation.
- `scripts/`: Repository checks, validation helpers, report generators, and bounded maintenance utilities.
- `src/`: Runtime and library implementation surfaces for HC-TRUST-LAYER tooling.
- `.github/`: CI, workflow, governance, and review automation configuration.

## Trust Kernel

The trust kernel includes protected areas that affect record identity, provenance continuity, policy interpretation, signing expectations, federation behavior, validation semantics, or governance controls.

Protected and high-risk areas include:

- workflow, CI, automation, and bot-routing files such as `.github/workflows/**`
- schema, validator, runtime, and public verification surfaces such as `schema/**`, `validators/**`, and runtime code
- records, signatures, canonical artifacts, generated artifacts, and other evidence-bearing or derived surfaces
- policy, federation, signing, trust-anchor, and trust-kernel artifacts
- governance and project-control files that affect review boundaries or authority interpretation
- root ownership and operating-layer files such as `CODEOWNERS`, `AGENTS.md`, and `HC_BOOTSTRAP.md`

Touching these areas does not mean a PR is rejected. It means additional human review, explicit justification, and human-supervised validation are required before merge. Contributors and agents should explain why the protected path is touched, what evidence was checked, what tests were run, and whether behavior, authority, or trust boundary changed. CI green is evidence, not trust authority. Bot and AI comments are advisory only. Human maintainers make the final decision. Do not infer production guarantees from draft, advisory, or experimental material.

## Contributor Rules

Contributors MUST:

- preserve evidence
- avoid inventing facts
- preserve auditability
- keep changes minimal
- prefer documentation before architecture changes

Contributors MUST NOT:

- fabricate hashes
- fabricate signatures
- fabricate approvals
- bypass governance controls
- modify protected paths without justification

## Agent Rules

Agents should:

- inspect existing files first
- follow repository conventions
- avoid speculative implementation
- report uncertainty explicitly
- prefer REPORT ONLY investigations before major changes

Agents must preserve HC:// and HC-TRUST-LAYER terminology, keep work scoped and reviewable, and avoid claims of autonomous governance finality, forensic certainty, live federation guarantees, or production readiness unless those claims are implemented and validated in-repo.

## Current Development Phase

Current development is focused on:

- v0.1.0 stabilization
- governance hardening
- validation reliability
- documentation maturity
- operating layer development

This phase prioritizes clear review boundaries, reliable checks, concise documentation, and human-supervised validation over uncontrolled automation or architecture expansion.

## Preferred Workflow

1. Investigate
2. Report
3. Review
4. Implement
5. Validate
6. Merge

For non-trivial or trust-kernel-adjacent work, begin with a report that identifies affected files, uncertainty, expected impact, and required validation before implementation.

## Future Direction

Future HC-TRUST-LAYER work may include:

- Public Explorer
- Verification API
- Federation
- Trust scoring research
- Release evidence lifecycle

Future work should remain evidence-preserving, audit-friendly, human-reviewable, and aligned with HC:// verification map, protocol graph, provenance, and canonical record boundaries.
