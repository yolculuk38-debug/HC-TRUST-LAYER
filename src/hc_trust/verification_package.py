"""Verification package integrity checks for HC-TRUST-LAYER."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

SUPPORTED_DIGEST_ALGORITHMS = {"sha256", "sha-256"}
ISSUER_PROOF_REQUIRED_FIELDS = ("issuer", "subject", "proof_type", "issued_at")
TIMESTAMP_PROOF_REQUIRED_FIELDS = ("method", "timestamp", "subject_sha256")
SIGNATURE_PROOF_REQUIRED_FIELDS = ("key_id", "algorithm", "signature", "subject_sha256")
WITNESS_PROOF_REQUIRED_FIELDS = ("witness_id", "statement", "subject_sha256")


def verify_verification_package(package_path: str | Path) -> dict[str, Any]:
    """Verify a local verification package manifest and listed file hashes.

    This function is deliberately local and advisory. It only checks that the
    package manifest is readable, listed files are present inside the package
    directory, and each listed file's SHA-256 digest matches the manifest.
    """

    package_root = Path(package_path)
    package_root_resolved = package_root.resolve()
    manifest_path = package_root / "manifest.json"

    missing_evidence: list[str] = []
    conflicting_evidence: list[str] = []
    warnings: list[str] = []

    result: dict[str, Any] = {
        "status": "UNVERIFIED",
        "verified": False,
        "package_path": str(package_root),
        "manifest_path": str(manifest_path),
        "files": [],
        "missing_evidence": missing_evidence,
        "conflicting_evidence": conflicting_evidence,
        "warnings": warnings,
        "issuer_proof": _issuer_proof_not_provided(),
        "timestamp_proof": _timestamp_proof_not_provided(),
        "signature_proof": _signature_proof_not_provided(),
        "witness_proof": _witness_proof_not_provided(),
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "checks": {
            "manifest_present": False,
            "manifest_valid_json": False,
            "files_checked": 0,
            "all_files_match_manifest": False,
            "issuer_proof_checked": False,
            "issuer_proof_present": False,
            "identity_verified": False,
            "timestamp_proof_checked": False,
            "timestamp_proof_present": False,
            "timestamp_external_verified": False,
            "signature_proof_checked": False,
            "signature_proof_present": False,
            "signatures_verified": False,
            "witness_proof_checked": False,
            "witness_proof_present": False,
            "witnesses_verified": False,
        },
    }

    if not manifest_path.exists():
        missing_evidence.append("manifest.json")
        result["status"] = "MISSING_EVIDENCE"
        return result

    result["checks"]["manifest_present"] = True

    try:
        with manifest_path.open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
    except json.JSONDecodeError:
        conflicting_evidence.append("manifest_json_invalid")
        result["status"] = "INVALID"
        return result
    except (OSError, UnicodeDecodeError):
        conflicting_evidence.append("manifest_unreadable")
        result["status"] = "INVALID"
        return result

    if not isinstance(manifest, dict):
        conflicting_evidence.append("manifest_not_object")
        result["status"] = "INVALID"
        return result

    result["checks"]["manifest_valid_json"] = True
    result["manifest"] = {
        "package_id": manifest.get("package_id"),
        "record_id": manifest.get("record_id"),
        "created_at": manifest.get("created_at"),
    }

    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        missing_evidence.append("manifest.files")
        result["status"] = "MISSING_EVIDENCE"
        return result

    for index, entry in enumerate(files):
        file_result = _verify_manifest_file_entry(
            package_root=package_root,
            package_root_resolved=package_root_resolved,
            entry=entry,
            missing_evidence=missing_evidence,
            conflicting_evidence=conflicting_evidence,
            warnings=warnings,
            index=index,
        )
        result["files"].append(file_result)

    result["checks"]["files_checked"] = len(result["files"])
    result["checks"]["all_files_match_manifest"] = all(
        file_result.get("status") == "MATCH" for file_result in result["files"]
    )

    result["issuer_proof"] = _verify_issuer_proof(
        package_root=package_root,
        package_root_resolved=package_root_resolved,
        entry=manifest.get("issuer_proof"),
        missing_evidence=missing_evidence,
        conflicting_evidence=conflicting_evidence,
        warnings=warnings,
    )
    result["checks"]["issuer_proof_checked"] = result["issuer_proof"].get("checked", False)
    result["checks"]["issuer_proof_present"] = result["issuer_proof"].get("status") == "PRESENT"
    result["checks"]["identity_verified"] = False

    local_subject_sha256s = _collect_local_subject_sha256s(manifest, result["files"])
    result["timestamp_proof"] = _verify_timestamp_proof(
        package_root=package_root,
        package_root_resolved=package_root_resolved,
        entry=manifest.get("timestamp_proof"),
        local_subject_sha256s=local_subject_sha256s,
        missing_evidence=missing_evidence,
        conflicting_evidence=conflicting_evidence,
        warnings=warnings,
    )
    result["checks"]["timestamp_proof_checked"] = result["timestamp_proof"].get("checked", False)
    result["checks"]["timestamp_proof_present"] = result["timestamp_proof"].get("status") == "PRESENT"
    result["checks"]["timestamp_external_verified"] = False

    result["signature_proof"] = _verify_signature_proof(
        package_root=package_root,
        package_root_resolved=package_root_resolved,
        entry=manifest.get("signature_proof"),
        local_subject_sha256s=local_subject_sha256s,
        missing_evidence=missing_evidence,
        conflicting_evidence=conflicting_evidence,
        warnings=warnings,
    )
    result["checks"]["signature_proof_checked"] = result["signature_proof"].get("checked", False)
    result["checks"]["signature_proof_present"] = result["signature_proof"].get("status") == "PRESENT"
    result["checks"]["signatures_verified"] = False

    result["witness_proof"] = _verify_witness_proof(
        package_root=package_root,
        package_root_resolved=package_root_resolved,
        entry=manifest.get("witness_proof"),
        local_subject_sha256s=local_subject_sha256s,
        missing_evidence=missing_evidence,
        conflicting_evidence=conflicting_evidence,
        warnings=warnings,
    )
    result["checks"]["witness_proof_checked"] = result["witness_proof"].get("checked", False)
    result["checks"]["witness_proof_present"] = result["witness_proof"].get("status") == "PRESENT"
    result["checks"]["witnesses_verified"] = False

    if missing_evidence:
        result["status"] = "MISSING_EVIDENCE"
    elif conflicting_evidence:
        result["status"] = "INVALID"
    elif not result["checks"]["all_files_match_manifest"]:
        result["status"] = "INVALID"
    else:
        result["status"] = "VERIFIED"
        result["verified"] = True

    return result


def _verify_manifest_file_entry(
    package_root: Path,
    package_root_resolved: Path,
    entry: Any,
    missing_evidence: list[str],
    conflicting_evidence: list[str],
    warnings: list[str],
    index: int | None = None,
) -> dict[str, Any]:
    label = f"manifest.files[{index}]" if index is not None else "manifest file entry"

    if not isinstance(entry, dict):
        conflicting_evidence.append(f"{label}:not_object")
        return {"status": "INVALID", "path": None, "reason": "entry_not_object"}

    relative_path = entry.get("path")
    expected_sha256 = _extract_sha256(entry)

    if not isinstance(relative_path, str) or not relative_path.strip():
        missing_evidence.append(f"{label}.path")
        return {"status": "MISSING", "path": None, "reason": "path_missing"}

    relative_path = relative_path.strip()
    if _is_unsafe_relative_path(relative_path):
        conflicting_evidence.append(f"unsafe_path:{relative_path}")
        return {"status": "INVALID", "path": relative_path, "reason": "unsafe_path"}

    if not isinstance(expected_sha256, str) or not expected_sha256.strip():
        missing_evidence.append(f"{label}.sha256")
        return {"status": "MISSING", "path": relative_path, "reason": "sha256_missing"}

    expected_sha256 = expected_sha256.lower()
    if not _looks_like_sha256(expected_sha256):
        conflicting_evidence.append(f"sha256_invalid:{relative_path}")
        return {"status": "INVALID", "path": relative_path, "reason": "sha256_invalid"}

    file_path = package_root / relative_path
    file_path_resolved = file_path.resolve()
    if not _is_within_directory(file_path_resolved, package_root_resolved):
        conflicting_evidence.append(f"path_outside_package:{relative_path}")
        return {"status": "INVALID", "path": relative_path, "reason": "path_outside_package"}

    if not file_path.exists():
        missing_evidence.append(f"file_missing:{relative_path}")
        return {"status": "MISSING", "path": relative_path, "reason": "file_missing"}

    actual_sha256 = hashlib.sha256(file_path.read_bytes()).hexdigest()
    if actual_sha256 != expected_sha256:
        conflicting_evidence.append(f"sha256_mismatch:{relative_path}")
        return {
            "status": "MISMATCH",
            "path": relative_path,
            "expected_sha256": expected_sha256,
            "actual_sha256": actual_sha256,
        }

    return {
        "status": "MATCH",
        "path": relative_path,
        "expected_sha256": expected_sha256,
        "actual_sha256": actual_sha256,
    }


def _looks_like_sha256(value: str) -> bool:
    return len(value) == 64 and all(character in "0123456789abcdef" for character in value.lower())


def _verify_issuer_proof(
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
            "subject": proof["subject"],
            "proof_type": proof["proof_type"],
            "issued_at": proof["issued_at"],
        }
    )
    return result


def _verify_timestamp_proof(
    package_root: Path,
    package_root_resolved: Path,
    entry: Any,
    local_subject_sha256s: set[str],
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

    subject_sha256 = proof["subject_sha256"].lower()
    if not _looks_like_sha256(subject_sha256):
        conflicting_evidence.append(f"timestamp_proof_subject_sha256_invalid:{relative_path}")
        result.update({"status": "INVALID", "reason": "timestamp_proof_subject_sha256_invalid"})
        return result

    if subject_sha256 not in local_subject_sha256s:
        conflicting_evidence.append(f"timestamp_proof_subject_mismatch:{relative_path}")
        result.update(
            {
                "status": "SUBJECT_MISMATCH",
                "reason": "timestamp_proof_subject_mismatch",
                "subject_sha256": subject_sha256,
            }
        )
        return result

    result.update(
        {
            "status": "PRESENT",
            "method": proof["method"],
            "timestamp": proof["timestamp"],
            "subject_sha256": subject_sha256,
        }
    )
    return result


def _verify_signature_proof(
    package_root: Path,
    package_root_resolved: Path,
    entry: Any,
    local_subject_sha256s: set[str],
    missing_evidence: list[str],
    conflicting_evidence: list[str],
    warnings: list[str],
) -> dict[str, Any]:
    if entry is None:
        return _signature_proof_not_provided()

    if not isinstance(entry, dict):
        conflicting_evidence.append("signature_proof_entry_not_object")
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
        conflicting_evidence.append(f"signature_proof_json_invalid:{relative_path}")
        result.update({"status": "INVALID", "reason": "signature_proof_json_invalid"})
        return result
    except (OSError, UnicodeDecodeError):
        conflicting_evidence.append(f"signature_proof_json_unreadable:{relative_path}")
        result.update({"status": "INVALID", "reason": "signature_proof_json_unreadable"})
        return result

    if not isinstance(proof, dict):
        conflicting_evidence.append(f"signature_proof_json_not_object:{relative_path}")
        result.update({"status": "INVALID", "reason": "signature_proof_json_not_object"})
        return result

    missing_fields = [
        field
        for field in SIGNATURE_PROOF_REQUIRED_FIELDS
        if not isinstance(proof.get(field), str) or not proof.get(field, "").strip()
    ]
    if missing_fields:
        for field in missing_fields:
            missing_evidence.append(f"signature_proof_field_missing:{relative_path}:{field}")
        result.update({"status": "INVALID", "reason": "signature_proof_required_field_missing"})
        return result

    subject_sha256 = proof["subject_sha256"].lower()
    if not _looks_like_sha256(subject_sha256):
        conflicting_evidence.append(f"signature_proof_subject_sha256_invalid:{relative_path}")
        result.update({"status": "INVALID", "reason": "signature_proof_subject_sha256_invalid"})
        return result

    if subject_sha256 not in local_subject_sha256s:
        conflicting_evidence.append(f"signature_proof_subject_mismatch:{relative_path}")
        result.update(
            {
                "status": "SUBJECT_MISMATCH",
                "reason": "signature_proof_subject_mismatch",
                "subject_sha256": subject_sha256,
            }
        )
        return result

    result.update(
        {
            "status": "PRESENT",
            "key_id": proof["key_id"],
            "algorithm": proof["algorithm"],
            "subject_sha256": subject_sha256,
        }
    )
    return result


def _verify_witness_proof(
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


def _signature_proof_not_provided() -> dict[str, Any]:
    return {"status": "NOT_PROVIDED", "checked": False, "path": None, "signature_verified": False}


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
