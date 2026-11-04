# Crypto & exchange security

## Accounts
- Authenticator app or hardware key (not SMS). Unique password in a password manager. Anti-phishing code.
- Whitelist withdrawal addresses; new-address cooling period. Review active devices/API keys monthly.
- Bookmark the official site. Never click links in DMs, emails, ads, "support" chats. Binance staff never ask for passwords/2FA.

## Keys & custody
- Exchange = convenient, counterparty risk. Hardware wallet (Ledger, Trezor, etc.) for long-term holdings.
- Seed phrase: written on paper/metal, offline, never photographed, never typed into websites or AI chat.
- Test with a small transfer first; verify address first/last 6 chars (clipboard malware).

## API keys (bots)
- Permissions: read + spot trade ONLY. **Never withdrawals.** IP restrict. Separate key per bot. Keep in env/secret manager.
- Rotate keys if the machine/repo was ever exposed. Check `.gitignore` covers `.env`.
- Revoke immediately if unusual activity.

## Scam patterns
Guaranteed returns, "AI trading bot" for sale, signal groups, copy-trading DMs, romance/"pig-butchering", fake exchanges/airdrops, wallet-drainer approvals, recovery scams, fake customer support, giveaways impersonating celebrities. Token approvals: review/revoke on revoke.cash.

## DeFi basics
Smart-contract risk, impermanent loss, rug pulls, oracle manipulation, bridge hacks. Use audited, battle-tested protocols; small test amounts; separate "hot" wallet.

## Operational
Keep OS updated; dedicated browser profile; no cracked software or shady Chrome extensions; VPS hardened (SSH keys, firewall, no root login).
