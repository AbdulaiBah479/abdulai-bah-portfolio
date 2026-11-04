---
name: dividend-screen
description: Screen and rank dividend stocks/ETFs for safety, growth and valuation; build an income plan.
---
# Dividend screen
Criteria from `docs/04-dividends.md`: yield 2-6%, payout <65% (REIT AFFO <85%), 5y DPS CAGR >4%, no cuts 10y, net debt/EBITDA <3, interest cover >5, FCF positive, sector cap 25%.
Get data via yfinance (`Ticker.dividends`, `.info`) or other sources; show formulas and dates. Flag yield traps. Output ranked table + risks + suggested weights (max 5% each) + yearly income projection (`python3 bot/tools/calc.py dividend ...`). Mention ETFs as the lower-effort alternative. Mention tax/withholding by country.
