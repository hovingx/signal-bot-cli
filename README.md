# signal-bot-cli

Real-time trading signals & market data — right in your terminal.

[![CI](https://github.com/hovingx/signal-bot-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/hovingx/signal-bot-cli/actions)
[![PyPI](https://img.shields.io/pypi/v/signal-bot-cli?color=blue)](https://pypi.org/project/signal-bot-cli/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org)
[![Tests](https://img.shields.io/badge/tests-12%2F12-brightgreen)](tests/)

---

## Install

```bash
pip install signal-bot-cli
```

Or from source:

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

## `--json` Output (for scripts & AI agents)

Every command supports `--json` for machine-readable output. Use this to pipe data into scripts, dashboards, or AI agents (Claude, ChatGPT, Cursor, Copilot, etc.).

```bash
# JSON output — parseable by any script or agent
signal-bot --json signals forex | jq '.signals[] | select(.confidence > 70)'

signal-bot --json scanner sol | jq '.signals[] | select(.signal == "HIGH_CONVICTION")'

signal-bot --json calendar | jq '.events[] | select(.impact == "high")'
```

**Agent use cases:**
- **Trading assistant**: pipe scanner output to an LLM for narrative analysis
- **Backtesting**: export signals to CSV with `--json` → `jq` → pandas
- **Alert bots**: cron + `signal-bot --json` + Telegram/Discord/email webhook
- **Dashboard**: pipe JSON into a Grafana panel, Streamlit app, or Google Sheets

Errors also output as JSON when `--json` is set:
```json
{"error": "❌ Invalid API key. Get one at https://signal-bot.ai/contact"}
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
│   ├── cli.py          # argparse entry point, --json flag handling
│   ├── api.py          # API client (requests wrapper, auth, error handling)
│   ├── signals.py      # Trading signals handler
│   ├── scanner.py      # Memecoin scanner handler (concurrent, 5 chains)
│   ├── calendar.py     # Economic calendar handler
│   └── utils.py        # Formatting helpers (price, tables)
├── tests/
│   └── test_cli.py     # Smoke tests (CLI interface + JSON validation)
├── .github/workflows/
│   └── ci.yml          # CI pipeline (lint + test, Python 3.9–3.12)
├── examples/           # Shell scripts (CLI usage)
├── setup.py            # pip install entry point
├── pyproject.toml      # Pytest config
├── CONTRIBUTING.md     # How to contribute
├── CODE_OF_CONDUCT.md  # Contributor covenant
├── LICENSE             # MIT
└── README.md           # ← you are here
```

---

## Contributing

Pull requests are welcome! See [`CONTRIBUTING.md`](CONTRIBUTING.md) for details on the development workflow.

## License

MIT © [signal-bot.ai](https://signal-bot.ai)
