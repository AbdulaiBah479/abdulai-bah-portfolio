# 02 · Forex (FX)

## Basics
- Quote `EUR/USD = 1.0850`: 1 EUR costs 1.0850 USD. Base/quote. Buy = long base.
- **Pip**: 0.0001 (0.01 for JPY pairs). **Pipette**: 1/10 pip. **Lot**: standard 100,000 · mini 10,000 · micro 1,000.
- Pip value on XXX/USD pairs ≈ $10 / std lot, $1 / mini, $0.10 / micro. Others: convert to account currency.
- Spread = ask − bid (your cost). Swap/rollover = interest differential paid/received overnight.
- Leverage multiplies gains **and** losses; margin call/stop-out closes you automatically.

## Pairs
Majors (tightest spreads): EUR/USD, USD/JPY, GBP/USD, USD/CHF, AUD/USD, USD/CAD, NZD/USD.
Minors/crosses: EUR/GBP, EUR/JPY, GBP/JPY… Exotics (USD/ZAR, USD/TRY): wide spreads, gap risk → avoid.

## Sessions (UTC, approx; shift with DST)
Sydney 21–06 · Tokyo 00–09 · London 07–16 · New York 12–21. Best liquidity: **London/NY overlap 12–16**. Spreads widen at rollover (~21–22) and around news.

## What moves FX
Interest-rate expectations (central banks: Fed, ECB, BoE, BoJ, SNB, RBA, BoC, RBNZ) · inflation (CPI) · jobs (NFP) · GDP/PMI · risk sentiment · commodities (CAD, AUD, NOK) · geopolitics. Calendar: Forex Factory / Investing.com / central bank sites.

## Costs & broker selection
Prefer regulated brokers (FCA, ASIC, CySEC, NFA/CFTC…) with ECN/raw spread + small commission, negative balance protection, segregated funds. Check: spread on EUR/USD in live hours, execution speed, withdrawal record. Retail CFD accounts show most clients lose.

## Beginner-safe approach
1. Demo 60+ days (MetaTrader 5, cTrader, TradingView paper).
2. Trade 1–2 majors, one session, H1/H4/Daily; ≤ 1% risk, stop always set, leverage ≤ 5× effective.
3. Trade with the higher-timeframe trend; avoid 30 min either side of red-folder news.
4. Position size: `lots = equity × risk% ÷ (stop_pips × pip_value)` → `python bot/tools/calc.py fxsize --equity 5000 --risk 0.01 --pips 40`.

## Setups (see 07 & cheatsheets)
Trend pullback to 20/50 EMA · support/resistance break-retest · London breakout of Asian range · carry (only with proper hedging/diversification; crashes hard) · mean reversion in ranges (RSI/Bollinger).

## Automation
MetaTrader 5 Expert Advisors (MQL5) · `MetaTrader5` Python package (Windows) · OANDA v20 API (`oandapyV20`) · cTrader Open API · Alpaca does not do FX · Freqtrade is crypto only. Backtest with tick/1-min data incl. spread; many FX backtests ignore variable spreads and are too optimistic.

## Red flags
"Signal groups," prop-firm challenge mills with unrealistic claims, EAs with Martingale/grid (blow up eventually), 500:1 leverage, unregulated offshore brokers, deposit bonuses with lock-ins.
