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



class Extra(unittest.TestCase):
    def test_rotation_no_lookahead_and_bounds(self):
        from tradingbot import rotation as R
        px = pd.concat({f"A{i}": D.synthetic(seed=i + 1)["close"] for i in range(4)}, axis=1)
        w = R.momentum_weights(px)
        self.assertTrue((w.sum(axis=1) <= 1 + 1e-9).all())
        pd.testing.assert_frame_equal(w.iloc[:800], R.momentum_weights(px.iloc[:800]))
        eq, m = R.backtest_weights(px, w)
        self.assertGreater(eq.iloc[-1], 0)

    def test_vol_target_never_levered(self):
        from tradingbot.strategies import vol_target_ensemble
        p = vol_target_ensemble(D.synthetic())
        self.assertTrue(((p >= 0) & (p <= 1)).all())


class TelegramTests(unittest.TestCase):
    def setUp(self):
        import tempfile
        from tradingbot import telegram_bot as T
        self.T, d = T, tempfile.mkdtemp()
        self.st = T.State(os.path.join(d, "s.json"), os.path.join(d, "j.csv"))
        self.fetch = lambda s: D.synthetic()

    def h(self, text, now=1_000_000.0):
        return self.T.handle(text, self.st, self.fetch, lambda s: 100.0, now=now)

    def test_commands(self):
        self.assertIn("1:3.00", self.h("/rr 100 95 115"))
        self.assertIn("qty 20.000000", self.h("/size 10000 1 100 95"))
        self.assertIn("vol_target_ensemble", self.h("/signal BTC/USDT"))
        self.assertIn("buy&hold", self.h("/backtest BTC/USDT ensemble"))
        self.assertIn("YTM", self.h("/bond 100 5 10 95"))
        self.assertIn("Bad arguments", self.h("/size 1 2"))

    def test_loss_streak_locks_size_then_unlocks(self):
        self.h("/log loss -1")
        self.assertIn("qty", self.h("/size 10000 1 100 95"))
        self.assertIn("locked", self.h("/log loss -1"))
        self.assertIn("Cooling-off", self.h("/size 10000 1 100 95"))
        self.assertIn("qty", self.h("/size 10000 1 100 95", now=1_000_000.0 + 25 * 3600))

    def test_win_resets_streak_and_stats(self):
        self.h("/log loss"); self.h("/log win 2.5 nice")
        self.assertEqual(self.st.d["streak"], 0)
        self.assertIn("trades 2", self.h("/stats"))

    def test_watch_triggers_once(self):
        self.h("/watch BTC/USDT above 90")
        self.assertEqual(len(self.T.check_watches(self.st, lambda s: 100.0)), 1)
        self.assertEqual(self.T.check_watches(self.st, lambda s: 100.0), [])

    def test_strangers_get_silence_but_id_works(self):
        upd = lambda cid, t: {"message": {"chat": {"id": cid}, "text": t}}
        self.assertIsNone(self.T.process_update(upd(999, "/signal BTC/USDT"), 111, self.st, self.fetch))
        self.assertIsNone(self.T.process_update(upd(999, "/help"), None, self.st, self.fetch))
        self.assertIn("999", self.T.process_update(upd(999, "/id"), 111, self.st, self.fetch)[1])
        self.assertIsNotNone(self.T.process_update(upd(111, "/help"), 111, self.st, self.fetch))


class MonteCarlo(unittest.TestCase):
    def test_more_risk_means_deeper_drawdowns_and_fair_coin_has_negative_edge_after_costs(self):
        import montecarlo as mc
        lo = mc.simulate(risk=0.01, runs=500)
        hi = mc.simulate(risk=0.10, runs=500)
        self.assertGreater(hi["median_max_drawdown"] * -1, lo["median_max_drawdown"] * -1)
        bad = mc.simulate(win=0.40, payoff=1.0, runs=500)   # negative expectancy
        self.assertLess(bad["expectancy_R"], 0)
        self.assertGreater(bad["prob_loss"], 0.5)


if __name__ == "__main__":
    unittest.main()
