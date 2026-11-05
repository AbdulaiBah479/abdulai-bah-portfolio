# My plan: Sierra Leone · $100/month · growth + income + learning · Windows

> Educational, not financial or legal advice. I could not verify current Sierra Leone laws, broker availability or interest rates.
> Items marked **CHECK** must be confirmed by you from official sources before you rely on them.

## 1. Honest expectations
- $100/month will not produce a living from trading. At the 1% rule, risk per trade is about **$1**. Fees, data and time matter more than profit at this size.
- What $100/month *can* do: build savings and an investing habit, protect against Leone inflation, and teach you a real skill cheaply.
- The real "return" in year one is **learning without big losses**. Money growth comes mostly from steady saving over years.

## 2. Your three goals mapped to buckets
| Goal | Bucket | Tools |
|---|---|---|
| Income (safe, regular) | Savings & fixed income | Local Treasury bills / fixed deposits, bond funds if reachable |
| Growth (long-term) | Core investing | Monthly purchases of broad, low-cost assets (see section 4) |
| Learning (active trading) | Practice first, tiny live later | Paper trading, bot, Telegram co-pilot |

## 3. Order of operations (do not skip)
1. **Emergency fund** (3 months of costs) in a safe place you can reach fast. Until this exists, nothing else gets real money.
2. **Paper trade** 30–90 days (free).
3. **Core monthly saving** (the sections below).
4. **Tiny live trading**, only if paper results beat simple holding after costs.

## 4. Monthly $100 plan (adjust to your situation)
**Months 1–3** (learning phase, mostly safe):
- $70–80 → safe savings/fixed income (emergency fund first, then Treasury bills / fixed deposit **CHECK** current rates and terms at your bank or via the Bank of Sierra Leone auction through a commercial bank).
- $20–30 → start the long-term core (BTC/ETH monthly purchase **only if** crypto is legal and you can fund it safely, see section 5) or save it toward an international broker.
- $0 → active trading. Paper only.

**Month 4 onward** (if the emergency fund is done and paper results are decent):
- $50 safe income (T-bills/fixed deposits)
- $30 core growth (monthly DCA)
- $10–20 "lab" money for tiny live experiments (risk $0.10–$0.25 per trade)

Rule: never put in money you need for food, rent, school fees or family.

## 5. How to actually reach markets from Sierra Leone (CHECK everything)
| Market | Realistic route | Watch out for |
|---|---|---|
| Leone savings / T-bills | Commercial banks; BoSL auctions via banks | Inflation can exceed the rate; check real (after-inflation) return |
| Local stocks | Sierra Leone Stock Exchange exists but is very small and illiquid | Few listings; hard to sell |
| Crypto | Binance (check availability for your country and your ID), funding via **P2P** with mobile money or bank | P2P scams: use only verified merchants with many trades, never release/accept outside the platform, never share OTPs |
| International stocks / ETFs | Only through a broker that accepts Sierra Leone residents **CHECK the broker's "supported countries" page** | Unlicensed brokers. Verify the licence on the regulator's own website, test with a tiny deposit **and** a tiny withdrawal first |
| Forex | Same broker test as above | Many unregulated "forex" firms in Africa are scams; leverage; do paper only for months |
| Bonds | Local T-bills first; international bonds via an accepting broker | Currency risk (Leone vs USD) |

**Leone vs dollar:** if the Leone loses value, saving only in Leones can lose purchasing power. Holding some savings in a dollar-linked form (e.g. USDT/USDC stablecoin, or a USD account) can help, but stablecoins can lose their peg, so keep amounts moderate and use reputable ones.

## 6. Security essentials
- 2-factor login with an authenticator app (not SMS); unique passwords.
- Never share your seed phrase, passwords, or OTP with anyone, including "support" people on WhatsApp/Telegram.
- Exchange API keys: spot trading only, **withdrawals off**.
- Beware: "double your money", signal groups, "trading mentors", fake Binance support, pig-butchering romance/investment chats. No one can guarantee profit.

