"""HC:// governance voting core."""

from __future__ import annotations


def build_vote(*, voter_id: str, proposal_id: str, decision: str, weight: int = 1) -> dict:
    return {
        "voter_id": voter_id.strip(),
        "proposal_id": proposal_id.strip(),
        "decision": decision.strip().upper(),
        "weight": max(0, int(weight)),
    }


def tally_votes(votes: list[dict]) -> dict:
    totals: dict[str, int] = {}
    for vote in votes:
        decision = vote.get("decision", "UNKNOWN")
        totals[decision] = totals.get(decision, 0) + int(vote.get("weight", 0))
    return {"vote_totals": totals}
