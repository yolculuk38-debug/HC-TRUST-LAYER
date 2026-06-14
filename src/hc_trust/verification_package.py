"""Local HC:// verification package hash verifier.

This module implements the first usable verification-package core:
manifest-listed file existence and SHA-256 integrity checks.

It is intentionally local-only and advisory-only. It verifies package integrity,
not legal truth, QR authenticity, signature validity, witness authority, timestamp
authority, or production readiness.
"""

from __future__ import annotations

from datetime import datetime
import hashlib
import json
from pathlib import Path
from typing import Any

VERIFICATION_PACKAGE_HASH_CORE_VERSION = "HC-VERIFICATION-PACKAGE-HASH-CORE-V1"
SUPPORTED_DIGEST_ALGORITHMS = {"sha256"}
ISSUER_PROOF_REQUIRED_FIELDS = ("issuer", "statement")
TIMESTAMP_PROOF_REQUIRED_FIELDS = ("claimed_at", "subject_sha256")
WITNESS_PROOF_REQUIRED_FIELDS = ("witness_id", "statement", "subject_sha256")


class VerificationPackageStatus:
    VERIFIED = "VERIFIED"
    INVALID = "INVALID"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"


def verify_verification_package(package_path: str | Path) -> dict[str, Any]:
    """Verify a local verification package directory against manifest digests.

    Expected minimal manifest shape::

        {
          "package_id": "HC-PKG-...",
          "schema_version": "...",
          "record_id": "HC-...",
          "files": [
            {"path": "metadata/source-info.json", "sha256": "..."}
          ]
        }

    Optional issuer evidence shape::

        {
          "issuer_proof": {"path": "issuer-proof.json", "sha256": "..."}
        }

    Optional timestamp evidence shape::

        {
          "timestamp_proof": {"path": "timestamp-proof.json", "sha256": "..."}
        }

    Optional witness evidence shape::

        {
          "witness_proof": {"path": "witness-proof.json", "sha256": "..."}
        }

    Supported file entries may use ``sha256``, ``digest`` with
    ``algorithm: sha256``, or ``hash`` with ``algorithm: sha256``.
    """

    package_root = Path(package_path)
    manifest_path = package_root / "manifest.json"
    warnings: list[str] = []
    missing_evidence: list[str] = []
    conflicting_evidence: list[str] = []
    file_results: list[dict[str, Any]] = []
    issuer_proof = _issuer_proof_not_provided()
    timestamp_proof = _timestamp_proof_not_provided()
    witness_proof = _witness_proof_not_provided()

    if not package_root.exists():
        missing_evidence.append("package_path_missing")
        return _build_response(
            status=VerificationPackageStatus.INVALID,
            package_root=package_root,
            manifest_path=manifest_path,
            files=file_results,
            issuer_proof=issuer_proof,
            timestamp_proof=timestamp_proof,
            witness_proof=witness_proof,
            missing_evidence=missing_evidence,
            conflicting_evidence=conflicting_evidence,
            warnings=warnings,
        )

    if not package_root.is_dir():
        conflicting_evidence.append("package_path_not_directory")
        return _build_response(
            status=VerificationPackageStatus.INVALID,
            package_root=package_root,
            manifest_path=manifest_path,
            files=file_results,
            issuer_proof=issuer_proof,
            timestamp_proof=timestamp_proof,
            witness_proof=witness_proof,
            missing_evidence=missing_evidence,
            conflicting_evidence=conflicting_evidence,
            warnings=warnings,
        )

    try:
        package_root_resolved = package_root.resolve(strict=True)
    except OSError:
        conflicting_evidence.append("package_path_unresolvable")
        return _build_response(
            status=VerificationPackageStatus.INVALID,
            package_root=package_root,
            manifest_path=manifest_path,
            files=file_results,
            issuer_proof=issuer_proof,
            timestamp_proof=timestamp_proof,
            witness_proof=witness_proof,
            missing_evidence=missing_evidence,
            conflicting_evidence=conflicting_evidence,
            warnings=warnings,
        )

    manifest = _load_manifest(manifest_path, missing_evidence, conflicting_evidence)
    if manifest is None:
        return _build_response(
            status=VerificationPackageStatus.INVALID,
            package_root=package_root,
            manifest_path=manifest_path,
            files=file_results,
            issuer_proof=issuer_proof,
            timestamp_proof=timestamp_proof,
            witness_proof=witness_proof,
            missing_evidence=missing_evidence,
            conflicting_evidence=conflicting_evidence,
            warnings=warnings,
        )

    files = manifest.get("files")
    if not isinstance(files, list):
        missing_evidence.append("manifest_files_list_missing")
        return _build_response(
            status=VerificationPackageStatus.INVALID,
            package_root=package_root,
            manifest_path=manifest_path,
            files=file_results,
            issuer_proof=issuer_proof,
            timestamp_proof=timestamp_proof,
            witness_proof=witness_proof,
            missing_evidence=missing_evidence,
            conflicting_evidence=conflicting_evidence,
            warnings=warnings,
            manifest=manifest,
        )

    if not files:
        warnings.append("manifest_files_list_empty")

    for entry in files:
        file_results.append(
            _verify_manifest_file_entry(
                package_root=package_root,
                package_root_resolved=package_root_resolved,
                entry=entry,
                missing_evidence=missing_evidence,
                conflicting_evidence=conflicting_evidence,
                warnings=warnings,
            )
        )

    issuer_proof = _verify_issuer_proof_entry(
        package_root=package_root,
        package_root_resolved=package_root_resolved,
        entry=manifest.get("issuer_proof"),
        missing_evidence=missing_evidence,
        conflicting_evidence=conflicting_evidence,
        warnings=warnings,
    )
    timestamp_proof = _verify_timestamp_proof_entry(
        package_root=package_root,
        package_root_resolved=package_root_resolved,
        entry=manifest.get("timestamp_proof"),
        missing_evidence=missing_evidence,
        conflicting_evidence=conflicting_evidence,
        warnings=warnings,
    )
    witness_proof = _verify_witness_proof_entry(
        package_root=package_root,
        package_root_resolved=package_root_resolved,
        entry=manifest.get("witness_proof"),
        local_subject_sha256s=_collect_local_subject_sha256s(manifest, file_results),
        missing_evidence=missing_evidence,
        conflicting_evidence=conflicting_evidence,
        warnings=warnings,
    )

    if conflicting_evidence or missing_evidence:
        status = VerificationPackageStatus.INVALID
    elif warnings or not files:
        status = VerificationPackageStatus.REVIEW_REQUIRED
    else:
        status = VerificationPackageStatus.VERIFIED

    return _build_response(
        status=status,
        package_root=package_root,
        manifest_path=manifest_path,
        files=file_results,
        issuer_proof=issuer_proof,
        timestamp_proof=timestamp_proof,
        witness_proof=witness_proof,
        missing_evidence=missing_evidence,
        conflicting_evidence=conflicting_evidence,
        warnings=warnings,
        manifest=manifest,
    )


