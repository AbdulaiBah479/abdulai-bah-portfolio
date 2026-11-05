"""Monte Carlo 'what could happen' simulator. Teaches the single most important lesson in trading:
even a GOOD strategy has bad streaks, and size decides whether you survive them.

  python3 tools/montecarlo.py --win 0.45 --payoff 2 --risk 0.01 --trades 200

win     probability a trade wins            payoff  average win / average loss (in R)
risk    fraction of account risked per trade cost   fees+slippage per trade, in R (0.05 = 5% of a loss)
"""
from __future__ import annotations

import argparse

import numpy as np


def simulate(win=0.45, payoff=2.0, risk=0.01, trades=200, runs=5000, cost=0.05, dd_limit=0.20, seed=1):
    rng = np.random.default_rng(seed)
    wins = rng.random((runs, trades)) < win
    r = np.where(wins, payoff, -1.0) - cost                    # result of each trade in R
    equity = np.cumprod(1 + risk * r, axis=1)                  # compounding on current equity
    peak = np.maximum.accumulate(np.concatenate([np.ones((runs, 1)), equity], axis=1), axis=1)[:, 1:]
    mdd = (equity / peak - 1).min(axis=1)
    longest = np.zeros(runs, dtype=int)
    for i in range(runs):                                      # longest losing streak
        run = best = 0
        for w in wins[i]:
            run = 0 if w else run + 1
            best = max(best, run)
        longest[i] = best
    final = equity[:, -1]
    return {
        "expectancy_R": win * payoff - (1 - win) - cost,
        "median_final": float(np.median(final)),
        "p05_final": float(np.percentile(final, 5)),
        "p95_final": float(np.percentile(final, 95)),
        "prob_loss": float((final < 1).mean()),
        f"prob_drawdown_over_{int(dd_limit * 100)}pct": float((mdd < -dd_limit).mean()),
        "median_max_drawdown": float(np.median(mdd)),
        "median_longest_losing_streak": int(np.median(longest)),
        "worst_losing_streak_seen": int(longest.max()),
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--win", type=float, default=0.45)
    p.add_argument("--payoff", type=float, default=2.0)
    p.add_argument("--risk", type=float, default=0.01)
    p.add_argument("--trades", type=int, default=200)
    p.add_argument("--runs", type=int, default=5000)
    p.add_argument("--cost", type=float, default=0.05)
    p.add_argument("--dd", type=float, default=0.20)
    a = p.parse_args()
    out = simulate(a.win, a.payoff, a.risk, a.trades, a.runs, a.cost, a.dd)
    print(f"{a.runs} simulated futures of {a.trades} trades (win {a.win:.0%}, payoff {a.payoff}R, risk {a.risk:.1%}/trade)")
    for k, v in out.items():
        print(f"  {k:36s} {v:.3f}" if isinstance(v, float) else f"  {k:36s} {v}")
    print("Account multiple: 1.0 = unchanged. Try --risk 0.05 and watch the drawdown odds explode.")


if __name__ == "__main__":
    main()
