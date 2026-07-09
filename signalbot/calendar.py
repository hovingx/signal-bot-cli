"""Economic calendar command."""

from signalbot.api import get
from signalbot.utils import print_table, IMPACT_ICON


def run(key: str | None = None, json_output: bool = False) -> dict | None:
    """Fetch and display forex economic calendar. Returns dict when json_output=True."""
    data = get("calendar/forex", key=key)
    events = data.get("events", [])

    if json_output:
        return data

    rows = []
    for e in events:
        rows.append([
            e["time"][:16].replace("T", " "),
            e["country"],
            IMPACT_ICON.get(e["impact"], "—"),
            e["event"],
            e.get("actual", "—"),
            e.get("forecast", "—"),
            e.get("previous", "—"),
        ])

    high = sum(1 for e in events if e["impact"] == "high")
    print_table(rows, ["Time", "Country", "Imp", "Event", "Actual", "Forecast", "Previous"],
                f"{len(events)} events · {high} high-impact")
    return None
