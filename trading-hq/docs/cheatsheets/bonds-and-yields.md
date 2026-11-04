# Bonds & yields

- Price ↑ ⇒ yield ↓. Par = 100. Price < 100 = discount (YTM > coupon).
- Current yield = annual coupon ÷ price. YTM includes pull-to-par.
- Price change ≈ −ModDuration × Δyield + ½ Convexity × Δyield².
- Duration examples: T-bill 0.25 · 2y ≈ 1.9 · 10y ≈ 8 · 30y ≈ 17–20. Bond ETF duration listed on fund page.
- Yield curve: normal (upward) / flat / inverted. 10y−2y and 10y−3m are recession watchers.
- Credit spread = corporate yield − Treasury yield (wider = stress).
- Ratings: AAA→BBB− investment grade; BB+ and below high yield.
- Tax-equivalent yield (munis) = muni yield ÷ (1 − tax rate).
- Real yield ≈ nominal − expected inflation (TIPS yield is the market real yield).
- Accrued interest: clean vs dirty price (dirty = clean + accrued).
- Ladder example, £/$50k over 5 rungs (1–5y): 10k each; at each maturity reinvest at the 5y end.
- Barbell (short + long) vs bullet (single maturity) vs ladder (even).

## Rate-sensitivity cheat
| Yields move | 2y bond | 10y bond | 30y bond |
|---|---|---|---|
| +1% | ≈ −1.9% | ≈ −8% | ≈ −17% |
| −1% | ≈ +1.9% | ≈ +8% | ≈ +17% |
(Approximate, ignoring coupon and convexity.)

CLI: `python bot/tools/calc.py bond --face 100 --coupon 0.045 --years 10 --price 97.5`
