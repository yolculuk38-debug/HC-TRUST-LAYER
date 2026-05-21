from node_registry import NodeStatus, build_registry, validate_node_entry


def valid_node():
    return {
        "node_id": "node-1",
        "source_url": "https://example.org/hc",
        "public_key": "PUBKEY",
        "registered_at": "2026-05-21T00:00:00Z",
        "status": NodeStatus.ACTIVE,
        "verified": True,
    }


def test_valid_node_entry():
    result = validate_node_entry(valid_node())
    assert result["valid"] is True
    assert result["trusted"] is True


def test_invalid_node_protocol():
    node = valid_node()
    node["source_url"] = "http://unsafe.local"

    result = validate_node_entry(node)
    assert result["valid"] is False


def test_invalid_status():
    node = valid_node()
    node["status"] = "UNKNOWN"

    result = validate_node_entry(node)
    assert result["valid"] is False


def test_build_registry_filters_duplicates():
    node = valid_node()

    registry = build_registry([node, node])

    assert registry["node_count"] == 1
    assert registry["invalid_count"] == 1
