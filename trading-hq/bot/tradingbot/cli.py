"""CLI:  python -m tradingbot <command>

  backtest   run a strategy over data, compare with buy&hold, in/out-of-sample + walk-forward
  paper      replay bar-by-bar through PaperBroker + RiskManager (stop-loss sizing, kill switch)
  signal     print the current target position for the latest bar (feed to your alerts)
"""
from __future__ import annotations

import argparse

import pandas as pd

from . import backtest as bt
from . import data as D
from .broker import PaperBroker
from .indicators import atr
from .risk import RiskManager, position_size
from .strategies import STRATEGIES


def load(a) -> pd.DataFrame:
    if a.source == "synthetic":
        return D.synthetic()
    if a.source == "csv":
        return D.from_csv(a.path)
    if a.source == "ccxt":
        return D.from_ccxt(a.symbol, a.timeframe, a.limit)
    if a.source == "yfinance":
        return D.from_yfinance(a.symbol)
    raise SystemExit(f"unknown source {a.source}")


def cmd_backtest(a):
    df, fn = load(a), STRATEGIES[a.strategy]
    kw = dict(fee=a.fee, slippage=a.slippage, periods_per_year=a.ppy)
    res, bh = bt.run(df, fn(df), **kw), bt.buy_and_hold(df, **kw)
    ins, oos = bt.in_out_of_sample(df, fn, **kw)
    show = lambda m: {k: round(v, 4) if isinstance(v, float) else v for k, v in m.items()}
    print(f"== {a.strategy} on {len(df)} bars ==")
    print("strategy   :", show(res.metrics))
    print("buy & hold :", show(bh.metrics))
    print("in-sample  :", show(ins))
    print("out-sample :", show(oos))
    print("walk-forward Sharpe by window:", bt.walk_forward(df, fn, **kw)["sharpe"].round(2).tolist())
    print("\nRead honestly: beat buy&hold AFTER costs, OUT of sample, in most windows, with enough trades (>30)?")


def cmd_paper(a):
    df, fn = load(a), STRATEGIES[a.strategy]
    pos = fn(df)
    a_ = atr(df)
    broker, rm = PaperBroker(cash=a.cash, fee=a.fee, slippage=a.slippage), RiskManager(risk_per_trade=a.risk)
    sym, curve = a.symbol, []
    for i in range(1, len(df)):
        px, ts = df["close"].iloc[i], df.index[i]
        eq = broker.equity({sym: px})
        rm.update(eq, str(ts.date()))
        want, held = pos.iloc[i - 1], broker.positions.get(sym, 0.0) > 0   # act on prior bar's signal
        if want > 0 and not held:
            ok, why = rm.can_open(eq, len(broker.positions))
            stop = px - 2 * a_.iloc[i - 1] if pd.notna(a_.iloc[i - 1]) else px * 0.95
            qty = position_size(eq, rm.risk_per_trade, px, stop)
            if ok and qty > 0:
                broker.market_order(sym, qty, px)
        elif want <= 0 and held:
            broker.market_order(sym, -broker.positions[sym], px)
        curve.append(broker.equity({sym: px}))
    eq = pd.Series(curve)
    print(f"final equity {eq.iloc[-1]:,.2f} ({eq.iloc[-1] / a.cash - 1:+.1%}) | "
          f"max DD {(eq / eq.cummax() - 1).min():.1%} | orders {len(broker.log)} | halted={rm.halted}")


def cmd_signal(a):
    df = load(a)
    s = STRATEGIES[a.strategy](df).iloc[-1]
    print(f"{a.symbol} {a.strategy}: target position = {s:+.0f} as of {df.index[-1]} (NOT financial advice)")


def cmd_rotate(a):
    from . import rotation as R
    syms = a.symbols.split(",")
    if a.source == "synthetic":
        px = pd.concat({s: D.synthetic(seed=i + 1)["close"] for i, s in enumerate(syms)}, axis=1)
    else:
        get = (lambda s: D.from_ccxt(s, "1d", 1000)) if a.source == "ccxt" else D.from_yfinance
        px = pd.concat({s: get(s)["close"] for s in syms}, axis=1).dropna()
    w = R.momentum_weights(px, lookback=a.lookback, top_n=a.top)
    _, m = R.backtest_weights(px, w, periods_per_year=a.ppy)
    _, b = R.equal_weight_hold(px, periods_per_year=a.ppy)
    show = lambda d: {k: round(v, 3) for k, v in d.items() if k in ("total_return", "cagr", "sharpe", "max_drawdown")}
    print("rotation   :", show(m))
    print("equal-hold :", show(b))
    print("latest weights:", {k: round(v, 2) for k, v in w.iloc[-1].items() if v > 0} or "CASH")


def main(argv=None):
    p = argparse.ArgumentParser(prog="tradingbot")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn in (("backtest", cmd_backtest), ("paper", cmd_paper), ("signal", cmd_signal)):
        s = sub.add_parser(name)
        s.add_argument("--strategy", default="sma_cross", choices=list(STRATEGIES))
        s.add_argument("--source", default="synthetic", choices=["synthetic", "csv", "ccxt", "yfinance"])
        s.add_argument("--path", default="")
        s.add_argument("--symbol", default="BTC/USDT")
        s.add_argument("--timeframe", default="1d")
        s.add_argument("--limit", type=int, default=1000)
        s.add_argument("--fee", type=float, default=0.001)
        s.add_argument("--slippage", type=float, default=0.0005)
        s.add_argument("--ppy", type=int, default=365, help="periods/year: 365 crypto daily, 252 stocks daily")
        s.add_argument("--cash", type=float, default=10_000)
        s.add_argument("--risk", type=float, default=0.01)
        s.set_defaults(fn=fn)
    r = sub.add_parser("rotate", help="multi-asset momentum rotation vs equal-weight hold")
    r.add_argument("--symbols", default="BTC/USDT,ETH/USDT,BNB/USDT,SOL/USDT")
    r.add_argument("--source", default="synthetic", choices=["synthetic", "ccxt", "yfinance"])
    r.add_argument("--lookback", type=int, default=90)
    r.add_argument("--top", type=int, default=2)
    r.add_argument("--ppy", type=int, default=365)
    r.set_defaults(fn=cmd_rotate)
    sub.add_parser("telegram", help="run the private Telegram co-pilot").set_defaults(fn=lambda a: __import__("tradingbot.telegram_bot", fromlist=["run"]).run())
    a = p.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()
