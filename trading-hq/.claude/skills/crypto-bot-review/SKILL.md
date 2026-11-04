---
name: crypto-bot-review
description: Review any crypto trading bot (this repo's, Freqtrade config, or third-party code) for safety, correctness and risk controls before it touches money.
---
# Crypto bot review
Use the production checklist in `docs/08-backtesting-and-bots.md`. Inspect: secrets handling, API permissions (no withdrawals), live gating, order idempotency, precision/min-notional, stops on exchange, rate limits, error handling, logging/alerts, position/loss limits, look-ahead bias, fees/slippage assumptions, data quality, dry-run parity. For third-party code also check for exfiltration (network calls, obfuscation, key logging) and abandoned dependencies.
Output: findings by severity (Critical/High/Med/Low), file:line references, concrete fixes, and a go/no-go for paper vs live.
