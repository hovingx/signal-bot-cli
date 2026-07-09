"""Trading signals command."""

from signalbot.api import get, SignalBotError
from signalbot.utils import fmt_price, print_table

VALID_MARKETS = ("forex", "crypto", "stocks", "binary")


def run(market: str, key: str | None = None, json_output: bool = False) -> dict | None:
    """Fetch and display trading signals. Returns dict when json_output=True."""
    if market not in VALID_MARKETS:
        msg = f"❌ Unknown market: {market}. Valid: {', '.join(VALID_MARKETS)}"
        if json_output:
            return {"error": msg}
        raise SignalBotError(msg)

    data = get(f"signals/{market}", key=key)
    signals_list = data.get("signals", [])

    if json_output:
        return data

    rows = []
    for s in signals_list:
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
    return None
