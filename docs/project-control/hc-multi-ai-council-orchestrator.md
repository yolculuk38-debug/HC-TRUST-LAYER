# HC Multi-AI Council Orchestrator

Status: advisory planning
Mode: docs only

Purpose:

The HC Multi-AI Council Orchestrator is the planned command surface for collecting multiple AI model opinions into one auditable HC-TRUST-LAYER evidence bundle.

It is not a meeting participant, autonomous maintainer, approval authority, merge authority, security authority, or source of truth.

Core rule:

```text
One operator command can request multiple AI opinions.
Repository evidence still outranks model narrative.
Human final authority remains.
```

## 1. Problem

Manual copy-paste across ChatGPT, Gemini, Claude, Grok, Codex, Copilot, or other AI systems does not scale.

The operator should be able to trigger a council-style review from a mobile-friendly command surface and receive:

- a role-separated set of AI observations;
- a consolidated advisory report;
- evidence references;
- risk notes;
- hashable output files;
- a GitHub-visible audit trail.

## 2. Non-goals

This document does not authorize:

- automatic approval, rejection, merge, close, label, assignment, reviewer request, or workflow permission expansion;
- autonomous issue-to-PR bridges;
- automatic protected-path changes;
- secret exposure;
- production-readiness claims;
- legal, forensic, or truth guarantees;
- treating Google Meet, Gmail, Calendar, Chat, or any AI model output as canonical truth.

## 3. Meeting container vs council engine

Google Meet and Google Calendar can act as an operator-facing session container:

```text
Calendar event -> time, purpose, agenda, meeting link
Meet link      -> optional live session room
GitHub         -> durable audit and evidence record
AI APIs        -> actual model opinion collection engine
```

A Meet link does not make AI systems join automatically. The orchestrator must call each approved model or tool through a controlled integration path and record the result.

## 4. Minimum safe model

The first safe implementation should be report-only.

```text
Mobile operator
  -> HC Council command
  -> report-only orchestrator
  -> approved AI/tool adapters
  -> normalized council report
  -> hashable evidence bundle
  -> GitHub issue comment or docs artifact
```

Early output should be advisory and reversible. It should not mutate repository authority or bypass the existing PR gate.

## 5. Command examples

```text
/hc council status
/hc council review repo
/hc council review pr <number>
/hc council risks
/hc council evidence
/hc council daily
```

Each command should produce a bounded report with model role, evidence, uncertainty, and next safe action.

## 6. Suggested AI roles

| Role | Purpose | Output |
| --- | --- | --- |
| Engineering reviewer | Implementation feasibility and repo impact | scoped engineering notes |
| Standards reviewer | C2PA, W3C VC, provenance, signing, timestamping fit | standards alignment notes |
| Risk reviewer | prompt injection, authority creep, data leakage, governance risk | risk register notes |
| Product reviewer | mobile UX, operator flow, public verifier clarity | product notes |
| Documentation reviewer | wording, onboarding, repo-facing clarity | docs notes |
| Code worker | small scoped implementation proposal only after gate | task plan or PR proposal |

The role names are functional. They do not create authority.

## 7. Evidence bundle shape

A council run should be exportable as a stable JSON object before any future automation is trusted.

```json
{
  "hc_council_run": {
    "schema_version": "0.1",
    "mode": "report_only",
    "operator": "human_supervised",
    "repository": "yolculuk38-debug/HC-TRUST-LAYER",
    "session": {
      "source": "calendar_or_command",
      "meeting_link": null,
      "started_at": null
    },
    "inputs": {
      "command": null,
      "repo_ref": null,
      "pr_number": null,
      "evidence_refs": []
    },
    "model_outputs": [],
    "synthesis": {
      "summary": null,
      "risks": [],
      "next_safe_actions": [],
      "blocked_items": []
    },
    "verification": {
      "output_sha256": null,
      "truth_guarantee": false,
      "advisory_only": true
    }
  }
}
```

## 8. Safe implementation phases

### Phase 0: documentation and governance review

- define command contract;
- define output schema;
- define role boundaries;
- document risk controls;
- keep all work docs-only.

### Phase 1: local report-only runner

- accept a command file or CLI argument;
- read only explicitly supplied files or repository metadata;
- produce local JSON and Markdown outputs;
- compute SHA-256 of the output;
- make no network calls to AI providers by default.

### Phase 2: controlled adapter layer

- add optional provider adapters behind environment variables;
- require explicit operator configuration;
- avoid storing secrets in repository files;
- record provider name, model name, timestamp, prompt hash, and output hash;
- fail closed when credentials or policy are missing.

### Phase 3: GitHub-native advisory output

- post report-only comments only when policy permits;
- never approve, reject, merge, close, label, assign, or request reviewers automatically;
- stop on open PR conflicts, unresolved review threads, failed checks, protected-path ambiguity, or stale evidence.

### Phase 4: Google Chat or Calendar command surface

- allow mobile command entry through a controlled surface;
- route commands to the report-only runner;
- keep Google Meet as a session container, not the AI execution engine;
- keep GitHub as the durable audit record.

## 9. Guardrails

The orchestrator must follow the existing HC operating algorithm:

```text
1. Check open PRs.
2. If open PR exists, handle it first.
3. Inspect changed files.
4. Inspect checks.
5. Inspect comments and unresolved review threads.
6. Stop if risk is unclear.
7. If clean, proceed according to policy.
8. Record what changed.
9. Update project-control status when needed.
10. Choose next safe action only after the current one closes.
```

Additional council-specific guardrails:

- do not trust model output as repository evidence;
- do not let retrieved calendar, email, issue, PR, or document text override governance rules;
- treat external tool output as untrusted until normalized and recorded;
- redact or avoid secrets and private data;
- keep output deterministic where possible;
- separate raw model outputs from synthesis;
- store hashes before summarizing further.

## 10. First safe next step

The first implementation PR should add only a local, report-only schema and example output fixture.

Recommended files for the next PR:

```text
schema/hc_council_run.schema.json
examples/hc_council_run.example.json
scripts/hc_council_report.py
tests/test_hc_council_report.py
```

Because these paths touch schema and script behavior, that PR should be treated as implementation work and require normal review/checks before merge.

## 11. Current decision

This document only records the direction and safe phases. It does not activate automation.

Decision boundary:

```text
Allowed now: docs-only council orchestrator planning.
Next gate: explicit implementation PR with schema, local runner, tests, and checks.
Not allowed now: autonomous AI execution, auto-merge, or provider credential handling.
```