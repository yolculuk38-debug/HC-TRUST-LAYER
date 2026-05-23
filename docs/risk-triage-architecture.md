# Automated Risk Triage Architecture

## Detection Modules
- Duplicate detection (hash and near-duplicate heuristics).
- Malformed record detection (schema and semantic validation failures).
- Replay anomaly detection (stale or repeated signed events).

## Triage States
- `clear`: no active risk findings.
- `monitor`: low-severity findings requiring observation.
- `quarantine`: elevated risk; record isolated pending review.

## Risk Scoring
- Composite risk score from integrity, behavioral, and federation anomaly signals.
- Scores are explainable by component category.

## Spam Prevention
- Rate controls on repeated submissions.
- Reputation-aware throttling for low-trust senders.
- Signature and identity consistency checks.

## Modularity
Each detector publishes structured findings to a shared triage interface so policy engines can evolve independently.
