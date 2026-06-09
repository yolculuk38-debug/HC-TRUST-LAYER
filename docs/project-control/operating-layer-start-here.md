# HC Operating Layer Start Guide

This guide is a short entry point for contributors, reviewers, AI agents, and maintainers who need to understand the HC project-control layers.

It complements `docs/START_HERE.md`.

## Read this when

Read this guide if you are asking:

- Which HC bot does what?
- Is there a live guide bot?
- What is the difference between HC Control Bot and HC Guide Bot?
- What is HC Multi-AI Council?
- Who makes the final decision?

## Fast answer

HC-TRUST-LAYER separates project-control responsibilities into layers.

No single bot has full authority.

## Layer 1: HC Control Bot

Status: active as advisory GitHub checks.

Purpose:

- inspect changed PR file paths
- identify protected or governance-adjacent surfaces
- produce advisory reports
- suggest review routes and evidence prompts

It does not approve, merge, release, or make final decisions.

Main reference:

- `docs/project-control/hc-operating-layer-map.md`

## Layer 2: HC Guide Bot

Status: design only.

Purpose:

- future live guidance for humans and AI agents
- explain repository rules
- point to source-of-truth documents
- help contributors understand safe next steps

It is not active yet.

Main reference:

- `docs/project-control/hc-guide-bot-design.md`

## Layer 3: HC Multi-AI Council

Status: manual decision-record layer.

Purpose:

- collect structured advisory input
- preserve founder and maintainer intent
- record AI role perspectives
- document alignment, conflicts, and unresolved questions
- keep important decisions auditable

It does not vote as authority and does not replace maintainers.

Main references:

- `council/README.md`
- `council/roles.md`
- `council/decision-template.md`
- `council/records/HC-DEC-0001.md`
- `council/external-ai-review-prompts.md`

## Recommended reading path

For humans:

1. `README.md`
2. `docs/START_HERE.md`
3. `docs/project-control/hc-operating-layer-map.md`
4. `docs/project-control/hc-guide-bot-design.md`
5. `council/README.md`

For AI agents:

1. `AGENTS.md`
2. `HC_BOOTSTRAP.md`
3. `docs/START_HERE.md`
4. `docs/project-control/hc-operating-layer-map.md`
5. `council/roles.md`
6. `council/external-ai-review-prompts.md`

For maintainers:

1. `GOVERNANCE.md`
2. `docs/project-control/hc-operating-layer-map.md`
3. `council/records/HC-DEC-0001.md`
4. `council/decision-template.md`

## Authority boundary

All layers are advisory unless a human maintainer explicitly approves an action through normal repository governance.

Human final authority remains required for trust-critical decisions.

## Current safe next step

Collect external AI feedback using `council/external-ai-review-prompts.md`.

Then update `council/records/HC-DEC-0001.md` with summarized advisory inputs.
