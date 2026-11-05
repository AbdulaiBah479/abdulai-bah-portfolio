"""Strategies return a DESIRED position per bar (0 = flat, 1 = long, -1 = short).

The backtester executes it on the NEXT bar (no look-ahead). These are teaching
baselines, not edges: most simple rules are flat-to-negative after costs.
Always validate with out-of-sample / walk-forward before believing any result.
"""
from __future__ import annotations

import numpy as np
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


def vol_target_trend(df: pd.DataFrame, n: int = 100, target_vol: float = 0.40, vol_n: int = 20,
                     ppy: int = 365, cap: float = 1.0) -> pd.Series:
    """Trend filter x volatility targeting: size shrinks when realised vol is high (no leverage, cap=1).
    The classic way to cut drawdowns in crypto without predicting anything."""
    rv = df["close"].pct_change().rolling(vol_n).std() * np.sqrt(ppy)
    size = (target_vol / rv).clip(upper=cap)
    return (ema_trend(df, n) * size).fillna(0.0)


def bb_squeeze_breakout(df: pd.DataFrame, n: int = 20, k: float = 2.0, lookback: int = 120,
                        pct: float = 0.2) -> pd.Series:
    """Volatility compression -> expansion. Enter long on an upper-band close right after a squeeze
    (bandwidth in bottom `pct` of its history); exit when price loses the middle band."""
    lo, mid, up = ind.bollinger(df["close"], n, k)
    rank = ((up - lo) / mid).rolling(lookback).rank(pct=True)
    squeezed = (rank.shift(1) < pct)
    pos, cur = [], 0.0
    for c, u, m, sq in zip(df["close"], up, mid, squeezed):
        if pd.notna(u):
            if cur == 0 and sq and c > u:
                cur = 1.0
            elif cur == 1 and c < m:
                cur = 0.0
        pos.append(cur)
    return pd.Series(pos, index=df.index)


def ensemble(df: pd.DataFrame) -> pd.Series:
    """Democratic vote of 3 uncorrelated-ish trend rules -> position 0, 1/3, 2/3 or 1.
    Averaging rules is more robust than picking the best one in a backtest."""
    votes = pd.concat([sma_cross(df, 20, 100), ema_trend(df, 200), donchian_breakout(df, 55, 20)], axis=1)
    return votes.mean(axis=1)


def vol_target_ensemble(df: pd.DataFrame, target_vol: float = 0.40, ppy: int = 365) -> pd.Series:
    """Ensemble vote x volatility targeting: the default 'serious baseline' in this repo."""
    rv = df["close"].pct_change().rolling(20).std() * np.sqrt(ppy)
    return (ensemble(df) * (target_vol / rv).clip(upper=1.0)).fillna(0.0)


STRATEGIES = {
    "sma_cross": sma_cross,
    "ema_trend": ema_trend,
    "rsi_reversion": rsi_reversion,
    "donchian_breakout": donchian_breakout,
    "vol_target_trend": vol_target_trend,
    "bb_squeeze": bb_squeeze_breakout,
    "ensemble": ensemble,
    "vol_target_ensemble": vol_target_ensemble,
}
