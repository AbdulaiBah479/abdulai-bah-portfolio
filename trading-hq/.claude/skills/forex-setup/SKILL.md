---
name: forex-setup
description: Analyse a forex pair setup: trend, levels, session, news risk, lots and pip risk.
---
# Forex setup
Pull pair data and the economic calendar (cite sources). Steps: D1/H4 trend -> key levels -> session/liquidity -> news within 24h -> entry/stop in pips (ATR) -> lots via `python3 bot/tools/calc.py fxsize` -> R:R -> swap/spread cost. Use `docs/02-forex.md` and `docs/cheatsheets/forex-pairs-and-sessions.md`. Warn about leverage. Not advice.
