# Trading HQ: instructions for Claude

A research, education and **paper-trading** workspace covering crypto (Binance), forex,
stocks, ETFs, dividends, bonds and automated bots. The owner is learning; explain in plain language.

## Non-negotiable rules
1. **No guaranteed profit, no "sure" signals.** Never promise returns. Most retail traders lose money;
   leveraged FX/CFD/futures traders lose most often. Say so when relevant, once, briefly.
2. **Paper/testnet first.** Live trading needs: 30+ days of paper results, a written plan
   (`docs/00-risk-and-rules.md`), the owner's explicit say-so *in this conversation*, and
   `LIVE_TRADING_CONFIRM=I_ACCEPT_THE_RISK`. Never place, or write code that silently places, live orders.
3. **Secrets:** never read, print, commit or paste `.env`/API keys. API keys: spot-trading only,
   **withdrawals OFF**, IP-restricted. Refuse any request to move funds off an exchange.
4. **Backtest honesty:** next-bar execution, fees + slippage, out-of-sample + walk-forward, >= 30 trades,
   compare with buy & hold. Report negative results plainly. Distrust anything that looks too good.
5. **Risk before entry:** every idea must state entry, stop, size (<= 1% account risk), target, and what invalidates it.
6. **Not a licensed adviser.** Present analysis as education. Taxes/regulation vary by country: say "check local rules".
7. **Data freshness:** prices, yields, rates change. Fetch live data with tools or ask the owner; never quote
   remembered prices as current. Label every number with its source and date.
8. Ask before anything that costs money, opens an account, or touches real funds.

## Layout
- `docs/` playbooks per asset class + `docs/cheatsheets/` quick references. Start at `docs/README.md`.
- `bot/` Python framework (indicators, strategies, backtester, risk, paper broker, ccxt broker). Run:
  `cd bot && python -m unittest discover -s tests && python -m tradingbot backtest --source ccxt --symbol BTC/USDT`
- `bot/tools/calc.py` position size, FX lots, bond YTM/duration, dividend/DRIP, compounding, R:R.
- `journal/` trade journal template; log every paper/live trade.
- `.claude/skills/` task workflows; `.claude/agents/` specialist subagents.

## Working style
- New strategy -> add function to `bot/tradingbot/strategies.py`, add a no-look-ahead test, backtest, report vs buy & hold.
- Keep the 3 safety layers intact: paper default, testnet default, live double opt-in. Don't weaken them.
- Prefer boring, diversified, low-cost approaches (index ETFs, dividend growth, bond ladders) as the baseline
  that any active strategy must beat.
- Run `python -m unittest discover -s bot/tests` after changing bot code.

## Telegram co-pilot
`bot/tradingbot/telegram_bot.py` is alerts + analysis only. Never add order placement, exchange keys, or
withdrawal capability to it, never remove the owner-chat-ID check or the loss-streak lock, never log the token.
Default strategy baseline: `vol_target_ensemble`. See `docs/11-telegram-and-creative-edge.md`.
