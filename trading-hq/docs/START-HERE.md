# START HERE: the complete beginner's guide to Trading HQ

You said you're new to all of this. This guide explains **every part of the project by category**: what it is, why it exists,
what I did, how I did it, what I used, and what *you* do with it. Unknown word? See `GLOSSARY.md`.

---------------------------------------------------------------------------

## 0. The big picture in 2 minutes

**Goal you gave me:** one place to learn and practise trading Binance/crypto, forex, stocks, shares, dividends, bonds and more,
with the best free tools, an automated bot, and cheat sheets.

**The honest truth first (this protects your money):**
1. There is no bot, signal, or Telegram group that reliably makes money. If one claims to, it is almost always a scam.
2. Most beginners lose money, mostly through *big position sizes, leverage, and emotion*, not because they lacked a clever indicator.
3. Therefore this project is built around **risk control + testing + learning first**, and *paper trading* (fake money) by default.

**How the pieces fit (think of a small trading firm with you as the owner):**

```
 Knowledge        Tools you run              Safety               Helpers
 ---------        -------------              ------               -------
 docs/ guides     bot/ (Python code)         risk rules           Claude skills  (/trade-plan ...)
 cheat sheets     backtester (test ideas)    paper money first    Claude agents  (risk-officer ...)
 glossary         Telegram co-pilot          loss-streak lock     journal/ (your trade diary)
 roadmap          calculators                live-trading locks
```

**Where everything lives** (folder `trading-hq/` in your GitHub repo):

| Folder / file | One-line meaning |
|---|---|
| `README.md` | Front page and quick commands |
| `CLAUDE.md` | The rulebook Claude reads automatically; keeps Claude safe and honest |
| `docs/` | All the learning guides (00–11) and this file |
| `docs/cheatsheets/` | One-page quick references |
| `bot/` | The Python software (research, backtests, paper trading, Telegram) |
| `bot/tools/` | Small calculators (position size, bonds, dividends, Monte Carlo) |
| `journal/` | Your trade diary template and portfolio tracker |
| `.claude/skills` and `.claude/agents` | Ready-made Claude helpers |

---------------------------------------------------------------------------

## 1. Category: the foundation, risk and rules (`docs/00`)

**What it is:** the rules that keep you alive. Surviving is step one; profit is step two.

**What I did / how:** wrote ten rules and a "kill-switch protocol" from standard professional practice (the same ideas used by
funds and prop firms): risk at most 1% of the account per trade, always use a stop, daily/monthly loss limits, no leverage while learning.

**Why it matters, in plain words:**
- *Risking 1% per trade* means 20 losses in a row still leaves you with ~82% of your money. Risking 20% per trade means 5 losses wipes you out.
- *A stop-loss* is an order that exits automatically when the trade goes against you by an amount you chose in advance.
- *Leverage* means trading with borrowed money, which multiplies gains **and** losses. It is the top account killer.

**What you do:** read `docs/00-risk-and-rules.md` once now and once a month. Write your own 1-page plan (the roadmap tells you how).

---------------------------------------------------------------------------

## 2. Category: each market, explained from zero

For every market I wrote a guide with: what it is, how it makes/loses money, costs, the main dangers, and a beginner-safe approach.

### 2a. Crypto and Binance (`docs/01`)
- **What:** digital coins (Bitcoin, Ethereum...) traded 24/7. Binance is an exchange (a marketplace).
- **Key lessons:** start with **Spot** (you buy actual coins); stay away from **Futures/Margin** (leverage → liquidation = forced loss of your money).
- **Security:** two-factor login with an authenticator app, withdrawal whitelist, hardware wallet for long-term coins, and bot API keys with *withdrawals OFF*.
- **Free practice:** Binance **Spot Testnet** gives fake money to practise bots safely.

### 2b. Forex (`docs/02`)
- **What:** trading one currency against another (EUR/USD). Prices move in **pips** (0.0001). Sizes are **lots**.
- **Key lessons:** sessions (London/New York overlap is most active), economic news can spike prices, brokers must be **regulated**.
- **Tool:** `calc.py fxsize` tells you how many lots to trade so a stop-out costs only 1% of your account.

### 2c. Stocks, shares and ETFs (`docs/03`)
- **What:** a share = a tiny piece of a company. An **ETF** = a basket of many shares you buy in one click.
- **Key lessons:** a low-cost global index ETF beats most professionals over 10+ years, so it is the **benchmark every active idea must beat**.

### 2d. Dividends (`docs/04`)
- **What:** cash a company pays shareholders. **Ex-dividend date** = you must own the share *before* it to get paid.
- **Key lessons:** a very high yield often signals danger (a "yield trap"); look at payout ratio, debt, cash flow.
- **Tool:** `calc.py dividend` projects income and reinvestment (DRIP).

