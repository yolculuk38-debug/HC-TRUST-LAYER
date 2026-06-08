# HC Control Bot Report Workflow Trigger Note

> Status: trigger validation note
>
> Scope: documentation only
>
> Related workflow: `.github/workflows/hc-control-bot-report.yml`

## Purpose

This small documentation-only change exists to trigger the HC Control Bot report-only workflow after the workflow has already been merged to the default branch.

## Expected Observation

A pull request containing this file should allow maintainers to confirm whether the report-only workflow appears in the pull request checks.

Expected workflow name:

```text
HC Control Bot Report
```

Expected behavior:

- collect changed file path metadata;
- run the deterministic scanner;
- upload the JSON report artifact;
- avoid comments;
- avoid labels;
- avoid merge behavior;
- avoid LLM behavior.

## Boundary

This file does not change runtime code, schema, validators, records, generated artifacts, QR behavior, signing, federation, workflow configuration, labels, comments, or bot authority.

Human-supervised review remains the final authority.
