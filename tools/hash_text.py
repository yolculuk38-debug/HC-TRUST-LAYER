import hashlib
from pathlib import Path

INPUT_DIR = Path("records/verified")
OUTPUT_DIR = Path("hash")

OUTPUT_DIR.mkdir(exist_ok=True)

for file_path in INPUT_DIR.glob("*.md"):
    content = file_path.read_bytes()
    hash_value = hashlib.sha256(content).hexdigest()

    output_file = OUTPUT_DIR / f"{file_path.stem}.sha256"

    output_file.write_text(
        f"{hash_value}  {file_path.as_posix()}\n",
        encoding="utf-8"
    )

    print(f"Generated: {output_file}")
