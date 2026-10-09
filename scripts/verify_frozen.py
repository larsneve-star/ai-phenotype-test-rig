#!/usr/bin/env python3
"""Check exact Git blob digests of the frozen baseline; emit SHA-256 for future lock."""
import hashlib
import json
import sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "protocol/FROZEN-BLOBS-v1.0.json").read_text())
bad = []
for name, expected in manifest["files"].items():
    data = (root / name).read_bytes()
    actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()
    print(f"{name}: git-blob={actual} sha256={sha256}")
    if actual != expected:
        bad.append(name)
if bad:
    print("FAIL: frozen file content changed: " + ", ".join(bad), file=sys.stderr)
    sys.exit(1)
print("PASS: exact frozen file bytes match baseline Git blob digests.")
