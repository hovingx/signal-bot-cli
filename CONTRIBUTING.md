# Contributing to signal-bot-cli

Thanks for your interest! signal-bot-cli is the open-source CLI tool for [signal-bot.ai](https://signal-bot.ai) — real-time trading signals, memecoin scanner, and economic calendar in your terminal.

## Getting Started

```bash
git clone https://github.com/hovingx/signal-bot-cli
cd signal-bot-cli
pip install -e .[dev]
```

## Development Workflow

1. **Fork** the repo and create a feature branch
2. **Write tests** for any new functionality
3. **Run the full suite** before committing:
   ```bash
   ruff check signalbot/
   pytest tests/ -v
   ```
4. **Submit a PR** to `main` with a clear description

## Project Structure

```
signalbot/
├── cli.py          # argparse entry point, --json flag handling
├── api.py          # API client (requests wrapper, auth, error handling)
├── signals.py      # Trading signals handler (forex, crypto, stocks, binary)
├── scanner.py      # Memecoin scanner (concurrent, 5 chains)
├── calendar.py     # Economic calendar handler
└── utils.py        # Formatting helpers (price, tables)

tests/
└── test_cli.py     # Smoke tests (CLI interface + JSON output validation)
```

## Conventions

- **Python 3.9+** — no 3.13+ syntax
- **Type hints** on all public functions
- **Backward compatible** — existing commands and flags must not break
- **Error handling**: use `SignalBotError` (from `signalbot.api`) for user-facing errors; CLI catches it and outputs JSON when `--json` is set
- **Formatting**: follow the existing style — no auto-formatter required, just be consistent

## Testing

Tests use `pytest` and `subprocess` to invoke the actual CLI binary. This ensures real-world behavior is validated, not just internal functions.

```bash
# Run all tests
pytest tests/ -v

# Run a specific test
pytest tests/test_cli.py::test_signals_json_no_key -v
```

## Adding a New Command

1. Create a new module in `signalbot/` (e.g. `signalbot/backtest.py`)
2. Implement `run(key, json_output, ...)` — return `dict` when `json_output=True`, `None` when printing tables
3. Register in `signalbot/cli.py` under `sub.add_parser(...)`
4. Add smoke tests in `tests/test_cli.py`
5. Document in `README.md`

## Questions?

Open an issue on GitHub or contact us at [hello@signal-bot.ai](mailto:hello@signal-bot.ai).
