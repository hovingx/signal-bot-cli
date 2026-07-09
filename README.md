# signal-bot-cli

Real-time trading signals & market data — right in your terminal.

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org)

---

## Install

```bash
git clone https://github.com/hovingx/signal-bot-cli
cd signal-bot-cli
pip install .
```

That's it. You now have the `signal-bot` command.

---

## Quick Start

```bash
# Set your API key once (get one free at https://signal-bot.ai/contact)
export SIGNALBOT_KEY=your_key_here

# Forex signals
signal-bot signals forex

# Crypto signals
signal-bot signals crypto

# Solana memecoin scanner (fetches all 5 chains concurrently)
signal-bot scanner sol

# Economic calendar
signal-bot calendar

# API key info
signal-bot keys
```

---

## Commands

### `signal-bot signals <market>`

Live trading signals with direction, confidence %, stop loss, and take profit.

| Market   | Assets                          | Timeframes      |
|----------|---------------------------------|-----------------|
| `forex`  | 10 major & minor pairs          | 15m / 1h / 4h   |
| `crypto` | 30 assets by market cap         | 15m / 1h / 4h   |
| `stocks` | 17 US equities                  | 15m / 1h / 4h   |
| `binary` | 10 forex pairs                  | 1m / 5m / 15m    |

```bash
signal-bot signals forex
```

```
┌──────────┬─────────┬──────┬───────┬──────────┬──────────┐
│ Pair     │ Price   │ Dir  │ Conf  │ SL       │ TP       │
├──────────┼─────────┼──────┼───────┼──────────┼──────────┤
│ EUR/USD  │ 1.1429  │ BUY  │ 76%   │ 1.1384   │ 1.1507   │
│ GBP/USD  │ 1.3329  │ SELL │ 68%   │ 1.3395   │ 1.3208   │
│ USD/JPY  │ 159.041 │ SELL │ 72%   │ 160.12   │ 157.34   │
└──────────┴─────────┴──────┴───────┴──────────┴──────────┘

3 signals
```

---

### `signal-bot scanner [chain]`

Real-time memecoin scanner — fetches all 5 chains concurrently with smart money tracking and conviction scoring.

```bash
signal-bot scanner sol      # Solana (fetches all chains)
signal-bot scanner bsc      # BSC
signal-bot scanner          # Default: shows all 5 chains
```

**Chains:** `sol`, `bsc`, `base`, `eth`, `robinhood`

```
┌───────┬────────┬───────────┬───────┬──────────────────┬──────────────────────┐
│ Chain │ Symbol │ MCap      │ Score │ Signal           │ Smart Money          │
├───────┼────────┼───────────┼───────┼──────────────────┼──────────────────────┤
│ SOL   │ BONK   │ $251.00M  │ 87.5  │ HIGH_CONVICTION  │ smart:14 snipers:2   │
│ SOL   │ WIF    │ $182.30M  │ 82.1  │ HIGH_CONVICTION  │ smart:11 snipers:1   │
│ BSC   │ FLOKI  │ $95.40M   │ 78.3  │ WATCHLIST        │ smart:8  snipers:0   │
└───────┴────────┴───────────┴───────┴──────────────────┴──────────────────────┘

3 tokens · 2 HIGH_CONVICTION
```

---

### `signal-bot calendar`

Real-time economic calendar with impact levels and actual vs forecast data.

```bash
signal-bot calendar
```

```
┌──────────────────┬─────────┬─────┬────────────────────┬────────┬──────────┬──────────┐
│ Time             │ Country │ Imp │ Event              │ Actual │ Forecast │ Previous │
├──────────────────┼─────────┼─────┼────────────────────┼────────┼──────────┼──────────┤
│ 2026-07-09 12:30 │ US      │ 🔴  │ CPI (YoY)          │ 3.4%   │ 3.5%     │ 3.6%     │
│ 2026-07-09 14:00 │ US      │ 🟡  │ Fed Chair Speech   │ —      │ —        │ —        │
│ 2026-07-10 01:30 │ AU      │ 🟡  │ Unemployment Rate  │ 4.0%   │ 4.1%     │ 4.1%     │
└──────────────────┴─────────┴─────┴────────────────────┴────────┴──────────┴──────────┘

3 events · 1 high-impact
```

---

### `signal-bot keys`

Get your free API key.

```bash
signal-bot keys
# 🔑 Get your free API key → https://signal-bot.ai/contact
```

---

## Authentication

Set your API key once:

```bash
export SIGNALBOT_KEY=your_key_here
```

Or pass per-command:

```bash
signal-bot --key your_key_here signals forex
```

Keys are free — request yours at [signal-bot.ai/contact](https://signal-bot.ai/contact).

---

## Examples

Ready-to-run shell scripts in [`examples/`](examples/):

```bash
./examples/forex-signals.sh
./examples/crypto-scanner.sh       # default: sol
./examples/crypto-scanner.sh bsc   # specific chain
./examples/calendar.sh
```

---

## Requirements

- Python 3.9+
- `requests` ≥ 2.28
- `tabulate` ≥ 0.9

Both are installed automatically with `pip install .`

---

## Project Structure

```
signal-bot-cli/
├── signalbot/
│   ├── __init__.py     # Package root
│   ├── cli.py          # argparse entry point
│   ├── api.py          # API client (requests wrapper)
│   ├── signals.py      # Trading signals handler
│   ├── scanner.py      # Memecoin scanner handler (concurrent)
│   ├── calendar.py     # Economic calendar handler
│   └── utils.py        # Formatting helpers
├── examples/           # Shell scripts (CLI usage)
├── setup.py            # pip install entry point
├── LICENSE             # MIT
└── README.md           # ← you are here
```

---

## License

MIT © [signal-bot.ai](https://signal-bot.ai)
