#!/usr/bin/env python3
"""Price calculator for freelancers.

Examples
  python3 scripts/price_calc.py rate --income 12000 --costs 1200 --tax 0.20 --hours 20 --weeks 46
  python3 scripts/price_calc.py quote --hours 10 --rate 18 --fee 0.20 --buffer 0.25
  python3 scripts/price_calc.py net --price 100 --fee 0.20 --extra 0.5
  python3 scripts/price_calc.py product --price 19 --fee 0.10 --processing 0.029 --fixed 0.30

All money is in one currency of your choice. Fees are fractions (0.20 = 20%).
"""
import argparse
import sys


def pos(v, name):
    if v < 0:
        sys.exit(f"{name} must not be negative")
    return v


def rate(a):
    if not 0 <= a.tax < 1:
        sys.exit("--tax must be between 0 and <1 (e.g. 0.20)")
    hours = a.hours * a.weeks
    if hours <= 0:
        sys.exit("hours x weeks must be > 0")
    r = ((a.income + a.costs) / (1 - a.tax)) / hours
    print(f"Billable hours/year: {hours:.0f}")
    print(f"Minimum hourly rate to reach take-home {a.income:,.0f}: {r:.2f}")
    print("Tip: real effective rate is lower when you count unpaid search/admin time.")


def quote(a):
    if not 0 <= a.fee < 1:
        sys.exit("--fee must be between 0 and <1")
    base = a.hours * a.rate * (1 + a.buffer) + a.costs
    gross = base / (1 - a.fee)
    print(f"Work value (hours x rate + buffer + costs): {base:.2f}")
    print(f"Price to charge so you NET that after a {a.fee:.0%} platform fee: {gross:.2f}")
    print(f"Suggested tiers  Basic {gross:.0f}  Standard {gross * 2.5:.0f}  Premium {gross * 5:.0f}")


def net(a):
    fee = a.price * a.fee
    left = a.price - fee - a.extra
    print(f"Price {a.price:.2f} - platform fee {fee:.2f} - other costs {a.extra:.2f} = net {left:.2f}")
    if a.hours:
        print(f"Effective hourly (net / {a.hours} h): {left / a.hours:.2f}")


def product(a):
    fees = a.price * (a.fee + a.processing) + a.fixed
    left = a.price - fees
    print(f"Price {a.price:.2f}: fees {fees:.2f} ({fees / a.price:.1%}), you keep {left:.2f}")
    if a.build_hours and a.value_per_hour:
        need = (a.build_hours * a.value_per_hour) / left if left > 0 else float("inf")
        print(f"Sales needed to repay {a.build_hours} h at {a.value_per_hour}/h: {need:.0f}")


p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
s = p.add_subparsers(dest="cmd", required=True)
x = s.add_parser("rate"); x.add_argument("--income", type=float, required=True); x.add_argument("--costs", type=float, default=0)
x.add_argument("--tax", type=float, default=0.2); x.add_argument("--hours", type=float, default=20); x.add_argument("--weeks", type=float, default=46); x.set_defaults(f=rate)
x = s.add_parser("quote"); x.add_argument("--hours", type=float, required=True); x.add_argument("--rate", type=float, required=True)
x.add_argument("--fee", type=float, default=0.2); x.add_argument("--buffer", type=float, default=0.25); x.add_argument("--costs", type=float, default=0); x.set_defaults(f=quote)
x = s.add_parser("net"); x.add_argument("--price", type=float, required=True); x.add_argument("--fee", type=float, default=0.2)
x.add_argument("--extra", type=float, default=0); x.add_argument("--hours", type=float, default=0); x.set_defaults(f=net)
x = s.add_parser("product"); x.add_argument("--price", type=float, required=True); x.add_argument("--fee", type=float, default=0.10)
x.add_argument("--processing", type=float, default=0.029); x.add_argument("--fixed", type=float, default=0.30)
x.add_argument("--build-hours", dest="build_hours", type=float, default=0); x.add_argument("--value-per-hour", dest="value_per_hour", type=float, default=0); x.set_defaults(f=product)
a = p.parse_args()
for name in ("income", "costs", "hours", "weeks", "rate", "price", "extra", "fixed"):
    if hasattr(a, name):
        pos(getattr(a, name), name)
a.f(a)
