import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))

import pandas as pd

from tradingbot import backtest as bt
from tradingbot import data as D
from tradingbot import indicators as ind
from tradingbot.broker import PaperBroker
from tradingbot.risk import RiskManager, kelly_fraction, position_size
from tradingbot.strategies import STRATEGIES
import calc


class Core(unittest.TestCase):
    def setUp(self):
        self.df = D.synthetic()

    def test_rsi_bounds(self):
        r = ind.rsi(self.df["close"]).dropna()
        self.assertTrue(((r >= 0) & (r <= 100)).all())

    def test_no_lookahead_signals(self):
        """Signal at bar t must not change when future bars are removed."""
        for name, fn in STRATEGIES.items():
            full = fn(self.df)
            cut = fn(self.df.iloc[:900])
            pd.testing.assert_series_equal(full.iloc[:900], cut, check_names=False, obj=name)

    def test_flat_position_costs_nothing(self):
        r = bt.run(self.df, pd.Series(0.0, index=self.df.index))
        self.assertAlmostEqual(r.metrics["total_return"], 0.0)

    def test_buy_hold_no_cost_matches_price(self):
        r = bt.run(self.df, pd.Series(1.0, index=self.df.index), fee=0, slippage=0)
        # first bar return is 0 by construction (nothing held before bar 0)
        self.assertAlmostEqual(r.equity.iloc[-1], self.df["close"].iloc[-1] / self.df["close"].iloc[0], places=6)

    def test_costs_reduce_return(self):
        pos = STRATEGIES["sma_cross"](self.df)
        a = bt.run(self.df, pos, fee=0, slippage=0).metrics["total_return"]
        b = bt.run(self.df, pos, fee=0.005, slippage=0.005).metrics["total_return"]
        self.assertLess(b, a)

    def test_position_size(self):
        self.assertAlmostEqual(position_size(10_000, 0.01, 100, 95), 20.0)
        self.assertEqual(position_size(10_000, 0.01, 100, 100), 0.0)
        self.assertEqual(position_size(10_000, 0.01, 100, 95, step=3), 18.0)

    def test_kelly(self):
        self.assertAlmostEqual(kelly_fraction(0.5, 2.0), 0.25)
        self.assertEqual(kelly_fraction(0.3, 1.0), 0.0)

    def test_risk_manager_kill_switch(self):
        rm = RiskManager(max_drawdown=0.10)
        rm.update(1000, "d1")
        rm.update(880, "d2")
        self.assertTrue(rm.halted)
        self.assertFalse(rm.can_open(880, 0)[0])

    def test_paper_broker_never_overspends_or_oversells(self):
        b = PaperBroker(cash=1000, fee=0, slippage=0)
        b.market_order("X", 1e9, 10)
        self.assertGreaterEqual(b.cash, -1e-9)
        b.market_order("X", -1e9, 10)
        self.assertNotIn("X", b.positions)

    def test_bond_math(self):
        self.assertAlmostEqual(calc.bond_price(100, 0.05, 0.05, 10), 100.0, places=6)
        self.assertAlmostEqual(calc.bond_ytm(95, 100, 0.05, 10), calc.bond_ytm(95, 100, 0.05, 10))
        y = calc.bond_ytm(calc.bond_price(100, 0.04, 0.06, 7), 100, 0.04, 7)
        self.assertAlmostEqual(y, 0.06, places=6)
        mac, mod = calc.bond_duration(100, 0.05, 0.05, 10)
        self.assertLess(mod, mac)

    def test_fx_lots(self):
        self.assertAlmostEqual(calc.fx_lots(10_000, 0.01, 50), 0.2)


if __name__ == "__main__":
    unittest.main()