### 2e. Bonds (`docs/05`)
- **What:** you lend money to a government/company and receive interest (coupons), then your money back.
- **Key lessons:** when interest rates rise, existing bond prices fall; **duration** measures by how much. Build a **ladder** (bonds maturing in different years).
- **Tool:** `calc.py bond` computes yield-to-maturity and duration.

### 2f. Other instruments (`docs/06`)
Options, futures, commodities, CFDs, REITs, leveraged ETFs: what they are, and honestly flagged as advanced or dangerous. Also sample allocation mixes.

**How I made these guides:** from established finance knowledge (not live data). I deliberately left out live prices, fees and tax rates because they change and differ per country; Claude fetches those on demand.

---------------------------------------------------------------------------

## 3. Category: strategies (`docs/07`, `bot/tradingbot/strategies.py`)

A **strategy** is a written rule for when to hold something. I implemented these in code:

| Name | Plain-English idea | Best for | Weak when |
|---|---|---|---|
| `sma_cross` | Hold when the short-term average price is above the long-term average ("trend is up") | Trending markets | Sideways chop (many small losses) |
| `ema_trend` | Hold only when price is above its 200-period average | Avoiding long bear markets | Lags at turns |
| `rsi_reversion` | Buy after a sharp drop (RSI low), sell on recovery | Calm, ranging markets | Strong downtrends ("catching a falling knife") |
| `donchian_breakout` | Buy when price breaks its 55-day high, exit at 20-day low (the old "Turtle" idea) | Big trends | Fake breakouts |
| `vol_target_trend` | Trend rule **plus** smaller size when the market is wild | Cutting drawdowns | Slow recoveries |
| `bb_squeeze` | After a quiet squeeze, buy the breakout | Volatility expansion | False breaks |
| `ensemble` | 3 trend rules **vote**; position = share of "yes" votes | Robustness | Same as trend |
| `vol_target_ensemble` | Ensemble **×** volatility sizing; never leveraged. **My default baseline** | A sane starting point | Sideways markets |
| momentum **rotation** (`rotation.py`) | Hold the 2 strongest assets of a basket, weighted by calmness; go to **cash** when nothing is rising | Multi-asset | Sudden reversals |

**How they work in code (simple version):** each function receives price history (open/high/low/close/volume) and returns, for every
day, a number: `0` = hold nothing, `1` = fully invested, `0.5` = half. Nothing else; the backtester does the rest.

**Why these and not "AI predicts the price":** simple trend + risk-sizing ideas have decades of evidence and few knobs to over-tune. "Predicting" is where overfitting and scams live.

**Honest warning:** the starter strategies are *teaching baselines*, not money machines. On the fake test data several lose money, which is realistic.

---------------------------------------------------------------------------

## 4. Category: backtesting, "testing an idea on the past" (`bot/tradingbot/backtest.py`)

**What it is:** replay history and see what the rule *would have* done.

**How I built it:** a vectorised function using **pandas** (a data-table library) and **numpy** (math). Key protections against self-deception:
1. **Next-bar execution** (no peeking): a signal decided at today's close is only traded on the next bar. Cheating here is called *look-ahead bias* and makes fake-great results.
2. **Costs included:** trading fee 0.1% + slippage 0.05% per side by default. Costs quietly kill many strategies.
3. **Out-of-sample test:** the data is split; the second part is "unseen" to check the idea isn't just memorised history.
4. **Walk-forward:** five consecutive time windows; a good strategy should be OK in most, not one lucky stretch.
5. **Comparison to buy-and-hold:** if you can't beat doing nothing, don't trade it.
6. **Automated test** (`test_no_lookahead_signals`) that proves no strategy sees the future.

**Numbers it reports (what they mean):**
- *Total return / CAGR:* growth overall / per year.
- *Sharpe:* return per unit of risk (above ~1 decent; above ~2 be suspicious).
- *Max drawdown:* worst peak-to-trough fall. If it's -50%, ask: could I stomach that?
- *Win rate / profit factor / trades:* how often it wins / gross profit ÷ gross loss / sample size (want 30+).

**Run it:**
```bash
cd trading-hq/bot
python3 -m tradingbot backtest --strategy vol_target_ensemble --source ccxt --symbol BTC/USDT
python3 -m tradingbot backtest --strategy ema_trend --source yfinance --symbol SPY --ppy 252
```
(`--ppy` = periods per year: 365 for crypto daily, 252 for stocks daily.)

---------------------------------------------------------------------------

## 5. Category: risk engine (`bot/tradingbot/risk.py`)