## 7. Windows setup (about 45 minutes, free)
1. **Python:** python.org → Downloads → install 3.12 or newer. **Tick "Add python.exe to PATH".**
2. **Git:** git-scm.com → install with defaults.
3. **VS Code (optional editor):** code.visualstudio.com.
4. Open **PowerShell** (Start → type PowerShell):
```powershell
git clone https://github.com/abdulaibah479/abdulai-bah-portfolio.git
cd abdulai-bah-portfolio
git checkout ccr-620cd774-lkftu1
cd trading-hq\bot
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m unittest discover -s tests
```
If activation says scripts are disabled, run once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then try again.
5. Try the demos (use `python`, not `python3`, on Windows):
```powershell
python -m tradingbot backtest --source ccxt --symbol BTC/USDT
python tools\calc.py size --equity 100 --risk 0.01 --entry 60000 --stop 58500
python tools\montecarlo.py --win 0.45 --payoff 2 --risk 0.01
```
If `--source ccxt` cannot connect (some networks block Binance), try `--source yfinance --symbol BTC-USD` instead.
6. **Claude Code:** follow the current install instructions at docs.claude.com for Windows, then run `claude` inside the `trading-hq` folder.
7. **Data use:** the bot uses little data. Daily candles are tiny.

## 8. Telegram co-pilot on Windows
1. Telegram → search **@BotFather** → `/newbot` → copy the token. Keep it secret.
2. In PowerShell (inside `trading-hq\bot`, venv active):
```powershell
$env:TELEGRAM_BOT_TOKEN="paste-token-here"
python -m tradingbot telegram
```
3. Message your bot `/id`, copy the number, stop the bot (Ctrl+C), then:
```powershell
$env:TELEGRAM_CHAT_ID="your-number"
python -m tradingbot telegram
```
The variables last only for that PowerShell window. To keep them, use `setx TELEGRAM_BOT_TOKEN "..."` and open a new window.
Your PC must stay on for it to run. Later you can move it to a cheap always-on computer.

## 9. Binance testnet (fake money) setup
1. Go to testnet.binance.vision (the Spot Testnet; it usually signs in with a GitHub account).
2. Generate an API key there. These are fake-money keys, but still keep them private.
3. Put them in `trading-hq\bot\.env` (copy `.env.example`; never commit it).
4. Practice: `python -m tradingbot paper --source ccxt --symbol BTC/USDT --strategy vol_target_ensemble`.

## 10. Your first 14 days
| Day | Do |
|---|---|
| 1–2 | Read `docs/START-HERE.md`; install Python/Git |
| 3 | Clone project, run tests and demos |
| 4 | Run Monte Carlo at 1% and 5% risk; write what you notice |
| 5 | Visit your bank: ask about T-bills and fixed-deposit rates and minimums; ask what the current inflation rate is |
| 6 | Create the Telegram bot |
| 7 | Binance testnet + 3 paper trades logged with `/log` |
| 8–10 | Backtest BTC and ETH with `ema_trend` and `vol_target_ensemble`; compare with buy-and-hold |
| 11 | Check which international brokers list Sierra Leone; verify licences; do **not** deposit yet |
| 12 | Write your one-page rules (section 11) |
| 13–14 | Review week; adjust. Still paper only |

## 11. My one-page rules (fill in)
- My monthly amount: $____ (never money for essentials)
- Emergency fund target: $____ (done by ____)
- Max risk per trade: 1% of trading money (0.5% at first)
- Stop for the day after 2 losses. Stop and review at -15% from peak.
- No leverage, no futures/options/CFDs for at least 12 months.
- I only trade what is on my written plan.
- I log every trade.
- Before real money: 30+ paper trades, results beat holding after costs.
- I never share keys, seed phrases or OTPs.

## 12. Things to confirm (I could not)
1. Whether Binance serves residents of Sierra Leone with your ID, and the legal status of crypto (ask a local lawyer/accountant; check Bank of Sierra Leone and National Revenue Authority notices).
2. Current Treasury bill and fixed-deposit rates, and current inflation.
3. Which regulated international brokers accept Sierra Leone residents, and how you would fund and withdraw.
4. Tax treatment of investment income and crypto gains.
