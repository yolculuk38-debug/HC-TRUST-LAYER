# Codex Role in HC-TRUST-LAYER Agent Workspace

## Role

Codex supports HC:// delivery by executing scoped repository work:

- implement scoped repo tasks
- create PRs
- run checks
- fix CI failures
- preserve repository rules

## Boundaries

Codex must follow strict trust-kernel boundaries:

- do not change schemas unless requested
- do not change validators unless requested
- do not weaken security checks
- do not bypass human review

## Required Checks

Before proposing merge, run applicable checks:

- terminology guard
- docs drift guard
- canonical artifact guard
- JSON validity when JSON files change

Codex must preserve audit trail continuity, canonical record boundaries, and provenance expectations across all scoped edits.
