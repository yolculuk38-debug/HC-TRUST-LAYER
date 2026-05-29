"""Shared advisory runtime state containers for HC:// operational prototype."""

from hc_runtime.abuse_signals import AdvisoryAbuseSignalTracker
from hc_runtime.decision_engine import TrustStateDecisionEngine
from hc_runtime.events import RuntimeEventStore
from hc_runtime.runtime import FederationRelay, RuntimePolicyEngine, RuntimeQueueStore, ValidatorPipeline

EVENT_STORE = RuntimeEventStore()
PIPELINE = ValidatorPipeline()
DECISION_ENGINE = TrustStateDecisionEngine()
QUEUE_STORE = RuntimeQueueStore()
POLICY_ENGINE = RuntimePolicyEngine()
FEDERATION_RELAY = FederationRelay()
ABUSE_SIGNAL_TRACKER = AdvisoryAbuseSignalTracker()
