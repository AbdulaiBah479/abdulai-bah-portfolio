# 04 · Dividends & income investing

## Key dates
**Declaration** → **Ex-dividend date** (own shares *before* it to receive; price drops ≈ dividend) → **Record date** → **Payment date**. Buying just before ex-date gives no free money: price adjusts, and tax may apply.

## Metrics
| Metric | Formula | Healthy range |
|---|---|---|
| Dividend yield | DPS ÷ price | 2–5% (>8% often signals a cut risk) |
| Payout ratio | DPS ÷ EPS | <60% (REITs: use FFO/AFFO, <85%) |
| FCF payout | Dividends ÷ FCF | <70% |
| Dividend growth rate (5y CAGR) | | >5% |
| Years of growth | | Aristocrats 25+, Kings 50+ |
| Debt/EBITDA, interest cover | | <3×, >5× |
| Yield on cost | Annual dividend ÷ your cost | grows over time |

## Strategies
- **Dividend growth**: quality companies raising payouts yearly (e.g. universe: S&P 500 Dividend Aristocrats; ETFs like SCHD, VIG, NOBL, DGRO, VYM, ex-US: VIGI, IDV, UK: VHYL — verify current holdings and fees).
- **High yield**: higher yield, higher cut risk; diversify (REITs, utilities, BDCs, covered-call ETFs trade upside for income).
- **DRIP** (reinvest) compounds: `python bot/tools/calc.py dividend --price 50 --dps 2 --shares 100 --growth 0.06 --years 20`.
- **Dividend capture**: usually not worth it after costs/taxes.
- **Total-return mindset**: dividends are just part of return; selling shares can substitute for dividends.

## Traps
Yield trap (price collapsing) · payout >100% · falling FCF · heavy debt · cyclicals (energy/shipping) variable dividends · special one-offs counted as regular · currency risk · withholding tax on foreign dividends (treaty rates, forms like W-8BEN) · tax on reinvested dividends.

## Screening recipe (see `/dividend-screen`)
1. Yield 2–6%, payout <65%, 5y dividend CAGR >4%, ≥10y without a cut.
2. Debt/EBITDA <3, interest cover >5, positive FCF 5/5 years.
3. ROIC > cost of capital; sector-diversified (≤25% per sector).
4. Valuation: yield above own 5y average, P/E ≤ sector, or FCF yield >4%.
5. Position cap 5%; 15–25 holdings (or just buy an ETF).

## Income planning
Target income ÷ yield = capital needed (e.g. $1,000/mo at 4% → $300k). Mix: dividend ETFs + bond ladder + cash buffer for 12 months. Track in the journal sheet; plan calendar of pay dates.

## Free data
Yahoo/`yfinance` (`Ticker.dividends`), Nasdaq dividend calendar, Dividend.com, Digrin, Dividend Channel, company IR pages, SEC filings.