**What it is:** code versions of the rules from section 1.
- `position_size`: *how much to buy* so that your stop-out loses exactly 1% of the account.
  Example: account $10,000, risk 1% = $100; entry 60,000, stop 58,500 → distance 1,500 → buy 0.0667 BTC.
- `kelly_fraction`: a theoretical bet-size formula (use only a quarter of it; estimates are noisy).
- `RiskManager`: remembers peak equity and today's start; refuses new trades after a **3% daily loss** or **15% drawdown**, or too many open positions.

**What I used:** plain Python, no extra libraries, with unit tests proving the math.

---------------------------------------------------------------------------

## 6. Category: brokers and the "three locks" (`bot/tradingbot/broker.py`)

- **PaperBroker:** a pretend account with cash, fees and slippage. It cannot spend money it doesn't have or sell what it doesn't own.
- **CcxtBroker:** connects to Binance through **ccxt** (an open-source library that speaks to 100+ exchanges). **Testnet by default.**
- **Three locks before any real order can exist:** (1) paper is the default everywhere; (2) exchange connection defaults to the testnet;
  (3) live needs `sandbox=False` **and** the environment variable `LIVE_TRADING_CONFIRM=I_ACCEPT_THE_RISK`.
  I built it this way because the cheapest mistake is the one the software refuses to let you make.

**API keys, explained:** like a limited-power password for software. Create them with *Spot trading* permission only, **never withdrawals**, restricted to your IP.

---------------------------------------------------------------------------

## 7. Category: the Telegram co-pilot (`bot/tradingbot/telegram_bot.py`, `docs/11`)

**What it is:** a private chat bot on your phone that answers commands: `/signal`, `/backtest`, `/size`, `/watch`, `/log`, `/stats`...,
and sends a daily digest and price alerts.

**How it works:** Telegram lets anyone create a bot via `@BotFather`. My code asks Telegram "any new messages?" (called *long-polling*),
checks the sender, runs the matching function, and replies. Built with only Python's standard library, so there is nothing extra to install or trust.

**Why it is "the best" version rather than a typical Telegram trading bot:**
1. **Private**: replies only to your chat ID; strangers are ignored.
2. **Cannot trade or hold keys**: even if hacked, nobody can take funds through it.
3. **Behaviour lock**: log two losses in a row and `/size` refuses for 24 hours. This stops "revenge trading", where beginners lose most money.
4. **Honest analysis**: `/backtest` always shows buy-and-hold and out-of-sample beside the strategy.

**What to avoid:** public Telegram "signal" channels, "sniper"/copy-trade bots that want your keys or deposits, and anyone DMing you profit screenshots.

---------------------------------------------------------------------------

## 8. Category: calculators (`bot/tools/`)

| Command | Answers the question |
|---|---|
| `calc.py size` | How many coins/shares so I risk only X%? |
| `calc.py fxsize` | How many forex lots? |
| `calc.py rr` | What reward:risk, and what win rate do I need to break even? |
| `calc.py bond` | What yield and sensitivity does this bond have? |
| `calc.py dividend` | What income now, and after reinvesting for N years? |
| `calc.py compound` | What does saving a monthly amount become? |
| **`montecarlo.py`** (new) | **What could my next 200 trades look like? How bad can a bad streak get?** |

**Monte Carlo explained:** the computer plays your strategy thousands of times with random wins/losses. Try:
```bash
python3 tools/montecarlo.py --win 0.45 --payoff 2 --risk 0.01
python3 tools/montecarlo.py --win 0.45 --payoff 2 --risk 0.05
```
Even with a *good* edge, a typical run shows a losing streak of ~8 trades, and at 5% risk the median worst drawdown is about -43% versus about -10% at 1%.
That is the single best reason for small position size. Caveat: it assumes you *know* your true win rate; in real life you don't, so be conservative.

---------------------------------------------------------------------------

## 9. Category: the Claude helpers (`.claude/`)

**Skills** are saved instructions; you trigger them by typing a slash command in Claude Code:

| Command | What it does |
|---|---|
| `/trade-plan` | Turns an idea into entry/stop/size/target and checks it against the checklist |
| `/risk-check` | Audits your portfolio or bot against the rules, gives GREEN/AMBER/RED |
| `/backtest-strategy` | Builds and honestly tests a new strategy |
| `/market-brief` | Sourced summary of markets and the economic calendar |
| `/dividend-screen`, `/bond-ladder`, `/forex-setup` | Specialised analyses |
| `/crypto-bot-review` | Security/correctness review of any bot code before money touches it |
| `/journal-review` | Finds patterns in your diary |
| `/telegram-copilot` | Helps set up or extend the Telegram bot |

