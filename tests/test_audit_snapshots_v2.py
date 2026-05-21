from audit_snapshots_v2 import (
    GENESIS_PARENT,
    create_snapshot,
    verify_snapshot,
    verify_snapshot_chain,
)


def test_valid_snapshot():
    snapshot = create_snapshot(
        "SNAP-1",
        ["hash-a", "hash-b"],
        "2026-05-21T00:00:00Z",
    )

    result = verify_snapshot(snapshot)
    assert result["verified"] is True


def test_tampered_snapshot_detection():
    snapshot = create_snapshot(
        "SNAP-1",
        ["hash-a"],
        "2026-05-21T00:00:00Z",
    )

    snapshot["record_hashes"].append("tampered")

    result = verify_snapshot(snapshot)
    assert result["verified"] is False


def test_valid_snapshot_chain():
    snap1 = create_snapshot(
        "SNAP-1",
        ["a"],
        "2026-05-21T00:00:00Z",
        parent_snapshot_hash=GENESIS_PARENT,
    )

    snap2 = create_snapshot(
        "SNAP-2",
        ["b"],
        "2026-05-21T01:00:00Z",
        parent_snapshot_hash=snap1["snapshot_hash"],
    )

    result = verify_snapshot_chain([snap1, snap2])
    assert result["verified"] is True


def test_snapshot_chain_parent_mismatch():
    snap1 = create_snapshot(
        "SNAP-1",
        ["a"],
        "2026-05-21T00:00:00Z",
    )

    snap2 = create_snapshot(
        "SNAP-2",
        ["b"],
        "2026-05-21T01:00:00Z",
        parent_snapshot_hash="WRONG",
    )

    result = verify_snapshot_chain([snap1, snap2])
    assert result["verified"] is False
