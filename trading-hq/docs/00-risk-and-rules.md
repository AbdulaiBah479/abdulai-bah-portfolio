# 00 · Risk, rules and the plan

## Reality check
- Most retail day traders lose money; broker disclosures for FX/CFDs commonly show roughly 70–80% of retail accounts losing. Check your broker's own risk-disclosure percentage.
- Costs (spread, fees, slippage, tax) are certain; profits are not.
- The only free lunch is diversification. The only controllable variable is risk.
- A strategy's backtest is an upper bound on live results.

## The ten rules
1. Risk ≤ **1%** of account per trade (0.5% while learning). Never more than **5%** total open risk.
2. Every trade has a stop **before** entry. Never widen a stop; never average down on a loser.
3. Minimum reward:risk **1:2** unless win rate is proven higher (see breakeven table in cheatsheets/risk-math).
4. Daily loss limit **3%**, monthly **8%**, drawdown kill-switch **15%** → stop, review, paper trade again.
5. No leverage while learning. Spot only. Later: ≤ 2–3× effective leverage.
6. Only trade liquid instruments. Avoid new/illiquid coins, penny stocks, exotic FX.
7. Don't trade news spikes, thin sessions, or when tired/angry/bored/chasing losses.
8. One strategy at a time, tested out-of-sample, ≥ 30 trades before trusting.
9. Journal every trade (`journal/TEMPLATE.md`). Review weekly.
10. Keep 6 months of expenses in cash **outside** trading. Trade only "can lose it all" money.

## Position sizing in one line
`qty = (account × risk%) ÷ |entry − stop|` → `python bot/tools/calc.py size ...`

## Account structure (suggested for a beginner)
| Bucket | % | Purpose |
|---|---|---|
| Emergency fund | outside | 3–6 months expenses |
| Core (index ETFs, dividend growth, bonds) | 70–90% | Boring compounding; baseline to beat |
| Satellite (active crypto/FX/stocks) | 5–20% | Learning + upside; can go to zero |
| Cash/dry powder | 5–10% | Rebalancing, opportunities |

## Psychology
FOMO, revenge trading, overtrading, moving stops, hope, over-leverage, confirmation bias, recency bias.
Counter with: checklist before every trade, max trades/day, written plan, walking away after 2 losses in a row.

## Legal / tax / safety (check your country)
- Capital gains / income / dividend / crypto tax; keep exports of every trade (`cheatsheets/tax-and-journal.md`).
- Use regulated brokers; verify licence on the regulator's register (FCA, SEC/FINRA, ASIC, CySEC…). Avoid "signal sellers", "guaranteed return" schemes, copy-trade scams, recovery scams, pig-butchering. If someone DMs you about trading profits, it's a scam.
- Binance availability and rules differ by country (e.g. Binance.US vs Binance.com); confirm eligibility and local law.
- 2FA (authenticator app / hardware key), unique passwords, anti-phishing code, withdrawal whitelist.

## Kill-switch protocol
Hit a limit → close or leave positions per plan → no trading 48h → write what happened → revert to paper → resume only after 20 paper trades following the plan.
