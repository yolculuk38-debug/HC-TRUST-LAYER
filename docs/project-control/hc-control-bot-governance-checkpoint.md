# HC Control Bot Governance Checkpoint

This checkpoint summarizes the completed HC Control Bot governance phase.

## Completed governance block

The following governance and workflow clarifications are now in place:

- advanced capability gate
- advisory comment capability class clarification
- label allowlist policy
- reviewer routing policy
- duplicate report trigger fix
- check status guide

## Current approved behavior

HC Control Bot is an advisory reviewer.

It may produce deterministic path-based metadata.

It may publish a report check.

It may display advisory metadata in a single advisory comment when available.

## Not active

The following are not active:

- label application
- assignment
- reviewer requests
- approval decisions
- request-changes decisions
- merge actions
- close actions
- LLM authority
- GitHub App write authority

## Expected check model

A normal pull request may show:

- HC Control Bot Report
- HC Control Bot Advisory Comment

Duplicate report checks should be avoided by keeping report workflow triggers narrow.

## Next direction

After this checkpoint, the preferred next focus is runtime and protocol hardening.

Suggested next technical sequence:

1. telemetry payload hardening
2. replay and continuity edge-case tests
3. degraded runtime recovery tests
4. validator pipeline consistency tests
5. runtime to canonical schema/hash bridge planning
6. QR spoof protection layer

## Authority boundary

HC Control Bot supports maintainers.

It does not replace maintainers.

Human final authority remains unchanged.
