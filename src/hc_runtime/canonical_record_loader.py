"""Deterministic canonical record loader for HC:// advisory runtime lookup."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from threading import Lock
from typing import Any

from hc_trust.verification import is_generated_artifact_file

APPROVED_CANONICAL_RECORD_DIRS: tuple[Path, ...] = (
    Path("records/pending"),
    Path("records/verified"),
    Path("records/archived"),
    Path("records/archive"),
)

MALFORMED_RECORD = object()
DUPLICATE_RECORD = object()


class _StrictRecordLoadError(Exception):
    pass


def _load_strict_record(path: Path) -> object:
    try:
        from hc_trust.canonicalization import CanonicalizationError, strict_json_load
    except ImportError as exc:
        raise _StrictRecordLoadError from exc

    try:
        with path.open(encoding="utf-8") as handle:
            return strict_json_load(handle)
    except CanonicalizationError as exc:
        raise _StrictRecordLoadError from exc


@dataclass(slots=True)
class CanonicalRecordLoader:
    """Load local canonical records from approved directories without granting trust."""

    root: Path = Path(".")
    approved_dirs: tuple[Path, ...] = APPROVED_CANONICAL_RECORD_DIRS
    _records: dict[str, object] = field(default_factory=dict, init=False)
    _malformed: dict[str, Path] = field(default_factory=dict, init=False)
    _duplicates: set[str] = field(default_factory=set, init=False)
    _loaded: bool = field(default=False, init=False)
    _load_lock: Any = field(default_factory=Lock, init=False, repr=False)

    def get(self, record_id: str, default: object | None = None) -> object | None:
        """Return one record, a malformed/duplicate marker, or the provided default."""

        with self._load_lock:
            self._ensure_loaded()
            if record_id in self._malformed:
                return MALFORMED_RECORD
            if record_id in self._duplicates:
                return DUPLICATE_RECORD
            if record_id in self._records:
                return self._records[record_id]
            return default

    def refresh(self) -> None:
        """Clear cached advisory lookup state so the next lookup reloads records."""

        with self._load_lock:
            self._records.clear()
            self._malformed.clear()
            self._duplicates.clear()
            self._loaded = False

    def _ensure_loaded(self) -> None:
        if self._loaded:
            return
        self._load()
        self._loaded = True

    def _load(self) -> None:
        for relative_dir in self.approved_dirs:
            try:
                directory = (self.root / relative_dir).resolve()
                directory.relative_to(self.root.resolve())
            except (ValueError, OSError, RuntimeError):
                continue
            if not directory.is_dir():
                continue
            for path in sorted(directory.rglob("*.json"), key=lambda candidate: candidate.as_posix()):
                if not self._is_approved_record_path(path=path, directory=directory):
                    continue
                record_id_hint = path.stem
                try:
                    record = _load_strict_record(path)
                except (OSError, UnicodeDecodeError, _StrictRecordLoadError):
                    self._malformed[record_id_hint] = path
                    continue
                if not isinstance(record, dict):
                    self._register(record_id_hint, MALFORMED_RECORD)
                    continue
                record_id = record.get("record_id")
                if isinstance(record_id, str) and record_id.strip():
                    self._register(record_id, record)
                else:
                    self._register(record_id_hint, record)

    def _register(self, record_id: str, record: object) -> None:
        if record_id in self._duplicates:
            return
        if record_id in self._records:
            self._records.pop(record_id)
            self._duplicates.add(record_id)
        else:
            self._records[record_id] = record

    def _is_approved_record_path(self, *, path: Path, directory: Path) -> bool:
        try:
            resolved = path.resolve()
            resolved.relative_to(directory)
            resolved.relative_to(self.root.resolve())
        except (ValueError, OSError, RuntimeError):
            return False
        return not (
            is_generated_artifact_file(path) or is_generated_artifact_file(resolved)
        )



def default_canonical_record_loader() -> CanonicalRecordLoader:
    """Build the default repository-local canonical record loader."""

    return CanonicalRecordLoader(root=Path(__file__).resolve().parents[2])
