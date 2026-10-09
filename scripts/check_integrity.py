#!/usr/bin/env python3
"""Phase 1B structural validation; no model calls, no phenotype scoring."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

def fail(message):
    errors.append(message)

def text(path):
    p = ROOT / path
    if not p.is_file():
        fail(f"Missing required file: {path}")
        return ""
    return p.read_text(encoding="utf-8")

battery = text("protocol/TEST-BATTERY-v1.0.md")
codebook = text("protocol/CODEBOOK-v1.0.md")
prereg = text("protocol/PREREGISTRATION.md")

tests = re.findall(r"^## (T\d{2})\s+—", battery, re.M)
expected_tests = [f"T{i:02d}" for i in range(1, 13)]
if tests != expected_tests:
    fail(f"Test headings must be T01–T12 once, in order; found {tests}")

codes = re.findall(r"^## ([RCKPS][1-6])\s+—", codebook, re.M)
expected_codes = [f"{group}{i}" for group in "RCKPS" for i in range(1, 7)]
if sorted(codes) != sorted(expected_codes):
    fail(f"Codebook must contain exactly 30 unique dimensions; found {codes}")

for path in (ROOT / "raw", ROOT / "data" / "raw"):
    if not path.is_dir():
        continue
    for f in path.rglob("*.json"):
        try:
            record = json.loads(f.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as exc:
            fail(f"{f.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        if not isinstance(record, dict):
            fail(f"{f.relative_to(ROOT)}: expected JSON object")
            continue
        required = ("model_name", "model_version", "timestamp", "test_id",
                    "condition", "prompt", "raw_response")
        missing = [k for k in required if k not in record]
        if missing:
            fail(f"{f.relative_to(ROOT)}: missing fields: {missing}")
        if record.get("test_id") not in expected_tests:
            fail(f"{f.relative_to(ROOT)}: invalid test_id")
        if "raw_response" in record and not isinstance(record["raw_response"], str):
            fail(f"{f.relative_to(ROOT)}: raw_response must be string")

if errors:
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    sys.exit(1)
print("PASS: 12 test headings, 30 code headings, preregistration present, JSON raw records structurally checked.")
print("NOTE: This does not verify prompt equivalence, immutable raw data, T11/T12 session linkage, or scientific validity.")
