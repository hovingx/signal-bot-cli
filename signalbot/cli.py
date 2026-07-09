#!/usr/bin/env python3
"""signal-bot CLI — real-time trading signals, memecoin scanner & economic calendar.

Usage:
    signal-bot signals forex        Live forex signals
    signal-bot scanner sol          Solana memecoin scanner
    signal-bot scanner              Scanner (all 5 chains)
    signal-bot calendar             Forex economic calendar
    signal-bot keys                 API key info

Add --json for machine-readable output (agent-friendly, parseable).
Get your free API key at https://signal-bot.ai/contact
"""

import argparse
import json
import sys

from signalbot import signals, scanner, calendar
from signalbot.api import SignalBotError


def main():
    parser = argparse.ArgumentParser(
        prog="signal-bot",
        description="signal-bot.ai CLI — trading signals & market data in your terminal",
    )
    parser.add_argument("--key", help="API key (or set SIGNALBOT_KEY env)")
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output raw JSON instead of formatted tables (for scripts/agents)",
    )

    sub = parser.add_subparsers(dest="command")

    # signals
    p_sig = sub.add_parser("signals", help="Get trading signals")
    p_sig.add_argument(
        "market",
        help="Market to fetch (forex, crypto, stocks, binary)",
    )

    # scanner
    p_scan = sub.add_parser("scanner", help="Memecoin scanner (5 chains)")
    p_scan.add_argument(
        "chain",
        nargs="?",
        default="sol",
        choices=["sol", "bsc", "base", "eth", "robinhood"],
        help="Chain to scan (default: sol — always fetches all 5 chains)",
    )

    # calendar
    sub.add_parser("calendar", help="Forex economic calendar")

    # keys
    sub.add_parser("keys", help="API key information")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == "signals":
            result = signals.run(args.market, key=args.key, json_output=args.json_output)
            if result:
                print(json.dumps(result, indent=2))
        elif args.command == "scanner":
            result = scanner.run(args.chain, key=args.key, json_output=args.json_output)
            if result:
                print(json.dumps(result, indent=2))
        elif args.command == "calendar":
            result = calendar.run(key=args.key, json_output=args.json_output)
            if result:
                print(json.dumps(result, indent=2))
        elif args.command == "keys":
            if args.json_output:
                print(json.dumps({"action": "get_api_key", "url": "https://signal-bot.ai/contact"}))
            else:
                print("🔑 Get your free API key → https://signal-bot.ai/contact")
    except SignalBotError as e:
        if args.json_output:
            print(json.dumps({"error": str(e)}), file=sys.stderr)
            sys.exit(1)
        raise SystemExit(str(e))
    except SystemExit:
        raise
    except Exception as e:
        if args.json_output:
            print(json.dumps({"error": str(e)}), file=sys.stderr)
            sys.exit(1)
        raise SystemExit(f"❌ {e}")


if __name__ == "__main__":
    main()
