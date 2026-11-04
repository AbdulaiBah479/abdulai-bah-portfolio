"""Brokers. PaperBroker is the default. CcxtBroker (Binance etc.) is testnet by default and
refuses live orders unless TWO things are set: sandbox=False AND env LIVE_TRADING_CONFIRM=I_ACCEPT_THE_RISK.

API-key hygiene: create keys with 'Enable Spot Trading' ONLY. NEVER enable withdrawals.
Restrict by IP. Keep keys in .env (git-ignored), never in code or chat.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field


@dataclass
class PaperBroker:
    cash: float = 10_000.0
    fee: float = 0.001
    slippage: float = 0.0005
    positions: dict = field(default_factory=dict)  # symbol -> qty
    log: list = field(default_factory=list)

    def equity(self, prices: dict) -> float:
        return self.cash + sum(q * prices[s] for s, q in self.positions.items())

    def market_order(self, symbol: str, qty: float, price: float) -> dict:
        """qty > 0 buys, qty < 0 sells. Long-only: cannot sell more than held, cannot overspend."""
        if qty == 0:
            return {"status": "noop"}
        fill = price * (1 + self.slippage * (1 if qty > 0 else -1))
        if qty > 0:
            qty = min(qty, self.cash / (fill * (1 + self.fee)))
        else:
            qty = -min(-qty, self.positions.get(symbol, 0.0))
        if qty == 0:
            return {"status": "rejected"}
        cost = qty * fill
        self.cash -= cost + abs(cost) * self.fee
        self.positions[symbol] = self.positions.get(symbol, 0.0) + qty
        if abs(self.positions[symbol]) < 1e-12:
            self.positions.pop(symbol)
        order = {"symbol": symbol, "qty": qty, "price": fill, "status": "filled"}
        self.log.append(order)
        return order


class CcxtBroker:
    """Thin ccxt wrapper. Default = Binance spot TESTNET."""

    def __init__(self, exchange: str = "binance", sandbox: bool = True):
        import ccxt

        key, secret = os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_API_SECRET")
        if not key or not secret:
            raise RuntimeError("Set BINANCE_API_KEY / BINANCE_API_SECRET in .env (testnet keys first).")
        if not sandbox and os.getenv("LIVE_TRADING_CONFIRM") != "I_ACCEPT_THE_RISK":
            raise PermissionError("Live trading blocked. Paper/testnet for >= 30 days first. "
                                  "Then set LIVE_TRADING_CONFIRM=I_ACCEPT_THE_RISK deliberately.")
        self.ex = getattr(ccxt, exchange)({"apiKey": key, "secret": secret, "enableRateLimit": True})
        if sandbox:
            self.ex.set_sandbox_mode(True)
        self.sandbox = sandbox

    def balance(self, asset: str) -> float:
        return float(self.ex.fetch_balance().get(asset, {}).get("free", 0.0))

    def market_order(self, symbol: str, qty: float, price: float | None = None) -> dict:
        side = "buy" if qty > 0 else "sell"
        amount = float(self.ex.amount_to_precision(symbol, abs(qty)))
        return self.ex.create_order(symbol, "market", side, amount)
