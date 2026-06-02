# HC Operating Layer v0.1 Bootstrap

HC_BOOTSTRAP.md is the first operational entrypoint for humans, ChatGPT, Codex, Copilot, future autonomous agents, the future HC Guide Bot, the future HC Control Bot, and external contributors working in HC-TRUST-LAYER.

This file starts the repository-native operating layer for shift-ledger style project continuity. It does not create runtime behavior, governance automation, security guarantees, or production-readiness claims. It is advisory documentation for safer project handoff, review, and planning.

## Required startup sequence

Before proposing or performing work, read these sources in order:

1. `AGENTS.md`
2. `docs/project-control/project-state.md`
3. `docs/project-control/agent-operating-model.md`
4. `docs/project-control/task-ledger.md`
5. `docs/project-control/next-actions.md`

Repository state is the source of truth. Do not rely on chat memory alone.

## Operating rules

- Treat an issue as a work order.
- Treat an agent as an operator.
- Treat a tool as a machine.
- Treat a PR as a production batch.
- Treat a commit hash as a task barcode.
- Treat CI checks as quality control.
- Treat the task ledger as the shift ledger.
- Treat project state as the shift handoff summary.
- Treat a future `hc_context` JSON file as TREX-like machine-readable project memory.
- Treat the future HC Guide Bot as a shift guide and onboarding assistant.
- Treat the future HC Control Bot as a risk and control officer.
- Treat human review as the supervisor decision gate.

## Continuity rules

- Do not repeat merged or abandoned work.
- Do not reuse work marked closed, conflicted, or do-not-repeat.
- Cross-check proposed work against repository evidence, including the task ledger, project state, related PRs, changed files, checks, and review decisions.
- Preserve an evidence bundle for any completed task.
- Use agent check-in before starting work and agent checkout before handing off work.

## Trust and authority boundaries

- Human-supervised validation is required for trust-kernel-sensitive changes.
- Preserve advisory-only semantics.
- Do not claim production readiness.
- Do not claim truth finality.
- Do not claim security guarantees.
- Do not claim autonomous governance.
- Do not modify protected path boundaries unless the task explicitly authorizes that scope and reviewer expectations are satisfied.

Protected path boundaries include runtime-sensitive, schema, validator, workflow, records, signing, federation, policy, trust kernel, protocol graph, verification map, and governance-enforcement surfaces as defined by repository instructions and review rules.
