# HC-TRUST-LAYER AI Collaboration and Contribution Workflow

## Purpose

This workflow defines how humans and AI systems contribute through one shared project backbone for HC-TRUST-LAYER.

The goal is governance clarity for verification infrastructure and provenance infrastructure work, with human-supervised validation, public audit trail discipline, and one task / one PR / one architectural purpose.

## Main Principle: Repository Source of Truth

For HC-TRUST-LAYER, the repository is the source of truth.

Chat memory, AI suggestions, screenshots, and external messages are not authoritative unless they are converted into repository records, documentation, issues, pull requests, or reviewed code changes.

Authoritative project state must remain repo-visible evidence.

## Contribution Roles

### Human Maintainer

Human maintainers retain final project authority:
- final decision authority
- merge authority
- release control
- governance approval
- conflict resolution

### ChatGPT

ChatGPT contribution scope:
- architecture planning
- PR sequencing
- terminology control
- risk analysis
- QA checklist design
- protocol consistency review

### Codex

Codex contribution scope:
- repo-wide implementation
- refactor
- automation
- test updates
- documentation updates tied to implementation
- consistency fixes

### Other AI Systems

Other AI systems contribution scope:
- research
- external comparison
- documentation review
- alternative design review
- stress testing assumptions

## AI Contribution Rules

- AI output is advisory until reviewed.
- No AI can be treated as final authority.
- No AI-generated claim should be accepted without repo-visible evidence.
- Every meaningful change must pass through PR review.
- Every PR must have one clear architectural purpose.
- Every PR must preserve HC-TRUST-LAYER terminology.
- Every PR must avoid hype language.
- Every PR must avoid truth-guarantee language.
- Every PR must preserve canonical record boundary rules.

## Pull Request Template

Use the PR self-audit template for every contribution: [`/.github/pull_request_template.md`](../.github/pull_request_template.md).

This template reinforces verification infrastructure, provenance, audit consistency, human-supervised validation, AI-assisted witness, public audit trail, and canonical record boundary checks before human review.

## Self-Audit Workflow for Every PR

Each PR should be checked against these questions:

- Does this strengthen the trust kernel?
- Does this preserve protocol terminology?
- Does this match the implementation map?
- Does this avoid duplicate systems?
- Does this separate canonical records from generated artifacts?
- Does this keep AI as assistant/witness, not authority?
- Does this improve verification, provenance, audit, or federation?
- Does this add implementation, or only expand docs?
- Does this create future maintenance risk?

## Contribution Pipeline

Standard flow:

Idea  
→ architecture check  
→ scoped PR task  
→ Codex implementation  
→ automated checks  
→ human review  
→ merge  
→ roadmap/update if needed

This keeps PR intent bounded and reviewable.

## AI Witness and Provenance Context

AI-assisted work may be captured as contribution context, but not as project authority.

AI systems may assist with analysis, drafting, implementation, and review. Their outputs may provide witness context, but final project authority remains with human maintainers and public repository evidence.

This model supports AI-assisted witness participation while keeping authoritative boundaries human-governed.

## Automation Roadmap (Planned)

The following items are planned workflow controls and should be treated as roadmap items unless explicitly marked implemented elsewhere:

- PR template checklist
- issue templates
- terminology check workflow
- canonical record boundary check
- docs drift check
- implementation map consistency check
- generated artifact exclusion check
- security policy check
- release checklist

## Risk Areas

Primary collaboration and governance risks:

- conflicting AI advice
- hallucinated implementation claims
- docs growing faster than code
- terminology drift
- duplicate architecture
- uncontrolled roadmap expansion
- trust score being misunderstood as truth score
- over-reliance on GitHub
- AI authority confusion

## Non-Goals

This workflow does not:

- give AI systems merge authority
- create autonomous governance
- guarantee correctness
- replace human review
- replace automated validation
- make HC-TRUST-LAYER a social AI club

## Terminology and Boundary Guardrails

Required baseline language for this workflow:

- Main brand: HC-TRUST-LAYER
- Protocol short name: HC://
- Historical/origin context only: Humanity Chain
- Preferred framing: verification infrastructure, provenance infrastructure, public audit trail, human-supervised validation, AI-assisted witness, repo-visible evidence, canonical record boundary

Avoid language that implies final truth authority, including:

- proves truth
- guarantees truth
- AI judge
- AI authority
- autonomous AI governance
- truth score
- world-changing claims

## Scope Discipline

This workflow is documentation-focused governance guidance.

It does not introduce new product features, validator behavior changes, or record schema changes.