def _load_manifest(
    manifest_path: Path,
    missing_evidence: list[str],
    conflicting_evidence: list[str],
) -> dict[str, Any] | None:
    if not manifest_path.exists():
        missing_evidence.append("manifest_json_missing")
        return None

    if not manifest_path.is_file():
        conflicting_evidence.append("manifest_json_not_file")
        return None

    try:
        with manifest_path.open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
    except json.JSONDecodeError:
        conflicting_evidence.append("manifest_json_invalid")
        return None
    except (OSError, UnicodeDecodeError):
        conflicting_evidence.append("manifest_json_unreadable")
        return None

    if not isinstance(manifest, dict):
        conflicting_evidence.append("manifest_json_not_object")
        return None

    return manifest


def _verify_manifest_file_entry(
    *,
    package_root: Path,
    package_root_resolved: Path,
    entry: Any,
    missing_evidence: list[str],
    conflicting_evidence: list[str],
    warnings: list[str],
) -> dict[str, Any]:
    if not isinstance(entry, dict):
        conflicting_evidence.append("manifest_file_entry_not_object")
        return {"path": None, "status": "INVALID", "reason": "entry_not_object"}

    relative_path = entry.get("path")
    if not isinstance(relative_path, str) or not relative_path.strip():
        missing_evidence.append("manifest_file_path_missing")
        return {"path": relative_path, "status": "INVALID", "reason": "path_missing"}

    if _is_unsafe_relative_path(relative_path):
        conflicting_evidence.append(f"unsafe_manifest_file_path:{relative_path}")
        return {"path": relative_path, "status": "INVALID", "reason": "unsafe_path"}

    digest = _extract_sha256(entry)
    if digest is None:
        missing_evidence.append(f"sha256_missing:{relative_path}")
        return {"path": relative_path, "status": "INVALID", "reason": "sha256_missing"}

    if not _looks_like_sha256(digest):
        conflicting_evidence.append(f"sha256_invalid_format:{relative_path}")
        return {
            "path": relative_path,
            "status": "INVALID",
            "expected_sha256": digest,
            "reason": "sha256_invalid_format",
        }

    file_path = package_root / relative_path
    if not file_path.exists():
        missing_evidence.append(f"file_missing:{relative_path}")
        return {
            "path": relative_path,
            "status": "MISSING",
            "expected_sha256": digest,
            "actual_sha256": None,
        }

    try:
        resolved_file_path = file_path.resolve(strict=True)
    except OSError:
        conflicting_evidence.append(f"manifest_file_unresolvable:{relative_path}")
        return {
            "path": relative_path,
            "status": "INVALID",
            "expected_sha256": digest.lower(),
            "actual_sha256": None,
            "reason": "file_unresolvable",
        }

    if not _is_within_directory(resolved_file_path, package_root_resolved):
        conflicting_evidence.append(f"manifest_file_not_under_package:{relative_path}")
        return {
            "path": relative_path,
            "status": "INVALID",
            "expected_sha256": digest.lower(),
            "actual_sha256": None,
            "reason": "not_under_package",
        }

    if not file_path.is_file():
        conflicting_evidence.append(f"manifest_path_not_file:{relative_path}")
        return {
            "path": relative_path,
            "status": "INVALID",
            "expected_sha256": digest,
            "actual_sha256": None,
            "reason": "path_not_file",
        }

    actual = _sha256_file(file_path)
    if actual != digest.lower():
        conflicting_evidence.append(f"sha256_mismatch:{relative_path}")
        return {
            "path": relative_path,
            "status": "MISMATCH",
            "expected_sha256": digest.lower(),
            "actual_sha256": actual,
        }

    return {
        "path": relative_path,
        "status": "MATCH",
        "expected_sha256": digest.lower(),
        "actual_sha256": actual,
    }


