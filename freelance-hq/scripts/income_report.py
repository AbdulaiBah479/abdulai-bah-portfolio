#!/usr/bin/env python3
"""Summarise tracker/income.csv: gross, fees, net by month and by platform.

Columns: date (YYYY-MM-DD), platform, client_or_product, type, gross, fees, currency, notes
Usage: python3 scripts/income_report.py [path/to/income.csv]
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "tracker" / "income.csv"
if not path.exists():
    sys.exit(f"Not found: {path}")

def money(v):
    try:
        return float((v or "0").replace(",", "").replace("$", "").strip() or 0)
    except ValueError:
        return 0.0

by_month = defaultdict(lambda: [0.0, 0.0])
by_platform = defaultdict(lambda: [0.0, 0.0])
by_type = defaultdict(lambda: [0.0, 0.0])
currencies = set()
rows = 0
with path.open(newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        if not (r.get("date") or "").strip():
            continue
        rows += 1
        g, fee = money(r.get("gross")), money(r.get("fees"))
        for bucket, key in ((by_month, r["date"][:7]), (by_platform, r.get("platform") or "?"), (by_type, r.get("type") or "?")):
            bucket[key][0] += g
            bucket[key][1] += fee
        if r.get("currency"):
            currencies.add(r["currency"].strip().upper())

def table(title, data):
    print(f"\n{title}")
    print(f"{'':<22}{'gross':>12}{'fees':>12}{'net':>12}{'fee %':>8}")
    for k in sorted(data):
        g, fee = data[k]
        pct = (fee / g * 100) if g else 0
        print(f"{k:<22}{g:>12.2f}{fee:>12.2f}{g - fee:>12.2f}{pct:>7.1f}%")
    tg = sum(v[0] for v in data.values())
    tf = sum(v[1] for v in data.values())
    print(f"{'TOTAL':<22}{tg:>12.2f}{tf:>12.2f}{tg - tf:>12.2f}")

print(f"Income report: {path.name} ({rows} rows)")
if rows == 0:
    print("No income logged yet. Add rows to tracker/income.csv.")
    sys.exit(0)
if len(currencies) > 1:
    print(f"WARNING: mixed currencies {sorted(currencies)}; totals are not converted.")
table("By month", by_month)
table("By platform", by_platform)
table("By type", by_type)
top = max(by_platform.items(), key=lambda kv: kv[1][0])
total = sum(v[0] for v in by_platform.values())
if total and top[1][0] / total > 0.5:
    print(f"\nNote: {top[0]} is {top[1][0] / total:.0%} of gross income (concentration risk).")
