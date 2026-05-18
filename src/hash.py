#!/usr/bin/env python3
import sys
from hc_trust.cli import main

if __name__ == "__main__":
    # backward compatible: python src/hash.py <file>
    sys.exit(main(["hash", *sys.argv[1:]]))
