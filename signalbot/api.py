"""API client — thin wrapper around signal-bot.ai REST API."""

import os

try:
    import requests
except ImportError:
    requests = None

API_BASE = "https://api.signal-bot.ai/api/v1"


class SignalBotError(Exception):
    """Expected user-facing error (e.g. missing key, invalid key, rate limit)."""
    pass


def get_key(key_override: str | None = None) -> str:
    """Resolve API key: explicit arg > SIGNALBOT_KEY env."""
    key = key_override or os.environ.get("SIGNALBOT_KEY", "")
    if not key:
        raise SignalBotError(
            "🔑 No API key found.\n\n"
            "Set it once:\n"
            "  export SIGNALBOT_KEY=your_key_here\n\n"
            "Or pass per-command:\n"
            "  signal-bot --key your_key_here signals forex\n\n"
            "Get your free key → https://signal-bot.ai/contact"
        )
    return key


def _ensure_requests():
    if requests is None:
        raise SignalBotError(
            "Missing dependency: requests\n"
            "Install it: pip install requests"
        )


def get(endpoint: str, params: dict | None = None, key: str | None = None) -> dict:
    """GET request to signal-bot.ai API."""
    _ensure_requests()
    key = key or get_key()
    url = f"{API_BASE}/{endpoint}"
    resp = requests.get(url, headers={"X-API-Key": key}, params=params, timeout=30)
    if resp.status_code == 401:
        raise SignalBotError("❌ Invalid API key. Get one at https://signal-bot.ai/contact")
    if resp.status_code == 429:
        raise SignalBotError("⏳ Rate limited. Wait a moment and try again.")
    resp.raise_for_status()
    return resp.json()
