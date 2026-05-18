import hashlib
import json


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def calculate_content_hash(content):
    if isinstance(content, str):
        content_bytes = content.encode("utf-8")
    else:
        content_bytes = json.dumps(content, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(content_bytes).hexdigest()
