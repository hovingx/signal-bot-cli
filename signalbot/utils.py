"""Formatting utilities — price, market cap, table output."""

from tabulate import tabulate


def fmt_price(p, decimals: int = 2) -> str:
    """Human-readable price formatting."""
    if not isinstance(p, (int, float)):
        return str(p)
    if abs(p) >= 1e6:
        return f"${p / 1e6:.{decimals}f}M"
    if abs(p) >= 1e3:
        return f"${p / 1e3:.{decimals}f}K"
    if p < 0.0001:
        return f"{p:.2e}"
    if p < 1:
        return f"{p:.6f}"
    return f"{p:.4f}"


def print_table(rows: list[list[str]], headers: list[str], footer: str = "") -> None:
    """Print a formatted table with footer line."""
    print(tabulate(rows, headers=headers, tablefmt="simple_outline"))
    if footer:
        print(f"\n{footer}")


IMPACT_ICON = {"high": "🔴", "medium": "🟡", "low": "⚪"}
