# HC Trust Engineer Report Quickstart

This quickstart shows how to run the local HC Trust Engineer report generator.

The generator is local, deterministic, and report-only.

It does not call a network, call an LLM, write to the repository, apply labels, assign users, request reviewers, approve, reject, merge, close, or claim legal truth.

## Run a clean docs example

```bash
python scripts/hc_trust_engineer_report.py examples/hc-trust-engineer/clean-docs-pr.json --pretty
```

Expected high-level result:

```text
mode: report_only
advisory_only: true
public_safe: true
truth_guarantee: false
recommended_next_action: continue
stop_reasons: []
```

## Run a protected-path example

```bash
python scripts/hc_trust_engineer_report.py examples/hc-trust-engineer/protected-path-pr.json --pretty
```

Expected high-level result:

```text
mode: report_only
advisory_only: true
public_safe: true
truth_guarantee: false
recommended_next_action: stop
stop_reasons includes: protected_paths_touched
```

## Input shape

A fixture may include:

```json
{
  "repository": "yolculuk38-debug/HC-TRUST-LAYER",
  "event_type": "pull_request",
  "target_number": 1000,
  "base_sha": "...",
  "head_sha": "...",
  "open_prs": [1000],
  "changed_files": ["docs/demo/example.md"],
  "checks": [
    {
      "name": "HC-TRUST-LAYER Validation",
      "status": "completed",
      "conclusion": "success"
    }
  ],
  "unresolved_threads": [],
  "missing_evidence": []
}
```

## Output boundary

The output is advisory evidence for repository operation. It is not an approval, rejection, merge decision, certification, production-readiness claim, or truth guarantee.

Human final authority remains required for repository decisions.
