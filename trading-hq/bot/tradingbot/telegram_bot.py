"""Private Telegram co-pilot: alerts, signals, quick backtests, calculators and a discipline journal.

DESIGN (deliberately different from the 'trading bots' that circulate on Telegram):
  * PRIVATE: only TELEGRAM_CHAT_ID can use it. Everyone else gets silence (except /id, needed for setup).
  * NO ORDER PLACEMENT. It cannot trade, cannot hold exchange keys, cannot withdraw. Alerts + analysis only.
  * DISCIPLINE: /log win|loss; after 2 losses in a row it locks /size for 24h (anti revenge-trading).
  * Stdlib only (urllib). Token read from env, never logged.

Setup:  talk to @BotFather -> /newbot -> token.  export TELEGRAM_BOT_TOKEN=...
        message your bot, send /id, then export TELEGRAM_CHAT_ID=<that number>.
Run:    python -m tradingbot telegram
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

from . import backtest as bt
from . import data as D
from .risk import position_size
from .strategies import STRATEGIES

LOCK_AFTER_LOSSES = 2
LOCK_HOURS = 24
DISCLAIMER = "Educational analysis, not advice."

HELP = """Commands
/signal SYMBOL [strategy]   current target position(s)  e.g. /signal BTC/USDT ensemble
/backtest SYMBOL [strategy] quick test vs buy&hold      e.g. /backtest SPY vol_target_trend
/size EQUITY RISK% ENTRY STOP   position size (locked after 2 losses)
/rr ENTRY STOP TARGET       reward:risk + breakeven win rate
/bond FACE COUPON% YEARS PRICE  YTM + duration
/watch SYMBOL above|below PRICE price alert   (/watches, /unwatch N)
/log win|loss [R] [note]    journal a trade (2 losses in a row => 24h cooling-off)
/stats                      journal stats
/pause /resume /status
/strategies  /id
""" + DISCLAIMER


# ---------- state ----------
class State:
    def __init__(self, path: str | Path = "telegram_state.json", journal: str | Path = "../journal/telegram_log.csv"):
        self.path, self.journal = Path(path), Path(journal)
        self.d = {"watches": [], "paused": False, "lock_until": 0.0, "streak": 0}
        if self.path.exists():
            try:
                self.d.update(json.loads(self.path.read_text()))
            except (ValueError, OSError):
                pass

    def save(self):
        try:
            self.path.write_text(json.dumps(self.d))
        except OSError:
            pass


# ---------- data (injectable for tests) ----------
def default_fetch(symbol: str) -> pd.DataFrame:
    return D.from_ccxt(symbol, "1d", 1000) if "/" in symbol else D.from_yfinance(symbol)


def default_price(symbol: str) -> float:
    return float(default_fetch(symbol)["close"].iloc[-1])


# ---------- command handlers ----------
def _fmt(m: dict) -> str:
    return (f"ret {m['total_return']:+.1%} | CAGR {m['cagr']:+.1%} | Sharpe {m['sharpe']:.2f} | "
            f"maxDD {m['max_drawdown']:.1%} | trades {m['trades']}")


def handle(text: str, st: State, fetch=default_fetch, price=default_price, now: float | None = None) -> str:
    now = now or time.time()
    parts = text.strip().split()
    if not parts:
        return HELP
    cmd, args = parts[0].lower().split("@")[0], parts[1:]
    try:
        if cmd in ("/start", "/help"):
            return HELP
        if cmd == "/strategies":
            return "\n".join(STRATEGIES) + "\n\n'vol_target_ensemble' is the default serious baseline."
        if cmd == "/signal":
            df = fetch(args[0])
            names = [args[1]] if len(args) > 1 else list(STRATEGIES)
            rows = [f"{n}: {STRATEGIES[n](df).iloc[-1]:+.2f}" for n in names]
            return f"{args[0]} close {df['close'].iloc[-1]:,.4f} ({df.index[-1].date()})\n" + "\n".join(rows) + \
                   "\n(+1 = fully long, 0 = flat; fractions = partial size)\n" + DISCLAIMER
        if cmd == "/backtest":
            df, name = fetch(args[0]), (args[1] if len(args) > 1 else "vol_target_ensemble")
            fn = STRATEGIES[name]
            ppy = 365 if "/" in args[0] else 252
            kw = dict(periods_per_year=ppy)
            res, bh = bt.run(df, fn(df), **kw), bt.buy_and_hold(df, **kw)
            _, oos = bt.in_out_of_sample(df, fn, **kw)
            return (f"{args[0]} / {name} / {len(df)} bars\nstrategy: {_fmt(res.metrics)}\nbuy&hold: {_fmt(bh.metrics)}\n"
                    f"out-of-sample: {_fmt(oos)}\nBeat buy&hold after costs AND out-of-sample? Be honest.")
        if cmd == "/size":
            if st.d["paused"]:
                return "Paused. /resume first."
            if now < st.d["lock_until"]:
                left = (st.d["lock_until"] - now) / 3600
                return f"Cooling-off active ({left:.1f}h left) after {LOCK_AFTER_LOSSES} losses in a row. Review your journal instead."
            eq, rp, entry, stop = (float(x) for x in args[:4])
            q = position_size(eq, rp / 100, entry, stop)
            return (f"qty {q:.6f} | notional {q * entry:,.2f} | risk {eq * rp / 100:,.2f} | "
                    f"leverage {q * entry / eq:.2f}x")
        if cmd == "/rr":
            e, s, t = (float(x) for x in args[:3])
            risk, rew = abs(e - s), abs(t - e)
            return f"R:R 1:{rew / risk:.2f} | breakeven win rate {risk / (risk + rew):.1%} (before costs)"
        if cmd == "/bond":
            import sys
            sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
            import calc
            face, cpn, yrs, px = (float(x) for x in args[:4])
            y = calc.bond_ytm(px, face, cpn / 100, yrs)
            mac, mod = calc.bond_duration(face, cpn / 100, y, yrs)
            return f"YTM {y:.3%} | Macaulay {mac:.2f}y | modified {mod:.2f} (+1% yield ~ {-mod:.1f}% price)"
        if cmd == "/watch":
            sym, side, lvl = args[0], args[1].lower(), float(args[2])
            if side not in ("above", "below"):
                return "Usage: /watch SYMBOL above|below PRICE"
            st.d["watches"].append({"symbol": sym, "side": side, "level": lvl})
            st.save()
            return f"Watching {sym} {side} {lvl}"
        if cmd == "/watches":
            w = st.d["watches"]
            return "\n".join(f"{i + 1}. {x['symbol']} {x['side']} {x['level']}" for i, x in enumerate(w)) or "No alerts."
        if cmd == "/unwatch":
            st.d["watches"].pop(int(args[0]) - 1)
            st.save()
            return "Removed."
        if cmd == "/log":
            return _log(args, st, now)
        if cmd == "/stats":
            return _stats(st)
        if cmd == "/pause":
            st.d["paused"] = True; st.save()
            return "Paused (alerts continue, /size disabled)."
        if cmd == "/resume":
            st.d["paused"] = False; st.save()
            return "Resumed."
        if cmd == "/status":
            lock = max(0.0, (st.d["lock_until"] - now) / 3600)
            return (f"paused={st.d['paused']} | cooling-off={lock:.1f}h | loss streak={st.d['streak']} | "
                    f"alerts={len(st.d['watches'])}")
        return "Unknown command. /help"
    except (IndexError, ValueError, KeyError):
        return "Bad arguments. /help"
    except Exception as e:  # network/data errors must not kill the bot
        return f"Error: {type(e).__name__}: {str(e)[:150]}"


def _log(args, st: State, now: float) -> str:
    if not args or args[0].lower() not in ("win", "loss"):
        return "Usage: /log win|loss [R] [note]"
    result = args[0].lower()
    r = None
    if len(args) > 1:
        try:
            r = float(args[1])
        except ValueError:
            pass
    note = " ".join(args[2 if r is not None else 1:])
    if r is None:
        r = 1.0 if result == "win" else -1.0
    st.journal.parent.mkdir(parents=True, exist_ok=True)
    new = not st.journal.exists()
    with st.journal.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["utc", "result", "R", "note"])
        w.writerow([dt.datetime.fromtimestamp(now, dt.timezone.utc).isoformat(timespec="seconds"), result, r, note])
    msg = f"Logged {result} {r:+.2f}R."
    if result == "loss":
        st.d["streak"] += 1
        if st.d["streak"] >= LOCK_AFTER_LOSSES:
            st.d["lock_until"] = now + LOCK_HOURS * 3600
            msg += f"\n{st.d['streak']} losses in a row: /size locked for {LOCK_HOURS}h. Walk away. Review the plan, not the chart."
    else:
        st.d["streak"] = 0
    st.save()
    return msg


def _stats(st: State) -> str:
    if not st.journal.exists():
        return "No trades logged. /log win|loss"
    df = pd.read_csv(st.journal)
    n, wins = len(df), (df["result"] == "win").sum()
    exp = df["R"].mean()
    note = "" if n >= 30 else f"\nOnly {n} trades: inconclusive until 30+."
    return f"trades {n} | win rate {wins / n:.0%} | expectancy {exp:+.2f}R | total {df['R'].sum():+.1f}R{note}"


# ---------- alerts ----------
def check_watches(st: State, price=default_price) -> list[str]:
    out, keep = [], []
    for w in st.d["watches"]:
        try:
            p = price(w["symbol"])
        except Exception:
            keep.append(w)
            continue
        hit = p >= w["level"] if w["side"] == "above" else p <= w["level"]
        if hit:
            out.append(f"ALERT {w['symbol']} {w['side']} {w['level']} (now {p:,.4f})")
        else:
            keep.append(w)
    if out:
        st.d["watches"] = keep
        st.save()
    return out


def daily_digest(symbols: list[str], fetch=default_fetch) -> str:
    lines = ["Daily digest"]
    for s in symbols:
        try:
            df = fetch(s)
            sig = STRATEGIES["vol_target_ensemble"](df).iloc[-1]
            chg = df["close"].iloc[-1] / df["close"].iloc[-2] - 1
            lines.append(f"{s}: {df['close'].iloc[-1]:,.4f} ({chg:+.1%}) | baseline target {sig:+.2f}")
        except Exception as e:
            lines.append(f"{s}: error {type(e).__name__}")
    lines.append(DISCLAIMER)
    return "\n".join(lines)


# ---------- transport ----------
class Telegram:
    def __init__(self, token: str):
        self.base = f"https://api.telegram.org/bot{token}"

    def call(self, method: str, **params):
        data = urllib.parse.urlencode(params).encode()
        with urllib.request.urlopen(urllib.request.Request(f"{self.base}/{method}", data=data), timeout=60) as r:
            return json.loads(r.read())

    def send(self, chat_id: int, text: str):
        self.call("sendMessage", chat_id=chat_id, text=text[:4000])


def process_update(upd: dict, owner: int | None, st: State, fetch=default_fetch, price=default_price) -> tuple[int, str] | None:
    """Pure routing + authorization. Returns (chat_id, reply) or None to stay silent."""
    msg = upd.get("message") or {}
    chat, text = msg.get("chat", {}).get("id"), msg.get("text", "")
    if chat is None or not text.startswith("/"):
        return None
    if text.split()[0].split("@")[0].lower() == "/id":
        return chat, f"Your chat id: {chat}. Set TELEGRAM_CHAT_ID to this."
    if owner is None or chat != owner:
        return None                      # strangers get nothing
    return chat, handle(text, st, fetch, price)


def run():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise SystemExit("Set TELEGRAM_BOT_TOKEN (from @BotFather).")
    owner = int(os.environ["TELEGRAM_CHAT_ID"]) if os.environ.get("TELEGRAM_CHAT_ID") else None
    watchlist = [s for s in os.environ.get("WATCHLIST", "BTC/USDT,ETH/USDT,SPY").split(",") if s]
    digest_hour = int(os.environ.get("DIGEST_HOUR_UTC", "7"))
    tg, st = Telegram(token), State()
    offset, last_check, last_digest_day = 0, 0.0, None
    print("Telegram co-pilot running. Ctrl+C to stop.", "(owner not set: only /id works)" if owner is None else "")
    while True:
        try:
            res = tg.call("getUpdates", offset=offset, timeout=30)
            for u in res.get("result", []):
                offset = u["update_id"] + 1
                out = process_update(u, owner, st)
                if out:
                    tg.send(*out)
            now = time.time()
            if owner and now - last_check > 60:
                last_check = now
                for a in check_watches(st):
                    tg.send(owner, a)
                utc = dt.datetime.now(dt.timezone.utc)
                if utc.hour == digest_hour and last_digest_day != utc.date():
                    last_digest_day = utc.date()
                    tg.send(owner, daily_digest(watchlist))
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("loop error:", type(e).__name__)   # never print the URL (contains the token)
            time.sleep(5)
