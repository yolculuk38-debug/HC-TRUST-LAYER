"""Shared canonical record directory and generated-artifact selection rules."""

from pathlib import Path

# Include the documented legacy archive spelling without migrating evidence.
ALLOWED_RECORD_DIRS = ("pending", "verified", "archived", "archive")


GENERATED_ARTIFACT_NAMES = frozenset({
    "explorer_index.json", "generated_index.json", "index.json", "manifest.json",
    "cache.json", "export.json", "generated.json",
})
GENERATED_ARTIFACT_SUFFIXES = tuple(
    f"{delimiter}{kind}.json"
    for delimiter in ("-", "_")
    for kind in ("index", "manifest", "cache", "export", "generated")
)
GENERATED_ARTIFACT_DIRS = frozenset({"generated", "cache", "export", "exports"})


def is_generated_artifact_file(file_path: str | Path) -> bool:
    """Recognize reserved artifacts, never arbitrary words inside record IDs."""
    file_path = Path(file_path)
    parts = file_path.parts
    if "records" in parts:
        parts = parts[parts.index("records") + 1:]
    return (
        file_path.name.lower() in GENERATED_ARTIFACT_NAMES
        or file_path.name.lower().endswith(GENERATED_ARTIFACT_SUFFIXES)
        or any(part.lower() in GENERATED_ARTIFACT_DIRS for part in parts[:-1])
    )
