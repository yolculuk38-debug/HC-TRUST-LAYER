# HC Control Bot Report Artifact Validation

This note exists to validate that the HC Control Bot Report workflow remains visible on pull requests and produces report logs/artifacts after the trigger visibility fix.

## Scope

Documentation-only validation trigger.

No runtime, schema, validator, record, policy, or workflow behavior is changed by this file.

## Expected checks

A pull request containing this file should show the HC Control Bot Report check.

The report workflow should remain:

- advisory-only
- public-safe
- deterministic
- artifact/log based
- non-LLM
- non-approving
- non-merging
- non-labeling
- non-commenting

## Safety boundary

This validation note must not be treated as evidence that the bot makes decisions. Human review remains the final authority.
