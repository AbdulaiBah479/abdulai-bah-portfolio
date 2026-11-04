# 08 · Backtesting & automated bots

## The pipeline (follow it in order)
1. **Idea** → written hypothesis.
2. **Data** → clean OHLCV (adjusted for splits/dividends for stocks). Split: train / validate / untouched test.
3. **Backtest** with `python -m tradingbot backtest ...` (next-bar fills, fees, slippage).
4. **Robustness**: in/out-of-sample, walk-forward windows, parameter sweeps (look for a plateau, not a spike), other symbols/timeframes, Monte-Carlo shuffle of trades.
5. **Paper** with `python -m tradingbot paper` or exchange testnet/dry-run for ≥ 30 days.
6. **Live pilot**: ≤ 5% of intended size, hard daily-loss limit, alerts, kill switch.
7. **Monitor** vs expectations (live Sharpe, drawdown inside 1.5× backtest MaxDD); retire when it breaks.

## Metrics
CAGR · Sharpe (>1 ok, >2 suspicious) · Sortino · Max drawdown · Calmar · Profit factor (>1.3) · Win rate × payoff · Exposure · Trade count · Turnover · Tail loss. Compare to buy & hold.

## Bot architecture (what `bot/` implements)
`data` → `indicators` → `strategies` (target position) → `risk` (size, limits, kill switch) → `broker` (paper | ccxt testnet | ccxt live behind double opt-in) → logs/journal.

## Production checklist for any bot
- [ ] Idempotent: restart-safe, reads state from exchange, no duplicate orders (use client order IDs)
- [ ] Rate limits and retries with backoff; handles network/exchange outages
- [ ] Precision & min-notional/lot-size filters respected
- [ ] Max position, max daily loss, max drawdown, max orders/min
- [ ] Stop-loss placed on exchange (OCO/stop orders), not just in bot memory
- [ ] Secrets in env; keys without withdrawal; IP-whitelisted
- [ ] Logging, alerting (Telegram/Discord), heartbeat
- [ ] Clock sync (NTP); time-in-force; handles partial fills
- [ ] Runs on a VPS/Raspberry Pi/Docker with auto-restart; tested failure modes
- [ ] Dry-run and testnet parity with live

## Choosing a framework
| Need | Pick |
|---|---|
| Crypto bot out-of-the-box with backtest, hyperopt, Telegram | **Freqtrade** |
| Market making / arbitrage / DEX | **Hummingbot** |
| Python algo-trading across assets; event-driven | **Nautilus Trader**, **QuantConnect LEAN**, **Backtrader/backtesting.py** |
| Fast vectorised research | **vectorbt**, **bt**, this repo's backtester |
| Stocks with broker API | **Alpaca (alpaca-py), Lumibot, IB (ib_async)** |
| FX | MetaTrader 5 / OANDA v20 / cTrader |
| ML / RL research | **FinRL, Qlib, scikit-learn, XGBoost** |
| No-code | Binance Grid/DCA, 3Commas, TradingView alerts + webhooks (check fees/security) |

## Using Claude for bots
Ask Claude to: write/review strategy code, add tests for no-look-ahead, build dashboards, summarise logs, write Pine Script/MQL5/Freqtrade strategies, review risk controls (`/crypto-bot-review`). Claude can't see the future; treat its signals as hypotheses to test.

## Alerts-only alternative
Many traders get most value from rules + alerts (TradingView / `tradingbot signal`) and manual execution: fewer infrastructure failure modes.
