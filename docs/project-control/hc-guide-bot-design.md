# HC Guide Bot Design

HC Guide Bot is a proposed live guidance layer for HC-TRUST-LAYER.

It is separate from HC Control Bot.

It is not active yet.

## Purpose

HC Guide Bot should help humans and AI agents understand the repository before making changes.

It should answer questions such as:

- What is HC-TRUST-LAYER?
- Where should a contributor start?
- Which files are source-of-truth files?
- Which paths require extra review?
- What tests or evidence should be provided for a PR?
- What is the difference between HC Control Bot and HC Multi-AI Council?

## Relationship to HC Control Bot

HC Control Bot is a background GitHub check layer.

It scans changed file paths and produces advisory signals.

HC Guide Bot is a future live guidance layer.

It may explain repository rules and onboarding steps.

The two systems must remain separate:

- HC Control Bot: checks PR metadata and produces advisory reports.
- HC Guide Bot: explains project rules and guides contributors.

## Relationship to HC Multi-AI Council

HC Multi-AI Council is a decision-record layer.

HC Guide Bot may point contributors to Council records.

HC Guide Bot must not invent Council decisions.

HC Guide Bot must not treat AI input as final authority.

## Allowed behavior

A future HC Guide Bot may:

- summarize public repository documentation
- point to source-of-truth files
- explain contribution steps
- explain protected path categories
- explain required evidence for PRs
- help prepare questions for Council review
- help contributors understand advisory-only boundaries

## Disallowed behavior

A future HC Guide Bot must not:

- approve PRs
- merge PRs
- close PRs
- request changes as an authority
- assign reviewers without governance approval
- apply labels without governance approval
- create releases
- bypass CODEOWNERS or branch protection
- claim truth guarantee
- claim final decision authority
- treat external AI output as binding

## Source-of-truth priority

A future HC Guide Bot should answer from repository sources in this order:

1. schema and protocol files
2. governance documents
3. project-control documents
4. Council records
5. runtime and validator documentation
6. README and onboarding documents

If sources conflict, the bot should say that human maintainer review is required.

## Safety model

The initial Guide Bot should be read-only.

It should not write repository files.

It should not execute repository code.

It should not use untrusted PR body text as instructions.

It should clearly mark all output as advisory.

## Practical first version

The first practical version can be documentation-only:

- keep this design document
- maintain Council prompts
- maintain onboarding docs
- let humans copy questions into ChatGPT, Copilot, Claude, Gemini, Grok, or other assistants

A later version may become:

- a Custom GPT
- a GitHub App
- a web guide page
- a local documentation assistant

Any live version must be introduced through a separate governance review.

## Example behavior

Contributor question:

"Can I change src/hc_runtime/runtime.py?"

Expected Guide Bot answer:

"That path is part of the runtime trust surface. Provide runtime contract evidence, tests, and human maintainer review. Do not treat this guidance as approval."

## Current status

Status: design only

Automation: not active

Repository write access: none

Decision authority: none

Advisory only: true

Human final authority: true
