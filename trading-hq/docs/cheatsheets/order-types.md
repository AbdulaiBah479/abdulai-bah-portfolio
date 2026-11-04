# Order types & execution

| Order | What | Use / watch out |
|---|---|---|
| Market | Fill now at best price | Certain fill, uncertain price (slippage in thin books) |
| Limit | Buy ≤ / sell ≥ price | Price control, may not fill; maker fees lower |
| Stop (stop-market) | Becomes market at trigger | Protective exit; gaps fill worse than stop |
| Stop-limit | Becomes limit at trigger | May not fill in a fast move: risky as a stop-loss |
| OCO | Take-profit + stop; one cancels other | Standard exit bracket (Binance spot supports) |
| Bracket | Entry + TP + SL | Stocks/FX brokers |
| Trailing stop | Stop follows price by %/ATR | Locks profit; tight trails get whipped |
| Post-only | Never takes liquidity | Guarantees maker fee |
| IOC / FOK | Immediate-or-cancel / fill-or-kill | Execution algos |
| GTC / Day | Time in force | Know expiry; GTC can fill unexpectedly |
| Market-if-touched / limit-on-close (MOC) | Stocks | Auction orders |

## Terms
Bid/ask/spread · Slippage · Liquidity/depth · Maker vs taker · Partial fill · Margin / maintenance margin · Liquidation price · Long/short · Leverage = notional ÷ equity · Gap · Halt.

## Execution hygiene
- Check spread and volume first; use limit orders in illiquid markets.
- Avoid market orders at open/close, news, and rollover.
- Always send the stop with (or immediately after) the entry; verify it exists.
- Use client order IDs in bots to prevent duplicates.
- Respect tick size, lot size, min notional (ccxt `amount_to_precision`).