def _verify_issuer_proof_entry(
    *,
    package_root: Path,
    package_root_resolved: Path,
    entry: Any,
    missing_evidence: list[str],
    conflicting_evidence: list[str],
    warnings: list[str],
) -> dict[str, Any]:
    if entry is None:
        return _issuer_proof_not_provided()

    if not isinstance(entry, dict):
        conflicting_evidence.append("issuer_proof_entry_not_object")
        return {
            "status": "INVALID",
            "checked": True,
            "path": None,
            "identity_verified": False,
            "reason": "entry_not_object",
        }

    file_result = _verify_manifest_file_entry(
        package_root=package_root,
        package_root_resolved=package_root_resolved,
        entry=entry,
        missing_evidence=missing_evidence,
        conflicting_evidence=conflicting_evidence,
        warnings=warnings,
    )
    relative_path = file_result.get("path")
    result: dict[str, Any] = {
        "status": file_result["status"],
        "checked": True,
        "path": relative_path,
        "file": file_result,
        "identity_verified": False,
    }

    if file_result["status"] != "MATCH":
        return result

    proof_path = package_root / str(relative_path)
    try:
        with proof_path.open("r", encoding="utf-8") as handle:
            proof = json.load(handle)
    except json.JSONDecodeError:
        conflicting_evidence.append(f"issuer_proof_json_invalid:{relative_path}")
        result.update({"status": "INVALID", "reason": "issuer_proof_json_invalid"})
        return result
    except (OSError, UnicodeDecodeError):
        conflicting_evidence.append(f"issuer_proof_json_unreadable:{relative_path}")
        result.update({"status": "INVALID", "reason": "issuer_proof_json_unreadable"})
        return result

    if not isinstance(proof, dict):
        conflicting_evidence.append(f"issuer_proof_json_not_object:{relative_path}")
        result.update({"status": "INVALID", "reason": "issuer_proof_json_not_object"})
        return result

    missing_fields = [
        field
        for field in ISSUER_PROOF_REQUIRED_FIELDS
        if not isinstance(proof.get(field), str) or not proof.get(field, "").strip()
    ]
    if missing_fields:
        for field in missing_fields:
            missing_evidence.append(f"issuer_proof_field_missing:{relative_path}:{field}")
        result.update({"status": "INVALID", "reason": "issuer_proof_required_field_missing"})
        return result

    result.update(
        {
            "status": "PRESENT",
            "issuer": proof["issuer"],
            "statement": proof["statement"],
            "identity_verified": False,
        }
    )
    return result