**Agents** are specialist assistants Claude can call: `quant-dev` (writes tested code), `risk-officer` (can veto), `market-researcher` (sourced facts only), `portfolio-planner`.

**`CLAUDE.md` + `settings.json`:** the rulebook and permissions. They forbid reading `.env` secrets and pre-approve only safe commands.

---------------------------------------------------------------------------

## 10. Category: free GitHub repos and tools (`docs/09`)

Grouped lists with one-line purposes, e.g. **Freqtrade** (full crypto bot), **ccxt** (exchange connector), **vectorbt/backtesting.py** (fast testing),
**yfinance** (stock data), **OpenBB** (research platform), **FinRL/Qlib** (AI research), **QuantStats** (report cards).
**Important:** I could not verify star counts/activity because this session can't browse other GitHub repos. Before using any: check last update, licence, and read the code.

---------------------------------------------------------------------------

## 11. Category: creative, out-of-the-box edge (`docs/11`)

Ideas beyond "buy when the line crosses":
- **Alerts-first**: bot watches, you decide, so most infrastructure risk disappears.
- **Behavioural firewall**: the cooling-off lock (built).
- **Cash-flow rebalancer**: new money and dividends go to the most underweight bucket; rebalance without selling.
- **Regime switch / barbell**: boring core 85–90%, experiments 10–15% with a hard cap.
- **Pre-mortem**: write "this fails if..." before entering.
- **Shadow trading**: run paper and tiny-live side by side to expose real-world costs.
- **Claude as analyst**: summarise filings, attack your thesis, audit code, but never predict prices.
- **Event calendar discipline**: pause new trades around central-bank/inflation releases.
- **Income ladder**: coupons/dividends cover monthly bills; trading is optional on top.

---------------------------------------------------------------------------

## 12. How I built it (tools and method), for transparency

| Thing | What I used | Why |
|---|---|---|
| Language | Python 3 | Standard for finance, readable for beginners |
| Data tables / math | pandas, numpy | Industry-standard |
| Exchange access | ccxt (optional) | One interface to Binance and others |
| Stock/FX data | yfinance (optional) | Free Yahoo data for learning |
| Telegram | Python standard library only | No extra dependencies to trust |
| Tests | `unittest` (built in) | 19 automated checks, including "no peeking at the future" |
| Version control | Git, pushed to your GitHub branch `ccr-620cd774-lkftu1` | History + backup |
| Knowledge docs | Markdown files | Opens anywhere |

**Method:** (1) wrote the safety rules first; (2) built small pieces (indicators → strategies → backtester → risk → brokers);
(3) wrote tests for the dangerous parts (look-ahead, overspending, locks, unauthorised Telegram users); (4) ran everything on synthetic data;
(5) wrote the docs. **Not done / not verified:** live Binance and Telegram connections (I had no keys/network for them), real-market backtest results, and the GitHub repo list.

---------------------------------------------------------------------------

## 13. Your first 7 days (concrete)

| Day | Do this | Time |
|---|---|---|
| 1 | Read sections 0–1 here and `docs/00`. Open `GLOSSARY.md` beside you | 45 min |
| 2 | Install Python, run the tests and the three demo commands (see root README) | 30 min |
| 3 | Run `montecarlo.py` with 1% vs 5% risk. Write what you learn | 20 min |
| 4 | Read your first market guide (crypto *or* stocks); open the matching cheat sheets | 45 min |
| 5 | Open Binance **testnet** or TradingView paper account; place 3 fake trades with `/trade-plan` | 45 min |
| 6 | Run a real-data backtest of `vol_target_ensemble` and `ema_trend` on BTC and SPY; compare to buy-and-hold | 30 min |
| 7 | Create the Telegram bot (`docs/11`), set one price alert, write your 1-page plan | 45 min |

Then follow `docs/10-roadmap.md`: 30 days learning, 90 days testing, only then a tiny live pilot, if your own paper results justify it.

---------------------------------------------------------------------------

## 14. Frequently asked beginner questions

**How much money do I need?** To learn: $0 (paper). Real trading: only money you can lose completely, after an emergency fund.
**Which market first?** Index-ETF investing (stocks) or Spot BTC/ETH DCA; forex and futures last.
**Can the bot make me rich?** No tool can promise that. It can help you test, stay disciplined and avoid mistakes.
**Will Claude trade for me?** Not here. It analyses, builds and reviews. You stay in control of money.
**Can I lose more than I put in?** With leverage/margin/futures/CFDs, yes in some cases. Another reason to avoid them at first.
**Is this financial advice?** No. It's educational software. Consider a licensed adviser for taxes and large decisions.
