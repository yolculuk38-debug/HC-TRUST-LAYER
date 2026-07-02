import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hc_trust.cli import main


def test_hash_missing_file_prints_english_error(capsys, tmp_path):
    missing_file = tmp_path / "missing-record.json"

    assert main(["hash", str(missing_file)]) == 1

    captured = capsys.readouterr()
    assert f"Error: File not found: {missing_file}" in captured.out


def test_qr_missing_positional_args_reports_english_parser_error(capsys):
    try:
        main(["qr"])
    except SystemExit as exc:
        assert exc.code == 2
    else:
        raise AssertionError("qr without arguments should exit with parser error")

    captured = capsys.readouterr()
    assert "qr requires <record_id> <content_hash> <archive_ref>, or use --batch" in captured.err


def test_qr_batch_rejects_positional_args_with_english_parser_error(capsys):
    try:
        main(["qr", "record-id", "content-hash", "archive-ref", "--batch"])
    except SystemExit as exc:
        assert exc.code == 2
    else:
        raise AssertionError("qr --batch with positional arguments should exit with parser error")

    captured = capsys.readouterr()
    assert "--batch cannot be used with positional arguments" in captured.err
