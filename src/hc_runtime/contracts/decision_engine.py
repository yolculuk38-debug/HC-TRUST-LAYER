"""Advisory trust-state decision engine for the HC:// reference runtime."""

from __future__ import annotations

from enum import StrEnum


class TrustState(StrEnum):
    ADVISORY = "ADVISORY"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    UNRESOLVED = "UNRESOLVED"
    DEGRADED = "DEGRADED"
    REPLAY_WARNING = "REPLAY_WARNING"


class TrustStateDecisionEngine:
    """Minimal trust-state classification and warning handling for advisory flow."""

    def classify(
        self,
        *,
        record_id: str,
        qr_input: str,
        schema_valid: bool,
        hash_verified: bool,
        continuity_ok: bool,
        replay_warning: bool,
    ) -> tuple[TrustState, list[str]]:
        warnings: list[str] = []

        if replay_warning:
            warnings.append("Replay warning detected in QR verification input.")
            state = TrustState.REPLAY_WARNING
        elif not continuity_ok:
            warnings.append("Continuity warning detected in advisory runtime flow.")
            state = TrustState.DEGRADED
        elif "degraded" in record_id.lower() or "degraded" in qr_input.lower():
            warnings.append("Runtime is operating in degraded advisory mode for this verification request.")
            state = TrustState.DEGRADED
        elif not schema_valid:
            warnings.append("Canonical schema verification was not performed or did not validate the record.")
            state = TrustState.UNRESOLVED
        elif not hash_verified:
            warnings.append("Canonical digest verification was not performed or did not match the expected digest.")
            state = TrustState.REVIEW_REQUIRED
        else:
            state = TrustState.ADVISORY

        if state is not TrustState.ADVISORY:
            warnings.append("Human-supervised validation is required before trust interpretation.")

        return state, self.public_safe_warnings(warnings)

    def public_safe_warnings(self, warnings: list[str]) -> list[str]:
        return [warning for warning in warnings if "private" not in warning.lower()]
