# Indicators cheat sheet

| Indicator | Type | Reading | Default | Caveat |
|---|---|---|---|---|
| SMA / EMA | Trend | Price above = uptrend; crossovers | 20/50/200 | Lagging; whipsaws in ranges |
| MACD | Trend/momentum | Line crosses signal; histogram | 12,26,9 | Lagging |
| ADX | Trend strength | >25 trending, <20 range | 14 | Non-directional |
| RSI | Momentum | >70 overbought, <30 oversold; in strong trends stays extreme | 14 | Overbought ≠ sell |
| Stochastic | Momentum | %K/%D cross in extremes | 14,3,3 | Noisy |
| Bollinger Bands | Volatility | Squeeze → expansion; band walk in trends | 20, 2σ | Not a reversal signal alone |
| ATR | Volatility | Stop distance, position sizing | 14 | Absolute units |
| Donchian | Breakout | N-bar high/low | 20/55 | Classic Turtle system |
| Ichimoku | Trend | Cloud = S/R and trend | 9,26,52 | Complex |
| VWAP | Volume/price | Intraday fair value | session | Resets daily |
| Volume / OBV | Confirmation | Breakout on rising volume | – | FX volume unreliable |
| Fibonacci | Levels | Retracements 38.2/50/61.8 | – | Self-fulfilling at best |
| Pivot points | Levels | Daily S/R | – | Intraday |

## Combining
Pick 1 trend + 1 momentum/entry + 1 volatility (stops). More indicators ≠ more edge (they're mostly the same price data).

## Python (this repo)
`from tradingbot import indicators as ind` → `sma, ema, rsi, atr, bollinger, donchian, macd`.

## Rules
- Parameters that only work at one exact value are overfit.
- Use higher timeframe for direction, lower for entry.
- Indicators describe, they don't predict.
