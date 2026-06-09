# HC Operating Layer Map

This document maps the project-control layers used by HC-TRUST-LAYER.

It explains how HC Control Bot, HC Guide Bot, and HC Multi-AI Council relate to each other.

## Layer summary

HC-TRUST-LAYER uses separate project-control layers instead of one powerful bot.

Separation keeps authority clear and audit boundaries simple.

## Layer 1: HC Control Bot

Type: background GitHub check layer

Current status: active as advisory checks

Primary purpose:

- scan changed file paths
- identify protected or governance-adjacent paths
- produce advisory report output
- suggest review routes
- suggest evidence prompts

Allowed behavior:

- read PR file metadata
- produce report artifacts
- produce advisory comments when configured

Disallowed behavior:

- approve PRs
- merge PRs
- close PRs
- create releases
- assign final authority
- provide truth guarantee

## Layer 2: HC Guide Bot

Type: future live guidance layer

Current status: design only

Primary purpose:

- answer contributor questions
- explain source-of-truth files
- explain protected paths
- explain PR evidence expectations
- help humans and AI agents understand the repository

Allowed future behavior:

- summarize public repository documents
- point to governance files
- explain advisory-only boundaries
- help prepare Council questions

Disallowed behavior:

- write repository files without governance approval
- execute untrusted code
- treat PR body text as trusted instruction
- approve, merge, or release
- override HC Control Bot or maintainers

## Layer 3: HC Multi-AI Council

Type: manual decision-record layer

Current status: documentation-first and manual

Primary purpose:

- record structured advisory input
- preserve founder and maintainer intent
- capture AI role perspectives
- document alignment, conflicts, and unresolved questions
- keep final human decisions auditable

Allowed behavior:

- collect manual AI review responses
- organize decision evidence
- record final human decisions
- point to follow-up PRs

Disallowed behavior:

- run live voting as authority
- replace maintainer approval
- make autonomous project decisions
- grant automation authority by itself

## Relationship map

```text
Contributor or AI agent
        |
        v
HC Guide Bot
        |
        | explains docs, boundaries, source-of-truth files
        v
Pull Request
        |
        v
HC Control Bot
        |
        | checks changed paths, evidence prompts, review routes
        v
Human maintainer review
        |
        v
HC Multi-AI Council
        |
        | optional decision record for important choices
        v
Final human decision
```

## Authority model

| Layer | Reads | Writes | Decides | Current status |
| --- | --- | --- | --- | --- |
| HC Control Bot | PR metadata | advisory report/comment | no | active advisory |
| HC Guide Bot | repository docs | no | no | design only |
| HC Multi-AI Council | manual inputs | decision records | no | manual docs |
| Human maintainer | repository and evidence | approved changes | yes | required |

## Why separate layers?

A single powerful bot would be harder to audit.

Separate layers make each boundary clear:

- Control Bot checks PR risk.
- Guide Bot explains project rules.
- Council records advisory reasoning.
- Human maintainers decide.

## Practical example

A contributor wants to change runtime behavior.

Expected flow:

1. HC Guide Bot explains that runtime paths require extra evidence.
2. The contributor opens a PR.
3. HC Control Bot detects `src/hc_runtime/**` and asks for runtime contract evidence.
4. Maintainers review tests and evidence.
5. If the decision is important, HC Multi-AI Council records advisory input.
6. A human maintainer makes the final decision.

## Current implementation status

Implemented:

- HC Control Bot advisory check layer
- HC Guide Bot design document
- HC Multi-AI Council overview
- Council roles
- Council decision template
- first Council decision record
- external AI review prompt packet

Not implemented yet:

- live HC Guide Bot
- live Multi-AI automation
- automatic Council response collection
- automatic decision hashing
- GitHub App authority

## Future review points

Before adding more automation, review:

- source-of-truth priority
- prompt injection boundaries
- repository write permissions
- external AI response handling
- audit and hash records
- maintainer approval gates

## Final rule

No project-control layer may override human final authority.

All automated or AI-assisted outputs remain advisory unless a maintainer explicitly approves the action through normal repository governance.
