# HC Engineer Command Surface Status

Status: advisory operating-layer checkpoint.

## Purpose

This document records the current HC Trust Engineer / HC Assistant command surface based on repository evidence after the HC Control Bot reviewer-role roadmap synchronization sequence.

It is documentation only. It does not add command behavior, workflow behavior, runtime behavior, repository-write authority, or decision authority.

## Source evidence

Current repository evidence shows:

- `docs/project-control/project-state.md` records the project as post-runtime stabilization / operating-layer refinement and states that HC Control Bot advisory reviewer-role suggestions and roadmap synchronization are complete through #824.
- `docs/project-control/next-actions.md` keeps future work in report-only mode unless new repository evidence or explicit authorization appears.
- `docs/project-control/operator-entry-map.md` points operators to the active assistant console issue and lists the HC Control Bot / HC Trust Engineer reference chain.
- `docs/project-control/hc-trust-engineer-command-interface.md` documents the implemented command surface.
- `scripts/hc_assistant_command.py` implements the deterministic non-LLM parser.

## Implemented command surface

The current local deterministic parser supports:

```text
/hc help
/hc status
/hc next
/hc evidence
/hc explain
/hc risks
/hc review
```

These commands are documented as available through the advisory issue-comment listener.

## Current implementation mode

The command surface is:

```text
local deterministic parser
machine-readable JSON output
static response maps and checklists only
issue and pull request comments beginning with /hc can trigger the listener
trusted default-branch checkout for command execution
no PR-branch code execution
```

## Explicit boundary

The command surface does not perform live repository inspection or authority-changing repository actions.

It does not claim truth, legal validity, forensic certainty, production readiness, or final review status.

It remains an advisory command surface that helps humans prepare evidence, understand risk categories, and preserve project-control discipline.

## Current safe interpretation

The current HC Engineer command surface is real but intentionally narrow.

It can:

```text
explain available commands
summarize static command-surface status
provide static next-action guidance
provide evidence checklist guidance
explain supported static topics
provide static risk checklist guidance
prepare a human-review checklist
```

It cannot:

```text
inspect a pull request diff
open work automatically
write repository files from commands
change issue or pull request state
make truth, legal, forensic, or production claims
```

## Recommended next expansion path

Any future expansion should remain staged:

1. Add documentation-only status checkpoints when repository evidence changes.
2. Add tests before expanding parser behavior.
3. Add live GitHub inspection only through a separately reviewed integration.
4. Keep default-branch trusted code execution only.
5. Keep pull request content untrusted.
6. Preserve advisory-only output.
7. Require explicit human approval before enabling any authority-changing automation.

## Human authority reminder

AI and automation may assist with routing, evidence collection, risk checklists, and status summaries.

Human maintainers retain final authority.

Trust the record, not the narrative.
