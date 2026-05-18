#!/usr/bin/env python3
import sys
from hc_trust.cli import main

if __name__ == "__main__":
    # backward compatible: python src/qr.py ... / --batch
    sys.exit(main(["qr", *sys.argv[1:]]))
