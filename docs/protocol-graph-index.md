# HC-TRUST-LAYER Protocol Graph Index (Machine-readable Foundation)

## Purpose

`protocol-graph.json` provides a machine-readable companion to the verification map and protocol graph documentation in HC-TRUST-LAYER.

It is designed to help AI agents, future tooling, and contributors quickly discover core HC:// trust-kernel domains, documentation anchors, review sensitivity, and cross-component relationships.

## How AI Agents Should Use It

AI agents should treat `protocol-graph.json` as an orientation index before proposing edits.

Recommended usage pattern:

1. locate the dominant component scope for a requested change
2. open the listed `docs` references before drafting modifications
3. inspect `related_components` for cross-domain impact
4. honor `human_review_required` and `risk_level` when routing reviewers
5. preserve audit trail and provenance continuity in change summaries

This supports documentation-first change planning and reduces boundary drift across canonical record, validator, policy, signing, federation, and governance surfaces.

## How Contributors Should Use It

Contributors should use the index as a navigation and review aid:

- map a proposed change to one or more component IDs
- use component docs to confirm in-repo implementation status
- apply higher review rigor for high-risk trust-kernel domains
- include affected related components in PR impact notes

The index improves consistency between docs, review routing, and trust-kernel boundaries while keeping scope auditable.

## Advisory-Only Boundary (Not Runtime Enforcement)

This index is documentation metadata only.

It does not:

- change runtime behavior
- enforce validator logic
- alter schema contracts
- modify workflow gates
- replace human-supervised validation

Repository evidence and implemented checks remain the source of truth for merge decisions.

## Future Use

As HC-TRUST-LAYER evolves, this index can support:

- agent routing hints for reviewer escalation
- structured change-impact analysis across related components
- verification map tooling that can render trusted navigation views
- consistency checks between architecture docs and component metadata

Any future expansion remains subject to documentation-first review and explicit human-supervised validation.

## Related References

- `protocol-graph.json`
- `docs/protocol-graph-agent-context.md`
- `docs/verification-map.md`
- `AGENTS.md`
