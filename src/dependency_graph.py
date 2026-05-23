"""HC:// dependency graph core."""

from __future__ import annotations


def _clean_dependencies(value: object) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, str):
        return {value.strip()} if value.strip() else set()
    try:
        return {str(item).strip() for item in value if str(item).strip()}  # type: ignore[operator]
    except TypeError:
        return set()


def build_dependency_node(*, node_id: str, depends_on: list[str] | None = None) -> dict:
    return {
        "node_id": node_id.strip(),
        "depends_on": sorted(_clean_dependencies(depends_on)),
    }


def find_ready_nodes(nodes: list[dict], completed: set[str]) -> list[str]:
    ready: list[str] = []
    for node in nodes:
        node_id = str(node.get("node_id", "")).strip()
        dependencies = _clean_dependencies(node.get("depends_on"))
        if node_id and node_id not in completed and dependencies.issubset(completed):
            ready.append(node_id)
    return sorted(ready)


def has_dependency_cycle(nodes: list[dict]) -> bool:
    graph = {
        str(node.get("node_id", "")).strip(): _clean_dependencies(node.get("depends_on"))
        for node in nodes
        if str(node.get("node_id", "")).strip()
    }
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node_id: str) -> bool:
        if node_id in visiting:
            return True
        if node_id in visited:
            return False
        visiting.add(node_id)
        for dep in graph.get(node_id, set()):
            if dep in graph and visit(dep):
                return True
        visiting.remove(node_id)
        visited.add(node_id)
        return False

    return any(visit(node_id) for node_id in graph)
