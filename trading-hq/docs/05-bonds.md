# 05 · Bonds & fixed income

## Mechanics
Lend money for a coupon and get face value back at maturity. **Price and yield move inversely.**
- Coupon rate · Face/par (100) · Maturity · Current yield = coupon ÷ price · **YTM** = total annualised return if held to maturity.
- **Duration** ≈ % price change per 1% change in yield (modified duration 7 → −7% if yields +1%).
- Credit risk · interest-rate risk · inflation risk · reinvestment risk · liquidity · call risk · currency risk.
- Calculator: `python bot/tools/calc.py bond --face 100 --coupon 0.05 --years 10 --price 95`.

## Types
| Type | Notes |
|---|---|
| Government (T-bills <1y, T-notes 2–10y, T-bonds 20–30y; gilts; bunds) | Safest in own currency; state tax benefits vary |
| Inflation-linked (TIPS, ILBs, I-Bonds) | Protect purchasing power |
| Investment-grade corporate (BBB− and above) | Spread over governments |
| High yield / junk (BB+ and below) | Equity-like risk |
| Municipal (US) | Often tax-exempt |
| Emerging-market | Higher yield, currency/political risk |
| Convertible, preferred, perpetual/AT1 | Complex; skip until experienced |
| Money-market funds / short-term treasuries | Cash alternative |

## Ways to hold
- Individual bonds (hold to maturity → known outcome, minus default).
- **Ladder**: split money across maturities (1–5y) and reinvest maturing rungs. See `/bond-ladder`.
- **Bond ETFs/funds** (AGG/BND, BNDW, IEF/TLT, SHY, TIP, LQD, HYG, local equivalents): diversified, no maturity, price fluctuates with rates.
- Direct from treasury (TreasuryDirect, DMO gilts via broker, national savings).

## Rules of thumb
- Match duration to your horizon. Short horizon → short duration.
- Rates up → existing bond prices down; long bonds suffer most (2022 lesson).
- Yield curve: inverted (short > long) historically precedes recessions; spreads (HY−Treasury) show stress.
- Bonds diversify equities *usually* but not in inflation shocks (2022). Mix with cash/commodities/inflation-linked.
- Real yield = nominal − inflation; compare after tax.
- Check credit rating (S&P/Moody's/Fitch), covenants, issuer financials; never reach for yield blindly.

## Allocation heuristics (not advice)
Age-in-bonds (or 100/110 − age in stocks), or by goal: <3 yrs → mostly bonds/cash; 3–10 → mix; 10+ → mostly equities.

## Free data
FRED (yields, curves, spreads) · US Treasury (daily yield curve) · Bank of England/ECB data · FINRA bond data/TRACE · WorldGovernmentBonds · Morningstar fund pages · broker bond screeners.
