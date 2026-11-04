---
name: trade-plan
description: Build a complete, risk-first trade plan (entry, stop, size, targets, invalidation) for a crypto, FX or stock idea. Use when the user proposes or asks about a trade.
---
# Trade plan
1. Ask (if missing): market/symbol, timeframe, account size, risk % (default 1%), direction, thesis.
2. Fetch current data (never quote remembered prices). State source + timestamp. If no data access, ask the user for price/levels.
3. Output a table: Entry, Stop (with ATR/structure reason), Target(s) in R, R:R, size via `python3 bot/tools/calc.py size|fxsize`, leverage implied, max loss $, breakeven win rate.
4. List: invalidation, key levels, upcoming events (calendar), correlation with existing positions, costs.
5. Run `docs/cheatsheets/pre-trade-checklist.md`. Mark each item pass/fail.
6. If R:R < 1:2, risk > 1%, no stop, leverage > 3x, or illiquid: say it fails and propose fixes.
7. End with: educational analysis, not advice; no guaranteed outcome.
