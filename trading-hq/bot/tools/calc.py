"""Dependency-free calculators for every asset class.   python tools/calc.py <cmd> --help

  size       position size from account risk %            (crypto / stocks)
  fxsize     forex lots from risk % and stop in pips
  bond       bond price, YTM, Macaulay & modified duration
  dividend   yield, yield-on-cost, DRIP projection
  compound   future value with monthly contributions
  rr         risk:reward and breakeven win-rate
"""
from __future__ import annotations

import argparse
import math


def bond_price(face, coupon_rate, ytm, years, freq=2):
    n, c, y = int(round(years * freq)), face * coupon_rate / freq, ytm / freq
    if y == 0:
        return c * n + face
    return c * (1 - (1 + y) ** -n) / y + face * (1 + y) ** -n


def bond_ytm(price, face, coupon_rate, years, freq=2):
    lo, hi = -0.5, 2.0
    for _ in range(200):  # bisection: price falls as yield rises
        mid = (lo + hi) / 2
        if bond_price(face, coupon_rate, mid, years, freq) > price:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def bond_duration(face, coupon_rate, ytm, years, freq=2):
    n, c, y = int(round(years * freq)), face * coupon_rate / freq, ytm / freq
    pv = [(t, (c + (face if t == n else 0)) / (1 + y) ** t) for t in range(1, n + 1)]
    price = sum(v for _, v in pv)
    mac = sum(t * v for t, v in pv) / price / freq
    return mac, mac / (1 + y)


def fx_lots(equity, risk_pct, stop_pips, pip_value_per_lot=10.0):
    """pip_value_per_lot: ~10 USD for XXX/USD pairs on a 100k standard lot; convert for JPY/crosses."""
    return equity * risk_pct / (stop_pips * pip_value_per_lot)


def main():
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest="c", required=True)
    x = s.add_parser("size"); [x.add_argument(f"--{k}", type=float, required=True) for k in ("equity", "risk", "entry", "stop")]
    x = s.add_parser("fxsize"); [x.add_argument(f"--{k}", type=float, required=True) for k in ("equity", "risk", "pips")]; x.add_argument("--pipvalue", type=float, default=10.0)
    x = s.add_parser("bond"); [x.add_argument(f"--{k}", type=float, required=True) for k in ("face", "coupon", "years")]; x.add_argument("--ytm", type=float); x.add_argument("--price", type=float); x.add_argument("--freq", type=int, default=2)
    x = s.add_parser("dividend"); [x.add_argument(f"--{k}", type=float, required=True) for k in ("price", "dps", "shares")]; x.add_argument("--growth", type=float, default=0.05); x.add_argument("--years", type=int, default=20); x.add_argument("--cost", type=float)
    x = s.add_parser("compound"); [x.add_argument(f"--{k}", type=float, required=True) for k in ("start", "monthly", "rate", "years")]
    x = s.add_parser("rr"); [x.add_argument(f"--{k}", type=float, required=True) for k in ("entry", "stop", "target")]
    a = p.parse_args()

    if a.c == "size":
        q = a.equity * a.risk / abs(a.entry - a.stop)
        print(f"qty {q:.6f} | notional {q * a.entry:,.2f} | risk ${a.equity * a.risk:,.2f} | leverage {q * a.entry / a.equity:.2f}x")
    elif a.c == "fxsize":
        print(f"{fx_lots(a.equity, a.risk, a.pips, a.pipvalue):.2f} standard lots (risk ${a.equity * a.risk:,.2f})")
    elif a.c == "bond":
        if a.price:
            a.ytm = bond_ytm(a.price, a.face, a.coupon, a.years, a.freq)
        price = bond_price(a.face, a.coupon, a.ytm, a.years, a.freq)
        mac, mod = bond_duration(a.face, a.coupon, a.ytm, a.years, a.freq)
        print(f"price {price:,.4f} | YTM {a.ytm:.4%} | Macaulay {mac:.3f}y | modified {mod:.3f} "
              f"(+1% yield ~ {-mod / 100:.2%} price)")
    elif a.c == "dividend":
        inc = a.dps * a.shares
        print(f"yield {a.dps / a.price:.2%} | annual income ${inc:,.2f}")
        if a.cost:
            print(f"yield on cost {a.dps / a.cost:.2%}")
        sh, dps, px = a.shares, a.dps, a.price
        for y in range(1, a.years + 1):  # DRIP; assumes price grows with dividend growth (constant yield)
            sh += sh * dps / px
            dps *= 1 + a.growth
            px *= 1 + a.growth
        print(f"DRIP after {a.years}y @ {a.growth:.0%} growth: {sh:,.1f} shares, income ${sh * dps:,.2f}/yr (pre-tax, constant yield)")
    elif a.c == "compound":
        r, bal = a.rate / 12, a.start
        for _ in range(int(a.years * 12)):
            bal = bal * (1 + r) + a.monthly
        print(f"future value ${bal:,.2f} | contributed ${a.start + a.monthly * 12 * a.years:,.2f}")
    elif a.c == "rr":
        risk, rew = abs(a.entry - a.stop), abs(a.target - a.entry)
        print(f"R:R 1:{rew / risk:.2f} | breakeven win rate {risk / (risk + rew):.1%} (before costs)")


if __name__ == "__main__":
    main()
