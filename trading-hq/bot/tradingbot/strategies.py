"""Strategies return a DESIRED position per bar (0 = flat, 1 = long, -1 = short).

The backtester executes it on the NEXT bar (no look-ahead). These are teaching
baselines, not edges: most simple rules are flat-to-negative after costs.
Always validate with out-of-sample / walk-forward before believing any result.
"""
from __future__ import annotations

import pandas as pd

from . import indicators as ind


def sma_cross(df: pd.DataFrame, fast: int = 20, slow: int = 50) -> pd.Series:
    f, s = ind.sma(df["close"], fast), ind.sma(df["close"], slow)
    pos = (f > s).astype(float)
    return pos.where(s.notna(), 0.0)


def ema_trend(df: pd.DataFrame, n: int = 200) -> pd.Series:
    e = ind.ema(df["close"], n)
    return (df["close"] > e).astype(float).where(e.notna(), 0.0)


def rsi_reversion(df: pd.DataFrame, n: int = 14, lo: float = 30, exit_at: float = 55) -> pd.Series:
    r = ind.rsi(df["close"], n)
    pos, cur = [], 0.0
    for v in r:
        if pd.notna(v):
            if cur == 0 and v < lo:
                cur = 1.0
            elif cur == 1 and v > exit_at:
                cur = 0.0
        pos.append(cur)
    return pd.Series(pos, index=df.index)


def donchian_breakout(df: pd.DataFrame, entry: int = 55, exit_: int = 20, allow_short: bool = False) -> pd.Series:
    hi, lo_entry = ind.donchian(df, entry)
    hi_exit, lo_exit = ind.donchian(df, exit_)
    pos, cur = [], 0.0
    for c, h, le, lx, hx in zip(df["close"], hi, lo_entry, lo_exit, hi_exit):
        if pd.notna(h):
            if cur == 0:
                if c > h:
                    cur = 1.0
                elif allow_short and c < le:
                    cur = -1.0
            elif cur == 1 and c < lx:
                cur = 0.0
            elif cur == -1 and c > hx:
                cur = 0.0
        pos.append(cur)
    return pd.Series(pos, index=df.index)


STRATEGIES = {
    "sma_cross": sma_cross,
    "ema_trend": ema_trend,
    "rsi_reversion": rsi_reversion,
    "donchian_breakout": donchian_breakout,
}
