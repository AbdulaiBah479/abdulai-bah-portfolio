---
name: telegram-copilot
description: Set up, extend, debug or security-review the private Telegram trading co-pilot in bot/tradingbot/telegram_bot.py.
---
# Telegram co-pilot
Read `docs/11-telegram-and-creative-edge.md` and `telegram_bot.py`. Walk the user through BotFather setup, `.env`, `/id`, and running 24/7.
When extending: add a command in `handle()`, add a test in `bot/tests/test_core.py` (TelegramTests), keep it stdlib-only, run `cd bot && python3 -m unittest discover -s tests`.
Invariants (refuse to break): owner-only via chat ID, no trading/keys/withdrawals, token never printed, loss-streak lock stays.
If the user wants it to place orders: explain why not, suggest alerts + manual execution or Freqtrade's Telegram control with dry-run first.
