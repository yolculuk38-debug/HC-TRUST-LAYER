# HC-TRUST-LAYER Verification Map Index (Machine-readable Foundation)

## Purpose

`verification-map.json` is a machine-readable companion to `docs/verification-map.md` for HC-TRUST-LAYER and HC://.

It provides structured documentation metadata so agents and future tooling can map verification domains, identify related trust-kernel components, and route review attention with clearer provenance and audit trail continuity.

## How Agents Should Use `verification-map.json`

Agents should treat `verification-map.json` as a pre-edit orientation index:

1. identify the dominant section(s) for the requested change
2. open the listed `docs` references before proposing edits
3. inspect `related_components` for cross-domain impact
4. respect `risk_level` and `human_review_required` when recommending reviewers
5. preserve canonical terminology, provenance continuity, and human-supervised validation boundaries in summaries

Agent usage is advisory-only and must not be treated as autonomous approval.

## How Humans Should Review with the Index

Human reviewers should use the index to:

- confirm change scope against the relevant verification map sections
- verify that linked documentation reflects in-repo implementation status
- escalate high-risk trust-kernel impacts for explicit human-supervised validation
- ensure cross-component impacts are documented in PR notes

The repository remains the source of truth for merge decisions.

## Advisory-only Metadata (No Runtime Enforcement)

`verification-map.json` is documentation/index metadata only.

It does not:

- enforce runtime verification behavior
- change validator logic
- alter schema contracts
- modify CI/workflow policy gates
- replace reviewer oversight or human-supervised validation

## Future Use (Planned Direction)

As HC-TRUST-LAYER evolves, this structured index can support:

- explorer preflight context loading for safer change planning
- validator and policy-impact routing hints for documentation-first review
- protocol graph and verification map tooling alignment
- structured change-impact analysis across trust-kernel domains

Any future automation remains subject to explicit repository validation and reviewer oversight.

## Related References

- `verification-map.json`
- `docs/verification-map.md`
- `docs/protocol-graph-index.md`
- `docs/protocol-graph-agent-context.md`
- `docs/implementation-transition-plan.md`
- `AGENTS.md`
- `agents/README.md`

- `trust-kernel-index.json`
- `docs/trust-kernel-index.md`
