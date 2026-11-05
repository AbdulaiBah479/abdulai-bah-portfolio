"""Multi-asset momentum rotation with an absolute-momentum (cash) filter and inverse-vol weights.

Every `rebalance` bars: rank assets by `lookback`-bar return, keep the top_n with POSITIVE momentum
(otherwise sit in cash), weight by inverse volatility. Works for crypto baskets, sector ETFs,
country ETFs, or an asset-class mix (stocks/bonds/gold). Weights at t use data up to t only.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import backtest as bt


def momentum_weights(prices: pd.DataFrame, lookback: int = 126, top_n: int = 2, rebalance: int = 21,
                     abs_filter: bool = True, inv_vol: bool = True, vol_n: int = 60) -> pd.DataFrame:
    mom = prices.pct_change(lookback)
    vol = prices.pct_change().rolling(vol_n).std()
    w = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
    cur = pd.Series(0.0, index=prices.columns)
    for i in range(len(prices)):
        if i >= lookback and (i - lookback) % rebalance == 0:
            m = mom.iloc[i].dropna()
            if abs_filter:
                m = m[m > 0]
            picks = m.nlargest(top_n).index
            cur = pd.Series(0.0, index=prices.columns)
            if len(picks):
                v = vol.iloc[i][picks]
                if inv_vol and v.notna().all() and (v > 0).all():
                    iv = 1 / v
                    cur[picks] = iv / iv.sum()
                else:
                    cur[picks] = 1 / len(picks)
        w.iloc[i] = cur
    return w


def backtest_weights(prices: pd.DataFrame, weights: pd.DataFrame, fee: float = 0.001,
                     slippage: float = 0.0005, periods_per_year: int = 365):
    ret = prices.pct_change().fillna(0.0)
    held = weights.shift(1).fillna(0.0)
    turnover = held.diff().abs().sum(axis=1)
    turnover.iloc[0] = held.iloc[0].abs().sum()
    strat = (held * ret).sum(axis=1) - turnover * (fee + slippage)
    equity = (1 + strat).cumprod()
    empty = pd.DataFrame(columns=["start", "end", "side", "bars", "ret"])
    return equity, bt._metrics(equity, strat, empty, periods_per_year)


def equal_weight_hold(prices: pd.DataFrame, **kw):
    w = pd.DataFrame(1 / prices.shape[1], index=prices.index, columns=prices.columns)
    return backtest_weights(prices, w, **kw)
