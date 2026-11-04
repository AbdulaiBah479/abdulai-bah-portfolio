---
name: risk-check
description: Audit a portfolio, trade list or bot config against the risk rules in docs/00-risk-and-rules.md and return pass/fail with fixes.
---
# Risk check
Inputs: positions (or `journal/portfolio-tracker.csv`), account size, bot config.
Check: per-trade risk <=1%; total open risk <=5%; single asset caps (crypto <=25%, stock <=5%); correlation clusters; leverage; stops present; daily/monthly/drawdown limits defined; emergency fund separate; API keys (no withdrawal, IP-limited); live-trading gates intact.
Output: table of rule / status / evidence / fix, then a verdict (GREEN / AMBER / RED) and top 3 actions. Be blunt.
