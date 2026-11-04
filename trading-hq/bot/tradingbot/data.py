"""Data loaders. All return a DataFrame indexed by time with open/high/low/close/volume."""
from __future__ import annotations

import numpy as np
import pandas as pd

COLS = ["open", "high", "low", "close", "volume"]


def synthetic(n: int = 1500, seed: int = 7, drift: float = 0.0003, vol: float = 0.02, start: float = 100.0) -> pd.DataFrame:
    """Geometric random walk with regime changes. For TESTING code only, never for judging edge."""
    rng = np.random.default_rng(seed)
    regime = np.where((np.arange(n) // 250) % 2 == 0, 1.0, -0.6)
    r = rng.normal(drift * regime, vol, n)
    close = start * np.exp(np.cumsum(r))
    open_ = np.r_[start, close[:-1]]
    spread = np.abs(rng.normal(0, vol / 2, n)) * close
    high = np.maximum(open_, close) + spread
    low = np.minimum(open_, close) - spread
    idx = pd.date_range("2020-01-01", periods=n, freq="D")
    return pd.DataFrame({"open": open_, "high": high, "low": low, "close": close,
                         "volume": rng.uniform(1e3, 1e4, n)}, index=idx)


def from_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = [c.lower() for c in df.columns]
    tcol = next((c for c in ("timestamp", "date", "datetime", "time") if c in df.columns), None)
    if tcol:
        unit = "ms" if df[tcol].dtype.kind in "iu" else None
        df.index = pd.to_datetime(df.pop(tcol), unit=unit)
    return df[COLS].astype(float).sort_index()


def from_ccxt(symbol: str = "BTC/USDT", timeframe: str = "1d", limit: int = 1000, exchange: str = "binance") -> pd.DataFrame:
    """Public market data, no API key needed. pip install ccxt"""
    import ccxt  # lazy: optional dependency

    ex = getattr(ccxt, exchange)({"enableRateLimit": True})
    rows = ex.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(rows, columns=["timestamp"] + COLS)
    df.index = pd.to_datetime(df.pop("timestamp"), unit="ms")
    return df


def from_yfinance(symbol: str = "SPY", period: str = "5y", interval: str = "1d") -> pd.DataFrame:
    """Stocks, ETFs, FX ('EURUSD=X'), indices. pip install yfinance (unofficial; personal use)."""
    import yfinance as yf

    df = yf.download(symbol, period=period, interval=interval, auto_adjust=True, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df.columns = [c.lower() for c in df.columns]
    return df[COLS].dropna()
