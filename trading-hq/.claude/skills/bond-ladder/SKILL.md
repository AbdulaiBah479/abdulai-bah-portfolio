---
name: bond-ladder
description: Design a bond or treasury ladder / fixed-income allocation with yield, duration and rate-shock numbers.
---
# Bond ladder
Ask: amount, currency/country, horizon, tax status, income vs growth need, risk tolerance.
Design rungs (e.g. 1-5y or 1-10y), choose instruments (government, inflation-linked, IG corporate, ETFs vs individual), compute YTM/duration with `python3 bot/tools/calc.py bond`, show +-1% rate shock impact, reinvestment rule, concentration/credit limits, tax notes. Current yields must come from a live source (FRED/Treasury/broker); cite date.
