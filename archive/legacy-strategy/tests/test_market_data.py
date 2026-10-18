from pathlib import Path

from tc_trade_strategy.market_data import load_symbols, to_yahoo_symbol


def test_load_symbols_preserves_order_and_removes_duplicates(tmp_path: Path) -> None:
    path = tmp_path / "symbols.txt"
    path.write_text("aapl\n\n# comment\nSPY\nAAPL\n", encoding="utf-8")

    assert load_symbols(path) == ["AAPL", "SPY"]


def test_special_yahoo_symbol_mapping() -> None:
    assert to_yahoo_symbol("BRK.B") == "BRK-B"
    assert to_yahoo_symbol(".VVIX") == "^VVIX"
    assert to_yahoo_symbol(".KOSPI") == "^KS11"
    assert to_yahoo_symbol("SQ") == "XYZ"
    assert to_yahoo_symbol("XAUUSD") == "GC=F"
    assert to_yahoo_symbol("AAPL") == "AAPL"
