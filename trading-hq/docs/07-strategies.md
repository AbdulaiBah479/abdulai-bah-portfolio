# 07 · Strategies catalogue

Every strategy = **edge hypothesis + entry + exit + sizing + costs + failure mode**. If you can't state why it should work and who's on the other side, don't trade it.

| # | Strategy | Markets | Edge hypothesis | Typical failure | In `bot/`? |
|---|---|---|---|---|---|
| 1 | Buy & hold index + DCA | Stocks, BTC | Risk premium, no timing | Deep drawdowns, behaviour | `buy_and_hold` baseline |
| 2 | Trend following (SMA cross / EMA filter / Donchian) | All liquid | Behavioural under-reaction, momentum | Whipsaw in ranges; many small losses, few big wins | `sma_cross`, `ema_trend`, `donchian_breakout` |
| 3 | Mean reversion (RSI/Bollinger) | Stocks/ETFs/FX ranges | Overreaction snaps back | Trends crush it ("catching knives") | `rsi_reversion` |
| 4 | Momentum rotation (top-N by 6–12m return, monthly) | ETFs/stocks/crypto | Cross-sectional momentum | Crashes at reversals | todo |
| 5 | Dual momentum / trend-filtered allocation | ETFs | Avoid bear markets | Lag, whipsaw | via `ema_trend` |
| 6 | Dividend growth | Stocks | Quality + income | Concentration, valuation | docs/04 |
| 7 | Value / quality factor tilts | Stocks | Risk premia | Decade-long droughts | ETFs |
| 8 | Grid trading | Crypto ranges | Harvest chop | Strong trend one way = heavy bags | Binance grid bot |
| 9 | DCA/value averaging | Crypto/stocks | Discipline | Same as holding | manual/Recurring Buy |
| 10 | Breakout (opening range, London range) | FX/futures | Volatility expansion | False breaks | todo |
| 11 | Pairs / stat-arb | Stocks/crypto | Cointegration | Relationship breaks | advanced |
| 12 | Carry (FX, funding rate/basis) | FX, crypto | Collect yield | Sudden unwinds | advanced, avoid early |
| 13 | Market making | Crypto | Capture spread | Inventory risk, adverse selection | Hummingbot |
| 14 | Options income (covered calls, CSP) | Stocks | Sell volatility premium | Capped upside / crash | manual |
| 15 | ML/RL | Any | Pattern extraction | Overfitting, regime shift | FinRL, Qlib (research only) |

## Entry/exit toolkit
Stops: ATR-based (2–3× ATR), structure-based (below swing low), time stop. Targets: R-multiples (2R, 3R), trailing (Chandelier/ATR), partial profits at 1R with trail on rest.

## Filters
Trend (price > 200 EMA) · volatility (ATR percentile) · liquidity (volume) · session/time · news blackout · market regime (VIX, BTC dominance).

## Rules for adopting a strategy
1. Written hypothesis. 2. Backtest with costs. 3. Out-of-sample + walk-forward. 4. Parameter neighbourhood stable (±20% params still work). 5. ≥ 30 trades, multiple regimes/assets. 6. Paper trade 30 days; live results within expected drawdown range. 7. Size small, scale slowly. 8. Pre-define the "stop trading it" criteria.

## Common backtest sins
Look-ahead (using the same bar's close), survivorship bias (only today's winners), ignoring fees/slippage/funding, overfitting parameters, data snooping across hundreds of variants, too few trades, unrealistic fills, ignoring tax.
