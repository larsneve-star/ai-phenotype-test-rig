#!/usr/bin/env python3
"""Validate public-safe session metadata; never open raw transcripts."""
import json, pathlib, sys
BASE = pathlib.Path(__file__).resolve().parents[1]
ALLOWED = {"E01","E02","E03","E04","E05","E06"}
REQUIRED = {"run_id","model","status","startprompt_sha256","raw_location"}
errors=[]
for path in sorted((BASE/"metadata").glob("*.json")):
    try:
        data=json.loads(path.read_text(encoding="utf-8"))
        missing=REQUIRED-set(data)
        if missing: errors.append(f"{path.name}: missing {sorted(missing)}")
        if data.get("run_id") not in ALLOWED: errors.append(f"{path.name}: unknown run_id")
        if data.get("status") not in ("planned","in_progress","complete","locked"): errors.append(f"{path.name}: invalid status")
        if data.get("raw_location") not in ("private_repository","not_collected"): errors.append(f"{path.name}: raw_location must be private_repository or not_collected")
        sha=data.get("startprompt_sha256","")
        if sha and (len(sha)!=64 or any(c not in "0123456789abcdef" for c in sha.lower())): errors.append(f"{path.name}: invalid SHA256")
        for key in ("transcript","questions","answers","profile","host_feedback"):
            if key in data: errors.append(f"{path.name}: sensitive field {key} not allowed")
    except Exception as e: errors.append(f"{path.name}: {e}")
if errors:
    print("\n".join(errors),file=sys.stderr);sys.exit(1)
print("Six Mirrors public metadata validation OK")
