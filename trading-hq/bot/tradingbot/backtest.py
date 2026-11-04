"""Vectorised backtester with fees + slippage and next-bar execution."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class Result:
    equity: pd.Series
    returns: pd.Series
    metrics: dict
    trades: pd.DataFrame


def run(
    df: pd.DataFrame,
    position: pd.Series,
    fee: float = 0.001,
    slippage: float = 0.0005,
    periods_per_year: int = 365,
) -> Result:
    """position[t] is decided with data up to bar t and filled at close of bar t+1's
    return stream, i.e. we hold position.shift(1) during bar t's return."""
    close = df["close"]
    ret = close.pct_change().fillna(0.0)
    held = position.shift(1).fillna(0.0)
    turnover = held.diff().abs()
    turnover.iloc[0] = abs(held.iloc[0])
    strat = held * ret - turnover * (fee + slippage)
    equity = (1 + strat).cumprod()
    trades = _trades(held, strat)
    return Result(equity, strat, _metrics(equity, strat, trades, periods_per_year), trades)


def _trades(held: pd.Series, strat: pd.Series) -> pd.DataFrame:
    seg = (held != held.shift()).cumsum()
    rows = []
    for _, g in strat.groupby(seg):
        side = held.loc[g.index[0]]
        if side != 0:
            rows.append({"start": g.index[0], "end": g.index[-1], "side": side,
                         "bars": len(g), "ret": float((1 + g).prod() - 1)})
    return pd.DataFrame(rows, columns=["start", "end", "side", "bars", "ret"])


def _metrics(equity: pd.Series, strat: pd.Series, trades: pd.DataFrame, ppy: int) -> dict:
    n = max(len(strat), 1)
    total = float(equity.iloc[-1] - 1)
    years = n / ppy
    cagr = (equity.iloc[-1] ** (1 / years) - 1) if years > 0 and equity.iloc[-1] > 0 else float("nan")
    sd = strat.std()
    sharpe = float(strat.mean() / sd * np.sqrt(ppy)) if sd and sd > 0 else 0.0
    dn = strat[strat < 0].std()
    sortino = float(strat.mean() / dn * np.sqrt(ppy)) if dn and dn > 0 else 0.0
    mdd = float((equity / equity.cummax() - 1).min())
    wins = trades["ret"] > 0 if len(trades) else pd.Series(dtype=bool)
    gp = trades.loc[wins, "ret"].sum() if len(trades) else 0.0
    gl = -trades.loc[~wins, "ret"].sum() if len(trades) else 0.0
    return {
        "total_return": total, "cagr": float(cagr), "sharpe": sharpe, "sortino": sortino,
        "max_drawdown": mdd, "calmar": float(cagr / abs(mdd)) if mdd < 0 and cagr == cagr else float("nan"),
        "trades": int(len(trades)), "win_rate": float(wins.mean()) if len(trades) else float("nan"),
        "profit_factor": float(gp / gl) if gl > 0 else float("inf") if gp > 0 else float("nan"),
        "exposure": float((strat != 0).mean()),
    }


def in_out_of_sample(df, strategy_fn, split: float = 0.6, **kw):
    """Fit nothing, just report the same rule on the first `split` and the rest.
    A strategy that only works in-sample is overfit."""
    k = int(len(df) * split)
    a, b = df.iloc[:k], df.iloc[k:]
    return (run(a, strategy_fn(a), **kw).metrics, run(b, strategy_fn(b), **kw).metrics)


def walk_forward(df, strategy_fn, windows: int = 5, **kw) -> pd.DataFrame:
    """Non-overlapping consecutive test windows -> consistency check across regimes."""
    size = len(df) // windows
    rows = []
    for i in range(windows):
        chunk = df.iloc[i * size:(i + 1) * size if i < windows - 1 else len(df)]
        m = run(chunk, strategy_fn(chunk), **kw).metrics
        m["window"] = i + 1
        rows.append(m)
    return pd.DataFrame(rows).set_index("window")


def buy_and_hold(df, **kw) -> Result:
    return run(df, pd.Series(1.0, index=df.index), **kw)
