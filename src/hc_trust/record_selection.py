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


class RecordSelectionError(ValueError):
    """The caller has not identified one unambiguous canonical tree."""


def record_selection_context(search_path, *, repo_root=None):
    """Return an absolute lexical input path and its repository context.

    Explicit-root relative paths are relative to that root. Otherwise a single
    plausible records anchor is required; a bare directory is a repository root.
    Never resolve the input first: doing so would erase artifact/symlink aliases.
    """
    path = Path(search_path)
    if repo_root is not None:
        root = Path(repo_root).absolute()
        return (path if path.is_absolute() else root / path), root
    path = path.absolute()
    anchors = []
    for candidate in (path, *path.parents):
        if candidate.name != "records":
            continue
        tail = path.relative_to(candidate).parts
        if not tail or tail[0] in ALLOWED_RECORD_DIRS:
            anchors.append(candidate.parent)
    if len(anchors) > 1:
        raise RecordSelectionError("Ambiguous records tree; specify --repo-root.")
    return path, anchors[0] if anchors else (path if path.is_dir() else None)


def classify_record_file(file_path, *, repo_root):
    """Classify a contained canonical path as record/artifact, else outside."""
    if repo_root is None:
        return "outside"
    path = Path(file_path).absolute()
    root = Path(repo_root).absolute()
    try:
        relative = path.relative_to(root)
        parts = relative.parts
        if (len(parts) < 3 or parts[0] != "records"
                or parts[1] not in ALLOWED_RECORD_DIRS or ".." in parts
                or path.suffix != ".json"):
            return "outside"
        resolved_root = root.resolve(strict=True)
        directory = resolved_root / "records" / parts[1]
        if directory.resolve(strict=True) != directory:
            return "outside"
        resolved = path.resolve(strict=True)
        resolved.relative_to(directory)
        if not resolved.is_file():
            return "outside"
        if (is_generated_artifact_file(relative)
                or is_generated_artifact_file(resolved.relative_to(resolved_root))):
            return "artifact"
        return "record"
    except (ValueError, OSError, RuntimeError):
        return "outside"


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
