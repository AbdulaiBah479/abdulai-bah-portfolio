# Risk math

## Position size
`qty = equity × risk% ÷ |entry − stop|`  ·  FX: `lots = equity × risk% ÷ (stop_pips × pip_value/lot)`  
Example: $10,000, 1%, entry 60,000, stop 58,500 → $100 ÷ 1,500 = 0.0667 BTC (notional $4,000 = 0.4× leverage).

## Reward:risk vs breakeven win rate (before costs)
| R:R | Breakeven win % |
|---|---|
| 1:1 | 50 |
| 1:1.5 | 40 |
| 1:2 | 33.3 |
| 1:3 | 25 |
| 1:4 | 20 |
Formula: `breakeven = risk ÷ (risk + reward)`. Add costs: effective R shrinks.

## Expectancy
`E = win% × avg win − loss% × avg loss` (per trade, in R). Need E > 0 after costs. 40% win, 2R wins, 1R losses → 0.4×2 − 0.6×1 = **+0.2R**.

## Drawdown recovery
| Loss | Gain needed |
|---|---|
| 10% | 11% |
| 20% | 25% |
| 30% | 43% |
| 50% | 100% |
| 75% | 300% |
Hence the drawdown kill-switch.

## Losing streaks (probability of N losses in a row)
At 50% win rate: 5 in a row ≈ 3% per sequence, but over 100 trades you'll likely see a streak of 6–7. At 1% risk, 10 losses = −9.6%. Size so a 15-loss streak is survivable.

## Kelly
`f* = p − (1−p)/b` (b = payoff ratio). Use ¼ Kelly or less; estimates are noisy. `risk.kelly_fraction`.

## Volatility sizing
Risk-parity-ish: `size ∝ target_vol ÷ asset_vol`. ATR stop: `stop = entry − k×ATR(14)`, k = 2–3.

## Leverage & liquidation (long, isolated)
Approx liquidation ≈ `entry × (1 − 1/leverage + maintenance_margin)`. At 10× you're liquidated near −9%; at 20×, ≈ −4.5%. Crypto 5% daily swings make high leverage fatal.

## Compounding
`FV = P(1+r)^n` + contributions. `python bot/tools/calc.py compound --start 1000 --monthly 200 --rate 0.07 --years 20`. Rule of 72: years to double ≈ 72 ÷ return %.

## Costs
Round-trip cost = 2×(fee + slippage) + spread. 0.1% fee + 0.05% slip each side = 0.3% per round trip: 100 round trips/year drains 30% of the account if the strategy only breaks even.

## Portfolio risk
Correlated positions are one position. Cap per-asset (≤ 25% crypto, ≤ 5% single stock), per-sector, and total open risk (≤ 5%).
