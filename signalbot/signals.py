"""Trading signals command."""

from signalbot.api import get
from signalbot.utils import fmt_price, print_table

VALID_MARKETS = ("forex", "crypto", "stocks", "binary")


def run(market: str, key: str | None = None) -> None:
    """Fetch and display trading signals."""
    if market not in VALID_MARKETS:
        raise SystemExit(f"❌ Unknown market: {market}. Valid: {', '.join(VALID_MARKETS)}")

    data = get(f"signals/{market}", key=key)
    signals = data.get("signals", [])

    rows = []
    for s in signals:
        pair = s.get("pair") or s.get("ticker") or s.get("asset") or "—"
        direction = s.get("direction") or s.get("signal") or "—"
        rows.append([
            pair,
            fmt_price(s.get("price", 0)),
            direction,
            f"{s['confidence']}%",
            fmt_price(s.get("sl", 0)),
            fmt_price(s.get("tp", 0)),
        ])

    print_table(rows, ["Pair", "Price", "Dir", "Conf", "SL", "TP"], f"{len(rows)} signals")
