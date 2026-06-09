# HC Control Bot Advisory Reviewer Checkpoint

This checkpoint records the current HC Control Bot advisory reviewer state.

## Current capability

HC Control Bot can produce advisory-only metadata from changed file paths:

- protected paths touched
- governance-adjacent paths touched
- generated artifacts observed
- warnings
- evidence prompts
- review routes
- review priority
- suggested labels

The advisory comment workflow can display those fields when comment writing is available.

## Safety boundary

HC Control Bot does not apply labels.

HC Control Bot does not assign reviewers or maintainers.

HC Control Bot does not approve pull requests.

HC Control Bot does not request changes.

HC Control Bot does not merge pull requests.

HC Control Bot does not use an LLM for this path-scanning behavior.

HC Control Bot uses changed file path metadata only for this deterministic advisory result.

## Operating rule

The bot output is advisory.

Human maintainers keep final authority.

Generated artifacts are not canonical records by default.

Protected and trust-kernel-adjacent paths require human review.

## Next safe options

- keep the bot at advisory reviewer level
- add documentation for maintainers on reading bot comments
- add report artifact examples
- defer GitHub App, assignment, approval, and LLM memory features until separate governance approval