def _verify_timestamp_proof_entry(
    *,
    package_root: Path,
    package_root_resolved: Path,
    entry: Any,
    missing_evidence: list[str],
    conflicting_evidence: list[str],
    warnings: list[str],
) -> dict[str, Any]:
    if entry is None:
        return _timestamp_proof_not_provided()

    if not isinstance(entry, dict):
        conflicting_evidence.append("timestamp_proof_entry_not_object")
        return {"status": "INVALID", "checked": True, "path": None, "reason": "entry_not_object"}

    file_result = _verify_manifest_file_entry(
        package_root=package_root,
        package_root_resolved=package_root_resolved,
        entry=entry,
        missing_evidence=missing_evidence,
        conflicting_evidence=conflicting_evidence,
        warnings=warnings,
    )
    relative_path = file_result.get("path")
    result: dict[str, Any] = {
        "status": file_result["status"],
        "checked": True,
        "path": relative_path,
        "file": file_result,
        "external_verified": False,
    }

    if file_result["status"] != "MATCH":
        return result

    proof_path = package_root / str(relative_path)
    try:
        with proof_path.open("r", encoding="utf-8") as handle:
            proof = json.load(handle)
    except json.JSONDecodeError:
        conflicting_evidence.append(f"timestamp_proof_json_invalid:{relative_path}")
        result.update({"status": "INVALID", "reason": "timestamp_proof_json_invalid"})
        return result
    except (OSError, UnicodeDecodeError):
        conflicting_evidence.append(f"timestamp_proof_json_unreadable:{relative_path}")
        result.update({"status": "INVALID", "reason": "timestamp_proof_json_unreadable"})
        return result

    if not isinstance(proof, dict):
        conflicting_evidence.append(f"timestamp_proof_json_not_object:{relative_path}")
        result.update({"status": "INVALID", "reason": "timestamp_proof_json_not_object"})
        return result

    missing_fields = [
        field
        for field in TIMESTAMP_PROOF_REQUIRED_FIELDS
        if not isinstance(proof.get(field), str) or not proof.get(field, "").strip()
    ]
    if missing_fields:
        for field in missing_fields:
            missing_evidence.append(f"timestamp_proof_field_missing:{relative_path}:{field}")
        result.update({"status": "INVALID", "reason": "timestamp_proof_required_field_missing"})
        return result

    if not _is_valid_claimed_at(proof["claimed_at"]):
        conflicting_evidence.append(f"timestamp_proof_claimed_at_invalid:{relative_path}")
        result.update({"status": "INVALID", "reason": "timestamp_proof_claimed_at_invalid"})
        return result

    if not _looks_like_sha256(proof["subject_sha256"]):
        conflicting_evidence.append(f"timestamp_proof_subject_sha256_invalid:{relative_path}")
        result.update({"status": "INVALID", "reason": "timestamp_proof_subject_sha256_invalid"})
        return result

    result.update(
        {
            "status": "PRESENT",
            "claimed_at": proof["claimed_at"],
            "subject_sha256": proof["subject_sha256"].lower(),
        }
    )
    return result


