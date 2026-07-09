#!/bin/bash
# signal-bot.ai CLI — Economic Calendar Example
#
# Usage:
#   chmod +x examples/calendar.sh
#   ./examples/calendar.sh
#
# Or directly:
#   signal-bot calendar

set -euo pipefail

echo "📅 Forex Economic Calendar"
echo "=========================="
echo ""

signal-bot calendar

echo ""
echo "High-impact events are marked with 🔴"
