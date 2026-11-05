# 11 · Telegram co-pilot & creative edge

## What "best Telegram trading bot" really means
Public Telegram trading bots (sniper bots, copy-trade bots, "signal" channels, "AI profit" bots) are where
many retail users lose money: they ask for private keys or deposits, front-run you, pump tokens to exit on you,
or are plain scams. **Never give a Telegram bot your seed phrase, exchange withdrawal rights, or a deposit.**
The best Telegram bot is one **you** run, that only talks to **you**, and that **cannot move money**.
That is what `bot/tradingbot/telegram_bot.py` is.

## Set up (10 minutes)
1. Telegram → `@BotFather` → `/newbot` → copy the token.
2. `cd bot && cp .env.example .env`, put `TELEGRAM_BOT_TOKEN` in it, then `export $(grep -v '^#' .env | xargs)` (or use python-dotenv / your shell).
3. `python3 -m tradingbot telegram`, message your bot `/id`, put the number in `TELEGRAM_CHAT_ID`, restart.
4. Run it on a small always-on box (Raspberry Pi, cheap VPS, or a home PC) with `systemd`/`docker --restart`.

## Commands
`/signal BTC/USDT [strategy]` · `/backtest SPY vol_target_trend` · `/size 10000 1 60000 58500` · `/rr` · `/bond` ·
`/watch BTC/USDT above 70000` · `/watches` · `/unwatch 1` · `/log win|loss [R] [note]` · `/stats` · `/pause` · `/resume` · `/status`
Daily digest at `DIGEST_HOUR_UTC` for `WATCHLIST`; price alerts checked every minute.

## Safety design
- Only the owner chat ID gets replies; strangers get silence (`/id` is the only public command).
- No order placement, no exchange keys in the bot. Alerts and analysis only.
- Token never printed (loop errors log the exception type only).
- **Anti-revenge lock:** two logged losses in a row → `/size` refuses for 24h. Behaviour, not signals, is where most accounts die.

## The strategy stack (what to run, in order of "boring but robust")
| Rank | Strategy | Why it's credible | Command |
|---|---|---|---|
| 1 | `vol_target_ensemble` | Votes of 3 trend rules (less parameter luck) × volatility targeting (smaller size when markets are wild); never levered | `backtest --strategy vol_target_ensemble` |
| 2 | `vol_target_trend` | Single 100-EMA filter + vol sizing; simple | |
| 3 | Momentum rotation + cash filter | Trend-following across assets; goes to cash when nothing trends | `python3 -m tradingbot rotate --source ccxt` |
| 4 | `bb_squeeze` | Volatility compression → expansion | |
| 5 | Plain DCA into index/BTC | Beats most active traders after costs and behaviour | manual / Binance Recurring Buy |
Rule: a strategy is allowed on real money only if it beats buy & hold on **risk-adjusted** terms (Sharpe/max drawdown), after costs, out-of-sample, on several assets. Lower drawdown with similar return is a win even if raw return is lower.

## Creative / out-of-the-box ideas (each with its catch)
1. **Alerts-first trading**: let the bot watch, you decide. Removes execution bugs and most impulsive trades.
2. **Behavioural firewall** (built): cooling-off lock after 2 losses; extend with a max-trades-per-day counter.
3. **Cash-flow sleeve**: route every dividend/coupon/salary-surplus into the most underweight bucket in `journal/portfolio-tracker.csv` → rebalances for free, no selling, no tax events.
4. **Regime switch**: hold the trend strategy only when price > 200-day MA, otherwise T-bills/stable-yield. Catch: lag and whipsaw.
5. **Barbell**: 85–90% boring core (index + bonds), 10–15% experiments with a hard budget; when a strategy graduates (30+ paper trades, positive after costs), allocate 1% risk, not more.
6. **Pre-mortem**: before each trade, `/log` a one-line "this fails if…". Review failures monthly; patterns reveal your leaks.
7. **Event calendar bot**: digest FOMC/CPI/NFP dates and pause new entries around them (add a calendar feed to `daily_digest`).
8. **Funding-rate / Fear & Greed dashboard**: extreme positive funding or greed = crowded long → reduce size (a size filter, not a signal).
9. **LLM as analyst, not oracle**: use Claude (`/market-brief`, `/risk-check`, `/crypto-bot-review`) to summarise filings/news, audit code and attack your thesis ("argue the other side"). Never to predict price.
10. **Tax-aware rebalancing**: harvest losses where legal, prefer tax-advantaged accounts for high-turnover ideas.
11. **Paper-vs-live shadow**: run the live pilot and the paper twin together; if live drifts from paper (slippage, fees), find out why before scaling.
12. **Kill-switch by design**: separate process that flattens/halts if drawdown > limit or heartbeat is lost.
13. **Income ladder**: coupons and dividends scheduled to cover monthly bills; trading profits only on top.
14. **Pair of independent signals**: only act when a trend rule and a macro/risk filter (VIX, credit spreads, BTC dominance) agree.

## Things that do NOT work (don't build)
Martingale/"recovery" grids · latency arbitrage for retail · "AI predicts price" subscriptions · copy-trading strangers · pump groups · leverage to "speed up" a small account.

## Hardening checklist for the always-on bot
Dedicated low-privilege user · token in env or secret store · firewall, SSH keys only · log rotation · restart-on-fail · tests green before deploy (`python3 -m unittest discover -s tests`) · pin dependencies.