def _verify_witness_proof_entry(
    *,
    package_root: Path,
    package_root_resolved: Path,
    entry: Any,
    local_subject_sha256s: set[str],
    missing_evidence: list[str],
    conflicting_evidence: list[str],
    warnings: list[str],
) -> dict[str, Any]:
    if entry is None:
        return _witness_proof_not_provided()

    if not isinstance(entry, dict):
        conflicting_evidence.append("witness_proof_entry_not_object")
        return {"status": "INVALID", "checked": True, "path": None, "reason": "entry_not_object"}

    file_result = _verify_manifest_file_entry(
        package_root=package_root,
        package_root_resolved=package_root_resolved,
        entry=entry,
        missing_evidence=missing_evidence,
        conflicting_evidence=conflicting_evidence,
        warnings=warnings,
    )
    relative_path = file_result.get("path")
    result: dict[str, Any] = {
        "status": file_result["status"],
        "checked": True,
        "path": relative_path,
        "file": file_result,
        "signature_verified": False,
    }

    if file_result["status"] != "MATCH":
        return result

    proof_path = package_root / str(relative_path)
    try:
        with proof_path.open("r", encoding="utf-8") as handle:
            proof = json.load(handle)
    except json.JSONDecodeError:
        conflicting_evidence.append(f"witness_proof_json_invalid:{relative_path}")
        result.update({"status": "INVALID", "reason": "witness_proof_json_invalid"})
        return result
    except (OSError, UnicodeDecodeError):
        conflicting_evidence.append(f"witness_proof_json_unreadable:{relative_path}")
        result.update({"status": "INVALID", "reason": "witness_proof_json_unreadable"})
        return result

    if not isinstance(proof, dict):
        conflicting_evidence.append(f"witness_proof_json_not_object:{relative_path}")
        result.update({"status": "INVALID", "reason": "witness_proof_json_not_object"})
        return result

    missing_fields = [
        field
        for field in WITNESS_PROOF_REQUIRED_FIELDS
        if not isinstance(proof.get(field), str) or not proof.get(field, "").strip()
    ]
    if missing_fields:
        for field in missing_fields:
            missing_evidence.append(f"witness_proof_field_missing:{relative_path}:{field}")
        result.update({"status": "INVALID", "reason": "witness_proof_required_field_missing"})
        return result

    subject_sha256 = proof["subject_sha256"].lower()
    if not _looks_like_sha256(subject_sha256):
        conflicting_evidence.append(f"witness_proof_subject_sha256_invalid:{relative_path}")
        result.update({"status": "INVALID", "reason": "witness_proof_subject_sha256_invalid"})
        return result

    if subject_sha256 not in local_subject_sha256s:
        conflicting_evidence.append(f"witness_proof_subject_mismatch:{relative_path}")
        result.update(
            {
                "status": "SUBJECT_MISMATCH",
                "reason": "witness_proof_subject_mismatch",
                "subject_sha256": subject_sha256,
            }
        )
        return result

    result.update(
        {
            "status": "PRESENT",
            "witness_id": proof["witness_id"],
            "statement": proof["statement"],
            "subject_sha256": subject_sha256,
        }
    )
    return result


def _issuer_proof_not_provided() -> dict[str, Any]:
    return {"status": "NOT_PROVIDED", "checked": False, "path": None, "identity_verified": False}


