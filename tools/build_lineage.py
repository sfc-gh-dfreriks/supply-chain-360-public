#!/usr/bin/env python3
"""Bake public/data/lineage.json for the "BDC Sources & Lineage" page.

The payload is produced by the local Supply Chain 360 server's /api/lineage
(row counts from SAP_SUPPLY_CHAIN.ANALYTICS.LINEAGE_COUNTS), so the public
copy shows exactly what the live app shows.

Usage:  python tools/build_lineage.py [--url http://localhost:3001/api/lineage]
"""
import argparse, json, pathlib, urllib.request

OUT = pathlib.Path(__file__).resolve().parent.parent / "public" / "data" / "lineage.json"

ap = argparse.ArgumentParser()
ap.add_argument("--url", default="http://localhost:3001/api/lineage")
data = json.load(urllib.request.urlopen(ap.parse_args().url, timeout=60))
if "error" in data:
    raise SystemExit(f"lineage endpoint error: {data['error']}")
OUT.write_text(json.dumps(data, indent=2) + "\n")
print(f"wrote {OUT} ({len(data['products'])} products)")
