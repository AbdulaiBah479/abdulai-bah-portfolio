# 09 · Resources: GitHub repos, tools, data, learning

> **Verification note:** this list was compiled from knowledge, not live-checked (no GitHub API access in the build session).
> Before depending on any repo: check last commit date, open issues, licence, stars. Prefer maintained repos. Never run code you haven't read, and never paste API keys into third-party tools.

## Trading bots & execution frameworks
| Repo | Use |
|---|---|
| `freqtrade/freqtrade` | Crypto bot: backtest, hyperopt, dry-run, Telegram/web UI, FreqAI (ML) |
| `freqtrade/freqtrade-strategies` | Community strategy samples (learn from; most don't work live) |
| `hummingbot/hummingbot` | Market making, arbitrage, many CEX/DEX connectors |
| `jesse-ai/jesse` | Crypto research/backtest/live with clean strategy API |
| `Drakkar-Software/OctoBot` | Crypto bot with UI, grid/DCA, TradingView webhooks |
| `nautechsystems/nautilus_trader` | High-performance event-driven engine (Rust+Python) |
| `QuantConnect/Lean` | Multi-asset engine (stocks, FX, crypto, options); cloud/local |
| `mementum/backtrader` | Classic Python backtester/live (maintenance-mode) |
| `kernc/backtesting.py` | Minimal, easy backtester with plots |
| `polakowo/vectorbt` | Very fast vectorised backtesting/analysis |
| `stefan-jansen/zipline-reloaded` | Maintained fork of Quantopian Zipline |
| `robcarver17/pysystemtrade` | Systematic futures trading framework (Carver) |
| `alpacahq/alpaca-py`, `alpacahq/lumibot` | US stocks/crypto/options API + strategy framework |
| `ccxt/ccxt` | Unified API for 100+ crypto exchanges (incl. Binance) |
| `binance/binance-connector-python` | Official Binance connectors |
| `oanda/v20-python` / `hootnot/oanda-api-v20` | OANDA FX API |
| `ib-api-reloaded/ib_async` (successor to `ib_insync`) | Interactive Brokers API |

## Data, analysis, indicators, portfolio
| Repo | Use |
|---|---|
| `OpenBB-finance/OpenBB` | Open investment research platform, many data sources, AI/MCP hooks |
| `ranaroussi/yfinance` | Yahoo data (unofficial) |
| `ranaroussi/quantstats` | Performance tear sheets |
| `pmorissette/ffn`, `pmorissette/bt` | Finance functions, flexible backtests |
| `PyPortfolio/PyPortfolioOpt`, `dcajasn/Riskfolio-Lib` | Portfolio optimisation, risk parity |
| `TA-Lib/ta-lib-python`, `twopirllc/pandas-ta`, `bukosabino/ta` | Technical indicators |
| `skfolio/skfolio` | scikit-learn style portfolio optimisation |
| `mortada/fredapi` | FRED macro/yield data |
| `edgartools` / `dgunning/edgartools` | SEC EDGAR filings in Python |

## AI / ML / agents (research, treat outputs sceptically)
| Repo | Use |
|---|---|
| `AI4Finance-Foundation/FinRL`, `FinRobot`, `FinGPT` | RL trading, LLM finance agents |
| `microsoft/qlib` | Quant ML platform |
| `TauricResearch/TradingAgents` | Multi-agent LLM trading research framework |
| `virattt/ai-hedge-fund` | Educational multi-agent hedge-fund demo |
| `asavinov/intelligent-trading-bot` | ML signal bot |
| Claude Code + MCP servers (market data, Binance, Alpaca, OpenBB MCP) | Natural-language research and tooling |

## Learning / lists
`wilsonfreitas/awesome-quant` · `georgezouq/awesome-ai-in-finance` · `je-suis-tm/quant-trading` · `stefan-jansen/machine-learning-for-trading` · `firmai/financial-machine-learning` · `ranaroussi` blog · `public-apis/public-apis` (finance section).

## Free data & tools (no GitHub needed)
- Charts/alerts/paper: **TradingView** (free tier), Thinkorswim paper, MT5 demo.
- Crypto: Binance public API & testnet, CoinGecko, DefiLlama, Coinglass.
- Stocks: Yahoo, Finviz, SEC EDGAR, Stockanalysis, Alpha Vantage, Finnhub, Twelve Data, Polygon (free tiers), Stooq (CSV).
- Macro/bonds: FRED, ECB/BoE data portals, US Treasury, World Bank, IMF.
- FX/economic calendar: Forex Factory, Investing.com, TradingEconomics (limited), central-bank sites.
- Sentiment: Fear & Greed, AAII, CBOE put/call, COT reports (CFTC).
- Screeners: Finviz, TradingView, Barchart, Koyfin (free tier).

## Books & courses (high signal)
*The Intelligent Investor* (Graham) · *A Random Walk Down Wall Street* (Malkiel) · *The Little Book of Common Sense Investing* (Bogle) · *Trading in the Zone* (Douglas) · *Following the Trend* (Clenow) · *Advances in Financial Machine Learning* (López de Prado) · *Systematic Trading* (Carver) · *Options as a Strategic Investment* (McMillan) · *Fixed Income Securities* (Tuckman) · Investopedia, Babypips (forex school, free), Khan Academy finance, Coursera/edX finance courses.

## Claude / MCP ideas
Connect a market-data MCP server (e.g. OpenBB, Alpha Vantage, yfinance, CoinGecko), a broker MCP (Alpaca paper), and use skills in `.claude/skills`. Review every MCP server's code/permissions first; give it read-only or paper credentials.
