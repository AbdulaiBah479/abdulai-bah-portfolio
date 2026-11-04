# 01 · Binance & crypto

## Products (know what you're touching)
| Product | Risk | Notes |
|---|---|---|
| Spot | Low–med | Buy/sell actual coins. Start here. |
| Convert / Recurring Buy (DCA) | Low | Simple, higher fee on Convert; DCA beats timing for most people |
| Earn / staking / savings | Med | Counterparty & smart-contract risk; "yield" isn't free |
| Margin | High | Borrowed funds; liquidation |
| Futures / perpetuals | Very high | Leverage up to 100×+; funding fees; liquidations. Avoid until proven on paper |
| Options, leveraged tokens | Very high | Decay/compounding drag. Avoid |
| Launchpool / new listings | High | Most new tokens trend to zero |

## Fees (verify current schedule)
Spot base ~0.1% maker/taker; ~25% discount paying with BNB; lower with VIP/volume. Use **limit (maker)** orders to cut cost. Fees + spread eat high-frequency strategies.

## Account setup checklist
1. Complete KYC on the official site/app only (type URL yourself; beware phishing).
2. 2FA via authenticator or passkey/YubiKey (not SMS); set anti-phishing code; enable withdrawal whitelist & address-book-only.
3. Withdraw long-term holdings to a hardware wallet you control ("not your keys, not your coins").
4. API key for bots: **Spot trading only, withdrawals OFF, IP whitelist**. One key per bot. Rotate regularly.
5. Test on **Spot Testnet** (testnet.binance.vision) first — free fake funds.

## Order types on Binance
Market · Limit · Stop-Limit · OCO (take-profit + stop at once) · Trailing stop · Post-only. See `cheatsheets/order-types.md`.

## What to trade
- Core: BTC, ETH (liquid, deep books). Satellite: top-20 by volume. Avoid micro-caps, meme tokens, anything promising yield.
- Pairs: quote in USDT/USDC (or your fiat). Check 24h volume and spread before every trade.

## Crypto-specific risks
Exchange failure/hack (FTX precedent) · smart-contract exploits · stablecoin depeg · rug pulls · 24/7 market with weekend gaps in liquidity · regulatory change · tax complexity (every swap can be taxable) · correlation: altcoins fall with BTC.

## Useful data (free)
Binance public API (no key for market data) · CoinGecko/CoinMarketCap · Glassnode (limited free) · DefiLlama (TVL, stablecoins) · Coinglass (funding, open interest, liquidations) · Alternative.me Fear & Greed · Blockchain explorers.

## Strategies that suit crypto (see 07)
DCA · trend following (Donchian/EMA on daily) · grid trading in ranges (Binance built-in grid bot) · volatility-scaled sizing · funding-rate/basis (advanced; needs futures and capital) · rebalancing a BTC/ETH/stable mix.

## Bot options
1. This repo's `bot/` (ccxt → Binance testnet).
2. **Freqtrade** (full-featured, Telegram control, hyperopt, FreqAI). Recommended for serious automation.
3. **Hummingbot** (market making/arbitrage), **Jesse**, **OctoBot**, **Nautilus Trader**.
4. Binance's built-in Grid/DCA/Rebalancing bots (no code, spot).
Always: dry-run ≥ 30 days → tiny live size → scale slowly. Cap daily loss in code.

## Weekly crypto routine
Sun: review journal, BTC dominance, funding, macro calendar → Mon–Fri: execute plan only → alerts not staring at charts.
