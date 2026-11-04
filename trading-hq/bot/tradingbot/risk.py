"""Risk rules. These matter more than the entry signal."""
from __future__ import annotations

import math
from dataclasses import dataclass, field


def position_size(equity: float, risk_pct: float, entry: float, stop: float, step: float = 0.0) -> float:
    """Units to buy so that hitting `stop` loses `risk_pct` of equity.
    qty = equity * risk_pct / |entry - stop|  (floored to lot `step` if given)."""
    dist = abs(entry - stop)
    if equity <= 0 or risk_pct <= 0 or dist <= 0:
        return 0.0
    qty = equity * risk_pct / dist
    if step > 0:
        qty = math.floor(qty / step) * step
    return max(qty, 0.0)


def kelly_fraction(win_rate: float, payoff: float) -> float:
    """Full Kelly f* = p - (1-p)/b. Use at most 1/4 of it; it is very noisy."""
    if payoff <= 0:
        return 0.0
    return max(win_rate - (1 - win_rate) / payoff, 0.0)


@dataclass
class RiskManager:
    risk_per_trade: float = 0.01      # 1% of equity at risk per trade
    max_daily_loss: float = 0.03      # stop trading for the day at -3%
    max_drawdown: float = 0.15        # hard kill switch at -15% from peak
    max_open_positions: int = 3
    peak: float = 0.0
    day: str = ""
    day_start_equity: float = 0.0
    halted: bool = False
    reason: str = field(default="")

    def update(self, equity: float, day: str) -> None:
        self.peak = max(self.peak, equity)
        if day != self.day:
            self.day, self.day_start_equity = day, equity
        if self.peak > 0 and equity / self.peak - 1 <= -self.max_drawdown:
            self.halted, self.reason = True, f"max drawdown {self.max_drawdown:.0%} hit"

    def can_open(self, equity: float, open_positions: int) -> tuple[bool, str]:
        if self.halted:
            return False, self.reason or "halted"
        if self.day_start_equity and equity / self.day_start_equity - 1 <= -self.max_daily_loss:
            return False, "daily loss limit hit"
        if open_positions >= self.max_open_positions:
            return False, "max open positions"
        return True, "ok"
