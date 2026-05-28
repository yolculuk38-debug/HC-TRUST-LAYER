# Public Trial Quickstart (Advisory Runtime)

> **Documentation Status**
> - **status:** ACTIVE
> - **scope:** Public-safe trial onboarding for HC-TRUST-LAYER advisory runtime evaluation.
> - **canonical relevance:** Non-canonical onboarding guidance; does not modify schema, validators, policy, or runtime semantics.
> - **runtime relevance:** High for evaluator onboarding and safe trial execution boundaries.

This quickstart helps external users run a **public-safe trial** of the HC-TRUST-LAYER advisory runtime.

HC:// trial outputs are **advisory-only** and must not be interpreted as objective-truth verification.

## Safety and Scope Guardrails

Before running the trial, treat these as hard requirements:

- **advisory-only:** outputs are verification signals for review, not final truth.
- **public-safe:** use non-sensitive sample or local test data only.
- **truth_guarantee=false:** HC:// does not provide objective-truth finality.
- **human-supervised validation:** consequential interpretation requires human reviewers.
- **not production-ready:** do not represent HC-TRUST-LAYER as production-ready trust arbitration.

## 1) Install Dependencies

```bash
pip install -r requirements.txt
```

## 2) Run Runtime Tests

```bash
PYTHONPATH=src pytest -q tests/test_hc_runtime_app.py tests/test_hc_runtime_pipeline.py tests/test_hc_runtime_response_contracts.py
```

## 3) Safe Trial Flow

Use this minimal trial flow to keep evaluation scoped and auditable:

1. **Run tests** to confirm local baseline behavior.
2. **Inspect docs** to understand HC:// trust boundaries and limitations.
3. **Review runtime contracts** so outputs are interpreted within declared response semantics.
4. **Do not submit sensitive data** in trial flows, examples, or screenshots.

## 4) Recommended Supporting References

- Runtime limits and boundaries: [`docs/limitations-and-risks.md`](limitations-and-risks.md)
- Verification map orientation: [`docs/verification-map.md`](verification-map.md)
- Protocol graph orientation: [`docs/protocol-graph.md`](protocol-graph.md)
- Trust kernel orientation: [`docs/trust-kernel.md`](trust-kernel.md)
- Runtime contract tests:
  - [`tests/test_hc_runtime_app.py`](../tests/test_hc_runtime_app.py)
  - [`tests/test_hc_runtime_pipeline.py`](../tests/test_hc_runtime_pipeline.py)
  - [`tests/test_hc_runtime_response_contracts.py`](../tests/test_hc_runtime_response_contracts.py)

## 5) Trial Interpretation Reminder

HC-TRUST-LAYER trial runs support reproducible, auditable review workflows and provenance analysis.
They do **not** establish objective truth, autonomous governance finality, or production trust guarantees.
All consequential decisions should remain within human-supervised validation workflows.
