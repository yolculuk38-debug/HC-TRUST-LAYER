"""Deterministic canonical record loader for HC:// advisory runtime lookup."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
APPROVED_CANONICAL_RECORD_DIRS: tuple[Path, ...] = (
    Path("records/pending"),
    Path("records/verified"),
    Path("records/archived"),
)

IGNORED_ARTIFACT_MARKERS: tuple[str, ...] = (
    "generated",
    "index",
    "cache",
    "export",
)

MALFORMED_RECORD = object()


@dataclass(slots=True)
class CanonicalRecordLoader:
    """Load local canonical records from approved directories without granting trust."""

    root: Path = Path(".")
    approved_dirs: tuple[Path, ...] = APPROVED_CANONICAL_RECORD_DIRS
    _records: dict[str, object] = field(default_factory=dict, init=False)
    _malformed: dict[str, Path] = field(default_factory=dict, init=False)
    _loaded: bool = field(default=False, init=False)

    def get(self, record_id: str, default: object | None = None) -> object | None:
        """Return a canonical record by id, a malformed marker, or the provided default."""

        self._ensure_loaded()
        if record_id in self._records:
            return self._records[record_id]
        if record_id in self._malformed:
            return MALFORMED_RECORD
        return default

    def refresh(self) -> None:
        """Clear cached advisory lookup state so the next lookup reloads records."""

        self._records.clear()
        self._malformed.clear()
        self._loaded = False

    def _ensure_loaded(self) -> None:
        if self._loaded:
            return
        self._load()
        self._loaded = True

    def _load(self) -> None:
        for relative_dir in self.approved_dirs:
            directory = (self.root / relative_dir).resolve()
            if not directory.is_dir():
                continue
            for path in sorted(directory.rglob("*.json"), key=lambda candidate: candidate.as_posix()):
                if not self._is_approved_record_path(path=path, directory=directory):
                    continue
                record_id_hint = path.stem
                try:
                    record = json.loads(path.read_text(encoding="utf-8"))
                except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                    self._malformed[record_id_hint] = path
                    continue
                if not isinstance(record, dict):
                    self._records.setdefault(record_id_hint, MALFORMED_RECORD)
                    continue
                record_id = record.get("record_id")
                if isinstance(record_id, str) and record_id.strip():
                    self._records.setdefault(record_id, record)
                else:
                    self._records.setdefault(record_id_hint, record)

    def _is_approved_record_path(self, *, path: Path, directory: Path) -> bool:
        try:
            path.relative_to(directory)
        except ValueError:
            return False
        lowered_parts = {part.lower() for part in path.parts}
        lowered_name = path.name.lower()
        if lowered_name == "explorer_index.json":
            return False
        if any(marker in lowered_parts for marker in IGNORED_ARTIFACT_MARKERS):
            return False
        return not any(marker in lowered_name for marker in IGNORED_ARTIFACT_MARKERS)


def default_canonical_record_loader() -> CanonicalRecordLoader:
    """Build the default repository-local canonical record loader."""

    return CanonicalRecordLoader(root=Path(__file__).resolve().parents[2])
