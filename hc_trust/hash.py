#!/usr/bin/env python3
import hashlib
import sys
from pathlib import Path

def calculate_sha256(file_path):
    """Dosyanın SHA256 hash'ini hesapla"""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python src/hash.py <dosya_yolu>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not Path(file_path).exists():
        print(f"Hata: Dosya bulunamadı: {file_path}")
        sys.exit(1)
    
    hash_value = calculate_sha256(file_path)
    print(f"SHA256: {hash_value}")
