# Trading HQ

One workspace for learning and practising **crypto (Binance), forex, stocks, ETFs, dividends, bonds**, and
building an **automated bot**: safely, with paper trading by default.

> Honest note: there is no "best bot" that reliably prints money. What exists: good risk management,
> low costs, diversification, patience, and testing ideas rigorously before risking cash. This project is
> built around that.

## Quick start
```bash
cd trading-hq/bot
pip install -r requirements.txt
python -m unittest discover -s tests                         # 18 tests should pass
python -m tradingbot rotate --source ccxt                    # multi-asset momentum rotation
python -m tradingbot telegram                                # private Telegram co-pilot (see docs/11)
python -m tradingbot backtest --strategy donchian_breakout   # synthetic data demo
python -m tradingbot backtest --source ccxt --symbol BTC/USDT --timeframe 1d --limit 1000
python -m tradingbot backtest --source yfinance --symbol SPY --ppy 252
python -m tradingbot paper --source ccxt --symbol ETH/USDT --strategy sma_cross
python tools/calc.py size --equity 10000 --risk 0.01 --entry 60000 --stop 58500
```
Open the folder in Claude Code (`claude` inside `trading-hq/`) and use the skills below.

## Map
| Topic | Doc |
|---|---|
| Rules, risk, psychology, the plan | `docs/00-risk-and-rules.md` |
| Binance / crypto | `docs/01-binance-crypto.md` |
| Forex | `docs/02-forex.md` |
| Stocks, shares, ETFs | `docs/03-stocks-shares-etfs.md` |
| Dividends / income | `docs/04-dividends.md` |
| Bonds & fixed income | `docs/05-bonds.md` |
| Options, futures, commodities, other | `docs/06-other-instruments.md` |
| Strategies catalogue | `docs/07-strategies.md` |
| Backtesting & automation / bots | `docs/08-backtesting-and-bots.md` |
| GitHub repos, tools, data, learning | `docs/09-resources.md` |
| Roadmap (30/90/180 days) | `docs/10-roadmap.md` |
| Telegram co-pilot + creative ideas | `docs/11-telegram-and-creative-edge.md` |
| Cheat sheets | `docs/cheatsheets/` |

## Claude skills (`.claude/skills`)
`/trade-plan` · `/risk-check` · `/backtest-strategy` · `/market-brief` · `/dividend-screen` ·
`/bond-ladder` · `/forex-setup` · `/crypto-bot-review` · `/journal-review`

## Claude agents (`.claude/agents`)
`quant-dev` (builds/tests bot code) · `risk-officer` (vetoes unsafe plans) · `market-researcher` (sourced briefs)
· `portfolio-planner` (allocation, income, rebalancing)

## Not financial advice
Educational software. You can lose all the money you put in. Never trade money you can't afford to lose.
