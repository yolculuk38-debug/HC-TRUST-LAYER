# CodeQL Default Setup Boundary

## Status

The repository currently relies on GitHub CodeQL default setup for code scanning.

A new advanced CodeQL workflow must not be added while default setup remains enabled.

## Reason

GitHub rejects CodeQL SARIF uploads from advanced configurations when CodeQL default setup is enabled. This can make a pull request look like a workflow or permissions hardening change while actually introducing a conflicting CodeQL configuration.

## Operator rule

Do not add `.github/workflows/codeql.yml` or another advanced CodeQL analysis workflow unless a separate governance and repository-settings decision intentionally disables CodeQL default setup first.

## Allowed immediate action

For transient CodeQL API rate-limit failures, retry the failed CodeQL check after the rate-limit window resets.

## Not allowed in this boundary

- disabling or weakening CodeQL scanning
- adding PATs, `CODEQL_TOKEN`, secrets, or credential handling
- adding auto-merge, approve, close, label, assignment, or reviewer authority
- mixing repository settings changes with unrelated PR scope

## Future decision path

If the project later chooses advanced CodeQL setup, it must be handled as a separate protected-path change after the default setup decision is documented and performed through repository settings.
