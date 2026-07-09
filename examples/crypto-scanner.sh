#!/bin/bash
# signal-bot.ai CLI — Memecoin Scanner Example
#
# Usage:
#   chmod +x examples/crypto-scanner.sh
#   ./examples/crypto-scanner.sh
#
# Or directly:
#   signal-bot scanner sol

set -euo pipefail

CHAIN="${1:-sol}"

echo "🔥 Memecoin Scanner — ${CHAIN^^}"
echo "==============================="
echo ""

signal-bot scanner "$CHAIN"

echo ""
echo "Available chains: sol, bsc, base, eth, robinhood"
