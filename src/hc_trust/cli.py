import argparse
import json
import sys
from pathlib import Path

from .hashing import calculate_sha256
from .qr_tools import generate_qr, find_verified_records
from .verification import verify_record_hash, find_record_files
from .verification_package import VerificationPackageStatus, verify_verification_package


def cmd_verify(args):
    record_files, skipped_files = find_record_files(args.path or "records")
    for skipped in skipped_files:
        print(f"⏭️ SKIP: {skipped}")
    if not record_files:
        print(f"No JSON record files found in: {args.path or 'records'}")
        return 0
    failed = 0
    passed = 0
    print(f"Verifying SHA-256 hashes for {len(record_files)} record(s)...\n")
    for record_path in record_files:
        ok, message = verify_record_hash(record_path)
        if ok:
            passed += 1
            print(f"✅ {message}")
        else:
            failed += 1
            print(f"❌ {message}")
    print(f"\nResults: {passed} passed, {failed} failed")
    return 1 if failed else 0


def cmd_hash(args):
    file_path = args.file_path
    if not Path(file_path).exists():
        print(f"Hata: Dosya bulunamadı: {file_path}")
        return 1
    print(f"SHA256: {calculate_sha256(file_path)}")
    return 0


def cmd_qr(args):
    if args.batch:
        verified_records = find_verified_records("records")
        if verified_records is None:
            return 1
        if not verified_records:
            print("ℹ️ Verified kayıt bulunamadı, QR üretimi atlandı.")
            return 0
        print(f"{len(verified_records)} verified kayıt için QR üretiliyor...")
        for record_id, content_hash, archive_ref, source_path in verified_records:
            print(f"- Kaynak: {source_path}")
            out, url = generate_qr(record_id, content_hash, archive_ref)
            print(f"✅ Secure QR oluşturuldu: {out}")
            print(f"🔗 URL: {url}")
        print("✅ Batch QR üretimi tamamlandı.")
        return 0

    out, url = generate_qr(args.record_id, args.content_hash, args.archive_ref)
    print(f"✅ Secure QR oluşturuldu: {out}")
    print(f"🔗 URL: {url}")
    return 0


def cmd_verify_package(args):
    result = verify_verification_package(args.package_path)
    if args.summary:
        print(_format_verify_package_summary(result))
    else:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if result["status"] == VerificationPackageStatus.VERIFIED else 1


def _summary_value(value):
    if value is None:
        return "None"
    return str(value).encode("unicode_escape").decode("ascii")


def _summary_list(values):
    return ", ".join(_summary_value(value) for value in values)


def _format_verify_package_summary(result):
    lines = [
        "HC verification package summary",
        f"status: {result['status']}",
        f"verified: {str(result['verified']).lower()}",
        f"package_id: {_summary_value(result.get('package_id'))}",
        f"record_id: {_summary_value(result.get('record_id'))}",
        f"files_checked: {result.get('checks', {}).get('manifest_files_checked')}",
        f"issuer_proof: {result.get('issuer_proof', {}).get('status', 'NOT_PROVIDED')}",
        f"timestamp_proof: {result.get('timestamp_proof', {}).get('status', 'NOT_PROVIDED')}",
        f"witness_proof: {result.get('witness_proof', {}).get('status', 'NOT_PROVIDED')}",
        f"human_review_required: {str(result['human_review_required']).lower()}",
        "advisory_only: true",
        "public_safe: true",
        "truth_guarantee: false",
    ]
    if result.get("missing_evidence"):
        lines.append("missing_evidence: " + _summary_list(result["missing_evidence"]))
    if result.get("conflicting_evidence"):
        lines.append("conflicting_evidence: " + _summary_list(result["conflicting_evidence"]))
    if result.get("warnings"):
        lines.append("warnings: " + _summary_list(result["warnings"]))
    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(prog="hc-trust", description="HC Trust Layer CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_verify = sub.add_parser("verify", help="Verify record content hashes")
    p_verify.add_argument("path", nargs="?", default="records")
    p_verify.set_defaults(func=cmd_verify)

    p_hash = sub.add_parser("hash", help="Calculate file SHA256")
    p_hash.add_argument("file_path")
    p_hash.set_defaults(func=cmd_hash)

    p_qr = sub.add_parser("qr", help="Generate verification QR")
    p_qr.add_argument("record_id", nargs="?")
    p_qr.add_argument("content_hash", nargs="?")
    p_qr.add_argument("archive_ref", nargs="?")
    p_qr.add_argument("--batch", action="store_true")
    p_qr.set_defaults(func=cmd_qr)

    p_verify_package = sub.add_parser(
        "verify-package",
        help="Verify a local HC verification package manifest and SHA-256 file integrity",
    )
    p_verify_package.add_argument("package_path")
    p_verify_package.add_argument(
        "--summary",
        action="store_true",
        help="Print a short operator summary instead of full JSON",
    )
    p_verify_package.set_defaults(func=cmd_verify_package)
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "qr" and not args.batch and not (args.record_id and args.content_hash and args.archive_ref):
        parser.error("qr için <record_id> <content_hash> <archive_ref> veya --batch gerekli")
    if args.command == "qr" and args.batch and (args.record_id or args.content_hash or args.archive_ref):
        parser.error("--batch positional parametrelerle birlikte kullanılamaz.")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
