---
name: backtest-strategy
description: Implement and honestly backtest a trading strategy with the bot/ framework (fees, slippage, next-bar fills, out-of-sample, walk-forward, vs buy and hold).
---
# Backtest a strategy
1. Write a hypothesis (why it should work, who loses). 2. Add the function to `bot/tradingbot/strategies.py` returning desired position (0/1/-1) and register it in STRATEGIES.
3. The existing test `test_no_lookahead_signals` covers all registered strategies; run `cd bot && python3 -m unittest discover -s tests`.
4. Run `python3 -m tradingbot backtest --strategy X --source ccxt|yfinance|csv ... --ppy 365|252`. Try >=3 symbols and 2 timeframes.
5. Report: metrics vs buy and hold, in/out-of-sample, walk-forward by window, trade count, parameter sensitivity (+-20%).
6. Verdict using `docs/07-strategies.md` adoption rules. Say plainly if it fails. Synthetic data is for testing code only.