def _timestamp_proof_not_provided() -> dict[str, Any]:
    return {"status": "NOT_PROVIDED", "checked": False, "path": None, "external_verified": False}


def _witness_proof_not_provided() -> dict[str, Any]:
    return {"status": "NOT_PROVIDED", "checked": False, "path": None, "signature_verified": False}


def _collect_local_subject_sha256s(manifest: dict[str, Any], files: list[dict[str, Any]]) -> set[str]:
    subjects: set[str] = set()
    for key in ("subject_sha256", "content_hash", "record_hash"):
        value = manifest.get(key)
        if isinstance(value, str) and _looks_like_sha256(value.lower()):
            subjects.add(value.lower())

    for file_result in files:
        if file_result.get("status") != "MATCH":
            continue
        value = file_result.get("actual_sha256")
        if isinstance(value, str) and _looks_like_sha256(value.lower()):
            subjects.add(value.lower())
    return subjects


def _extract_sha256(entry: dict[str, Any]) -> str | None:
    if isinstance(entry.get("sha256"), str):
        return entry["sha256"]

    algorithm = entry.get("algorithm")
    if isinstance(algorithm, str) and algorithm.lower() not in SUPPORTED_DIGEST_ALGORITHMS:
        return None

    for key in ("digest", "hash"):
        value = entry.get(key)
        if isinstance(value, str):
            return value

    return None


def _is_unsafe_relative_path(value: str) -> bool:
    path = Path(value)
    return path.is_absolute() or ".." in path.parts


def _is_within_directory(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
    except ValueError:
        return False
    return True


def _looks_like_sha256(value: str) -> bool:
    if len(value) != 64:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def _is_valid_claimed_at(value: str) -> bool:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None and parsed.tzinfo.utcoffset(parsed) is not None


def _sha256_file(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _build_response(
    *,
    status: str,
    package_root: Path,
    manifest_path: Path,
    files: list[dict[str, Any]],
    issuer_proof: dict[str, Any],
    timestamp_proof: dict[str, Any],
    witness_proof: dict[str, Any],
    missing_evidence: list[str],
    conflicting_evidence: list[str],
    warnings: list[str],
    manifest: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "verifier_version": VERIFICATION_PACKAGE_HASH_CORE_VERSION,
        "status": status,
        "verified": status == VerificationPackageStatus.VERIFIED,
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "human_review_required": status != VerificationPackageStatus.VERIFIED,
        "package_path": str(package_root),
        "manifest_path": str(manifest_path),
        "package_id": manifest.get("package_id") if manifest else None,
        "record_id": manifest.get("record_id") if manifest else None,
        "schema_version": manifest.get("schema_version") if manifest else None,
        "checks": {
            "manifest_present": manifest is not None,
            "manifest_files_checked": len(files),
            "sha256_only": True,
            "issuer_proof_checked": issuer_proof.get("checked", False),
            "issuer_proof_present": issuer_proof.get("status") == "PRESENT",
            "issuer_identity_verified": issuer_proof.get("identity_verified", False),
            "timestamp_proof_checked": timestamp_proof.get("checked", False),
            "timestamp_proof_present": timestamp_proof.get("status") == "PRESENT",
            "external_timestamp_verified": timestamp_proof.get("external_verified", False),
            "witness_proof_checked": witness_proof.get("checked", False),
            "witness_proof_present": witness_proof.get("status") == "PRESENT",
            "signatures_verified": False,
            "witnesses_verified": False,
        },
        "files": files,
        "issuer_proof": issuer_proof,
        "timestamp_proof": timestamp_proof,
        "witness_proof": witness_proof,
        "missing_evidence": sorted(set(missing_evidence)),
        "conflicting_evidence": sorted(set(conflicting_evidence)),
        "warnings": sorted(set(warnings)),
    }


__all__ = [
    "VERIFICATION_PACKAGE_HASH_CORE_VERSION",
    "VerificationPackageStatus",
    "verify_verification_package",
]
