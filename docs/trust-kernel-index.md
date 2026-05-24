# HC-TRUST-LAYER Trust Kernel Index (Machine-readable Foundation)

## Purpose

`trust-kernel-index.json` is an advisory machine-readable trust kernel index for HC-TRUST-LAYER and HC://.

It links existing machine-readable protocol graph and verification map indexes into one navigation layer for agents, contributors, and future verification tooling.

## Relationship to `protocol-graph.json`

`protocol-graph.json` provides machine-readable protocol graph component metadata.

`trust-kernel-index.json` does not replace that index. It references and organizes it as part of a combined trust-kernel navigation surface.

## Relationship to `verification-map.json`

`verification-map.json` provides machine-readable verification map domain metadata.

`trust-kernel-index.json` links that verification map metadata with protocol graph metadata so cross-domain review routing and documentation-first orientation can be performed through one index entrypoint.

## How Agents Should Use the Index

Agents should treat `trust-kernel-index.json` as a pre-edit orientation and routing index:

1. open `project` and `source_of_truth` first
2. review `core_layers` and `high_risk_components` before proposing changes
3. apply `human_review_gates` and `agent_routing` to recommend reviewer scope
4. run or report `validation_commands` aligned with touched scope
5. preserve provenance, audit trail continuity, and human-supervised validation boundaries in change summaries

Agent use is advisory-only and does not constitute autonomous approval.

## How Humans Should Review Index Changes

Human reviewers should verify that trust-kernel index updates:

- preserve HC-TRUST-LAYER and HC:// terminology
- remain documentation/index only
- do not imply runtime enforcement, schema changes, validator changes, or workflow changes
- accurately reference repository source-of-truth documentation
- maintain cross-index consistency with `protocol-graph.json` and `verification-map.json`

## Advisory-only Metadata Boundary

`trust-kernel-index.json` is documentation metadata only.

It does not:

- enforce runtime verification behavior
- modify validator logic
- alter schema contracts
- change workflow gates
- claim production readiness

All non-trivial trust-kernel-impacting changes remain subject to explicit human-supervised validation.

## Future Use

This index can support future repository tooling in advisory mode, including:

- explorer preflight context loading
- CI consistency checks for documentation/index drift
- agent and contributor routing hints
- verification tooling entrypoint alignment across protocol graph and verification map surfaces

Any expanded automation remains subject to repository-defined checks and reviewer oversight.

## Related References

- `trust-kernel-index.json`
- `protocol-graph.json`
- `verification-map.json`
- `docs/protocol-graph-index.md`
- `docs/verification-map-index.md`
- `docs/protocol-graph-agent-context.md`
- `docs/implementation-transition-plan.md`
- `AGENTS.md`
- `agents/README.md`
- `docs/trust-pr-engine.md`
- `docs/trust-impact-analysis.md`
- `docs/verification-proposal-model.md`
- `docs/trust-review-workflow.md`
