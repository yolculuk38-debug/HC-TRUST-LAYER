# HC Control Bot Report Workflow Validation

> Status: validation note
>
> Scope: documentation only
>
> Related workflow: `.github/workflows/hc-control-bot-report.yml`

## Purpose

This note exists to validate the first report-only HC Control Bot workflow after its initial merge.

The workflow is expected to run on pull requests and produce a report artifact from changed file path metadata.

## Expected Behavior

The report workflow should:

- check out the trusted base revision;
- collect changed file paths through GitHub pull request file metadata;
- run `scripts/hc_control_bot.py` against those paths;
- upload `hc-control-bot-report.json` as an artifact;
- avoid pull request comments;
- avoid labels;
- avoid merge behavior;
- avoid LLM integration.

## Validation Boundary

This file does not implement code, scripts, workflows, runtime behavior, validators, schemas, records, QR behavior, signing, federation, generated artifacts, labels, comments, or bot automation.

It only provides a small documentation-only pull request so the report-only workflow can be observed safely.

## Review Notes

Expected scanner classification for this pull request:

```text
protected_paths_touched:
- docs/project-control/hc-control-bot-report-workflow-validation.md

human_review_required: true
advisory_only: true
public_safe: true
truth_guarantee: false
evidence_source: changed file path metadata only
```

The protected-path match is advisory only. Human-supervised review remains the final authority.
