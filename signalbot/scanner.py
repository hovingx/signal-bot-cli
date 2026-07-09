"""Memecoin scanner command."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from signalbot.api import get, get_key
from signalbot.utils import fmt_price, print_table

CHAINS = ("sol", "bsc", "base", "eth", "robinhood")


def run(chain: str = "sol", key: str | None = None) -> None:
    """Fetch and display memecoin scanner results."""
    key = get_key(key)

    # Fetch all chains concurrently
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures = {ex.submit(get, "scanner/memecoin", {"chain": ch}, key): ch for ch in CHAINS}
        for future in as_completed(futures):
            try:
                data = future.result()
                results.extend(data.get("signals", []))
            except SystemExit:
                raise
            except Exception:
                pass  # one chain down shouldn't kill the whole command

    results.sort(key=lambda s: s.get("score", 0), reverse=True)

    rows = []
    for s in results:
        sm = s.get("smart_money", {})
        rows.append([
            s.get("chain", "—").upper(),
            s["symbol"],
            fmt_price(s.get("mcap", 0)),
            f"{s['score']:.1f}",
            s["signal"],
            f"smart:{sm.get('smart_degen', 0)} snipers:{sm.get('snipers', 0)}",
        ])

    high = sum(1 for s in results if s["signal"] == "HIGH_CONVICTION")
    print_table(rows, ["Chain", "Symbol", "MCap", "Score", "Signal", "Smart Money"],
                f"{len(rows)} tokens · {high} HIGH_CONVICTION")
