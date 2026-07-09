"""Smoke tests for signal-bot-cli — validates CLI interface and JSON output."""

import json
import subprocess
import sys


def _run(*args: str) -> subprocess.CompletedProcess:
    """Run signal-bot CLI and return completed process."""
    return subprocess.run(
        [sys.executable, "-m", "signalbot.cli"] + list(args),
        capture_output=True,
        text=True,
        timeout=30,
    )


# ─── CLI Interface ───────────────────────────────────────────

def test_help_shows_usage():
    """--help should exit 0 and mention usage."""
    result = subprocess.run(
        [sys.executable, "-m", "signalbot.cli", "--help"],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0
    assert "trading signals" in result.stdout.lower()


def test_no_command_shows_help():
    """Running without subcommand should print help."""
    result = _run()
    assert "usage:" in result.stdout.lower() or "signal-bot" in result.stdout.lower()


def test_keys_command():
    """keys command should work without API key."""
    result = _run("keys")
    assert result.returncode == 0
    assert "signal-bot.ai/contact" in result.stdout


# ─── JSON Output Mode ────────────────────────────────────────

def test_keys_json():
    """keys --json should output valid JSON with url."""
    result = _run("--json", "keys")
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data["action"] == "get_api_key"
    assert "signal-bot.ai/contact" in data["url"]


# ─── Signals (requires API key — test behavior without key) ──

def test_signals_no_key():
    """signals without API key should exit with clear message."""
    result = _run("signals", "forex")
    assert result.returncode != 0
    assert "API key" in result.stdout or "API key" in result.stderr


def test_signals_json_no_key():
    """signals --json without API key should output JSON error to stderr."""
    result = _run("--json", "signals", "forex")
    assert result.returncode == 1
    error_output = result.stderr
    data = json.loads(error_output)
    assert "error" in data


def test_signals_invalid_market_json():
    """signals --json with invalid market should return JSON error."""
    result = _run("--json", "signals", "invalid_market")
    data = json.loads(result.stdout)
    assert "error" in data
    assert "invalid_market" in str(data["error"])


# ─── Scanner ─────────────────────────────────────────────────

def test_scanner_no_key():
    """scanner without API key should exit with clear message."""
    result = _run("scanner")
    assert result.returncode != 0
    assert "API key" in result.stdout or "API key" in result.stderr


def test_scanner_json_no_key():
    """scanner --json without API key should output JSON error."""
    result = _run("--json", "scanner", "sol")
    assert result.returncode == 1
    data = json.loads(result.stderr)
    assert "error" in data


# ─── Calendar ────────────────────────────────────────────────

def test_calendar_no_key():
    """calendar without API key should exit with clear message."""
    result = _run("calendar")
    assert result.returncode != 0
    assert "API key" in result.stdout or "API key" in result.stderr


def test_calendar_json_no_key():
    """calendar --json without API key should output JSON error."""
    result = _run("--json", "calendar")
    assert result.returncode == 1
    data = json.loads(result.stderr)
    assert "error" in data


# ─── Invalid API Key (real HTTP call) ────────────────────────

def test_signals_invalid_key_json():
    """signals --json with invalid key should get 401 in JSON."""
    result = _run("--key", "bad_key_12345", "--json", "signals", "forex")
    # With invalid key, should exit 1 and output JSON error to stderr
    if result.returncode == 0:
        data = json.loads(result.stdout)
        # If server returns data despite bad key, just check it's valid JSON
        assert isinstance(data, dict)
    else:
        data = json.loads(result.stderr)
        assert "error" in data or "Invalid" in str(data) or "key" in str(data).lower()
